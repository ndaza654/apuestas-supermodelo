# -*- coding: utf-8 -*-
"""Califica las combinadas ENTRE partidos que Claude envió por el chat (jornadas/<día>/combinadas_enviadas_HHMM.json) con los resultados reales.

    python3 recoleccion/calificar_combinadas_enviadas.py jornadas/AAAA-MM-DD <resultados_por_partido.json>

Escribe en cada combinada `patas_real` ([[true|false, "valor real"], ...]) y `resultado` (cumplió / falló / pendiente). Las patas con línea ENTERA (p. ej. «Más 7.0»)
que caen justo en la línea son push: la pata se anula (Betano devuelve esa selección y la combinada sigue con las demás); se marca true con «= línea: pata anulada».
Patas que entiende: `<mercado> [local|visitante|<equipo>] Más|Menos <línea>` (córners, goles, tarjetas en puntos, remates, tiros al arco, faltas, fueras) y `resultado 1X|X2|12|1|X|2`.
Lo que no entiende o no tiene resultado queda «sin resultado» (la combinada queda pendiente): no se inventa."""
import glob, json, os, re, sys, unicodedata

ETQ = {'gk': 'saques de meta', 'ti': 'saques de banda', 'sot': 'tiros al arco', 'sh': 'remates', 'c': 'córners', 'g': 'goles', 'y': 'puntos de tarjetas', 'f': 'faltas', 'off': 'fueras de juego'}
MERC = [('saques de meta', 'gk'), ('saques de banda', 'ti'), ('tiros al arco', 'sot'), ('remates', 'sh'), ('corners', 'c'), ('goles', 'g'), ('tarjetas', 'y'), ('faltas', 'f'), ('fueras', 'off')]


def n(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()


def partido(txt, R):
    t = re.sub(r'\s+\d{2}:\d{2}$', '', n(txt.replace('–', ' - '))).replace('  ', ' ').strip()
    for p in R:
        if n(p) == t:
            return p
    pal = [w for w in re.split(r'\W+', t) if len(w) > 3 and w not in ('club', 'real', 'city')]
    c = [p for p in R if all(any(w in x for x in re.split(r' - ', n(p))) for w in pal[:1])] if pal else []
    c = [p for p in R if sum(w in n(p) for w in pal) >= min(2, len(pal))] or c
    return c[0] if c else None


def evaluar(texto, p, R):
    t = n(texto)
    if p not in R:
        return None, 'sin resultado'
    r = R[p]
    mr = re.match(r'resultado\s+(1x|x2|12|1|x|2)\s*$', t)
    if mr and 'g' in r:
        gh, ga = r['g']; g = '1' if gh > ga else 'x' if gh == ga else '2'
        sel = mr.group(1)
        return g in sel, f'{gh}-{ga}'
    m = re.search(r'(mas|menos)\s+([\d.]+)\s*$', t)
    if not m:
        return None, 'sin resultado'
    lado, linea = m.group(1), float(m.group(2))
    k = next((c for nom, c in MERC if nom in t), None)
    if not k or k not in r:
        return None, 'sin dato'
    sede = None
    if 'visitante' in t:
        sede = 1
    elif 'local' in t:
        sede = 0
    a, b = (x.strip() for x in re.split(r' - ', n(p)))
    a_, b_ = [w for w in re.split(r'\W+', a) if len(w) > 3], [w for w in re.split(r'\W+', b) if len(w) > 3]
    if sede is None:
        pre = t[:t.find(next(nom for nom, c in MERC if nom in t))] + t[t.find(next(nom for nom, c in MERC if nom in t)):]
        if any(w in t for w in b_ if w not in a_):
            sede = 1
        elif any(w in t for w in a_ if w not in b_):
            sede = 0
    v = r[k]
    val = v[0] + v[1] if sede is None else v[sede]
    if val == linea:
        return True, f'{val:g} {ETQ[k]} = línea {linea:g}: pata anulada (push)'
    ok = val > linea if lado == 'mas' else val < linea
    return ok, f"{val:g} {ETQ[k]}" + ('' if sede is None else (' (local)' if sede == 0 else ' (visitante)'))


def main(jor, resf):
    R = json.load(open(resf, encoding='utf-8'))
    for rc in sorted(glob.glob(os.path.join(jor, 'combinadas_enviadas_*.json'))):
        C = json.load(open(rc, encoding='utf-8'))
        for c in C:
            out = []
            for pt in c['patas']:
                p = partido(pt[0], R)
                out.append(list(evaluar(pt[1], p, R)) if p else [None, 'sin resultado'])
            c['patas_real'] = out
            oks = [o[0] for o in out]
            c['resultado'] = 'falló' if any(o is False for o in oks) else ('cumplió' if all(o is True for o in oks) else 'pendiente')
        json.dump(C, open(rc, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(os.path.basename(rc), {x: sum(c['resultado'] == x for c in C) for x in ('cumplió', 'falló', 'pendiente')})
        for c in C:
            print(' ', c['id'], c['resultado'], c['patas_real'])


if __name__ == '__main__':
    main(*sys.argv[1:3])
