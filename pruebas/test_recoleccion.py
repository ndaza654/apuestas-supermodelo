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

# --- historial por jugador (Flashscore) y baja que contradice el XI ---
lu2 = {'tipo': 'Alineaciones probables', 'probables': {'L': [{'n': 'Malen D.'}, {'n': 'Gakpo C.'}], 'V': []}, 'bajas': {'L': [{'n': 'Gakpo C.', 'motivo': 'Lesión'}], 'V': []}}
jj2, _ = A.jugadores_de(lu2, bet, '')
check(len([j for j in jj2 if j['nombre'] == 'Cody Gakpo']) == 1 and next(j for j in jj2 if j['nombre'] == 'Cody Gakpo').get('fuera') and next(j for j in jj2 if j['nombre'] == 'Cody Gakpo').get('conflicto_xi'), 'si un jugador sale en el XI y en bajas, manda la baja')
hist, sin_h = A.hist_de({'Malen D.': {'pos': 'Extremo', 'p': [['m1', '2026-10-01', 72, 2, 0, 0, 0, 1, 0, 3, 1]]}, 'Nadie X.': {'pos': None, 'p': [['m2', '2026-10-01', 90, 0, 0, 0, 0, 0, 0, 0, 0]]}}, bet)
pp = hist['Donyell Malen']['partidos'][0]
check(pp['min'] == 72 and pp['remates'] == 2 and pp['tarjeta'] == 1 and pp['faltas'] == 3 and sin_h == ['Nadie X.'], 'el historial de Flashscore pasa a ficha.jugadores_hist con nombres de Betano')

# --- el puntaje de jugadores cuenta todas las líneas (no solo remates/tiros al arco) ---
# (datos del 13-nov recogidos con muestra de 7: con la regla de 10 ya casi ninguna línea llega a cumplir; solo se exige que cuenten)
for clave, minimo in (('eslovenia-suiza', 0), ('serbia-alemania', 0)):
    ej = json.load(open(os.path.join(RAIZ, 'jornadas', '2026-11-13', 'entradas', clave + '.json'), encoding='utf8'))
    rj = PU.evaluar(ej)
    check(rj['mercados']['jugadores']['estado'] != 'no ofrece' and rj['mercados']['jugadores']['datos'] > 0 and rj['mercados']['jugadores']['cumplen'] >= minimo, f'{clave}: los jugadores con línea de anota/asiste/tarjeta/entradas/faltas cuentan en el puntaje')
# --- registro de líneas (ficha + modelo en la misma fila) ---
import tempfile, csv as _csv
import registrar_jornada as RJ
_jor = os.path.join(RAIZ, 'jornadas', '2026-11-13')
_tmp = os.path.join(tempfile.mkdtemp(), 'lineas.csv')
n1, _ = RJ.registrar(_jor, _tmp)
n2, prev2 = RJ.registrar(_jor, _tmp)
check(n1 == n2 and prev2 == 0 and n1 > 1000, 'registrar dos veces la misma jornada reemplaza sus filas (no duplica)')
_R = list(_csv.DictReader(open(_tmp, encoding='utf-8-sig'), delimiter=';'))
_f = [r for r in _R if r['partido'] == 'Países Bajos - Grecia' and r['mercado'] == 'corners' and r['ambito'] == 'total' and r['linea'] == '6.5' and r['lado'] == 'Más'][0]
check(_f['cumple_ficha'] == 'sí' and _f['reg_local'] == '7 de 7' and _f['p_modelo'] != '' and float(_f['cuota']) > 1.0,'cada fila trae la lectura de la ficha y la del modelo a la vez')
check(all(r['cumple_ficha'] == '' for r in _R if r['ambito'] in ('1T', '2T') and not r['mercado'].startswith('jugador')), 'las líneas 1T/2T no llevan «cumple» (sin estadística por tiempo)')
check(all(r['resultado'] == '' and r['apostada'] == '' for r in _R), 'las columnas de resultado quedan vacías para el agente de calificación')
check(any(r['cumple_ficha'] == 'sin alineación' for r in _R if r['mercado'].startswith('jugador')), 'jugadores sin alineación quedan marcados, no como «no cumple»')

