# -*- coding: utf-8 -*-
"""Análisis de una jornada con lo aprendido en la auditoría de sugerencias (4–13 nov-2026). Corre sin navegador, después de correr_jornada.py.

    python3 recoleccion/analisis_jornada.py jornadas/2026-11-14 [--sin-combos]

Lee     registro/lineas.csv (líneas de la jornada + las ya calificadas de otros días), registro/sugerencias.csv (auditoría),
        <jornada>/ranking.json, <jornada>/informes/*_resultado.json, <jornada>/fichas/ficha_*.json, <jornada>/entradas/*.json
Escribe <jornada>/analisis.json   (lo muestra informe_html.py en la pestaña «Análisis»; el «Enfoque de mercados» lo escribe Claude en <jornada>/enfoque.md)
        <jornada>/informe_final.md (el mismo análisis en texto)
        <jornada>/sugerencias.json (lo lee sugerencias.py para calificar cada sugerencia después, pata por pata)

Reglas (todas vienen de la auditoría; las constantes están abajo, único lugar donde cambiarlas):
  · «Real hasta hoy»: junto a cada p se muestra lo que de verdad se dio en las líneas ya calificadas (por mercado y lado, y por banda de cuota).
  · p recortada = p del modelo × el menor de dos factores reales (mercado-lado y banda de cuota), nunca mayor que la p del modelo.
    Cada factor = aciertos / esperados en las líneas con «cumple» ya calificadas, suavizado hacia el factor global con M líneas ficticias
    (con pocas líneas calificadas manda el global).
  · Sencillas: cuota < 1,50 = «protección» (se dan, no pagan); 1,50–1,99 = «sencilla» con la p recortada a la vista.
  · Combinadas del mismo partido: máximo 2 patas, cada una con p recortada ≥ 70 %; la p conjunta sale de la simulación del modelo
    (combos.evaluar) y se recorta RECORTE_COMBO; no se usan patas de una familia en la que la simulación se aleja del mercado en ese
    partido (alerta del modelo: «más córners que» cuenta como córners); remates y tiros al arco cuentan como la misma familia;
    cada patrón (p. ej. «córners Más + goles Menos») máximo una vez por día. La cuota es el producto de las cuotas (techo: el cupón de Betano puede pagar menos).
  · 3 o más patas: solo «lotería» de stake mínimo (una, entre partidos distintos).
  · Tarjetas: sin estadísticas de árbitro y con la peor calibración, no entran en sugerencias (quedan en las tablas del informe).
  · Jugadores: solo con alineación y con historial; sin historial no hay sugerencia (regla 1 de CLAUDE.md).
No apuesta, no lee la red, no inventa: lo que falta se declara.
"""
import csv, datetime, glob, itertools, json, math, os, sys
from collections import defaultdict
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
sys.path.insert(0, RAIZ)
import ficha as FI

P_MIN = 0.70            # p recortada mínima de una «protección» y de cada pata de combinada
P_MIN_SENCILLA = 0.55   # p recortada mínima de una sencilla de cuota 1,50–1,99
CUOTA_MIN = 1.20        # por debajo no se sugiere (no paga)
CUOTA_PROTECCION = 1.50
CUOTA_SENCILLA_MAX = 2.00
RECORTE_COMBO = 0.20    # la auditoría pide 15–20 %: se usa el extremo prudente
M_SUAVIZADO = 20        # líneas ficticias con las que cada factor se acerca al factor global
MAX_COMBOS = 8
SIN_SUGERENCIA = ('tarjetas',)
MISMA_HISTORIA = {'remates': 'tiros', 'al_arco': 'tiros'}
AMBITOS = ('total', 'local', 'visitante')
NOMBRE = {'corners': 'Córners', 'goles': 'Goles', 'tarjetas': 'Tarjetas', 'al_arco': 'Tiros al arco', 'remates': 'Remates', 'faltas': 'Faltas',
          'fueras': 'Fueras de juego', 'saques_meta': 'Saques de meta', 'saques_banda': 'Saques de banda'}
BANDAS = [(0, 1.30, 'cuota < 1,30'), (1.30, 1.50, 'cuota 1,30–1,49'), (1.50, 2.00, 'cuota 1,50–1,99'), (2.00, 99, 'cuota ≥ 2,00')]


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def banda(c):
    for a, b, t in BANDAS:
        if a <= c < b:
            return t
    return BANDAS[-1][2]


