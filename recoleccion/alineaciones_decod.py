# -*- coding: utf-8 -*-
"""Pasa el texto compacto de alineaciones (lo emite `__luenc` en el navegador; ver flashscore_alineaciones.js) al JSON que lee armar_entrada.lineups_de().
Uso: python3 recoleccion/alineaciones_decod.py jornadas/AAAA-MM-DD   (lee raw/lu_<clave>.txt → alineaciones/<clave>.json)
Texto: M|mid|tipo|lectura_UTC (tipo «null» = Flashscore no publicó la pestaña) · P|L/V|pid|nombre|dorsal|1 si arquero · B|L/V|pid|nombre|motivo.
Salida: probables.L/V = [nombre, dorsal, pid, gk] · bajas.L/V = [nombre, pid, motivo] (L = local del partido)."""
import sys, os, glob, json


def decod(texto):
    c = {'mid': None, 'tipo': None, 'lectura_utc': None, 'probables': {'L': [], 'V': []}, 'bajas': {'L': [], 'V': []}}
    for ln in texto.split('\n'):
        p = ln.split('|')
        if p[0] == 'M':
            c['mid'], c['tipo'], c['lectura_utc'] = p[1], (None if p[2] == 'null' else p[2]), p[3]
        elif p[0] == 'P':
            c['probables'][p[1]].append([p[3], p[4], p[2], int(p[5])])
        elif p[0] == 'B':
            c['bajas'][p[1]].append([p[3], p[2], p[4] if len(p) > 4 else ''])
    if not c['tipo'] or not c['probables']['L']:
        c = {'mid': c['mid'], 'sin_pestana': True, 'lectura_utc': c['lectura_utc'], 'probables': {'L': [], 'V': []}, 'bajas': {'L': [], 'V': []}}
    else:
        c['nota'] = 'Alineaciones oficiales esperadas 1 hora antes del inicio del partido.'
    return c


if __name__ == '__main__':
    jor = sys.argv[1]
    os.makedirs(os.path.join(jor, 'alineaciones'), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(jor, 'raw', 'lu_*.txt'))):
        clave = os.path.basename(f)[3:-4]
        c = decod(open(f, encoding='utf8').read().rstrip('\n'))
        json.dump(c, open(os.path.join(jor, 'alineaciones', clave + '.json'), 'w', encoding='utf8'), ensure_ascii=False)
        print(clave, 'SIN PESTAÑA' if c.get('sin_pestana') else f"{len(c['probables']['L'])}+{len(c['probables']['V'])} XI · bajas {len(c['bajas']['L'])}+{len(c['bajas']['V'])}")
