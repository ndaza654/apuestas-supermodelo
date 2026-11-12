# -*- coding: utf-8 -*-
"""Combinadas del mismo partido (builders) y carteras de boletos, con el precio REAL del cupón de Betano.

Une lo que antes estaba suelto (joint3.py del 9-nov) con las lecciones del balance:
  · dos probabilidades por combo: «sim.» (la conjunta de la simulación, un techo en patas de 1T y Ambos No) y
    «ajust.» (la sim. llevando cada pata a su probabilidad de decisión, que ya mezcla el mercado). Se decide con ajust.;
  · cuota justa y cuota mínima; EV con la cuota del cupón (no la de la tarjeta «Mejores cuotas», que no es la del cupón);
  · stress por pata: qué pasa si una pata está 5 pts peor de lo que creemos (Junior–Cúcuta: con Más 2.5 al 47 % el combo
    pasaba de +3,5 % a −11 %); la pata más frágil;
  · margen acumulado: cuánto margen de la casa se paga por pata (0,95^n);
  · avisos de la memoria propia de cada pata (p. ej. fuga en córners Más);
  · cartera: boletos de distintos partidos que dependen del mismo guion cuentan como UNA apuesta repetida.

Uso:
  python3 -m supermodelo --combos partido.json combos.json [--registro registro.csv]
combos.json = [{"nombre": "Junior gana + Más 2.5 + córners Más 9.5", "cuota": 6.36, "apostado": true, "stake": 1,
                "patas": ["Gana Junior", "Goles Más 2.5", "Córners Más 9.5"]}, ...]
Cada pata es el nombre que sale en el informe (columna Selección) o un dict de selección (mercados.py).
"""
import json, math, sys
import numpy as np
from . import config as C, mercados as MS, escenarios as ES, dependencia as DEP

STRESS_PTS = 0.05


def _norm(t):
    import unicodedata
    t = unicodedata.normalize('NFKD', str(t)).encode('ascii', 'ignore').decode().lower().replace(',', '.')
    return ' '.join(t.split())


def _buscar(A, pata):
    """Línea del análisis que corresponde a la pata (por nombre, sin importar tildes, mayúsculas ni coma decimal, o por
    selección)."""
    if isinstance(pata, dict):
        for r in A['lineas']:
            q = r['sel']
            if all(q.get(k) == v for k, v in pata.items()):
                return r
        return None
    t = _norm(pata)
    for r in A['lineas']:
        if _norm(r['seleccion']) == t:
            return r
    cand = [r for r in A['lineas'] if t in _norm(r['seleccion'])]
    return cand[0] if len(cand) == 1 else None


def evaluar(A, S, patas, cuota=None, nombre=None):
    """A: resultado de analizar(); S: simulación (analizar(..., devolver_sim=True) → A['_S']).
    Devuelve dict con p_sim, p_ajust, cuota justa/mínima, EV a la cuota del cupón, stress, margen y avisos."""
    sim, jug, lab, pg = S['sim'], S.get('jug'), S['lab'], S['pg']
    filas, faltan = [], []
    for p in patas:
        r = _buscar(A, p)
        if r is None:
            faltan.append(p if isinstance(p, str) else json.dumps(p, ensure_ascii=False))
        else:
            filas.append(r)
    if faltan:
        return dict(nombre=nombre, error='No encontré estas patas en el análisis: ' + '; '.join(faltan))
    if len({r['seleccion'] for r in filas}) < len(filas):
        return dict(nombre=nombre, error='Hay una pata repetida en el combo')
    evs = [MS.evento(sim, r['sel'], jug) for r in filas]
    j = np.logical_and.reduce(evs)
    p_sim = float(j.mean())
    ps = [float(e.mean()) for e in evs]
    fac = math.prod(r['p'] / pc for r, pc in zip(filas, ps) if pc > 0)
    fdep, ndep = DEP.factor([(r['sel'], pc) for r, pc in zip(filas, ps)], A.get('favorito_lado'))
    p_aj = min(p_sim * fac * fdep, min(r['p'] for r in filas)) if p_sim > 0 else 0.0
    prod_sim = math.prod(ps)
    corr = p_sim * fdep / prod_sim if prod_sim > 0 else None
    # stress: cada pata 5 pts peor (en su probabilidad de decisión), una a la vez
    stress = []
    for i, r in enumerate(filas):
        if ps[i] <= 0:
            continue
        p_i = max(0.01, r['p'] - STRESS_PTS)
        stress.append((r['seleccion'], p_aj * p_i / r['p']))
    peor = min(stress, key=lambda x: x[1]) if stress else (None, p_aj)
    # margen acumulado (solo patas con precio de dos lados)
    margen = [r['p_mercado'] * r['cuota'] for r in filas if r.get('p_mercado')]
    # guion
    g = {nm: float(j[lab == i].mean()) for i, nm in enumerate(ES.GUIONES) if (lab == i).sum() > 200}
    rel = [g[ES.GUIONES[i]] * (p_aj / p_sim if p_sim else 1) for i in range(len(ES.GUIONES))
           if pg[i] >= C.UMBRAL_ESCENARIO_RELEVANTE and ES.GUIONES[i] in g]
    avisos = sorted({m for r in filas for m in (r.get('memoria') or [])} | {r['alerta'] for r in filas if r.get('alerta')})
    out = dict(nombre=nombre or ' + '.join(r['seleccion'] for r in filas), patas=[r['seleccion'] for r in filas],
               p_patas=[round(r['p'], 4) for r in filas], p_sim=round(p_sim, 4), p_ajust=round(p_aj, 4),
               cuota_justa=round(1 / p_aj, 2) if p_aj > 0 else None, cuota_minima=round(1.03 / p_aj, 2) if p_aj > 0 else None,
               producto_cuotas=round(math.prod(r['cuota'] for r in filas), 2),
               correlacion=None if corr is None else round(corr, 2),
               guion_comun=max(g, key=g.get) if g else None, robustez=round(min(rel), 3) if rel else None,
               pata_mas_fragil=peor[0], p_stress=round(peor[1], 4),
               margen_acumulado=round(1 - math.prod(margen), 3) if margen else None,
               avisos=avisos, ajuste_dependencia=round(fdep, 3), notas_dependencia=ndep)
    if cuota:
        out.update(cuota=cuota, ev_sim=round(p_sim * cuota - 1, 4), ev_ajust=round(p_aj * cuota - 1, 4),
                   ev_stress=round(peor[1] * cuota - 1, 4))
        out['estado'] = estado(out)
    return out