def es_equipo(r):
    return not r['mercado'].startswith('jugador')


# ---------------------------------------------------------------------------------------------- «real hasta hoy»
def _grupo(filas):
    n = len(filas)
    ac = sum(1 for r in filas if r['resultado'] == 'cumplió')
    esp = sum(num(r['p_modelo']) or 0 for r in filas)
    return {'n': n, 'aciertos': ac, 'real': round(ac / n, 4) if n else None, 'dicho': round(esp / n, 4) if n else None, 'esperados': round(esp, 2)}


def real_hasta_hoy(hist, sug):
    """hist: líneas de equipo ya calificadas (cumplió/falló) con p del modelo; sug: filas de registro/sugerencias.csv."""
    H = [r for r in hist if es_equipo(r) and r['resultado'] in ('cumplió', 'falló') and num(r['p_modelo']) is not None and num(r['cuota'])]
    C = [r for r in H if r['cumple_ficha'] == 'sí']
    g = _grupo(C)
    fg = min(1.0, g['aciertos'] / g['esperados']) if g['esperados'] else 1.0

    def factor(gr):
        return round(min(1.0, (gr['aciertos'] + M_SUAVIZADO * fg * (gr['dicho'] or 0)) / (gr['esperados'] + M_SUAVIZADO * (gr['dicho'] or 0))), 4) if gr['n'] else round(fg, 4)

    ml = defaultdict(list)
    for r in C:
        ml[(r['mercado'], r['lado'])].append(r)
    bc = defaultdict(list)
    for r in C:
        bc[banda(num(r['cuota']))].append(r)
    bp = defaultdict(list)
    for r in H:
        p = num(r['p_modelo'])
        if p >= 0.5:
            bp[min(9, int(p * 10))].append(r)
    out = {'partidos': len({(r['jornada'], r['partido']) for r in H}), 'lineas': len(H), 'global_cumple': {**g, 'factor': round(fg, 4)},
           'mercado_lado': {f'{m}|{l}': {**_grupo(v), 'factor': factor(_grupo(v))} for (m, l), v in sorted(ml.items())},
           'banda_cuota': {t: {**_grupo(bc[t]), 'factor': factor(_grupo(bc[t]))} for _, _, t in BANDAS if t in bc},
           'banda_p': {f'{k * 10}–{k * 10 + 10} %': _grupo(v) for k, v in sorted(bp.items())}}
    # auditoría de sugerencias (sencillas por banda de cuota; combinadas por número de patas)
    def tasa(fs):
        fs = [s for s in fs if s['resultado'] in ('cumplió', 'falló')]
        ps = [num(s['p_estimada']) for s in fs if num(s['p_estimada']) is not None]
        return {'n': len(fs), 'aciertos': sum(1 for s in fs if s['resultado'] == 'cumplió'),
                'real': round(sum(1 for s in fs if s['resultado'] == 'cumplió') / len(fs), 4) if fs else None,
                'dicho': round(sum(ps) / len(ps), 4) if ps else None}
    sen = [s for s in sug if int(s['n_patas'] or 0) == 1]
    com = [s for s in sug if int(s['n_patas'] or 0) >= 2]
    mismo = [s for s in com if 'mismo partido' in s['tipo'] and 'vivo' not in s['tipo']]
    out['sugerencias'] = {
        'sencillas': tasa(sen),
        'sencillas cuota < 1,50': tasa([s for s in sen if (num(s['cuota']) or 0) and num(s['cuota']) < 1.5]),
        'sencillas cuota 1,50–1,99': tasa([s for s in sen if num(s['cuota']) and 1.5 <= num(s['cuota']) < 2]),
        'sencillas cuota ≥ 2,00': tasa([s for s in sen if num(s['cuota']) and num(s['cuota']) >= 2]),
        'combinadas del mismo partido': tasa(mismo),
        'combinadas de 2 patas (todas)': tasa([s for s in com if int(s['n_patas']) == 2]),
        'combinadas de 3 patas (todas)': tasa([s for s in com if int(s['n_patas']) == 3]),
        'combinadas de 4 o más patas (todas)': tasa([s for s in com if int(s['n_patas']) >= 4]),
    }
    return out


