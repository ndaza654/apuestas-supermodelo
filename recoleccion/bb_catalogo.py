# -*- coding: utf-8 -*-
"""Catálogo del Bet Builder de Betano (página /betbuilder/<id>/?bt=10 → API cuotas-de-partido) → selecciones del modelo.

Cada selección del catálogo se traduce al mismo diccionario `sel` que usa el súper modelo (`{'mercado','ambito','linea','lado'}`),
así se puede pedir al modelo la probabilidad conjunta y a Betano el precio real del trío (ver `bb_precios.py` y `bb_precios_betano.js`).
El catálogo lo guarda `recoleccion/bb_catalogo_extraer.js` en `jornadas/AAAA-MM-DD/bb/catalogo_HHMM.json`:
  {clave: {id, name, start, leida, allowed, m: [{i, n, t, h, s: [[id, nombre, precio, handicap, nombreCompleto]], sc}]}}
Solo se traducen los mercados que el modelo sabe calcular (goles, córners, tarjetas, al arco, remates, fueras, saques, faltas, resultado,
doble oportunidad, ambos marcan, ambos con tarjetas, 1T/2T). Los de jugador no se traducen aquí.
"""
import re, json, unicodedata


def _n(t):
    return unicodedata.normalize('NFKD', str(t)).encode('ascii', 'ignore').decode().lower().strip()


# (nombre exacto del mercado total) → (mercado del modelo, ámbito)
TOTALES = {
    'Goles totales Más/Menos': ('goles', 'total'),
    'Tiros de esquina Menos/Más': ('corners', 'total'),
    'Tarjetas Totales Más/Menos': ('tarjetas', 'total'),
    'Tiros al Arco': ('al_arco', 'total'),
    'Remates totales': ('remates', 'total'),
    'Total de Fueras de lugar': ('fueras', 'total'),
    'Total de Saques de meta': ('saques_meta', 'total'),
    'Total de Faltas Cometidas': ('faltas', 'total'),
    'Total de Saques de banda': ('saques_banda', 'total'),
    'Goles en Primer Tiempo': ('goles', '1T'),
    'Tiros de esquina en Primer Tiempo': ('corners', '1T'),
    'Tarjetas Totales (Más/Menos) Primer Tiempo': ('tarjetas', '1T'),
    'Más/Menos Goles en Segundo Tiempo': ('goles', '2T'),
    'Tiros de esquina en Segundo Tiempo Más/Menos': ('corners', '2T'),
}
# sufijo de los mercados por equipo: «<equipo> <sufijo>» o «<equipo> - <sufijo>»
EQUIPO = {
    'Goles totales Más/Menos': 'goles',
    'Tiros de esquina Menos/Más': 'corners',
    'Tarjetas Totales Más/Menos': 'tarjetas',
    'Tiros al Arco': 'al_arco',
    'Remates totales': 'remates',
    'Total de Fueras de lugar': 'fueras',
    'Total de Saques de meta': 'saques_meta',
    'Total de Faltas Cometidas': 'faltas',
    'Total de Saques de banda': 'saques_banda',
}
RE_LADO = re.compile(r'^(M[aá]s de|Menos)\s+([0-9]+(?:\.[0-9]+)?)$', re.I)


def _lado_linea(nombre):
    m = RE_LADO.match(nombre.strip())
    if not m:
        return None
    return ('mas' if m.group(1).lower().startswith('m') and 'menos' not in m.group(1).lower() else 'menos'), float(m.group(2))


def traducir(cat, local, visitante):
    """cat = catálogo de UN partido. Devuelve lista de dicts {sel, id, precio, mercado, nombre} (solo mercados que el modelo calcula)."""
    out = []
    nl, nv = _n(local), _n(visitante)

    def add(sel, s, mercado):
        out.append(dict(sel=sel, id=s[0], precio=s[2], mercado=mercado, nombre=s[1]))

    for m in cat['m']:
        n = m['n']
        ambito = None
        if n in TOTALES:
            merc, ambito = TOTALES[n]
        else:
            merc = None
            for suf, mm in EQUIPO.items():
                for eq, amb in ((local, 'local'), (visitante, 'visitante')):
                    if _n(n) in (_n(f'{eq} {suf}'), _n(f'{eq} - {suf}')):
                        merc, ambito = mm, amb
            if merc is None:
                pass
        if merc:
            for s in m['s']:
                ll = _lado_linea(s[1])
                if ll:
                    add(dict(mercado=merc, ambito=ambito, linea=ll[1], lado=ll[0]), s, n)
            continue
        if n == 'Resultado del partido':
            for s in m['s']:
                if s[1] in ('1', 'X', '2'):
                    add(dict(mercado='resultado', lado=s[1]), s, n)
        elif n == 'Doble oportunidad':
            for s in m['s']:
                t = _n(s[1])
                if ' o empate' in t:
                    lado = '1X' if t.startswith(nl) else 'X2'
                else:
                    lado = '12'
                add(dict(mercado='resultado', lado=lado), s, n)
        elif n == 'Ambos equipos anotan':
            for s in m['s']:
                add(dict(mercado='ambos', lado='si' if _n(s[1]).startswith('s') else 'no'), s, n)
        elif n in ('Ambos equipos reciben una tarjeta', 'Ambos equipos reciben 2 o más tarjetas'):
            k = 1 if 'una' in n else 2
            for s in m['s']:
                add(dict(mercado='ambos_n_tarjetas', n=k, lado='si' if _n(s[1]).startswith('s') else 'no'), s, n)
        elif n == 'Resultado Primer Tiempo':
            for s in m['s']:
                t = _n(s[1])
                add(dict(mercado='resultado_1t', lado='1' if t == nl else ('2' if t == nv else 'X')), s, n)
        elif n == 'Equipo con más tarjetas' or n == 'Equipo con más Tiros de esquina':
            stat = 'tarjetas' if 'tarjetas' in n else 'corners'
            for s in m['s']:
                t = _n(s[1])
                add(dict(mercado='mas_que', stat=stat, lado='local' if t == nl else ('visitante' if t == nv else 'empate')), s, n)
    return out


def indice_modelo(A):
    """Líneas del análisis del modelo por clave canónica de `sel`."""
    return {json.dumps(r['sel'], sort_keys=True): r for r in A['lineas']}


def clave(sel):
    return json.dumps(sel, sort_keys=True)
