# -*- coding: utf-8 -*-
"""Pruebas de armar_entrada y puntuar con datos reales guardados (Betano + Flashscore, Italia–Francia). python3 pruebas/test_recoleccion.py"""
import os, sys, json
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'recoleccion'))
import armar_entrada as A, ficha as FI, puntuar as PU

ok = 0
def check(c, m):
    global ok
    assert c, m
    ok += 1
    print('✓', m)

b = json.load(open(os.path.join(RAIZ, 'jornadas', '2026-11-12', 'betano', 'italia-francia.json'), encoding='utf8'))
fs = json.load(open(os.path.join(RAIZ, 'pruebas', 'fixtures', 'flashscore_italia_francia.json'), encoding='utf8'))
e = A.armar(b, fs, None)
check(e['local'] == 'Italia' and e['fecha'] == '2026-11-12 14:45', 'la hora UTC de Betano pasa a hora de Bogotá')
check(len(e['ficha']['forma']['local']) == 7 and e['ficha']['forma']['local'][0]['stats']['g'] == [3, 1] and e['ficha']['forma']['local'][0]['v'] == 'H', 'forma: 7 partidos, goles y sede')
check(len(e['ficha']['h2h']) == 3 and all('c' in d['stats'] or 'y' in d['stats'] for d in e['ficha']['h2h']), 'directos: solo los de los últimos 5 años y con alguna estadística (7 → 3)')
check(e['ficha']['arbitro']['nombre'] == 'Kovacs I.' and e['ficha']['arbitro']['tarjetas_por_partido'] is None, 'árbitro anunciado, sin inventar su promedio')
F = FI.construir(e)
check(F['corners']['esperado'] == {'local': 4.14, 'visitante': 5.93, 'total': 10.07}, 'Flashscore da el mismo esperado de córners que la fuente anterior (10.07)')
check(F['corners']['n_directos'] == 3, 'los directos recientes entran a la ficha (3 con córners)')
r = PU.evaluar(e)
check(r['estado'] == 'reserva' and r['situacion'] is None and 'situación sin leer' in r['motivos'], 'sin lectura de situación → reserva, no apto en silencio')
check(r['mercados']['jugadores']['estado'] == 'no apto', 'sin historial ni alineación el mercado de jugadores no es apto')
notas = {'importancia': 'alta', 'local': {'necesita_ganar': True}, 'visitante': {}}
r2 = PU.evaluar(A.armar(b, fs, notas))
check(r2['situacion'] is not None and r2['situacion'] >= 45 and r2['estado'] == 'apto', 'con la situación leída y datos suficientes → apto')
sin = A.armar(b, None, None)
check(len(sin['ficha']['forma']['local']) == 0 and any('Flashscore' in x for x in sin['ficha']['faltan']), 'sin Flashscore se declara lo que falta')

# --- directos viejos y alineaciones probables de Flashscore ---
dd = A.h2h_de([{'fecha': '2026-10-01', 'g': [1, 0], 'stats': {'c': [3, 4]}}, {'fecha': '2013-09-10', 'g': [1, 0], 'stats': {'c': [5, 4]}}], '2026-11-13')
check(len(dd) == 1 and dd[0]['fecha'] == '2026-10-01', 'los directos de más de 5 años no cuentan')
check(A.coincide('Verbruggen B.', 'Bart Verbruggen') and A.coincide('van Hecke J. P.', 'Jan Paul van Hecke') and not A.coincide('Pavlović A.', 'Strahinja Pavlović'), 'nombres de Flashscore ↔ Betano (apellido + inicial)')
lu = {'tipo': 'Alineaciones probables', 'probables': {'L': [{'n': 'Malen D.'}], 'V': [{'n': 'Pavlidis V.'}]}, 'bajas': {'L': [{'n': 'Gakpo C.', 'motivo': 'Lesión'}], 'V': []}}
bet = {'jugadores': [{'jugador': 'Donyell Malen', 'lado': 'local'}, {'jugador': 'Vangelis Pavlidis', 'lado': 'visitante'}, {'jugador': 'Cody Gakpo', 'lado': 'local'}]}
jj, sin = A.jugadores_de(lu, bet, '12-nov 13:00')
check({j['nombre'] for j in jj if not j.get('fuera')} == {'Donyell Malen', 'Vangelis Pavlidis'} and any(j['nombre'] == 'Cody Gakpo' and j.get('fuera') for j in jj) and not sin, 'la alineación probable marca titulares y bajas')
print(f'\n{ok} pruebas de recolección superadas')
