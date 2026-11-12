# -*- coding: utf-8 -*-
"""Pruebas automáticas del supermodelo. Ejecutar: python3 pruebas/test_modelo.py
Las bandas de las pruebas de calibración salen de los 62 000 partidos reales (ver docs/MAPA_DE_ORIGEN.md)."""
import sys, os, tempfile, json, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from supermodelo import mercado as MK, mercados as MS, registro as RG, ligas, sistemas, dependencia as DEP, combos as CB
from supermodelo.simulador import Partido
from supermodelo.contexto import traducir
from supermodelo.analizar import analizar
from supermodelo.reporte import markdown

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBJ = [dict(g=1.6, sh=15, sot=5.2, c=5.8, f=11, y=1.9), dict(g=1.0, sh=11, sot=3.6, c=4.2, f=12.5, y=2.2)]
ok = 0
def check(cond, msg):
    global ok
    assert cond, msg
    ok += 1
    print('✓', msg)

# ------------------------------------------------------------------ fórmulas y precio
check(abs(MK.devig(1.9, 1.9) - 0.5) < 1e-9, 'sin margen: cuotas iguales = 50 %')
check(abs(sum(MK.devig_n([2.1, 3.4, 3.6])) - 1) < 1e-9, 'sin margen 1X2 suma 100 %')
check(MK.devig(1.25, 3.9) > MK.devig(1.25, 3.9, 'proporcional') + 0.01,
      'método de potencia: el favorito queda más probable que con el reparto proporcional (sesgo favorito–longshot)')
check(abs(MK.devig_n([2.0, 2.0], 'potencia')[0] - 0.5) < 1e-9 and abs(sum(MK.devig_n([1.4, 4.5, 8.0])) - 1) < 1e-9, 'potencia: simétrico y suma 100 %')
check(MK.cuota_minima(0.6) > 1 / 0.6, 'cuota mínima por encima de la justa')
check(abs(MK.ev(0.5, 2.0)) < 1e-12, 'EV de una apuesta justa = 0')

# ------------------------------------------------------------------ simulador: medias
P = Partido(OBJ, n=15000)
R = P.res
for l in (0, 1):
    for s in ('g', 'sh', 'sot', 'c', 'f'):
        m = R[l][s].mean()
        check(abs(m / OBJ[l][s] - 1) < 0.05, f'calibración: media simulada de {s} (lado {l}) ≈ objetivo ({m:.2f} vs {OBJ[l][s]})')
    t = R[l]['tarjetas'].mean()
    check(abs(t / OBJ[l]['y'] - 1) < 0.06, f'calibración: tarjetas en puntos de Betano (lado {l}) ≈ objetivo ({t:.2f} vs {OBJ[l]["y"]})')
check(np.array_equal(R[0]['tarjetas'], R[0]['y'] + R[0]['r'] + R[0]['rd']), 'tarjetas = amarillas + rojas + rojas directas (directa = 2, doble amarilla = 3)')

# ------------------------------------------------------------------ simulador: forma, calibrada con 62 000 partidos
sh2 = lambda l: R[l]['sh'] - R[l]['sh1']
d_ht = R[0]['g1'] - R[1]['g1']
gana = d_ht > 0; pierde = d_ht < 0
share = lambda m: (sh2(0)[m] / np.maximum(sh2(0)[m] + sh2(1)[m], 1)).mean()
check(share(pierde) > share(gana) + 0.04, f'estado del partido: el local remata más en el 2T si va perdiendo ({share(pierde):.2f}) que si va ganando ({share(gana):.2f})')
tot_c = R[0]['c'] + R[1]['c']; tot_sh = R[0]['sh'] + R[1]['sh']
r_shc = np.corrcoef(tot_c, tot_sh)[0, 1]
check(0.15 < r_shc < 0.40, f'remates y córners correlacionados (sim {r_shc:.2f}; real 0,28)')
vm = tot_c.var() / tot_c.mean()
check(1.0 < vm < 1.30, f'dispersión de córners totales realista (var/media {vm:.2f}; real 1,11; el v2 daba 1,45)')
y = R[0]['tarjetas'] + R[1]['tarjetas']; d = np.abs(R[0]['g'] - R[1]['g'])
check(y[d <= 1].mean() > y[d >= 3].mean(), 'partido cerrado da más tarjetas que una goleada')
check(np.array_equal(R[0]['sv'], R[1]['sot'] - R[1]['g']), 'atajadas del portero = tiros al arco rivales − goles')
gh, ga = R[0]['g'], R[1]['g']
lh, la = gh.mean(), ga.mean()
pB_pois = (1 - np.exp(-lh)) * (1 - np.exp(-la))
pB = ((gh > 0) & (ga > 0)).mean()
check(pB > pB_pois + 0.008, f'Ambos Marcan por encima del Poisson independiente ({pB:.3f} vs {pB_pois:.3f}; real +2,25 pts en 76 000 partidos)')
from scipy.stats import poisson
K = np.arange(13); pX_pois = float(np.trace(np.outer(poisson.pmf(K, lh), poisson.pmf(K, la))))
check((gh == ga).mean() > pX_pois + 0.008, f'empate por encima del Poisson independiente ({(gh == ga).mean():.3f} vs {pX_pois:.3f}; real +1,9 pts)')
y1 = (R[0]['y1'] + R[1]['y1']).sum() / max((R[0]['y'] + R[1]['y']).sum(), 1)
check(0.28 < y1 < 0.40, f'tarjetas del 1.er tiempo ≈ un tercio (sim {y1:.2f}; la amarilla media llega al 59 % del partido)')
g1 = (R[0]['g1'] + R[1]['g1']).sum() / (gh + ga).sum()
check(0.42 < g1 < 0.47, f'goles del 1.er tiempo ≈ 44 % (sim {g1:.3f}; real 0,443)')
gd = gh - ga
r_sh = np.corrcoef(gd, R[0]['sh'] - R[1]['sh'])[0, 1]
r_sot = np.corrcoef(gd, R[0]['sot'] - R[1]['sot'])[0, 1]
check(0.05 < r_sh < 0.25, f'ganar y rematar más van juntos, pero poco (corr {r_sh:.2f}; real 0,14 en 62 000 partidos, no 0,34)')
check(r_sot > r_sh + 0.2, f'la relación es mucho más fuerte con los tiros al arco (corr {r_sot:.2f}; real 0,50)')
rc = np.corrcoef(R[0]['c'], R[1]['c'])[0, 1]
check(rc < -0.05, f'córners de un equipo y del otro se reparten el territorio (corr {rc:.2f}; real −0,18)')

