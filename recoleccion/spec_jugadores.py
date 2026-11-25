#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el `spec` de jugadores_en_decod.py desde jornadas/<día>/flashscore/<clave>.json (forma de cada equipo) y la cola de mids.
Uso: python3 recoleccion/spec_jugadores.py jornadas/AAAA-MM-DD [cola.json]
  → jornadas/AAAA-MM-DD/crudo/spec_jugadores.json  {mid: [[<clave>:<L|V>, <L|V del equipo en ese partido>, fecha, rival]]}  (solo los mids de la cola si se da)
  → imprime los mids a leer en tandas (lista para pegar en el navegador)."""
import sys, os, json, glob

dia = sys.argv[1]
cola = set(json.load(open(sys.argv[2], encoding='utf8'))) if len(sys.argv) > 2 else None
spec = {}
for f in sorted(glob.glob(f'{dia}/flashscore/*.json')):
    c = os.path.basename(f)[:-5]
    if c.startswith('jugadores_'):
        continue
    d = json.load(open(f, encoding='utf8'))
    for lado, k in (('L', 'local'), ('V', 'visitante')):
        for p in d['forma'][k]:
            if cola is not None and p['mid'] not in cola:
                continue
            spec.setdefault(p['mid'], []).append([f'{c}:{lado}', p['v'], p['fecha'], p['rival']])
json.dump(spec, open(f'{dia}/crudo/spec_jugadores.json', 'w', encoding='utf8'), ensure_ascii=False)
print(len(spec), 'partidos en el spec')