def recorte(REAL, mercado, lado, cuota):
    """(factor, texto «real hasta hoy») de una línea de equipo."""
    a = REAL['mercado_lado'].get(f'{mercado}|{lado}')
    b = REAL['banda_cuota'].get(banda(cuota))
    g = REAL['global_cumple']
    fa = a['factor'] if a else g['factor']
    fb = b['factor'] if b else g['factor']
    t = []
    if a:
        t.append(f"{NOMBRE.get(mercado, mercado)} {lado} con «cumple»: {a['aciertos']} de {a['n']} ({a['real']:.0%} real contra {a['dicho']:.0%} dicho)")
    else:
        t.append(f"{NOMBRE.get(mercado, mercado)} {lado} con «cumple»: sin líneas calificadas todavía (se usa el global: {g['real']:.0%} real contra {g['dicho']:.0%} dicho)")
    if b:
        t.append(f"{banda(cuota)}: {b['aciertos']} de {b['n']} ({b['real']:.0%} real contra {b['dicho']:.0%})")
    return min(fa, fb, 1.0), ' · '.join(t)


# ---------------------------------------------------------------------------------------------- líneas de la jornada
def texto(r):
    amb = '' if r['ambito'] == 'total' else (' ' + r['ambito'])
    return f"{NOMBRE.get(r['mercado'], r['mercado'])}{amb} {r['lado']} {r['linea']}"


def clave(r):
    return [r['partido'], r['mercado'], r['ambito'], r['linea'], r['lado']]


def candidatas(J, REAL):
    """Líneas de equipo con «cumple» (ámbito de partido completo), con su p recortada y su «real hasta hoy»."""
    out = []
    for r in J:
        if not es_equipo(r) or r['cumple_ficha'] != 'sí' or r['ambito'] not in AMBITOS:
            continue
        p, c = num(r['p_modelo']), num(r['cuota'])
        if p is None or not c:
            continue
        f, real = recorte(REAL, r['mercado'], r['lado'], c)
        d = r['directos'].split(' de ') if ' de ' in (r['directos'] or '') else None
        if d and int(d[1]) >= 3 and int(d[0]) * 3 <= int(d[1]):          # los directos dicen lo contrario (solo aviso; no excluye)
            real = f"⚠ directos en contra ({r['directos']}) · " + real
        out.append({'partido': r['partido'], 'hora': r['hora_partido'], 'mercado': r['mercado'], 'ambito': r['ambito'], 'linea': num(r['linea']), 'lado': r['lado'],
                    'texto': texto(r), 'cuota': c, 'p': round(p, 4), 'p_rec': round(p * f, 4), 'factor': round(f, 3), 'real': real,
                    'p_mercado': num(r['p_mercado']), 'ev': num(r['ev_modelo']), 'esperado': num(r['esperado']), 'colchon': num(r['colchon']),
                    'L': r['reg_local'], 'V': r['reg_visitante'], 'D': r['directos'], 'alerta': bool(r['alerta_modelo']), 'clave': clave(r)})
    return out


def mejor_escalon(cands, ok):
    """De cada escalera (partido, mercado, ámbito, lado) deja UNA línea: la de mayor cuota que pasa el filtro."""
    best = {}
    for c in cands:
        if not ok(c):
            continue
        k = (c['partido'], c['mercado'], c['ambito'], c['lado'])
        if k not in best or c['cuota'] > best[k]['cuota']:
            best[k] = c
    return sorted(best.values(), key=lambda c: (-c['p_rec'], c['hora']))


def sencillas(cands):
    apta = lambda c: c['mercado'] not in SIN_SUGERENCIA and c['cuota'] >= CUOTA_MIN and not c['alerta']
    prot = mejor_escalon(cands, lambda c: apta(c) and c['cuota'] < CUOTA_PROTECCION and c['p_rec'] >= P_MIN)
    sen = mejor_escalon(cands, lambda c: apta(c) and CUOTA_PROTECCION <= c['cuota'] < CUOTA_SENCILLA_MAX and c['p_rec'] >= P_MIN_SENCILLA)
    return prot, sen


