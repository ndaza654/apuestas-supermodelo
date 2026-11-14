# Auditoría · bloque A: ¿hay ventaja? Líneas calificadas de registro/lineas.csv (12-noche y 13-nov). Solo lectura.
import csv, collections, math, random
import numpy as np
import os
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
rng = np.random.default_rng(7)
R = list(csv.DictReader(open(RAIZ + '/registro/lineas.csv', encoding='utf-8-sig'), delimiter=';'))


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


G = [r for r in R if r['resultado'] in ('cumplió', 'falló')]
for r in G:
    r['y'] = 1.0 if r['resultado'] == 'cumplió' else 0.0
    r['c'], r['p'], r['pm'], r['ps'] = f(r['cuota']), f(r['p_modelo']), f(r['p_mercado']), f(r['p_simulacion'])
    r['k'] = (r['jornada'], r['partido'])
    r['eq'] = not r['mercado'].startswith('jugador')
print('calificadas (cumplió/falló):', len(G), '· otras:', collections.Counter(r['resultado'] for r in R if r['resultado'] not in ('cumplió', 'falló', '')))
E = [r for r in G if r['eq'] and r['p'] is not None and r['c']]
Jg = [r for r in G if not r['eq'] and r['c']]
print('equipo con p y cuota:', len(E), '· partidos:', len({r['k'] for r in E}), '· jugador:', len(Jg), '· partidos jugador:', len({r['k'] for r in Jg}))
print('líneas por partido (equipo):', sorted(collections.Counter(r['k'] for r in E).values()))
print('partidos:', sorted({r['k'] for r in E}))


def boot(rows, stat, B=4000):
    """IC 95 % remuestreando PARTIDOS (las líneas del mismo partido no son independientes)."""
    ks = sorted({r['k'] for r in rows})
    by = collections.defaultdict(list)
    for r in rows:
        by[r['k']].append(r)
    out = []
    for _ in range(B):
        samp = []
        for i in rng.integers(0, len(ks), len(ks)):
            samp += by[ks[i]]
        v = stat(samp)
        if v is not None:
            out.append(v)
    return (np.percentile(out, 2.5), np.percentile(out, 97.5)) if out else (float('nan'), float('nan'))


roi = lambda rows: (sum((r['c'] - 1) if r['y'] else -1 for r in rows) / len(rows)) if rows else None
gap = lambda rows: (sum(r['y'] - r['p'] for r in rows) / len(rows)) if rows else None
gapm = lambda rows: (sum(r['y'] - r['pm'] for r in rows if r['pm'] is not None) / max(1, sum(1 for r in rows if r['pm'] is not None))) if rows else None


def fila(t, rows, extra=''):
    if not rows:
        print(f'{t:44s} n=0')
        return
    lo, hi = boot(rows, roi)
    glo, ghi = boot(rows, gap)
    print(f"{t:44s} n={len(rows):4d} part={len({r['k'] for r in rows}):2d} real={np.mean([r['y'] for r in rows]):5.1%} p={np.mean([r['p'] for r in rows]):5.1%} "
          f"real−p={gap(rows):+6.1%} [{glo:+.1%},{ghi:+.1%}]  ROI={roi(rows):+6.1%} [{lo:+.0%},{hi:+.0%}] {extra}")


print('\n== 1. ROI a 1 u por línea (IC 95 % por partidos)')
fila('todas las líneas de equipo', E)
fila('cumple sí', [r for r in E if r['cumple_ficha'] == 'sí'])
fila('cumple no', [r for r in E if r['cumple_ficha'] == 'no'])
fila('sin ficha (1T/2T)', [r for r in E if r['cumple_ficha'] not in ('sí', 'no')])
for lado in ('Más', 'Menos'):
    fila('lado ' + lado, [r for r in E if r['lado'] == lado])
    fila('  cumple sí · ' + lado, [r for r in E if r['lado'] == lado and r['cumple_ficha'] == 'sí'])
for m in sorted({r['mercado'] for r in E}):
    fila('mercado ' + m, [r for r in E if r['mercado'] == m])
    fila('  cumple sí · ' + m, [r for r in E if r['mercado'] == m and r['cumple_ficha'] == 'sí'])
