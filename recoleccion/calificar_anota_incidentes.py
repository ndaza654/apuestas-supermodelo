# -*- coding: utf-8 -*-
"""Califica las líneas «anota Más 1» de partidos SIN tabla de jugadores en Flashscore, solo con los incidentes (goles, tarjetas, cambios).

    python3 recoleccion/calificar_anota_incidentes.py <jornada> <clave> "<partido de lineas.csv>" <incidentes.json> "<goleador1;goleador2;...>"

  · «cumplió»: el jugador figura entre los goleadores del tiempo reglamentario (lista dada a mano tras leer los incidentes; los penales de la tanda NO cuentan).
  · «falló»: el jugador figura en algún incidente (gol, tarjeta, cambio) = jugó, y no marcó.
  · El resto queda SIN resultado: sin alineación ni tabla no se sabe si jugó (Betano anula si no jugó), no se inventa.
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calificar_jugadores as CJ


def casar_estricto(nombre, plantel):
    """Como casar_flashscore pero exige que la inicial de Flashscore («Rodriguez J.») sea la de un nombre de pila de Betano (James ≠ Nicolás)."""
    c = CJ.casar_flashscore(nombre, plantel)
    if not c:
        return None
    ini = [t for t in CJ.norm(c) if len(t) == 1]
    n = CJ.norm(nombre)
    ap = [t for t in CJ.norm(c) if len(t) > 1]
    pilas = [t for t in n if t not in ap]
    return c if (not ini or any(t[0] == ini[0] for t in pilas)) else None


def main(jornada, clave, partido, inc, goleadores):
    I = json.load(open(inc, encoding='utf-8'))[clave]['eventos']
    jugaron = {e['jugador']: 1 for e in I if e.get('jugador')}
    gol = {g.strip(): 1 for g in goleadores.split(';') if g.strip()}
    rc = os.path.join(CJ.RAIZ, 'registro', 'lineas.csv')
    f = open(rc, encoding='utf-8-sig', newline=''); rd = csv.DictReader(f, delimiter=';')
    campos, filas = rd.fieldnames, list(rd); f.close()
    ok = ko = sin = 0
    for r in filas:
        if r['jornada'] != jornada or r['partido'] != partido or r['mercado'] != 'jugador:anota' or r['resultado']:
            continue
        g = casar_estricto(r['jugador'], gol)
        if g:
            r['resultado'] = 'cumplió'; ok += 1
            r['nota'] = (r['nota'] + ' · ' if r['nota'] else '') + f'marcó ({g}) según incidentes de Flashscore, 19-nov'
            continue
        p = casar_estricto(r['jugador'], jugaron)
        if p:
            r['resultado'] = 'falló'; ko += 1
            r['nota'] = (r['nota'] + ' · ' if r['nota'] else '') + f'jugó ({p} figura en incidentes) y no marcó; sin tabla de jugadores'
        else:
            sin += 1
    f = open(rc, 'w', encoding='utf-8-sig', newline='')
    w = csv.DictWriter(f, fieldnames=campos, delimiter=';'); w.writeheader(); w.writerows(filas); f.close()
    print(f'{partido}: {ok} cumplieron, {ko} fallaron (jugaron), {sin} quedan sin resultado (no se sabe si jugaron)')


if __name__ == '__main__':
    main(*sys.argv[1:6])
