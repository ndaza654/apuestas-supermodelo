# -*- coding: utf-8 -*-
"""Pasa el texto compacto del historial por jugador (lo emite `__exportar` de flashscore_jugadores_iframe.js) a
jornadas/AAAA-MM-DD/jugadores/<partido>.json, el formato que lee armar_entrada.hist_de().
Uso: python3 recoleccion/jugadores_decod.py jornadas/AAAA-MM-DD   (lee raw/pj_<partido>__<L|V>.txt)
Texto: T|<partido>:<L|V>  ·  R|pid|nombre|posición  ·  J|pid|mid|fecha|min|goles|asist|remates|al_arco|entradas(ganadas/total)|faltas|atajadas|amarillas|rojas|rating|xG
Salida por jugador: {lado, pos, pid, p: [[mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas, entradas_ganadas, atajadas, entradas_total]]}
(la más reciente primero). Las atajadas solo cuentan para porteros. Faltas recibidas NO existen en Flashscore: no se inventan."""
import sys, os, glob, json, collections


def decod(texto):
    clave = None
    ros, filas = {}, collections.defaultdict(list)
    for ln in texto.split('\n'):
        p = ln.split('|')
        if p[0] == 'T':
            clave = p[1]
        elif p[0] == 'R':
            ros[p[1]] = (p[2], p[3])
        elif p[0] == 'J':
            _, pid, mid, fecha, mn, g, a, sh, sot, en, fa, sv, am, ro, rt, xg = p
            if any(x[0] == mid for x in filas[pid]):
                continue
            eg, et = (en.split('/') + ['0'])[:2]
            filas[pid].append([mid, fecha, int(float(mn)), int(float(sh)), int(float(sot)), int(float(g)), int(float(a)),
                               int(float(am)), int(float(ro)), int(float(fa)), int(eg), int(float(sv)), int(et)])
    out = {}
    lado = clave.split(':')[1] if clave and ':' in clave else None
    for pid, (nm, pos) in ros.items():
        ps = sorted(filas.get(pid, []), key=lambda r: r[1], reverse=True)
        nombre = nm
        k = nombre
        n = 2
        while k in out:                       # nombres repetidos en un mismo equipo: se distinguen por id
            k = f'{nombre} #{n}'
            n += 1
        out[k] = {'lado': lado, 'pos': pos, 'pid': pid, 'p': ps}
    return clave, out


if __name__ == '__main__':
    jor = sys.argv[1]
    raw = os.path.join(jor, 'raw')
    # pj_<partido>__<L|V>.txt  (o con sufijo __a / __b si se leyó desde varias pestañas: se unen las filas de cada equipo)
    grupos = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(raw, 'pj_*.txt'))):
        base = os.path.basename(f)[3:-4].split('__')
        grupos[(base[0], base[1])].append(f)
    por_partido = collections.defaultdict(dict)
    for (partido, lado), fs in sorted(grupos.items()):
        texto = '\n'.join(l for f in fs for l in open(f, encoding='utf8').read().rstrip('\n').split('\n')
                          if not l.startswith('T|')).strip('\n')
        clave, d = decod('T|%s:%s\n%s' % (partido, lado, texto))
        por_partido[partido].update(d)
        filas = sum(len(v['p']) for v in d.values())
        print(partido, lado, len(d), 'jugadores', filas, 'apariciones', '(%d archivos)' % len(fs))
    os.makedirs(os.path.join(jor, 'jugadores'), exist_ok=True)
    for partido, d in por_partido.items():
        json.dump(d, open(os.path.join(jor, 'jugadores', partido + '.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
