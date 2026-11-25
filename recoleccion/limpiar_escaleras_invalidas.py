# -*- coding: utf-8 -*-
"""Limpia lo ya guardado de las jornadas afectadas por el error de las tablas de jugadores de Betano (22 al 26-nov-2026).
Betano entrega los mercados de jugador como UNA tabla con todos los jugadores a nombre del primero; el extractor viejo pegaba las ~39 escaleras en un solo jugador y
`betano.py` se quedaba con la última cuota de cada línea (p. ej. «Julián Álvarez · Remates 1+ @3,20»: esa línea no existe en Betano).
Para cada jornada: busca en raw/bet_*.txt las escaleras con líneas repetidas (la huella del error) y
  1) las quita de betano/<clave>.json,
  2) quita esas filas de registro/lineas.csv y las guarda en registro/lineas_invalidas.csv (con el motivo) — no se borra nada sin dejar copia,
  3) avisa si alguna estaba en registro/sugerencias.csv o marcada como apostada.
Uso: python3 recoleccion/limpiar_escaleras_invalidas.py 2026-11-22 [2026-11-23 ...]      (no toca las demás filas ni los resultados)"""
import sys, os, glob, csv, json, io

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
STAT = {'as': 'asiste', 'sh': 'remates', 'sot': 'al_arco', 'tk': 'entradas', 'fc': 'faltas', 'sv': 'atajadas'}
MOTIVO = 'cuota inválida: tabla de jugadores de Betano mal leída (escaleras de ~39 jugadores pegadas a uno; error corregido el 25-nov-2026)'


def contaminadas(raw_txt):
    """(jugador, stat) de las escaleras con líneas repetidas en un bet_<clave>.txt."""
    out = []
    for ln in open(raw_txt, encoding='utf8'):
        if not ln.startswith('P|'):
            continue
        t = ln.rstrip('\n').split('|')
        for it in t[3:]:
            k, _, v = it.partition('=')
            if k in STAT:
                ks = [int(a.split(':')[0]) for a in v.split(',') if ':' in a]
                if len(ks) != len(set(ks)):
                    out.append((t[1], STAT[k]))
    return out


def main(dias):
    ruta_l = os.path.join(RAIZ, 'registro', 'lineas.csv')
    txt = open(ruta_l, encoding='utf-8-sig', newline='').read()
    rd = csv.DictReader(io.StringIO(txt), delimiter=';')
    cab, filas = rd.fieldnames, list(rd)
    malas = {}                                   # (jornada, partido, jugador, mercado) → clave
    for d in dias:
        for raw in sorted(glob.glob(os.path.join(RAIZ, 'jornadas', d, 'raw', 'bet_*.txt'))):
            k = os.path.basename(raw)[4:-4]
            bj = os.path.join(RAIZ, 'jornadas', d, 'betano', k + '.json')
            if not os.path.exists(bj):
                continue
            B = json.load(open(bj, encoding='utf8'))
            partido = f"{B['meta']['local']} - {B['meta']['visitante']}"
            mal = contaminadas(raw)
            if not mal:
                continue
            ant = len(B['betano']['jugadores'])
            B['betano']['jugadores'] = [j for j in B['betano']['jugadores'] if (j['jugador'], j['stat']) not in set(mal)]
            B['betano']['avisos'] = [f'{p} · {s}: escalera descartada (tabla de jugadores mal leída; limpiado el 25-nov-2026)' for p, s in mal]
            json.dump(B, open(bj, 'w', encoding='utf8'), ensure_ascii=False, indent=0)
            for p, s in mal:
                malas[(d, partido, p, 'jugador:' + s)] = k
            print(f'{d} {k}: {len(mal)} escaleras inválidas, {ant - len(B["betano"]["jugadores"])} entradas quitadas de betano/')
    quitar = [r for r in filas if (r['jornada'], r['partido'], r['jugador'], r['mercado']) in malas]
    mantener = [r for r in filas if (r['jornada'], r['partido'], r['jugador'], r['mercado']) not in malas]
    ruta_i = os.path.join(RAIZ, 'registro', 'lineas_invalidas.csv')
    nuevo = not os.path.exists(ruta_i)
    ya = set()
    if not nuevo:
        ya = {tuple(r.values()) for r in csv.DictReader(open(ruta_i, encoding='utf-8-sig', newline=''), delimiter=';')}
    with open(ruta_i, 'a', encoding='utf-8-sig' if nuevo else 'utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cab + ['motivo'], delimiter=';', extrasaction='ignore')
        if nuevo:
            w.writeheader()
        for r in quitar:
            r = dict(r, motivo=MOTIVO)
            if tuple(r.get(c, '') for c in cab + ['motivo']) not in ya:
                w.writerow(r)
    with open(ruta_l, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cab, delimiter=';', lineterminator='\r\n' if '\r\n' in txt[:5000] else '\n')
        w.writeheader()
        w.writerows(mantener)
    ap = [r for r in quitar if r.get('apostada') or r.get('resultado')]
    print(f'registro/lineas.csv: {len(quitar)} filas inválidas quitadas ({len(ap)} con apostada/resultado) → registro/lineas_invalidas.csv')
    sj = os.path.join(RAIZ, 'registro', 'sugerencias.csv')
    if os.path.exists(sj):
        S = list(csv.DictReader(open(sj, encoding='utf-8-sig', newline=''), delimiter=';'))
        js = {(p, j) for (_, p, j, _) in malas}
        hit = [s for s in S if any(j and j in json.dumps(s, ensure_ascii=False) and p in json.dumps(s, ensure_ascii=False) for p, j in js)]
        print(f'registro/sugerencias.csv: {len(hit)} sugerencias mencionan un jugador contaminado de su partido' + (' → revisar: ' + '; '.join(sorted({h.get("seleccion", h.get("descripcion", ""))[:60] for h in hit})[:6]) if hit else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) if len(sys.argv) > 1 else print(__doc__) or 1)
