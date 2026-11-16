#!/usr/bin/env python3
"""Completa el Histórico del dashboard para el 9–15 nov (lo que el libro no trae: solo cubre 4–8 nov).

Entradas (todo en el repo):
  registro/crudo_partidos/AAAA-MM-DD.txt   estadísticas de Flashscore por partido (feeds df_st / df_sur, leídos con el navegador)
  registro/boletos_9-12nov.json, jornadas/*/balance/boletos_betano.json, patas_calificadas.json   boletos y patas
  jornadas/2026-11-11/resultados/*.json    Sheffield Wed–Accrington y Barnsley–Oldham (no salen en la lista de Flashscore)
Salidas:
  registro/historico_9-15nov.json          {selecciones, partidos} con el mismo formato que registro/historico_libro.json
  registro/patas_calificadas_9-12nov.json  patas de los boletos 52–64 (el balance de esos días no las guardó)

Cada selección lleva: boleto, fecha, partido, liga, marcador, familia, ámbito, lado, línea, valor real, resultado, cuota de la pata.
Resultado «Anulada» = no se pudo verificar (jugador sin dato, mercado no legible o boleto con cash out antes de jugarse).
La «cuota de la pata» es el precio propio solo cuando Betano lo mostró; en un Bet Builder es el precio del grupo (el dashboard lo marca).
Uso: python3 recoleccion/historico_extra.py
"""
import glob
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------- partidos: id de Flashscore -> (nombre, liga) ----------
EUR = 'EUROPA: UEFA Liga de Naciones'
ES2 = 'ESPAÑA: Segunda División'
COL = 'COLOMBIA: Primera A'
CON = 'CONCACAF: Liga de Naciones'
PART = {
    # 9-nov
    '8AjgFXwJ': ('Junior - Cúcuta', COL), 'QF6JVSAD': ('Técnico Universitario - Manta', 'ECUADOR: LigaPro - Grupo descenso'),
    'EgEXvXmR': ('Mushuc Runa - Delfín', 'ECUADOR: LigaPro - Grupo descenso'), 'GEWsQBr9': ('Las Palmas - Eldense', 'ESPAÑA: LaLiga Hypermotion'),
    'l2WUIcv3': ('Kristiansund - Vålerenga', 'NORUEGA: Eliteserien'), '04gF73Ss': ('Sabadell - Real Sociedad B', 'ESPAÑA: LaLiga Hypermotion'),
    # 10-nov
    'KlE7j8Rr': ('Internacional de Bogotá - América de Cali', COL), 'OISydU3L': ('Once Caldas - Atlético Nacional', COL),
    # 11-nov
    'YwRP0DQE': ('Quindío - Tigres', 'COLOMBIA: Primera B - Cuadrangular'), 'tGAKx5VH': ('Juventus (F) - Lyon (F)', 'EUROPA: UEFA Champions League Femenina'),
    'dIXA0t9s': ('Londrina - Náutico', 'BRASIL: Serie B'), 'SSWUGN7m': ('Independiente Petrolero - Always Ready', 'BOLIVIA: Copa Bolivia'),
    # 12-nov
    'AJh0DeXa': ('Turquía - Bélgica', EUR), '8AlPZdzK': ('Estudiantes de La Plata - Independiente Rivadavia', 'ARGENTINA: Supercopa'),
    '6isiMKqI': ('Costa de Marfil - Gambia', 'ÁFRICA: Eliminatorias Copa Africana'), 'Q7OGKyqf': ('Senegal - Sudán', 'ÁFRICA: Eliminatorias Copa Africana'),
    'IqxRBrde': ('Italia - Francia', EUR), 'lfBbB5E4': ('Albania - Finlandia', EUR), 'OKNATSve': ('Inglaterra - Croacia', EUR),
    'vBfNkJec': ('República Checa - España', EUR), 'pYOIBire': ('Montenegro - Letonia', EUR), 'CrivN9NM': ('Curazao - Panamá', CON), '8ExAHmop': ('Panamá - Curazao', CON),
    'nyvAHotQ': ('FC Barcelona (F) - Arsenal FC (F)', 'EUROPA: UEFA Champions League Femenina'), 'hOu755k5': ('Atlético Morelia - Leones Negros', 'MÉXICO: Liga de Expansión MX'),
    # 13-nov
    't0Cjphwg': ('Internacional de Bogotá - Independiente Santa Fe', COL), 'GzS4tf1n': ('Países Bajos - Grecia', EUR), 'QqdVALGL': ('Nigeria - Tanzania', 'ÁFRICA: Eliminatorias Copa Africana'),
    '2DHtlqiI': ('Túnez - Libia', 'ÁFRICA: Eliminatorias Copa Africana'), 'QiOSzuG8': ('Sudáfrica - Kenia', 'ÁFRICA: Eliminatorias Copa Africana'), '6sjuQYG5': ('Serbia - Alemania', EUR),
    'KAogLGHG': ('Escocia - Macedonia del Norte', EUR), 'zqsNLPOQ': ('Eslovenia - Suiza', EUR), '0ztMGL7s': ('Moldavia - Kazajistán', EUR), 'EHIYsb6t': ('Bulgaria - Islandia', EUR),
    'K0OYkbnR': ('Liechtenstein - Azerbaiyán', EUR), 'dQZgSiJ5': ('Andorra - Gibraltar', EUR), 'Ewl0AMw2': ('Argentina - Uruguay', 'INTERNACIONAL: Amistosos'),
    'GIt89MIO': ('Luxemburgo - Estonia', EUR), '6XrUEaxf': ('Eslovaquia - Islas Feroe', EUR), 'CW2JFHFs': ('Ecuador - Costa Rica', 'INTERNACIONAL: Amistosos'),
    '2Pafs6I6': ('Colombia - Chile', 'INTERNACIONAL: Amistosos'), 'jgMK1EUj': ('Saint Martin - El Salvador', CON), '8Winxe63': ('Montserrat - Nicaragua', CON),
    '0SV4LdnI': ('Guatemala - Canadá', CON),
    # 14-nov
    '0Kk0GWXA': ('Banfield - Boca Juniors', 'ARGENTINA: Copa Argentina'), 'xpXIVhOa': ('Águilas Doradas - Independiente Medellín', COL), 'SGAbrW75': ('Millonarios - Alianza', COL),
    '8fCEvl7U': ('Deportivo Cali - Deportes Tolima', COL), 'WnUAXEgm': ('Atlético Nacional - Once Caldas', COL), 'ARJ356Ua': ('Chapecoense - Vasco da Gama', 'BRASIL: Brasileirao Serie A'),
    'v9YyLeNG': ('Mirassol - Atlético Mineiro', 'BRASIL: Brasileirao Serie A'), 'IZMIMqJl': ('Almería - Andorra', ES2), 'dhKuF6i5': ('Real Valladolid - Castellón', ES2),
    'GEIPIlht': ('Real Sociedad B - Sporting de Gijón', ES2), 'Q7rBGbBC': ('Mallorca - Córdoba', ES2), 'tv3rrSgl': ('Portugal - Dinamarca', EUR), 'b31hwkw2': ('Irlanda del Norte - Ucrania', EUR),
    'vyCbg1Ta': ('Kosovo - Israel', EUR), 'EwECQBgd': ('Georgia - Hungría', EUR), 'SYw37rNa': ('Noruega - Gales', EUR), 'bLpOQiOc': ('Jamaica - México', CON),
    '406RaDLU': ('Querétaro - Monterrey', 'MÉXICO: Liga MX'), 'focWCnQk': ('Suecia - Bosnia y Herzegovina', EUR), 'YejRGeRN': ('Rumanía - Polonia', EUR), 'UHpKugvm': ('Japón - Brasil', 'INTERNACIONAL: Amistosos'),
    # 15-nov
    'l8bw2adJ': ('Eibar - Cádiz', ES2), 'EojPP2lQ': ('Eldense - Sabadell', ES2), 'AHyeKtCm': ('Granada - Las Palmas', ES2), 'OvMXGSMh': ('Tenerife - Ceuta', ES2),
    '4YNzMsxg': ('Bélgica - Italia', EUR), '4ppF09Hq': ('Chipre - Montenegro', EUR), 'pWwJD4Rr': ('Francia - Turquía', EUR), 'zs0jyKt4': ('España - Inglaterra', EUR),
    'WlNQ9VC7': ('Letonia - Armenia', EUR), 'GfK2VlAr': ('Croacia - República Checa', EUR), 'AoaMhFKb': ('Bielorrusia - Albania', EUR), 'dOS9WO3d': ('Finlandia - San Marino', EUR),
}
# partidos que Flashscore no listó en su página del día: solo lo que traen los resultados ya guardados
SIN_LISTA = {'2026-11-11': [('sheffield-wednesday-accrington', 'Sheffield Wednesday - Accrington Stanley', 'INGLATERRA: EFL Trophy'),
                            ('barnsley-oldham', 'Barnsley - Oldham Athletic', 'INGLATERRA: EFL Trophy')]}


