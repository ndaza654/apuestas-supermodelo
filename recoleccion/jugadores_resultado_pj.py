# -*- coding: utf-8 -*-
"""Convierte las tablas de jugadores de partidos YA JUGADOS (Flashscore, iframe de «Estadísticas de jugadores») en el .txt que lee calificar_jugadores.py.

    python3 recoleccion/jugadores_resultado_pj.py <crudo.json> <incidentes.json> <mapa.json> <salida.txt> [etiqueta]

  crudo.json      {"<mid>": {"k": "<clave>", "f": "AAAA-MM-DD", "P": {"<jugador>": {"logo":..., "Minutos jugados":..., ...}}}}   (lo deja el navegador)
  incidentes.json {"<clave>": {"eventos": [{"equipo": 1|2, "jugador": "...", ...}]}}      (resultados_flashscore.py): sirve para saber qué logo es el local
  mapa.json       {"<clave>": "<partido tal como sale en registro/lineas.csv>"}
El lado de cada jugador se decide por votación: los jugadores que aparecen en los incidentes (goles, tarjetas, cambios) con equipo 1/2 fijan qué escudo es el local.
Solo salen quienes jugaron (minutos > 0). «entradas» = intentadas (denominador de «ganadas/intentadas»). Flashscore no trae faltas recibidas (0 = no medido).
"""
import json, re, sys
from collections import Counter


def n0(s):
    m = re.match(r'^(\d+(?:\.\d+)?)', str(s or ''))
    return int(float(m.group(1))) if m else 0


def intentadas(s):
    m = re.match(r'^(\d+)/(\d+)', str(s or ''))
    return int(m.group(2)) if m else n0(s)


def main(crudo, inc, mapa, salida, etiqueta='19-nov'):
    C, I, M = (json.load(open(x, encoding='utf-8')) for x in (crudo, inc, mapa))
    out = ['# Estadísticas finales por jugador (Flashscore, pestaña «Estadísticas de jugadores», %s; solo quienes jugaron).' % etiqueta,
           '# columnas: lado|jugador|min|remates|al_arco|goles|asistencias|faltas_cometidas|faltas_recibidas|entradas|atajadas|amarillas|rojas  (lado = h local/a visitante)',
           '# Límites: Flashscore no trae faltas recibidas (0 = no medido); «entradas» = entradas intentadas de Flashscore (Betano cuenta entradas totales); «atajadas» de la columna Paradas.']
    avisos = []
    for mid, v in C.items():
        k = v['k']
        if k not in M:
            continue
        P = v['P']
        votos = {}
        eventos = (I.get(k) or {}).get('eventos', [])
        por_nombre = {}
        for e in eventos:
            if e.get('jugador') and e.get('equipo'):
                por_nombre.setdefault(e['jugador'], []).append(e['equipo'])
        for nom, o in P.items():
            if nom in por_nombre and o.get('logo'):
                c = Counter(por_nombre[nom])
                votos.setdefault(o['logo'], Counter())[c.most_common(1)[0][0]] += 1
        logos = {lg: c.most_common(1)[0][0] for lg, c in votos.items()}
        if len(set(logos.values())) < 2 and len({o.get('logo') for o in P.values()}) == 2:
            avisos.append(f'{k}: los incidentes no distinguieron los dos escudos ({logos}); partido omitido')
            continue
        out.append('#' + M[k])
        n = 0
        for nom, o in P.items():
            mn = n0(o.get('Minutos jugados'))
            if not mn or o.get('logo') not in logos:
                continue
            lado = 'h' if logos[o['logo']] == 1 else 'a'
            out.append('|'.join(str(x) for x in (lado, nom, mn, n0(o.get('Remates totales')), n0(o.get('Remates a puerta')), n0(o.get('Goles')), n0(o.get('Asistencias')),
                                                 n0(o.get('Faltas cometidas')), 0, intentadas(o.get('Entradas ganadas')), n0(o.get('Paradas del arquero') or o.get('Paradas')),
                                                 n0(o.get('Tarjetas amarillas')), n0(o.get('Tarjetas rojas')))))
            n += 1
        avisos.append(f'{k}: {n} jugadores con minutos')
    open(salida, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return avisos


if __name__ == '__main__':
    for a in main(*sys.argv[1:6]):
        print(a)
