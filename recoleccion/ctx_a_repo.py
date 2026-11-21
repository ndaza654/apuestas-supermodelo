#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vuelca lo leído con la pestaña de contexto (flashscore_alineaciones_en.js `leerLU` + texto de la página del partido) a
jornadas/<día>/paginas/<clave>.txt, alineaciones/<clave>.json y (vía paginas_a_notas.py) notas/<clave>.json.
Entrada: JSON {clave: {mid, txt, lu}} descargado del navegador. Uso: python3 recoleccion/ctx_a_repo.py jornadas/AAAA-MM-DD <entrada.json>... [--hora HH:MM]"""
import sys, os, json, subprocess, datetime

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import alineaciones_en_decod as A


def main(dia, ents, hora):
    os.makedirs(f'{dia}/paginas', exist_ok=True)
    pares, ent_lu = [], {}
    for e in ents:
        D = json.load(open(e, encoding='utf8'))
        for clave, o in D.items():
            if o.get('txt'):
                open(f'{dia}/paginas/{clave}.txt', 'w', encoding='utf8').write(o['txt'])
            if o.get('lu'):
                ent_lu[clave] = o['lu']
    json.dump(ent_lu, open('/tmp/ent_lu.json', 'w', encoding='utf8'), ensure_ascii=False)
    lectura = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')
    A.main(dia, '/tmp/ent_lu.json', [f'{c}={c}' for c in ent_lu], lectura)
    subprocess.run([sys.executable, os.path.join(here, 'paginas_a_notas.py'), dia, hora, '--forzar'], check=True)


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    hora = sys.argv[sys.argv.index('--hora') + 1] if '--hora' in sys.argv else '07:30'
    if hora in a: a.remove(hora)
    main(a[0], a[1:], hora)
