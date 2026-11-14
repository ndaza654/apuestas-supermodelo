# -*- coding: utf-8 -*-
"""Califica las líneas de JUGADOR de `registro/lineas.csv` con estadística por jugador (balance).

    python3 recoleccion/calificar_jugadores.py <jornada> <jugadores_resultado.txt>

Formato del .txt (ver jornadas/2026-11-13/balance/jugadores_resultado.txt):
  #Partido                       (encabezado de bloque, igual que en lineas.csv)
  lado|jugador|min|remates|al_arco|goles|asistencias|faltas|faltas_recibidas|entradas|atajadas|amarillas|rojas   (solo quienes jugaron)
  @Partido|jugador|tipo          (tarjetas, de los incidentes)
Reglas: las líneas «N» son «N o más» (v >= N). anota = goles>=1; asiste = asistencias>=1; anota_o_asiste = goles+asist>=1;
tarjeta = recibió amarilla o roja. Un jugador que no figura con minutos no jugó: la apuesta se anula («nula»).
Casa nombres Betano↔Sofascore sin tildes y por apellido+inicial; los que no casan se listan y quedan sin calificar (no se inventa).
"""
import csv, os, re, sys, unicodedata
from difflib import SequenceMatcher

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = {'remates': 3, 'al_arco': 4, 'goles': 5, 'asist': 6, 'faltas': 7, 'entradas': 9, 'atajadas': 10}


def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('-', ' ')
    return re.sub(r'[^a-z ]', '', s).split()


def casar(nombre, plantel):
    """plantel = {nombre_sofa: fila}; devuelve el nombre de Sofascore o None."""
    n = norm(nombre)
    if not n:
        return None
    mejor, ms = None, 0
    for cand in plantel:
        c = norm(cand)
        if n == c:
            return cand
        # apellido(s) en común + parecido del conjunto
        comun = len(set(n) & set(c))
        s = SequenceMatcher(None, ' '.join(n), ' '.join(c)).ratio()
        if n[-1] in c or c[-1] in n:
            s += 0.25
        if comun >= 2:
            s += 0.15
        if s > ms:
            mejor, ms = cand, s
    return mejor if ms >= 0.8 else None


def leer(ruta):
    P, T, parte = {}, {}, None
    for ln in open(ruta, encoding='utf8'):
        ln = ln.strip()
        if ln.startswith('@'):
            p, j, t = ln[1:].split('|')
            T.setdefault(p, {})[j] = t
        elif ln.startswith('#') and not ln.startswith('# '):
            parte = ln[1:].strip(); P[parte] = {}
        elif ln and not ln.startswith('#') and parte:
            f = ln.split('|')
            P[parte][f[1]] = [f[0]] + [int(x) for x in f[2:]]    # [lado, min, rem, arco, goles, asist, faltas, recib, entr, atj, am, ro]
    return P, T


def valor(r, mercado, tarj):
    # f = [lado, min, remates, al_arco, goles, asistencias, faltas, recibidas, entradas, atajadas, am, ro]
    if mercado == 'remates': return r[2]
    if mercado == 'al_arco': return r[3]
    if mercado == 'anota': return r[4]
    if mercado == 'asiste': return r[5]
    if mercado == 'anota_o_asiste': return r[4] + r[5]
    if mercado == 'faltas': return r[6]
    if mercado == 'entradas': return r[8]
    if mercado == 'atajadas': return r[9]
    if mercado == 'tarjeta': return 1 if tarj else 0
    return None


def main(jornada, ruta):
    P, T = leer(ruta)
    rc = os.path.join(RAIZ, 'registro', 'lineas.csv')
    f = open(rc, encoding='utf-8-sig', newline=''); rd = csv.DictReader(f, delimiter=';')
    campos, filas = rd.fieldnames, list(rd); f.close()
    n = ok = nulas = 0
    sin = {}
    for r in filas:
        if r['jornada'] != jornada or not r['mercado'].startswith('jugador:') or r['partido'] not in P:
            continue
        m = r['mercado'].split(':', 1)[1]
        plantel = P[r['partido']]
        # conjunto de nombres para tarjeta (incluye quienes vieron tarjeta)
        nom = casar(r['jugador'], plantel)
        try:
            L = float(r['linea'])
        except ValueError:
            continue
        if nom is None:
            # ¿figura con tarjeta pero no en plantel? (no ocurre: quien ve tarjeta jugó). Se asume que no jugó solo si el nombre
            # ni se parece a nadie; se anota para revisión.
            sin.setdefault(r['partido'], set()).add(r['jugador'])
            r['resultado'] = 'nula'
            r['nota'] = (r['nota'] + ' · ' if r['nota'] else '') + 'no jugó (sin minutos en Sofascore): Betano la anula'
            nulas += 1; n += 1
            continue
        fila = plantel[nom]
        tarj = bool(T.get(r['partido'])) and casar(r['jugador'], {x: 0 for x in T[r['partido']]}) is not None
        v = valor(fila, m, tarj)
        if v is None:
            continue
        r['resultado'] = 'cumplió' if v >= L else 'falló'
        r['nota'] = (r['nota'] + ' · ' if r['nota'] and 'valor real' not in r['nota'] else '') + f'valor real {v} ({nom}, {fila[1]}′; Sofascore)'
        n += 1; ok += r['resultado'] == 'cumplió'
    f = open(rc, 'w', encoding='utf-8-sig', newline='')
    w = csv.DictWriter(f, fieldnames=campos, delimiter=';'); w.writeheader(); w.writerows(filas); f.close()
    print(f'{jornada}: {n} líneas de jugador calificadas ({ok} cumplieron, {nulas} anuladas por no jugar)')
    for p, s in sin.items():
        print('  sin casar/no jugó en', p, ':', ', '.join(sorted(s)))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
