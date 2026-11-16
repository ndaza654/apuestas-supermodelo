# -*- coding: utf-8 -*-
"""Bet Builders del mismo partido con condiciones del usuario: mínimo N patas, cada pata con cuota >= CUOTA_PATA, producto de cuotas >= TOTAL.
Usa la simulación del súper modelo (conjunta real, no producto) y el ajuste de dependencia de supermodelo/combos.py. Ordena por probabilidad conjunta.
    python3 recoleccion/combos_bb.py jornadas/AAAA-MM-DD/entradas/<partido>.json [--patas 3] [--pata 1.5] [--total 5.3] [--precio 5.4] [--sin-jugadores] [--top 12] [--max-cand 22]
Límites: la cuota del Bet Builder la fija Betano (suele quedar por debajo del producto); el modelo no sabe qué mercados Betano deja combinar;
el producto es una referencia, hay que mirar el precio del cupón. precio_est = 0,95 / p conjunta (ver K_PRECIO): con «total ≥ 5» el techo de p es ≈ 19 %."""
import re, itertools, json, math, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from supermodelo.analizar import analizar
from supermodelo import combos as CB


def familia(r):
    s = r['sel']
    if s['mercado'] == 'jugador':
        return ('jugador', s.get('jugador'), s.get('stat'))
    if s['mercado'] == 'mas_que':
        return (s.get('stat'),)
    return (s['mercado'], s.get('ambito')) if s['mercado'] in ('goles', 'corners', 'tarjetas') else (s['mercado'],)


SOLO_LINEAS = ()   # con --solo-lineas: solo mercados que están en registro/lineas.csv (así el dashboard puede mostrar la combinada)
K_PRECIO = 0.95   # precio del Bet Builder × p del modelo ≈ 0,95 (13-nov: 20 precios leídos, 0,76–1,05): Betano cobra la correlación, el producto de cuotas NO es el precio


def correr(ruta, n_patas=3, cuota_pata=1.5, total=5.3, jugadores=True, top=12, max_cand=22, max_patas=4, precio=5.4, solo=None, excluir=None, max_jug=8):
    e = json.load(open(ruta, encoding='utf8'))
    A = analizar(e, devolver_sim=True, builders=False)
    S = A.pop('_S')
    cand = [r for r in A['lineas'] if r['cuota'] >= cuota_pata and not r.get('asiatica') and r['p'] >= 0.30 and (jugadores or r['sel']['mercado'] not in ('jugador', 'pareja')) and (not SOLO_LINEAS or r['sel']['mercado'] in SOLO_LINEAS)]
    if solo:
        cand = [r for r in cand if re.search(solo, r['seleccion'])]
    if excluir:
        cand = [r for r in cand if not re.search(excluir, r['seleccion'])]
    cand = sorted(cand, key=lambda r: -r['p'])
    nj = 0
    pool = []
    for r in cand:                                    # los mercados de jugador son cientos: se limitan a 8 para no tapar al resto
        if r['sel']['mercado'] in ('jugador', 'pareja'):
            nj += 1
            if nj > max_jug:
                continue
        pool.append(r)
    cand = pool[:max_cand]
    res = []
    for n in range(n_patas, max_patas + 1):
        for c in itertools.combinations(cand, n):
            fams = [familia(r) for r in c]
            if len(set(fams)) < len(fams):
                continue                              # dos líneas del mismo mercado: Betano no las deja combinar o son casi la misma apuesta
            prod = math.prod(r['cuota'] for r in c)
            if prod < total:
                continue
            x = CB.evaluar(A, S, [r['seleccion'] for r in c], cuota=None)
            if x.get('error'):
                continue
            x['producto'] = round(prod, 2)
            x['cuotas'] = [r['cuota'] for r in c]
            x['precio_est'] = round(K_PRECIO / x['p_ajust'], 2) if x['p_ajust'] else None
            if not x['precio_est'] or x['precio_est'] < precio:
                continue                              # con patas muy correlacionadas Betano paga mucho menos que el producto
            res.append(x)
    res.sort(key=lambda x: -x['p_ajust'])
    return A, res[:top], len(cand)


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--solo-lineas' in a:
        SOLO_LINEAS = ('goles', 'corners', 'tarjetas', 'al_arco', 'remates', 'faltas', 'fueras', 'saques_meta', 'saques_banda')
    g = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    A, R, nc = correr(a[0], g('--patas', 3), g('--pata', 1.5), g('--total', 5.3), '--sin-jugadores' not in a, g('--top', 12), g('--max-cand', 22), precio=g('--precio', 5.4), solo=g('--solo', '') or None, excluir=g('--excluir', '') or None, max_jug=g('--max-jug', 8))
    print(f"# {A['partido']} · {nc} candidatas (cuota ≥ {g('--pata', 1.5)}) · combos que cumplen: top {len(R)} por probabilidad conjunta")
    for x in R:
        print(f"p {x['p_ajust']:.3f} (sim {x['p_sim']:.3f}) · prod {x['producto']} · precio est. {x['precio_est']} · corr {x['correlacion']} · stress {x['p_stress']:.3f} | " + ' + '.join(f"{s} @{q} ({p:.2f})" for s, p, q in zip(x['patas'], x['p_patas'], x['cuotas'])) + (f" | avisos: {'; '.join(x['avisos'])}" if x['avisos'] else ''))
