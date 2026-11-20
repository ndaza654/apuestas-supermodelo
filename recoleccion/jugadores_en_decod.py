#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Historial por jugador leído con recoleccion/flashscore_jugadores_en.js (Flashscore en inglés) → jornadas/<día>/jugadores/<partido>.json
(el mismo formato que lee armar_entrada.hist_de) + crudo_<partido>.json + LEEME.md con la cobertura real.
Entrada: un JSON descargado del navegador {spec:{mid:[[<partido>:<L|V>, <L|V del equipo en ese partido>, fecha, rival]]}, pj:{mid:{h,a,rows:{pid:{n,pos,eq,v:{col:valor}}},cols}}, faltan:[...]}
Uso: python3 recoleccion/jugadores_en_decod.py jornadas/AAAA-MM-DD <entrada.json>
Salida por jugador: {lado, pos, pid, p:[[mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas_cometidas, entradas_ganadas, atajadas,
                                          entradas_total, faltas_recibidas, rating, xG]]} (la más reciente primero).
Límites: «Tackles won» = ganadas/intentadas de Flashscore (Betano cuenta entradas totales: no son idénticas); «Fouls suffered» (faltas recibidas) SÍ sale en esta versión en inglés."""
import sys, os, re, json, collections


def num(s):
    if s is None:
        return 0
    s = str(s).strip()
    if s in ('', '-'):
        return 0
    m = re.match(r'^(\d+(?:\.\d+)?)', s)
    return float(m.group(1)) if m else 0


def par(s):
    s = str(s or '').strip()
    m = re.match(r'^(\d+)/(\d+)', s)
    if m:
        return int(m.group(1)), int(m.group(2))
    n = int(num(s))
    return n, n


def main(dia, ent):
    D = json.load(open(ent, encoding='utf8'))
    spec, pj = D['spec'], D['pj']
    por = collections.defaultdict(lambda: collections.defaultdict(dict))     # partido -> lado -> pid -> datos
    cob = collections.defaultdict(lambda: {'L': [0, 0, []], 'V': [0, 0, []]})  # partido -> lado -> [leidos, total, faltan]
    jug = collections.defaultdict(dict)
    for mid, lst in spec.items():
        for key, v, fecha, rival in lst:
            partido, lado = key.split(':')
            cob[partido][lado][1] += 1
            P = pj.get(mid)
            if not P:
                cob[partido][lado][2].append(f'{fecha} vs {rival} ({mid})')
                continue
            cob[partido][lado][0] += 1
            eq = 'H' if v == 'L' else 'A'
            for pid, o in P['rows'].items():
                if o['eq'] != eq:
                    continue
                x = o['v']
                mn = int(num(x.get('Minutes played')))
                if not mn:
                    continue
                g, e = par(x.get('Tackles won'))
                fila = [mid, fecha, mn, int(num(x.get('Total shots'))), int(num(x.get('Shots on target'))), int(num(x.get('Goals'))), int(num(x.get('Assists'))),
                        int(num(x.get('Yellow cards'))), int(num(x.get('Red cards'))), int(num(x.get('Fouls committed'))), g, int(num(x.get('Goalkeeper saves'))), e,
                        int(num(x.get('Fouls suffered'))), num(x.get('Rating')), num(x.get('Expected goals (xG)'))]
                d = jug[partido].setdefault(pid, {'lado': lado, 'pos': o['pos'], 'nombre': o['n'], 'filas': []})
                if not any(r[0] == mid for r in d['filas']):
                    d['filas'].append(fila)
    os.makedirs(f'{dia}/jugadores', exist_ok=True)
    L = ['# Historial por jugador · cobertura real\n', 'Fuente: Flashscore (www.flashscore.com, «Player stats» de cada partido pasado), leído con `recoleccion/flashscore_jugadores_en.js`.\n']
    for partido, jd in jug.items():
        out = {}
        for pid, d in jd.items():
            nombre = d['nombre']
            k, n = nombre, 2
            while k in out:
                k = f'{nombre} #{n}'
                n += 1
            out[k] = {'lado': d['lado'], 'pos': d['pos'], 'pid': pid, 'p': sorted(d['filas'], key=lambda r: r[1], reverse=True)}
        json.dump(out, open(f'{dia}/jugadores/{partido}.json', 'w', encoding='utf8'), ensure_ascii=False)
        L.append(f'\n## {partido}\n')
        for lado in ('L', 'V'):
            ok, tot, falta = cob[partido][lado]
            nj = sum(1 for d in jd.values() if d['lado'] == lado)
            L.append(f'- {"Local" if lado == "L" else "Visitante"}: {ok} de {tot} partidos leídos, {nj} jugadores con minutos.' + (' No se pudo leer: ' + '; '.join(falta) + '.' if falta else ''))
    L.append('\n## Límites\n- «Tackles won» (entradas ganadas/intentadas de Flashscore) no es idéntico a las entradas totales de Betano.\n- Se guardan solo jugadores con minutos > 0; el rating y el xG de Flashscore van en las posiciones 14 y 15.\n- Lo recogido pasa transcrito por el chat y se verifica con hash.')
    open(f'{dia}/jugadores/LEEME.md', 'w', encoding='utf8').write('\n'.join(L) + '\n')
    json.dump({'spec': spec, 'pj': pj}, open(f'{dia}/jugadores/crudo_flashscore_en.json', 'w', encoding='utf8'), ensure_ascii=False)
    print('\n'.join(L))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