# ------------------------------------------------------------------ contexto
aj = traducir({'derbi': True})
OBJ2 = [{k: v * aj.mult[l].get(k, 1) for k, v in OBJ[l].items()} for l in (0, 1)]
P2 = Partido(OBJ2, aj, n=12000)
y2 = (P2.res[0]['tarjetas'] + P2.res[1]['tarjetas']).mean()
check(y2 > y.mean() * 1.1, f'derbi sube las tarjetas ({y.mean():.2f} → {y2:.2f})')
aj = traducir({'eliminatoria': {'global_local': 0, 'global_visitante': 2}})
check(aj.offset_global == [-2, 2], 'eliminatoria: el local arranca dos goles abajo en el estado del partido')
a = traducir({'_liga': 'España LaLiga', 'arbitro': {'amarillas_por_partido': 5.6, 'rojas_por_partido': 0.3, 'partidos': 12}})
check(a.mult[0]['y'] > 1.0 and any('prior de la liga' in n for n in a.notas),
      'árbitro sin media de liga: usa la media verificada de la liga y convierte amarillas + rojas a puntos de Betano')
b = traducir({'bajas': [{'jugador': 'A', 'lado': 'local', 'posicion': 'delantero', 'peso': 0.3, 'reemplazo': 'suplente', 'horas_desde_noticia': 2}]})
c = traducir({'bajas': [{'jugador': 'A', 'lado': 'local', 'posicion': 'delantero', 'peso': 0.3, 'reemplazo': 'suplente', 'horas_desde_noticia': 48}]})
check(b.mult[0]['g'] < c.mult[0]['g'] < 1.0 and 'bajas' in b.frescos and 'bajas' not in c.frescos,
      'baja con noticia de <24 h va completa; la de >24 h solo en parte (ya está en la cuota)')
t = traducir({'info_tardia': [{'tipo': 'arbitro', 'hecho': 'cambio de árbitro', 'horas': 1}]})
check('arbitro' in t.frescos, 'información tardía marca su tipo como fresco')

# ------------------------------------------------------------------ builders y combos
e1 = MS.evento(R, dict(mercado='remates', ambito='local', lado='mas', linea=14.5))
e2 = MS.evento(R, dict(mercado='corners', ambito='local', lado='mas', linea=5.5))
check((e1 & e2).mean() > e1.mean() * e2.mean(), 'correlación positiva: remates y córners del mismo equipo')
f_, notas = DEP.factor([({'mercado': 'resultado', 'lado': '1'}, .5), ({'mercado': 'corners', 'ambito': 'local', 'lado': 'mas', 'linea': 5.5}, .5)], 0)
check(f_ < 0.97 and notas, f'dependencia real: «gana el favorito + sus córners Más» se estorban más de lo que da el simulador (×{f_:.3f})')
ent = dict(local='A', visitante='B', liga='Inglaterra · Premier League',
           betano={'lineas': [dict(mercado='corners', ambito='total', linea=9.5, mas=1.9, menos=1.9),
                              dict(mercado='goles', ambito='total', linea=2.5, mas=1.95, menos=1.85)],
                   'unicos': [dict(mercado='resultado', opciones={'1': 2.0, 'X': 3.4, '2': 3.9})]},
           ficha={'derbi': True})
