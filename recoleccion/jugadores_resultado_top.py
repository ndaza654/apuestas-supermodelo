#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tablas «Player stats» de partidos YA JUGADOS leídas con flashscore_jugadores_toplevel.js (`pjTop`, claves pjE_<mid>)
→ .txt que lee calificar_jugadores.py (un bloque «#Partido» por partido; lado h/a desde eq H/A de Flashscore).
Uso: python3 recoleccion/jugadores_resultado_top.py <descarga.json {pj:{mid:...}}> <mapa mid→partido.json> <salida.txt> [etiqueta]
Columnas: lado|jugador|min|remates|al_arco|goles|asistencias|faltas_cometidas|faltas_recibidas|entradas|atajadas|amarillas|rojas.
«entradas» = intentadas de «Tackles won» (Betano cuenta entradas totales: no son idénticas). Solo quienes jugaron (min > 0)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jugadores_en_decod import valores, num, par


def main(ent, mapa, sal, etq='balance'):
    D = json.load(open(ent, encoding='utf8'))['pj']; M = json.load(open(mapa, encoding='utf8'))
    L = [f'# Estadísticas finales por jugador (Flashscore EN, Player stats leído en la pestaña, {etq}; solo quienes jugaron).',
         '# columnas: lado|jugador|min|remates|al_arco|goles|asistencias|faltas_cometidas|faltas_recibidas|entradas|atajadas|amarillas|rojas  (lado = h local/a visitante)',
         '# Límites: «entradas» = intentadas de Tackles won; atajadas = Goalkeeper saves del arquero.']
    for mid, P in D.items():
        if mid not in M:
            print('sin partido para', mid); continue
        L.append('#' + M[mid]); n = 0
        for pid, o in P['rows'].items():
            x = valores(o, P.get('th') or {})
            mn = int(num(x.get('Minutes played')))
            if not mn:
                continue
            g, e = par(x.get('Tackles won'))
            f = [int(num(x.get(k))) for k in ('Total shots', 'Shots on target', 'Goals', 'Assists', 'Fouls committed', 'Fouls suffered')] + [e, int(num(x.get('Goalkeeper saves'))), int(num(x.get('Yellow cards'))), int(num(x.get('Red cards')))]
            L.append('|'.join(['h' if o['eq'] == 'H' else 'a', o['n'], str(mn)] + [str(v) for v in f])); n += 1
        print(M[mid], n, 'jugadores')
    open(sal, 'w', encoding='utf8').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:])