# --- alineaciones / clima / clasificación recolectados el 13-nov para el 14-nov ---
_j14 = os.path.join(RAIZ, 'jornadas', '2026-11-14')
_al = json.load(open(os.path.join(_j14, 'alineaciones', 'noruega-gales.json'), encoding='utf8'))
_lu = A.lineups_de(_al)
check(len(_lu['probables']['L']) == 11 and _lu['probables']['L'][0]['gk'] and _lu['probables']['L'][9]['n'] == 'Haaland E.' and _lu['bajas']['V'][1]['motivo'] == 'Tarjetas amarillas', 'alineaciones compactas → la forma que lee jugadores_de (XI, arquero, bajas con motivo)')
check(A.lineups_de(json.load(open(os.path.join(_j14, 'alineaciones', 'millonarios-fc-alianza-fc.json'), encoding='utf8'))) is None, 'partido sin pestaña de alineaciones en Flashscore → None (no se inventa XI)')
_cs = json.load(open(os.path.join(_j14, 'clasificacion', 'clasificacion.json'), encoding='utf8'))
_fq = A.fila_de(_cs['tablas']['T8'], 'Querétaro')
check(_fq['pos'] == 12 and _fq['pts'] == 20 and _fq['pj'] == 15 and _fq['dg'] == -5, 'fila de la tabla: Querétaro 12.º, 20 pts en 15 PJ')
check(A.fila_de(_cs['tablas']['T1'], 'Sporting de Gijón')['pos'] == 7 and A.fila_de(_cs['tablas']['T1'], 'Real Madrid') is None, 'Sporting de Gijón ↔ «Real Sporting» por palabra distintiva; «Real» solo no basta')
check(A.fila_de(_cs['tablas']['T8'], 'Equipo Que No Existe') is None, 'un equipo que no casa con la tabla da None (no se adivina)')
_cl = json.load(open(os.path.join(_j14, 'clima', 'clima.json'), encoding='utf8'))
_c = A.clima_de(_cl['kosovo-israel'])
check(_c['temperatura'] == 3.4 and _c['lluvia'] is None and not _c['viento_fuerte'] and 'Open-Meteo' in _c['texto'], 'clima: temperatura al inicio; lluvia/viento «fuerte» solo por umbral fijo (7,6 mm/h, 30 km/h)')

# --- informe interactivo de la jornada (recoleccion/informe_html.py) ---
import informe_html as IH
_j, _f, _rk, _res, _es = IH.cargar(os.path.join(RAIZ, 'jornadas', '2026-11-13'))
_d = IH.datos(_j, _f, _rk, _res, _es)
check(len(_d['P']) >= 3 and len(_d['F']) == len(_f) and all(len(x) == 20 for x in _d['F']), 'el informe HTML recibe todas las líneas del registro (nada se filtra por colchón) con 20 campos')
_h = IH.PLANTILLA.replace('/*DATA*/', json.dumps(_d, ensure_ascii=False))
check('constD={' in _h.replace(' ', '') and 'el informe no apuesta' in _h, 'el HTML es autónomo (datos incrustados, sin recursos externos) y declara que no apuesta')
check('http://' not in IH.PLANTILLA.replace('http://www.w3.org', '') and 'https://' not in IH.PLANTILLA, 'el HTML no pide nada a la red')
check(_d['N'] >= 1 and 1 <= _d['K'] <= _d['N'] and 1 <= _d['MN'] <= _d['N'], f"el informe trae N={_d['N']}, K={_d['K']}, n mínimo={_d['MN']} según la muestra real de la jornada")
check("id=\"kbar\"" in IH.PLANTILLA and 'function cum(' in IH.PLANTILLA and 'data-k=' in IH.PLANTILLA, 'el informe trae la barra para cambiar el mínimo de «cumple» (K de N) y recalcula con ella')

# --- calificador de líneas y balance ---
import calificar_lineas as CL, balance_html as BH
check(CL.calificar(3, 2.5, 'Más') == 'cumplió' and CL.calificar(2, 2.0, 'Más') == 'nula' and CL.calificar(2, 2.25, 'Más') == 'media perdida' and CL.calificar(2, 2.75, 'Menos') == 'cumplió' and CL.calificar(2, 2.25, 'Menos') == 'media ganada', 'calificar: líneas enteras (nula), .5 y asiáticas (.25/.75 = dos medias líneas)')
check(CL.valor({'g': [1, 2], 'g1': [0, 1], 'y': [2, 3]}, 'goles', '2T') == 2 and CL.valor({'g': [1, 2]}, 'goles', '1T') is None and CL.valor({'y': [2, 3]}, 'tarjetas', 'visitante') == 3, 'calificar: 2T = total − 1T; sin dato por tiempo no se inventa')
check('function cum(' in BH.PLANTILLA and 'id="kbar"' in BH.PLANTILLA and 'https://' not in BH.PLANTILLA, 'el balance HTML trae el filtro K de N y no pide nada a la red')

