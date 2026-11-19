# -*- coding: utf-8 -*-
"""Une los combos del Bet Builder (bb/res_<clave>.json: probabilidad del modelo + precio REAL de Betano) con la evidencia de la ficha
de cada pata (registro/lineas.csv: X de 10 por equipo, colchón, cumple) y escribe bb/final_<clave>.json con las columnas de evidencia.
    python3 recoleccion/bb_evidencia.py jornadas/AAAA-MM-DD <clave>
Solidez de una pata: 1 si la ficha cumple (ambos equipos >= 7 de 10); 0,6 si ambos >= 6 de 10 y el colchón es positivo; 0 si no (o sin estadística).
Es solo lectura de evidencia: no cambia la probabilidad."""
import csv, json, os, sys

MAP = {'goles': 'goles', 'corners': 'corners', 'tarjetas': 'tarjetas', 'al_arco': 'al_arco', 'remates': 'remates', 'fueras': 'fueras',
       'saques_meta': 'saques_meta', 'faltas': 'faltas', 'saques_banda': 'saques_banda'}


def _n(t):
    t = str(t).split(' de ')[0].strip()
    return int(t) if t.isdigit() else None


def leer(jornada, partido):
    idx = {}
    for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(jornada))), 'registro', 'lineas.csv') if False else 'registro/lineas.csv', encoding='utf-8-sig'), delimiter=';'):
        if r['jornada'] == os.path.basename(jornada.rstrip('/')) and r['partido'] == partido:
            idx[(r['mercado'], r['ambito'], r['linea'], r['lado'], r['jugador'])] = r
    return idx


def pata(idx, sel):
    m = sel['mercado']
    if m in MAP:
        k = (m, sel['ambito'], str(sel['linea']), 'Más' if sel['lado'] == 'mas' else 'Menos', '')
    elif m == 'ambos':
        k = ('ambos', 'total', '', 'Sí' if sel['lado'] == 'si' else 'No', '')
    elif m == 'ambos_n_tarjetas':
        k = ('ambos_n_tarjetas', 'total', str(sel.get('n')), 'Sí' if sel['lado'] == 'si' else 'No', '')
    elif m == 'resultado':
        k = ('resultado', 'total', '', sel['lado'], '')
    else:
        return None
    r = idx.get(k)
    if r is None:
        # prueba con línea sin decimales extra
        for kk, v in idx.items():
            if kk[0] == k[0] and kk[1] == k[1] and kk[3] == k[3] and kk[2] not in ('',) and k[2] not in ('',) and abs(float(kk[2]) - float(k[2])) < 1e-9:
                return v
        return None
    return r


def solidez(r):
    if r is None:
        return 0.0, 'sin fila'
    if r['cumple_ficha'] == 'sí':
        return 1.0, f"{r['reg_local']}/{r['reg_visitante']} ✓"
    a, b = _n(r['reg_local']), _n(r['reg_visitante'])
    try:
        col = float(r['colchon']) if r['colchon'] else None
    except ValueError:
        col = None
    if a is not None and b is not None and a >= 6 and b >= 6 and (col or 0) > 0:
        return 0.6, f"{r['reg_local']}/{r['reg_visitante']} (6+)"
    return 0.0, f"{r['reg_local'] or '–'}/{r['reg_visitante'] or '–'}" + (' (sin stat. por tiempo)' if 'por tiempo' in (r.get('nota') or '') else '')


def correr(jornada, clave):
    res = json.load(open(os.path.join(jornada, 'bb', f'res_{clave}.json'), encoding='utf8'))
    idx = leer(jornada, res['partido'])
    for x in res['candidatos']:
        ss, det = [], []
        for sel in x['sels']:
            s, d = solidez(pata(idx, sel))
            ss.append(s)
            det.append(d)
        x['solidez_patas'] = ss
        x['reg_patas'] = det
        x['solidez'] = round(sum(ss) / len(ss), 2)
        x['n_cumple'] = sum(1 for s in ss if s == 1.0)
    json.dump(res, open(os.path.join(jornada, 'bb', f'final_{clave}.json'), 'w', encoding='utf8'), ensure_ascii=False)
    return res


if __name__ == '__main__':
    r = correr(sys.argv[1], sys.argv[2])
    ok = [x for x in r['candidatos'] if x['cumple']]
    import collections
    print(r['partido'], len(ok), 'cumplen precio; por nº de patas que cumplen la ficha:', sorted(collections.Counter(x['n_cumple'] for x in ok).items()))
