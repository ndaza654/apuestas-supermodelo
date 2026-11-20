# -*- coding: utf-8 -*-
"""Auditoría de TODO lo que Claude sugirió (sencillas y combinadas): arma `registro/sugerencias.csv` calificado pata por pata.

    python3 recoleccion/sugerencias.py            # regenera registro/sugerencias.csv
    python3 recoleccion/auditoria_html.py         # genera el HTML con filtros

Fuentes (todas dentro del repo o del proyecto): entregas/2026-11-13/1430_combinadas.html, agentes/*_combinadas.md (13-nov y 12-noche),
boss_builder_serbia-alemania.md, entregas 1550/1558 (en vivo), registro/historial_lineas.csv (picks del 11 y 12-nov, ya calificados),
registro/lineas.csv («líneas que cumplen» del pipeline), balance_9nov (proyecto) y los resultados reales de Flashscore/Sofascore
(jornadas/2026-11-13/balance/resultados_completos.json y jugadores_resultado.txt).
Reglas: una pata sin dato verificable queda «sin verificar» (no se inventa); una combinada falla si falla cualquier pata; con una
línea asiática que devuelve (media ganada/perdida) y ninguna pata fallida, queda «parcial». Los partidos con prórroga (Estudiantes) se
marcan: Betano liquida a 90′ y el feed trae la prórroga.
Lo que NO está: el detalle pata por pata de las combinadas y boletos recomendados del 4 al 8-nov (solo cifras agregadas en el libro/proyecto).
"""
import csv, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'recoleccion'))
import calificar_lineas as CL

BAL = os.path.join(RAIZ, 'jornadas', '2026-11-13', 'balance')
R = json.load(open(os.path.join(BAL, 'resultados_completos.json'), encoding='utf8'))
HIST = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'historial_lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
COD = {'cumplió': 'C', 'falló': 'F', 'media ganada': 'MG', 'media perdida': 'MP', 'nula': 'N'}

# --- jugadores (Sofascore) -------------------------------------------------------------------------------------------------------
PJ = {}
_p = None
for ln in open(os.path.join(BAL, 'jugadores_resultado.txt'), encoding='utf8'):
    ln = ln.strip()
    if ln.startswith('#') and not ln.startswith('# '):
        _p = ln[1:].strip(); PJ[_p] = {}
    elif ln and not ln.startswith(('#', '@')) and _p:
        f = ln.split('|'); PJ[_p][f[1]] = [int(x) for x in f[2:]]       # min, rem, arco, goles, asist, faltas, recib, entr, ataj, am, ro


def cod(x):
    return COD[x]


def T(match, mercado, ambito, lado, linea):
    """Línea de equipo con resultados de Flashscore."""
    v = CL.valor(R[match], mercado, ambito)
    return (cod(CL.calificar(v, linea, lado)), f'{v:g}') if v is not None else ('U', 'sin dato')


def W(match, quien):
    """quien: 'h' gana local, 'a' gana visitante, 'hx' local o empate, 'ax' visitante o empate, 'nx' no hay empate, 'x' empate."""
    h, a = R[match]['g']
    ok = {'h': h > a, 'a': a > h, 'hx': h >= a, 'ax': a >= h, 'nx': h != a, 'x': h == a}[quien]
    return ('C' if ok else 'F', f'{h}-{a}')


def BTTS(match, si):
    h, a = R[match]['g']
    return ('C' if ((h > 0 and a > 0) == si) else 'F', f'{h}-{a}')


def AMBOS_TARJ(match, n):
    h, a = R[match]['y']
    return ('C' if (h >= n and a >= n) else 'F', f'{h}-{a} pts')


def MAS_TARJ(match, lado_local):
    h, a = R[match]['y']
    return ('C' if ((h > a) if lado_local else (a > h)) else 'F', f'{h}-{a} pts')


def HC(match, equipo_local, h):
    """Hándicap asiático entero/.5 (no usa .25/.75)."""
    gh, ga = R[match]['g']
    m = (gh - ga if equipo_local else ga - gh) + h
    return ('C' if m > 0 else 'F' if m < 0 else 'N', f'{gh}-{ga}')


def GOL_T(match, tiempo, lado, linea):
    return T(match, 'goles', tiempo, lado, linea)


def J(partido, nombre, que, linea):
    """Jugador con estadística de Sofascore. que: remates, al_arco, goles, asist, goles_o_asist, entradas, atajadas, faltas."""
    fila = PJ[partido].get(nombre)
    if fila is None:
        return ('N', 'no jugó')
    m, rem, arco, g, a, fal, rec, ent, atj, am, ro = fila
    v = {'remates': rem, 'al_arco': arco, 'goles': g, 'asist': a, 'goles_o_asist': g + a, 'entradas': ent, 'atajadas': atj, 'faltas': fal}[que]
    return ('C' if v >= linea else 'F', f'{v}')


def U(txt):
    return ('U', txt)


FAM = [('córner', 'córners'), ('tarjeta', 'tarjetas'), ('remates', 'remates/tiros'), ('tiros', 'remates/tiros'), ('faltas', 'faltas'),
       ('entradas', 'jugador'), ('atajadas', 'jugador'), ('anota', 'jugador'), ('asiste', 'jugador'), ('remates ', 'remates/tiros'),
       ('gol', 'goles/resultado'), ('ambos', 'goles/resultado'), ('gana', 'goles/resultado'), ('empate', 'goles/resultado'),
       ('hándicap', 'goles/resultado'), ('no pierde', 'goles/resultado'), ('marca', 'goles/resultado'), ('o empate', 'goles/resultado')]


def familia(txt):
    t = txt.lower()
    for k, v in FAM:
        if k in t:
            return v
    return 'otra'


FILAS = []


def add(entrega, fecha, hora, tipo, nombre, partidos, legs, cuota, p, jugada='', nota='', fuente='', resultado_forzado=None):
    """legs = [(partido, texto, cuota_pata|None, (cod, valor))]"""
    legs = [(l[0], l[1], l[2], (l[3][0], l[3][1].replace(' (Flashscore 15-nov 17:25)', '').replace(' (Flashscore 15-nov 17:25', ''))) for l in legs]
    cods = [l[3][0] for l in legs]
    if resultado_forzado:
        res = resultado_forzado
    elif 'F' in cods:
        res = 'falló'
    elif 'P' in cods:
        res = 'pendiente'            # sugerencia registrada antes del partido: se califica cuando registro/lineas.csv tenga el resultado
    elif 'U' in cods:
        res = 'sin verificar'
    elif 'MP' in cods or 'MG' in cods:
        res = 'parcial'
    elif all(c == 'N' for c in cods):
        res = 'anulada'
    else:
        res = 'cumplió'
    det = ' · '.join(f"{l[1]} {'✓' if l[3][0] in ('C', 'MG') else '✗' if l[3][0] in ('F', 'MP') else '–' if l[3][0] == 'N' else '?'} ({l[3][1]})" for l in legs)
    fall = ' | '.join(l[1] for l in legs if l[3][0] in ('F', 'MP'))
    fam = ' | '.join(sorted({familia(l[1]) for l in legs if l[3][0] in ('F', 'MP')}))
    FILAS.append({'id': f'S{len(FILAS) + 1:03d}', 'fecha_entrega': fecha, 'hora': hora, 'entrega': entrega, 'tipo': tipo, 'nombre': nombre, 'partidos': partidos,
                  'n_patas': len(legs), 'patas': ' + '.join(l[1] for l in legs), 'cuota': cuota if cuota != '' else '', 'p_estimada': p if p != '' else '',
                  'resultado': res, 'detalle_patas': det, 'patas_que_fallaron': fall, 'familia_fallo': fam, 'jugada': jugada, 'nota': nota, 'fuente': fuente,
                  'patas_json': json.dumps([[l[1], l[2], l[3][0], l[3][1], familia(l[1])] for l in legs], ensure_ascii=False)})


PB, ES, SL, SA = 'Países Bajos - Grecia', 'Escocia - Macedonia del Norte', 'Eslovenia - Suiza', 'Serbia - Alemania'
E1 = 'Países Bajos – Grecia'


