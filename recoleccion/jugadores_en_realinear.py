#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Realinea el crudo de flashscore_jugadores_en_par.js leído el 20/21-nov-2026 (encabezados duplicados + «ALL» de más → celdas corridas una columna) a los
nombres que espera jugadores_en_decod.py. Alineación verificada contra los totales de equipo de las fichas (250 partidos × 2 equipos):
  minutos = celda «Rating» (≈ suma 990) · goles = «Minutes played» (329) · xG = «Goals» (347) · asistencias = «Own goals» (≤ goles en 490 de 500) ·
  amarillas = «Assists» (363) · tiros al arco = «xG on target» (486) · remates totales = «xG on target»+«Shots on target»+«Shots off target» (455) ·
  faltas cometidas = «Tackles won» (459) · entradas ganadas/intentadas = «Ground duels won» (formato g/e) · faltas recibidas = «Touches» (278 = faltas del rival).
22-nov: si el crudo trae `raw` (celdas tal cual de cada pestaña: general / shots / attack / defense / goalkeeping) se leen de ahí, sin depender del corrimiento:
  rating = general[1] · rojas = general[7] · atajadas = goalkeeping[1] (contra remates al arco del rival − goles: igual en 51 %, ±1 en 70 % de 270 equipos-partido: se usa, con ese límite).
  Solo se aceptan partidos con las columnas completas (general:8 shots:11 attack:7 defense:10 goalkeeping:8): si las pestañas no cambiaron al leer (8/8/8/8/8), el partido se descarta y se vuelve a leer.
NO verificado y NO se usa: nada más. Uso: python3 recoleccion/jugadores_en_realinear.py <crudo.json> <salida_entrada.json>"""
import sys, json, re


def num(s):
    m = re.match(r'^(-?\d+(?:\.\d+)?)', str(s or '').strip())
    return float(m.group(1)) if m else 0


def val(v, k):
    return v.get(k + k, v.get(k))


def main(crudo, salida):
    D = json.load(open(crudo, encoding='utf8'))
    pj2 = {}
    COLS = ['general:8', 'shots:11', 'attack:7', 'defense:10', 'goalkeeping:8']
    malos = [m for m, P in D['pj'].items() if P.get('cols') != COLS]
    if malos:
        print('DESCARTADOS por columnas incompletas (releer):', len(malos), malos[:10])
    for mid, P in D['pj'].items():
        if mid in malos:
            continue
        rows = {}
        for pid, o in P['rows'].items():
            v = o['v']
            tiros = sum(num(val(v, k)) for k in ('xG on target (xGOT)', 'Shots on target', 'Shots off target'))
            rows[pid] = {'n': o['n'], 'pos': o['pos'], 'eq': o['eq'], 'v': {
                'Minutes played': val(v, 'Rating'), 'Goals': val(v, 'Minutes played'), 'Expected goals (xG)': val(v, 'Goals'),
                'Assists': val(v, 'Own goals'), 'Yellow cards': val(v, 'Assists'), 'Total shots': str(int(tiros)),
                'Shots on target': val(v, 'xG on target (xGOT)'), 'Fouls committed': val(v, 'Tackles won'),
                'Tackles won': val(v, 'Ground duels won'), 'Fouls suffered': val(v, 'Touches')}}
            rw = o.get('raw') or {}
            if len(rw.get('general', [])) >= 8:
                rows[pid]['v']['Rating'] = rw['general'][1]; rows[pid]['v']['Red cards'] = rw['general'][7]
            if len(rw.get('goalkeeping', [])) >= 2:
                rows[pid]['v']['Goalkeeper saves'] = rw['goalkeeping'][1]
        pj2[mid] = {'url': P.get('url'), 'h': P.get('h'), 'a': P.get('a'), 'rows': rows, 'cols': P.get('cols')}
    json.dump({'spec': D['spec'], 'pj': pj2}, open(salida, 'w', encoding='utf8'), ensure_ascii=False)
    mins = [sum(num(r['v']['Minutes played']) for r in P['rows'].values() if r['eq'] == e) for P in pj2.values() for e in 'HA']
    print('partidos', len(pj2), '· minutos por equipo (mediana)', sorted(mins)[len(mins) // 2])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
