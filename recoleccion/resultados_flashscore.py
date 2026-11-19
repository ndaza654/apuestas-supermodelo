# -*- coding: utf-8 -*-
"""Resultados reales desde el crudo de Flashscore (feeds df_st_1 = estadísticas, df_su_1 = incidentes) → formato de calificar_lineas.py.

    python3 recoleccion/resultados_flashscore.py <crudo.json> <salida_resultados.json> <salida_incidentes.json>

El crudo lo deja el navegador: {"<clave>": {"mid":..., "df_st_1_": "200|SE÷Match¬...", "df_su_1_": "200|AC÷1st Half¬..."}}.
Salida 1 (resultados): {"<clave>": {"g":[h,a], "g1":[h,a], "c","c1","y","y1","sh","sh1","sot","sot1","f","f1","off","off1","ti","ti1","gk","gk1","sv","sv1","fuente"}}
  · y/y1 = tarjetas en PUNTOS de Betano (amarilla 1 + roja 2).  · g = goles del tiempo reglamentario (sin prórroga/penales de definición); el autogol cuenta para el equipo beneficiado.
Salida 2 (incidentes): por partido, goles (equipo, jugador, minuto, tipo, asistente), tarjetas y sustituciones, con el periodo.
Lo que Flashscore no trae queda fuera: no se inventa.
"""
import json, re, sys

NOMBRES = {'c': ['Corner kicks'], 'sh': ['Total shots'], 'sot': ['Shots on target'], 'f': ['Fouls'], 'off': ['Offsides'],
           'ti': ['Throw-ins', 'Throw ins'], 'gk': ['Goal kicks'], 'sv': ['Goalkeeper saves']}


def rec(s):
    return {x[:x.index('÷')]: x[x.index('÷') + 1:] for x in s.split('¬') if '÷' in x}


def num(s):
    m = re.search(r'-?\d+(\.\d+)?', str(s) if s is not None else '')
    return float(m.group(0)) if m else None


def stats(texto):
    """{periodo: {nombre: [h, a]}}"""
    per, p = {}, None
    t = texto.split('|', 1)[1] if '|' in texto[:6] else texto
    for r in (rec(x) for x in t.split('~')):
        if 'SE' in r:
            p = r['SE']; per[p] = {}
        elif 'SG' in r and p:
            per[p].setdefault(r['SG'], [r.get('SH'), r.get('SI')])
    return per


def tomar(periodo):
    o = {}
    for k, nombres in NOMBRES.items():
        for n in nombres:
            if n in periodo:
                h, a = num(periodo[n][0]), num(periodo[n][1])
                if h is not None and a is not None:
                    o[k] = [int(h), int(a)]
                break
    am, ro = periodo.get('Yellow cards'), periodo.get('Red cards')
    if am:
        h, a = num(am[0]) or 0, num(am[1]) or 0
        rh, ra = (num(ro[0]) or 0, num(ro[1]) or 0) if ro else (0, 0)
        o['y'] = [int(h + 2 * rh), int(a + 2 * ra)]
    return o


def incidentes(texto):
    """Lee df_su_1 en orden. Un bloque `~III` puede traer varios eventos (gol + asistencia, cambio salida + entrada): los campos de cada
    evento (IE, IF jugador, IU, ICT, IL motivo) vienen ANTES de su IK (tipo) y IM (id del jugador); IA (equipo) e IB (minuto) son del bloque."""
    t = texto.split('|', 1)[1] if '|' in texto[:6] else texto
    ev, per = [], None
    for bloque in t.split('~'):
        base, pend = {}, {}
        for campo in bloque.split('¬'):
            if '÷' not in campo:
                continue
            k, v = campo.split('÷', 1)
            if k == 'AC':
                per = v
            elif k == 'III':
                base, pend = {}, {}
            elif k == 'IA':
                base['equipo'] = int(v)
            elif k == 'IB':
                base['min'] = v
            elif k == 'IF':
                pend['jugador'] = v
            elif k == 'IL':
                pend['motivo'] = v
            elif k == 'IK':
                e = {'periodo': per, 'tipo': v, **base, **pend}
                ev.append(e); pend = {}
            elif k == 'IM' and ev and 'id' not in ev[-1] and ev[-1]['tipo'] == pend.get('_t', ev[-1]['tipo']):
                ev[-1]['id'] = v
    return ev


def main(crudo, sal_res, sal_inc):
    d = json.load(open(crudo, encoding='utf-8'))
    res, inc = {}, {}
    for clave, v in d.items():
        per = stats(v['df_st_1_'])
        m, p1 = tomar(per.get('Match', {})), tomar(per.get('1st Half', {}))
        p2 = tomar(per.get('2nd Half', {}))
        if p1 and p2 and any(x.startswith('Extra') for x in per):      # el «Match» incluye la prórroga: se arma con 1T + 2T (90 minutos)
            m = {k: [p1[k][0] + p2[k][0], p1[k][1] + p2[k][1]] for k in p1 if k in p2}
        ev = incidentes(v['df_su_1_'])
        # goles del tiempo reglamentario: tipos Goal / Penalty (no tanda) / Own Goal (cuenta para el rival)
        g = [0, 0]; g1 = [0, 0]
        for e in ev:
            if e['periodo'] and e['periodo'].lower().startswith(('penalties', 'extra', 'pen')) or e['periodo'] and 'Extra' in e['periodo']:
                continue
            if e['tipo'] in ('Goal', 'Penalty', 'Own goal', 'Own Goal'):
                lado = e['equipo'] - 1                       # Flashscore anota el autogol en el lado que se beneficia
                g[lado] += 1
                if e['periodo'] and e['periodo'].startswith('1st'):
                    g1[lado] += 1
        o = {'g': g, 'g1': g1, **{k: m[k] for k in m}, 'fuente': 'Flashscore (feeds df_st/df_su, leído el 19-nov ~10:00 Bogotá con el navegador integrado)'}
        for k, val in p1.items():
            o[k + '1'] = val
        res[clave] = o
        inc[clave] = {'mid': v.get('mid'), 'eventos': ev}
    json.dump(res, open(sal_res, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(inc, open(sal_inc, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return res, inc


if __name__ == '__main__':
    main(*sys.argv[1:4])
