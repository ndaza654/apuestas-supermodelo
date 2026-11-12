# -*- coding: utf-8 -*-
"""Base de cada liga (prior) medida con datos reales: ago-2022 a nov-2026, 38 ligas (datos/prior_liga.csv).

Fuente: copia pública de football-data.co.uk (github.com/xgabora/Club-Football-Match-Data-2000-2025). Tarjetas en
puntos de Betano (amarilla 1, roja 2). Ligas sin córners/tarjetas en la fuente (Argentina, Brasil, México, MLS,
nórdicas...) solo traen goles y resultado. Colombia y Ecuador NO están: su base saldrá del registro propio
(partidos.csv), que se mezcla con este prior cuando haya partidos (ver `prior`).

Para qué sirve (no cambia el precio de Betano):
  · media de tarjetas de la liga para el árbitro cuando la ficha no la trae (lección del 9-nov);
  · línea base del informe: "en esta liga el Más 2.5 sale el 57 %, los córners promedian 10,3";
  · valores por defecto de las estadísticas que Betano no cotiza en ese partido (en vez de un promedio genérico);
  · objetivo del encogimiento del modelo de perfiles (si algún día se enciende).
"""
import csv, os, unicodedata

RUTA = os.path.join(os.path.dirname(__file__), '..', 'datos', 'prior_liga.csv')
RUTA_PROPIA = os.path.join(os.path.dirname(__file__), '..', 'datos', 'partidos.csv')

# Reconocimiento del nombre de la liga: primero el PAÍS (si el texto lo trae), después la categoría dentro del país.
# Así «Austria Bundesliga» no cae en Alemania, «Rusia Premier League» no cae en Inglaterra y «Egipto Premier League» o
# «Ecuador Serie A» devuelven None (no están en la fuente) en vez de una liga equivocada.
PAISES = {
    'inglaterra': 'ENG', 'england': 'ENG', 'espana': 'ESP', 'spain': 'ESP', 'italia': 'ITA', 'italy': 'ITA',
    'alemania': 'GER', 'germany': 'GER', 'francia': 'FRA', 'france': 'FRA', 'paises bajos': 'NED', 'holanda': 'NED',
    'netherlands': 'NED', 'portugal': 'POR', 'belgica': 'BEL', 'belgium': 'BEL', 'turquia': 'TUR', 'turkey': 'TUR',
    'grecia': 'GRE', 'greece': 'GRE', 'escocia': 'SCO', 'scotland': 'SCO', 'argentina': 'ARG', 'brasil': 'BRA', 'brazil': 'BRA',
    'mexico': 'MEX', 'estados unidos': 'USA', 'usa': 'USA', 'eeuu': 'USA', 'japon': 'JAP', 'japan': 'JAP', 'china': 'CHN',
    'austria': 'AUT', 'dinamarca': 'DEN', 'denmark': 'DEN', 'finlandia': 'FIN', 'finland': 'FIN', 'irlanda': 'IRL',
    'ireland': 'IRL', 'noruega': 'NOR', 'norway': 'NOR', 'polonia': 'POL', 'poland': 'POL', 'rumania': 'ROM', 'romania': 'ROM',
    'rusia': 'RUS', 'russia': 'RUS', 'suiza': 'SUI', 'switzerland': 'SUI', 'suecia': 'SWE', 'sweden': 'SWE',
    'inglesa': 'ENG', 'espanola': 'ESP', 'italiana': 'ITA', 'alemana': 'GER', 'francesa': 'FRA', 'holandesa': 'NED',
    'portuguesa': 'POR', 'turca': 'TUR', 'escocesa': 'SCO', 'brasilena': 'BRA', 'mexicana': 'MEX',
}
# Países sin datos en la fuente (se devuelve None para no confundirlos con otra liga del mismo nombre).
SIN_DATOS = ['colombia', 'ecuador', 'peru', 'chile', 'uruguay', 'paraguay', 'bolivia', 'venezuela', 'egipto', 'egypt',
             'ucrania', 'ukraine', 'gales', 'wales', 'arabia', 'saudi', 'catar', 'qatar', 'emiratos', 'iran', 'marruecos',
             'sudafrica', 'australia', 'corea', 'korea', 'india', 'israel', 'croacia', 'serbia', 'chequia', 'eslovaquia',
             'eslovenia', 'hungria', 'bulgaria', 'chipre', 'islandia', 'estonia', 'letonia', 'lituania', 'malasia', 'costa rica',
             'honduras', 'guatemala', 'el salvador', 'panama', 'canada', 'irlanda del norte', 'northern ireland']


def _segunda(t):
    return bool(__import__('re').search(r'(^| )(2|ii|b|segunda|second|hypermotion)( |$)', t)) or '2.' in t