# ---------------------------------------------------------------------------------------------- combinadas (simulación del modelo)
def _slug_por_partido(base):
    out = {}
    for p in glob.glob(os.path.join(base, 'entradas', '*.json')):
        try:
            e = json.load(open(p, encoding='utf8'))
        except ValueError:
            continue
        if isinstance(e, dict) and e.get('local'):
            out[f"{e['local']} - {e['visitante']}"] = p
    return out


def combinadas(base, prot, alertas_partido):
    """Pares del mismo partido con patas de familias distintas (p recortada ≥ P_MIN cada una); p conjunta = simulación ajustada × (1 − recorte)."""
    from supermodelo.analizar import analizar
    from supermodelo import combos as CB
    rutas = _slug_por_partido(base)
    por = defaultdict(list)
    for c in prot:
        por[c['partido']].append(c)
    out, saltados = [], []
    for partido, patas in sorted(por.items()):
        fuera = alertas_partido.get(partido) or []
        if any(x['mercado'] in fuera for x in patas):
            saltados.append(f"{partido} (sin patas de {', '.join(NOMBRE.get(m, m).lower() for m in fuera)})")
        patas = [x for x in patas if x['mercado'] not in fuera]
        fam = lambda x: MISMA_HISTORIA.get(x['mercado'], x['mercado'])   # tiros al arco es parte de remates: no son dos eventos
        pares = [(a, b) for a, b in itertools.combinations(patas, 2) if fam(a) != fam(b)]
        if not pares or partido not in rutas:
            continue
        A = analizar(json.load(open(rutas[partido], encoding='utf8')), devolver_sim=True)
        S = A.pop('_S')
        mejores = []
        for a, b in pares:
            sel = [{'mercado': x['mercado'], 'ambito': x['ambito'], 'linea': x['linea'], 'lado': 'mas' if x['lado'] == 'Más' else 'menos'} for x in (a, b)]
            r = CB.evaluar(A, S, sel)
            if r.get('error'):
                continue
            p_final = r['p_ajust'] * (1 - RECORTE_COMBO)                  # regla de la auditoría: conjunta de la simulación, recortada
            mejores.append({'partido': partido, 'hora': a['hora'], 'patas': [a, b], 'texto': f"{a['texto']} + {b['texto']}",
                            'cuota': round(a['cuota'] * b['cuota'], 2), 'p_sim': r['p_sim'], 'p_ajust': r['p_ajust'],
                            'p_rec': round(p_final, 4), 'correlacion': r.get('correlacion'), 'guion': r.get('guion_comun'),
                            'fragil': r.get('pata_mas_fragil'), 'patron': ' + '.join(sorted(f"{x['mercado']} {x['lado']}" for x in (a, b)))})
        mejores.sort(key=lambda c: -c['p_rec'] * c['cuota'])              # dentro del partido: la de mejor relación p × cuota (informativo)
        out += mejores[:1]
    out.sort(key=lambda c: -c['p_rec'])
    final, usados = [], defaultdict(int)
    for c in out:
        if usados[c['patron']] >= 1:                                       # auditoría: el mismo patrón en varios partidos es una sola apuesta repetida
            continue
        usados[c['patron']] += 1
        final.append(c)
    return final[:MAX_COMBOS], saltados


def loteria(prot):
    """Una sola: tres «protecciones» de tres partidos distintos (independientes), las de mayor p recortada con cuota ≥ 1,25."""
    vistos, patas = set(), []
    for c in prot:
        if c['cuota'] >= 1.25 and c['partido'] not in vistos:
            vistos.add(c['partido'])
            patas.append(c)
        if len(patas) == 3:
            break
    if len(patas) < 3:
        return None
    return {'patas': patas, 'texto': ' + '.join(f"{c['partido']}: {c['texto']}" for c in patas), 'cuota': round(math.prod(c['cuota'] for c in patas), 2),
            'p': round(math.prod(c['p'] for c in patas), 4), 'p_rec': round(math.prod(c['p_rec'] for c in patas), 4)}


