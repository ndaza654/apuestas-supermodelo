# -*- coding: utf-8 -*-
"""Califica de una vez las líneas de JUGADOR que quedaron sin resultado en varias jornadas (24-nov-2026).

    python3 recoleccion/calificar_jugadores_pendientes.py <carpeta> [--calificar]

<carpeta> trae: objetivos.json (clave «jornada|partido» → [n_líneas, clave, mid]), feeds_*.json ({mid: {df_st_1_, df_su_1_}}) y uno o más pj_*.json (lotes de
flashscore_jugadores_en_par.js). Por jornada escribe en jornadas/<j>/resultados/: resultados_jug.json, incidentes_jug.json, mapa_jug.json, mids_jug.json y
jugadores_resultado_pendientes.txt; con --calificar corre calificar_jugadores.py sobre ese .txt. Partidos sin tabla en el lote quedan sin calificar (se listan)."""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import resultados_flashscore as RF, jugadores_resultado_en as JE, calificar_jugadores as CJ

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ajustes(j, txt, d):
    """Cruza la tabla de jugadores con los totales del equipo (df_st): si la tabla no trae remates (Cluj–Otelul: 0 de 30) esas líneas quedan SIN calificar;
    si la tabla suma bastante más que el partido (prórroga: Betano liquida a los 90 minutos) las líneas «cumplió» llevan una nota."""
    import csv
    res = json.load(open(os.path.join(d, 'resultados_jug.json'), encoding='utf8')); mapa = json.load(open(os.path.join(d, 'mapa_jug.json'), encoding='utf8'))
    inv = {v: k for k, v in mapa.items()}
    P, T = CJ.leer(txt)
    anular, inflado = {}, set()
    for p, pl in P.items():
        r = res.get(inv.get(p))
        if not r:
            continue
        rem, arc, fal = sum(v[2] for v in pl.values()), sum(v[3] for v in pl.values()), sum(v[6] for v in pl.values())
        real_rem, real_fal = sum(r.get('sh', [0, 0])), sum(r.get('f', [0, 0]))
        if rem == 0 and real_rem > 0:
            anular[p] = {'remates', 'al_arco'}
        elif fal == 0 and real_fal > 0:
            anular[p] = {'faltas'}
        elif real_rem and rem > real_rem * 1.1 or real_fal and fal > real_fal * 1.1:
            inflado.add(p)
    if not anular and not inflado:
        return
    rc = os.path.join(RAIZ, 'registro', 'lineas.csv')
    f = open(rc, encoding='utf-8-sig', newline=''); rd = csv.DictReader(f, delimiter=';'); campos, filas = rd.fieldnames, list(rd); f.close()
    na = ni = 0
    for r in filas:
        if r['jornada'] != j or not r['mercado'].startswith('jugador:'):
            continue
        m = r['mercado'].split(':', 1)[1]
        if r['partido'] in anular and m in anular[r['partido']]:
            r['resultado'] = ''; r['nota'] = (r['nota'] + ' · ' if r['nota'] else '') + 'sin calificar: la tabla de Flashscore no trae esta estadística en este partido'; na += 1
        elif r['partido'] in inflado and r['resultado'] == 'cumplió' and m in ('remates', 'al_arco', 'faltas', 'entradas') and 'prórroga' not in r['nota']:
            r['nota'] += ' · la tabla incluye prórroga (puede estar inflada)'; ni += 1
    f = open(rc, 'w', encoding='utf-8-sig', newline=''); w = csv.DictWriter(f, fieldnames=campos, delimiter=';'); w.writeheader(); w.writerows(filas); f.close()
    print(f'  ajustes {j}: {na} líneas devueltas a «sin calificar» (tabla sin remates: {sorted(anular)}), {ni} «cumplió» marcadas con aviso de prórroga ({sorted(inflado)})')


def main(carpeta, calificar=False):
    obj = json.load(open(os.path.join(carpeta, 'objetivos.json'), encoding='utf8'))
    feeds = {}
    for f in glob.glob(os.path.join(carpeta, 'feeds_*.json')):
        feeds.update(json.load(open(f, encoding='utf8')))
    pj = {}
    for f in sorted(glob.glob(os.path.join(carpeta, 'pj_*.json'))):
        pj.update(json.load(open(f, encoding='utf8'))['pj'])
    lote = os.path.join(carpeta, 'lote_unido.json')
    json.dump({'pj': pj}, open(lote, 'w', encoding='utf8'))
    por_j = {}
    for k, (n, clave, mid) in obj.items():
        j, partido = k.split('|', 1)
        por_j.setdefault(j, {})[clave] = (partido, mid)
    resumen = []
    for j, cs in sorted(por_j.items()):
        d = os.path.join(RAIZ, 'jornadas', j, 'resultados'); os.makedirs(d, exist_ok=True)
        crudo = {c: feeds[m] for c, (p, m) in cs.items() if m in feeds and 'df_su_1_' in feeds[m]}
        cp = os.path.join(d, 'crudo_jug.json'); json.dump(crudo, open(cp, 'w', encoding='utf8'), ensure_ascii=False)
        RF.main(cp, os.path.join(d, 'resultados_jug.json'), os.path.join(d, 'incidentes_jug.json'))
        os.remove(cp)
        json.dump({c: p for c, (p, m) in cs.items()}, open(os.path.join(d, 'mapa_jug.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        json.dump({c: m for c, (p, m) in cs.items()}, open(os.path.join(d, 'mids_jug.json'), 'w', encoding='utf8'), indent=1)
        sal = os.path.join(d, 'jugadores_resultado_pendientes.txt')
        JE.main(lote, os.path.join(d, 'incidentes_jug.json'), os.path.join(d, 'mapa_jug.json'), os.path.join(d, 'mids_jug.json'), sal, 'balance 24-nov')
        sin_tabla = [p for c, (p, m) in cs.items() if m not in pj]
        resumen.append((j, len(cs) - len(sin_tabla), sin_tabla))
        if calificar and len(cs) - len(sin_tabla):
            CJ.main(j, sal)
            ajustes(j, sal, d)
    for j, n, s in resumen:
        print(f'{j}: {n} partidos con tabla; sin tabla: {len(s)}' + (' → ' + '; '.join(x[:38] for x in s) if s else ''))


if __name__ == '__main__':
    main(sys.argv[1], '--calificar' in sys.argv)