def par(a, b):
    return f'{a}-{b}'


def leer_crudo():
    out = []
    for f in sorted(glob.glob(os.path.join(RAIZ, 'registro', 'crudo_partidos', '*.txt'))):
        for ln in open(f, encoding='utf8'):
            p = ln.rstrip('\n').split('|')
            if len(p) < 9:
                continue
            d = {'fecha': p[0], 'mid': p[1], 'home': p[2], 'away': p[3], 'ref': p[6]}
            d['g1'] = [int(x) for x in p[4].split(',')]
            d['g2'] = [int(x) for x in p[5].split(',')]
            for blk in (p[7], p[8]):
                for kv in blk.split():
                    k, v = kv.split('=')
                    d[k] = None if v == '-' else [x for x in v.split(',')]
            out.append(d)
    return out


def num(d, k):
    v = d.get(k)
    return None if v is None else [float(x) if '.' in x else int(x) for x in v]


def construir_partidos():
    P = []
    for d in leer_crudo():
        nom, liga = PART[d['mid']]
        g = [d['g1'][0] + d['g2'][0], d['g1'][1] + d['g2'][1]]
        y, r, c, f, sh = num(d, 'y'), num(d, 'r'), num(d, 'c'), num(d, 'f'), num(d, 'sh')
        P.append({
            'Fecha': d['fecha'], 'Partido': nom, 'Liga': liga, 'Marcador': par(*g), 'Descanso': par(*d['g1']), 'Árbitro': d['ref'] or None,
            'xG': par(*d['xg']) if d.get('xg') else None, 'Posesión %': par(*d['pos']) if d.get('pos') else None,
            'Remates': par(*sh) if sh else None, 'Al arco': par(*num(d, 'sot')) if d.get('sot') else None,
            'Córners': par(*c) if c else None, 'Córners 1T': par(*num(d, 'c1')) if d.get('c1') else None,
            'Faltas': par(*f) if f else None, 'Amarillas': par(*y) if y else None, 'Rojas': par(*r) if r else None,
            'Fueras de lugar': par(*num(d, 'off')) if d.get('off') else None, 'Saques de meta': par(*num(d, 'gk')) if d.get('gk') else None,
            'Saques de banda': par(*num(d, 'ti')) if d.get('ti') else None, 'Atajadas': par(*num(d, 'sv')) if d.get('sv') else None,
            'Remates 1T': par(*num(d, 'sh1')) if d.get('sh1') else None, 'Al arco 1T': par(*num(d, 'sot1')) if d.get('sot1') else None,
            'Amarillas 1T': par(*num(d, 'y1')) if d.get('y1') else None, 'Faltas 1T': par(*num(d, 'f1')) if d.get('f1') else None,
            'Total córners': sum(c) if c else None, 'Total tarjetas': (sum(y) + 2 * sum(r)) if y else None,
            'Total faltas': sum(f) if f else None, 'Total remates': sum(sh) if sh else None, 'Goles y expulsiones': None,
            'mid': d['mid']})
    for dia, lst in SIN_LISTA.items():
        for slug, nom, liga in lst:
            x = json.load(open(os.path.join(RAIZ, 'jornadas', dia, 'resultados', slug + '.json'), encoding='utf8'))
            g, c, y, r, f = x['goles'], x['corners'], x['amarillas'], x['rojas'], x.get('faltas')
            P.append({'Fecha': dia, 'Partido': nom, 'Liga': liga, 'Marcador': par(*g), 'Descanso': None, 'Árbitro': None, 'xG': None, 'Posesión %': None, 'Remates': None, 'Al arco': None,
                      'Córners': par(*c), 'Córners 1T': par(*x['corners_1t']) if x.get('corners_1t') else None, 'Faltas': par(*f) if f else None, 'Amarillas': par(*y), 'Rojas': par(*r),
                      'Fueras de lugar': None, 'Saques de meta': None, 'Saques de banda': None, 'Atajadas': None, 'Remates 1T': None, 'Al arco 1T': None,
                      'Amarillas 1T': par(*x['amarillas_1t']) if x.get('amarillas_1t') else None, 'Faltas 1T': None,
                      'Total córners': sum(c), 'Total tarjetas': sum(y) + 2 * sum(r), 'Total faltas': sum(f) if f else None, 'Total remates': None, 'Goles y expulsiones': None, 'mid': None})
    P.sort(key=lambda p: (p['Fecha'], p['Partido']))
    return P