# ---------------------------------------------------------------------------------------------- situación por partido
def partidos(base, J, cands):
    rk = {}
    p = os.path.join(base, 'ranking.json')
    if os.path.exists(p):
        rk = {r['partido']: r for r in json.load(open(p, encoding='utf8'))}
    inf = {}
    for f in glob.glob(os.path.join(base, 'informes', '*_resultado.json')):
        d = json.load(open(f, encoding='utf8'))
        inf[d.get('partido') or ''] = d
    fic = {}
    for f in glob.glob(os.path.join(base, 'fichas', 'ficha_*.json')):
        d = json.load(open(f, encoding='utf8'))
        fic[d['encuentro']] = d
    orden = sorted({(r['hora_partido'], r['partido']) for r in J})
    out = []
    for hora, n in orden:
        F, R, I = fic.get(n, {}), rk.get(n, {}), inf.get(n) or next((v for k, v in inf.items() if k.replace('–', '-').replace(' vs ', ' - ') == n), {})
        c = F.get('contexto') or {}
        js = [r for r in J if r['partido'] == n and not es_equipo(r)]
        con_xi = sum(1 for r in js if r['cumple_ficha'] != 'sin alineación')
        cs = [x for x in cands if x['partido'] == n]
        pr = I.get('p_resultado') or {}
        out.append({'n': n, 'hora': hora, 'liga': next(r['liga'] for r in J if r['partido'] == n), 'estado': R.get('estado'), 'datos': R.get('datos'),
                    'p1': pr.get('local'), 'px': pr.get('empate'), 'p2': pr.get('visitante'),
                    'alertas': I.get('alertas') or [], 'enfoque': I.get('enfoque_resumen') or '',
                    'familias_alerta': sorted({'corners' if l['sel'].get('mercado') == 'mas_que' else l['sel'].get('mercado') for l in I.get('lineas', []) if l.get('alerta')}),
                    'tabla': FI._tabla_txt(c.get('tabla')) if c.get('tabla') else 'sin tabla', 'clima': c.get('clima') or 'sin dato',
                    'arbitro': c.get('arbitro') or 'sin publicar', 'bajas': c.get('bajas') or [], 'dudas': c.get('dudas') or [],
                    'xi': 'probable' if con_xi else 'sin alineación', 'lineas_jugador': len(js),
                    'cumplen': len(cs), 'cumplen_por_mercado': {m: sum(1 for x in cs if x['mercado'] == m) for m in sorted({x['mercado'] for x in cs})}})
    return out


