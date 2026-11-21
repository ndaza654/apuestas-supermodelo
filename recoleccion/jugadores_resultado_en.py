# -*- coding: utf-8 -*-
"""Tablas «Player stats» de Flashscore (inglés, partidos ya jugados; salida de flashscore_jugadores_en_par.js) → .txt que lee calificar_jugadores.py.

    python3 recoleccion/jugadores_resultado_en.py <lote.json> <incidentes.json> <mapa_partidos.json> <mids.json> <salida.txt> [etiqueta]

  lote.json   {"pj": {"<mid>": {"h","a","rows": {pid: {"n","pos","eq":"H|A","v":{...}, "raw":{...}}}}}}   (lo descarga pjDescargar)
  mids.json   {"<clave>": "<mid>"}      ·  mapa_partidos.json  {"<clave>": "<partido como en lineas.csv>"}
Las celdas de Flashscore salen corridas una columna desde el 20-nov (encabezados duplicados + «ALL»): se usa la misma realineación verificada de
jugadores_en_realinear.py (minutos = celda «Rating», goles = «Minutes played», asistencias = «Own goals», amarillas = «Assists», tiros al arco = «xG on target»,
remates = «xG on target» + «Shots on target» + «Shots off target», faltas cometidas = «Tackles won», entradas = «Ground duels won»). No verificado y NO usado: atajadas y rojas
(las rojas y las tarjetas salen de los incidentes con «@»). Solo salen quienes jugaron (minutos > 0): quien no figura = «nula».
Límites: Flashscore EN trae «Fouls suffered» corrido (se usa 0 = no medido); entradas = intentadas de Flashscore (Betano cuenta entradas totales)."""
import json, re, sys


def num(s):
    m = re.match(r'^(-?\d+(?:\.\d+)?)', str(s or '').strip())
    return int(float(m.group(1))) if m else 0


def val(v, k):
    return v.get(k + k, v.get(k))


def intentadas(s):
    m = re.match(r'^(\d+)/(\d+)', str(s or ''))
    return int(m.group(2)) if m else num(s)


def main(lote, inc, mapa, mids, salida, etiqueta='20-nov'):
    D = json.load(open(lote, encoding='utf8'))['pj']
    I = json.load(open(inc, encoding='utf8')); M = json.load(open(mapa, encoding='utf8')); K = json.load(open(mids, encoding='utf8'))
    out = [f'# Estadísticas finales por jugador (Flashscore EN, pestaña Player stats, {etiqueta}; solo quienes jugaron).',
           '# columnas: lado|jugador|min|remates|al_arco|goles|asistencias|faltas_cometidas|faltas_recibidas|entradas|atajadas|amarillas|rojas  (lado = h local/a visitante)',
           '# Límites: «entradas» = Tackles won intentadas de Flashscore (Betano cuenta entradas totales); faltas recibidas y atajadas no leídas (0); tarjetas de la tabla (amarillas) y de los incidentes (@).']
    cobertura = []
    for clave, mid in K.items():
        if mid not in D or clave not in M:
            continue
        P = D[mid]
        # goles de la PRÓRROGA (Betano liquida a los 90'): se restan al jugador; los remates de la prórroga no se pueden separar (se declara)
        pror = {}
        for e in (I.get(clave) or {}).get('eventos', []):
            if e.get('tipo') == 'Goal' and e.get('periodo') == 'Extra Time' and e.get('jugador'):
                pror[e['jugador']] = pror.get(e['jugador'], 0) + 1
        out.append('#' + M[clave])
        if pror:
            out.append('# (prórroga: minutos y remates incluyen el tiempo extra; los goles de prórroga ya se descontaron)')
        n = 0
        for pid, o in P['rows'].items():
            v = o['v']
            mn = num(val(v, 'Rating'))
            if mn <= 0:
                continue
            lado = 'h' if o['eq'] == 'H' else 'a' if o['eq'] == 'A' else None
            if not lado:
                continue
            tiros = num(val(v, 'xG on target (xGOT)')) + num(val(v, 'Shots on target')) + num(val(v, 'Shots off target'))
            out.append('|'.join(str(x) for x in (lado, o['n'], mn, tiros, num(val(v, 'xG on target (xGOT)')), max(0, num(val(v, 'Minutes played')) - pror.get(o['n'], 0)), num(val(v, 'Own goals')),
                                                 num(val(v, 'Tackles won')), 0, intentadas(val(v, 'Ground duels won')), 0, num(val(v, 'Assists')), 0)))
            n += 1
        for e in (I.get(clave) or {}).get('eventos', []):
            if e.get('tipo') in ('Yellow Card', 'Red Card') and e.get('jugador'):
                out.append(f"@{M[clave]}|{e['jugador']}|{'amarilla' if e['tipo'] == 'Yellow Card' else 'roja'}")
        cobertura.append((M[clave], n))
    open(salida, 'w', encoding='utf8').write('\n'.join(out) + '\n')
    for p, n in cobertura:
        print(f'{n:3d} jugadores · {p}')


if __name__ == '__main__':
    main(*sys.argv[1:7])
