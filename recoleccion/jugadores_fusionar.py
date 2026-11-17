# -*- coding: utf-8 -*-
"""Fusiona en jugadores/<clave>.json las entradas duplicadas del mismo jugador por la forma del nombre (Opta «Højlund R.» + Flashscore «Hojlund R.», «Ødegaard»/«Odegaard», «Mæhle»/«Maehle»).
Se queda con la grafía sin signos especiales (la que escribe Betano), une las filas `p` (sin repetir partido), `opta` y `fs`. Idempotente.
Uso: python3 recoleccion/jugadores_fusionar.py jornadas/AAAA-MM-DD [clave ...]"""
import sys, os, json
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pj_json_decod import norm


def fusionar(d):
    g = defaultdict(list)
    for k in d:
        g[norm(k)].append(k)
    out, fus = {}, []
    for ks in g.values():
        if len(ks) == 1:
            out[ks[0]] = d[ks[0]]
            continue
        ks.sort(key=lambda k: (not k.isascii(), k))          # primero la grafía ascii
        base = json.loads(json.dumps(d[ks[0]]))
        for k in ks[1:]:
            o = d[k]
            mids = {x[0] for x in base['p']}
            base['p'] += [x for x in o['p'] if x[0] not in mids]
            if o.get('opta'):
                mo = {x[0] for x in base.get('opta', [])}
                base.setdefault('opta', []).extend(x for x in o['opta'] if x[0] not in mo)
            if o.get('fs'):
                base.setdefault('fs', {}).update(o['fs'])
            if not base.get('pid') and o.get('pid'):
                base['pid'] = o['pid']
        base['p'].sort(key=lambda x: x[1], reverse=True)
        out[ks[0]] = base
        fus.append((ks, len(base['p'])))
    return out, fus


if __name__ == '__main__':
    c = sys.argv[1]
    jd = os.path.join(c, 'jugadores')
    claves = sys.argv[2:] or [f[:-5] for f in sorted(os.listdir(jd)) if f.endswith('.json')]
    for k in claves:
        p = os.path.join(jd, k + '.json')
        d = json.load(open(p, encoding='utf-8'))
        d2, fus = fusionar(d)
        if fus:
            json.dump(d2, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
            print(k, len(fus), 'jugadores fusionados:', '; '.join(f"{'+'.join(a)}→{n} partidos" for a, n in fus[:12]))
