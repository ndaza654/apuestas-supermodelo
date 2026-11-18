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

# regla de muestra: 10 por equipo, cumple con 7 de 10 (n mínimo 7), directos 6 como máximo
check((FI.N, FI.N_H2H, FI.MIN_N, FI.CUMPLE) == (10, 6, 7, 7), 'constantes de la regla: 10 partidos, 6 directos, cumple 7 de 10')
largo = [(6, 4)] * 10 + [(0, 0)] * 5
r5 = FI.ficha_estadistica(partido(largo, largo, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')
check(r5['n_local'] == 10 and r5['lineas'][0]['mas']['reg_local']['x'] == 10, 'la muestra es de 10 partidos (los más recientes)')
m7 = [(6, 4)] * 7 + [(0, 0)] * 3          # 7 de 10 cumplen la línea 8.5 (Más)
m6 = [(6, 4)] * 6 + [(0, 0)] * 4          # 6 de 10 no cumple
a7 = FI.ficha_estadistica(partido(m7, m7, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')['lineas'][0]['mas']
a6 = FI.ficha_estadistica(partido(m6, m6, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')['lineas'][0]['mas']
check(a7['reg_local']['txt'] == '7 de 10' and a7['cumple'] and a6['reg_local']['txt'] == '6 de 10' and not a6['cumple'], '7 de 10 cumple; 6 de 10 se muestra y no cumple')
c5 = FI.ficha_estadistica(partido([(6, 4)] * 6, [(6, 4)] * 6, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')['lineas'][0]['mas']
check(c5['reg_local']['txt'] == '6 de 6' and not c5['cumple'], 'con menos de 7 partidos (n mínimo) no cumple aunque sean todos')

# directos
e6 = partido(L7, V7, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.5, 'menos': 2.5}])
e6['ficha']['h2h'] = [{'stats': {'c': [5, 6]}}, {'stats': {'c': [5, 4]}}, {'stats': {'c': [6, 6]}}]
r6 = FI.ficha_estadistica(e6, 'corners')
check(r6['n_directos'] == 3 and r6['lineas'][0]['mas']['directos']['txt'] == '3 de 3', 'los directos con estadísticas se cuentan aparte')
e6['ficha']['h2h'] = [{'stats': {'c': [6, 6]}}] * 9
r6b = FI.ficha_estadistica(e6, 'corners')
check(r6b['n_directos'] == 6 and r6b['lineas'][0]['mas']['directos']['txt'] == '6 de 6', 'los directos se limitan a 6 como máximo')

# jugadores
hist = {'Juan Perez': {'pos': 'Delantero', 'partidos': [{'min': 90, 'remates': 3, 'al_arco': 1, 'goles': 1, 'asist': 0}] * 7 + [{'min': 90, 'remates': 0, 'al_arco': 0, 'goles': 0, 'asist': 0}] * 3}}
jug = [{'jugador': 'J. Perez', 'lado': 'local', 'stat': 'remates', 'escalera': {'1': 1.2, '2': 1.7, '4': 4.0}},
       {'jugador': 'J. Perez', 'lado': 'local', 'stat': 'anota', 'cuota': 2.0}]
ej = partido(L7, V7, [], jug, hist, [{'nombre': 'Juan Perez', 'lado': 'local', 'titular': 0.9, 'minutos': 90}])
J = FI.ficha_jugadores(ej)
rem = [j for j in J if j['stat'] == 'remates'][0]
check(rem['por_90'] == round(21 * 90 / 900, 2) and rem['partidos_muestra'] == 10, 'tasa por 90 con los minutos jugados')
check([s['reg']['x'] for s in rem['escalones']] == [7, 7, 0] and rem['escalones'][0]['reg']['cumple'], 'regularidad por escalón: 1+ y 2+ en 7 de 10; 4+ en 0')
check([j for j in J if j['stat'] == 'anota'][0]['reg']['x'] == 7, 'anota: veces que marcó en los últimos partidos')
check(rem['titular'] == 0.9, 'el nombre abreviado de Betano se une al jugador del historial y a su titularidad')

# --- goles y tarjetas (agentes goles-resultado y tarjetas) y líneas asiáticas ---
v = [1, 2, 3, 2, 4]
check((FI.cuenta(v, 2.25, 'mas'), FI.cuenta(v, 2.25, 'menos'), FI.cuenta(v, 2.75, 'mas'), FI.cuenta(v, 2.75, 'menos')) == (2, 1, 1, 3),
      'línea asiática (.25/.75): solo cuenta la victoria completa; el punto medio es media ganancia/pérdida y no cumple')
check((FI.cuenta(v, 2.0, 'mas'), FI.cuenta(v, 2.0, 'menos'), FI.cuenta(v, 2.5, 'mas')) == (2, 1, 2), 'línea entera: el empate no cuenta; .5 sin cambios')
eg = {'local': 'A', 'visitante': 'B', 'liga': 'X', 'fecha': '2026-01-01',
      'ficha': {'forma': {'local': [{'stats': {'g': [2, 1], 'y': [2, 3]}}] * 7, 'visitante': [{'stats': {'g': [1, 1], 'y': [1, 2]}}] * 7}},
      'betano': {'lineas': [{'mercado': 'goles', 'ambito': 'total', 'linea': 2.5, 'mas': 1.8, 'menos': 2.0},
                            {'mercado': 'tarjetas', 'ambito': 'total', 'linea': 3.5, 'mas': 1.9, 'menos': 1.9}], 'jugadores': []}}
Fg = FI.construir(eg)
check(Fg['goles']['esperado']['total'] == 2.5 and Fg['goles']['lineas'][0]['mas']['reg_local']['x'] == 7, 'la ficha trae goles (serie g)')
check('amarillas' in Fg['tarjetas']['nota'] and Fg['tarjetas']['esperado']['total'] == 4.0, 'tarjetas: usa amarillas y avisa que Betano cuenta puntos (rojas no vienen en la fuente)')

# jornada recogida con 7 partidos: «muestra de 7», cumple 5 de 7 (proporción de 7 de 10); después vuelve a la regla
check(FI.fijar_muestra(7) == (7, 5, 5), 'muestra de 7 -> cumple 5 de 7, n mínimo 5')
s5 = [(6, 4)] * 5 + [(0, 0)] * 2
s4 = [(6, 4)] * 4 + [(0, 0)] * 3
b5 = FI.ficha_estadistica(partido(s5, s5, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')['lineas'][0]['mas']
b4 = FI.ficha_estadistica(partido(s4, s4, [{'mercado': 'corners', 'ambito': 'total', 'linea': 8.5, 'mas': 1.8, 'menos': 1.9}]), 'corners')['lineas'][0]['mas']
check(b5['reg_local']['txt'] == '5 de 7' and b5['cumple'] and not b4['cumple'], 'con muestra de 7: 5 de 7 cumple y 4 de 7 no')
check('5 de 7' in FI.construir(eg)['regla']['cumple'] and 'últimos 7' in FI.construir(eg)['regla']['muestra'], 'la ficha declara «muestra de 7» y «5 de 7»')
check(FI.fijar_muestra(10) == (10, 7, 7) and FI.fijar_muestra(0) == (10, 7, 7) and FI.fijar_muestra(12) == (10, 7, 7), 'con 10 o más (o sin dato) vale la regla 7 de 10')
import tempfile, json as _j
with tempfile.TemporaryDirectory() as td:
    _j.dump(eg, open(os.path.join(td, 'a.json'), 'w'))
    check(FI.muestra_de(td) == 7, 'muestra_de: lee el mayor número de partidos por equipo de las entradas')

# ambos marcan y resultado (desde el 18-nov-2026): se cuentan en los últimos partidos de cada equipo, sin línea ni colchón
FI.fijar_muestra(10)
gl = [{'g': [2, 1]}] * 8 + [{'g': [0, 0]}] * 2          # local: ganó 8, empató 2; marcaron ambos en 8
gv = [{'stats': {'g': [1, 2]}}] * 7 + [{'g': [1, 1]}] * 3  # visitante: perdió 7, empató 3; marcaron ambos en 10 (g dentro de stats o arriba)
er = {'local': 'A', 'visitante': 'B', 'liga': 'X', 'fecha': '2026-01-01', 'ficha': {'forma': {'local': gl, 'visitante': gv}, 'h2h': [{'g': [2, 0]}, {'g': [1, 1]}]},
      'betano': {'lineas': [], 'jugadores': [], 'unicos': [{'mercado': 'ambos', 'opciones': {'si': 1.8, 'no': 2.0}},
                                                          {'mercado': 'resultado', 'opciones': {'1': 1.6, 'X': 4.0, '2': 5.0, '1X': 1.2, 'X2': 2.4, '12': 1.3}}]}}
R = FI.construir(er)['resultados']
fila = lambda m, s: [x for x in R[m] if x['seleccion'] == s][0]
check(fila('ambos', 'si')['reg_local']['txt'] == '8 de 10' and fila('ambos', 'si')['reg_visitante']['txt'] == '10 de 10' and fila('ambos', 'si')['cumple'], 'ambos marcan Sí: cuenta cuántas veces marcaron los dos en cada equipo (g arriba o dentro de stats)')
check(fila('ambos', 'no')['reg_local']['txt'] == '2 de 10' and not fila('ambos', 'no')['cumple'], 'ambos marcan No: lo contrario, no cumple con 2 de 10')
check(fila('resultado', '1')['reg_local']['txt'] == '8 de 10' and fila('resultado', '1')['reg_visitante']['txt'] == '7 de 10' and fila('resultado', '1')['cumple'], 'resultado 1: el local ganó y el visitante perdió')
check(fila('resultado', 'X')['reg_local']['txt'] == '2 de 10' and fila('resultado', 'X')['reg_visitante']['txt'] == '3 de 10' and not fila('resultado', 'X')['cumple'], 'resultado X: empates de cada equipo')
check(fila('resultado', '12')['reg_local']['txt'] == '8 de 10' and fila('resultado', '12')['reg_visitante']['txt'] == '7 de 10', '12 = sin empate')
check(fila('resultado', '1X')['reg_local']['txt'] == '10 de 10' and fila('resultado', '1X')['directos']['txt'] == '2 de 2', '1X: el local no perdió; directos desde el local de hoy')
check(len(R['resultado']) == 6 and 'Sin línea' not in R['nota'] and 'colchón' in R['nota'], 'trae las 6 selecciones y avisa que no hay línea ni colchón')
check('## Ambos marcan y resultado' in FI.markdown(FI.construir(er)), 'la ficha en Markdown incluye la sección')
import registrar_jornada as RJ, calificar_lineas as CL
filas_r = RJ.filas_de(FI.construir(er), None, '2026-01-01')
check({(x['mercado'], x['lado']) for x in filas_r if x['mercado'] in ('ambos', 'resultado')} >= {('ambos', 'Sí'), ('ambos', 'No'), ('resultado', '1X')}, 'registro/lineas.csv recibe una fila por selección')
check(CL.calificar_unico({'g': [2, 1]}, 'ambos', 'Sí')[0] == 'cumplió' and CL.calificar_unico({'g': [1, 1]}, 'resultado', '1')[0] == 'falló'
      and CL.calificar_unico({'g': [1, 1]}, 'resultado', 'X2')[0] == 'cumplió' and CL.calificar_unico({}, 'ambos', 'Sí') == (None, None), 'calificación de ambos marcan y resultado con los goles del partido')

print(f'\n{ok} pruebas de la ficha superadas')