fila('EV modelo > 0', [r for r in E if f(r['ev_modelo']) is not None and f(r['ev_modelo']) > 0])
fila('EV modelo > 0 y cumple sí', [r for r in E if f(r['ev_modelo']) is not None and f(r['ev_modelo']) > 0 and r['cumple_ficha'] == 'sí'])
fila('alerta del modelo', [r for r in E if r['alerta_modelo']])
print('\n== 2. ¿El modelo aporta algo sobre el precio? (líneas con p y p_mercado)')
M = [r for r in E if r['pm'] is not None]
d = np.array([r['p'] - r['pm'] for r in M]); y = np.array([r['y'] for r in M]); p = np.array([r['p'] for r in M]); pm = np.array([r['pm'] for r in M]); ps = np.array([r['ps'] if r['ps'] is not None else np.nan for r in M])
print(f'n={len(M)} · |p−pm| media {np.abs(d).mean():.4f} · mediana {np.median(np.abs(d)):.4f} · p90 {np.percentile(np.abs(d), 90):.4f} · corr(p,pm) {np.corrcoef(p, pm)[0, 1]:.4f} · líneas con |p−pm|≥0,03: {(np.abs(d) >= .03).sum()} ({(np.abs(d) >= .03).mean():.1%})')
brier = lambda q, yy: float(np.mean((q - yy) ** 2))
ll = lambda q, yy: float(-np.mean(yy * np.log(np.clip(q, 1e-6, 1)) + (1 - yy) * np.log(np.clip(1 - q, 1e-6, 1))))
print(f'Brier  modelo {brier(p, y):.5f} · mercado {brier(pm, y):.5f} · simulación {brier(ps[~np.isnan(ps)], y[~np.isnan(ps)]):.5f} (n sim {int((~np.isnan(ps)).sum())}) · constante 0,5: {brier(np.full_like(y, .5), y):.5f}')
print(f'LogLoss modelo {ll(p, y):.5f} · mercado {ll(pm, y):.5f} · simulación {ll(ps[~np.isnan(ps)], y[~np.isnan(ps)]):.5f}')
lo, hi = boot(M, lambda rows: float(np.mean([(r['p'] - r['y']) ** 2 - (r['pm'] - r['y']) ** 2 for r in rows])))
print(f'Brier(modelo) − Brier(mercado) = {brier(p, y) - brier(pm, y):+.5f}  IC95 por partidos [{lo:+.5f}, {hi:+.5f}]  (negativo = el modelo mejora al mercado)')
lo, hi = boot([r for r in M if r['ps'] is not None], lambda rows: float(np.mean([(r['ps'] - r['y']) ** 2 - (r['pm'] - r['y']) ** 2 for r in rows])))
print(f'Brier(simulación pura) − Brier(mercado) IC95 [{lo:+.5f}, {hi:+.5f}]')
for a, z, t in ((-1, -.03, 'modelo ≥3 pts POR DEBAJO del mercado'), (-.03, -.01, '1–3 pts por debajo'), (-.01, .01, 'igual (±1 pt)'), (.01, .03, '1–3 pts por encima'), (.03, 1, 'modelo ≥3 pts POR ENCIMA del mercado')):
    s = [r for r in M if a <= r['p'] - r['pm'] < z]
    if s:
        lo, hi = boot(s, gapm)
        print(f"  {t:40s} n={len(s):4d} part={len({r['k'] for r in s}):2d} real={np.mean([r['y'] for r in s]):5.1%} p_merc={np.mean([r['pm'] for r in s]):5.1%} p_mod={np.mean([r['p'] for r in s]):5.1%} real−p_merc={gapm(s):+.1%} [{lo:+.1%},{hi:+.1%}] ROI={roi(s):+.1%}")
print('\n== 3. ¿«Cumple» añade información sobre el precio? real − p_mercado por grupo')
for t, s in (('cumple sí', [r for r in M if r['cumple_ficha'] == 'sí']), ('cumple no', [r for r in M if r['cumple_ficha'] == 'no'])):
    lo, hi = boot(s, gapm)
    print(f"  {t:12s} n={len(s):4d} real={np.mean([r['y'] for r in s]):5.1%} p_merc={np.mean([r['pm'] for r in s]):5.1%} real−p_merc={gapm(s):+.1%} IC95 [{lo:+.1%},{hi:+.1%}]")
