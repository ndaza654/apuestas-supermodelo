"""
backtest_estrategia.py
======================
Mide el % de acierto de la estrategia "7 de 10" (filtro de regularidad)
en las 5 grandes ligas de Europa + Brasil.

Ligas incluidas:
  E0 = Premier League (Inglaterra)
  SP1 = La Liga (España)
  D1  = Bundesliga (Alemania)
  I1  = Serie A (Italia)
  F1  = Ligue 1 (Francia)
  BRA = Brasileirao

Mercados evaluados (binarios: Más / Menos o sí/no):
  - Goles totales: >1.5, >2.5, >3.5
  - Córners totales: >8.5, >9.5, >10.5
  - Remates totales: >20, >25
  - Tiros al arco totales: >8, >10
  - Faltas totales: >20, >24
  - Tarjetas en puntos (AM=1, AR=2): >2, >3, >4

Para cada línea y cada partido con historial ≥7 de los últimos 10:
  - cumple_local: local tuvo ≥7 de 10 partidos anteriores por encima del umbral
  - cumple_visita: visitante igual
  - Según combinación (ambos / solo local / solo visita / ninguno) → bucket

Salida: val/backtest_estrategia.json + val/backtest_estrategia.html
"""
import csv, json, math, os
from collections import defaultdict
from datetime import datetime

LIGAS = {'E0','SP1','D1','I1','F1','BRA'}
N = 10          # ventana
MIN_N = 7       # mínimo para "cumple"
UMBRAL_CUMPLE = 7  # de N

LINEAS = {
    'goles_1.5':  ('FTHome','FTAway', 1.5, True),
    'goles_2.5':  ('FTHome','FTAway', 2.5, True),
    'goles_3.5':  ('FTHome','FTAway', 3.5, True),
    'corners_8.5':('HomeCorners','AwayCorners', 8.5, True),
    'corners_9.5':('HomeCorners','AwayCorners', 9.5, True),
    'corners_10.5':('HomeCorners','AwayCorners',10.5, True),
    'remates_20': ('HomeShots','AwayShots', 20, True),
    'remates_25': ('HomeShots','AwayShots', 25, True),
    'arco_8':     ('HomeTarget','AwayTarget', 8, True),
    'arco_10':    ('HomeTarget','AwayTarget',10, True),
    'faltas_20':  ('HomeFouls','AwayFouls', 20, True),
    'faltas_24':  ('HomeFouls','AwayFouls', 24, True),
    'tarj_2':     ('HomeYellow','AwayYellow', 2, True, 'HomeRed','AwayRed'),
    'tarj_3':     ('HomeYellow','AwayYellow', 3, True, 'HomeRed','AwayRed'),
    'tarj_4':     ('HomeYellow','AwayYellow', 4, True, 'HomeRed','AwayRed'),
}

def val(row, cols):
    """Suma de columnas; None si alguna vacía."""
    total = 0
    for c in cols:
        v = row.get(c,'').strip()
        if v == '': return None
        total += float(v)
    return total

def parse_date(s):
    for fmt in ('%d/%m/%Y','%Y-%m-%d','%m/%d/%Y','%d/%m/%y'):
        try: return datetime.strptime(s.strip(), fmt)
        except: pass
    return None

