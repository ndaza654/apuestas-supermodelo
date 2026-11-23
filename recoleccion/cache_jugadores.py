#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Caché del historial por jugador (diseño aprobado 23-nov-2026): lo ya leído en jornadas anteriores no se vuelve a leer.

Índice: de cada `jornadas/*/jugadores/<partido>.json` (jugador → {lado, pos, pid, p:[filas], fs:{mid: estadísticas}}) y del equipo que cada lado
representa en esa jornada (`jornadas/*/flashscore/<partido>.json`: local / visitante) sale (equipo, mid) → jugadores.
  python3 recoleccion/cache_jugadores.py cola jornadas/AAAA-MM-DD [--claves a,b,c]
      → escribe jornadas/AAAA-MM-DD/flashscore/jugadores_cola.json (mids que faltan, uno por partido pasado) y jugadores_cache_cobertura.json
  python3 recoleccion/cache_jugadores.py fusionar jornadas/AAAA-MM-DD
      → completa jugadores/<partido>.json con las filas en caché de cada equipo (después de que jugadores_en_decod.py escribió lo nuevo)
Límite: la caché solo cubre equipos y partidos ya leídos; el nombre del equipo se compara normalizado (sin acentos, minúsculas)."""
import glob, json, os, re, sys, unicodedata


def n(s):
    s = unicodedata.normalize('NFD', (s or '').lower())
    return re.sub(r'[^a-z0-9]+', '', ''.join(c for c in s if unicodedata.category(c) != 'Mn'))


def indice(excluir=None):
    idx = {}
    for f in sorted(glob.glob('jornadas/*/jugadores/*.json')):
        jor = f.split('/')[1]
        if excluir and jor == excluir:
            continue
        clave = os.path.basename(f)[:-5]
        if clave.startswith('crudo') or clave.startswith('cobertura'):
            continue
        fsj = os.path.join('jornadas', jor, 'flashscore', clave + '.json')
        if not os.path.exists(fsj):
            continue
        try:
            F = json.load(open(fsj, encoding='utf8')); J = json.load(open(f, encoding='utf8'))
        except Exception:
            continue
        eq = {'L': n(F.get('local')), 'V': n(F.get('visitante'))}
        for nombre, d in J.items():
            if not isinstance(d, dict) or d.get('lado') not in eq:
                continue
            for r in d.get('p', []):
                k = (eq[d['lado']], r[0])
                idx.setdefault(k, {})[nombre] = {'pid': d.get('pid'), 'pos': d.get('pos'), 'fila': r, 'fs': (d.get('fs') or {}).get(r[0])}
    return idx


def mids_equipo(jor, clave):
    F = json.load(open(os.path.join(jor, 'flashscore', clave + '.json'), encoding='utf8'))
    return {'L': (F['local'], [e['mid'] for e in F['forma']['local']]), 'V': (F['visitante'], [e['mid'] for e in F['forma']['visitante']])}


def cola(jor, claves):
    idx = indice(excluir=os.path.basename(jor.rstrip('/')))
    faltan, cob = [], {}
    for c in claves:
        for lado, (nom, mids) in mids_equipo(jor, c).items():
            hechos = [m for m in mids if (n(nom), m) in idx]
            cob[f'{c}:{lado}:{nom}'] = {'en_cache': len(hechos), 'de': len(mids), 'faltan': [m for m in mids if m not in hechos]}
            for m in mids:
                if m not in hechos and m not in faltan:
                    faltan.append(m)
    json.dump(faltan, open(os.path.join(jor, 'flashscore', 'jugadores_cola.json'), 'w'))
    json.dump(cob, open(os.path.join(jor, 'flashscore', 'jugadores_cache_cobertura.json'), 'w'), ensure_ascii=False, indent=1)
    tot = sum(v['de'] for v in cob.values()); hc = sum(v['en_cache'] for v in cob.values())
    print(f'equipos {len(cob)}: {hc} de {tot} partidos-equipo ya en caché; a leer: {len(faltan)} partidos distintos')
    return faltan


def fusionar(jor):
    idx = indice(excluir=os.path.basename(jor.rstrip('/')))
    tot = 0
    for f in sorted(glob.glob(os.path.join(jor, 'jugadores', '*.json'))):
        clave = os.path.basename(f)[:-5]
        if clave.startswith('crudo'):
            continue
        J = json.load(open(f, encoding='utf8'))
        eqs = mids_equipo(jor, clave)
        for lado, (nom, mids) in eqs.items():
            for m in mids:
                datos = idx.get((n(nom), m))
                if not datos:
                    continue
                for nombre, d in datos.items():
                    cur = J.setdefault(nombre, {'lado': lado, 'pos': d['pos'], 'pid': d['pid'], 'p': [], 'fs': {}})
                    if cur.get('lado') != lado:
                        continue
                    if not any(r[0] == m for r in cur['p']):
                        cur['p'].append(d['fila']); tot += 1
                    if d['fs'] and m not in cur.setdefault('fs', {}):
                        cur['fs'][m] = d['fs']
        orden = {m: i for lado, (nom, mids) in eqs.items() for i, m in enumerate(mids)}
        for d in J.values():
            if isinstance(d, dict) and 'p' in d:
                d['p'].sort(key=lambda r: orden.get(r[0], 99))
        json.dump(J, open(f, 'w', encoding='utf8'), ensure_ascii=False)
    print('filas añadidas desde caché:', tot)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'cola':
        cl = a[a.index('--claves') + 1].split(',') if '--claves' in a else sorted(os.path.basename(x)[:-5] for x in glob.glob(os.path.join(a[1], 'flashscore', '*.json')) if not os.path.basename(x).startswith(('jugadores', 'goles')))
        cola(a[1], cl)
    elif a[0] == 'fusionar':
        fusionar(a[1])