def estado(c):
    """Convención del 9-nov, ahora con stress: 'valor' si el EV ajustado ≥ +3 % y aguanta el stress (≥ −3 %);
    'justo' si el EV sim. ≥ −1 % y el ajustado ≥ −7 %; 'evitar' por debajo. Es una etiqueta, no una orden."""
    if c['ev_ajust'] >= 0.03 and c['ev_stress'] >= -0.03:
        return 'valor'
    if c['ev_sim'] >= -0.01 and c['ev_ajust'] >= -0.07:
        return 'justo'
    return 'evitar'


# ------------------------------------------------------------------ cartera de boletos (varios partidos)
DIRECCION = {
    'goles': {'mas': 'muchos goles', 'menos': 'pocos goles'},
    'ambos': {'si': 'muchos goles', 'no': 'pocos goles'},
    'corners': {'mas': 'muchos córners', 'menos': 'pocos córners'},
    'tarjetas': {'mas': 'partido caliente', 'menos': 'partido limpio'},
    'remates': {'mas': 'mucho volumen', 'menos': 'poco volumen'},
    'al_arco': {'mas': 'mucho volumen', 'menos': 'poco volumen'},
}


def cartera(boletos):
    """boletos: lista de dicts de evaluar() con 'sel' de cada pata (o el nombre). Agrupa por la idea de partido de la que
    depende cada boleto. Si ≥2 boletos dependen de la misma idea, no son apuestas independientes: si el modelo se equivoca
    en esa idea (como el 9-nov con 'muchos goles y córners'), pierden juntos."""
    ideas = {}
    for b in boletos:
        for s in b.get('_sels', []):
            fam = s.get('mercado')
            d = DIRECCION.get(fam, {}).get(s.get('lado'))
            if d:
                ideas.setdefault(d, set()).add(b.get('nombre'))
    rep = {k: sorted(v) for k, v in ideas.items() if len(v) >= 2}
    return dict(ideas=rep, aviso=('Boletos que dependen de la misma idea (cuentan como una apuesta repetida): ' +
                                  '; '.join(f"{k}: {', '.join(v)}" for k, v in rep.items())) if rep else None)


def tabla_md(cs):
    L = ['| Combo | Patas | Prob. sim. | Prob. ajust. | Cuota justa | Cuota mínima | Cupón | EV ajust. | Stress (pata −5 pts) | Correlación | Margen acumulado | Estado |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    f = lambda x: '—' if x is None else f'{x * 100:.0f} %'
    g = lambda x: '—' if x is None else f'{x * 100:+.1f} %'
    for c in cs:
        if c.get('error'):
            L.append(f"| {c.get('nombre')} | {c['error']} |  |  |  |  |  |  |  |  |  |  |")
            continue
        L.append(f"| {c['nombre']} | {' + '.join(c['patas'])} | {f(c['p_sim'])} | {f(c['p_ajust'])} | {c['cuota_justa']} | "
                 f"{c['cuota_minima']} | {c.get('cuota', '—')} | {g(c.get('ev_ajust'))} | {g(c.get('ev_stress'))} ({c['pata_mas_fragil']}) | "
                 f"{c['correlacion']} | {f(c['margen_acumulado'])} | {c.get('estado', '—')} |")
        if c.get('avisos'):
            L.append(f"| ↳ avisos | {' · '.join(c['avisos'])} |  |  |  |  |  |  |  |  |  |  |")
    return '\n'.join(L)


def main(argv):
    from .analizar import analizar
    e = json.load(open(argv[0], encoding='utf8'))
    lista = json.load(open(argv[1], encoding='utf8'))
    A = analizar(e, devolver_sim=True)
    S = A.pop('_S')
    cs = []
    for c in lista:
        r = evaluar(A, S, c['patas'], c.get('cuota'), c.get('nombre'))
        r['_sels'] = [x['sel'] for x in A['lineas'] if x['seleccion'] in r.get('patas', [])]
        cs.append(r)
        if '--registro' in argv and c.get('apostado') and not r.get('error'):
            from . import registro as RG
            RG.guardar_combo(argv[argv.index('--registro') + 1], A, r, apostado=True, stake=c.get('stake', ''), sels=r['_sels'])
    print(f"# Combos: {A['partido']}\n")
    print(tabla_md(cs))
    cart = cartera(cs)
    if cart['aviso']:
        print('\n' + cart['aviso'])
    for c in cs:
        c.pop('_sels', None)
    json.dump(cs, open(argv[1].rsplit('.', 1)[0] + '_resultado.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main(sys.argv[1:])
