#!/usr/bin/env python3
"""Lectura de una jornada con la estrategia del usuario (15-nov-2026):
cuota >= 1,40 (objetivo 1,50), regularidad >= 7 de 10 en lo que mide la línea, colchón > 0, todos los mercados;
combinadas de cuota >= 3 sin tope de patas. Las combinadas se declaran en <jornada>/estrategia_combos.json
(las escoge Claude: una historia coherente por combinada); las cifras salen siempre de registro/lineas.csv.
Uso: python3 recoleccion/estrategia_usuario.py jornadas/AAAA-MM-DD [HHMM]
Escribe <jornada>/reanalisis_<HHMM>_estrategia.md (tarjeta en la pestaña «Análisis» del informe) y estrategia.json (para calificar)."""
import csv, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMIN, CMAX, MARGEN = 1.40, 2.20, 1.06
NOM = {'corners': 'Córners', 'goles': 'Goles', 'tarjetas': 'Tarjetas', 'remates': 'Remates', 'al_arco': 'Tiros al arco', 'faltas': 'Faltas',
       'fueras': 'Fueras de juego', 'saques_banda': 'Saques de banda', 'saques_meta': 'Saques de meta'}


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def texto(r):
    m = r['mercado']
    if r['jugador']:
        return f"{r['jugador']} · {NOM.get(m.split(':')[1], m.split(':')[1]).lower()} {r['lado']} {r['linea']}".replace('Más 1', '1 o más').replace('Más 2', '2 o más').replace('Más 3', '3 o más')
    eq = {'total': '', 'local': ' ' + r['partido'].split(' - ')[0], 'visitante': ' ' + r['partido'].split(' - ')[1]}.get(r['ambito'], ' ' + r['ambito'])
    return f"{NOM.get(m, m)}{eq} {r['lado']} {r['linea']}"


def prob(r):
    p = f(r['p_modelo'])
    return (p, '') if p is not None else (1 / f(r['cuota']) / MARGEN, '≈')


def main(a):
    base = a[1].rstrip('/'); jor = os.path.basename(base); hhmm = a[2] if len(a) > 2 else '0000'
    filas = [r for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';') if r['jornada'] == jor]
    S = []
    for r in filas:
        c, col = f(r['cuota']), f(r['colchon'])
        if c is None or not CMIN <= c <= CMAX or r['cumple_ficha'] != 'sí': continue
        if r['jugador'] and (f(r['titular']) or 0) < 0.7: continue          # jugador fuera del XI probable
        if col is not None and col <= 0: continue
        p, ap = prob(r)
        S.append(dict(r, _c=c, _p=p, _ap=ap, _t=texto(r), _reg=' · '.join(x for x in (r['reg_local'], r['reg_visitante']) if x)))
    S.sort(key=lambda r: (r['hora_partido'], r['partido'], -r['_p']))
    idx = {(r['partido'], r['mercado'], r['ambito'], r['jugador'], r['lado'], r['linea']): r for r in S}

    out = [f'# Tu estrategia aplicada a la jornada ({len(S)} líneas, combinadas de cuota ≥ 3)', '',
           f'**Filtro:** cuota {CMIN:.2f}–{CMAX:.2f}, regularidad ≥ 7 de 10 en ambos equipos (o en el jugador, titular probable), colchón > 0, todos los mercados. '
           '**p** = probabilidad del modelo (≈ = solo la cuota sin margen: partido sin modelo). El modelo queda casi igual al precio de Betano: '
           'ninguna línea tiene ventaja probada, y una combinada pierde ~5 % por cada pata que se le suma.', '']
    cj = os.path.join(base, 'estrategia_combos.json'); combos = json.load(open(cj, encoding='utf8')) if os.path.exists(cj) else []
    reg = []
    if combos:
        out += ['**Combinadas**', '', '| # | Tipo | Patas | Cuota | p | Nota |', '|---|---|---|---|---|---|']
        for i, cb in enumerate(combos, 1):
            patas = []
            for k in cb['patas']:
                r = idx.get(tuple(k))
                if r is None: sys.exit(f'combinada {i}: pata fuera del filtro o inexistente: {k}')
                patas.append(r)
            cu = 1; p = 1
            for r in patas: cu *= r['_c']; p *= r['_p']
            mismo = len({r['partido'] for r in patas}) == 1
            out.append(f"| {i} | {'mismo partido' if mismo else 'varios partidos'} | " + ' + '.join(f"{r['_t']} @{r['_c']:.2f} ({r['partido'].split(' - ')[0] if not mismo else r['_reg']})" for r in patas)
                       + f" | {'~' if mismo else ''}{cu:.2f} | {'~' if mismo else ''}{p*100:.0f} % | {cb.get('nota', '')} |")
            reg.append({'n': i, 'mismo_partido': mismo, 'cuota_producto': round(cu, 2), 'p_producto': round(p, 4), 'nota': cb.get('nota', ''),
                        'patas': [{'partido': r['partido'], 'texto': r['_t'], 'mercado': r['mercado'], 'ambito': r['ambito'], 'jugador': r['jugador'], 'lado': r['lado'],
                                   'linea': r['linea'], 'cuota': r['_c'], 'p': round(r['_p'], 4)} for r in patas]})
        out += ['', 'En «varios partidos» la cuota es el producto exacto. En «mismo partido» Betano recalcula el precio (las patas van juntas): la cuota y la p con ~ son solo el producto; mira el precio real en el cupón.', '']
    out += ['**Sencillas que pasan el filtro**', '', '| Hora | Partido | Línea | Cuota | p | Regularidad (local · visit.) | Directos | Esperado | Colchón |', '|---|---|---|---|---|---|---|---|---|']
    for r in S:
        out.append(f"| {r['hora_partido'][11:]} | {r['partido']} | {r['_t']} | {r['_c']:.2f} | {r['_ap']}{r['_p']*100:.0f} % | {r['_reg']} | {r['directos'] or '–'} | {r['esperado'] or '–'} | {r['colchon'] or '–'} |")
    out += ['', '**Límites:** cuotas de Betano leídas el 14-nov 19:55 Bogotá (pueden haber cambiado); tarjetas: Betano cuenta puntos (roja = 2) y el historial solo amarillas, '
            'así que «Menos tarjetas» es más frágil de lo que muestra la regularidad; Chipre–Montenegro sin alineación (solo líneas de equipo); sin lectura de árbitro, clima ni situación de tabla.']
    open(os.path.join(base, f'reanalisis_{hhmm}_estrategia.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
    json.dump({'jornada': jor, 'filtro': {'cuota': [CMIN, CMAX], 'cumple': '>=7 de 10', 'colchon': '>0'}, 'combinadas': reg,
               'sencillas': [{'partido': r['partido'], 'texto': r['_t'], 'mercado': r['mercado'], 'ambito': r['ambito'], 'jugador': r['jugador'], 'lado': r['lado'],
                              'linea': r['linea'], 'cuota': r['_c'], 'p': round(r['_p'], 4)} for r in S]},
              open(os.path.join(base, 'estrategia.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(len(S), 'sencillas,', len(reg), 'combinadas')
    for x in reg: print(x['n'], 'mismo' if x['mismo_partido'] else 'varios', x['cuota_producto'], x['p_producto'])


if __name__ == '__main__':
    main(sys.argv)