# ---------------------------------------------------------------------------------------------- informe_final.md (texto; el interactivo es informe.html)
def informe_md(base, A):
    pc = lambda x: '–' if x is None else f'{100 * x:.0f} %'
    q = lambda x: f'{x:.2f}'.replace('.', ',')
    hora = lambda c: c['hora'][11:16]

    def bog(z):                                                           # 2026-11-14T00:01:43.364Z -> 13-nov 19:01 (Bogotá)
        try:
            t = datetime.datetime.fromisoformat(z.replace('Z', '+00:00')).astimezone(datetime.timezone(datetime.timedelta(hours=-5)))
            return f"{t.day}-{('ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic')[t.month - 1]} {t:%H:%M}"
        except ValueError:
            return z
    L = [f"# Informe de la jornada {A['jornada']}", '',
         f"Hecho: {A['hecho']} (Bogotá) · Cuotas: Betano, leídas {' a '.join(bog(z) for z in A['cuotas_leidas'])} (Bogotá), sin releer · Muestra de {A['muestra']} partidos por equipo: "
         f"«cumple» = {A['cumple']} de {A['muestra']} en ambos (n mínimo {A['n_minimo']}) · {A['n_cumplen']} líneas de equipo cumplen. El informe interactivo es `informe.html`.", '',
         '## Enfoque de mercados', '']
    e = os.path.join(base, 'enfoque.md')
    L += [open(e, encoding='utf8').read().strip() if os.path.exists(e) else '_Sin enfoque.md: falta la lectura de Claude sobre qué mercados pesan en esta jornada._', '']
    R = A['real']
    L += ['## Real hasta hoy', '', '| Grupo | n | Se dieron | Real | Dicho | Recorte de p |', '|---|---|---|---|---|---|']
    for k, v in R['mercado_lado'].items():
        m, l = k.split('|')
        L.append(f"| {NOMBRE.get(m, m)} {l} (con «cumple») | {v['n']} | {v['aciertos']} | {pc(v['real'])} | {pc(v['dicho'])} | × {q(v['factor'])} |")
    for k, v in R['banda_cuota'].items():
        L.append(f"| {k} (con «cumple») | {v['n']} | {v['aciertos']} | {pc(v['real'])} | {pc(v['dicho'])} | × {q(v['factor'])} |")
    for k, v in R['sugerencias'].items():
        L.append(f"| Sugerencias auditadas: {k} | {v['n']} | {v['aciertos']} | {pc(v['real'])} | {pc(v['dicho'])} | |")
    cab = ['| Hora | Partido | Sugerencia | Cuota | p modelo | p recortada | Local | Visitante | Directos | Real hasta hoy |', '|---|---|---|---|---|---|---|---|---|---|']
    fila = lambda c: f"| {hora(c)} | {c['partido']} | {c['texto']} | {q(c['cuota'])} | {pc(c['p'])} | {pc(c['p_rec'])} | {c['L']} | {c['V']} | {c['D'] or '–'} | {c['real']} |"
    L += ['', f"## Protección (cuota < {q(CUOTA_PROTECCION)}: se dan, no pagan) — {len(A['proteccion'])}", ''] + cab + [fila(c) for c in A['proteccion']]
    L += ['', f"## Sencillas de cuota 1,50–1,99 (p recortada a la vista) — {len(A['sencillas'])}", ''] + cab + [fila(c) for c in A['sencillas']]
    L += ['', f"## Combinadas de 2 patas del mismo partido — {len(A['combinadas'])}", '',
          f"Cada pata con p recortada ≥ {pc(P_MIN)}; la conjunta sale de la simulación y se recorta {pc(RECORTE_COMBO)}; la cuota es el producto de las cuotas (techo).", '',
          '| Hora | Partido | Patas | Cuota (producto) | p simulación | p ajustada | p recortada | Pata más frágil |', '|---|---|---|---|---|---|---|---|']
    L += [f"| {hora(c)} | {c['partido']} | {c['texto']} | {q(c['cuota'])} | {pc(c['p_sim'])} | {pc(c['p_ajust'])} | {pc(c['p_rec'])} | {c.get('fragil') or '–'} |" for c in A['combinadas']]
    if A['combos_saltados_por_alerta']:
        L += ['', 'Familias fuera de las combinadas por alerta del modelo: ' + '; '.join(A['combos_saltados_por_alerta']) + '.']
    if A.get('loteria'):
        l = A['loteria']
        L += ['', '## Lotería (3 patas de 3 partidos; solo stake mínimo)', '', f"{l['texto']} · cuota {q(l['cuota'])} · p del modelo {pc(l['p'])} · p recortada {pc(l['p_rec'])}."]
    L += ['', '## Situación por partido (lo que hay en las fichas)', '', '| Hora | Partido | 1X2 del modelo | Tabla | Árbitro | XI | Cumplen | Alerta del modelo |', '|---|---|---|---|---|---|---|---|']
    for p in A['partidos']:
        L.append(f"| {p['hora'][11:16]} | {p['n']} | {pc(p['p1'])} · {pc(p['px'])} · {pc(p['p2'])} | {p['tabla']} | {p['arbitro']} | {p['xi']} | {p['cumplen']} | "
                 f"{', '.join(NOMBRE.get(m, m) for m in p['familias_alerta']) or '–'} |")
    L += ['', 'Límites y datos que faltan: ver `ESTADO.md` de la jornada. El detalle por mercado de los agentes está en `agentes/`.', '']
    open(os.path.join(base, 'informe_final.md'), 'w', encoding='utf8').write('\n'.join(L))


