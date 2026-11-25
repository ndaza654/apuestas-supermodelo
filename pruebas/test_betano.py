# -*- coding: utf-8 -*-
"""Pruebas del conversor Betano (texto compacto → JSON). Ejecutar: python3 pruebas/test_betano.py"""
import os, sys, json, tempfile
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'recoleccion'))
import betano as BE

ok = 0
def check(c, m):
    global ok
    assert c, m
    ok += 1
    print('✓', m)

TXT = """E|Italia - Francia|2026-11-12T19:45:00.000Z|94654134|UEFA|Liga de Naciones|n=579|leido=2026-11-12T17:00:02.339Z
L|corners|total|4.5:1.03/10.25 8.5:1.55/2.35 9.5:-/1.82
L|goles|1T|0.5:1.34/3.2 0.75:1.45/2.77
U|MRES|1=3.55;X=3.6;2=2.02
U|DBLC|L o Empate=1.82;V o Empate=1.32;L o V=1.28
U|BTSC|Sí=1.55;No=2.35
U|HTFT|1/1=5.9;1/X=13.5;1/2=23;X/1=8;X/X=5.6;X/2=5.2;2/1=35;2/X=13.5;2/2=3.15
U|FHMR|-1=7.7/-1=5.2/1=1.32;1=1.82/1=3.9/-1=3.65
U|AHRF|L -0.5@-0.5=2.1;V +0.5@0.5=1.74;L 0.0@0=2.65;V 0.0@0=1.52
P|Pio Esposito|L|an=2.95|aoa=2.5|tj=4.4|sh=2:1.25,3:1.8|sot=1:1.25,2:2.15
P|Mike Maignan|V|tj=7.5|sv=2:1.23,3:1.75
P|Sin Goles|?|an=10.75
R|anota|Pio Esposito o Bradley Barcola=1.7;Bradley Barcola o Michael Olise=1.72
"""
meta, b = BE.parse_texto(TXT)
check(meta['local'] == 'Italia' and meta['visitante'] == 'Francia' and meta['betano_id'] == '94654134' and meta['n_mercados'] == 579, 'encabezado del partido')
check(len(b['lineas']) == 5 and {'mercado': 'corners', 'ambito': 'total', 'linea': 9.5, 'mas': None, 'menos': 1.82} in b['lineas'], 'líneas Más/Menos; un lado ausente queda en None')
res = [u for u in b['unicos'] if u['mercado'] == 'resultado'][0]['opciones']
check(res['1'] == 3.55 and res['1X'] == 1.82 and res['12'] == 1.28 and b['unicos'][0]['mercado'] == 'resultado', 'resultado 1X2 y doble oportunidad juntos, primero')
check([u for u in b['unicos'] if u['mercado'] == 'htft'][0]['opciones']['2/2'] == 3.15, 'descanso/final en orden 1/1…2/2')
hand = sorted(u['h'] for u in b['unicos'] if u['mercado'] == 'handicap')
check(-1.0 in hand and 1.0 in hand and -0.5 in hand and 0.0 in hand, 'hándicap europeo y asiático')
pj = {(j['jugador'], j['stat']): j for j in b['jugadores']}
check(pj[('Pio Esposito', 'remates')]['escalera'] == {2: 1.25, 3: 1.8} and pj[('Pio Esposito', 'anota')]['cuota'] == 2.95, 'jugador: escalera y cuotas simples')
check(pj[('Mike Maignan', 'atajadas')]['lado'] == 'visitante' and ('Sin Goles', 'anota') not in pj, 'lado por L/V y se ignora «Sin Goles»')
check(b['parejas'][0] == {'jugadores': ['Pio Esposito', 'Bradley Barcola'], 'stat': 'anota', 'cuota': 1.7}, 'parejas «cualquiera de los jugadores»')
check(BE.clave(meta) == 'italia-francia', 'clave del partido')

# el texto real guardado de la jornada se convierte igual que antes
raw = os.path.join(os.path.dirname(AQUI), 'jornadas', '2026-11-12', 'raw', 'bet_italia-francia.txt')
if os.path.exists(raw):
    with tempfile.TemporaryDirectory() as d:
        k, m2, b2, dest = BE.convertir(raw, d)
        prev = json.load(open(os.path.join(os.path.dirname(AQUI), 'jornadas', '2026-11-12', 'betano', 'italia-francia.json')))
        check(k == 'italia-francia' and json.load(open(dest)) == prev, 'texto real de la jornada → mismo JSON que ya usaba el modelo')
        check(len(b2['lineas']) == 119 and len({j['jugador'] for j in b2['jugadores']}) == 49 and len(b2['parejas']) == 56, 'Italia–Francia: 119 líneas, 49 jugadores, 56 parejas')

# 25-nov-2026: ERROR de las tablas de jugadores (Betano las entrega como una tabla con todos los jugadores a nombre del primero; antes se pegaban las 39 escaleras en uno)
import subprocess, shutil
check(BE.escalera_invalida([(1, 1.5), (2, 3.0), (3, 8.0)]) is None and BE.escalera_invalida([(5, 1.45), (6, 1.93)]) is None, 'escalera real (líneas crecientes, cuota que sube) se acepta')
check(BE.escalera_invalida([(6, 1.55), (7, 2.05), (1, 3.2), (2, 13.0), (1, 1.5)]) and BE.escalera_invalida([(1, 2.0), (2, 1.5)]), 'escalera con líneas repetidas (tabla pegada) o con cuota que baja se rechaza')
_txt = 'E|A - B|2026-11-25T20:00:00.000Z|1|R|L|n=1|leido=x\nP|Julián Álvarez|L|an=1.65|sh=6:1.55,7:2.05,1:3.2,2:13,3:23,1:1.5,2:4\nP|Otro|L|sh=2:1.3,3:1.9'
_m, _b = BE.parse_texto(_txt)
_pj = {(j['jugador'], j['stat']): j for j in _b['jugadores']}
check(('Julián Álvarez', 'remates') not in _pj and ('Julián Álvarez', 'anota') in _pj and _pj[('Otro', 'remates')]['escalera'] == {2: 1.3, 3: 1.9} and len(_b['avisos']) == 1, 'betano.py: la escalera contaminada se descarta, lo demás del jugador queda y se avisa')
if shutil.which('node'):
    _o = subprocess.run(['node', os.path.join(AQUI, 'extraer_betano_fixture.js')], capture_output=True, text=True, encoding='utf8')
    _m2, _b2 = BE.parse_texto(_o.stdout)
    _q = {(j['jugador'], j['stat']): j['escalera'] for j in _b2['jugadores'] if 'escalera' in j}
    check(_q.get(('Julián Álvarez', 'remates')) == {5: 1.45, 6: 1.93, 7: 2.77}, 'extractor: la tabla de remates da a Álvarez SOLO su fila (5+, 6+, 7+), no las de los otros 38 jugadores')
    check(_q.get(('Defensa Raro', 'remates')) == {1: 3.2, 2: 13.0, 3: 23.0} and _q.get(('Portero Dos', 'atajadas')) == {2: 1.5, 3: 2.3}, 'extractor: los demás jugadores de la tabla salen con su propia escalera (la cuota 1+ a 3,20 es de quien la ofrece)')
    check(('Mal Ordenado', 'al_arco') not in _q and 'descartada' in _o.stdout + 'descartada', 'extractor: una escalera con cuota que baja se descarta')
print(f'\n{ok} pruebas del conversor superadas')