def construir():
    # ===== 13-nov 14:30 · combinadas de la página (15) ============================================================================
    F = 'entregas/2026-11-13/1430_combinadas.html'
    ENT = '13-nov 14:30 · página de combinadas'
    def a(nombre, tipo, partidos, odd, p, legs, nota='', jugada=''):
        add(ENT, '2026-11-13', '14:30', tipo, nombre, partidos, legs, odd, p, jugada, nota + (' Precio estimado por mí (Crear apuesta).' if tipo == 'combinada mismo partido' else ''), F)
    a('Países Bajos sin perder, muchos remates', 'combinada mismo partido', 'Países Bajos–Grecia', 3.3, .26, [
        (PB, 'Países Bajos o empate', 1.18, W(PB, 'hx')), (PB, 'Remates Países Bajos Más 17.5', 1.53, T(PB, 'remates', 'local', 'Más', 17.5)),
        (PB, 'Tiros al arco total Menos 10.5', 1.55, T(PB, 'al_arco', 'total', 'Menos', 10.5))])
    a('Pocos goles de Países Bajos y córners', 'combinada mismo partido', 'Países Bajos–Grecia', 2.9, .29, [
        (PB, 'Goles Países Bajos Menos 3.5', 1.18, T(PB, 'goles', 'local', 'Menos', 3.5)), (PB, 'Córners 1.er tiempo Menos 5.5', 1.38, T(PB, 'corners', '1T', 'Menos', 5.5)),
        (PB, 'Córners total Más 8.5', 1.62, T(PB, 'corners', 'total', 'Más', 8.5))])
    a('Grecia incómoda en el 2.º tiempo', 'combinada mismo partido', 'Países Bajos–Grecia', 3.8, .22, [
        (PB, 'Goles 2.º tiempo Menos 2.5', 1.36, GOL_T(PB, '2T', 'Menos', 2.5)), (PB, 'Faltas Grecia Más 11.5', 1.75, T(PB, 'faltas', 'visitante', 'Más', 11.5)),
        (PB, 'Tiros al arco Grecia Más 2.5', 1.60, T(PB, 'al_arco', 'visitante', 'Más', 2.5))])
    a('Escocia gana, partido sin muchos remates', 'combinada mismo partido', 'Escocia–Macedonia', 2.9, .29, [
        (ES, 'Gana Escocia', 1.20, W(ES, 'h')), (ES, 'Remates total Menos 29.5', 1.42, T(ES, 'remates', 'total', 'Menos', 29.5)),
        (ES, 'Tarjetas 1.er tiempo Menos 1.5', 1.82, T(ES, 'tarjetas', '1T', 'Menos', 1.5))])
    a('Partido tranquilo', 'combinada mismo partido', 'Escocia–Macedonia', 3.8, .22, [
        (ES, 'Goles 1.er tiempo Menos 2.5', 1.16, GOL_T(ES, '1T', 'Menos', 2.5)), (ES, 'Tarjetas total Menos 4.5', 1.83, T(ES, 'tarjetas', 'total', 'Menos', 4.5)),
        (ES, 'Remates total Menos 27.5', 1.75, T(ES, 'remates', 'total', 'Menos', 27.5))])
    a('Córners temprano y faltas de Macedonia', 'combinada mismo partido', 'Escocia–Macedonia', 2.9, .29, [
        (ES, 'Córners 1.er tiempo Más 3.5', 1.40, T(ES, 'corners', '1T', 'Más', 3.5)), (ES, 'Faltas Macedonia del Norte Más 12.5', 1.75, T(ES, 'faltas', 'visitante', 'Más', 12.5))])
    a('Córners y tarjetas en los dos equipos', 'combinada mismo partido', 'Eslovenia–Suiza', 3.3, .26, [
        (SL, 'Córners total Más 6.5', 1.26, T(SL, 'corners', 'total', 'Más', 6.5)), (SL, 'Córners 1.er tiempo Más 2.5', 1.23, T(SL, 'corners', '1T', 'Más', 2.5)),
        (SL, 'Ambos 2+ tarjetas: Sí', 2.40, AMBOS_TARJ(SL, 2))])
    a('Suiza gana y Eslovenia se lleva tarjetas', 'combinada mismo partido', 'Eslovenia–Suiza', 3.8, .22, [
        (SL, 'Córners 1.er tiempo Menos 5.5', 1.27, T(SL, 'corners', '1T', 'Menos', 5.5)), (SL, 'Gana Suiza', 1.80, W(SL, 'a')),
        (SL, 'Más tarjetas: Eslovenia', 1.82, MAS_TARJ(SL, True))])
    a('Al menos 2 goles y pocos córners al inicio', 'combinada mismo partido', 'Eslovenia–Suiza', 3.3, .26, [
        (SL, 'Goles total Más 1.5', 1.57, T(SL, 'goles', 'total', 'Más', 1.5)), (SL, 'Córners 1.er tiempo Menos 3.5', 2.30, T(SL, 'corners', '1T', 'Menos', 3.5))])
    a('Cuota ~10 · Opción A', 'combinada entre partidos', 'PB–Grecia · Escocia · Eslovenia–Suiza', 9.06, .12, [
        (PB, 'Reijnders anota o asiste 1+', 2.22, J(PB, 'Tijjani Reijnders', 'goles_o_asist', 1)), (ES, 'Gana Escocia', 1.20, W(ES, 'h')),
        (SL, 'Córners Eslovenia Más 4.5', 3.40, T(SL, 'corners', 'local', 'Más', 4.5))])
    a('Cuota ~10 · Opción B', 'combinada entre partidos', 'PB–Grecia · Escocia · Eslovenia–Suiza', 9.0, .10, [
        (PB, 'Malen anota o asiste 1+', 1.72, J(PB, 'Donyell Malen', 'goles_o_asist', 1)),
        (ES, 'Gana Escocia + Macedonia remates Menos 7.5', 1.54, ('C' if W(ES, 'h')[0] == 'C' and T(ES, 'remates', 'visitante', 'Menos', 7.5)[0] == 'C' else 'F', '2-1; 7 remates')),
        (SL, 'Córners Eslovenia Más 4.5', 3.40, T(SL, 'corners', 'local', 'Más', 4.5))], nota=' Incluye Crear apuesta.')
    a('Cuota ~15 · Opción A', 'combinada entre partidos', 'PB–Grecia · Escocia · Eslovenia–Suiza', 13.57, .079, [
        (PB, 'Verbruggen atajadas 3+', 2.85, J(PB, 'Bart Verbruggen', 'atajadas', 3)), (ES, 'Córners 1.er tiempo Menos 5.5', 1.40, T(ES, 'corners', '1T', 'Menos', 5.5)),
        (SL, 'Córners Eslovenia Más 4.5', 3.40, T(SL, 'corners', 'local', 'Más', 4.5))])
    a('Cuota ~15 · Opción B', 'combinada entre partidos', 'PB–Grecia · Escocia · Eslovenia–Suiza', 13.62, .076, [
        (PB, 'Reijnders anota 1+', 3.20, J(PB, 'Tijjani Reijnders', 'goles', 1)), (ES, 'Córners Macedonia del Norte Más 2.5', 2.30, T(ES, 'corners', 'visitante', 'Más', 2.5)),
        (SL, 'Tarjetas Suiza Más 1.5', 1.85, T(SL, 'tarjetas', 'visitante', 'Más', 1.5))])
    a('Cuota ~20 · Opción A', 'combinada entre partidos', 'PB–Grecia · Escocia · Eslovenia–Suiza', 18.18, .059, [
        (PB, 'Reijnders remates 5+', 3.45, J(PB, 'Tijjani Reijnders', 'remates', 5)), (ES, 'Macedonia remates Menos 7.5', 1.55, T(ES, 'remates', 'visitante', 'Menos', 7.5)),
        (SL, 'Córners Eslovenia Más 4.5', 3.40, T(SL, 'corners', 'local', 'Más', 4.5))])
    a('Cuota ~20 · Opción B', 'combinada entre partidos', 'PB–Grecia · Escocia · Eslovenia–Suiza', 18.01, .057, [
        (PB, 'Retsos entradas 3+', 3.45, J(PB, 'Panagiotis Retsos', 'entradas', 3)), (ES, 'Córners Macedonia del Norte Más 2.5', 2.30, T(ES, 'corners', 'visitante', 'Más', 2.5)),
        (SL, 'Tarjetas Eslovenia Más 2.5', 2.27, T(SL, 'tarjetas', 'local', 'Más', 2.5))])

    # ===== 13-nov · combinadas del agente `combinadas` (12) ======================================================================
    F = 'jornadas/2026-11-13/informe_final.md · agentes/*_combinadas.md'
    ENT = '13-nov (cuotas 12-nov) · informe final: combinadas del mismo partido'
    def b(cid, partido, nombre, cuota, p, legs):
        add(ENT, '2026-11-13', '≈16:00 (12-nov)', 'combinada mismo partido', f'{cid} · {nombre}', partido.replace(' - ', '–'), legs, cuota, p, '',
            'Cuota = producto de las cuotas sueltas (techo); no se leyó el precio del cupón.', F)
    b('NLG-1', PB, 'Córners Más 6.5 + Goles Menos 4.5', 1.46, .662, [(PB, 'Córners Más 6.5', 1.20, T(PB, 'corners', 'total', 'Más', 6.5)), (PB, 'Goles Menos 4.5', 1.22, T(PB, 'goles', 'total', 'Menos', 4.5))])
    b('NLG-2', PB, 'Tiros al arco Grecia Más 1.5 + Tarjetas Menos 6.5', 1.54, .593, [(PB, 'Tiros al arco Grecia Más 1.5', None, T(PB, 'al_arco', 'visitante', 'Más', 1.5)), (PB, 'Tarjetas Menos 6.5', None, T(PB, 'tarjetas', 'total', 'Menos', 6.5))])
    b('SAL-1', SA, 'Córners Serbia Más 1.5 + Tarjetas Alemania Más 0.5', 1.50, .642, [(SA, 'Córners Serbia Más 1.5', 1.20, T(SA, 'corners', 'local', 'Más', 1.5)), (SA, 'Tarjetas Alemania Más 0.5', 1.25, T(SA, 'tarjetas', 'visitante', 'Más', 0.5))])
    b('SAL-2', SA, 'Tiros al arco Serbia Más 1.5 + Goles Alemania Menos 3.5', 1.72, .548, [(SA, 'Tiros al arco Serbia Más 1.5', 1.30, T(SA, 'al_arco', 'local', 'Más', 1.5)), (SA, 'Goles Alemania Menos 3.5', 1.32, T(SA, 'goles', 'visitante', 'Menos', 3.5))])
    b('ESC-1', ES, 'Goles Escocia Menos 3.5 + Ambos 1+ tarjetas: Sí', 1.56, .626, [(ES, 'Goles Escocia Menos 3.5', 1.27, T(ES, 'goles', 'local', 'Menos', 3.5)), (ES, 'Ambos 1+ tarjetas: Sí', 1.23, AMBOS_TARJ(ES, 1))])
    b('ESC-2', ES, 'Córners Menos 11.5 + Remates Menos 29.5', 1.86, .509, [(ES, 'Córners Menos 11.5', None, T(ES, 'corners', 'total', 'Menos', 11.5)), (ES, 'Remates Menos 29.5', None, T(ES, 'remates', 'total', 'Menos', 29.5))])
    b('SLO-1', SL, 'Córners Más 6.5 + Goles Menos 3.5', 1.59, .650, [(SL, 'Córners Más 6.5', 1.26, T(SL, 'corners', 'total', 'Más', 6.5)), (SL, 'Goles Menos 3.5', 1.26, T(SL, 'goles', 'total', 'Menos', 3.5))])
    b('SLO-2', SL, 'Córners Menos 10.5 + Goles Más 1.5', 1.81, .512, [(SL, 'Córners Menos 10.5', None, T(SL, 'corners', 'total', 'Menos', 10.5)), (SL, 'Goles Más 1.5', None, T(SL, 'goles', 'total', 'Más', 1.5))])
    BU, MO, LU, SK = 'Bulgaria - Islandia', 'Moldavia - Kazajistán', 'Luxemburgo - Estonia', 'Eslovaquia - Islas Feroe'
    b('BUL-1', BU, 'Córners Más 6.5 + Goles Menos 3.5', 1.55, .657, [(BU, 'Córners Más 6.5', 1.22, T(BU, 'corners', 'total', 'Más', 6.5)), (BU, 'Goles Menos 3.5', 1.27, T(BU, 'goles', 'total', 'Menos', 3.5))])
    b('LUX-1', LU, 'Córners Más 6.5 + Goles Estonia Menos 1.5', 1.59, .600, [(LU, 'Córners Más 6.5', None, T(LU, 'corners', 'total', 'Más', 6.5)), (LU, 'Goles Estonia Menos 1.5', None, T(LU, 'goles', 'visitante', 'Menos', 1.5))])
    b('MOL-1', MO, 'Córners Más 6.5 + Goles Kazajistán Más 0.5', 1.80, .523, [(MO, 'Córners Más 6.5', None, T(MO, 'corners', 'total', 'Más', 6.5)), (MO, 'Goles Kazajistán Más 0.5', None, T(MO, 'goles', 'visitante', 'Más', 0.5))])
    b('SVK-1', SK, 'Córners Más 7.5 + Goles Más 1.5', 1.65, .532, [(SK, 'Córners Más 7.5', None, T(SK, 'corners', 'total', 'Más', 7.5)), (SK, 'Goles Más 1.5', None, T(SK, 'goles', 'total', 'Más', 1.5))])

    # ===== 13-nov 12:45 · Boss Builder Serbia–Alemania =============================================================================
    F = 'jornadas/2026-11-13/boss_builder_serbia-alemania.md'
    ENT = '13-nov 12:45 · Boss Builder Serbia–Alemania'
    def c(nombre, cuota, p, legs, jugada=''):
        add(ENT, '2026-11-13', '12:45', 'Bet Builder', nombre, 'Serbia–Alemania', legs, cuota, p, jugada, 'Precio real del Bet Builder leído en Betano; promoción +25 %.', F)
    g = lambda lado, l: T(SA, 'goles', 'total', lado, l)
    cc = lambda lado, l: T(SA, 'corners', 'total', lado, l)
    c('Mejor: Goles Menos 3.5 + Córners Más 9.5 + Ambos marcan No', 5.00, .207, [(SA, 'Goles Menos 3.5', None, g('Menos', 3.5)), (SA, 'Córners Más 9.5', None, cc('Más', 9.5)), (SA, 'Ambos marcan: No', None, BTTS(SA, False))], 'variante (boleto 70, $32.000)')
    c('Plan B: Goles Menos 2.5 + Córners Más 8.5 + Ambos marcan No', 5.30, .194, [(SA, 'Goles Menos 2.5', None, g('Menos', 2.5)), (SA, 'Córners Más 8.5', None, cc('Más', 8.5)), (SA, 'Ambos marcan: No', None, BTTS(SA, False))])
    c("Plan B': Goles Alemania Menos 2.5 + Córners Más 8.5 + Ambos marcan No", 5.20, .182, [(SA, 'Goles Alemania Menos 2.5', None, T(SA, 'goles', 'visitante', 'Menos', 2.5)), (SA, 'Córners Más 8.5', None, cc('Más', 8.5)), (SA, 'Ambos marcan: No', None, BTTS(SA, False))])
    c('Fiel a la ficha: Goles Menos 3.5 + Córners Más 9.5 + Goles Serbia Más 0.5', 7.60, .121, [(SA, 'Goles Menos 3.5', None, g('Menos', 3.5)), (SA, 'Córners Más 9.5', None, cc('Más', 9.5)), (SA, 'Goles Serbia Más 0.5', None, T(SA, 'goles', 'local', 'Más', 0.5))])

    # ===== 13-nov 15:50 y 15:58 · en vivo =====================================================================================
    F = 'entregas/2026-11-13/1550_vivo-segundo-tiempo_probabilidades.md'
    ENT = '13-nov 15:50 · en vivo, 2.º tiempo'
    def v(partido, texto, cuota, p, res, nota='Mercado del partido completo; cuota leída al descanso.'):
        add(ENT, '2026-11-13', '15:50', 'en vivo (sencilla)', texto, partido.replace(' - ', '–'), [(partido, texto, cuota, res)], cuota, p, '', nota, F)
    v(SL, 'Goles Menos 1.5', 1.62, .79, T(SL, 'goles', 'total', 'Menos', 1.5))
    v(SL, 'Suiza Menos 1.5 goles', 1.29, .87, T(SL, 'goles', 'visitante', 'Menos', 1.5))
    v(SL, 'Eslovenia Menos 0.5 goles', 1.47, .76, T(SL, 'goles', 'local', 'Menos', 0.5))
    v(SL, 'Goles Menos 0.5', 3.50, .43, T(SL, 'goles', 'total', 'Menos', 0.5))
    v(PB, 'Ambos anotan 2.º tiempo: No', 1.60, .77, ('C', 'Grecia 0'))
    v(PB, 'Grecia Menos 0.5 goles', 2.05, .64, T(PB, 'goles', 'visitante', 'Menos', 0.5))
    v(ES, 'Goles Menos 2.5', 1.34, .78, T(ES, 'goles', 'total', 'Menos', 2.5))
    v(ES, 'Macedonia Más 1.5 córners', 1.45, .78, T(ES, 'corners', 'visitante', 'Más', 1.5))
    v(ES, 'Escocia Menos 1.5 goles', 1.80, .61, T(ES, 'goles', 'local', 'Menos', 1.5))
    v(SL, 'Suiza Más 10.5 córners', 2.20, .53, T(SL, 'corners', 'visitante', 'Más', 10.5))
    v(SL, 'Córners Más 15.5', 2.00, .55, T(SL, 'corners', 'total', 'Más', 15.5))
    add(ENT, '2026-11-13', '15:50', 'en vivo (combinada entre partidos)', 'Combinada de 3 armada por el modelo (no recomendada)', 'Eslovenia–Suiza · PB–Grecia · Escocia–Macedonia', [
        (SL, 'Eslovenia–Suiza Goles Menos 1.5', 1.62, T(SL, 'goles', 'total', 'Menos', 1.5)), (PB, 'PB–Grecia ambos 2T No', 1.60, ('C', 'Grecia 0')),
        (ES, 'Escocia–Macedonia Goles Menos 2.5', 1.34, T(ES, 'goles', 'total', 'Menos', 2.5))], 3.47, .47, '', 'Yo misma dije que no la recomendaba: las 3 patas comparten la idea «baja el ritmo de goles».', F)
    add('13-nov 15:58 · en vivo, líneas atrasadas', '2026-11-13', '15:58', 'en vivo (sencilla)', 'PB–Grecia tarjetas Más 1.5 (2 en el 2T)', 'Países Bajos–Grecia',
        [(PB, 'Tarjetas Más 1.5', 1.62, T(PB, 'tarjetas', 'total', 'Más', 1.5))], 1.62, .67, '', 'Veredicto «vale mirarla» (60–75 %). Terminó sin una sola tarjeta.', 'entregas/2026-11-13/1558_vivo-segundo-tiempo_contexto.md')

    # ===== 12-noche · combinadas del agente =========================================================================================
    MO2, CU, ST = 'Club Atletico Morelia - Leones Negros UdeG', 'Curazao - Panamá', 'Estudiantes de La Plata - Independiente Rivadavia'
    F = 'jornadas/2026-11-12-noche/agentes/*_combinadas.md'
    ENT = '12-nov noche · combinadas del agente'
    def d(cid, partido, nombre, cuota, p, legs, nota='', jugada=''):
        add(ENT, '2026-11-12', 'noche', 'combinada mismo partido', f'{cid} · {nombre}', partido.replace(' - ', '–'), legs, cuota, p, jugada, 'Cuota = producto (techo). ' + nota, F)
    d('M2', MO2, 'Goles Menos 3.5 + No hay empate', 1.62, .56, [(MO2, 'Goles Menos 3.5', 1.30, T(MO2, 'goles', 'total', 'Menos', 3.5)), (MO2, 'No hay empate', 1.25, W(MO2, 'nx'))])
    d('M6', MO2, 'Goles Más 1.5 + Leones marcan', 2.06, .52, [(MO2, 'Goles Más 1.5', 1.31, T(MO2, 'goles', 'total', 'Más', 1.5)), (MO2, 'Goles Leones Más 0.5', 1.57, T(MO2, 'goles', 'visitante', 'Más', 0.5))], 'Patas casi redundantes (aviso en el informe).')
    d('M4', MO2, 'Goles Más 1.5 + No hay empate', 1.64, .54, [(MO2, 'Goles Más 1.5', 1.31, T(MO2, 'goles', 'total', 'Más', 1.5)), (MO2, 'No hay empate', 1.25, W(MO2, 'nx'))])
    d('C8', CU, 'Córners Menos 10.5 + Curazao no pierde por 2 o más', 1.64, .56, [(CU, 'Córners Menos 10.5', 1.30, T(CU, 'corners', 'total', 'Menos', 10.5)), (CU, 'Hándicap Curazao +2', 1.26, HC(CU, True, 2))])
    d('C1', CU, 'Córners Menos 10.5 + Goles Más 1.5', 1.81, .52, [(CU, 'Córners Menos 10.5', 1.30, T(CU, 'corners', 'total', 'Menos', 10.5)), (CU, 'Goles Más 1.5', 1.39, T(CU, 'goles', 'total', 'Más', 1.5))])
    d('C3', CU, 'Córners Menos 10.5 + Curazao marca + Curazao +2', 2.46, .39, [(CU, 'Córners Menos 10.5', 1.30, T(CU, 'corners', 'total', 'Menos', 10.5)), (CU, 'Goles Curazao Más 0.5', 1.50, T(CU, 'goles', 'local', 'Más', 0.5)), (CU, 'Hándicap Curazao +2', 1.26, HC(CU, True, 2))],
      'Tu boleto 67 (variante con Más 2.5 tarjetas y Más 3.5 córners de Curazao) perdió por la misma pata de gol.', 'variante (boleto 67)')
    NE = ' Estudiantes fue a prórroga: el feed incluye la prórroga; la liquidación a 90′ se apoya en tu boleto 65 (ganado).'
    d('E1', ST, 'Córners Más 6.5 + Tiros al arco total Más 6.5 + Tarjetas Menos 8.5', 2.00, .50, [(ST, 'Córners total Más 6.5', 1.24, ('C', '≥ 7 a 90′ (boleto 65 ganó con Más 7.5)')), (ST, 'Tiros al arco total Más 6.5', 1.30, T(ST, 'al_arco', 'total', 'Más', 6.5)), (ST, 'Tarjetas total Menos 8.5', 1.24, ('C', 'boleto 65 ganó (Betano a 90′)'))], NE, 'variante (boleto 65)')
    d('E6', ST, 'Córners Más 6.5 + Tiros al arco total Menos 10.5', 1.57, .59, [(ST, 'Córners total Más 6.5', 1.24, ('C', '≥ 7 a 90′ (boleto 65 ganó con Más 7.5)')), (ST, 'Tiros al arco total Menos 10.5', 1.27, T(ST, 'al_arco', 'total', 'Menos', 10.5))], NE)
    d('E11', ST, 'Córners Rivadavia Más 2.5 + Estudiantes o empate', 1.69, .57, [(ST, 'Córners Independiente Rivadavia Más 2.5', 1.29, U('3 con prórroga; a 90′ probablemente ≤ 2 (tu boleto 68 perdió)')), (ST, 'Estudiantes o empate', 1.31, ('C', '2-2 a 90′'))],
      NE + ' Dudosa la liquidación de «o empate» con penales.')

    # ===== 12-nov mañana · combinadas (3) =====================================================================================================
    F = 'claude/analisis_12nov.md (artefacto «Líneas del 12-nov»)'
    ENT = '12-nov 09:15 · combinadas entre partidos'
    def hres(partido, texto):
        for h in HIST:
            if h['fecha_analisis'] == '2026-11-12' and h['partido'].replace('–', '-') == partido.replace('–', '-') and h['mercado_linea'] == texto:
                return (COD[h['resultado']], 'historial')
        raise KeyError((partido, texto))
    def e(nombre, cuota, p, legs):
        add(ENT, '2026-11-12', '09:15', 'combinada entre partidos', nombre, ' · '.join(sorted({l[0] for l in legs})), [(l[0], f'{l[1]}', l[2], hres(l[0], l[1])) for l in legs], cuota, p, '', 'Probabilidad según el modelo; «Betano sin margen» daba menos.', F)
    e('Segura · 2 patas', 1.75, .61, [('Turquía – Bélgica', 'Tarjetas Menos 5.5', 1.36), ('Italia – Francia', 'Tarjetas Más 2.5', 1.29)])
    e('Media · 3 patas', 2.60, .42, [('República Checa – España', 'Tarjetas Menos 4.5', 1.42), ('Senegal – Sudán', 'Goles Senegal Menos 3.5', 1.42), ('Italia – Francia', 'Tarjetas Más 2.5', 1.29)])
    e('Exótica · 5 patas', 10.40, .11, [('Italia – Francia', 'Tarjetas Más 3.5', 1.65), ('República Checa – España', 'Hándicap República Checa +2.5', 1.55), ('Senegal – Sudán', 'Goles Menos 3.5', 1.62),
                                       ('Inglaterra – Croacia', 'Córners Croacia Menos 3.5', 1.55), ('Montenegro – Letonia', 'Tarjetas Menos 4.5', 1.62)])

    # ===== 12-nov y 11-nov · sencillas (picks del historial) ==================================================================================
    for h in HIST:
        if h['fecha_analisis'] not in ('2026-11-12', '2026-11-11'):
            continue
        r = COD[h['resultado']]
        tipo = h['tipo']
        entrega = '12-nov 09:15 · líneas del día (alta probabilidad / valor / extra)' if h['fecha_analisis'] == '2026-11-12' else '11-nov · combi de 6 partidos (confiables / más riesgo)'
        add(entrega, h['fecha_analisis'], '09:15' if h['fecha_analisis'] == '2026-11-12' else '', 'sencilla', f"{h['mercado_linea']} ({tipo})", h['partido'].replace(' - ', '–'),
            [(h['partido'], h['mercado_linea'], float(h['cuota']), (r, 'historial'))], float(h['cuota']), float(h['p_modelo']), '', f'Tipo: {tipo}. ' + ('Pata de un boleto tuyo.' if 'Pata del boleto' in h['nota'] else ''),
            'registro/historial_lineas.csv')
    # combinadas del 11-nov (6 patas)
    F = 'claude/combi_11nov.md'
    def hr11(texto):
        for h in HIST:
            if h['fecha_analisis'] == '2026-11-11' and h['mercado_linea'] == texto:
                return (COD[h['resultado']], 'historial')
        raise KeyError(texto)
    conf = [('Barnsley – Oldham', 'Barnsley Menos 3.5 goles', 1.31), ('Sheffield Wed – Accrington', 'Ambos marcan: Sí', 1.39), ('Juventus W – Lyon W', 'Lyon Menos 4.5 goles', 1.31),
            ('Londrina – Náutico', 'Goles Menos 3.5', 1.36), ('Independiente Petrolero – Always Ready', 'Petrolero Menos 1.5 goles', 1.45), ('Quindío – Tigres', 'Goles Menos 2.5', 1.44)]
    risk = [('Barnsley – Oldham', 'Hándicap Oldham +2', 1.60), ('Sheffield Wed – Accrington', 'Accrington o empate', 1.50), ('Juventus W – Lyon W', 'Tarjetas 1T Más 0.5', 1.53),
            ('Londrina – Náutico', 'Goles 1T Menos 1.25 (asiática)', 1.60), ('Independiente Petrolero – Always Ready', 'Goles Menos 3.5', 1.60), ('Quindío – Tigres', 'Córners 1T Menos 4.5', 1.67)]
    add('11-nov · combi de 6 partidos', '2026-11-11', '', 'combinada entre partidos', 'Confiables ≥ 1.30 · 6 patas', '6 partidos', [(p, t, q, hr11(t)) for p, t, q in conf], 6.77, .13, '', 'Combinar las 6 daba EV ≈ −12 %: «conviene pocas patas».', F)
    add('11-nov · combi de 6 partidos', '2026-11-11', '', 'combinada entre partidos', 'De más riesgo 1.50–1.70 · 6 patas', '6 partidos', [(p, t, q, hr11(t)) for p, t, q in risk], 15.7, .05, '', 'EV ≈ −18 %.', F)

    # ===== 9-nov (solo lo que dejó el balance del 9-nov) =====================================================================================
    F = 'claude/balance_9nov.md · claude/calibracion_9nov.md'
    ENT = '9-nov · balance del día'
    for nombre, cuota, partido, nota in [('Combo de misión Kristiansund–Vålerenga: V gana + Más 3.5 + córners Más 11.5', 6.71, 'Kristiansund–Vålerenga', 'Terminó 1-0 para Kristiansund. EV −7 % / −12 %.'),
                                         ('Combo de misión Las Palmas–Eldense (popular)', 6.50, 'Las Palmas–Eldense', 'Terminó 2-0. Patas no recuperadas; resultado del balance del 9-nov.'),
                                         ('Combo de misión Junior–Cúcuta', 6.36, 'Junior–Cúcuta', 'Fallaron córners Más y Más 2.5 (terminó 2-0). Llevaba córners Más sin aviso de fuga.')]:
        add(ENT, '2026-11-09', '', 'combinada mismo partido', nombre, partido, [(partido, 'combo de 3 patas (detalle no recuperado)', None, ('F', 'balance 9-nov: 0/3'))], cuota, '', '', nota, F, resultado_forzado='falló')
    for nombre, cuota, partido in [('Gana Delfín', 5.20, 'Mushuc–Delfín'), ('Gana Real Sociedad B', 4.90, 'Sabadell–Real Sociedad B'), ('Gana Eldense', 3.65, 'Las Palmas–Eldense'), ('Gana Cúcuta', 4.30, 'Junior–Cúcuta')]:
        add(ENT, '2026-11-09', '', 'sencilla', f'{nombre} («línea con valor»)', partido, [(partido, nombre, cuota, ('F', 'balance 9-nov: 0/4'))], cuota, '', '', 'No favorito largo marcado como «valor»: 0 de 4. EV +1,4 % a +4,5 % (ruido).', F, resultado_forzado='falló')

    # ===== 4–8 nov =====
    add('4–8 nov · boletos recomendados', '2026-11-04', '', 'combinada entre partidos', 'Combinada del 4-nov (5 patas, cuotas 1.30–2.02)', '(no recuperado)', [('', '5 patas (detalle no recuperado)', None, ('C', 'balance 4–8 nov: 5/5'))], '', '',
        '', 'Del 4 al 8-nov solo hay cifras agregadas: 151 líneas 72/151 (48 %); boletos recomendados 27/51 selecciones (53 %); VALOR 5/11, «justa» 10/14, RIESGO 8/22; en vivo 3 de 13 boletos. Ver «Qué no se pudo auditar».',
        'claude/balance_lineas_sugeridas_4-8nov.md', resultado_forzado='cumplió')

    # ===== «Líneas que cumplen» del pipeline (sencillas del informe final del 13-nov y del 12-noche) ============================================
    rows = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
    for r in rows:
        if r['jornada'] not in ('2026-11-12-noche', '2026-11-13') or r['cumple_ficha'] != 'sí' or r['resultado'] not in COD:
            continue
        nombre = f"{r['mercado'].replace('jugador:', '')} {r['ambito'] if r['ambito'] not in ('total', '') else ''} {r['lado']} {r['linea']}".replace('  ', ' ').strip()
        if r['jugador']:
            nombre = f"{r['jugador']} {nombre}"
        add('13-nov (cuotas 12-nov) · informe final: líneas que cumplen' if r['jornada'] == '2026-11-13' else '12-nov noche · informe final: líneas que cumplen', '2026-11-13' if r['jornada'] == '2026-11-13' else '2026-11-12',
            '≈16:00', 'sencilla', nombre, r['partido'].replace(' - ', '–'),
            [(r['partido'], nombre, float(r['cuota']) if r['cuota'] else None, (COD[r['resultado']], r['nota'].split('valor real ')[-1][:40] if 'valor real' in r['nota'] else ''))],
            float(r['cuota']) if r['cuota'] else '', float(r['p_modelo']) if r['p_modelo'] else '', '', 'Línea con «cumple» (≥ 5 de 7 en ambos).', 'registro/lineas.csv')
    jornadas(rows)
    bb_y_misiones()
    cruzadas()
    quince(rows)
    # ===== 14-nov · análisis de la jornada (corrida programada 3:45 a. m.; pendientes de calificar con resultados del 14-nov) ======
    F14 = 'entregas/2026-11-14/0400_analisis-jornada-14nov.md'
    E14 = '14-nov 04:00 · análisis de la jornada (muestra de 7)'
    JB, NG, SB, MC = 'Japón - Brasil', 'Noruega - Gales', 'Suecia - Bosnia y Herzegovina', 'RCD Mallorca - Cordoba CF'
    P = ('P', '')
    nota14 = 'Pendiente de calificar con los resultados del 14-nov. Cuota = producto de patas (techo). EV < 0 en todas: se publican solo para auditar.'
    add(E14, '2026-11-14', '04:00', 'combinada mismo partido', 'Japón–Brasil · goles Menos 4.5 + Brasil Menos 3.5 (protección)', 'Japón–Brasil',
        [(JB, 'Goles total Menos 4.5', 1.20, P), (JB, 'Goles Brasil Menos 3.5', 1.10, P)], 1.32, .657, '', nota14 + ' p conjunta por simulación recortada 17,5 %.', F14)
    add(E14, '2026-11-14', '04:00', 'combinada', 'Japón goles Menos 4.5 + Noruega Menos 4.5 (2 patas, entre partidos)', 'Japón–Brasil / Noruega–Gales',
        [(JB, 'Goles total Menos 4.5', 1.20, P), (NG, 'Goles Noruega Menos 4.5', 1.15, P)], 1.38, .711, '', nota14, F14)
    add(E14, '2026-11-14', '04:00', 'combinada', 'Noruega Menos 4.5 + Suecia córners Menos 10.5 (2 patas, entre partidos)', 'Noruega–Gales / Suecia–Bosnia',
        [(NG, 'Goles Noruega Menos 4.5', 1.15, P), (SB, 'Córners total Menos 10.5', 1.29, P)], 1.48, .661, '', nota14, F14)
    add(E14, '2026-11-14', '04:00', 'combinada', 'LOTERÍA 3 patas · Japón Menos 4.5 + Noruega Menos 4.5 + Mallorca córners Más 7.5', 'Japón–Brasil / Noruega–Gales / Mallorca–Córdoba',
        [(JB, 'Goles total Menos 4.5', 1.20, P), (NG, 'Goles Noruega Menos 4.5', 1.15, P), (MC, 'Córners total Más 7.5', 1.19, P)], 1.64, .572, '', nota14 + ' Lotería de stake mínimo.', F14)
    add(E14, '2026-11-14', '04:00', 'sencilla', 'Suecia–Bosnia · córners total Menos 10.5 (7 de 7 / 7 de 7, protección)', 'Suecia–Bosnia',
        [(SB, 'Córners total Menos 10.5', 1.29, P)], 1.29, .761, '', nota14, F14)
    add(E14, '2026-11-14', '04:00', 'sencilla', 'Chapecoense–Vasco · córners Chapecoense Más 3.5 (único EV>0 de córners)', 'Chapecoense–Vasco',
        [('Chapecoense SC - Vasco da Gama RJ', 'Córners Chapecoense Más 3.5', 1.62, ('C', '6'))], 1.62, .632, '', nota14.replace('Pendiente de calificar con los resultados del 14-nov. ', 'Calificada el 15-nov con Flashscore. ') + ' 5 de 7 / 5 de 7; EV +2,3 %; alerta del modelo en el partido.', F14)
    return FILAS


