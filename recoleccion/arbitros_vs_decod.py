#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ValueStats (recoleccion/arbitros_valuestats.js) → jornadas/AAAA-MM-DD/arbitros/<clave>.json (el formato que lee armar_entrada.arbitro_de).
Entrada: JSON descargado del navegador {<clave corta>: {arbitro, pais, vs, vs_nombre, pj_vs, otros, temporada, faq, leido, nota?, error?}}  (clave corta = primeros 12 caracteres de la clave del partido)
Uso: python3 recoleccion/arbitros_vs_decod.py jornadas/AAAA-MM-DD <entrada.json>
Totales del historial: se suman las filas de temporada (temporada, partidos, amarillas, rojas, faltas) del texto «Statistics by Season».
Sin muestra en ValueStats (error) → archivo con `error` y sin cifras: el análisis lo declara, no lo inventa."""
import sys, os, re, json, glob
from datetime import datetime, timedelta


def main(dia, ent):
    D = json.load(open(ent, encoding='utf-8'))
    claves = sorted({os.path.basename(f)[:-5] for c in ('flashscore', 'sofascore', 'betano') for f in glob.glob(os.path.join(dia, c, '*.json')) if not os.path.basename(f).startswith(('jugadores', 'contraste'))})   # Sofascore es la fuente principal desde el 25-nov
    os.makedirs(os.path.join(dia, 'arbitros'), exist_ok=True)
    n = 0
    for c in sorted(claves):
        r = D.get(c) or D.get(c[:12])
        if not r:
            continue
        leido = ''
        if r.get('leido'):
            t = datetime.fromisoformat(r['leido'].replace('Z', '+00:00')) - timedelta(hours=5)
            leido = t.strftime('%Y-%m-%d ~%H:%M Bogotá')
        o = {'arbitro': r.get('arbitro'), 'fuente': 'ValueStats ' + (r.get('vs') or 'sin página'), 'leido': leido}
        if r.get('error'):
            o['error'] = r['error']
        else:
            tx = r.get('temporada') or ''
            m = re.search(r'Total Matches:\s*(\d+)', tx)
            seas = re.findall(r'(?<![\d/])(20\d\d(?:/20\d\d)?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)(?!\d)', tx)
            pm = sum(int(s[1]) for s in seas); am = sum(int(s[2]) for s in seas); ro = sum(int(s[3]) for s in seas)
            o['partidos_registrados'] = int(m.group(1)) if m else (pm or None)
            if pm:
                o['amarillas_pp_total'] = round(am / pm, 2); o['rojas_pp_total'] = round(ro / pm, 2)
            f = r.get('faq') or ''
            mm = re.search(r'Sample of (\d+) matches', f)
            o['muestra_n'] = int(mm.group(1)) if mm else None
            o['faq_texto'] = f
            o['por_temporada_texto'] = tx
            o['vs_nombre'] = r.get('vs_nombre'); o['pj_vs'] = r.get('pj_vs')
            if r.get('otros'):
                o['otros_candidatos'] = r['otros']
            if r.get('nota'):
                o['nota'] = r['nota']
        json.dump(o, open(os.path.join(dia, 'arbitros', c + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        n += 1
    print(n, 'árbitros escritos')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
