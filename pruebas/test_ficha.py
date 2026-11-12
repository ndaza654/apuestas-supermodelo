# -*- coding: utf-8 -*-
"""Pruebas de la ficha por mercado. Ejecutar: python3 pruebas/test_ficha.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'recoleccion'))
import ficha as FI

ok = 0
def check(c, m):
    global ok
    assert c, m
    ok += 1
    print('✓', m)

def partido(vals_l, vals_v, lineas, jugs=None, hist=None, info=None):
    f = lambda vs: [{'stats': {'c': [a, b]}} for a, b in vs]
    e = {'local': 'A', 'visitante': 'B', 'liga': 'X', 'fecha': '2026-01-01',
         'ficha': {'forma': {'local': f(vals_l), 'visitante': f(vals_v)}, 'jugadores_hist': hist or {}},
         'betano': {'lineas': lineas, 'jugadores': jugs or []}, 'jugadores': info or []}
    return e

L7 = [(6, 4)] * 7          # local: 6 a favor, 4 en contra (total 10 en cada partido)
V7 = [(3, 7)] * 7          # visitante: 3 a favor, 7 en contra (total 10)
e = partido(L7, V7, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.5, 'menos': 2.5},
                     {'mercado': 'corners', 'ambito': 'total', 'linea': 10.5, 'mas': 2.5, 'menos': 1.5},
                     {'mercado': 'corners', 'ambito': 'local', 'linea': 5.5, 'mas': 1.9, 'menos': 1.9}])
r = FI.ficha_estadistica(e, 'corners')
check(r['esperado']['local'] == 6.5 and r['esperado']['visitante'] == 3.5 and r['esperado']['total'] == 10.0, 'esperado = (a favor propio + en contra del rival)/2, por equipo y total')
f85 = [x for x in r['lineas'] if x['linea'] == 8.5][0]
check(f85['mas']['colchon'] == 1.5 and f85['menos']['colchon'] == -1.5, 'colchón = esperado − línea (Más) y línea − esperado (Menos)')
check(f85['mas']['reg_local']['txt'] == '7 de 7' and f85['mas']['cumple'] and not f85['menos']['cumple'], 'regularidad 7 de 7 cumple; el lado contrario no')
f105 = [x for x in r['lineas'] if x['linea'] == 10.5][0]
check(f105['menos']['reg_local']['x'] == 7 and f105['menos']['cumple'], 'Menos 10.5: los 7 totales (10) quedan por debajo')
fl = [x for x in r['lineas'] if x['ambito'] == 'local'][0]
check(fl['mas']['reg_local']['x'] == 7 and fl['mas']['reg_visitante']['x'] == 7, 'línea de equipo: usa lo que hace el equipo y lo que concede el rival')

# 4 de 7 no cumple; n pequeño no cumple
mix = [(6, 4)] * 4 + [(2, 2)] * 3
r2 = FI.ficha_estadistica(partido(mix, mix, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')
c = r2['lineas'][0]['mas']
check(c['reg_local']['x'] == 4 and not c['reg_local']['cumple'] and not c['cumple'], '4 de 7 se muestra y no cumple')
r3 = FI.ficha_estadistica(partido([(6, 4)] * 3, [(6, 4)] * 3, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')
check(not r3['lineas'][0]['mas']['reg_local']['cumple'], 'con n < 5 nunca dice «cumple»')

# la línea entera con empate no cuenta para Más ni para Menos
r4 = FI.ficha_estadistica(partido(L7, V7, [{'mercado': 'corners', 'ambito': 'total', 'linea': 10.0, 'mas': 1.9, 'menos': 1.9}]), 'corners')
check(r4['lineas'][0]['mas']['reg_local']['x'] == 0 and r4['lineas'][0]['menos']['reg_local']['x'] == 0, 'línea entera con empate: no cuenta para ningún lado')

# solo se usan los 7 más recientes
largo = [(6, 4)] * 7 + [(0, 0)] * 5
r5 = FI.ficha_estadistica(partido(largo, largo, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')
check(r5['n_local'] == 7 and r5['lineas'][0]['mas']['reg_local']['x'] == 7, 'la muestra es de 7 partidos (los más recientes)')

# directos
e6 = partido(L7, V7, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.5, 'menos': 2.5}])
e6['ficha']['h2h'] = [{'stats': {'c': [5, 6]}}, {'stats': {'c': [5, 4]}}, {'stats': {'c': [6, 6]}}]
r6 = FI.ficha_estadistica(e6, 'corners')
check(r6['n_directos'] == 3 and r6['lineas'][0]['mas']['directos']['txt'] == '3 de 3', 'los directos con estadísticas se cuentan aparte')

# jugadores
hist = {'Juan Perez': {'pos': 'Delantero', 'partidos': [{'min': 90, 'remates': 3, 'al_arco': 1, 'goles': 1, 'asist': 0}] * 5 + [{'min': 90, 'remates': 0, 'al_arco': 0, 'goles': 0, 'asist': 0}] * 2}}
jug = [{'jugador': 'J. Perez', 'lado': 'local', 'stat': 'remates', 'escalera': {'1': 1.2, '2': 1.7, '4': 4.0}},
       {'jugador': 'J. Perez', 'lado': 'local', 'stat': 'anota', 'cuota': 2.0}]
ej = partido(L7, V7, [], jug, hist, [{'nombre': 'Juan Perez', 'lado': 'local', 'titular': 0.9, 'minutos': 90}])
J = FI.ficha_jugadores(ej)
rem = [j for j in J if j['stat'] == 'remates'][0]
check(rem['por_90'] == round(15 * 90 / 630, 2) and rem['partidos_muestra'] == 7, 'tasa por 90 con los minutos jugados')
check([s['reg']['x'] for s in rem['escalones']] == [5, 5, 0] and rem['escalones'][0]['reg']['cumple'], 'regularidad por escalón: 1+ y 2+ en 5 de 7; 4+ en 0')
check([j for j in J if j['stat'] == 'anota'][0]['reg']['x'] == 5, 'anota: veces que marcó en los últimos partidos')
check(rem['titular'] == 0.9, 'el nombre abreviado de Betano se une al jugador del historial y a su titularidad')

print(f'\n{ok} pruebas de la ficha superadas')
