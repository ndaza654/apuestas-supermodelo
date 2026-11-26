# -*- coding: utf-8 -*-
"""«X de 10 conjunto» de un Bet Builder: en cuántos de los últimos 10 partidos de cada equipo se dieron TODAS las patas a la vez.

Mide qué tan «fácil» fue la combinación completa en la forma reciente (la lección de Nacional–Medellín del 25-nov: el partido
con líneas fáciles rindió mejor que el que se eligió después). No es una probabilidad: cada equipo jugó contra rivales distintos.
Una pata de equipo se lee como «a favor» en la serie de ese equipo y «en contra» (lo que hizo el rival) en la serie del otro.

Uso: python3 recoleccion/bb_conjunto.py jornadas/AAAA-MM-DD <clave> corners:visitante:3.5:mas faltas:local:12.5:menos ...
mercados: corners, faltas, al_arco, remates, goles, tarjetas (solo amarillas), fueras; ámbito: local, visitante, total; lado: mas, menos.
"""
import json, os, sys

KEY = {'corners': 'c', 'faltas': 'f', 'al_arco': 'sot', 'remates': 'sh', 'goles': 'g', 'tarjetas': 'y', 'fueras': 'off', 'saques_meta': 'gk'}


def conjunto(entrada, patas, n=10):
    """patas = [(mercado, ámbito, línea, 'mas'|'menos'), ...] → {'local': (aciertos, n), 'visitante': (aciertos, n)}."""
    F = entrada['ficha']['forma']
    out = {}
    for team in ('local', 'visitante'):
        hit = tot = 0
        for m in (F.get(team) or [])[:n]:
            st = m.get('stats') or {}
            ok = valid = True
            for mer, amb, lin, lado in patas:
                p = st.get(KEY.get(mer, ''))
                if not p or p[0] is None or p[1] is None:
                    valid = False
                    break
                v = p[0] + p[1] if amb == 'total' else (p[0] if amb == team else p[1])
                ok &= (v > float(lin)) if lado == 'mas' else (v < float(lin))
            if valid:
                tot += 1
                hit += bool(ok)
        out[team] = (hit, tot)
    return out


if __name__ == '__main__':
    jornada, clave, *specs = sys.argv[1:]
    e = json.load(open(os.path.join(jornada, 'entradas', clave + '.json'), encoding='utf8'))
    patas = [tuple(s.split(':')) for s in specs]
    r = conjunto(e, patas)
    print(f"{e['local']}: {r['local'][0]} de {r['local'][1]} · {e['visitante']}: {r['visitante'][0]} de {r['visitante'][1]}")
