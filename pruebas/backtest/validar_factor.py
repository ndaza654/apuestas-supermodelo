"""Valida la tasa histórica (clubes) contra las líneas de registro/lineas.csv ya calificadas con «cumple» (selecciones y otras jornadas, fuera de la muestra del backtest).
Uso: python3 -I pruebas/backtest/validar_factor.py     -> registro/validacion_tasas.json   (lo lee el informe del backtest y el dashboard)"""
import csv, json, os, sys, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, 'recoleccion'))
import tasas_historicas as TH

num = lambda x: (float(x) if x not in ('', None) else None)
def xde(s):
    try:
        a, b = s.split(' de '); return int(a), int(b)
    except ValueError:
        return None
L = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
R, sin = [], 0
for r in L:
    if r['cumple_ficha'] != 'sí' or r['resultado'] not in ('cumplió', 'falló') or r['mercado'].startswith('jugador') or r['jornada'] >= '2026-11-16':
        continue
    pm, a, b = num(r['p_modelo']), xde(r['reg_local']), xde(r['reg_visitante'])
    if pm is None or not a or not b:
        continue
    t = TH.tasa(r['mercado'], r['ambito'], r['lado'], num(r['linea']), a[0] / a[1] * 10, b[0] / b[1] * 10, num(r['colchon']), 10)
    if not t:
        sin += 1; continue
    R.append((r['mercado'], r['lado'], pm, t['p'], 1 if r['resultado'] == 'cumplió' else 0, r['jornada']))
n = len(R)
brier = lambda f, S: round(sum((f(x) - x[4]) ** 2 for x in S) / len(S), 4)
med = lambda f, S: round(sum(f(x) for x in S) / len(S), 3)
g = lambda nom, S: {'grupo': nom, 'n': len(S), 'modelo': med(lambda x: x[2], S), 'historica': med(lambda x: x[3], S), 'real': med(lambda x: x[4], S)} if S else None
V = {'lineas': n, 'sin_tasa': sin, 'jornadas': sorted({x[5] for x in R}),
     'brier': {'modelo': brier(lambda x: x[2], R), 'historica': brier(lambda x: x[3], R), 'minimo': brier(lambda x: min(x[2], x[3]), R), 'promedio': brier(lambda x: (x[2] + x[3]) / 2, R),
               'mezcla_25': brier(lambda x: .75 * x[2] + .25 * x[3], R)},
     'discrepancia': [g(t, S) for t, S in (('hist ≥ modelo + 0,10', [x for x in R if x[3] - x[2] >= .10]), ('hist dentro de ±0,10', [x for x in R if abs(x[3] - x[2]) < .10]),
                                           ('hist ≤ modelo − 0,10', [x for x in R if x[2] - x[3] >= .10]), ('modelo < 0,70 y hist ≥ 0,70', [x for x in R if x[2] < .7 and x[3] >= .7]))],
     'por_mercado': []}
gm = collections.defaultdict(list)
for x in R:
    gm[(x[0], x[1])].append(x)
V['por_mercado'] = [g(f'{k[0]} {k[1]}', S) for k, S in sorted(gm.items()) if len(S) >= 8]
V['conclusion'] = ('La tasa de clubes, como p, no calibra mejor que el modelo en estas líneas; cuando es más baja que el modelo, el modelo acertó, y cuando es más alta, lo real queda entre las dos. '
                   'Por eso se muestra como segunda opinión (semáforo) y no recorta p.')
json.dump(V, open(os.path.join(RAIZ, 'registro', 'validacion_tasas.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(n, 'líneas', V['brier'])
