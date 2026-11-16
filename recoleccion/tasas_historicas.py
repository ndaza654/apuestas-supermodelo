# -*- coding: utf-8 -*-
"""Tasa histórica de acierto de una línea (backtest en ligas de clubes, registro/tasas_historicas.json).
    from tasas_historicas import tasa
    tasa('corners', 'total', 'Más', 8.5, x_local=8, x_visitante=7, colchon=1.4, n=10)
Cohorte = partidos donde el MENOR de los dos conteos fue >= k de 10 y el colchón cayó en el mismo tramo; periodo desde 2019/20 (si n >= N_MIN) o todo.
Si la celda tiene pocos partidos se ensancha: sin tramo de colchón, luego todas las temporadas y, si aun así no alcanza, baja el conteo de a uno (hasta 3 niveles). Sin dato (mercado no medido, línea asiática,
línea fuera de rango) devuelve None. Solo clubes de 5 grandes ligas (+ Brasil en goles): para selecciones es una referencia, no una medida."""
import json, os
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N_MIN = 150
_T = None


def cargar():
    global _T
    if _T is None:
        p = os.path.join(RAIZ, 'registro', 'tasas_historicas.json')
        _T = json.load(open(p, encoding='utf8')) if os.path.exists(p) else {'meta': {}, 't': {}}
    return _T


def _banda(col, cortes):
    i = 0
    while i < len(cortes) and col >= cortes[i]:
        i += 1
    return i


def tasa(mercado, ambito, lado, linea, x_local, x_visitante, colchon, n=10):
    T = cargar()
    if not T['t'] or ambito not in ('total', 'local', 'visitante') or linea is None or abs(linea * 2 - round(linea * 2)) > 1e-9 or abs(linea - round(linea)) < 1e-9:
        return None
    e = T['t'].get(f"{mercado}|{ambito}|{'mas' if lado == 'Más' else 'menos'}|{linea:.1f}")
    if not e:
        return None
    N = T['meta']['N']
    k = max(0, min(N, round(min(x_local, x_visitante) * N / n)))        # con menos de 10 partidos se reescala a «de 10»
    b = _banda(colchon if colchon is not None else 0.0, T['meta']['bandas_colchon'])
    for kk in range(k, max(4, k - 3), -1):                                # si no hay muestra con ese conteo, baja de a uno (cohorte más amplia = tasa más prudente)
        for per, nom in (('rec', 'desde 2019/20'), ('todo', 'todas las temporadas')):
            nn, hh = e[per]
            for amplio in (False, True):
                ncel = sum(nn[kk]) if amplio else nn[kk][b]
                hcel = sum(hh[kk]) if amplio else hh[kk][b]
                if ncel >= N_MIN:
                    return {'p': round(hcel / ncel, 4), 'n': ncel, 'periodo': nom, 'per': per, 'k': kk, 'banda': None if amplio else b,
                            'texto': f"{hcel} de {ncel} partidos de clubes con ≥ {kk} de {N} en ambos{'' if amplio else ' y colchón en el mismo tramo'} ({nom})"
                                     + (f"; sin muestra con ≥ {k}, se usó ≥ {kk}" if kk != k else '')}
    return None
