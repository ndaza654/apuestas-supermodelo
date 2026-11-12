# -*- coding: utf-8 -*-
"""¿La robustez (probabilidad en el peor guion relevante) agrega información a la probabilidad? 17 partidos del 5-nov."""
import sys, json
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from supermodelo import lectores as LE
from supermodelo.analizar import analizar
D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datos') + '/'
lad = json.load(open(D + 'ladders_5nov.json')); res = json.load(open(D + 'resultados_5nov.json'))
S = {'corners': 'c', 'remates': 'sh', 'al_arco': 'sot', 'faltas': 'f', 'tarjetas': 'y'}
def real(r, m, amb):
    P = r['P']; s = S[m]
    v = [P.get('y', [0, 0])[i] + P.get('r', [0, 0])[i] for i in (0, 1)] if s == 'y' else P[s]
    return {'local': v[0], 'visitante': v[1], 'total': v[0] + v[1]}[amb]
F = []; B = []
for k in lad:
    h, a = k.split('|')
    A = analizar(dict(local=h, visitante=a, betano=LE.desde_kit_v1(lad[k])), n=8000)
    for r in A['lineas']:
        s = r['sel']; x = real(res[k], s['mercado'], s['ambito'])
        y = (x > s['linea']) if s['lado'] == 'mas' else (x < s['linea'])
        F.append(dict(p=r['p'], rob=r['robustez'], z=r['colchon_z'], y=int(y), cuota=r['cuota']))
    for b in A['builders'][:3]:
        ok = all(any(r['seleccion'] == pt and ((real(res[k], r['sel']['mercado'], r['sel']['ambito']) > r['sel']['linea']) if r['sel']['lado'] == 'mas' else (real(res[k], r['sel']['mercado'], r['sel']['ambito']) < r['sel']['linea'])) for r in A['lineas']) for pt in b['patas'])
        B.append((b['p'], int(ok), b['cuota_justa']))
print('Líneas (ambos lados):', len(F))
for lo, hi in ((0.55, 0.65), (0.65, 0.80), (0.80, 0.99)):
    X = [f for f in F if lo <= f['p'] < hi]
    med = np.median([f['rob'] for f in X])
    alto = [f for f in X if f['rob'] >= med]; bajo = [f for f in X if f['rob'] < med]
    pm = lambda Z: np.mean([f['p'] for f in Z]); hr = lambda Z: np.mean([f['y'] for f in Z])
    print(f'p {lo:.2f}-{hi:.2f}: n={len(X)} | robustez alta: prob media {pm(alto):.2f}, acierto {hr(alto):.2f} (n={len(alto)}) | '
          f'robustez baja: prob media {pm(bajo):.2f}, acierto {hr(bajo):.2f} (n={len(bajo)})')
X = [f for f in F if f['p'] >= 0.65 and f['rob'] >= 0.5]
print(f"'Alta probabilidad' (p>=0.65 y robustez>=0.5): n={len(X)}, prob media {np.mean([f['p'] for f in X]):.2f}, acierto real {np.mean([f['y'] for f in X]):.2f}, "
      f"resultado a 1 u {sum((f['cuota'] - 1) if f['y'] else -1 for f in X):+.1f} u")
print(f'Builders sugeridos (3 por partido): n={len(B)}, prob media {np.mean([b[0] for b in B]):.2f}, acierto real {np.mean([b[1] for b in B]):.2f}, cuota justa media {np.mean([b[2] for b in B]):.2f}')
