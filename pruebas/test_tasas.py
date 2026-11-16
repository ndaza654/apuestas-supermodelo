"""Pruebas de la tasa histórica (recoleccion/tasas_historicas.py). python3 pruebas/test_tasas.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'recoleccion'))
import tasas_historicas as TH
n = 0
def check(c, msg):
    global n
    if not c:
        print('✗', msg); sys.exit(1)
    n += 1; print('✓', msg)
t = TH.tasa('corners', 'total', 'Más', 9.5, 7, 7, 2.0)
check(t and 0.55 < t['p'] < 0.80 and t['n'] >= TH.N_MIN, 'córners total Más 9.5 con 7 de 10 en ambos: tasa razonable y muestra suficiente')
check(TH.tasa('remates', 'total', 'Más', 22.5, 10, 10, 3.0) is not None, 'conteo muy alto: se ensancha hasta una cohorte con muestra suficiente')
check(TH.tasa('corners', 'total', 'Más', 9.25, 7, 7, 2.0) is None, 'línea asiática (.25): sin tasa')
check(TH.tasa('corners', '1T', 'Más', 4.5, 7, 7, 1.0) is None, 'ámbito 1T: sin tasa')
check(TH.tasa('fueras', 'total', 'Más', 2.5, 7, 7, 1.0) is None, 'mercado no medido (fueras de juego): sin tasa')
a, b = TH.tasa('tarjetas', 'total', 'Más', 3.5, 14, 14, 1.0, n=20), TH.tasa('tarjetas', 'total', 'Más', 3.5, 7, 7, 1.0, n=10)
check(a and b and a['k'] == b['k'], 'con muestra distinta se reescala a «de 10»')
check(TH.tasa('goles', 'total', 'Menos', 2.5, 7, 7, 0.8)['p'] > 0.35, 'goles total Menos 2.5: tasa calculada')
print(n, 'pruebas de tasas superadas')