A = analizar(ent, n=6000, devolver_sim=True)
S = A.pop('_S')
check(len(A['lineas']) == 7, 'el análisis evalúa ambos lados de cada línea y cada opción')
check(all(0 < r['p'] < 1 for r in A['lineas']), 'probabilidades válidas')
check(A.get('liga_base') and 'Premier' in A['liga_base'], 'el informe trae la base verificada de la liga')
cb = CB.evaluar(A, S, ['Gana A', 'Goles Más 2.5'], cuota=3.6)
check(cb['p_ajust'] <= min(cb['p_patas']) and cb['p_stress'] < cb['p_ajust'] and cb['estado'] in ('valor', 'justo', 'evitar'),
      f"combo: prob. ajustada ≤ la pata más baja, stress menor y estado ({cb['estado']}, EV {cb['ev_ajust'] * 100:+.0f} %)")
check(CB.evaluar(A, S, ['Pata que no existe']).get('error'), 'combo con una pata que no está en el análisis: avisa en vez de inventar')
cart = CB.cartera([dict(nombre='b1', _sels=[{'mercado': 'goles', 'lado': 'mas'}]), dict(nombre='b2', _sels=[{'mercado': 'ambos', 'lado': 'si'}])])
check(cart['aviso'] and 'muchos goles' in cart['aviso'], 'cartera: dos boletos que dependen de "muchos goles" cuentan como una apuesta repetida')

# ------------------------------------------------------------------ registro: guardar y cerrar solo
with tempfile.TemporaryDirectory() as tmp:
    ruta = os.path.join(tmp, 'reg.csv')
    RG.guardar(A, ruta, apostadas=['Gana A'], ficha=ent['ficha'], entrada=ent)
    filas = open(ruta, encoding='utf-8-sig').read().splitlines()
    check(len(filas) == 8, 'registro: una fila por línea más el encabezado')
    real = {'goles': [2, 1], 'goles_1t': [1, 0], 'corners': [6, 3], 'corners_1t': [3, 1], 'amarillas': [2, 2], 'rojas': [0, 0]}
    n_ok, n_sin = RG.cerrar(ruta, 'A - B', real, cierres={'Gana A': 1.85}, ruta_partidos=os.path.join(tmp, 'partidos.csv'))
    F = {r['seleccion']: r for r in csv.DictReader(open(ruta, encoding='utf-8-sig'), delimiter=';')}
    check(n_ok == 7 and F['Gana A']['resultado'] == '1' and F['Córners Menos 9.5']['resultado'] == '1' and F['Goles Más 2.5']['resultado'] == '1',
          'cierre automático: califica todas las líneas con las estadísticas reales')
    check(abs(float(F['Gana A']['clv']) - (2.0 / 1.85 - 1)) < 1e-3, 'cierre: anota la cuota de cierre y el CLV')
    check(os.path.exists(os.path.join(tmp, 'partidos.csv')), 'cierre: el partido queda en la base propia de la liga (partidos.csv)')
    from supermodelo.balance import balance
    txt = balance(ruta)
    check(all(f'## {k}.' in txt for k in range(1, 6)), 'balance: responde las 5 preguntas')

# ------------------------------------------------------------------ perfil de córners, etiquetas, sistemas, ligas
fa = traducir({'local': {'perfil_corners': {'centros_pj': 26, 'centros_media_liga': 17.7}}})
fb = traducir({'local': {'perfil_corners': {'centros_pj': 12, 'centros_media_liga': 17.7}}})
fn = traducir({'local': {'perfil_corners': {'centros_pj': 17.7, 'centros_media_liga': 17.7}}})
ma, mb, mn = fa.mult[0]['c'], fb.mult[0]['c'], fn.mult[0]['c']
check(ma > 1.0 > mb and abs(mn - 1) < 1e-9, 'muchos centros suben los córners propios, pocos los bajan, la media no cambia')
check(ma < 1.10, 'el efecto de centros respeta el tope (los centros ya están en el precio)')
ent2 = dict(local='A', visitante='B', betano={'unicos': [dict(mercado='resultado', opciones={'1': 1.40, 'X': 4.5, '2': 8.0})],
                                              'lineas': [dict(mercado='goles', ambito='total', linea=2.5, mas=1.40, menos=2.8),
                                                         dict(mercado='goles', ambito='1T', linea=1.5, mas=2.10, menos=1.7)]})
et = RG._etiquetas_precio(ent2, {'jugadores': [{'nombre': 'Estrella', 'popular': True}], 'local': {'propositivo': True}})
check({'precio:local<=1.50', 'precio:O2.5<=1.45', 'precio:1T_O1.5<=2.15', 'jugador_popular:Estrella', 'local:propositivo'} <= set(et),
      'el registro etiqueta precios del tipster, jugador popular y equipo propositivo para medirlos')
