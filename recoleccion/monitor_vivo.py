#!/usr/bin/env python3
"""Monitor en vivo (solo lectura; NO es un modelo validado).
Uso: python3 recoleccion/monitor_vivo.py snapshot.json [AAAA-MM-DD]
snapshot.json = salida de recoleccion/monitor_vivo.js (Sofascore, Europa/Conference).
Compara el ritmo en vivo (córners, tiros al arco, tarjetas) con el esperado de la ficha
(registro/lineas.csv) y, con Poisson, da la probabilidad de líneas cercanas.
Los esperados de la ficha son del partido completo (90').
"""
import csv, json, math, re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return set(w for w in re.findall(r'[a-z0-9]+', s) if len(w) > 3)

def esperados(dia):
    R = {}
    for r in csv.DictReader(open('registro/lineas.csv', encoding='utf-8-sig'), delimiter=';'):
        if r['jornada'] != dia or r['jugador'] or r['ambito'] != 'total': continue
        if r['mercado'] in ('corners', 'al_arco', 'tarjetas', 'remates', 'goles') and r['esperado']:
            R.setdefault(r['partido'], {})[r['mercado']] = float(r['esperado'])
    return R

def casar(ev, R):
    a = norm(ev['h']) | norm(ev['a']); best = (0, None)
    for p in R:
        sc = len(a & norm(p))
        if sc > best[0]: best = (sc, p)
    return best[1] if best[0] >= 2 else None

def pois_sf(k, mu):  # P(X >= k)
    if k <= 0: return 1.0
    s = sum(math.exp(-mu) * mu**i / math.factorial(i) for i in range(k))
    return max(0.0, 1 - s)

def proyectar(esp, obs, m):
    """total final proyectado = observado + resto; resto mezcla ficha y ritmo en vivo (peso del ritmo ≤ 0,5)."""
    m = max(m, 1); w = min(m / 90, 0.5)
    resto_ficha = esp * (90 - m) / 90
    resto_vivo = (obs / m) * (90 - m)
    return obs + (1 - w) * resto_ficha + w * resto_vivo

def tot(per, k, ev):
    v = (per.get('ALL') or {}).get(k)
    return sum(v) if v else None

def main():
    snap = json.load(open(sys.argv[1])); dia = sys.argv[2] if len(sys.argv) > 2 else '2026-11-26'
    R = esperados(dia); filas = []
    for ev in snap['ev']:
        p = casar(ev, R); m = ev['min'] if ev['min'] is not None else 45
        e = R.get(p, {}); per = ev['per']
        linea = {'partido': f"{ev['h']} - {ev['a']}", 'marcador': f"{ev['g'][0]}-{ev['g'][1]}", 'min': ev['min'], 'estado': ev['st'], 'ficha': bool(p)}
        for mk, key in (('corners', 'co'), ('al_arco', 'sot'), ('tarjetas', 'yc')):
            obs = tot(per, key, ev); es = e.get(mk)
            if obs is None or es is None: continue
            proy = proyectar(es, obs, m)
            linea[mk] = {'obs': obs, 'esperado_90': es, 'ritmo_vs_ficha': round(obs / max(es * m / 90, 0.1), 2), 'proyectado': round(proy, 1),
                         'P_mas': {str(l): round(pois_sf(int(l + .5), proy - obs) if False else pois_sf(int(l + .5) - int(obs), proy - obs), 2) for l in (math.floor(proy) - 1.5, math.floor(proy) - .5, math.floor(proy) + .5, math.floor(proy) + 1.5) if l > obs}}
        filas.append(linea)
    json.dump(filas, sys.stdout, ensure_ascii=False, indent=1)

if __name__ == '__main__': main()
