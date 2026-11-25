#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte lo leído con `flashscore_partido_toplevel.js` (`leerPartido`, pestaña de nivel superior; descarga {mid: {resumen, lu_texto, lu_anclas,
formaciones, st_texto,...}}) al formato del repo: paginas/<clave>.txt, alineaciones/<clave>.json y notas/<clave>.json (vía ctx_a_repo.py).
Las bajas («WILL NOT PLAY»/«QUESTIONABLE») salen sin lado en el texto: se asignan por nombre contra jugadores/<clave>.json; las que no calzan
quedan en `bajas_sin_lado` (no se inventa el lado).
Uso: python3 recoleccion/ctx_top_a_repo.py jornadas/AAAA-MM-DD <entrada.json> [--hora HH:MM]"""
import sys, os, json, re, subprocess, unicodedata


def nz(x):
    x = unicodedata.normalize('NFD', (x or '').lower())
    return re.sub(r'[^a-z0-9 ]+', '', ''.join(c for c in x if unicodedata.category(c) != 'Mn')).strip()

here = os.path.dirname(os.path.abspath(__file__))


def bajas_texto(t):
    """[(nombre, motivo, categoria)] de las secciones WILL NOT PLAY / QUESTIONABLE del texto de la pestaña Lineups."""
    out, cat = [], None
    L = [x.strip() for x in t.split('\n') if x.strip()]
    i = 0
    while i < len(L):
        x = L[i]
        if x in ('WILL NOT PLAY', 'QUESTIONABLE', 'DOUBTFUL'):
            cat = x
        elif x in ('COACHES', 'ODDS'):
            cat = None
        elif cat and i + 1 < len(L):
            out.append((x, L[i + 1], cat)); i += 1
        i += 1
    return out


def lu_de(o):
    anc = [a for a in o['lu_anclas'] if a['n'] and 'ParticipantName' in a['c']][:22]
    forma = [[s.strip() for s in f.split('|', 1)[1].split(';') if s.strip()] for f in o['formaciones']]
    hrefs = {}
    for a in anc:
        p = a['h'].split('/')
        hrefs.setdefault(a['n'], (p[2], p[3]) if len(p) > 3 else ('', ''))
    def lado(nombres):
        r = []
        for n in nombres:
            slug, pid = hrefs.get(n, ('', ''))
            r.append({'n': n, 'slug': slug, 'pid': pid})
        return r
    if len(forma) < 2:
        return {'mid': o['mid'], 'url': o.get('url'), 'tipo': None, 'sin_pestana': True, 'probables': {'L': [], 'V': []}, 'bajas': {'L': [], 'V': []}}
    tipo = 'Predicted lineups' if 'PREDICTED' in o['lu_texto'].upper() else 'Confirmed lineups'
    return {'mid': o['mid'], 'url': o.get('url'), 'tipo': tipo, 'probables': {'L': lado(forma[0]), 'V': lado(forma[1])}, 'bajas': {'L': [], 'V': []}}


def main(dia, ent, hora):
    D = json.load(open(ent, encoding='utf8'))
    mapa = json.load(open(f'{dia}/mapa_claves.json', encoding='utf8'))
    sal, sin_lado = {}, {}
    for mid, o in D.items():
        clave = (mapa.get(mid) or {}).get('clave')
        if not clave:
            print('sin clave para', mid); continue
        txt = o['resumen'] + '\n' + (o.get('st_texto') or '')
        lu = lu_de(o)
        jp = f'{dia}/jugadores/{clave}.json'
        J = json.load(open(jp, encoding='utf8')) if os.path.exists(jp) else {}
        por = {}
        for nom, d in J.items():
            if isinstance(d, dict) and d.get('lado'):
                por.setdefault(nz(re.sub(r'\s*#\d+$', '', nom)), d['lado'])
        sl = []
        bt = [] if lu.get('sin_pestana') else bajas_texto(o['lu_texto'])
        lados = [por.get(nz(n)) for n, _, _ in bt]
        # El texto trae primero el bloque del local y luego el del visitante: un jugador sin historial toma el lado de sus vecinos si ambos coinciden.
        for i, l in enumerate(lados):
            if l:
                continue
            ant = next((lados[j] for j in range(i - 1, -1, -1) if lados[j]), None)
            sig = next((lados[j] for j in range(i + 1, len(lados)) if lados[j]), None)
            if (ant == sig and ant) or (ant is None and sig == 'L') or (sig is None and ant == 'V'):
                lados[i] = (ant or sig) + '*'
        for (n, motivo, cat), lado in zip(bt, lados):
            etq = motivo if cat == 'WILL NOT PLAY' else f'{cat.capitalize()}: {motivo}'
            if lado:
                lu['bajas'][lado[0]].append({'n': n, 'pid': '', 'motivo': etq + (' (lado inferido por el orden del texto)' if lado.endswith('*') else '')})
            else:
                sl.append([n, etq])
        sin_lado[clave] = sl
        sal[clave] = {'mid': mid, 'txt': txt, 'lu': lu}
    json.dump(sal, open('/tmp/ent_ctx.json', 'w', encoding='utf8'), ensure_ascii=False)
    subprocess.run([sys.executable, os.path.join(here, 'ctx_a_repo.py'), dia, '/tmp/ent_ctx.json', '--hora', hora], check=True)
    for clave, sl in sin_lado.items():
        f = f'{dia}/alineaciones/{clave}.json'
        if os.path.exists(f):
            a = json.load(open(f, encoding='utf8')); a['bajas_sin_lado'] = sl
            json.dump(a, open(f, 'w', encoding='utf8'), ensure_ascii=False)
        print(clave, 'bajas sin lado:', len(sl))


if __name__ == '__main__':
    h = sys.argv[sys.argv.index('--hora') + 1] if '--hora' in sys.argv else '22:30'
    a = [x for i, x in enumerate(sys.argv[1:], 1) if not x.startswith('--') and not (sys.argv[i - 1] == '--hora')]
    main(a[0], a[1], h)   # antes la hora se perdía (quedaba en a y se usaba 22:30 siempre)