def run():
    path = os.path.join(os.path.dirname(__file__), 'data/Matches.csv')
    rows = []
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r['Division'] not in LIGAS: continue
            d = parse_date(r['MatchDate'])
            if d is None: continue
            r['_date'] = d
            rows.append(r)
    rows.sort(key=lambda r:(r['Division'], r['_date']))

    # historial por equipo (en su liga)
    # hist[liga][equipo] = lista de dicts {date, stat_key: val, ...}
    hist = defaultdict(lambda: defaultdict(list))

    # resultados por linea: {linea: {bucket: [0/1, ...]}}
    res = defaultdict(lambda: defaultdict(list))
    res_liga = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    stat_keys = set()
    for lname,(c1,c2,_,_,*extra) in LINEAS.items():
        stat_keys.add((c1,c2))
        if extra: stat_keys.add((extra[0],extra[1]))

    for row in rows:
        liga = row['Division']
        home = row['HomeTeam']
        away = row['AwayTeam']
        date = row['_date']

        h_hist = hist[liga][home][-N:]
        a_hist = hist[liga][away][-N:]

        # evaluar cada línea
        for lname, spec in LINEAS.items():
            c1,c2,thresh,_mas = spec[:4]
            extra = spec[4:] if len(spec)>4 else []

            # valor real del partido
            if extra:
                # tarjetas en puntos
                am = val(row,[c1,c2])
                ar = val(row,[extra[0],extra[1]])
                if am is None or ar is None: continue
                real = am + ar*2
            else:
                real = val(row,[c1,c2])
                if real is None: continue

            acierto = int(real > thresh)

            # historial de cada equipo
            def hist_rate(team_hist, stat_c1, stat_c2, thresh, extra_cols=None):
                vals = []
                for h in team_hist[-N:]:
                    if extra_cols:
                        v1 = h.get(stat_c1)
                        v2 = h.get(stat_c2)
                        ve1 = h.get(extra_cols[0])
                        ve2 = h.get(extra_cols[1])
                        if v1 is None or v2 is None or ve1 is None or ve2 is None: continue
                        vals.append(v1+v2+ve1*2+ve2*2)
                    else:
                        v1 = h.get(stat_c1)
                        v2 = h.get(stat_c2)
                        if v1 is None or v2 is None: continue
                        vals.append(v1+v2)
                n_data = len(vals)
                if n_data < MIN_N: return None, n_data
                n_sobre = sum(1 for v in vals if v > thresh)
                return n_sobre, n_data

            if extra:
                n_h, nd_h = hist_rate(h_hist, c1, c2, thresh, extra)
                n_a, nd_a = hist_rate(a_hist, c1, c2, thresh, extra)
            else:
                n_h, nd_h = hist_rate(h_hist, c1, c2, thresh)
                n_a, nd_a = hist_rate(a_hist, c1, c2, thresh)

            cumple_h = (n_h is not None and n_h >= UMBRAL_CUMPLE)
            cumple_a = (n_a is not None and n_a >= UMBRAL_CUMPLE)

            if n_h is None and n_a is None: continue  # sin historial

            if cumple_h and cumple_a:
                bucket = 'ambos'
            elif cumple_h:
                bucket = 'solo_local'
            elif cumple_a:
                bucket = 'solo_visita'
            else:
                bucket = 'ninguno'

            res[lname][bucket].append(acierto)
            res_liga[liga][lname][bucket].append(acierto)

        # actualizar historial (solo después de evaluar)
        def add_hist(team, rol):
            entry = {'date': date.isoformat()}
            # cols del equipo como local o visita
            if rol == 'home':
                pairs = [(c1,c2) for c1,c2 in [
                    ('FTHome','FTAway'),('HomeCorners','AwayCorners'),
                    ('HomeShots','AwayShots'),('HomeTarget','AwayTarget'),
                    ('HomeFouls','AwayFouls'),('HomeYellow','AwayYellow'),('HomeRed','AwayRed')
                ]]
                prefix_own = 'Home'; prefix_opp = 'Away'
            else:
                pairs = [(c1,c2) for c1,c2 in [
                    ('FTAway','FTHome'),('AwayCorners','HomeCorners'),
                    ('AwayShots','HomeShots'),('AwayTarget','HomeTarget'),
                    ('AwayFouls','HomeFouls'),('AwayYellow','HomeYellow'),('AwayRed','HomeRed')
                ]]
                prefix_own = 'Away'; prefix_opp = 'Home'
            # guardar totales del partido por columna
            for col in ['FTHome','FTAway','HomeCorners','AwayCorners',
                        'HomeShots','AwayShots','HomeTarget','AwayTarget',
                        'HomeFouls','AwayFouls','HomeYellow','AwayYellow','HomeRed','AwayRed']:
                v = row.get(col,'').strip()
                entry[col] = float(v) if v else None
            hist[liga][team].append(entry)

        add_hist(home, 'home')
        add_hist(away, 'away')

    # construir resumen
    summary = {}
    buckets = ['ambos','solo_local','solo_visita','ninguno']

    for lname in sorted(res):
        summary[lname] = {}
        for b in buckets:
            vals = res[lname][b]
            n = len(vals)
            if n == 0:
                summary[lname][b] = {'n':0,'acierto_pct':None}
            else:
                pct = round(100*sum(vals)/n, 1)
                summary[lname][b] = {'n':n,'acierto_pct':pct}

    # por liga
    by_liga = {}
    for liga in sorted(res_liga):
        by_liga[liga] = {}
        for lname in sorted(res_liga[liga]):
            by_liga[liga][lname] = {}
            for b in buckets:
                vals = res_liga[liga][lname][b]
                n = len(vals)
                if n == 0:
                    by_liga[liga][lname][b] = {'n':0,'acierto_pct':None}
                else:
                    pct = round(100*sum(vals)/n, 1)
                    by_liga[liga][lname][b] = {'n':n,'acierto_pct':pct}

    out = {'resumen': summary, 'por_liga': by_liga,
           'config': {'N':N,'MIN_N':MIN_N,'UMBRAL_CUMPLE':UMBRAL_CUMPLE,
                      'ligas': sorted(LIGAS)}}
    os.makedirs('val', exist_ok=True)
    with open('val/backtest_estrategia.json','w') as f:
        json.dump(out, f, indent=2)
    print("OK → val/backtest_estrategia.json")
    return out

if __name__ == '__main__':
    out = run()
    # preview rápido
    print(f"\n{'Línea':15} {'Ambos':>10} {'SoloLocal':>10} {'SoloVisita':>10} {'Ninguno':>10}")
    print('-'*57)
    for lname, bkts in out['resumen'].items():
        def fmt(b):
            d=bkts[b]
            return f"{d['acierto_pct']:5.1f}%({d['n']:5d})" if d['n'] else "    -    "
        print(f"{lname:15} {fmt('ambos'):>10} {fmt('solo_local'):>10} {fmt('solo_visita'):>10} {fmt('ninguno'):>10}")