import calificar_jugadores as CJ
_pl = {'Andy Robertson': ['h', 90], 'Ben Gannon-Doak': ['h', 76], 'Che Adams': ['h', 67], 'Srđan Babić': ['h', 90]}
check(CJ.casar('Andrew Robertson', _pl) == 'Andy Robertson' and CJ.casar('Ben Doak', _pl) == 'Ben Gannon-Doak' and CJ.casar('Ché Adams', _pl) == 'Che Adams' and CJ.casar('Srdjan Babic', _pl) == 'Srđan Babić', 'jugadores: casa nombres Betano↔Sofascore sin tildes ni apodos')
check(CJ.casar('Scott Bain', _pl) is None, 'jugadores: quien no figura con minutos no se casa con otro (jugador que no jugó)')
_f = ['h', 90, 3, 1, 1, 2, 4, 1, 2, 0]
check(CJ.valor(_f + [1, 0], 'tarjeta', False) == 1 and CJ.valor(_f + [0, 1], 'tarjeta', False) == 1 and CJ.valor(_f + [0, 0], 'tarjeta', False) == 0, 'jugadores: tarjeta también sale de las columnas amarillas/rojas de la fila (txt de Flashscore sin «@»)')
check(CJ.valor(_f, 'anota_o_asiste', False) == 3 and CJ.valor(_f, 'remates', False) == 3 and CJ.valor(_f, 'tarjeta', True) == 1 and CJ.valor(_f, 'tarjeta', False) == 0, 'jugadores: «N o más»; anota_o_asiste suma goles y asistencias; tarjeta sale de los incidentes')

# --- auditoría de sugerencias ---
import csv as _csv, json as _json, auditoria_html as AH
_S = list(_csv.DictReader(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'registro', 'sugerencias.csv'), encoding='utf-8-sig'), delimiter=';'))
check(len(_S) > 300 and len({r['id'] for r in _S}) == len(_S), 'sugerencias: ids únicos y más de 300 filas')
check(all(len(_json.loads(r['patas_json'])) == int(r['n_patas']) for r in _S if r['patas_json'] and not r['entrega'].startswith('4')), 'sugerencias: n_patas coincide con las patas guardadas')
check(all(r['resultado'] != 'cumplió' or 'F' not in [l[2] for l in _json.loads(r['patas_json'])] for r in _S if r['patas_json']), 'sugerencias: una combinada «cumplió» no puede tener una pata fallada')
check('https://' not in AH.PLANTILLA and 'id="flt"' in AH.PLANTILLA, 'auditoría HTML: autónoma (sin red) y con filtros')

# --- análisis de la jornada con las reglas de la auditoría (recoleccion/analisis_jornada.py) ---
import analisis_jornada as AJ
def _l(m, lado, cuota, p, res, cumple='sí', partido='A - B', jor='2026-01-01'):
    return {'jornada': jor, 'partido': partido, 'mercado': m, 'lado': lado, 'cuota': str(cuota), 'p_modelo': str(p), 'resultado': res, 'cumple_ficha': cumple}
_H = [_l('corners', 'Más', 1.25, 0.8, 'cumplió')] * 12 + [_l('corners', 'Más', 1.25, 0.8, 'falló')] * 8 + [_l('goles', 'Menos', 1.4, 0.7, 'cumplió')] * 7 + [_l('goles', 'Menos', 1.4, 0.7, 'falló')] * 3
_R = AJ.real_hasta_hoy(_H, [{'n_patas': '1', 'tipo': 'sencilla', 'cuota': '1.4', 'p_estimada': '0.8', 'resultado': 'cumplió'}, {'n_patas': '2', 'tipo': 'combinada mismo partido', 'cuota': '2', 'p_estimada': '0.5', 'resultado': 'falló'}])
check(_R['mercado_lado']['corners|Más']['aciertos'] == 12 and _R['mercado_lado']['corners|Más']['real'] == 0.6 and _R['mercado_lado']['corners|Más']['factor'] < 0.9,
      'análisis: «real hasta hoy» por mercado y lado (12 de 20 = 60 % contra 80 % dicho -> factor < 1)')
