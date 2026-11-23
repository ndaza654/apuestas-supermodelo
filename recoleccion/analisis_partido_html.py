#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Informe HTML interactivo de UN partido a fondo: BB Boost, contexto, ratings de rival, TODAS las líneas de equipo y de jugador
(crudo y ajustado por rival), historial de cada jugador. Autónomo (sin red). Lo ajustado por rival es informativo y SIN validar.
Uso: python3 recoleccion/analisis_partido_html.py jornadas/AAAA-MM-DD <clave> <datos_ligas/liga_fecha.json> [bb/combos_<clave>.json]
Salida: jornadas/AAAA-MM-DD/bb/analisis_<clave>.html"""
import csv, json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ajuste_rival as AR


def reunir(jor, clave, ratings, combos_json=None):
    dia = os.path.basename(jor.rstrip('/'))
    eq = AR.cargar(ratings)
    ent = json.load(open(f'{jor}/entradas/{clave}.json', encoding='utf8'))
    fs = json.load(open(f'{jor}/flashscore/{clave}.json', encoding='utf8'))
    L, V = fs['local'], fs['visitante']
    nombre_l, nombre_v = ent['local'], ent['visitante']
    ctx = json.load(open(f'{jor}/contexto/{clave}.json', encoding='utf8'))
    al = json.load(open(f'{jor}/alineaciones/{clave}.json', encoding='utf8')) if os.path.exists(f'{jor}/alineaciones/{clave}.json') else {}
    arb = json.load(open(f'{jor}/arbitros/{clave}.json', encoding='utf8')) if os.path.exists(f'{jor}/arbitros/{clave}.json') else {}
    adj = json.load(open(f'{jor}/ajustado/{clave}.json', encoding='utf8'))['filas']
    adjj = {(x['jugador'], x['mercado'], x['linea']): x for x in json.load(open(f'{jor}/ajustado/jugadores_{clave}.json', encoding='utf8'))['filas']}
    rows = [r for r in csv.DictReader(open('registro/lineas.csv', encoding='utf-8-sig'), delimiter=';') if r['jornada'] == dia and r['partido'].lower().startswith(nombre_l.lower()[:5])]
    jug = []
    for r in rows:
        if not r['mercado'].startswith('jugador:'):
            continue
        a = adjj.get((r['jugador'], r['mercado'], float(r['linea'])))
        x = n = None
        reg = r['reg_local'] or r['reg_visitante']
        if reg and ' de ' in reg:
            x, n = map(int, reg.split(' de '))
        p0 = float(r['p_mercado'] or 0)
        pm = (x + 6 * p0) / (n + 6) if n else None
        ax = an = pma = None
        if a:
            ax, an = map(int, a['ajustado'].split(' de '))
            pma = (ax + 6 * p0) / (an + 6) if an else None
        jug.append({'j': r['jugador'], 'eq': 'L' if r['ambito'] == 'local' else 'V', 'm': r['mercado'].split(':')[1], 'l': float(r['linea']), 'ld': r['lado'], 'c': float(r['cuota']),
                    'pm': p0, 'pmod': float(r['p_modelo'] or 0), 'x': x, 'n': n, 'pmz': None if pm is None else round(pm, 3), 'ax': ax, 'an': an, 'pmza': None if pma is None else round(pma, 3),
                    'esp': r['esperado'], 'col': r['colchon'], 'tit': r['titular'], 'cum': r['cumple_ficha'], 'media_aj': a and a['media_ajustada'], 'media': a and a['media_cruda']})
    hist = ent['ficha']['jugadores_hist']
    tit = {j['nombre']: j for j in ent['jugadores']}
    cards = []
    for nom, h in hist.items():
        lado = (tit.get(nom) or {}).get('lado') or next((x['eq'] for x in jug if x['j'] == nom), None)
        lado = {'local': 'L', 'visitante': 'V'}.get(lado, lado)
        cards.append({'j': nom, 'eq': lado, 'pos': h.get('pos'), 'tit': (tit.get(nom) or {}).get('titular'), 'fuera': bool((tit.get(nom) or {}).get('fuera')),
                      'p': [[p['fecha'], p.get('min'), p.get('remates'), p.get('al_arco'), p.get('goles'), p.get('asist'), p.get('tarjeta'), p.get('faltas'), p.get('entradas_tot'), p.get('atajadas')] for p in h['partidos']]})
    # ratings
    pl = [t for t, f in eq.items() if AR.primera_division(f)]
    rat = {}
    for m, nom in AR.MERCADOS.items():
        ml = AR.media_liga(eq, m)[0]
        if ml is None:
            continue
        fila = []
        for t in pl:
            r = AR.rating(eq, t, m)
            if r:
                fila.append([t, round(r[0], 2), round(r[1], 2)])
        rat[m] = {'nombre': nom, 'liga': round(ml, 2), 'equipos': sorted(fila, key=lambda z: z[2])}
    # partidos ajustados (transparencia)
    paj = {}
    for m in AR.MERCADOS:
        rl, rv = AR.rating(eq, L, m), AR.rating(eq, V, m)
        if not rl or not rv:
            continue
        def det(partidos, opp, tipo):
            out = []
            for p, s in zip(partidos, AR.serie(eq, partidos, opp, m, tipo)):
                pass
            return out
        res = {}
        for lado, part, opp in (('L', fs['forma']['local'], V), ('V', fs['forma']['visitante'], L)):
            sr = AR.serie(eq, [p for p in part if (m == 'g' or p.get('stats', {}).get(m))], opp, m, 'prop')
            pp = [p for p in part if (m == 'g' or p.get('stats', {}).get(m))]
            res[lado] = [[p['fecha'], p['rival'], p['comp'], p['v'], s[1], None if s[0] is None else round(s[0], 2), s[3], (round(AR.rating(eq, p['rival'], m, p.get('mid'))[1], 2) if AR.rating(eq, p['rival'], m, p.get('mid')) else None)] for p, s in zip(pp, sr)]
        paj[m] = res
    d = {'clave': clave, 'local': nombre_l, 'visitante': nombre_v, 'liga': ent['liga'], 'hora': ent.get('fecha'), 'leido': ent.get('cuotas_leidas'), 'fl': L, 'fv': V,
         'ctx': ctx['partido'], 'ctx_m': ctx['mercados'], 'arbitro': arb.get('arbitro'), 'arb_txt': (arb.get('faq_texto') or '')[:1200], 'bajas': al.get('bajas'), 'xi': al.get('probables'), 'xi_tipo': al.get('tipo'), 'xi_hora': al.get('lectura_utc'),
         'equipo': adj, 'jug': jug, 'cards': cards, 'rat': rat, 'paj': paj,
         'h2h': [[h['fecha'], h['comp'], h['g'], {k: h['stats'].get(k) for k in ('c', 'sh', 'sot', 'f', 'y')}] for h in fs['h2h']],
         'unicos': ent['betano'].get('unicos'), 'combos': json.load(open(combos_json, encoding='utf8')) if combos_json and os.path.exists(combos_json) else None}
    return d


PLANTILLA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plantillas_v2', 'analisis_partido.html'), encoding='utf8').read() if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plantillas_v2', 'analisis_partido.html')) else None

if __name__ == '__main__':
    jor, clave, rat = sys.argv[1:4]
    cj = sys.argv[4] if len(sys.argv) > 4 else f'{jor}/bb/combos_{clave}.json'
    d = reunir(jor, clave, rat, cj)
    tpl = PLANTILLA
    out = tpl.replace('/*__DATOS__*/', 'const D=' + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';')
    dst = f'{jor}/bb/analisis_{clave}.html'
    open(dst, 'w', encoding='utf8').write(out)
    print(dst, round(len(out) / 1024), 'KB', '| líneas equipo', len(d['equipo']), '| líneas jugador', len(d['jug']), '| jugadores', len(d['cards']))
