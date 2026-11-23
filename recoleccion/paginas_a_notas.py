#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pasa el texto de la página del partido en Flashscore (www.flashscore.com, inglés; se guarda en jornadas/<día>/paginas/<clave>.txt)
a `notas/<clave>.json` (formato de contexto_mercado.py) SOLO con hechos leídos: competición y fecha, posición y puntos de cada equipo en la
tabla, forma de los últimos 5 (G/E/P), zona de la tabla si Flashscore la rotula, y los datos del partido (árbitro, estadio) como texto.
No inventa motivación ni «necesita ganar»: eso queda para la lectura de Claude (campo `animo` solo trae la racha).
Uso: python3 recoleccion/paginas_a_notas.py jornadas/AAAA-MM-DD [hora_lectura 'HH:MM']   (no pisa notas existentes salvo --forzar)"""
import sys, os, re, json, glob

W = {'W': 'G', 'D': 'E', 'L': 'P'}


def parsear(txt, loc, vis):
    L = [x.strip() for x in txt.split('\n') if x.strip() and x.strip() != 'Advertisement']
    o = {}
    for i, x in enumerate(L):
        if x.startswith('FOOTBALL') and i + 1 < len(L) and L[i + 1] == 'New window':
            o['comp'] = x[len('FOOTBALL'):]
            o['kick'] = L[i + 2] if i + 2 < len(L) else None
            break
    # forma
    if 'FORM' in L:
        i = L.index('FORM')
        o['forma'] = {}
        j = i + 1
        while j < len(L) and re.match(r'^\d+\.$', L[j]):
            eq = L[j + 1]
            k = j + 3
            f = []
            while k < len(L) and L[k] in W:
                f.append(W[L[k]])
                k += 1
            o['forma'][eq] = f
            o.setdefault('pos_forma', {})[eq] = int(L[j][:-1])
            j = k
    # tabla (las columnas se leen del encabezado: «TEAM|MP|W|D|L|G|GD|PTS|FORM» o, p. ej., «GROUP A|MP|W|WO|LO|L|G|PTS|FORM»)
    filas = []
    if 'STANDINGS' in L and '#' in L:
        i = L.index('#')
        k_f = L.index('FORM', i)
        cols = L[i + 2:k_f]
        n = len(cols)
        o['grupo'] = L[i + 1] if L[i + 1] != 'TEAM' else ''
        j = k_f + 1
        while j < len(L):
            if re.match(r'^\d+\.$', L[j]) and j + 1 + n < len(L):
                eq = L[j + 1]
                v = L[j + 2:j + 2 + n]
                if not all(re.match(r'^-?\d+(:\d+)?$', x) for x in v):
                    break
                d = dict(zip(cols, v))
                k = j + 2 + n + 1
                f = []
                while k < len(L) and L[k] in W:
                    f.append(W[L[k]])
                    k += 1
                filas.append({'pos': int(L[j][:-1]), 'equipo': eq, 'pj': int(d.get('MP', 0)), 'g': int(d.get('W', 0)), 'e': int(d['D']) if 'D' in d else None,
                              'p': int(d.get('L', 0)), 'gf_gc': d.get('G'), 'dg': int(d['GD']) if 'GD' in d else None, 'pts': int(d.get('PTS', 0)), 'forma': f, 'cols': d})
                j = k
            else:
                break
        o['zonas'] = [x for x in L[j:j + 8] if re.match(r'^(Promotion|Relegation|Champions|Europa|Conference|Play|Qualification)', x)]
    o['filas'] = filas
    for rol, eq in (('local', loc), ('visitante', vis)):
        fl = [f for f in filas if f['equipo'] == eq]
        o[rol + '_fila'] = fl[0] if fl else None
    return o


def nota(p, loc, vis, hora, arb=None, est=None, fecha_lectura='el día de la jornada'):
    n = {}
    partes = []
    if p.get('comp'):
        partes.append(p['comp'].title() if p['comp'].isupper() else p['comp'])
    t = []
    o_grupo = p.get('grupo') or ''
    for rol, eq in (('local', loc), ('visitante', vis)):
        f = p.get(rol + '_fila')
        if f:
            t.append(f"{f['pos']}. {eq} {f['pts']} pts ({f['pj']} PJ, {f['g']}G{(' ' + str(f['e']) + 'E') if f['e'] is not None else ''} {f['p']}P{(', ' + ', '.join(k + ' ' + v for k, v in f['cols'].items() if k in ('WO', 'LO'))) if 'WO' in f['cols'] else ''}, goles {f['gf_gc']})" + (f" [{o_grupo}]" if o_grupo else ''))
    if t:
        n['tabla'] = ' · '.join(t)
        partes.append('Tabla: ' + n['tabla'])
        fl, fv = p.get('local_fila'), p.get('visitante_fila')
        if fl and fv:
            partes.append(f"Diferencia de puntos entre ambos: {abs(fl['pts'] - fv['pts'])}; hay {len(p['filas'])} equipos en la tabla.")
    else:
        partes.append('La tabla del partido no se pudo leer en esta pasada (copa, play-off o la página no la cargó): posición y puntos sin leer.')
    if p.get('zonas'):
        partes.append('Zonas rotuladas por Flashscore: ' + '; '.join(p['zonas']) + '.')
    n['se_juega'] = ' '.join(partes)
    for rol, eq in (('local', loc), ('visitante', vis)):
        fm = (p.get('forma') or {}).get(eq) or (p.get(rol + '_fila') or {}).get('forma')
        d = {}
        if fm:
            d['animo'] = 'Forma reciente según Flashscore (G ganó, E empató, P perdió; lo más reciente a la derecha): ' + ' '.join(fm)
        n[rol] = d
    if arb:
        n['arbitro'] = arb
    if est:
        n['estadio'] = est
    n['fuentes'] = [f'Flashscore, página del partido (tabla, forma, directos) leída {fecha_lectura} ~{hora} Bogotá']
    return n


if __name__ == '__main__':
    dia = sys.argv[1]
    hora = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('-') else '22:50'
    forzar = '--forzar' in sys.argv
    os.makedirs(f'{dia}/notas', exist_ok=True)
    for f in sorted(glob.glob(f'{dia}/paginas/*.txt')):
        k = os.path.basename(f)[:-4]
        fs = json.load(open(f'{dia}/flashscore/{k}.json', encoding='utf8'))
        p = parsear(open(f, encoding='utf8').read(), fs['local'], fs['visitante'])
        fecha = '%s-%s' % tuple(os.path.basename(dia.rstrip('/')).split('-')[2:0:-1])   # AAAA-MM-DD → DD-MM
        n = nota(p, fs['local'], fs['visitante'], hora, fs.get('arbitro'), fs.get('estadio'), fecha + ' (día de la jornada; confirmar con la hora de lectura)')
        out = f'{dia}/notas/{k}.json'
        if os.path.exists(out) and not forzar:
            print('existe', k)
            continue
        json.dump(n, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        print(k, '|', n.get('tabla', 'sin tabla')[:110])