ids = {s['id'] for s in sistemas.evaluar(ent2)}
check({'IA400', 'IA453', 'IA313'} <= ids, f'sistemas: el partido cumple los filtros de Ingeniero Analista que aplican ({sorted(ids)})')
check(all('historial' in s for s in sistemas.evaluar(ent2)), 'cada sistema trae su historial con cuotas reales')
check(ligas.codigo('Inglaterra · Premier League') == 'E0' and ligas.codigo('LaLiga EA Sports') == 'SP1' and ligas.codigo('Ecuador · LigaPro') is None,
      'ligas: reconoce nombres de Betano/Flashscore y no inventa las que no están')

# ------------------------------------------------------------------ en vivo
Pv = Partido(OBJ, n=8000, estado={'mitad': 2, 'minuto': 80, 'goles': [2, 0], 'goles_1t': [1, 0]})
gv = Pv.res[0]['g'] - Pv.res[1]['g']
check((Pv.res[0]['g'] >= 2).all() and (gv > 0).mean() > 0.9, f'en vivo: 2-0 al 80′ → el local gana {(gv > 0).mean() * 100:.0f} % y nunca baja de los goles que lleva')
alto = Partido(OBJ, n=8000, estado={'mitad': 1, 'minuto': 30, 'goles': [0, 0], 'corners': [9, 5], 'remates': [12, 8]}).res
bajo = Partido(OBJ, n=8000, estado={'mitad': 1, 'minuto': 30, 'goles': [0, 0], 'corners': [1, 0], 'remates': [3, 1]}).res
ra = (alto[0]['c'] + alto[1]['c']).mean() - 14; rb = (bajo[0]['c'] + bajo[1]['c']).mean() - 1
check(ra > rb + 0.5, f'en vivo: con mucho ritmo en el 1T se esperan más córners en lo que falta ({ra:.1f} contra {rb:.1f})')

# ------------------------------------------------------------------ memoria propia
from supermodelo import memoria as MEM
check(any('Historial propio' in x for x in MEM.notas('goles', 'menos', 'goles total Menos', 2.0, 0.05)), 'memoria: avisa en grupo con historial en contra')
check(MEM.notas('goles', 'menos', 'goles total Menos', 2.0, 0.0) == [], 'memoria: no avisa si la línea no tiene valor')
check(MEM.notas('tarjetas', 'menos', 'tarjetas total Menos', 1.8, 0.05) == [], 'memoria: no avisa si el historial es normal')
check(any('contra el guion' in x for x in MEM.notas('remates', 'menos', 'remates favorito Menos', 2.2, 0.05)), 'memoria: Menos de volumen del favorito avisa')

# ------------------------------------------------------------------ hallazgos de la revisión independiente (10-nov)
X12 = {'mercado': 'resultado', 'opciones': {'1': 2.6, 'X': 3.2, '2': 2.8}}
G25 = {'mercado': 'goles', 'ambito': 'total', 'linea': 2.5, 'mas': 1.95, 'menos': 1.85}
plantilla = json.load(open(os.path.join(AQUI, 'ejemplos', 'ejemplo_supermodelo.json'), encoding='utf8'))['ficha']
plantilla = dict(plantilla, rachas={'local': {'btts_seguidos': None, 'victorias_seguidas': None}, 'visitante': {'btts_seguidos': None, 'victorias_seguidas': None}},
                 h2h_empates_ult5=None, eliminatoria={'global_local': None, 'global_visitante': None},
                 jugadores=[{'nombre': 'J', 'lado': 'local', 'titular': None, 'minutos': None}])
Ar = analizar(dict(local='A', visitante='B', betano={'unicos': [X12], 'lineas': [G25],
                                                    'jugadores': [{'jugador': 'J', 'lado': 'local', 'stat': 'remates', 'escalera': {'1': 1.3, '2': 2.0}}]},
                   ficha=plantilla), n=3000, builders=False)
check(len(Ar['lineas']) > 5, 'G1/G2/M10: la ficha con campos en null (rachas, titular, minutos, eliminatoria) no rompe el análisis')
Au = analizar(dict(local='A', visitante='B', betano={'lineas': [G25], 'unicos': [
    X12, {'mercado': 'ambos', 'opciones': {'si': 1.95, 'no': None}},
    {'mercado': 'resultado', 'opciones': {'1X': 1.30, 'X2': 1.40, '12': 1.25}}]}), n=3000, builders=False)
