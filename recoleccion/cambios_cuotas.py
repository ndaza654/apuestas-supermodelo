#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compara dos lecturas de Betano de la misma jornada y deja qué cuotas se movieron.

Uso: python3 recoleccion/cambios_cuotas.py jornadas/AAAA-MM-DD
Antes de volver a leer Betano se copia betano/<clave>.json a betano_previo/<clave>.json (y el texto crudo a raw/previo_HHMM/).
Salida: jornadas/AAAA-MM-DD/cambios_cuotas.json = {clave: {antes, ahora, cambios: [[texto, mercado, antes, ahora, pct, jugador?], …], nuevas, quitadas}}
Solo cuotas entre 1,10 y 8 (las extremas se mueven sin significar nada). pct > 0 = la cuota subió (paga más)."""
import os, sys, json, glob

MK = {'corners': 'Córners', 'goles': 'Goles', 'tarjetas': 'Tarjetas', 'remates': 'Remates', 'al_arco': 'Tiros al arco', 'faltas': 'Faltas', 'fueras': 'Fueras de juego',
      'saques_banda': 'Saques de banda', 'saques_meta': 'Saques de meta'}
ST = {'remates': 'remates', 'al_arco': 'tiros al arco', 'entradas': 'entradas', 'faltas': 'faltas', 'atajadas': 'atajadas', 'asiste': 'asistencias',
      'anota': 'anota', 'anota_o_asiste': 'anota o asiste', 'tarjeta': 'tarjeta'}


def plano(b, loc, vis):
    """{clave: (texto, mercado, cuota, jugador)} de todas las selecciones comparables."""
    d = {}
    amb = {'total': '', 'local': ' ' + loc, 'visitante': ' ' + vis, '1T': ' 1.er tiempo', '2T': ' 2.º tiempo'}
    for l in b.get('lineas', []):
        for lado, k in (('Más', 'mas'), ('Menos', 'menos')):
            c = l.get(k)
            if c:
                ln = str(l['linea']).replace('.', ',')
                d[('L', l['mercado'], l['ambito'], l['linea'], lado)] = (f"{MK.get(l['mercado'], l['mercado'])}{amb.get(l['ambito'], ' ' + l['ambito'])} {lado} {ln}", l['mercado'], c, None)
    for j in b.get('jugadores', []):
        st = ST.get(j['stat'], j['stat'])
        if 'escalera' in j:
            for n, c in j['escalera'].items():
                d[('J', j['jugador'], j['stat'], n)] = (f"{j['jugador']} · {n}+ {st}", 'jugador:' + j['stat'], c, j['jugador'])
        elif j.get('cuota'):
            d[('J', j['jugador'], j['stat'], '')] = (f"{j['jugador']} · {st}", 'jugador:' + j['stat'], j['cuota'], j['jugador'])
    for u in b.get('unicos', []):
        if u.get('mercado') in ('resultado', 'ambos_marcan'):
            for o, c in (u.get('opciones') or {}).items():
                if isinstance(c, (int, float)):
                    nombre = {'1': loc, 'X': 'Empate', '2': vis, '1X': f'{loc} o empate', 'X2': f'{vis} o empate', '12': f'{loc} o {vis}'}.get(o, o)
                    d[('U', u['mercado'], o)] = ((('Resultado: ' if u['mercado'] == 'resultado' else 'Ambos marcan: ') + nombre), u['mercado'], c, None)
    return d


def main(argv):
    base = argv[0]
    out = {}
    for pv in sorted(glob.glob(os.path.join(base, 'betano_previo', '*.json'))):
        clave = os.path.basename(pv)[:-5]
        pn = os.path.join(base, 'betano', clave + '.json')
        if not os.path.exists(pn):
            continue
        A, B = json.load(open(pv, encoding='utf8')), json.load(open(pn, encoding='utf8'))
        if A['meta'].get('cuotas_leidas') == B['meta'].get('cuotas_leidas'):
            continue
        loc, vis = B['meta']['local'], B['meta']['visitante']
        a, b = plano(A['betano'], loc, vis), plano(B['betano'], loc, vis)
        cambios = []
        for k, (txt, mk, c1, jug) in b.items():
            if k in a:
                c0 = a[k][2]
                if c0 != c1 and 1.10 <= min(c0, c1) and max(c0, c1) <= 8:
                    cambios.append([txt, mk, c0, c1, round((c1 / c0 - 1) * 100, 1), jug])
        cambios.sort(key=lambda r: -abs(r[4]))
        rango = lambda d, ks: sorted(d[k][0] for k in ks if 1.10 <= d[k][2] <= 8 and k[0] == 'L')
        out[clave] = {'antes': A['meta'].get('cuotas_leidas'), 'ahora': B['meta'].get('cuotas_leidas'), 'cambios': cambios,
                      'nuevas': rango(b, set(b) - set(a)), 'quitadas': rango(a, set(a) - set(b))}
        print(f"{clave:30s} {len(cambios)} cuotas movidas · suben {sum(1 for c in cambios if c[4] > 0)} · bajan {sum(1 for c in cambios if c[4] < 0)}")
    json.dump(out, open(os.path.join(base, 'cambios_cuotas.json'), 'w', encoding='utf8'), ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
