# -*- coding: utf-8 -*-
"""Alineaciones probables de Flashscore en formato «cancha» (formaciones) + bajas → alineaciones/<clave>.json (mismo formato que alineaciones_decod.py).
Entradas (descargadas del navegador): flashscore/probables_crudo.json  {prob:{clave:{mid, formaciones:[{jug:[{n,slug,pid}]},{...}]}}}
                                      flashscore/previa_bajas_crudo.json {pre:{clave:{lineups:{bajas:{L,V}}, texto, grupos}}}
Uso: python3 recoleccion/alineaciones_pitch.py jornadas/AAAA-MM-DD
Nombre: «Apellido I.» a partir del texto del enlace y el slug (apellido-nombre). El primero de cada formación es el arquero.
"""
import sys, os, json


def nombre(n, slug):
    t = slug.split('-')
    k = len(n.split())
    ini = t[k][0].upper() if len(t) > k else ''
    return (n + ' ' + ini + '.').strip() if ini else n


def main(c):
    fs = os.path.join(c, 'flashscore')
    P = json.load(open(os.path.join(fs, 'probables_crudo.json'), encoding='utf-8'))
    B = json.load(open(os.path.join(fs, 'previa_bajas_crudo.json'), encoding='utf-8'))
    os.makedirs(os.path.join(c, 'alineaciones'), exist_ok=True)
    for k, v in P['prob'].items():
        out = {'mid': v.get('mid'), 'tipo': 'Alineaciones probables', 'lectura_utc': P['leido'],
               'probables': {'L': [], 'V': []}, 'bajas': {'L': [], 'V': []}}
        fm = v.get('formaciones') or []
        if len(fm) >= 2 and fm[0]['n'] >= 11 and fm[1]['n'] >= 11:
            for lado, f in (('L', fm[0]), ('V', fm[1])):
                out['probables'][lado] = [[nombre(j['n'], j['slug']), '', j['pid'], 1 if i == 0 else 0] for i, j in enumerate(f['jug'][:11])]
            out['nota'] = 'Alineaciones probables de Flashscore (pestaña Alineaciones); las oficiales salen ~1 h antes del inicio.'
        else:
            out['sin_pestana'] = True
        b = (B['pre'].get(k) or {}).get('lineups', {}).get('bajas', {})
        for lado in ('L', 'V'):
            out['bajas'][lado] = [[x['n'], x['pid'], x.get('motivo') or ''] for x in b.get(lado, [])]
        json.dump(out, open(os.path.join(c, 'alineaciones', k + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        print(k, len(out['probables']['L']), len(out['probables']['V']), len(out['bajas']['L']), len(out['bajas']['V']))


if __name__ == '__main__':
    main(sys.argv[1])
