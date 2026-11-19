# -*- coding: utf-8 -*-
"""Bet Builder «BB Boost» de Betano: candidatos del modelo + precio REAL leído en Betano.

Condiciones del usuario (promo BB Boost): mínimo 3 patas, cada pata con cuota >= 1,50 y cuota total del builder >= 5,00.
Flujo (todo solo lectura; no se coloca ninguna apuesta):
  1) navegador: `bb_catalogo_extraer.js` baja el catálogo del Bet Builder (cuotas frescas de cada mercado) → jornadas/AAAA-MM-DD/bb/catalogo_HHMM.json
  2) `python3 recoleccion/bb_precios.py candidatos jornadas/AAAA-MM-DD <clave> [--catalogo bb/catalogo_HHMM.json] [--top 150]`
     refresca en memoria las cuotas del modelo con el catálogo, enumera tríos (y cuartetos) de patas con cuota >= 1,50, calcula la
     probabilidad conjunta (simulación + dependencia medida) y escribe bb/cand_<clave>.json con los ids de selección de Betano.
  3) navegador: `bb_precios_betano.js` pide a Betano el precio real de cada candidato (POST /api/betslip/v3/mc-leg; una consulta por combo).
  4) `python3 recoleccion/bb_precios.py resultado jornadas/AAAA-MM-DD <clave> precios.json` une precios y probabilidades y escribe
     bb/res_<clave>.json y .md con las combinaciones que CUMPLEN las condiciones (patas >= 1,50 y precio real >= 5,00), ordenadas.
Límites: el precio del builder lo fija Betano (puede ser menor o mayor que el producto: 3 patas con goles+córners+tarjetas «Más» pagaron
5,70 frente a 5,41 de producto); la probabilidad es la del modelo (≈ mercado; no hay ventaja demostrada). El bono de la promo no se aplica aquí.
"""
import itertools, json, math, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from supermodelo.analizar import analizar
from supermodelo import combos as CB, mercados as MS, dependencia as DEP
import bb_catalogo as BC

CUOTA_PATA = 1.50
TOTAL_MIN = 5.00
CLAVES = {'vasco-da-gama-rj-internacional-rs': 'vasco', 'vitoria-ba-bragantino-sp': 'vitoria', 'sao-paulo-sp-fluminense-rj': 'saopaulo'}


def _familia(s):
    m = s['mercado']
    if m in ('goles', 'corners', 'tarjetas', 'al_arco', 'remates', 'fueras', 'saques_meta', 'faltas', 'saques_banda'):
        return (m, s.get('ambito'))
    if m in ('mas_que',):
        return (m, s.get('stat'))
    if m == 'ambos_n_tarjetas':
        return (m, s.get('n'))
    if m in ('resultado', 'resultado_1t'):
        return ('resultado',)           # 1X2 y doble oportunidad no se combinan entre sí
    return (m,)


def refrescar_entrada(e, legs):
    """Actualiza en memoria las cuotas de la entrada con las del catálogo (mismo mercado/ámbito/línea)."""
    por = {BC.clave(l['sel']): l['precio'] for l in legs}
    n = 0
    for r in e['betano']['lineas']:
        for lado, k in (('mas', 'mas'), ('menos', 'menos')):
            c = por.get(BC.clave(dict(mercado=r['mercado'], ambito=r['ambito'], linea=float(r['linea']), lado=lado)))
            if c and r.get(k) != c:
                r[k] = c
                n += 1
    for u in e['betano'].get('unicos', []):
        if u['mercado'] == 'resultado':
            for o in list(u['opciones']):
                c = por.get(BC.clave(dict(mercado='resultado', lado=o)))
                if c and u['opciones'][o] != c:
                    u['opciones'][o] = c
                    n += 1
        elif u['mercado'] == 'ambos':
            for o in list(u['opciones']):
                c = por.get(BC.clave(dict(mercado='ambos', lado=o)))
                if c and u['opciones'][o] != c:
                    u['opciones'][o] = c
                    n += 1
        elif u['mercado'] == 'ambos_n_tarjetas':
            for o in list(u['opciones']):
                c = por.get(BC.clave(dict(mercado='ambos_n_tarjetas', n=u['n'], lado=o)))
                if c and u['opciones'][o] != c:
                    u['opciones'][o] = c
                    n += 1
    return n


