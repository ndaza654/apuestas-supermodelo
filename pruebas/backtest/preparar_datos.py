"""CSV de football-data (copia xgabora) -> datos.json compacto para el motor del backtest.
Uso: python3 -I pruebas/backtest/preparar_datos.py pruebas/calibracion/data/Matches.csv pruebas/backtest/datos.json
Ligas: las 5 grandes + Brasil. Un carácter por valor (código 35 + valor; '!' = sin dato); cuotas x100 (0 = sin dato)."""
import csv, json, sys, datetime

LIGAS = [('E0', 'Premier League'), ('SP1', 'La Liga'), ('D1', 'Bundesliga'), ('I1', 'Serie A'), ('F1', 'Ligue 1'), ('BRA', 'Brasileirão')]
COLS = {'gH': 'FTHome', 'gA': 'FTAway', 'cH': 'HomeCorners', 'cA': 'AwayCorners', 'rH': 'HomeShots', 'rA': 'AwayShots',
        'tH': 'HomeTarget', 'tA': 'AwayTarget', 'fH': 'HomeFouls', 'fA': 'AwayFouls', 'yH': 'HomeYellow', 'yA': 'AwayYellow',
        'xH': 'HomeRed', 'xA': 'AwayRed'}
ODDS = {'oh': 'OddHome', 'od': 'OddDraw', 'oa': 'OddAway', 'o25': 'Over25', 'u25': 'Under25'}

def num(s):
    s = (s or '').strip()
    try:
        return float(s) if s else None
    except ValueError:
        return None

def main(src, dst):
    idx = {c: i for i, (c, _) in enumerate(LIGAS)}
    filas = []
    with open(src, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r['Division'] not in idx:
                continue
            try:
                d = datetime.date.fromisoformat(r['MatchDate'].strip())
            except ValueError:
                continue
            if num(r['FTHome']) is None or num(r['FTAway']) is None:
                continue
            filas.append((d.toordinal() - datetime.date(1970, 1, 1).toordinal(), idx[r['Division']], r['HomeTeam'].strip(), r['AwayTeam'].strip(), r))
    filas.sort(key=lambda x: (x[0], x[1], x[2]))
    equipos, eid = [], {}
    def tid(n):
        if n not in eid:
            eid[n] = len(equipos); equipos.append(n)
        return eid[n]
    def car(v):
        return '!' if v is None or v < 0 else chr(35 + min(int(round(v)), 90))
    out = {'n': len(filas), 'ligas': [n for _, n in LIGAS], 'lg': '', 'dfecha': [], 'h': [], 'a': [],
           'stats': {k: [] for k in COLS}, 'odds': {k: [] for k in ODDS}}
    prev, lg = 0, []
    for d, l, hn, an, r in filas:
        out['dfecha'].append(d - prev); prev = d
        lg.append(str(l)); out['h'].append(tid(hn)); out['a'].append(tid(an))
        for k, c in COLS.items():
            out['stats'][k].append(car(num(r[c])))
        for k, c in ODDS.items():
            v = num(r[c]); out['odds'][k].append(int(round(v * 100)) if v and v > 1 else 0)
    out['lg'] = ''.join(lg)
    out['stats'] = {k: ''.join(v) for k, v in out['stats'].items()}
    out['equipos'] = equipos
    out['fuente'] = 'football-data.co.uk (copia xgabora/Club-Football-Match-Data-2000-2025, data/Matches.csv)'
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(json.dumps(out, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
    print(len(filas), 'partidos,', len(equipos), 'equipos ->', dst)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
