#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Une los lotes `pj_*.json` descargados del navegador ({pj, log}), realinea columnas (jugadores_en_realinear.py), decodifica
(jugadores_en_decod.py) y deja jornadas/<día>/jugadores/. Uso: python3 recoleccion/jugadores_fusionar.py jornadas/AAAA-MM-DD lote1.json lote2.json ..."""
import sys, os, json, subprocess

here = os.path.dirname(os.path.abspath(__file__))


def main(dia, lotes):
    spec = json.load(open(f'{dia}/flashscore/jugadores_spec.json', encoding='utf8'))
    pj = {}
    for f in lotes:
        d = json.load(open(f, encoding='utf8'))
        pj.update(d['pj'] if 'pj' in d else d)
    ya = f'{dia}/jugadores/crudo_flashscore_en.json'
    if os.path.exists(ya):                      # conserva lo ya guardado (crudo de lecturas anteriores)
        prev = json.load(open(ya, encoding='utf8'))
        for m, v in prev['pj'].items():
            pj.setdefault(m, v) if 'rows' in v and any('Rating' in k for o in v['rows'].values() for k in o['v']) else None
    os.makedirs(f'{dia}/jugadores', exist_ok=True)
    json.dump({'spec': spec, 'pj': pj, 'faltan': [m for m in spec if m not in pj]}, open('/tmp/crudo_all.json', 'w', encoding='utf8'), ensure_ascii=False)
    subprocess.run([sys.executable, os.path.join(here, 'jugadores_en_realinear.py'), '/tmp/crudo_all.json', '/tmp/pj_real.json'], check=True)
    # el crudo (sin realinear) se guarda tal cual para poder verificar; el decodificador escribe además su propio «crudo» realineado
    subprocess.run([sys.executable, os.path.join(here, 'jugadores_en_decod.py'), dia, '/tmp/pj_real.json'], check=True, stdout=subprocess.DEVNULL)
    json.dump({'spec': spec, 'pj': pj}, open(f'{dia}/jugadores/crudo_flashscore_en.json', 'w', encoding='utf8'), ensure_ascii=False)
    print('partidos pasados leídos', len(pj), 'de', len(spec))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