# a igual precio: bandas de p_mercado
print('  a igual precio (banda de p_mercado): real con cumple sí vs no')
for a in (.3, .4, .5, .6, .7, .8, .9):
    s1 = [r for r in M if a <= r['pm'] < a + .1 and r['cumple_ficha'] == 'sí']; s0 = [r for r in M if a <= r['pm'] < a + .1 and r['cumple_ficha'] == 'no']
    if s1 and s0:
        print(f"    p_merc {a:.1f}–{a + .1:.1f}: sí {np.mean([r['y'] for r in s1]):5.1%} (n={len(s1)}) · no {np.mean([r['y'] for r in s0]):5.1%} (n={len(s0)})")
# K de N: regularidad mínima de ambos equipos
def reg(s):
    try:
        a, b = s.split(' de '); return int(a), int(b)
    except Exception:
        return None
print('  por regularidad mínima de los dos equipos (x de 7), real − p_mercado:')
for k in range(0, 8):
    s = [r for r in M if reg(r['reg_local']) and reg(r['reg_visitante']) and reg(r['reg_local'])[1] >= 5 and reg(r['reg_visitante'])[1] >= 5 and min(reg(r['reg_local'])[0], reg(r['reg_visitante'])[0]) == k]
    if s:
        print(f"    mínimo {k} de 7: n={len(s):4d} real={np.mean([r['y'] for r in s]):5.1%} p_merc={np.mean([r['pm'] for r in s]):5.1%} real−p_merc={gapm(s):+.1%} ROI={roi(s):+.1%}")
print('\n== 4. Calibración del modelo por tramos (IC por partidos)')
for a in np.arange(0, 1, .1):
    s = [r for r in E if a <= r['p'] < a + .1]
    if s:
        lo, hi = boot(s, gap)
        print(f"  p {a:.1f}–{a + .1:.1f}: n={len(s):4d} real={np.mean([r['y'] for r in s]):5.1%} dicho={np.mean([r['p'] for r in s]):5.1%} real−p={gap(s):+.1%} IC95 [{lo:+.1%},{hi:+.1%}]")
print('\n== 5. Margen de Betano (overround) por mercado en la jornada del 14-nov (pares Más/Menos)')
J = [r for r in R if r['jornada'] == '2026-11-14' and not r['mercado'].startswith('jugador')]
par = collections.defaultdict(dict)
for r in J:
    par[(r['partido'], r['mercado'], r['ambito'], r['linea'])][r['lado']] = f(r['cuota'])
ov = collections.defaultdict(list)
for (pa, m, a, l), v in par.items():
    if v.get('Más') and v.get('Menos'):
        ov[m].append(1 / v['Más'] + 1 / v['Menos'] - 1)
for m, v in sorted(ov.items()):
    print(f'  {m:14s} pares={len(v):4d} margen medio {np.mean(v):.1%} · mediana {np.median(v):.1%}')
print('\n== 6. Validación del «recorte de p» de analisis_jornada.py dejando un partido fuera (líneas con cumple sí)')
C = [r for r in E if r['cumple_ficha'] == 'sí']
ks = sorted({r['k'] for r in C})
MS = 20
def factores(train):
    g_ac = sum(r['y'] for r in train); g_es = sum(r['p'] for r in train); fg = min(1, g_ac / g_es) if g_es else 1
    def fac(rows):
        if not rows: return fg
        ac = sum(r['y'] for r in rows); es = sum(r['p'] for r in rows); d = es / len(rows)
        return min(1, (ac + MS * fg * d) / (es + MS * d))
    ml = collections.defaultdict(list); bc = collections.defaultdict(list)
    for r in train:
        ml[(r['mercado'], r['lado'])].append(r); bc[banda(r['c'])].append(r)
    return fg, {k: fac(v) for k, v in ml.items()}, {k: fac(v) for k, v in bc.items()}
def banda(c):
    return 0 if c < 1.3 else 1 if c < 1.5 else 2 if c < 2 else 3