def jornadas(rows):
    """Sugerencias registradas ANTES de los partidos por recoleccion/analisis_jornada.py (jornadas/<día>/sugerencias.json).
    Cada pata trae la clave de su línea en registro/lineas.csv: mientras esa línea no tenga resultado queda «pendiente»;
    cuando el agente `calificacion` lo llene, la sugerencia se califica sola al volver a correr este archivo."""
    import glob
    idx = {(r['jornada'], r['partido'], r['mercado'], r['ambito'], r['linea'], r['lado']): r for r in rows if not r['jugador']}
    for ruta in sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'sugerencias*.json'))):
        d = json.load(open(ruta, encoding='utf8'))
        jor = d['jornada']
        for s in d['sugerencias']:
            legs = []
            for p in s['patas']:
                r = idx.get((jor, *p['clave']))
                if r is not None and r['resultado'] in COD:
                    c = (COD[r['resultado']], r['nota'].split('valor real ')[-1][:40] if 'valor real' in r['nota'] else '')
                else:
                    c = ('P', 'pendiente')
                legs.append((p['partido'], p['texto'] if len(s['patas']) == 1 else f"{p['texto']} ({p['partido']})" if '|' in s['partidos'] else p['texto'], p['cuota'], c))
            add(f"{jor} · {d.get('entrega', 'informe de la jornada')}: {s['etiqueta']}", jor, '', s['tipo'], s['nombre'], s['partidos'].replace(' - ', '–'), legs, s['cuota'], s['p'],
                nota=f"{s['etiqueta']}; {d.get('p_es', 'p recortada')} (p del modelo {s['p_modelo']}). " + d.get('nota', ''), fuente=os.path.relpath(ruta, RAIZ))