amb = next(r for r in Au['lineas'] if r['seleccion'] == 'Ambos marcan: Sí')
dob = next(r for r in Au['lineas'] if r['seleccion'] == 'A o empate')
check(amb['p_mercado'] < 0.55 and amb['ev'] < 0.10, f"G3: una opción sola no se trata como 100 % (Ambos Sí mercado {amb['p_mercado']:.2f})")
check(0.55 < dob['p_mercado'] < 0.70, f"G3: la doble oportunidad sale del 1X2 ({dob['p_mercado']:.2f}), no de normalizar 1X+X2+12")
mal = dict(local='A', visitante='B', betano={'unicos': [X12], 'lineas': [G25, {'mercado': 'remates', 'ambito': 'local', 'linea': 13.5, 'mas': 1.9, 'menos': 1.9},
                                                                          {'mercado': 'remates', 'ambito': 'visitante', 'linea': 10.5, 'mas': 1.9, 'menos': 1.9},
                                                                          {'mercado': 'remates', 'ambito': 'total', 'linea': 12.5, 'mas': 1.9, 'menos': 1.9}]},
           ficha={'frescos': ['clima'], 'clima': {'lluvia': 'fuerte'}})
Am = analizar(mal, n=3000, builders=False)
check(any('simulación sin contexto' in (r.get('alerta') or '') for r in Am['lineas'] if r['sel']['mercado'] == 'remates' and r['sel']['ambito'] == 'total'),
      'G4: un hecho fresco no apaga la alerta de una línea mal copiada')
H = dict(local='A', visitante='B', betano={'unicos': [X12, {'mercado': 'handicap', 'h': -1, 'opciones': {'local': 4.2, 'empate': 3.9, 'visitante': 1.55}}], 'lineas': [G25]})
Ah = analizar(H, n=6000, builders=False)
nombres = {r['seleccion']: r for r in Ah['lineas']}
check({'Hándicap A -1', 'Hándicap empate (A -1)', 'Hándicap B +1'} <= set(nombres), 'G5: hándicap europeo con nombres distintos para empate y visitante (+h)')
pe = nombres['Hándicap empate (A -1)']['p_simulacion']
check(0.10 < pe < 0.30, f'G5: «empate» del hándicap = ganar por exactamente 1 (sim {pe:.2f}), no la victoria visitante')
Aa = analizar(dict(local='A', visitante='B', betano={'unicos': [X12, {'mercado': 'handicap', 'h': 0, 'opciones': {'local': 1.9, 'visitante': 1.9}}],
                                                    'lineas': [G25, {'mercado': 'goles', 'ambito': 'total', 'linea': 2.0, 'mas': 1.70, 'menos': 2.10},
                                                               {'mercado': 'goles', 'ambito': 'total', 'linea': 2.25, 'mas': 1.85, 'menos': 1.95}]}), n=6000, builders=False)
g2m = next(r for r in Aa['lineas'] if r['seleccion'] == 'Goles Menos 2.0')
dnb = next(r for r in Aa['lineas'] if r['seleccion'] == 'Hándicap A +0')
check(g2m['asiatica'] and g2m['devolucion'] > 0.1 and abs(g2m['p'] - g2m['p_mercado']) < 0.08 and not g2m.get('alerta'),
      f"M7: línea entera con devolución ({g2m['devolucion'] * 100:.0f} %) sin alerta falsa (p {g2m['p']:.2f} vs mercado {g2m['p_mercado']:.2f})")
check(dnb['asiatica'] and dnb['devolucion'] > 0.15, 'M7/G5: hándicap asiático 0 (empate devuelve)')
check(any(r['seleccion'] == 'Goles Más 2.25' for r in Aa['lineas']), 'M7: línea de cuarto (2.25) evaluada como media y media')
A8 = analizar(dict(local='A', visitante='B', betano={'unicos': [X12], 'lineas': [G25, {'mercado': 'fueras', 'ambito': '1T', 'linea': 1.5, 'mas': 2.0, 'menos': 1.75},
                                                                                {'mercado': 'goles', 'ambito': 'total', 'linea': 3.5, 'menos': 1.30},
                                                                                {'mercado': 'corners', 'linea': 9.5, 'mas': 1.9, 'menos': 1.9}]}), n=3000, builders=False)
check(any('Fueras de lugar 1.er tiempo' in r['seleccion'] for r in A8['lineas']) and any(r['seleccion'] == 'Goles Menos 3.5' for r in A8['lineas']),
      'M8/M9/m4: fueras del 1T, línea solo con «menos» y línea sin ámbito no rompen')
A11 = analizar(dict(local='A', visitante='B', liga='Inglaterra · Premier League', betano={'unicos': [X12]}), n=4000, builders=False)
check(A11['lambdas_mercado'] and abs(A11['lambdas_mercado'][0] - A11['lambdas_mercado'][1]) < 0.3, 'M11: sin línea de goles, los goles se anclan igual al 1X2')
check(ligas.codigo('Austria Bundesliga') == 'AUT' and ligas.codigo('Rusia Premier League') == 'RUS' and ligas.codigo('Escocia League One') == 'SC2'
      and ligas.codigo('Egipto Premier League') is None and ligas.codigo('Brasil Serie A') == 'BRA' and ligas.codigo('Serie A') is None,
      'M1: el país manda (Austria, Rusia, Escocia, Egipto, Brasil, «Serie A» sola)')
