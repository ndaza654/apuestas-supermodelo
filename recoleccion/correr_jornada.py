# -*- coding: utf-8 -*-
"""Etapa de ANÁLISIS de una jornada (corre sin navegador, por ejemplo en la nube): usa solo lo ya recolectado y guardado en el repo.

    python3 recoleccion/correr_jornada.py jornadas/2026-11-13

Lee      jornadas/<día>/betano/*.json  (+ flashscore/*.json, notas/*.json si existen)
Escribe  entradas/ (armadas), fichas/ (por mercado), informes/ (modelo SM-1.2 de cada partido apto o en reserva), ranking.md y ranking.json.
Si falta lo recolectado lo dice y termina; NO inventa datos.
"""
import os, sys, json, glob, shutil, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import armar_entrada as A, ficha as FI, puntuar as PU


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    base = argv[0]
    betanos = sorted(glob.glob(os.path.join(base, 'betano', '*.json')))
    if not betanos:
        print(f'Sin datos recolectados: no hay {base}/betano/*.json. La etapa 1 (recolección) no dejó nada; no hay nada que analizar.')
        return 2
    A.main([base])
    ent = os.path.join(base, 'entradas')
    PU.main([ent, base])                                              # ranking.json / ranking.md en la carpeta de la jornada
    R = json.load(open(os.path.join(base, 'ranking.json'), encoding='utf8'))
    orden = {r['partido']: r['estado'] for r in R}
    os.makedirs(os.path.join(base, 'fichas'), exist_ok=True)
    os.makedirs(os.path.join(base, 'informes'), exist_ok=True)
    for p in sorted(glob.glob(os.path.join(ent, '*.json'))):
        k = os.path.basename(p)[:-5]
        e = json.load(open(p, encoding='utf8'))
        nombre = f"{e['local']} - {e['visitante']}"
        FI.main(['ficha', p, os.path.join(base, 'fichas')])
        if orden.get(nombre) in ('apto', 'reserva'):
            r = subprocess.run([sys.executable, '-m', 'supermodelo', os.path.abspath(p)], cwd=RAIZ, capture_output=True, text=True)
            for suf in ('_informe.md', '_informe.html', '_resultado.json'):
                o = os.path.join(ent, k + suf)
                if os.path.exists(o):
                    shutil.move(o, os.path.join(base, 'informes', k + suf))
            print(f"{k:34s} modelo {'OK' if r.returncode == 0 else 'ERROR: ' + r.stderr[-200:]}")
        else:
            print(f"{k:34s} {orden.get(nombre)}: sin informe del modelo (ver ranking.md)")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
