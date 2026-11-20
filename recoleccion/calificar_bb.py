# -*- coding: utf-8 -*-
"""Califica con el resultado real los combos de BB Boost (bb/bb_boost_resumen.json) y las misiones (misiones/misiones.json) de una jornada.

    python3 recoleccion/calificar_bb.py jornadas/AAAA-MM-DD <resultados_por_partido.json> [mapa_partidos.json]

  resultados_por_partido.json  {"<partido como en lineas.csv>": {g,c,sh,sot,f,off,gk,y,ti ...}}  (salida de resultados_flashscore.py + mapa)
  mapa_partidos.json           {"<clave/slug>": "<partido>"}  (por defecto <jornada>/resultados/mapa_partidos.json)
Escribe en cada combo: `resultado` (cumplió / falló / pendiente), `patas_real` ([[ok, "valor real"], ...]) y `jugada` (False salvo que se indique).
Un combo cumple solo si TODAS sus patas se dieron; si alguna aún no tiene resultado queda «pendiente» (salvo que otra ya haya fallado: entonces falló).
"""
import json, os, re, sys, unicodedata

MERC = [('tiros al arco', 'sot'), ('remates', 'sh'), ('corners', 'c'), ('goles', 'g'), ('saques de meta', 'gk'), ('saques de banda', 'ti'),
        ('fueras', 'off'), ('faltas', 'f'), ('tarjetas', 'y')]
ETQ = {'sot': 'tiros al arco', 'sh': 'remates', 'c': 'córners', 'g': 'goles', 'gk': 'saques de meta', 'ti': 'saques de banda', 'off': 'fueras de juego', 'f': 'faltas', 'y': 'puntos de tarjetas'}


def n(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()


def partido_de(texto, equipos):
    """equipos: {partido: (palabras_local, palabras_visit)}"""
    t = n(texto)
    for p, (L, V) in equipos.items():
        if any(w in t for w in L + V):
            return p
    return None


def evaluar(pata, partido, R, kw, prefijo=False):
    """→ (ok|None, 'valor real')"""
    t = n(re.sub(r'@[\d,\.]+', '', pata)).strip()
    if prefijo:
        i = min([t.find(nom) for nom, _ in MERC if nom in t] or [0])
        t = t[i:]
    m = re.search(r'(mas|menos)\s+([\d.]+)\s*$', t)
    if not m or partido not in R:
        return None, 'sin resultado'
    lado, linea = m.group(1), float(m.group(2))
    k = next((c for nom, c in MERC if nom in t), None)
    if not k or k not in R[partido]:
        return None, 'sin dato'
    L, V = kw[partido]
    ie = 0 if any(w in t for w in L) else 1 if any(w in t for w in V) else None
    if k == 'off' and 'fueras' in t and ie is None:
        ie = None
    v = R[partido][k]
    val = (v[0] + v[1]) if ie is None else v[ie]
    ok = val > linea if lado == 'mas' else val < linea
    return ok, f"{val:g} {ETQ[k]}" + ('' if ie is None else f" ({'local' if ie == 0 else 'visitante'})")


def combo(pat, partidos, R, kw, equipos, fijo=None, prefijo=False):
    out, oks = [], []
    for p in pat:
        pa = fijo or partido_de(p, equipos)
        ok, real = evaluar(p, pa, R, kw, prefijo)
        out.append([ok, real]); oks.append(ok)
    if any(o is False for o in oks):
        return 'falló', out
    return ('cumplió' if all(o is True for o in oks) else 'pendiente'), out


def main(jor, resf, mapaf=None):
    R = json.load(open(resf, encoding='utf-8'))
    M = json.load(open(mapaf or os.path.join(jor, 'resultados', 'mapa_partidos.json'), encoding='utf-8'))
    # palabras de cada equipo a partir del nombre «Local - Visitante» (+ alias usados en las misiones)
    def pal(nom):
        return [x for x in re.split(r'\W+', n(nom)) if len(x) > 2 and x not in ('fc', 'sc', 'rj', 'sp', 'rs', 'ba', 'de', 'da', 'los', 'city', 'real')]
    kw = {}
    for part in set(M.values()):
        a_, b_ = part.split(' - ')
        La, Vb = pal(a_), pal(b_)
        if 'salt' in Vb: Vb.append('rsl')
        kw[part] = (La, Vb)
    equipos = kw
    pend = 0
    p = os.path.join(jor, 'bb', 'bb_boost_resumen.json')
    if os.path.exists(p):
        B = json.load(open(p, encoding='utf-8'))
        for slug, v in B.items():
            if isinstance(v, dict) and 'combos' in v:
                part = M.get(slug)
                for c in v['combos']:
                    c['resultado'], c['patas_real'] = combo(c['patas'], part, R, kw, equipos, fijo=part)
                    c['jugada'] = c.get('jugada', False)
                    pend += c['resultado'] == 'pendiente'
        json.dump(B, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    p = os.path.join(jor, 'misiones', 'misiones.json')
    if os.path.exists(p):
        Mi = json.load(open(p, encoding='utf-8'))
        for mm in ('m1', 'm2'):
            for c in Mi.get(mm, {}).get('combos', []):
                fijo = partido_de(c['partido'], equipos) if mm == 'm1' else None
                c['resultado'], c['patas_real'] = combo(c['patas'], None, R, kw, equipos, fijo=fijo, prefijo=(mm == 'm2'))
                c['jugada'] = c.get('jugada', False)
        json.dump(Mi, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('combos pendientes:', pend)


if __name__ == '__main__':
    main(*sys.argv[1:4])