check(ligas.clave('Ecuador LigaPro - Grupo descenso J6') == ligas.clave('Ecuador LigaPro - Grupo descenso J7'), 'M3: la base propia agrupa por liga sin jornada ni fase')
from supermodelo import memoria as _M
check(_M.nota_liga('Brasil Serie A') is None, 'M2: el aviso de Italia no cae en Brasil ni Ecuador')
with tempfile.TemporaryDirectory() as tmp:
    ruta = os.path.join(tmp, 'viejo.csv')
    with open(ruta, 'w', encoding='utf-8-sig', newline='') as f:
        f.write('fecha;partido;liga;tipo;guion_principal;familia;submercado;seleccion;cuota;p_mercado;p_sin_contexto;p;movimiento_contexto;robustez;etiqueta;hechos_contexto;apostada;stake;resultado;cuota_cierre\n')
        f.write('2026-11-01;X - Y;L;t;g;goles;goles total Más;Goles Más 2.5;1.9;0.5;0.5;0.52;0.02;0.5;Justa;;No;;;\n')
    falta = RG.guardar(A, ruta, apostadas=['gana a ', 'Pata inventada'])
    F = list(csv.DictReader(open(ruta, encoding='utf-8-sig'), delimiter=';'))
    check(F[0]['p'] == '0.52' and F[1]['seleccion'] and float(F[1]['p']) == A['lineas'][0]['p'],
          'M5: agregar a un registro viejo no corre las columnas')
    check(falta == ['Pata inventada'] and any(x['apostada'] == 'Sí' and x['seleccion'] == 'Gana A' for x in F),
          'M6: «--apostadas» ignora espacios/mayúsculas y avisa las que no existen')
    rp = os.path.join(tmp, 'p.csv')
    real = {'goles': [2, 1], 'goles_1t': [1, 0], 'corners': [6, 3], 'corners_1t': [3, 1], 'amarillas': [2, 2], 'rojas': [0, 0]}
    RG.cerrar(ruta, 'A - B', real, ruta_partidos=rp); RG.cerrar(ruta, 'A - B', real, ruta_partidos=rp)
    check(len(list(csv.DictReader(open(rp, encoding='utf-8-sig'), delimiter=';'))) == 1, 'M4: cerrar dos veces no duplica el partido en la base propia')
    rc = os.path.join(tmp, 'c.csv')
    RG.guardar(A, rc)
    cbr = CB.evaluar(A, S, ['Goles Más 2.5', 'Córners Menos 9.5'], cuota=3.0)
    RG.guardar_combo(rc, A, cbr, sels=[x['sel'] for x in A['lineas'] if x['seleccion'] in cbr['patas']])
    RG.cerrar(rc, 'A - B', real, ruta_partidos=rp)
    Fc = [x for x in csv.DictReader(open(rc, encoding='utf-8-sig'), delimiter=';') if x['familia'] == 'combo']
    check(Fc and Fc[0]['resultado'] == '1', 'M15: un combo guardado en el registro se califica con todas sus patas')
Pv2 = Partido(OBJ, n=4000, estado={'mitad': 2, 'minuto': 60, 'goles': [0, 0], 'goles_1t': [0, 0], 'rojas': [1, 0]})
check((Pv2.res[0]['tarjetas'] >= 2).all(), 'M12: en vivo, una roja sin «rojas_directas» cuenta 2 puntos')
from supermodelo.vivo import evaluar_vivo
Vv = evaluar_vivo(dict(local='A', visitante='B', betano={'unicos': [X12], 'lineas': [G25]}),
                  {'estado': {'mitad': 2, 'minuto': 60, 'goles': [1, 0]}, 'betano_vivo': {'lineas': [{'mercado': 'goles', 'ambito': '2T', 'linea': 0.5, 'mas': 1.5, 'menos': 2.5}]}}, n=3000)
check(Vv['avisos'] and all(x.get('aviso') for x in Vv['lineas']), 'M13: en vivo sin goles_1t avisa y marca las líneas de 2T')
check(CB.evaluar(A, S, ['goles mas 2,5', 'corners menos 9.5']).get('p_ajust') and CB.evaluar(A, S, ['Gana A', 'Gana A']).get('error'),
      'm1: combos encuentran patas sin tildes y con coma decimal, y rechazan patas repetidas')

mf = {m['mercado']: m for m in Vv['resumen']['medias_finales']}
check(mf['Goles']['jugado'] == 1 and mf['Goles']['final'] >= 1 and abs(mf['Goles']['final'] - 1 - mf['Goles']['restante']) < 0.11,
      'en vivo: media final esperada del partido = lo ya jugado + lo que falta')