def candidatos(jornada, clave, catalogo=None, top=150, max_patas=4, pool_n=90, pool4=26, prod_min=5.0, p_max=0.24, p_min=0.15, solidas=False, sin_jugadores=True, pool5=14):
    cat_ruta = catalogo or sorted(f for f in os.listdir(os.path.join(jornada, 'bb')) if f.startswith('catalogo_'))[-1]
    cats = json.load(open(os.path.join(jornada, 'bb', os.path.basename(cat_ruta)), encoding='utf8'))
    cat = cats[CLAVES[clave]]
    e = json.load(open(os.path.join(jornada, 'entradas', clave + '.json'), encoding='utf8'))
    legs = BC.traducir(cat, e['local'], e['visitante'])
    u = {}
    for l in legs:
        u.setdefault(BC.clave(l['sel']), l)
    legs = list(u.values())
    cambios = refrescar_entrada(e, legs)
    A = analizar(e, devolver_sim=True, builders=False)
    S = A.pop('_S')
    idx = BC.indice_modelo(A)
    pool = []
    for l in legs:
        r = idx.get(BC.clave(l['sel']))
        if not r or l['precio'] < CUOTA_PATA or r['p'] < 0.30:
            continue
        r = dict(r)
        r['cuota'] = l['precio']
        pool.append((l, r))
    if solidas:                                   # solo patas que la ficha respalda (X de 10 >= 7 en ambos equipos; o >= 6 con colchón positivo)
        import bb_evidencia as BE
        idx_f = BE.leer(jornada, A['partido'])
        pool = [(l, r) for l, r in pool if BE.solidez(BE.pata(idx_f, r['sel']))[0] >= 0.6 and l['precio'] > 1.50]
    pool.sort(key=lambda x: -x[1]['p'])
    pool = pool[:pool_n]
    ev = [np.asarray(MS.evento(S['sim'], r['sel'], S.get('jug')), dtype=bool) for _, r in pool]
    pm = [max(float(x.mean()), 1e-9) for x in ev]
    res = []
    for n in range(3, max_patas + 1):
        for c in itertools.combinations(range(min(len(pool), pool_n if n == 3 else pool4 if n == 4 else pool5)), n):
            fams = [_familia(pool[i][1]['sel']) for i in c]
            if len(set(fams)) < n:
                continue
            prod = math.prod(pool[i][1]['cuota'] for i in c)
            if prod < prod_min:
                continue
            j = ev[c[0]].copy()
            for i in c[1:]:
                j &= ev[i]
            p_sim = float(j.mean())
            if p_sim <= 0:
                continue
            res.append((p_sim * math.prod(pool[i][1]['p'] / pm[i] for i in c), c, prod))
    res = [x for x in res if p_min <= x[0] <= p_max]       # con precio real >= 5 la probabilidad no puede ser mucho mayor que ~0,2: lo demás Betano lo paga por debajo de 5
    res.sort(key=lambda x: -x[0])
    sal = []
    paso = max(1, len(res) // int(top * 1.3))       # muestreo parejo de la ventana de probabilidad (si hay más combos que `top`)
    for _, c, prod in res[::paso][:int(top * 1.3)]:
        nombres = [pool[i][1]['seleccion'] for i in c]
        x = CB.evaluar(A, S, nombres, cuota=None)
        if x.get('error'):
            continue
        x['producto'] = round(prod, 2)
        x['cuotas'] = [pool[i][1]['cuota'] for i in c]
        x['ids'] = [pool[i][0]['id'] for i in c]
        x['pidx'] = list(c)
        x['sels'] = [pool[i][1]['sel'] for i in c]
        sal.append(x)
    sal.sort(key=lambda x: -x['p_ajust'])
    sal = sal[:top]
    out = dict(clave=clave, partido=A['partido'], catalogo_leida=cat['leida'], cuotas_refrescadas=cambios, pool=len(pool), candidatos=sal,
               pool_ids=[l['id'] for l, _ in pool], pool_nombres=[r['seleccion'] for _, r in pool])
    out['compacto'] = ' '.join('.'.join(str(i) for i in x['pidx']) for x in sal)   # índices al pool (3.14.15 …) para pegar en el navegador
    os.makedirs(os.path.join(jornada, 'bb'), exist_ok=True)
    json.dump(out, open(os.path.join(jornada, 'bb', f'cand_{clave}.json'), 'w', encoding='utf8'), ensure_ascii=False)
    return out


def resultado(jornada, clave, precios_json):
    c = json.load(open(os.path.join(jornada, 'bb', f'cand_{clave}.json'), encoding='utf8'))
    pr = json.load(open(precios_json, encoding='utf8'))
    filas = []
    for x, p in zip(c['candidatos'], pr):
        if not p:
            continue
        cumple_patas = all(q >= CUOTA_PATA for q in x['cuotas']) and len(x['patas']) >= 3
        x['precio_bb'] = p
        x['cumple'] = bool(cumple_patas and p >= TOTAL_MIN)
        x['ev_modelo'] = round(x['p_ajust'] * p - 1, 3)
        x['ev_stress'] = round(x['p_stress'] * p - 1, 3)
        filas.append(x)
    json.dump(dict(c, candidatos=filas), open(os.path.join(jornada, 'bb', f'res_{clave}.json'), 'w', encoding='utf8'), ensure_ascii=False)
    ok = sorted([x for x in filas if x['cumple']], key=lambda x: -x['p_ajust'])
    L = [f"# BB Boost · {c['partido']} · {len(filas)} combos con precio real, {len(ok)} cumplen (≥3 patas, cada una ≥ {CUOTA_PATA}, precio ≥ {TOTAL_MIN})",
         f"Catálogo leído {c['catalogo_leida']} (UTC). p = modelo (ajustada). EV informativo; el bono no está incluido.\n"]
    for x in ok[:25]:
        L.append(f"- p {x['p_ajust']:.3f} (sim {x['p_sim']:.3f}, stress {x['p_stress']:.3f}) · precio BB **{x['precio_bb']}** (producto {x['producto']}) · EV {x['ev_modelo']:+.2f} · " +
                 ' + '.join(f"{s} @{q}" for s, q in zip(x['patas'], x['cuotas'])) + (f" · frágil: {x['pata_mas_fragil']}" if x.get('pata_mas_fragil') else ''))
    open(os.path.join(jornada, 'bb', f'res_{clave}.md'), 'w', encoding='utf8').write('\n'.join(L) + '\n')
    return ok


if __name__ == '__main__':
    a = sys.argv[1:]
    g = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    if a[0] == 'candidatos':
        o = candidatos(a[1], a[2], catalogo=g('--catalogo', '') or None, top=g('--top', 150), solidas='--solidas' in a, p_min=g('--pmin', 0.15), p_max=g('--pmax', 0.24),
                       pool_n=g('--pool', 90), pool4=g('--pool4', 26), prod_min=g('--prod', 5.0), max_patas=g('--patas', 4), pool5=g('--pool5', 14))
        if '--solidas' in a:
            os.replace(os.path.join(a[1], 'bb', f'cand_{a[2]}.json'), os.path.join(a[1], 'bb', f'cands{g("--sufijo", "")}_{a[2]}.json'))
        print(o['partido'], 'pool', o['pool'], 'cuotas refrescadas', o['cuotas_refrescadas'], 'candidatos', len(o['candidatos']))
        for x in o['candidatos'][:5]:
            print(round(x['p_ajust'], 3), x['producto'], x['patas'])
    elif a[0] == 'resultado':
        ok = resultado(a[1], a[2], a[3])
        print(len(ok), 'cumplen')