check(_R['mercado_lado']['goles|Menos']['factor'] <= 1.0 and all(v['factor'] <= 1.0 for v in _R['banda_cuota'].values()), 'análisis: ningún factor sube la p del modelo')
check(_R['sugerencias']['sencillas']['n'] == 1 and _R['sugerencias']['combinadas de 2 patas (todas)']['real'] == 0.0, 'análisis: auditoría de sugerencias por tipo y número de patas')
_f, _t = AJ.recorte(_R, 'corners', 'Más', 1.25)
check(_f < 1 and '12 de 20' in _t and AJ.recorte(_R, 'faltas', 'Más', 1.25)[0] <= 1 and 'sin líneas calificadas' in AJ.recorte(_R, 'faltas', 'Más', 1.25)[1],
      'análisis: la p se recorta con el factor real y se dice cuándo no hay líneas calificadas')
_Jx = [{'jornada': 'x', 'partido': 'A - B', 'hora_partido': '2026-01-02 10:00', 'mercado': 'corners', 'ambito': 'total', 'jugador': '', 'linea': str(l), 'lado': 'Menos', 'cuota': str(c), 'p_modelo': str(pm),
        'p_mercado': str(pm), 'ev_modelo': '-0.03', 'esperado': '8', 'colchon': '2', 'reg_local': '6 de 7', 'reg_visitante': '5 de 7', 'directos': d, 'cumple_ficha': k, 'alerta_modelo': ''}
       for l, c, pm, d, k in ((12.5, 1.10, 0.95, '3 de 3', 'sí'), (11.5, 1.25, 0.90, '0 de 4', 'sí'), (10.5, 1.60, 0.70, '', 'sí'), (9.5, 1.9, 0.5, '', 'no'))]
_C = AJ.candidatas(_Jx, _R)
_pr, _se = AJ.sencillas(_C)
check(len(_C) == 3 and all(c['p_rec'] <= c['p'] for c in _C), 'análisis: solo entran líneas con «cumple» y la p recortada nunca supera la del modelo')
check([c['linea'] for c in _pr] == [11.5] and [c['linea'] for c in _se] == [10.5], 'análisis: de cada escalera una protección (la de mayor cuota con p recortada ≥ 70 %) y una sencilla 1,50–1,99')
check('directos en contra (0 de 4)' in _pr[0]['real'], 'análisis: avisa cuando los directos dicen lo contrario (no excluye la línea)')
check(len(AJ.sencillas(AJ.candidatas([{**_Jx[1], 'mercado': 'tarjetas'}], _R))[0]) == 1, 'análisis: tarjetas entra en sugerencias como cualquier mercado (desde el 16-nov)')
check(all('hist_sem' in c for c in _C), 'análisis: cada línea trae la segunda opinión histórica (semáforo; no recorta p)')
check(AJ.loteria(_pr) is None, 'análisis: sin tres partidos distintos no hay lotería')
check('<h3>Título</h3>' in IH._md('## Título\n- uno **dos**\ntexto <b>') and '<li>uno <b>dos</b></li>' in IH._md('- uno **dos**') and '&lt;b&gt;' in IH._md('texto <b>'),
      'informe: el enfoque en markdown se convierte a HTML escapado')
check("['ana','Análisis']" in IH.PLANTILLA and 'function vAna(' in IH.PLANTILLA and 'Enfoque de mercados' in IH.PLANTILLA, 'informe: la pestaña «Análisis» abre con «Enfoque de mercados»')
_dA = dict(_d); _dA['A'] = IH.analisis(os.path.join(RAIZ, 'jornadas', '2026-11-13'), _d)
check(_dA['A'] is None, 'informe: sin analisis.json la jornada no muestra la pestaña «Análisis» (y sigue funcionando)')
import sugerencias as _SG
check("res = 'pendiente'" in open(_SG.__file__, encoding='utf8').read() and all(r['resultado'] == 'pendiente' or r['fecha_entrega'] < '2026-11-14' or r['resultado'] in ('cumplió', 'falló', 'parcial', 'anulada') for r in _S),
      'sugerencias: las registradas antes del partido quedan «pendiente» hasta que la línea tenga resultado')

import segundo_paso as _SP
_rr = {'p_mercado': '0.6', 'p_modelo': '0.62', 'colchon': '1.5', 'linea': '9.5', 'cumple_ficha': 'sí', 'reg_local': '8 de 10', 'reg_visitante': '7 de 10', 'lado': 'Menos'}
check(len(_SP._feat(_rr, 0)) == 1 and len(_SP._feat(_rr, 1)) == 7 and len(_SP._feat(_rr, 2)) == 8 and _SP._x('sin dato') == (0.5, 0), 'segundo paso: variables de la validación (precio, cumple X de N, colchón, lado, modelo)')

print(f'\n{ok} pruebas de recolección superadas')
