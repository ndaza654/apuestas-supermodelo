#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resumen por partido de los mercados pedidos (resultado, hándicap, goles, córners y goleador) con la probabilidad del modelo y de la simulación.
Uso: python3 recoleccion/resumen_mercados_foco.py jornadas/AAAA-MM-DD clave1,clave2,...  → jornadas/AAAA-MM-DD/resumen_foco.md
p mezcla del goleador = (partidos con gol + 10·p_cuota/1,08)/20: heurística propia SIN validar."""
import sys, os, json


def pct(x):
    return f'{round(x * 100)} %' if x is not None else '–'


def main(dia, claves):
    out = ['# Resumen de mercados foco (resultado, hándicap, goles, córners, goleador)', '',
           'p = probabilidad del modelo (simulación mezclada con el precio); EV = p·cuota − 1. Heurísticas sin validar; goleador: «p mezcla» = (partidos con gol de 10 + 10·p_cuota/1,08)/20.', '']
    for c in claves:
        rp = f'{dia}/informes/{c}_resultado.json'
        if not os.path.exists(rp):
            out.append(f'## {c}\n- sin informe del modelo\n'); continue
        d = json.load(open(rp, encoding='utf8'))
        pr = d['p_resultado']
        loc, vis = d['partido'].split(' - ', 1) if ' - ' in d['partido'] else ('Local', 'Visitante')
        out.append(f"## {d['partido']} ({d['fecha'][11:]} Bogotá)")
        out.append(f"- **Resultado (modelo):** {loc} {pct(pr['local'])} · empate {pct(pr['empate'])} · {vis} {pct(pr['visitante'])} · tipo: {d['tipo']}.")
        m = {(x['mercado'], x['ambito']): x for x in d.get('medias', [])}
        g = m.get(('goles', 'total'))
        if g:
            out.append(f"- **Goles esperados:** total {g['modelo']:.2f} (Betano {g['betano']:.2f}); intervalo 10–90 %: {g['p10']:.0f}–{g['p90']:.0f}.")
        L = d['lineas']
        res = [x for x in L if x['familia'] == 'resultado']
        hand = [x for x in res if 'ándicap' in x['seleccion'] and 'empate' not in x['seleccion']]
        hand.sort(key=lambda x: -x['p'])
        if hand:
            out.append('- **Hándicap (las 3 más probables):** ' + '; '.join(f"{x['seleccion'].replace('Hándicap ', '')} @{x['cuota']:.2f} p {pct(x['p'])} EV {x['ev'] * 100:+.0f} %" for x in hand[:3]) + '.')
            ev = sorted(hand, key=lambda x: -x['ev'])[0]
            out.append(f"  - Mayor EV: {ev['seleccion'].replace('Hándicap ', '')} @{ev['cuota']:.2f} p {pct(ev['p'])} EV {ev['ev'] * 100:+.0f} %.")
        gl = [x for x in L if x['familia'] == 'goles' and x['sel'].get('ambito') == 'total']
        gl.sort(key=lambda x: abs((x['p'] or 0) - 0.5))
        if gl:
            x = gl[0]
            out.append(f"- **Goles, línea más pareja:** {x['seleccion']} @{x['cuota']:.2f} p {pct(x['p'])} EV {x['ev'] * 100:+.0f} %. Línea 2.5: " + '; '.join(f"{y['seleccion']} @{y['cuota']:.2f} p {pct(y['p'])}" for y in L if y['familia'] == 'goles' and y['sel'].get('ambito') == 'total' and y['sel'].get('linea') == 2.5) + '.')
        co = [x for x in L if x['familia'] == 'corners' and x['sel'].get('ambito') == 'total']
        co.sort(key=lambda x: abs((x['p'] or 0) - 0.5))
        if co:
            x = co[0]
            cm = m.get(('corners', 'total'))
            out.append(f"- **Córners, línea más pareja:** {x['seleccion']} @{x['cuota']:.2f} p {pct(x['p'])} EV {x['ev'] * 100:+.0f} %" + (f" (esperado {cm['modelo']:.1f})." if cm else '.'))
        gp = f'{dia}/goleadores/{c}.json'
        if os.path.exists(gp):
            G = json.load(open(gp, encoding='utf8'))
            fila = []
            for lado in ('local', 'visitante'):
                for x in G['equipos'][lado]['lineas_betano']:
                    q = x['cuotas'].get('anota')
                    if q and x.get('n_partidos'):
                        pm = (x['partidos_con_gol'] + 10 * (1 / q) / 1.08) / 20
                        fila.append((pm, x['jugador'], q, x['partidos_con_gol'], x['n_partidos'], lado))
            fila.sort(reverse=True)
            if fila:
                out.append('- **Goleador (anota; mayor p mezcla):** ' + '; '.join(f'{n} @{q:.2f} · gol en {a} de {b} partidos · p mezcla {pct(p)}' for p, n, q, a, b, _ in fila[:3]) + '.')
            else:
                out.append('- **Goleador:** Betano no ofrece mercados de goleador para este partido (sin leer).')
        else:
            out.append('- **Goleador:** sin historial de goleadores.')
        out.append('')
    open(f'{dia}/resumen_foco.md', 'w', encoding='utf8').write('\n'.join(out) + '\n')
    print('\n'.join(out))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2].split(','))
