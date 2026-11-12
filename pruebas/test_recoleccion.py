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
check(len(e['ficha']['h2h']) == 6 and all('c' in d['stats'] or 'y' in d['stats'] for d in e['ficha']['h2h']), 'directos: solo los que traen alguna estadística')
check(e['ficha']['arbitro']['nombre'] == 'Kovacs I.' and e['ficha']['arbitro']['tarjetas_por_partido'] is None, 'árbitro anunciado, sin inventar su promedio')
F = FI.construir(e)
check(F['corners']['esperado'] == {'local': 4.14, 'visitante': 5.93, 'total': 10.07}, 'Flashscore da el mismo esperado de córners que la fuente anterior (10.07)')
check(F['corners']['n_directos'] == 5, 'los directos entran a la ficha (5 con córners)')
r = PU.evaluar(e)
check(r['estado'] == 'reserva' and r['situacion'] is None and 'situación sin leer' in r['motivos'], 'sin lectura de situación → reserva, no apto en silencio')
check(r['mercados']['jugadores']['estado'] == 'no apto', 'sin historial ni alineación el mercado de jugadores no es apto')
notas = {'importancia': 'alta', 'local': {'necesita_ganar': True}, 'visitante': {}}
r2 = PU.evaluar(A.armar(b, fs, notas))
check(r2['situacion'] is not None and r2['situacion'] >= 45 and r2['estado'] == 'apto', 'con la situación leída y datos suficientes → apto')
sin = A.armar(b, None, None)
check(len(sin['ficha']['forma']['local']) == 0 and any('Flashscore' in x for x in sin['ficha']['faltan']), 'sin Flashscore se declara lo que falta')
print(f'\n{ok} pruebas de recolección superadas')