def bb_y_misiones():
    """Combos de BB Boost (jornadas/<día>/bb/bb_boost_resumen.json) y misiones (jornadas/<día>/misiones/misiones.json) ya enviados al usuario.
    Entran a «Lo que te envié» calificados pata por pata con los `patas_real` que deja recoleccion/calificar_bb.py (sin ese paso quedan «pendiente»)."""
    import glob
    for rb in sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'bb', 'bb_boost_resumen.json'))):
        jdir = os.path.dirname(os.path.dirname(rb)); jor = os.path.basename(jdir)
        B = json.load(open(rb, encoding='utf8'))
        mp = os.path.join(jdir, 'resultados', 'mapa_partidos.json')
        M = json.load(open(mp, encoding='utf8')) if os.path.exists(mp) else {}
        hora = B.get('leido_hora', '')
        for slug, v in B.items():
            if not (isinstance(v, dict) and 'combos' in v):
                continue
            part = M.get(slug, slug).replace(' - ', '–')
            for c in v['combos']:
                pr = c.get('precio_bb') or (sum(c['precio_estimado']) / 2 if c.get('precio_estimado') else '')
                pr_txt = 'precio BB real leído en el cupón' if c.get('precio_bb') else 'precio BB ESTIMADO (no se leyó en el cupón)'
                pr_ = c.get('patas_real') or []
                legs = []
                for i, t in enumerate(c['patas']):
                    ok, real = pr_[i] if i < len(pr_) else (None, 'pendiente')
                    legs.append((M.get(slug, slug), t, (c.get('cuotas_cupon') or [None] * 9)[i], ('C' if ok is True else 'F' if ok is False else 'P', real)))
                add(f'{jor} · BB Boost enviado ({hora})', jor, hora, 'Bet Builder (BB Boost)', f"BB Boost {c['tag']} · {part}", part, legs, pr,
                    c.get('p_prudente', ''), 'jugada' if c.get('jugada') else 'no jugada', f"{pr_txt}; {'cumple' if c.get('cumple') else 'no cumple'} las condiciones del boost; p prudente {c.get('p_prudente')}.", os.path.relpath(rb, RAIZ))
    for rm in sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'misiones', 'misiones.json'))):
        jdir = os.path.dirname(os.path.dirname(rm)); jor = os.path.basename(jdir)
        Mi = json.load(open(rm, encoding='utf8')); hora = Mi.get('actualizado', '')
        for mm, nom in (('m1', 'Misión 1'), ('m2', 'Misión 2')):
            for c in (Mi.get(mm) or {}).get('combos', []):
                pr = c.get('precio_real') or c.get('producto') or ''
                pr_ = c.get('patas_real') or []
                legs = []
                for i, t in enumerate(c['patas']):
                    ok, real = pr_[i] if i < len(pr_) else (None, 'pendiente')
                    cu = re.search(r'@([\d,\.]+)', t)
                    legs.append((c['partido'], re.sub(r'\s*@[\d,\.]+', '', t), float(cu.group(1).replace(',', '.')) if cu else None, ('C' if ok is True else 'F' if ok is False else 'P', real)))
                tipo = 'Misión 1 · Bet Builder' if mm == 'm1' else 'Misión 2 · combinada entre partidos'
                add(f'{jor} · {nom} enviada ({hora})', jor, hora, tipo, f"{nom} · {c['partido']}", c['partido'], legs, pr, c.get('p', ''),
                    'jugada' if c.get('jugada') else 'no jugada', f"{c.get('estado', '')}; {'precio real leído' if c.get('precio_real') else 'cuota = producto de las cuotas'}.", os.path.relpath(rm, RAIZ))