# ------------------------------------------------------------------ medias esperadas e informe HTML
from supermodelo.reporte_html import html, lectura_par, veredicto
from supermodelo import proyeccion as PR
Mm = {(r['mercado'], r['ambito']): r for r in A['medias']}
check(abs(Mm[('goles', 'total')]['modelo'] - Mm[('goles', 'local')]['modelo'] - Mm[('goles', 'visitante')]['modelo']) < 0.02
      and abs(Mm[('corners', '1T')]['modelo'] + Mm[('corners', '2T')]['modelo'] - Mm[('corners', 'total')]['modelo']) < 0.02,
      'media esperada: total = local + visitante y 1T + 2T = total')
check(Mm[('corners', 'total')]['betano'] and abs(Mm[('corners', 'total')]['modelo'] / Mm[('corners', 'total')]['betano'] - 1) < 0.08
      and Mm[('corners', 'total')]['p10'] < Mm[('corners', 'total')]['modelo'] < Mm[('corners', 'total')]['p90'],
      'media esperada de córners ≈ la media que pone Betano, dentro de su rango del 80 %')
check(Mm[('saques_banda', 'total')]['betano'] is None and Mm[('saques_banda', 'total')]['modelo'] > 0,
      'media esperada también para lo que Betano no cotiza (Betano = None, modelo con el previo de la liga)')
h = html(A, ent)
check('<title>' in h and 'Gana A' in h and 'media esperada' in h and 'Proyección del partido' in h and "class='sub'" in h,
      'el informe HTML se genera solo a partir del análisis y trae la media esperada en cada bloque')
check(html(A) and 'Veces que salió Más' not in h, 'HTML sin la entrada ni historial: no inventa columnas de historial')
fm = {'local': [{'v': 'H', 'stats': {'g': [2, 1]}}, {'v': 'H', 'stats': {'g': [0, 0]}}, {'v': 'A', 'stats': {'g': [5, 5]}}],
      'visitante': [{'v': 'A', 'stats': {'g': [1, 2]}}]}
check(PR.forma_hits(fm, 'goles', 'total', 2.5, 'A', 'B') == 'A local: 1/2 · B visitante: 1/1'
      and PR.forma_hits(fm, 'goles', 'local', 1.5, 'A', 'B') == 'A local: 1/2 · Rivales de B fuera: 1/1'
      and PR.forma_hits(fm, 'goles', '1T', 0.5) is None and PR.forma_media(fm, 'g')['local'][2] == 2,
      'historial de equipos: veces que salió Más solo en la condición de hoy (local en casa, visitante fuera) y a favor / en contra')
check(PR.buscar_jugador({'Savanier Hidalgo': {}}, 'Hidalgo S.') and PR.buscar_jugador({'Savanier Hidalgo': {}}, 'Otro Jugador') is None
      and PR.jug_hits({'partidos': [{'min': 90, 'remates': 3}, {'min': 45, 'remates': 5}, {'min': 80, 'remates': 1}]}, 'remates', 2) == (1, 2),
      'historial de jugadores: nombres distintos coinciden y solo cuentan los partidos de 60′ o más')
mk_ = lambda p: dict(p=p, ev=-0.05, etiqueta='Justa', cuota=1.9, cuota_minima=2.0, robustez=p, seleccion='x', sel={})
check('moneda al aire' in lectura_par('goles', 2.5, mk_(0.50), mk_(0.50), {'modelo': 2.6, 'betano': 2.6}, {})
      and 'queda lejos' in lectura_par('goles', 0.5, mk_(0.9), mk_(0.1), {'modelo': 2.6, 'betano': 2.6}, {}),
      'lectura de cada línea: «moneda al aire» cerca de la línea y «queda lejos» cuando el lado probable pasa de 80 %')
check(veredicto(dict(etiqueta='Valor', cuota=2.6, ev=0.1))[0] == 'Riesgo' and veredicto(dict(etiqueta='Valor frágil (depende de un guion)', cuota=1.8, ev=0.1))[0] == 'Frágil'
      and veredicto(dict(etiqueta='Cara', cuota=1.8, ev=-0.1))[0] == 'No', 'etiquetas del informe: valor, riesgo (cuota ≥ 2.40), frágil, justa y no')
ej = json.load(open(os.path.join(AQUI, 'ejemplos', 'ejemplo_supermodelo.json'), encoding='utf-8'))
A2 = analizar(ej, n=4000)
h2 = html(A2, ej)
check('Veces que salió Más' in h2 and 'a favor / en contra' in h2 and '/90' in h2 and 'Histórico 60′' in h2 and A2['jugadores_esperado'],
      'ejemplo con historial: trae a favor / en contra, veces que salió Más, por 90′ y el histórico de 60′+ de los jugadores')
