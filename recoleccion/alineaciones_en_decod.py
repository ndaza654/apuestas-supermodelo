#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Entrada descargada del navegador con flashscore_alineaciones_en.js → jornadas/<día>/alineaciones/<clave>.json (formato compacto de alineaciones/LEEME.md).
Uso: python3 recoleccion/alineaciones_en_decod.py jornadas/AAAA-MM-DD <entrada.json> <clave>=<atajo> ...   (el JSON es {atajo: resultado de leerLU})
Nombre «Apellido I.» a partir del texto del enlace y del slug; el primero de cada formación es el arquero."""
import sys, os, json, datetime


def nombre(n, slug):
    t = slug.split('-')
    k = len(n.split())
    ini = t[k][0].upper() if len(t) > k else ''
    return (n + ' ' + ini + '.').strip() if ini else n


def main(dia, ent, pares, lectura):
    D = json.load(open(ent, encoding='utf8'))
    os.makedirs(f'{dia}/alineaciones', exist_ok=True)
    for par in pares:
        clave, at = par.split('=')
        v = D[at]
        out = {'mid': v['mid'], 'url': v.get('url'), 'tipo': 'Alineaciones probables' if 'redicted' in (v.get('tipo') or '') else (v.get('tipo') or 'Alineaciones'),
               'lectura_utc': lectura, 'probables': {'L': [], 'V': []}, 'bajas': {'L': [], 'V': []}}
        if v.get('sin_pestana') or not v['probables']['L']:
            out['sin_pestana'] = True
        else:
            for lado in ('L', 'V'):
                out['probables'][lado] = [[nombre(j['n'], j['slug']), '', j['pid'], 1 if i == 0 else 0] for i, j in enumerate(v['probables'][lado][:11])]
            out['nota'] = 'Alineaciones probables de Flashscore (pestaña Lineups, en inglés); las oficiales salen ~1 h antes del inicio: releer entonces.'
        for lado in ('L', 'V'):
            out['bajas'][lado] = [[x['n'], x['pid'], x.get('motivo') or ''] for x in v['bajas'][lado]]
        json.dump(out, open(f'{dia}/alineaciones/{clave}.json', 'w', encoding='utf8'), ensure_ascii=False)
        print(clave, len(out['probables']['L']), len(out['probables']['V']), out['bajas'])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3:], datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ'))
