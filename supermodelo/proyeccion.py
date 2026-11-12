# -*- coding: utf-8 -*-
"""Medias esperadas del modelo (para el informe) y lectura del historial reciente (forma) de equipos y jugadores.

· medias(): para cada mercado y ámbito, la media de los partidos simulados CON el contexto de la ficha, la misma sin la
  ficha, la media que pone Betano (la que reproduce su escalera sin margen) y el rango del 80 % de los partidos simulados.
· jugadores_esperado(): lo que se espera de cada jugador con línea en Betano (solo en las estadísticas donde hay línea).
· forma de los equipos (opcional, mismo formato que perfiles.py: 'v' H/A y 'stats' {stat: [a_favor, en_contra]}):
  medias a favor / en contra en la condición de hoy y cuántas veces salió Más en cada línea.
· historial de jugadores (opcional): por 90′ y cuántas veces cumplió cada línea en sus partidos de 60′ o más.
Nada de esto cambia las probabilidades: es lo que el informe muestra para decidir mejor.
"""
import re
import unicodedata
import numpy as np
from . import mercados as MS

ORDEN = ['goles', 'corners', 'tarjetas', 'remates', 'al_arco', 'faltas', 'fueras', 'saques_meta', 'saques_banda', 'atajadas']
AMBITOS = ['total', 'local', 'visitante', '1T', '2T']
STAT_DE = {'goles': 'g', 'corners': 'c', 'tarjetas': 'y', 'faltas': 'f', 'remates': 'sh', 'al_arco': 'sot',
           'fueras': 'off', 'saques_meta': 'gk', 'saques_banda': 'ti'}


# ------------------------------------------------------------------ medias del modelo
def _serie(sim, mercado, ambito):
    if mercado == 'atajadas':
        return None if ambito not in ('local', 'visitante') else sim[0 if ambito == 'local' else 1].get('sv')
    try:
        return MS.valor(sim, mercado, ambito)
    except KeyError:
        return None


def medias(S, bet, media_fn):
    """Lista de dicts {mercado, ambito, modelo, sin_contexto, betano, sd, p10, p90}.
    media_fn(bet, mercado, ambito) → media que pone Betano (o None si no hay escalera)."""
    out = []
    for m in ORDEN:
        for a in AMBITOS:
            x = _serie(S['sim'], m, a)
            if x is None:
                continue
            xb = _serie(S['base'], m, a)
            bt = None if m == 'atajadas' else media_fn(bet, m, a)
            out.append(dict(mercado=m, ambito=a, modelo=round(float(x.mean()), 2),
                            sin_contexto=round(float(xb.mean()), 2) if xb is not None else None,
                            betano=None if bt is None else round(float(bt), 2),
                            sd=round(float(x.std()), 2), p10=float(np.percentile(x, 10)), p90=float(np.percentile(x, 90))))
    return out


def jugadores_esperado(S, specs, bet):
    """Por jugador: titularidad, minutos esperados y la media esperada en cada estadística QUE TIENE LÍNEA en Betano."""
    con_linea = {}
    for jb in bet.get('jugadores', []):
        con_linea.setdefault(jb['jugador'], set()).add(jb['stat'])
    out = {}
    for sp in specs:
        j = (S.get('jug') or {}).get(sp['nombre'])
        if not j:
            continue
        d = dict(lado=sp['lado'], titular=sp.get('titular'), minutos=sp.get('minutos'),
                 con_linea=sorted(con_linea.get(sp['nombre'], [])), portero=bool(sp.get('portero')))
        for k, v in j.items():
            d[k] = round(float(np.mean(v)), 2)
        if 'anota' in j:
            d['p_anota'] = round(float((j['anota'] >= 1).mean()), 3)
        if 'anota_o_asiste' in j:
            d['p_anota_o_asiste'] = round(float((j['anota_o_asiste'] >= 1).mean()), 3)
        if 'tarjeta' in j:
            d['p_tarjeta'] = round(float((j['tarjeta'] >= 1).mean()), 3)
        out[sp['nombre']] = d
    return out