# ---------- selecciones de los boletos 52–94 ----------
G, F_, A = 'Ganó', 'Perdió', 'Anulada'
MK = {'Córners (total)': 'Tiros de esquina Menos/Más', 'Córners (equipo)': 'Tiros de esquina Menos/Más', 'Córners 1T': 'Tiros de esquina 1.er tiempo', 'Goles (total)': 'Goles totales Más/Menos',
      'Goles (equipo)': 'Goles del equipo Más/Menos', 'Goles 1er tiempo': 'Goles 1.er tiempo Más/Menos', 'Ambos marcan': 'Ambos equipos anotan', 'Tarjetas (total)': 'Tarjetas Totales Más/Menos',
      'Tarjetas (equipo)': 'Tarjetas del equipo Más/Menos', 'Tarjetas 1T': 'Tarjetas 1.er tiempo Más/Menos', 'Resultado / hándicap': 'Resultado del partido', 'Remates (total)': 'Remates totales',
      'Remates (equipo)': 'Remates del equipo', 'Tiros al arco (total)': 'Tiros al Arco', 'Tiros al arco (equipo)': 'Tiros al Arco del equipo', 'Faltas (total)': 'Total de Faltas Cometidas',
      'Faltas (equipo)': 'Faltas del equipo', 'Saques de meta (total)': 'Total de Saques de meta', 'Saques de meta (equipo)': 'Saques de meta del equipo', 'Saques de banda (total)': 'Total de Saques de banda',
      'Fueras de lugar (equipo)': 'Fueras de lugar del equipo', 'Jugador: atajadas': 'Atajadas de Portero', 'Jugador: anota o asiste': 'Jugador que anota o da una asistencia', 'Jugador: anota': 'Anotar en cualquier momento',
      'Jugador: tiros al arco': 'Tiros al Arco del jugador', 'Jugador: remates': 'Remates totales del jugador', 'Jugador: faltas': 'Faltas cometidas del jugador', 'Jugador: entradas': 'Entradas del jugador',
      'Jugador: 2+ goles': 'Jugador que anota 2 o más goles', 'Jugador: anota o asiste (pareja)': 'Cualquiera de los jugadores anota o asiste'}

BOL = {}      # n -> boleto
LEGS = []     # selecciones


def leg(b, partido, sel, fam, amb, lado, linea, real, res, c=None, vivo=False):
    LEGS.append({'boleto': b, 'partido': partido, 'seleccion': sel, 'familia': fam, 'ambito': amb, 'lado': lado, 'linea': linea, 'valor_real': real, 'resultado': res, 'cuota_pata': c, 'vivo': vivo})


# nombres cortos
EST = 'Estudiantes de La Plata - Independiente Rivadavia'
CUR = 'Curazao - Panamá'
ESC = 'Escocia - Macedonia del Norte'
PBG = 'Países Bajos - Grecia'
ESL = 'Eslovenia - Suiza'
ARU = 'Argentina - Uruguay'
SME = 'Saint Martin - El Salvador'
NOG = 'Noruega - Gales'
GEH = 'Georgia - Hungría'
POD = 'Portugal - Dinamarca'
CHV = 'Chapecoense - Vasco da Gama'
TUB = 'Turquía - Bélgica'
ITF = 'Italia - Francia'
ING = 'Inglaterra - Croacia'
BAR = 'FC Barcelona (F) - Arsenal FC (F)'
JLY = 'Juventus (F) - Lyon (F)'

