# -*- coding: utf-8 -*-
"""Califica los pronósticos de Flashscore (apuesta de la PREVIA del partido y picks de las NOTICIAS) con el marcador real.

    python3 recoleccion/calificar_pronosticos.py jornadas/AAAA-MM-DD <resultados_por_partido.json> [--resultados-de jornadas/OTRA]

Lee `jornadas/<día>/previas_flashscore/*.json` y `jornadas/<día>/noticias/*.json`; el `resultados_por_partido.json` es el mismo de `calificar_lineas.py`
({"<partido>": {"g":[h,a], ...}}). Casa los nombres sin tildes y sin «FC/AFC/CF/SC». Escribe en cada pick `resultado` (cumplió / falló / pendiente) y `real`.
Soporta: resultado (1, X, 2, 1X, X2, 12), goles total Más/Menos con línea, ambos marcan Sí/No. Lo que no sabe calificar queda «pendiente»: no se inventa."""
import glob, json, os, re, sys, unicodedata

RUIDO = {'fc', 'afc', 'cf', 'sc', 'cd', 'ud', 'the', 'de', 'club'}


def toks(s):
    s = unicodedata.normalize('NFKD', s.replace('æ', 'ae').replace('ø', 'o')).encode('ascii', 'ignore').decode().lower()
    return {t for t in re.findall(r'[a-z0-9]+', s) if t not in RUIDO}


def casa(a, b):
    ta, tb = toks(a), toks(b)
    return bool(ta) and bool(tb) and (ta <= tb or tb <= ta)


def buscar(partido, res):
    h, _, a = partido.partition(' - ')
    for k, v in res.items():
        kh, _, ka = k.partition(' - ')
        if casa(h, kh) and casa(a, ka):
            return v
    return None


def evaluar(p, r):
    """p = dict con mercado/lado/línea (o `patas` = lista de patas que deben darse TODAS); r = resultado del partido. Devuelve (True/False/None, texto real)."""
    if p.get('patas'):
        res = [evaluar(dict(q, partido=p.get('partido')), r) for q in p['patas']]
        if any(x[0] is None for x in res):
            return None, res[0][1]
        return all(x[0] for x in res), res[0][1]
    g = r.get('g')
    if not g:
        return None, None
    h, a = g
    m, lado = p.get('mercado'), p.get('lado')
    if m == 'resultado':
        ok = {'1': h > a, 'X': h == a, '2': a > h, '1X': h >= a, 'X2': a >= h, '12': h != a}.get(str(lado))
        return ok, f'{h}-{a}'
    if m == 'goles' and p.get('linea') is not None:
        t = {'local': h, 'visitante': a, 'total': h + a}.get(p.get('ambito') or 'total')
        return (t > p['linea']) if lado == 'Más' else (t < p['linea']), f'{t} goles ({h}-{a})'
    if m == 'goles' and p.get('rango'):
        v = {'local': h, 'visitante': a, 'total': h + a}.get(p.get('ambito') or 'total')
        return p['rango'][0] <= v <= p['rango'][1], f'{v} goles ({h}-{a})'
    if m == 'ambos':
        amb = h > 0 and a > 0
        return (amb if lado == 'Sí' else not amb), f'{h}-{a}'
    return None, f'{h}-{a}'


def main(carpeta, resultados):
    res = json.load(open(resultados, encoding='utf8'))
    n = c = 0
    for f in sorted(glob.glob(os.path.join(carpeta, 'noticias', '*.json')) + glob.glob(os.path.join(carpeta, 'previas_flashscore', '[!_]*.json'))):
        d = json.load(open(f, encoding='utf8'))
        picks = d.get('pronosticos') or ([dict(d['apuesta'], partido=d['partido'])] if d.get('apuesta') else [])
        for p in picks:
            r = buscar(p.get('partido') or d.get('partido', ''), res)
            ok, real = evaluar(p, r) if r else (None, None)
            tgt = p if d.get('pronosticos') else d['apuesta']
            tgt['resultado'] = 'pendiente' if ok is None else ('cumplió' if ok else 'falló')
            tgt['real'] = real
            n += 1
            c += ok is True
        json.dump(d, open(f, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(f'{n} pronósticos revisados, {c} cumplidos')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
