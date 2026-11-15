# -*- coding: utf-8 -*-
"""Pasa el texto compacto de Flashscore (lo emite `__enc` en el navegador) a JSON de contexto.
Uso: python3 recoleccion/flashscore_decod.py jornadas/AAAA-MM-DD/raw   (lee fs_<clave>.txt → flashscore/<clave>.json)
Líneas: M|mid|local|visitante|árbitro|país|estadio|capacidad|n · A|aviso · F|L/V|fecha|rival|comp|v|mid|g:g|stats|stats_1t · H|fecha|comp|mid|g:g|stats|stats_1t
stats = k=a:b,k=a:b (local:visitante del propio partido, ya orientado al equipo en F y al local en H)."""
import sys, os, glob, json

def st(s):
    o = {}
    for p in filter(None, s.split(',')):
        k, v = p.split('=')
        a, b = v.split(':')
        o[k] = [float(a) if '.' in a else int(a), float(b) if '.' in b else int(b)]
    return o

def gol(s):
    a, b = s.split(':')
    return [int(a), int(b)]

def decod(texto):
    c = {'forma': {'local': [], 'visitante': []}, 'h2h': [], 'avisos': []}
    for ln in texto.split('\n'):
        p = ln.split('|')
        if p[0] == 'M':
            c.update(mid=p[1], local=p[2], visitante=p[3], arbitro=p[4] or None, arbitro_pais=p[5] or None,
                     estadio=p[6] or None, capacidad=p[7] or None, n=int(p[8]))
        elif p[0] == 'A':
            c['avisos'].append('|'.join(p[1:]))
        elif p[0] == 'F':
            c['forma']['local' if p[1] == 'L' else 'visitante'].append(
                dict(fecha=p[2], rival=p[3], comp=p[4], v=p[5], mid=p[6], g=gol(p[7]), stats=st(p[8]), stats_1t=st(p[9])))
        elif p[0] == 'H':
            c['h2h'].append(dict(fecha=p[1], comp=p[2], mid=p[3], g=gol(p[4]), stats=st(p[5]), stats_1t=st(p[6])))
    return c

if __name__ == '__main__':
    raw = sys.argv[1]
    out = os.path.join(os.path.dirname(raw.rstrip('/')), 'flashscore')
    os.makedirs(out, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(raw, 'fs_*.txt'))):
        clave = os.path.basename(f)[3:-4]
        c = decod(open(f, encoding='utf8').read().rstrip('\n'))
        json.dump(c, open(os.path.join(out, clave + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        print(clave, c['local'], c['visitante'], len(c['forma']['local']), len(c['forma']['visitante']), len(c['h2h']))