def _por_pais(pais, t):
    if pais == 'ENG':
        for k, c in (('national league', 'EC'), ('league two', 'E3'), ('league 2', 'E3'), ('league one', 'E2'), ('league 1', 'E2'),
                     ('championship', 'E1'), ('premier', 'E0')):
            if k in t:
                return c
        return 'E0'
    if pais == 'SCO':
        for k, c in (('league two', 'SC3'), ('league one', 'SC2'), ('championship', 'SC1'), ('premiership', 'SC0'), ('premier', 'SC0')):
            if k in t:
                return c
        return 'SC0'
    dos = {'ESP': ('SP1', 'SP2'), 'ITA': ('I1', 'I2'), 'GER': ('D1', 'D2'), 'FRA': ('F1', 'F2')}
    if pais in dos:
        uno, d2 = dos[pais]
        if pais == 'ITA' and 'serie b' in t:
            return d2
        if pais == 'FRA' and 'ligue 2' in t:
            return d2
        if pais == 'ESP' and ('laliga 2' in t or 'la liga 2' in t or 'segunda' in t or 'hypermotion' in t):
            return d2
        if pais == 'GER' and ('2. bundesliga' in t or '2 bundesliga' in t or 'bundesliga 2' in t or 'zweite' in t):
            return d2
        return uno
    simple = {'NED': 'N1', 'POR': 'P1', 'BEL': 'B1', 'TUR': 'T1', 'GRE': 'G1', 'ARG': 'ARG', 'BRA': 'BRA', 'MEX': 'MEX', 'USA': 'USA',
              'JAP': 'JAP', 'CHN': 'CHN', 'AUT': 'AUT', 'DEN': 'DEN', 'FIN': 'FIN', 'IRL': 'IRL', 'NOR': 'NOR', 'POL': 'POL',
              'ROM': 'ROM', 'RUS': 'RUS', 'SUI': 'SUI', 'SWE': 'SWE'}
    if pais in simple:
        return None if _segunda(t.replace(_quitar_pais(t), '')) else simple[pais]
    return None


def _quitar_pais(t):
    for p in sorted(PAISES, key=len, reverse=True):
        if p in t:
            return p
    return ''


# Nombres de liga sin país (lo que más se escribe en Betano o en el chat).
SIN_PAIS = [('premier league', 'E0'), ('epl', 'E0'), ('efl championship', 'E1'), ('championship', 'E1'), ('league one', 'E2'),
            ('league two', 'E3'), ('national league', 'EC'), ('laliga hypermotion', 'SP2'), ('laliga 2', 'SP2'), ('la liga 2', 'SP2'),
            ('laliga', 'SP1'), ('la liga', 'SP1'), ('liga ea sports', 'SP1'), ('serie a tim', 'I1'), ('serie a enilive', 'I1'),
            ('2. bundesliga', 'D2'), ('2 bundesliga', 'D2'), ('bundesliga 2', 'D2'), ('bundesliga', 'D1'), ('ligue 1', 'F1'),
            ('ligue 2', 'F2'), ('eredivisie', 'N1'), ('primeira liga', 'P1'), ('liga portugal', 'P1'), ('jupiler', 'B1'),
            ('super lig', 'T1'), ('scottish premiership', 'SC0'), ('brasileirao', 'BRA'), ('liga mx', 'MEX'), ('mls', 'USA'),
            ('j1 league', 'JAP'), ('j league', 'JAP'), ('eliteserien', 'NOR'), ('allsvenskan', 'SWE'), ('ekstraklasa', 'POL'),
            ('veikkausliiga', 'FIN')]
_DATOS = None


def _norm(t):
    t = unicodedata.normalize('NFKD', str(t or '')).encode('ascii', 'ignore').decode().lower()
    return ' '.join(t.replace('-', ' ').replace('·', ' ').split())


def cargar():
    global _DATOS
    if _DATOS is None:
        _DATOS = {}
        try:
            for r in csv.DictReader(open(RUTA, encoding='utf-8')):
                _DATOS[r['liga']] = {k: (float(v) if v not in ('', None) and k not in ('liga', 'nombre') else v) for k, v in r.items()}
        except OSError:
            pass
    return _DATOS


def codigo(liga):
    """Código de la liga a partir del texto libre ('Inglaterra · Premier League' → 'E0'). None si no se reconoce o si es
    de un país que no está en la fuente. 'Serie A' sola es ambigua (Italia, Brasil, Ecuador): devuelve None."""
    t = _norm(liga)
    if not t:
        return None
    if t.upper() in cargar():
        return t.upper()
    for r in cargar().values():            # el nombre exacto del CSV (p. ej. 'Escocia League One')
        if _norm(r.get('nombre')) == t:
            return r['liga']
    import re
    for p in sorted(SIN_DATOS, key=len, reverse=True):
        if re.search(r'(^| )' + re.escape(p) + r'( |$)', t):
            return None
    pais = None
    for p in sorted(PAISES, key=len, reverse=True):
        if re.search(r'(^| )' + re.escape(p) + r'( |$)', t):
            pais = PAISES[p]
            break
    if pais:
        return _por_pais(pais, t)
    for k, c in SIN_PAIS:
        if re.search(r'(^| )' + re.escape(k) + r'( |$)', t):
            return c
    return None