b_raw = b_rec = b_glob = b_mkt = 0; n = 0; filas_rec = []
for k in ks:
    train = [r for r in C if r['k'] != k]; test = [r for r in C if r['k'] == k]
    fg, fml, fbc = factores(train)
    for r in test:
        fa = fml.get((r['mercado'], r['lado']), fg); fb = fbc.get(banda(r['c']), fg)
        pr = r['p'] * min(fa, fb, 1)
        b_raw += (r['p'] - r['y']) ** 2; b_rec += (pr - r['y']) ** 2; b_glob += (r['p'] * fg - r['y']) ** 2; b_mkt += ((r['pm'] if r['pm'] is not None else r['p']) - r['y']) ** 2; n += 1
        filas_rec.append({**r, 'pr': pr})
print(f'  n={n} en {len(ks)} partidos · Brier p cruda {b_raw / n:.5f} · p recortada (fuera de muestra) {b_rec / n:.5f} · solo factor global {b_glob / n:.5f} · mercado {b_mkt / n:.5f}')
lo, hi = boot(filas_rec, lambda rows: float(np.mean([(r['pr'] - r['y']) ** 2 - (r['p'] - r['y']) ** 2 for r in rows])))
print(f'  Brier(recortada) − Brier(cruda) = {(b_rec - b_raw) / n:+.5f} IC95 por partidos [{lo:+.5f}, {hi:+.5f}] (negativo = el recorte mejora)')
print(f"  real {np.mean([r['y'] for r in C]):.1%} · p cruda {np.mean([r['p'] for r in C]):.1%} · p recortada fuera de muestra {np.mean([r['pr'] for r in filas_rec]):.1%}")
# por jornada: ¿el sesgo es estable?
for j in sorted({r['jornada'] for r in C}):
    s = [r for r in C if r['jornada'] == j]
    print(f"  jornada {j}: n={len(s)} partidos={len({r['k'] for r in s})} real={np.mean([r['y'] for r in s]):.1%} dicho={np.mean([r['p'] for r in s]):.1%}")
print('  real − p por partido (cumple sí):', ' '.join(f"{gap([r for r in C if r['k'] == k]):+.0%}(n{len([r for r in C if r['k'] == k])})" for k in ks))
print('\n== 7. Jugadores (calificadas con cuota)')
Jp = [r for r in Jg if r['p'] is not None]
print('  con p del modelo:', len(Jp), '· sin p:', len(Jg) - len(Jp), '· partidos:', len({r['k'] for r in Jg}), '· nulas (no jugó):', sum(1 for r in R if r['resultado'] == 'nula'))
if Jp:
    fila('  jugadores (todas)', Jp)
    for m in sorted({r['mercado'] for r in Jp}):
        fila('   ' + m, [r for r in Jp if r['mercado'] == m])
    for a in np.arange(0, 1, .2):
        s = [r for r in Jp if a <= r['p'] < a + .2]
        if s:
            print(f"    p {a:.1f}–{a + .2:.1f}: n={len(s):4d} real={np.mean([r['y'] for r in s]):5.1%} dicho={np.mean([r['p'] for r in s]):5.1%}")
    Jm = [r for r in Jp if r['pm'] is not None]
    if Jm:
        print(f"  Brier jugadores: modelo {brier(np.array([r['p'] for r in Jm]), np.array([r['y'] for r in Jm])):.5f} · mercado {brier(np.array([r['pm'] for r in Jm]), np.array([r['y'] for r in Jm])):.5f} (n={len(Jm)})")
print('\n== 8. Potencia: ¿cuántas apuestas hacen falta para ver una ventaja?')
for edge in (.02, .03, .05):
    for cuo in (1.3, 1.9):
        pw = 1 / cuo * (1 + edge)   # p real que da ROI = edge
        sd = math.sqrt(pw * (1 - pw)) * cuo
        nn = (1.96 * sd / edge) ** 2
        print(f'  ROI real +{edge:.0%} a cuota {cuo}: desviación por apuesta {sd:.2f} u → ~{nn:,.0f} apuestas INDEPENDIENTES para que el IC95 excluya 0')
