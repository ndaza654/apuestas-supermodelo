# -*- coding: utf-8 -*-
"""Lectores de lo recolectado el 12-nov (Sofascore, árbitros, clima) y utilidades para armar la entrada del supermodelo."""
import json, os, re, unicodedata, statistics as st
RAW = '/home/claude/nov12/raw'
def norm(s):
    s = str(s).replace('ı', 'i').replace('İ', 'I').replace('ø', 'o').replace('Ø', 'O').replace('ł', 'l').replace('đ', 'd').replace('Đ', 'D').replace('ß', 'ss')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9 ]+', ' ', s).strip()
def toks(s): return [t for t in norm(s).split() if t]
def mismo(a, b):
    """True si dos nombres son el mismo jugador: los tokens del más corto están todos en el más largo (admite inicial «P. Esposito»)."""
    ta, tb = toks(a), toks(b)
    if not ta or not tb: return False
    s, l = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    def en(t, L): return any(t == x or (len(t) == 1 and x.startswith(t)) for x in L)
    return all(en(t, l) for t in s) and (len(s) > 1 or len(l) == 1 or s[-1] == l[-1])
def buscar(nombre, lista):
    c = [x for x in lista if mismo(nombre, x)]
    if len(c) == 1: return c[0]
    ex = [x for x in c if norm(x) == norm(nombre)]
    return ex[0] if ex else (c[0] if c and len({norm(x) for x in c}) == 1 else None)
def par(s):
    a, b = s.split('-', 1) if not s.startswith('-') else ('', s[1:])
    f = lambda x: None if x in ('', None) else float(x)
    return [f(a), f(b)]
def sofa(key):
    p = f'{RAW}/sofa_{key}.txt'
    if not os.path.exists(p): return None
    D = dict(h2h=[], tabla=[], xi={'H': [], 'A': []}, miss={'H': [], 'A': []}, forma={'H': [], 'A': []}, jh={'H': [], 'A': []}, form_xi=['', ''])
    for ln in open(p, encoding='utf8').read().splitlines():
        t = ln.split('|'); k = t[0]
        if k == 'EV': D.update(home=t[2], away=t[4], inicio=t[6], torneo=t[7], ronda=t[8].replace('round=', ''))
        elif k == 'REF': D['ref'] = None if len(t) < 4 else dict(nombre=t[1], pais=t[2], partidos=int(t[3] or 0), amarillas=int(t[4] or 0), rojas=int(t[5] or 0), dobles=int(t[6] or 0))
        elif k == 'VEN': D['estadio'] = dict(nombre=t[1], ciudad=t[2], capacidad=t[5] if len(t) > 5 else '')
        elif k == 'MGR': D['dt'] = [t[1], t[2]]
        elif k == 'PF':
            D['pf'] = [dict(zip(('pos', 'pts', 'forma', 'rating'), x.split(','))) for x in t[1:3]]
        elif k == 'H2H': D['h2h_total'] = dict(local=int(t[1]), visitante=int(t[2]), empates=int(t[3]))
        elif k == 'H2': D['h2h'].append(dict(fecha=t[1], comp=t[2], local=t[3], marcador=t[4], visitante=t[5]))
        elif k == 'ST': D['tabla'].append(dict(pos=int(t[1]), equipo=t[2], pj=int(t[3]), g=int(t[4]), e=int(t[5]), p=int(t[6]), gf=int(t[7]), gc=int(t[8]), pts=int(t[9])))
        elif k == 'LU' and len(t) > 3: D['form_xi'] = [t[2], t[3]]
        elif k == 'PL': D['xi'][t[1]].append(dict(nombre=t[2], pos=t[3], xi=t[5] == 'XI'))
        elif k == 'MISS': D['miss'][t[1]].append(dict(nombre=t[2], pos=t[3], tipo=t[4], motivo=t[5], hasta=t[6] if len(t) > 6 else ''))
        elif k == 'F':
            m = dict(fecha=t[2], comp=t[3], v=t[4], rival=t[5], g=par(t[6]), ht=par(t[7][3:]))
            for it in t[8:]:
                a, b = it.split(':', 1)
                m[a] = float(b) if a == 'pos' else par(b)
            D['forma'][t[1]].append(m)
        elif k == 'JH':
            ps = []
            for it in t[5].split(';'):
                v = [float(x) for x in it.split(',')]
                ps.append(dict(i=int(v[0]), min=v[1], remates=v[2], al_arco=v[3], entradas=v[4], faltas=v[5], faltas_recibidas=v[6], goles=v[7], asist=v[8], atajadas=v[9], tarjeta=int(v[10])))
            D['jh'][t[1]].append(dict(nombre=t[2], pos=t[3], partidos=ps))
    return D
def refs():
    out = {}
    p = f'{RAW}/refs_todos.txt'
    if not os.path.exists(p): return out
    for ln in open(p, encoding='utf8').read().splitlines():
        t = ln.split('|')
        if t[0] != 'RS' or ':' not in t[2]: continue
        d = {}
        for it in t[2].split(';'):
            nm, v = it.rsplit(':', 1); a = [int(x) for x in v.split(',')]
            d[nm] = dict(partidos=a[0], amarillas=a[1], rojas=a[2], dobles=a[3], penales=a[4])
        out[t[1]] = d
    return out
def meteo():
    out = {}
    p = f'{RAW}/meteo_todos.txt'
    if not os.path.exists(p): return out
    for ln in open(p, encoding='utf8').read().splitlines():
        t = ln.split('|')
        if t[0] != 'W': continue
        hs = []
        for h in t[2:]:
            m = re.match(r'(\S+) ([\d.-]+)C lluvia ([\d.]+)mm prob (\d+)% viento ([\d.]+) \(rafagas ([\d.]+)\) km/h hum (\d+)%', h)
            if m: hs.append(dict(hora_utc=m.group(1), temp=float(m.group(2)), lluvia_mm=float(m.group(3)), prob=int(m.group(4)), viento=float(m.group(5)), rafagas=float(m.group(6)), humedad=int(m.group(7))))
        out[t[1]] = hs
    return out
OFICIAL = lambda m: 'Friend' not in m['comp']
def stats_modelo(m):
    """Partido de Sofascore → formato 'forma' del modelo: [a favor, en contra]. Tarjetas en puntos de Betano (amarilla 1, roja 2)."""
    s = {'g': m['g']}
    for k in ('xg', 'c', 'sh', 'sot', 'f', 'off', 'ti', 'gk'):
        if k in m and None not in m[k]: s[k] = m[k]
    if 'y' in m and None not in m['y']:
        r = m.get('r') or [0, 0]
        s['y'] = [m['y'][0] + 2 * (r[0] or 0), m['y'][1] + 2 * (r[1] or 0)]
    return s
def media(xs): 
    xs = [x for x in xs if x is not None]
    return round(st.mean(xs), 2) if xs else None
def resumen_forma(ms):
    """Medias a favor / en contra de una lista de partidos (los que traen cada estadística)."""
    out = {}
    for k in ('g', 'xg', 'sh', 'sot', 'c', 'c1', 'f', 'y', 'y1', 'off', 'cr', 'ti', 'gk'):
        v = [m[k] for m in ms if k in m and None not in m[k]]
        if v: out[k] = (media([x[0] for x in v]), media([x[1] for x in v]), len(v))
    pos = [m['pos'] for m in ms if m.get('pos')]
    if pos: out['pos'] = (media(pos), None, len(pos))
    return out