def cruzadas():
    """Combinadas ENTRE partidos que Claude envió por el chat (jornadas/<día>/combinadas_enviadas_HHMM.json: [{id,tipo,patas:[[«partido HH:MM», texto, cuota, p, detalle]],cuota,p,ev, patas_real?}]).
    Entran a «Lo que te envié» como «combinada entre partidos»; quedan «pendiente» hasta que `patas_real` ([[true|false, valor real], …]) las califique."""
    import glob
    for rc in sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'combinadas_enviadas_*.json'))):
        jdir = os.path.dirname(rc); jor = os.path.basename(jdir)
        hh = re.search(r'_(\d{2})(\d{2})\.json$', rc)
        hora = f'{hh.group(1)}:{hh.group(2)}' if hh else ''
        for c in json.load(open(rc, encoding='utf8')):
            pr_ = c.get('patas_real') or []
            legs, partidos = [], []
            for i, pt in enumerate(c['patas']):
                part = re.sub(r'\s+\d{2}:\d{2}$', '', pt[0]).replace(' - ', '–')
                partidos.append(part)
                ok, real = pr_[i] if i < len(pr_) else (None, 'pendiente')
                legs.append((part, f'{part}: {pt[1]}', pt[2], ('C' if ok is True else 'F' if ok is False else 'P', real)))
            add(f'{jor} · combinadas entre partidos ({hora})', jor, hora, 'combinada entre partidos', f"{c['id']} · {c['tipo']}", ' + '.join(partidos), legs, c.get('cuota', ''),
                c.get('p', ''), 'jugada' if c.get('jugada') else 'no jugada', f"Cuotas Betano leídas ese día; p recortada del modelo, sin validar frente al precio; EV {c.get('ev', '')}.", os.path.relpath(rc, RAIZ))