# ---------------------------------------------------------------------------------------------- principal
def main(argv):
    if not argv:
        print(__doc__)
        return 1
    base = argv[0].rstrip('/')
    jor = os.path.basename(base)
    L = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
    J = [r for r in L if r['jornada'] == jor]
    if not J:
        print(f'registro/lineas.csv no tiene filas de {jor}: corre antes recoleccion/correr_jornada.py {base}')
        return 2
    ps = os.path.join(RAIZ, 'registro', 'sugerencias.csv')
    S = [s for s in csv.DictReader(open(ps, encoding='utf-8-sig'), delimiter=';') if s['fecha_entrega'] < jor] if os.path.exists(ps) else []
    REAL = real_hasta_hoy([r for r in L if r['jornada'] < jor], S)
    cands = candidatas(J, REAL)
    prot, sen = sencillas(cands)
    P = partidos(base, J, cands)
    alertas = {p['n']: p['familias_alerta'] for p in P}
    com, saltados = ([], []) if '--sin-combos' in argv else combinadas(base, prot, alertas)
    lot = loteria(prot)
    nmax = max([int(x.split(' de ')[1]) for r in J for x in (r['reg_local'], r['reg_visitante']) if ' de ' in (x or '')] or [FI.N])
    k, mn = (FI.REGLA[2], FI.REGLA[1]) if nmax >= FI.REGLA[0] else (max(1, round(FI.REGLA[2] * nmax / FI.REGLA[0])), max(1, round(FI.REGLA[1] * nmax / FI.REGLA[0])))
    leidas = sorted({r['cuotas_leidas'] for r in J if r['cuotas_leidas']})
    ahora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5)))
    A = {'jornada': jor, 'hecho': ahora.strftime('%Y-%m-%d %H:%M'), 'muestra': nmax, 'cumple': k, 'n_minimo': mn, 'cuotas_leidas': [leidas[0], leidas[-1]] if leidas else [],
         'reglas': {'p_min': P_MIN, 'p_min_sencilla': P_MIN_SENCILLA, 'cuota_min': CUOTA_MIN, 'cuota_proteccion': CUOTA_PROTECCION,
                    'recorte_combo': RECORTE_COMBO, 'sin_sugerencia': list(SIN_SUGERENCIA)},
         'real': REAL, 'partidos': P, 'proteccion': prot, 'sencillas': sen, 'combinadas': com, 'combos_saltados_por_alerta': saltados, 'loteria': lot,
         'n_cumplen': len(cands), 'n_jugadores_con_historial': sum(1 for r in J if not es_equipo(r) and r['cumple_ficha'] in ('sí', 'no'))}
    json.dump(A, open(os.path.join(base, 'analisis.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    informe_md(base, A)
    # registro de sugerencias para calificarlas después (sugerencias.py las une con el resultado de registro/lineas.csv)
    pata = lambda c: {'partido': c['partido'], 'texto': c['texto'], 'cuota': c['cuota'], 'clave': c['clave']}
    SG = [{'tipo': 'sencilla', 'etiqueta': 'protección', 'nombre': c['texto'], 'partidos': c['partido'], 'cuota': c['cuota'], 'p': c['p_rec'], 'p_modelo': c['p'], 'patas': [pata(c)]} for c in prot]
    SG += [{'tipo': 'sencilla', 'etiqueta': 'sencilla 1,50–1,99', 'nombre': c['texto'], 'partidos': c['partido'], 'cuota': c['cuota'], 'p': c['p_rec'], 'p_modelo': c['p'], 'patas': [pata(c)]} for c in sen]
    SG += [{'tipo': 'combinada mismo partido', 'etiqueta': 'combinada de 2 patas', 'nombre': c['texto'], 'partidos': c['partido'], 'cuota': c['cuota'], 'p': c['p_rec'],
            'p_modelo': c['p_ajust'], 'patas': [pata(x) for x in c['patas']]} for c in com]
    if lot:
        SG.append({'tipo': 'combinada entre partidos', 'etiqueta': 'lotería (stake mínimo)', 'nombre': 'Lotería de 3 protecciones', 'partidos': ' | '.join(c['partido'] for c in lot['patas']),
                   'cuota': lot['cuota'], 'p': lot['p_rec'], 'p_modelo': lot['p'], 'patas': [pata(c) for c in lot['patas']]})
    json.dump({'jornada': jor, 'nota': 'Sugerencias del informe de la jornada; la cuota de las combinadas es el producto de las cuotas (techo).', 'sugerencias': SG},
              open(os.path.join(base, 'sugerencias.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(f"{base}/analisis.json: {len(cands)} líneas con «cumple» · {len(prot)} protecciones · {len(sen)} sencillas 1,50–1,99 · {len(com)} combinadas"
          f" ({len(saltados)} partidos con una familia fuera por alerta del modelo) · lotería {'sí' if lot else 'no'} · {len(SG)} sugerencias registradas")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