# ------------------------------------------------------------------ forma de los equipos
def _par(x):
    """[a_favor, en_contra] numéricos o None (el historial puede traer huecos)."""
    try:
        return (float(x[0]), float(x[1])) if x[0] is not None and x[1] is not None else None
    except (TypeError, ValueError, IndexError, KeyError):
        return None


def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _cond(forma, lado):
    v = 'H' if lado == 'local' else 'A'
    return [p for p in ((forma or {}).get(lado) or []) if p.get('v') == v]


def forma_media(forma, stat):
    """{'local': (a_favor, en_contra, n) jugando en casa, 'visitante': (..) jugando fuera} o None."""
    out = {}
    for lado in ('local', 'visitante'):
        xs = [q for q in (_par((p.get('stats') or {}).get(stat)) for p in _cond(forma, lado)) if q]
        if xs:
            out[lado] = (float(np.mean([x[0] for x in xs])), float(np.mean([x[1] for x in xs])), len(xs))
    return out or None


def forma_hits(forma, mercado, ambito, linea, loc='Local', vis='Visitante'):
    """Texto «veces que salió Más» (o None si no hay historial para esta línea)."""
    s = STAT_DE.get(mercado)
    if not forma or not s or ambito in ('1T', '2T'):
        return None

    def cnt(ps, f):
        v = [f(q) for q in (_par((p.get('stats') or {}).get(s)) for p in ps) if q]
        return (sum(x > linea for x in v), len(v)) if v else None
    L, V = _cond(forma, 'local'), _cond(forma, 'visitante')
    if ambito == 'total':
        a, b = cnt(L, lambda x: x[0] + x[1]), cnt(V, lambda x: x[0] + x[1])
        et = (f'{loc} local', f'{vis} visitante')
    elif ambito == 'local':
        a, b = cnt(L, lambda x: x[0]), cnt(V, lambda x: x[1])
        et = (f'{loc} local', f'Rivales de {vis} fuera')
    else:
        a, b = cnt(V, lambda x: x[0]), cnt(L, lambda x: x[1])
        et = (f'{vis} visitante', f'Rivales de {loc} en casa')
    partes = [f'{t}: {r[0]}/{r[1]}' for t, r in zip(et, (a, b)) if r]
    return ' · '.join(partes) if partes else None


# ------------------------------------------------------------------ historial de jugadores
def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9 ]+', ' ', s).split()


def buscar_jugador(hist, nombre):
    """Encuentra al jugador en el historial aunque el nombre venga distinto («Hidalgo S.» / «Savanier Hidalgo»).
    Coincide si todas las palabras de un nombre (ignorando iniciales sueltas) están en el otro."""
    if not hist:
        return None
    a = [w for w in norm(nombre) if len(w) > 1]
    for k, v in hist.items():
        b = [w for w in norm(k) if len(w) > 1]
        if a and b and (set(a) <= set(b) or set(b) <= set(a)):
            return k, v
    return None


STAT_JUG = {'remates': 'remates', 'al_arco': 'al_arco', 'faltas': 'faltas', 'entradas': 'entradas', 'anota': 'goles',
            'atajadas': 'atajadas', 'tarjeta': 'tarjeta', 'anota_o_asiste': None, 'asiste': None}


def jug_por90(h, stat):
    c = STAT_JUG.get(stat)
    ps = h.get('partidos') or []
    if not c:
        return None
    ok = [p for p in ps if _num(p.get(c)) and _num(p.get('min'))]
    mins = sum(p['min'] for p in ok)
    return sum(p[c] for p in ok) / mins * 90 if mins > 0 else None


def jug_hits(h, stat, k=1):
    """(veces, partidos de 60′ o más) que llegó a k o más; None si el historial no trae la estadística."""
    ps = [p for p in (h.get('partidos') or []) if _num(p.get('min')) and p['min'] >= 60]
    if stat == 'anota_o_asiste':
        v = [(p.get('goles') or 0) + (p.get('asist') or 0) for p in ps if _num(p.get('goles'))]
    else:
        c = STAT_JUG.get(stat)
        v = [p[c] for p in ps if c and _num(p.get(c))]
    return (sum(x >= k for x in v), len(v)) if v else None
