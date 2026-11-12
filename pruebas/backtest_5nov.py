# -*- coding: utf-8 -*-
"""Prueba con datos reales previos al partido: 17 partidos del 5-nov (perfiles y escaleras de Betano del kit v1,
resultados de Flashscore). Compara la calibración de: mercado sin margen, modelo v1 (binomial negativa por
estadística + 50/50 con el mercado) y supermodelo SM-1 (simulador calibrado + 50/50 con el mercado). En el código la
columna se sigue llamando 'v2' por compatibilidad; los rótulos impresos dicen SM-1."""
import sys, json, math
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from supermodelo import perfiles as PF, mercado as MK, lectores as LE, mercados as MS
from supermodelo.analizar import analizar, media_mercado

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datos') + '/'
eq = PF.desde_kit_v1(D + 'teams12.txt') | PF.desde_kit_v1(D + 'ecl12.txt')
grupo = PF.promedios_grupo(eq)
prof = {t: PF.perfil(p, grupo) for t, p in eq.items()}
lad = json.load(open(D + 'ladders_5nov.json'))
res = json.load(open(D + 'resultados_5nov.json'))
S = {'corners': 'c', 'remates': 'sh', 'al_arco': 'sot', 'faltas': 'f', 'tarjetas': 'y'}
R1 = {'corners': (18, 25), 'remates': (50, 60), 'al_arco': (20, 25), 'faltas': (50, 80), 'tarjetas': (10, 12)}

# 1) medias del modelo y sesgo de la jornada (igual para v1 y v2: solo usa cuotas previas)
med, ratios = {}, {}
for k in lad:
    h, a = k.split('|')
    bet = LE.desde_kit_v1(lad[k])
    med[k] = {}
    for m, s in S.items():
        mh, ma = PF.media_partido(prof[h], prof[a], grupo, s)
        med[k][s] = (mh, ma)
        for amb, v in (('local', mh), ('visitante', ma), ('total', mh + ma)):
            mm = media_mercado(bet, m, amb)
            if mm:
                ratios.setdefault(f'{s}|{amb}', []).append(v / mm)
sesgo = {k: math.exp(np.mean(np.log(v))) for k, v in ratios.items() if len(v) >= 4}

def real(r, m, amb):
    P = r['P']; s = S[m]
    if s == 'y':
        v = [P.get('y', [0, 0])[i] + P.get('r', [0, 0])[i] for i in (0, 1)]
    else:
        v = P[s]
    return {'local': v[0], 'visitante': v[1], 'total': v[0] + v[1]}[amb]

filas = []
for k in lad:
    h, a = k.split('|')
    bet = LE.desde_kit_v1(lad[k])
    objetivos = {'local': {}, 'visitante': {}}
    for s in S.values():
        objetivos['local'][s] = med[k][s][0]; objetivos['visitante'][s] = med[k][s][1]
    sg = {}
    for s in S.values():
        for amb in ('local', 'visitante'):
            b = sesgo.get(f'{s}|{amb}') or sesgo.get(f'{s}|total')
            if b: sg[f'{s}|{amb}'] = b
    A = analizar(dict(local=h, visitante=a, objetivos=objetivos, sesgo=sg, betano=bet), n=8000, builders=False)
    for r in A['lineas']:
        sel = r['sel']
        if sel['lado'] != 'mas':
            continue
        m, amb, L = sel['mercado'], sel['ambito'], sel['linea']
        x = real(res[k], m, amb)
        y = 1 if x > L else 0
        s = S[m]
        mh, ma = med[k][s]
        bh = sg.get(f'{s}|local', 1); ba = sg.get(f'{s}|visitante', 1)
        if amb == 'total':
            m1, m2 = mh / bh, ma / ba; rr = R1[m][0]
            v = m1 + m1 ** 2 / rr + m2 + m2 ** 2 / rr; mu = m1 + m2; rt = mu * mu / max(v - mu, 1e-6)
        else:
            mu = mh / bh if amb == 'local' else ma / ba; rt = R1[m][0]
        p_nb = MK.p_mas_nb(mu, rt, L)
        pm = r['p_mercado']
        filas.append(dict(partido=k, mercado=m, ambito=amb, linea=L, y=y, real=x, mkt=pm, v1=0.5 * p_nb + 0.5 * pm,
                          v2=r['p'], v1_mod=p_nb, v2_mod=r.get('p_simulacion', r['p_sin_contexto']), cuota_mas=r['cuota'],
                          cuota_menos=next((q['cuota'] for q in A['lineas'] if q['sel'] == dict(sel, lado='menos')), None)))

def brier(col, F): return float(np.mean([(f[col] - f['y']) ** 2 for f in F]))
def logloss(col, F):
    e = 1e-6; return float(-np.mean([f['y'] * math.log(max(f[col], e)) + (1 - f['y']) * math.log(max(1 - f[col], e)) for f in F]))
print(f'líneas evaluadas: {len(filas)} (lado Más de cada línea), partidos: {len(lad)}')
print(f'{"grupo":22s} {"n":>4s} | Brier  mercado   v1    SM-1  | log-loss mercado   v1    SM-1  | solo modelo v1  SM-1 (simulación sin mezcla)')
grupos = [('TODO', filas)] + [(m, [f for f in filas if f['mercado'] == m]) for m in S] + \
         [('ámbito ' + a, [f for f in filas if f['ambito'] == a]) for a in ('total', 'local', 'visitante')]
out = []
for g, F in grupos:
    if not F: continue
    row = dict(grupo=g, n=len(F), brier_mkt=brier('mkt', F), brier_v1=brier('v1', F), brier_v2=brier('v2', F),
               ll_mkt=logloss('mkt', F), ll_v1=logloss('v1', F), ll_v2=logloss('v2', F),
               brier_v1_mod=brier('v1_mod', F), brier_v2_mod=brier('v2_mod', F))
    out.append(row)
    print(f"{g:22s} {len(F):4d} | {row['brier_mkt']:.4f} {row['brier_v1']:.4f} {row['brier_v2']:.4f} | "
          f"{row['ll_mkt']:.4f} {row['ll_v1']:.4f} {row['ll_v2']:.4f} | {row['brier_v1_mod']:.4f} {row['brier_v2_mod']:.4f}")

# 2) si se hubiera apostado 1 u en cada lado con EV >= 5 % (ambos lados)
def apuestas(col):
    n = gan = 0; pl = 0.0
    for f in filas:
        for lado in ('mas', 'menos'):
            c = f['cuota_mas'] if lado == 'mas' else f['cuota_menos']
            if not c: continue
            p = f[col] if lado == 'mas' else 1 - f[col]
            if p * c - 1 >= 0.05 and p - 1 / c >= 0.03:
                ok = f['y'] == 1 if lado == 'mas' else f['y'] == 0
                n += 1; gan += ok; pl += (c - 1) if ok else -1
    return n, gan, pl
print('\nApuestas simuladas (1 u por selección con EV >= 5 % y ventaja >= 3 pts):')
for col in ('v1', 'v2'):
    n, g, pl = apuestas(col)
    print(f'  {"SM-1" if col == "v2" else col}: {n} apuestas, {g} ganadas ({g / max(n, 1):.0%}), resultado {pl:+.1f} u (ROI {pl / max(n, 1):+.1%})')
json.dump(dict(resumen=out, filas=filas, sesgo=sesgo), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backtest_5nov_resultado.json'), 'w'), indent=1, default=float)
