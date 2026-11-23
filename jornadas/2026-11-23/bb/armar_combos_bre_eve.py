"""Arma bb/combos_brentford-fc-everton-fc.json (combos con precio real de Betano + probabilidad). Se corre desde la raíz del repo; se repite en cada relectura (13:55)."""
import json, sys
J = 'jornadas/2026-11-23/'; hora = sys.argv[1] if len(sys.argv) > 1 else '12:05'
d = json.load(open(J + 'bb/cands_brentford-fc-everton-fc.json'))
P = {tuple(k.split('|')): v for k, v in json.load(open(J + 'bb/precios_reales_1205.json')).items()}
ev = json.load(open(J + 'bb/evaluacion_equipo_1215.json'))
names = dict(zip(d['pool_ids'], d['pool_nombres'])); names['10849159081'] = 'Thierno Barry Remates 3+ (jugador)'
for i, n in (('10849137869', 'Remates Everton FC Más 12.5'), ('10848474916', 'Tarjetas Brentford FC Más 1.5'), ('10884403399', 'Saques de meta Brentford FC Más 6.5')): names.setdefault(i, n)
cat = json.load(open(J + 'bb/catalogo_brentford-fc-everton-fc_1151.json'))['brentford-fc-everton-fc']
price = {}
for m in cat['m']:
    for s in m['s']: price[s[0]] = s[2]
for m in json.load(open(J + 'bb/betano_full_brentford-fc-everton-fc_1152.json'))['full']:
    for s in m['s']: price.setdefault(s[0], s[2])
cand = {tuple(x['ids']): x for x in d['candidatos']}
out = []
for k, pr in P.items():
    c = cand.get(k); cu = [price.get(i) for i in k]; prod = 1
    for x in cu: prod *= (x or 1)
    out.append({'patas': [names.get(i, i) for i in k], 'ids': list(k), 'cuotas': cu, 'producto': round(prod, 2), 'precio': pr, 'p_ajust': c['p_ajust'] if c else None, 'p_stress': c['p_stress'] if c else None,
                'jugador': '10849159081' in k, 'cumple_bb': bool(all(x and x > 1.5 for x in cu) and pr >= 5.05 and len(k) >= 3)})
ER = 'Remates Everton FC Más 11.5'; EF = 'Faltas Everton FC Menos 10.5'; BC5 = 'Córners Brentford FC Menos 5.5'
def setp(legs, key):
    for o in out:
        if set(o['patas']) == set(legs): o['p_ajust'] = ev[key]['p_ajust']; o['p_stress'] = ev[key]['p_stress']
setp([ER, EF, BC5], 'CORE (ER+EF+BC5)'); setp([ER, EF, BC5, 'Remates Brentford FC Menos 16.5'], 'X2 core+BR'); setp([ER, EF, BC5, 'Tarjetas Brentford FC Más 1.5'], 'X4 core+BT')
setp([ER, EF, BC5, 'Saques de meta Brentford FC Más 6.5'], 'X5 core+BSM'); setp([ER, EF, BC5, 'Tiros al arco Everton FC Más 3.5'], 'X8 core+ES'); setp(['Remates Everton FC Más 12.5', EF, BC5], 'X1 ER12+EF+BC5')
setp([ER, EF, 'Remates Brentford FC Menos 16.5'], 'H2 sin Barry (ER+EF+BR)')
FB = 0.62
for o in out:
    if o['jugador']:
        eq = set(l for l in o['patas'] if 'Barry' not in l)
        base = next((q for q in out if set(q['patas']) == eq and q['p_ajust'] is not None), None)
        if base is None and eq == {ER, EF, 'Remates Brentford FC Menos 16.5'}:
            base = {'p_ajust': ev['H2 sin Barry (ER+EF+BR)']['p_ajust'], 'p_stress': ev['H2 sin Barry (ER+EF+BR)']['p_stress']}
        o['p_base_equipo'] = base and base['p_ajust']; o['f_barry'] = FB
        if base:
            o['p_ajust'] = round(base['p_ajust'] * FB, 4); o['p_stress'] = round(base['p_stress'] * 0.54, 4) if base['p_stress'] else None
        o['nota'] = 'Incluye un jugador: p = p del tramo de equipo × P(Barry 3+ remates | Everton tira mucho) ≈ 0,62 (rango 0,54–0,71; 6 de 7 partidos de Everton con ≥12 remates; sin validar). El «stress» usa 0,54 (sin dependencia).'
out.sort(key=lambda o: (-o['cumple_bb'], -(o['p_stress'] or 0)))
json.dump({'leido': f'2026-11-23 {hora} Bogotá (precios mc-leg; catálogo 11:51)', 'boost_nota': 'El % del Boost (+25 % o +50 %) se lee en el cupón: el 21-nov cobró +50 %.', 'combos': out}, open(J + 'bb/combos_brentford-fc-everton-fc.json', 'w'), ensure_ascii=False)
print(len(out), sum(1 for o in out if o['cumple_bb']))
for o in out:
    if o['jugador'] or set(o['patas']) in ({ER, EF, BC5},): print(o['precio'], o['p_ajust'], o['p_stress'], o['cumple_bb'], o['patas'])