# ---- 9–12 nov (boletos 52–64): valores reales de Flashscore (registro/crudo_partidos) y, para jugadores, de su pestaña «Estadísticas de jugadores» (15-nov) ----
KRI, SAB, JUN, ICA, OCN = 'Kristiansund - Vålerenga', 'Sabadell - Real Sociedad B', 'Junior - Cúcuta', 'Internacional de Bogotá - América de Cali', 'Once Caldas - Atlético Nacional'
leg(52, KRI, 'Más de 3.5', 'Goles (total)', 'Partido', 'Más', 3.5, 1, F_, 5.1); leg(52, KRI, 'Más de 10.5', 'Córners (total)', 'Partido', 'Más', 10.5, 7, F_, 5.1); leg(52, KRI, 'Vålerenga gana', 'Resultado / hándicap', 'Partido', 'Selección', None, None, F_, 5.1)
leg(53, SAB, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 0, F_, 5.1); leg(53, SAB, 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 8, F_, 5.1); leg(53, SAB, 'Más de 5.5', 'Tarjetas (total)', 'Partido', 'Más', 5.5, 6, G, 5.1)
leg(54, JUN, 'Junior gana', 'Resultado / hándicap', 'Partido', 'Selección', None, None, G, 5.5); leg(54, JUN, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 2, F_, 5.5); leg(54, JUN, 'Más de 9.5', 'Córners (total)', 'Partido', 'Más', 9.5, 8, F_, 5.5)
leg(55, ICA, 'Más de 9.5', 'Córners (total)', 'Partido', 'Más', 9.5, 13, G, 2.87); leg(55, ICA, 'América o empate', 'Resultado / hándicap', 'Partido', 'Selección', None, None, G, 2.87)
leg(56, OCN, 'Más de 9.5', 'Córners (total)', 'Partido', 'Más', 9.5, 5, F_, 4.0); leg(56, OCN, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 2, F_, 4.0)
SHA, BRN, QUT = 'Sheffield Wednesday - Accrington Stanley', 'Barnsley - Oldham Athletic', 'Quindío - Tigres'
leg(57, SHA, 'Sí', 'Ambos marcan', 'Partido', 'Sí', None, None, F_); leg(57, BRN, 'Barnsley Menos de 3.5', 'Goles (equipo)', 'Equipo', 'Menos', 3.5, 5, F_); leg(57, JLY, 'Más de 0.5', 'Tarjetas (total)', 'Partido', 'Más', 0.5, 0, F_)
leg(58, JLY, 'Más de 0.5 (1T)', 'Tarjetas (total)', 'Partido', 'Más', 0.5, 0, F_, 2.7); leg(58, JLY, 'Más de 3.5 (1T)', 'Córners (total)', 'Partido', 'Más', 3.5, 2, F_, 2.7); leg(58, JLY, 'Lyon (F) -1', 'Resultado / hándicap', 'Partido', 'Selección', -1, None, G, 2.7)
IPA, LON = 'Independiente Petrolero - Always Ready', 'Londrina - Náutico'
leg(59, IPA, 'Menos de 3.5', 'Goles (total)', 'Partido', 'Menos', 3.5, 0, G); leg(59, LON, 'Menos de 5.5 (1T)', 'Córners (total)', 'Partido', 'Menos', 5.5, 4, G); leg(59, LON, 'Menos de 1.5 (1T)', 'Goles (total)', 'Partido', 'Menos', 1.5, 0, G)
leg(59, QUT, 'Menos de 2.5', 'Goles (total)', 'Partido', 'Menos', 2.5, 1, G); leg(59, QUT, 'Menos de 4.5 (1T)', 'Córners (total)', 'Partido', 'Menos', 4.5, 9, F_)
leg(60, TUB, 'Sí', 'Ambos marcan', 'Partido', 'Sí', None, None, G); leg(60, TUB, 'Lammens 3+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 3, 6, G); leg(60, TUB, 'Arda Güler 1+ tiros al arco', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, 3, G)
leg(60, BAR, 'Más de 3.5 (1T)', 'Córners (total)', 'Partido', 'Más', 3.5, 8, G); leg(60, BAR, 'Más de 0.5 (1T)', 'Tarjetas (total)', 'Partido', 'Más', 0.5, 0, F_)
leg(61, TUB, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 3, G, 2.22); leg(61, TUB, 'Lammens 3+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 3, 6, G, 2.22)
leg(62, 'Senegal - Sudán', 'Senegal -1', 'Resultado / hándicap', 'Partido', 'Selección', -1, None, G); leg(62, 'Senegal - Sudán', 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 10, G); leg(62, 'Costa de Marfil - Gambia', 'Costa de Marfil -1', 'Resultado / hándicap', 'Partido', 'Selección', -1, None, F_)
leg(63, ITF, 'Más de 3.5', 'Tarjetas (total)', 'Partido', 'Más', 3.5, 4, G, 5.8); leg(63, ITF, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 4, G, 5.8); leg(63, ITF, 'Donnarumma 4+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 4, 4, G, 5.8)
leg(63, ITF, 'Doué o Barcola anota o asiste', 'Jugador: anota o asiste (pareja)', 'Jugador', 'Línea jugador', None, 0, F_, 5.8)
leg(64, ITF, 'Olise anota o asiste', 'Jugador: anota o asiste', 'Jugador', 'Línea jugador', None, 1, G); leg(64, ITF, 'Más de 8.5', 'Tiros al arco (total)', 'Partido', 'Más', 8.5, 10, G)
leg(64, ING, 'Más de 8.5', 'Tiros al arco (total)', 'Partido', 'Más', 8.5, 9, G); leg(64, ING, 'Bellingham 3+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 3, 2, F_)

# ---- 12-nov noche (65–68) ----
leg(65, EST, 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 10, G, 2.25); leg(65, EST, 'Menos de 8.5', 'Tarjetas (total)', 'Partido', 'Menos', 8.5, None, G, 2.25); leg(65, EST, 'Ind. Rivadavia Más de 2.5', 'Tiros al arco (equipo)', 'Equipo', 'Más', 2.5, 4, G, 2.25)
leg(66, EST, 'Muslera 3+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 3, 2, F_, 2.02); leg(66, EST, 'Baltasar Rodríguez 2+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 2, 2, A, 2.02)
leg(67, CUR, 'Más de 2.5', 'Tarjetas (total)', 'Partido', 'Más', 2.5, 6, G, 4.45); leg(67, CUR, 'Curazao Más de 3.5', 'Córners (equipo)', 'Equipo', 'Más', 3.5, 4, G, 4.45); leg(67, CUR, 'Curazao Más de 0.5', 'Goles (equipo)', 'Equipo', 'Más', 0.5, 0, F_, 4.45)
leg(67, CUR, 'Curazao +2', 'Resultado / hándicap', 'Partido', 'Selección', 2, None, G, 4.45)
leg(68, EST, 'Ind. Rivadavia Más de 2.5', 'Córners (equipo)', 'Equipo', 'Más', 2.5, None, F_, 3.1); leg(68, EST, 'Más de 4.5', 'Tarjetas (total)', 'Partido', 'Más', 4.5, 9, G, 3.1)
# ---- 13-nov (69–79) ----
leg(69, 'Túnez - Libia', 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 12, G, 1.65); leg(69, 'Sudáfrica - Kenia', 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 9, G, 1.57); leg(69, 'Nigeria - Tanzania', 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 9, G, 1.52)
SAL = 'Serbia - Alemania'
leg(70, SAL, 'Menos de 3.5', 'Goles (total)', 'Partido', 'Menos', 3.5, 4, F_, 5.3); leg(70, SAL, 'Más de 9.5', 'Córners (total)', 'Partido', 'Más', 9.5, 6, F_, 5.3)
leg(70, SAL, 'Nmecha 1+ (mercado no legible)', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, None, A, 5.3); leg(70, SAL, 'Wirtz faltas cometidas (umbral no legible)', 'Jugador: faltas', 'Jugador', 'Línea jugador', None, 0, A, 5.3)
leg(71, ESC, 'Escocia gana', 'Resultado / hándicap', 'Partido', 'Selección', None, None, G, 1.90); leg(71, ESC, 'Menos de 29.5', 'Remates (total)', 'Partido', 'Menos', 29.5, 25, G, 1.90)
leg(71, PBG, 'Malen anota o asiste', 'Jugador: anota o asiste', 'Jugador', 'Línea jugador', None, 3, G, 2.87); leg(71, PBG, 'Grecia Más de 2.5', 'Tiros al arco (equipo)', 'Equipo', 'Más', 2.5, 1, F_, 2.87); leg(71, PBG, 'Verbruggen 2+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 2, 1, F_, 2.87)
leg(71, ESL, 'Eslovenia Más de 2.5', 'Córners (equipo)', 'Equipo', 'Más', 2.5, 7, G, 2.27); leg(71, ESL, 'Más de 1.5', 'Goles (total)', 'Partido', 'Más', 1.5, 0, F_, 2.27)
leg(72, ESC, 'McTominay 1+ tiros al arco', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, 2, G, 1.78); leg(72, ESC, 'Más de 3.5 (1T)', 'Córners (total)', 'Partido', 'Más', 3.5, 7, G, 1.78)
leg(72, ESL, 'Más de 3.5', 'Tarjetas (total)', 'Partido', 'Más', 3.5, 2, F_, 1.72); leg(72, PBG, 'Retsos 2+ entradas', 'Jugador: entradas', 'Jugador', 'Línea jugador', 2, 0, F_, 1.82)
leg(73, ESC, 'Macedonia del Norte Más de 2.5', 'Córners (equipo)', 'Equipo', 'Más', 2.5, 5, G, 1.57); leg(73, PBG, 'Más de 1.5', 'Tarjetas (total)', 'Partido', 'Más', 1.5, 0, F_, 1.72)
leg(74, ARU, 'Menos de 4.5 (1T)', 'Córners (total)', 'Partido', 'Menos', 4.5, 4, G, 6.10); leg(74, ARU, 'Nico Paz anota', 'Jugador: anota', 'Jugador', 'Línea jugador', None, 0, F_, 6.10); leg(74, ARU, 'Argentina gana', 'Resultado / hándicap', 'Partido', 'Selección', None, None, F_, 6.10)
leg(74, SME, 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 5, F_, 1.40)
leg(75, ARU, 'Más de 1.5', 'Goles (total)', 'Partido', 'Más', 1.5, 3, G, 1.98); leg(75, 'Ecuador - Costa Rica', 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 12, G, 1.50); leg(75, SME, 'Saint Martin Más de 3.5', 'Córners (equipo)', 'Equipo', 'Más', 3.5, 5, G, 2.07)
leg(75, 'Colombia - Chile', 'Luis Suárez anota', 'Jugador: anota', 'Jugador', 'Línea jugador', None, None, A, 2.00)
leg(76, ARU, 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 9, G, 4.25); leg(76, ARU, 'Sí', 'Ambos marcan', 'Partido', 'Sí', None, None, G, 4.25)
leg(77, 'Montserrat - Nicaragua', 'Nicaragua gana', 'Resultado / hándicap', 'Partido', 'Selección', None, None, G, 2.07); leg(77, 'Colombia - Chile', 'Colombia Más de 0.5', 'Goles (equipo)', 'Equipo', 'Más', 0.5, 1, G, 1.29)
# ---- 13-nov noche (78–79) ----
leg(78, 'Guerreros del Pacífico - FC Santiago', 'Sí', 'Ambos marcan', 'Partido', 'Sí', None, None, G, 1.50); leg(78, 'Internacional de Bogotá - Independiente Santa Fe', 'Sí', 'Ambos marcan', 'Partido', 'Sí', None, None, F_, 1.60)
leg(78, 'Guatemala - Canadá', 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 7, F_, 2.45); leg(78, 'Guatemala - Canadá', 'Más de 3.5', 'Tarjetas (total)', 'Partido', 'Más', 3.5, 7, G, 2.45)
JB, VC, KI = 'Japón - Brasil', 'Real Valladolid - Castellón', 'Kosovo - Israel'
leg(79, JB, 'Brasil Más de 0.5', 'Tarjetas (equipo)', 'Equipo', 'Más', 0.5, 4, G, 2.02); leg(79, JB, 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 10, G, 2.02)
leg(79, VC, 'Más de 5.5', 'Tarjetas (total)', 'Partido', 'Más', 5.5, 7, G, 1.95); leg(79, VC, 'Más de 1.5', 'Goles (total)', 'Partido', 'Más', 1.5, 1, F_, 1.95)
leg(79, KI, 'Menos de 9.5', 'Córners (total)', 'Partido', 'Menos', 9.5, 9, G, 1.93); leg(79, KI, 'Israel Menos de 1.5', 'Goles (equipo)', 'Equipo', 'Menos', 1.5, 0, G, 1.93)
# ---- 14-nov (80–89) ----
leg(80, NOG, 'Haaland anota 2 o más goles', 'Jugador: 2+ goles', 'Jugador', 'Línea jugador', 2, 1, F_, 2.20); leg(80, GEH, 'Szoboszlai 2+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 2, 0, F_, 1.75); leg(80, GEH, 'Georgia Menos de 1.5', 'Goles (equipo)', 'Equipo', 'Menos', 1.5, 0, G, 1.75)
leg(81, NOG, 'Ødegaard anota o asiste', 'Jugador: anota o asiste', 'Jugador', 'Línea jugador', None, 0, F_, 2.40); leg(81, NOG, 'Gales Más de 2.5', 'Córners (equipo)', 'Equipo', 'Más', 2.5, 2, F_, 2.40); leg(81, NOG, 'Noruega gana', 'Resultado / hándicap', 'Partido', 'Selección', None, None, G, 2.40)
leg(81, GEH, 'Szoboszlai 1+ tiros al arco', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, 0, F_, 2.37); leg(81, GEH, 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 14, G, 2.37)
RP, SB, IU = 'Rumanía - Polonia', 'Suecia - Bosnia y Herzegovina', 'Irlanda del Norte - Ucrania'
leg(82, RP, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 3, G, 1.67); leg(82, SB, 'Suecia Menos de 18.5', 'Remates (equipo)', 'Equipo', 'Menos', 18.5, 13, G, 1.62)
leg(82, POD, 'Dinamarca Más de 2.5', 'Córners (equipo)', 'Equipo', 'Más', 2.5, 7, G, 2.85); leg(82, POD, 'D. Costa 2+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 2, None, A, 2.85); leg(82, POD, 'Hjulmand 1+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 1, 2, G, 2.85)
leg(82, IU, 'Ucrania Más de 9.5', 'Remates (equipo)', 'Equipo', 'Más', 9.5, 7, F_, 1.50)
leg(83, POD, 'Dinamarca Más de 1.5', 'Fueras de lugar (equipo)', 'Equipo', 'Más', 1.5, 1, F_, 6.8); leg(83, POD, 'Dinamarca Más de 10.5', 'Remates (equipo)', 'Equipo', 'Más', 10.5, 17, G, 6.8)
leg(83, POD, 'Más de 9.5', 'Córners (total)', 'Partido', 'Más', 9.5, 13, G, 6.8); leg(83, POD, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 5, G, 6.8)
MIA, NOC, AMT, CTO = 'Millonarios - Alianza', 'Atlético Nacional - Once Caldas', 'Águilas Doradas - Independiente Medellín', 'Deportivo Cali - Deportes Tolima'
leg(84, MIA, 'Menos de 3.5', 'Goles (total)', 'Partido', 'Menos', 3.5, 2, G, 2.05); leg(84, MIA, 'Menos de 11.5', 'Córners (total)', 'Partido', 'Menos', 11.5, 7, G, 2.05); leg(84, NOC, 'Menos de 3.5', 'Goles (total)', 'Partido', 'Menos', 3.5, 2, G, 1.42)
leg(84, AMT, 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 8, F_, 1.52); leg(84, CTO, 'Tolima Más de 3.5', 'Córners (equipo)', 'Equipo', 'Más', 3.5, 3, F_, 1.98); leg(84, CTO, 'Cali Más de 0.5', 'Goles (equipo)', 'Equipo', 'Más', 0.5, 2, G, 1.98)
# 85 y 86: cash out antes de jugarse -> las selecciones no se liquidaron; se dejan con el valor real del partido pero sin resultado (Anulada)
leg(85, CHV, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 2, A, 6.7); leg(85, CHV, 'Más de 16.5', 'Saques de meta (total)', 'Partido', 'Más', 16.5, 25, A, 6.7)
leg(85, CHV, 'Chapecoense Más de 3.5', 'Córners (equipo)', 'Equipo', 'Más', 3.5, 6, A, 6.7); leg(85, CHV, 'Gabriel Pereira 1+ faltas cometidas', 'Jugador: faltas', 'Jugador', 'Línea jugador', 1, None, A, 6.7)
leg(86, CHV, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 2, A, 5.7); leg(86, CHV, 'Chapecoense Más de 4.5', 'Córners (equipo)', 'Equipo', 'Más', 4.5, 6, A, 5.7); leg(86, CHV, 'Más de 35.5', 'Saques de banda (total)', 'Partido', 'Más', 35.5, 31, A, 5.7)
MIR = 'Mirassol - Atlético Mineiro'
leg(87, MIR, 'Atlético-MG Más de 11.5', 'Remates (equipo)', 'Equipo', 'Más', 11.5, 16, G, 3.0); leg(87, MIR, 'Mirassol Más de 6.5', 'Saques de meta (equipo)', 'Equipo', 'Más', 6.5, 11, G, 3.0)
leg(87, MIR, 'Más de 15.5', 'Saques de meta (total)', 'Partido', 'Más', 15.5, 21, G, 3.0); leg(87, MIR, 'Más de 8.5', 'Córners (total)', 'Partido', 'Más', 8.5, 7, F_, 3.0)
leg(88, CHV, 'Más de 16.5', 'Saques de meta (total)', 'Partido', 'Más', 16.5, 25, G, 6.0); leg(88, CHV, 'Chapecoense Más de 4.5', 'Córners (equipo)', 'Equipo', 'Más', 4.5, 6, G, 6.0); leg(88, CHV, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 2, F_, 6.0)
BB_ = 'Banfield - Boca Juniors'
leg(89, BB_, 'Banfield Más de 10.5', 'Remates (equipo)', 'Equipo', 'Más', 10.5, 12, G, 5.7); leg(89, BB_, 'Boca Menos de 17.5', 'Remates (equipo)', 'Equipo', 'Menos', 17.5, 15, G, 5.7)
leg(89, BB_, 'Menos de 9.5', 'Tiros al arco (total)', 'Partido', 'Menos', 9.5, 8, G, 5.7); leg(89, BB_, 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 5, F_, 5.7)
# ---- 15-nov (90–94) ----
CM, GL, TC, LA = 'Chipre - Montenegro', 'Granada - Las Palmas', 'Tenerife - Ceuta', 'Letonia - Armenia'
leg(90, CM, 'Chipre Más de 0.5', 'Goles (equipo)', 'Equipo', 'Más', 0.5, 1, G, 1.31); leg(90, GL, 'Más de 4.5', 'Tarjetas (total)', 'Partido', 'Más', 4.5, 8, G, 1.60); leg(90, TC, 'Más de 4.5', 'Tarjetas (total)', 'Partido', 'Más', 4.5, 4, F_, 1.47)
leg(90, LA, 'Letonia Más de 0.5', 'Goles (equipo)', 'Equipo', 'Más', 0.5, 0, F_, 1.50)
BA, FSM, ES, EC = 'Bielorrusia - Albania', 'Finlandia - San Marino', 'Eldense - Sabadell', 'Eibar - Cádiz'
leg(91, BA, 'Menos de 2.5', 'Goles (total)', 'Partido', 'Menos', 2.5, 2, G, 2.47); leg(91, BA, 'Menos de 6.5', 'Tarjetas (total)', 'Partido', 'Menos', 6.5, 6, G, 2.47)
leg(91, FSM, 'Finlandia -2', 'Resultado / hándicap', 'Partido', 'Selección', -2, None, G, 2.50); leg(91, FSM, 'Finlandia -5.5 (córners)', 'Córners (equipo)', 'Equipo', 'Selección', -5.5, 4, F_, 2.50)
leg(91, ES, 'Más de 4.5', 'Tarjetas (total)', 'Partido', 'Más', 4.5, 6, G, 1.90); leg(91, ES, 'Eldense Más de 3.5', 'Córners (equipo)', 'Equipo', 'Más', 3.5, 1, F_, 1.90)
leg(91, EC, 'Más de 7.5', 'Córners (total)', 'Partido', 'Más', 7.5, 6, F_, 2.05); leg(91, EC, 'Cádiz Más de 0.5', 'Goles (equipo)', 'Equipo', 'Más', 0.5, 1, G, 2.05)
EI, FT_, BIT, CRC = 'España - Inglaterra', 'Francia - Turquía', 'Bélgica - Italia', 'Croacia - República Checa'
leg(92, EI, 'Kane 1+ tiros al arco', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, 1, G, 1.83); leg(92, EI, 'Cucurella 1+ faltas', 'Jugador: faltas', 'Jugador', 'Línea jugador', 1, 2, G, 1.83)
leg(92, FT_, 'Jacquet 1+ faltas', 'Jugador: faltas', 'Jugador', 'Línea jugador', 1, 1, G, 2.10); leg(92, FT_, 'Özer 3+ atajadas', 'Jugador: atajadas', 'Jugador', 'Línea jugador', 3, 7, G, 2.10); leg(92, FT_, 'Olise 1+ tiros al arco', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, 2, G, 2.10)
leg(92, BIT, 'Italia Más de 3.5', 'Tiros al arco (equipo)', 'Equipo', 'Más', 3.5, 4, G, 2.27); leg(92, BIT, 'Tonali 1+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 1, 0, F_, 2.27); leg(92, BIT, 'De Bruyne 3+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 3, 5, G, 2.27)
leg(92, CRC, 'Červ 1+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 1, 0, F_, 2.42); leg(92, CRC, 'Croacia Menos de 6.5', 'Córners (equipo)', 'Equipo', 'Menos', 6.5, 5, G, 2.42); leg(92, CRC, 'Menos de 5.5', 'Tarjetas (total)', 'Partido', 'Menos', 5.5, 2, G, 2.42)
leg(93, EI, 'Bellingham 2+ remates', 'Jugador: remates', 'Jugador', 'Línea jugador', 2, 2, G, 5.8); leg(93, EI, 'Menos de 29.5', 'Remates (total)', 'Partido', 'Menos', 29.5, 32, F_, 5.8)
leg(93, EI, 'Kane o Bellingham anota o asiste', 'Jugador: anota o asiste (pareja)', 'Jugador', 'Línea jugador', None, 2, G, 5.8); leg(93, EI, 'Más de 2.5', 'Goles (total)', 'Partido', 'Más', 2.5, 5, G, 5.8)
leg(94, BIT, 'Menos de 5.5', 'Tarjetas (total)', 'Partido', 'Menos', 5.5, 3, G, 5.4); leg(94, BIT, 'Italia Menos de 12.5', 'Faltas (equipo)', 'Equipo', 'Menos', 12.5, 11, G, 5.4)
leg(94, BIT, 'Más de 8.5', 'Tiros al arco (total)', 'Partido', 'Más', 8.5, 14, G, 5.4); leg(94, BIT, 'De Ketelaere 1+ tiros al arco', 'Jugador: tiros al arco', 'Jugador', 'Línea jugador', 1, 0, F_, 5.4)


def boletos():
    d = {}
    for p in [os.path.join(RAIZ, 'registro', 'boletos_9-12nov.json')] + sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'balance', 'boletos_betano.json'))):
        for b in json.load(open(p, encoding='utf8'))['boletos']:
            d[b['n']] = b
    return d


def marcador(nombre, partidos):
    n = nombre.split(' - ')
    for p in partidos:
        if p['Partido'] == nombre:
            return p['Marcador']
    return None


def main():
    P = construir_partidos()
    bol = boletos()
    por_nombre = {p['Partido']: p for p in P}
    ligas = {p['Partido']: p['Liga'] for p in P}
    extra_mc = {'Guerreros del Pacífico - FC Santiago': ('1-1', '')}
    S = []
    for i, lg in enumerate(LEGS, start=1):
        b = bol[lg['boleto']]
        p = por_nombre.get(lg['partido'])
        mc = p['Marcador'] if p else extra_mc.get(lg['partido'], (None, ''))[0]
        liga = p['Liga'] if p else extra_mc.get(lg['partido'], (None, ''))[1]
        S.append({'n': 1000 + i, 'boleto': lg['boleto'], 'codigo': str(b.get('codigo') or ''), 'fecha': b['fecha'], 'partido': lg['partido'], 'liga': liga, 'marcador': mc,
                  'mercado_betano': MK.get(lg['familia'], lg['familia']), 'seleccion': lg['seleccion'], 'familia': lg['familia'], 'ambito': lg['ambito'], 'lado': lg['lado'],
                  'linea': lg['linea'], 'valor_real': lg['valor_real'], 'resultado': lg['resultado'], 'cuota_pata': lg['cuota_pata'], 'tipo_boleto': b['tipo'], 'vivo': lg['vivo']})
    # patas de los boletos 52–64 (para la pestaña Boletos)
    pcs = {}
    for s in S:
        if 52 <= s['boleto'] <= 64:
            q = pcs.setdefault(str(s['boleto']), {'falla': '', 'patas': []})
            q['patas'].append([f"{s['seleccion']} · {s['partido']}", '✓' if s['resultado'] == G else '✗' if s['resultado'] == F_ else '?', '–' if s['valor_real'] is None else str(s['valor_real'])])
    for n, q in pcs.items():
        malas = [x[0] for x in q['patas'] if x[1] == '✗']
        q['falla'] = ('Falló: ' + '; '.join(malas)) if malas and bol[int(n)]['resultado'] == 'Perdida' else ''
    # coherencia: el resultado del boleto contra sus selecciones
    avisos = []
    for n in sorted({s['boleto'] for s in S}):
        ss = [s for s in S if s['boleto'] == n]
        res = bol[n]['resultado']
        ok = all(s['resultado'] == G for s in ss)
        mal = any(s['resultado'] == F_ for s in ss)
        if res == 'Ganada' and mal:
            avisos.append(f'boleto {n}: ganado pero una selección figura perdida')
        if res == 'Perdida' and ok:
            avisos.append(f'boleto {n}: perdido pero todas las selecciones figuran ganadas')
        if res == 'Perdida' and not mal and not ok:
            pass
    json.dump({'fuente': 'Flashscore (feeds df_st/df_sur y pestaña «Estadísticas de jugadores»), leído el 15-nov-2026 con el navegador; boletos de Betano. Ver recoleccion/historico_extra.py',
               'selecciones': S, 'partidos': P}, open(os.path.join(RAIZ, 'registro', 'historico_9-15nov.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    json.dump(pcs, open(os.path.join(RAIZ, 'registro', 'patas_calificadas_9-12nov.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(len(S), 'selecciones de', len({s['boleto'] for s in S}), 'boletos;', len(P), 'partidos')
    for a in avisos:
        print('AVISO', a)


if __name__ == '__main__':
    main()