def clave(liga):
    """Clave estable de una liga para la base propia: el código si está en la fuente; si no, el nombre sin jornada, fecha,
    grupo ni fase ('Ecuador LigaPro - Grupo descenso J6' → 'ecuador ligapro')."""
    cod = codigo(liga)
    if cod:
        return cod
    import re
    t = _norm(liga)
    t = re.split(r' - | \| |, |\(', t)[0]
    t = re.sub(r'\b(j|jornada|fecha|f|ronda|round|matchday|md)\s*\d+\b', ' ', t)
    t = re.sub(r'\b(grupo|group|fase|hexagonal|cuadrangular|apertura|clausura|playoffs?|liguilla|descenso|final(es)?)\b.*$', ' ', t)
    return ' '.join(t.split())


def prior(liga):
    """Dict con la base de la liga o None. Si el registro propio (partidos.csv) tiene ≥ 20 partidos de esa liga,
    se mezcla: peso propio = n / (n + 100) (100 partidos propios pesan como el prior)."""
    cod = codigo(liga)
    base = dict(cargar().get(cod) or {}) if cod else {}
    propio = _propio(liga)
    if propio and propio['partidos'] >= 20:
        w = propio['partidos'] / (propio['partidos'] + 100.0)
        for k, v in propio.items():
            if k == 'partidos':
                continue
            if base.get(k) not in (None, ''):
                base[k] = (1 - w) * base[k] + w * v
            else:
                base[k] = v
        base['partidos_propios'] = propio['partidos']
        base.setdefault('nombre', liga)
    return base or None


def _propio(liga):
    """Medias de la liga en el registro propio de partidos (lo llena registro.cerrar_partido)."""
    if not os.path.exists(RUTA_PROPIA):
        return None
    k = clave(liga)
    filas = [r for r in csv.DictReader(open(RUTA_PROPIA, encoding='utf-8-sig'), delimiter=';')
             if (r.get('liga_clave') or clave(r.get('liga'))) == k]
    if not filas:
        return None
    f = lambda k: [float(r[k]) for r in filas if r.get(k) not in (None, '', 'None')]
    out = {'partidos': len(filas)}
    gl, gv = f('goles_local'), f('goles_visitante')
    if gl and gv:
        g = [a + b for a, b in zip(gl, gv)]
        out.update(goles_x_partido=sum(g) / len(g), goles_local=sum(gl) / len(gl), goles_visitante=sum(gv) / len(gv),
                   pct_mas_2_5=sum(x >= 3 for x in g) / len(g),
                   pct_ambos_marcan=sum(a > 0 and b > 0 for a, b in zip(gl, gv)) / len(g))
    cl, cv = f('corners_local'), f('corners_visitante')
    if len(cl) >= 10 and len(cl) == len(cv):
        c = [a + b for a, b in zip(cl, cv)]
        out.update(corners_x_partido=sum(c) / len(c), corners_local=sum(cl) / len(cl), corners_visitante=sum(cv) / len(cv))
    tl, tv = f('tarjetas_local'), f('tarjetas_visitante')
    if len(tl) >= 10 and len(tl) == len(tv):
        out.update(tarjetas_betano_x_partido=sum(a + b for a, b in zip(tl, tv)) / len(tl),
                   tarjetas_local=sum(tl) / len(tl), tarjetas_visitante=sum(tv) / len(tv))
    return out


def resumen(liga):
    """Texto corto para el informe."""
    p = prior(liga)
    if not p:
        return None
    partes = [f"{p.get('nombre', liga)}"]
    if p.get('goles_x_partido'):
        partes.append(f"{p['goles_x_partido']:.2f} goles/partido, Más 2.5 {p['pct_mas_2_5'] * 100:.0f} %, ambos marcan {p['pct_ambos_marcan'] * 100:.0f} %")
    if p.get('corners_x_partido'):
        partes.append(f"córners {p['corners_x_partido']:.1f}")
    if p.get('tarjetas_betano_x_partido'):
        partes.append(f"tarjetas (amarilla 1, roja 2) {p['tarjetas_betano_x_partido']:.1f}")
    n = int(p.get('partidos', 0) or 0)
    fuente = f"{n} partidos ago-2022/nov-2026" if n else ''
    if p.get('partidos_propios'):
        fuente += f" + {int(p['partidos_propios'])} del registro propio"
    return ' · '.join(partes) + (f' ({fuente})' if fuente else '')