# ------------------------------------------------------------------ medio tiempo / tiempo completo y parejas de jugadores
sim_ = P.res
ev_ = lambda **k: MS.evento(sim_, k)
tot9 = sum(ev_(mercado='htft', lado=f'{a}/{b}').mean() for a in '1X2' for b in '1X2')
check(abs(tot9 - 1) < 1e-9, 'HT/FT: las nueve combinaciones suman 100 % de los partidos simulados')
check(all(abs(sum(ev_(mercado='htft', lado=f'{a}/{b}').mean() for b in '1X2') - ev_(mercado='resultado_1t', lado=a).mean()) < 1e-9 for a in '1X2')
      and all(abs(sum(ev_(mercado='htft', lado=f'{a}/{b}').mean() for a in '1X2') - ev_(mercado='resultado', lado=b).mean()) < 1e-9 for b in '1X2'),
      'HT/FT: las filas suman el resultado del 1.er tiempo y las columnas el resultado final')
check(np.array_equal(ev_(mercado='htft_o', lado='1'), ev_(mercado='resultado_1t', lado='1') | ev_(mercado='resultado', lado='1')),
      '«Resultado medio tiempo o tiempo completo» = ese resultado en el descanso O al final')
d1_ = sim_[0]['g1'] - sim_[1]['g1']; d2_ = (sim_[0]['g'] - sim_[0]['g1']) - (sim_[1]['g'] - sim_[1]['g1'])
check(np.array_equal(ev_(mercado='resultado_2t', lado='X'), d2_ == 0) and np.array_equal(ev_(mercado='resultado_1t', lado='2'), d1_ < 0),
      'resultado del 1.er y del 2.º tiempo salen de los goles de cada tiempo')
ent_p = json.load(open(os.path.join(AQUI, 'ejemplos', 'ejemplo_supermodelo.json'), encoding='utf-8'))
ent_p['betano']['unicos'] += [dict(mercado='htft', opciones={f'{a}/{b}': 9.0 for a in '1X2' for b in '1X2'}),
                              dict(mercado='resultado_1t', opciones={'1': 3.0, 'X': 2.2, '2': 3.9})]
ent_p['betano']['jugadores'].append(dict(jugador='Delantero Local', lado='local', stat='asiste', escalera={1: 4.0, 2: 15.0}))
ent_p['betano']['parejas'] = [dict(stat='anota_o_asiste', jugadores=['Delantero Local', 'Volante Visitante'], cuota=1.5),
                              dict(stat='asiste', jugadores=['Delantero Local', 'Jugador Baja'], cuota=2.0)]
ent_p['jugadores'] = list(ent_p.get('jugadores') or []) + [dict(nombre='Jugador Baja', lado='visitante', titular=0, minutos=0, fuera=True)]
Ap = analizar(ent_p, n=4000)
lp = {r['seleccion']: r for r in Ap['lineas']}
check(any(r['sel']['mercado'] == 'htft' for r in Ap['lineas']) and any(r['sel']['mercado'] == 'resultado_1t' for r in Ap['lineas']),
      'el análisis evalúa HT/FT y el resultado del 1.er tiempo con las cuotas de Betano')
par_ = [r for r in Ap['lineas'] if r['sel']['mercado'] == 'pareja']
single_ = {r['seleccion']: r for r in Ap['lineas'] if r['sel']['mercado'] == 'jugador'}
check(len(par_) == 2 and par_[0]['familia'] == 'pareja'
      and par_[0]['p_simulacion'] >= single_['Delantero Local anota o asiste']['p_simulacion'] - 1e-9,
      'pareja «cualquiera de…»: al menos tan probable como cada uno de los dos por separado')
bj = [r for r in par_ if 'Jugador Baja' in r['seleccion']][0]
check(bj['p_mercado'] is None and bj['alerta'] and 'baja confirmada' in bj['alerta'],
      'pareja con una baja confirmada: solo la simulación (sin mezclar el precio de Betano) y alerta de no apostar')
check(all(not r['seleccion'].startswith('Jugador Baja') for r in single_.values()) and 'Jugador Baja' in Ap['jugadores_esperado'],
      'baja confirmada: no hay líneas propias y entra a la simulación con cero participación')
check('Cualquiera de los jugadores' in html(Ap, ent_p) and 'id="par"' in html(Ap, ent_p), 'el informe HTML trae la sección de parejas de jugadores')

# ---- enfoque de mercados por contexto
check(Ap.get('enfoque') and Ap.get('enfoque_resumen', '').startswith('Enfoque:'), 'el análisis trae el enfoque de mercados por contexto')
check(all(x['estado'] in ('favorece', 'neutro', 'en contra', 'sin señal') for x in Ap['enfoque']), 'el enfoque solo usa estados válidos')
check('Enfoque de mercados' in markdown(Ap) and 'id=\'enfoque\'' in html(Ap, ent_p), 'el enfoque sale en el informe Markdown y en el HTML')
_p0 = {r['seleccion']: r['p'] for r in Ap['lineas']}
check(all('enfoque' in r for r in Ap['lineas']), 'cada línea trae su marca de enfoque (no cambia la probabilidad)')

print(f'\n{ok} pruebas superadas')