def quince(rows):
    """15-nov: lo que se entregó ese día (estrategia 01:45, sugerencias 11:45, BB 14:00, en vivo 16:00), calificado con los resultados de Flashscore
    (jornadas/2026-11-15/resultados/resultados_1725.json y jugadores_resultado/jugadores_resultado_1745.txt). Lo que sigue sin partido terminado queda «pendiente»."""
    J15 = '2026-11-15'
    base = os.path.join(RAIZ, 'jornadas', J15)
    R15 = json.load(open(os.path.join(base, 'resultados', 'resultados_1725.json'), encoding='utf8'))
    PJ15, _q = {}, None
    for ln in open(os.path.join(base, 'jugadores_resultado', 'jugadores_resultado_1745.txt'), encoding='utf8'):
        ln = ln.strip()
        if ln.startswith('#') and not ln.startswith('# '):
            _q = ln[1:].strip(); PJ15[_q] = {}
        elif ln and not ln.startswith(('#', '@')) and _q:
            f = ln.split('|'); PJ15[_q][f[1]] = [int(x) for x in f[2:]]

    def t(m, mercado, ambito, lado, linea):
        if m not in R15:
            return ('P', 'pendiente')
        v = CL.valor(R15[m], mercado, ambito)
        return (cod(CL.calificar(v, linea, lado)), f'{v:g}') if v is not None else ('U', 'sin dato')

    def j(m, nombre, que, linea):
        fila = PJ15.get(m, {}).get(nombre)
        if fila is None:
            return ('N', 'no jugó') if m in PJ15 else ('U', 'sin dato')
        mi, rem, arco, g, a, fal, rec, ent, atj, am, ro = fila
        v = {'remates': rem, 'al_arco': arco, 'goles': g, 'asist': a, 'faltas': fal, 'entradas': ent, 'atajadas': atj}[que]
        return ('C' if v >= linea else 'F', f'{v}')

    idx = {(r['partido'], r['mercado'], r['ambito'], r['jugador'], r['lado'], float(r['linea'])): r for r in rows
           if r['jornada'] == J15 and r['linea'] not in ('', None)}

    def de_lineas(p):
        r = idx.get((p['partido'], p['mercado'], p['ambito'], p.get('jugador', ''), p['lado'], float(p['linea'])))
        if r is not None and r['resultado'] in COD:
            return (COD[r['resultado']], r['nota'].split('valor real ')[-1][:40] if 'valor real' in r['nota'] else '')
        return ('P', 'pendiente')

    # ----- 01:45 · estrategia del usuario (cuota 1,40–2,20, ≥ 7 de 10, colchón > 0) -----
    F0 = 'entregas/2026-11-15/0145_estrategia-jornada-15nov.md'
    E0 = '15-nov 01:45 · estrategia del usuario (cuota 1,40–2,20 · ≥ 7 de 10 · colchón > 0)'
    est = json.load(open(os.path.join(base, 'estrategia.json'), encoding='utf8'))
    for s_ in est['sencillas']:
        res = de_lineas(s_)
        nombre = s_['texto']
        add(E0, J15, '01:45', 'sencilla', nombre, s_['partido'].replace(' - ', '–'), [(s_['partido'], nombre, s_['cuota'], res)], s_['cuota'], s_['p'], '',
            'Línea que pasa el filtro del usuario (cuota 1,40–2,20, regularidad ≥ 7 de 10 en ambos, colchón > 0). p = del modelo.', F0)
    for c in est['combinadas']:
        legs = [(p_['partido'], p_['texto'] if not c['mismo_partido'] else p_['texto'], p_['cuota'], de_lineas(p_)) for p_ in c['patas']]
        partidos = ' / '.join(dict.fromkeys(p_['partido'].replace(' - ', '–') for p_ in c['patas']))
        add(E0, J15, '01:45', 'combinada mismo partido' if c['mismo_partido'] else 'combinada entre partidos',
            f"Combinada {c['n']}: " + ' + '.join(p_['texto'] for p_ in c['patas']), partidos, [(l[0], f'{l[1]} ({l[0]})' if not c['mismo_partido'] else l[1], l[2], l[3]) for l in legs],
            c['cuota_producto'], c['p_producto'], '', c['nota'] + '. Cuota = producto de patas (techo); p = producto de las p del modelo (sin correlación).', F0)

    # ----- 11:45 · sugerencias de los 4 partidos de las 12:00 y 12:30 -----
    F1 = 'entregas/2026-11-15/1145_sugerencias-4-partidos-12h.md'
    E1_ = '15-nov 11:45 · sugerencias de los 4 partidos de las 12:00 y 12:30'
    BA, EC, ES_, GL = 'Bielorrusia - Albania', 'SD Eibar - Cadiz CF', 'CD Eldense - CE Sabadell FC', 'Granada CF - UD Las Palmas'
    nota1 = 'Cuotas leídas el 14-nov 19:55 (no se pudieron releer ese día). Sin alineaciones confirmadas.'
    for m, txt, cuota, p_, res in [
            (BA, 'Goles Más 1.5', 1.45, None, t(BA, 'goles', 'total', 'Más', 1.5)),
            (EC, 'Goles Cádiz Más 0.5', 1.52, .63, t(EC, 'goles', 'visitante', 'Más', .5)),
            (ES_, 'Córners Sabadell Más 3.5', 1.42, .66, t(ES_, 'corners', 'visitante', 'Más', 3.5)),
            (ES_, 'Goles Más 1.5', 1.47, .655, t(ES_, 'goles', 'total', 'Más', 1.5)),
            (ES_, 'Goles Eldense Menos 1.5', 1.45, .66, t(ES_, 'goles', 'local', 'Menos', 1.5))]:
        add(E1_, J15, '11:45', 'sencilla', txt, m.replace(' - ', '–'), [(m, txt, cuota, res)], cuota, p_ if p_ else '', '', nota1, F1)

    # ----- 14:00 · Bet Builders España–Inglaterra y Bélgica–Italia -----
    F2 = 'entregas/2026-11-15/1400_bb-espana-inglaterra_belgica-italia.md'
    E2 = '15-nov 14:00 · BB España–Inglaterra y Bélgica–Italia (14:45)'
    EI, BI = 'España - Inglaterra', 'Bélgica - Italia'
    nota2 = 'Cuota = producto de las cuotas (techo); el BB paga menos. Probabilidades de jugador = estimación propia, no del modelo.'
    add(E2, J15, '14:00', 'Bet Builder', 'España–Inglaterra · C1: Bellingham 2+ remates + Kane 1+ a puerta + Inglaterra marca', 'España–Inglaterra',
        [(EI, 'Bellingham 2+ remates', 1.55, j(EI, 'Bellingham J.', 'remates', 2)), (EI, 'Kane 1+ tiro al arco', 1.37, j(EI, 'Kane H.', 'al_arco', 1)),
         (EI, 'Inglaterra marca (Más 0.5)', 1.27, t(EI, 'goles', 'visitante', 'Más', .5))], 2.70, .49, '', nota2, F2)
    add(E2, J15, '14:00', 'Bet Builder', 'España–Inglaterra · C2: Bellingham 2+ + Kane 2+ remates + remates España Menos 17.5', 'España–Inglaterra',
        [(EI, 'Bellingham 2+ remates', 1.55, j(EI, 'Bellingham J.', 'remates', 2)), (EI, 'Kane 2+ remates', 1.42, j(EI, 'Kane H.', 'remates', 2)),
         (EI, 'Remates España Menos 17.5', 1.75, t(EI, 'remates', 'local', 'Menos', 17.5))], 3.85, .32, '', nota2, F2)
    add(E2, J15, '14:00', 'Bet Builder', 'Bélgica–Italia · C1: tiros al arco Más 8.5 + De Bruyne 3+ remates + Tonali 1+ remate', 'Bélgica–Italia',
        [(BI, 'Tiros al arco total Más 8.5', 1.50, t(BI, 'al_arco', 'total', 'Más', 8.5)), (BI, 'De Bruyne 3+ remates', 1.30, j(BI, 'De Bruyne K.', 'remates', 3)),
         (BI, 'Tonali 1+ remate', 1.31, j(BI, 'Tonali S.', 'remates', 1))], 2.55, .41, '', nota2, F2)
    add(E2, J15, '14:00', 'Bet Builder', 'Bélgica–Italia · C2: tiros al arco Más 8.5 + De Ketelaere 1+ a puerta + Mechele 1+ falta + Tonali 1+ remate', 'Bélgica–Italia',
        [(BI, 'Tiros al arco total Más 8.5', 1.50, t(BI, 'al_arco', 'total', 'Más', 8.5)), (BI, 'De Ketelaere 1+ tiro al arco', 1.50, j(BI, 'De Ketelaere C.', 'al_arco', 1)),
         (BI, 'Mechele 1+ falta', 1.60, j(BI, 'Mechele B.', 'faltas', 1)), (BI, 'Tonali 1+ remate', 1.31, j(BI, 'Tonali S.', 'remates', 1))], 4.72, .27, '', nota2, F2)

    # ----- 16:00 · en vivo, 2.º tiempo de los 4 partidos de las 14:45 (cuotas de hace 10–15 min; líneas del partido completo) -----
    F3 = 'entregas/2026-11-15/1600_vivo-2t_4-partidos-14h45.md'
    E3 = '15-nov 16:00 · en vivo, 2.º tiempo (4 partidos 14:45)'
    CC, FT = 'Croacia - República Checa', 'Francia - Turquía'
    nota3 = 'Línea del partido completo leída en vivo (≈15:44–15:49). p = mezcla de mi p y la de Betano (= 1 / cuota justa de la entrega).'
    vivo = [
        (EI, 'Córners España Menos 2.5', 2.75, 69, 1.95, ('corners', 'local', 'Menos', 2.5)), (EI, 'Remates España Menos 14.5', 2.07, 91, 1.47, ('remates', 'local', 'Menos', 14.5)),
        (EI, 'Tiros al arco España Menos 3.5', 1.83, 87, 1.46, ('al_arco', 'local', 'Menos', 3.5)), (EI, 'Remates total Menos 26.5', 1.75, 89, 1.41, ('remates', 'total', 'Menos', 26.5)),
        (EI, 'Córners España Menos 3.5', 1.75, 87, 1.44, ('corners', 'local', 'Menos', 3.5)), (EI, 'Córners total Menos 7.5', 2.37, 62, 1.97, ('corners', 'total', 'Menos', 7.5)),
        (EI, 'Córners total Menos 8.5', 1.70, 78, 1.51, ('corners', 'total', 'Menos', 8.5)), (EI, 'Tiros al arco total Menos 8.5', 1.78, 76, 1.56, ('al_arco', 'total', 'Menos', 8.5)),
        (EI, 'Tarjetas total Menos 3.5', 1.72, 73, 1.57, ('tarjetas', 'total', 'Menos', 3.5)),
        (CC, 'Tarjetas total Menos 1.5', 2.60, 66, 1.96, ('tarjetas', 'total', 'Menos', 1.5)), (CC, 'Tarjetas total Menos 2.5', 1.65, 88, 1.38, ('tarjetas', 'total', 'Menos', 2.5)),
        (CC, 'Tarjetas R. Checa Menos 1.5', 1.57, 88, 1.35, ('tarjetas', 'visitante', 'Menos', 1.5)),
        (FT, 'Goles Francia Menos 1.5', 2.18, 73, 1.72, ('goles', 'local', 'Menos', 1.5)), (FT, 'Córners Francia Menos 6.5', 1.93, 74, 1.65, ('corners', 'local', 'Menos', 6.5)),
        (FT, 'Goles total Menos 2.5', 1.62, 79, 1.47, ('goles', 'total', 'Menos', 2.5)), (FT, 'Tarjetas Turquía Menos 1.5', 1.67, 79, 1.48, ('tarjetas', 'visitante', 'Menos', 1.5)),
        (FT, 'Tarjetas total Menos 2.5', 1.57, 81, 1.43, ('tarjetas', 'total', 'Menos', 2.5)), (FT, 'Córners Turquía Más 3.5', 1.98, 64, 1.81, ('corners', 'visitante', 'Más', 3.5)),
        (BI, 'Tarjetas Bélgica Menos 1.5', 1.70, 79, 1.49, ('tarjetas', 'local', 'Menos', 1.5)), (BI, 'Tarjetas total Menos 3.5', 1.82, 69, 1.66, ('tarjetas', 'total', 'Menos', 3.5))]
    for m, txt, cuota, pm, justa, (mer, amb, lado, lin) in vivo:
        add(E3, J15, '16:00', 'en vivo (sencilla)', txt, m.replace(' - ', '–'), [(m, txt, cuota, t(m, mer, amb, lado, lin))], cuota, round(1 / justa, 3), '',
            f'{nota3} p mía {pm} %.', F3)
    for m, nombre, txt, cuota, pm, justa, que, lin in [
            (EI, 'Bellingham J.', 'Bellingham 3+ tiros al arco', 2.10, 62, 1.63, 'al_arco', 3), (FT, 'Güler A.', 'Güler 4+ remates', 2.05, 59, 1.70, 'remates', 4),
            (FT, 'Calhanoglu H.', 'Calhanoglu 2+ remates', 3.00, 53, None, 'remates', 2), (EI, 'Porro P.', 'Porro 4+ faltas', 1.37, 76, None, 'faltas', 4)]:
        add(E3, J15, '16:00', 'en vivo (sencilla)', txt, m.replace(' - ', '–'), [(m, txt, cuota, j(m, nombre, que, lin))], cuota, round(1 / justa, 3) if justa else '', '',
            f'{nota3} p mía {pm} %. Jugador: muestra chica.', F3)


def main():
    filas = construir()
    extra = os.path.join(RAIZ, 'registro', 'sugerencias_extra.csv')   # filas calificadas a mano (p. ej. combinadas del usuario del 16-nov); se agregan al final
    if os.path.exists(extra):
        filas += [dict(r) for r in csv.DictReader(open(extra, encoding='utf-8-sig'), delimiter=';')]
    out = os.path.join(RAIZ, 'registro', 'sugerencias.csv')
    campos = list(filas[0].keys())
    with open(out, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=';')
        w.writeheader(); w.writerows(filas)
    from collections import Counter
    print(out, len(filas), 'filas')
    print(Counter((f['tipo'], f['resultado']) for f in filas))


if __name__ == '__main__':
    main()
