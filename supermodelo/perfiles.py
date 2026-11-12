# -*- coding: utf-8 -*-
"""Perfiles de equipo (heredado del kit v1: peso reciente 0,92, encogimiento k=3, normalización local/visitante).

Cada partido de un equipo es un dict:
  {'v': 'H'|'A', 'stats': {'c': (a_favor, en_contra), 'sh': (...), 'sot': ..., 'f': ..., 'y': ..., 'g': ..., 'xg': ...,
                           'off': ..., 'gk': ..., 'ti': ...},
   'ht': (gf, gc) opcional, 'pos': posesión propia opcional}
ordenados del más reciente al más antiguo.

Además de las medias, calcula dos rasgos de contexto que el v1 no tenía:
  · sensibilidad al marcador: cuánto cambia el volumen del equipo en el 2.º tiempo según cómo iba al descanso
    (1 = normal; >1 se encierra mucho al ganar / se vuelca mucho al perder; <1 sigue igual pase lo que pase).
  · posesión media (para leer quién tendrá la pelota).
"""
import numpy as np
from . import config as C

STATS = ['c', 'sh', 'sot', 'f', 'y', 'g', 'xg', 'off', 'gk', 'ti']


def promedios_grupo(equipos):
    """Medias del grupo de equipos por condición (H/A), para normalizar y encoger."""
    pool = {s: {'H': [], 'A': []} for s in STATS}
    for partidos in equipos.values():
        for p in partidos:
            for s in STATS:
                x = p['stats'].get(s)
                if x is not None:
                    pool[s][p['v']].append(x[0])
    out = {}
    for s in STATS:
        h, a = pool[s]['H'], pool[s]['A']
        if not h and not a:
            continue
        Hf = float(np.mean(h)) if h else float(np.mean(a))
        Af = float(np.mean(a)) if a else float(np.mean(h))
        out[s] = dict(H=Hf, A=Af, N=(Hf + Af) / 2)
    return out


def perfil(partidos, grupo):
    """Media a favor y en contra (neutral) por estadística, con peso reciente y encogimiento."""
    prof = {}
    for s, g in grupo.items():
        sf = sa = sw = 0.0
        n = 0
        for k, p in enumerate(partidos):
            x = p['stats'].get(s)
            if x is None:
                continue
            w = C.DECAY ** k
            f, a = x
            if p['v'] == 'H':
                f *= g['N'] / g['H'] if g['H'] else 1
                a *= g['N'] / g['A'] if g['A'] else 1
            else:
                f *= g['N'] / g['A'] if g['A'] else 1
                a *= g['N'] / g['H'] if g['H'] else 1
            sf += w * f; sa += w * a; sw += w; n += 1
        if sw == 0:
            prof[s] = dict(f=g['N'], a=g['N'], n=0)
            continue
        lam = sw / (sw + C.SHRINK_K)
        prof[s] = dict(f=lam * sf / sw + (1 - lam) * g['N'], a=lam * sa / sw + (1 - lam) * g['N'], n=n)
    # rasgos de contexto
    prof['_sens'] = sensibilidad_marcador(partidos)
    pos = [p.get('pos') for p in partidos if p.get('pos') is not None]
    prof['_pos'] = float(np.mean(pos)) if pos else None
    prof['_n'] = len(partidos)
    return prof


def sensibilidad_marcador(partidos):
    """Compara la cuota de remates del equipo en el 2.º tiempo contra el 1.º según iba al descanso.
    Devuelve un factor ~1 (encogido hacia 1 con pocos datos)."""
    cambios = []
    for p in partidos:
        ht = p.get('ht'); s1 = p.get('sh_1t'); s2 = p.get('sh_2t')
        if not ht or not s1 or not s2 or sum(s1) == 0 or sum(s2) == 0:
            continue
        d = ht[0] - ht[1]
        if d == 0:
            continue
        cambio = s2[0] / sum(s2) - s1[0] / sum(s1)
        esperado = -0.095 if d > 0 else 0.095   # balance 4–8 nov: ±9,5 pts
        cambios.append(cambio / esperado)
    if not cambios:
        return 1.0
    n = len(cambios)
    est = float(np.clip(np.mean(cambios), 0.0, 2.5))
    lam = n / (n + 4.0)
    return lam * est + (1 - lam) * 1.0


def media_partido(prof_local, prof_visit, grupo, s):
    """Media esperada de la estadística s para cada equipo en este partido (0,6 propio + 0,4 concedido)."""
    g = grupo[s]
    base_h = (1 - C.W_OPP) * prof_local[s]['f'] + C.W_OPP * prof_visit[s]['a']
    base_a = (1 - C.W_OPP) * prof_visit[s]['f'] + C.W_OPP * prof_local[s]['a']
    return base_h * g['H'] / g['N'], base_a * g['A'] / g['N']


# ---------------------------------------------------------------- adaptadores de formato
def desde_kit_v1(ruta):
    """Lee teams12.txt / ecl12.txt del kit v1: 'Equipo :: H c_f/c_a sh_f/sh_a sot_f/sot_a f_f/f_a y_f/y_a ; ...'"""
    claves = ['c', 'sh', 'sot', 'f', 'y']
    equipos = {}
    for linea in open(ruta, encoding='utf8'):
        if '::' not in linea:
            continue
        nombre, resto = linea.split('::')
        partidos = []
        for seg in resto.split(';'):
            tok = seg.split()
            if not tok:
                continue
            st = {}
            for k, t in zip(claves, tok[1:]):
                if t != 'NA':
                    a, b = t.split('/')
                    st[k] = (float(a), float(b))
            # saneo heredado: remates imposibles invalidan córners/remates/al arco
            if 'sh' in st and sum(st['sh']) < 12:
                for k in ('c', 'sh', 'sot'):
                    st.pop(k, None)
            if 'f' in st and sum(st['f']) == 0:
                st.pop('f')
            partidos.append(dict(v=tok[0], stats=st))
        equipos[nombre.strip()] = partidos
    return equipos


def desde_flashscore_rows(lineas, codigo):
    """Lee el formato fs_rows.txt de las plantillas (build6.py): 'cod H|A fecha v rival marcador k1a/b k2a/b ... comp x'."""
    import re
    equipos = {'H': [], 'A': []}
    for ln in lineas:
        if not ln.startswith(codigo + ' '):
            continue
        t = ln.split(); lado, v = t[1], t[3]
        gf, ga = map(int, t[5].split('-'))
        st = {'g': (gf, ga)}
        for tok in t[6:-2]:
            m = re.match(r'([a-z]+)(NA|[\d.]+/[\d.]+)$', tok)
            if not m or m.group(2) == 'NA':
                continue
            a, b = m.group(2).split('/')
            st[m.group(1)] = (float(a), float(b))
        equipos[lado].append(dict(v=v, stats=st))
    return equipos
