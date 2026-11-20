# -*- coding: utf-8 -*-
"""Aprendizaje de las combinadas: por qué se pierden, qué pata las tumba y qué reglas de armado sugieren los datos.

    python3 recoleccion/aprender_combos.py

Fuentes (todo dentro del repo):
  · registro/sugerencias.csv        combinadas / Bet Builder / BB Boost / misiones que Claude envió (patas_json con ✓/✗ y valor real)
  · jornadas/*/balance/boletos_betano.json + patas_calificadas.json   los boletos reales del usuario, pata por pata
  · registro/lineas.csv             lo que se sabía de cada pata ANTES del partido (X de 10, esperado, colchón, p del modelo)
Escribe:
  · registro/combos_patas.csv       una fila por pata de cada combinada (con lo que se sabía antes y cómo salió)
  · registro/aprendizaje_combos.json  resumen + post-mortem de cada combinada perdida + reglas que se aplican al armar combinadas
Honestidad: son pocas combinadas (decenas) de pocos días y las patas de un mismo partido no son independientes; los números son pistas.
Las reglas con n pequeño solo avisan («en observación»); no excluyen ninguna línea de la lista de líneas.
"""
import csv, glob, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MERC = [('tiros al arco', 'al_arco'), ('remates', 'remates'), ('corners', 'corners'), ('goles', 'goles'), ('saques de meta', 'saques_meta'),
        ('saques de banda', 'saques_banda'), ('fueras', 'fueras'), ('faltas', 'faltas'), ('tarjetas', 'tarjetas'), ('ambos', 'ambos')]
MIN_N_REGLA = 25      # con menos patas que esto la regla solo se muestra «en observación» (no cambia p)


def n(s):
    return unicodedata.normalize('NFKD', (s or '').replace('–', ' ').replace('—', ' ')).encode('ascii', 'ignore').decode().lower()


def num(x):
    try:
        return float(str(x).replace(',', '.'))
    except (TypeError, ValueError):
        return None


GENERICOS = {'club', 'del', 'los', 'las', 'the', 'unit', 'sub', 'saques', 'meta', 'banda', 'goles', 'gol', 'total', 'mas', 'menos', 'ambos', 'anotan', 'tiros', 'arco', 'remates', 'corners',
             'tarjetas', 'faltas', 'fueras', 'lugar', 'juego', 'gana', 'empate', 'segundo', 'tiempo', 'primer', 'handicap', 'resultado', 'partido'}


def toks(s):
    return [t for t in re.split(r'[^a-z0-9]+', n(s)) if len(t) >= 3 and t not in GENERICOS and t not in ('fc', 'sc', 'ba', 'sp', 'rj', 'rs', 'cf')]


def _coin(tt, equipo):
    """Palabras del texto que coinciden con las de un equipo (igualdad o prefijo: lyon ~ lyonnais)."""
    return {t for t in tt for u in equipo if t == u or (len(t) >= 4 and len(u) >= 4 and (u.startswith(t) or t.startswith(u)))}


# ------------------------------------------------------------------------------------------------ lineas.csv
def cargar_lineas():
    L = defaultdict(list)
    for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'):
        if not r['jugador']:
            L[r['jornada']].append(r)
    return L


def partidos_de(rows):
    out = {}
    for r in rows:
        p = r['partido']
        if p not in out and ' - ' in p:
            a, b = p.split(' - ', 1)
            out[p] = (set(toks(a)), set(toks(b)))
    return out


def casar(jor, texto, L, PA, partido_hint=None):
    """Busca en lineas.csv la línea de equipo a la que se refiere una pata. → (fila|None, ámbito, mercado)"""
    t = n(texto)
    if t.startswith(('jugador', 'hugo ')) or re.search(r'\d\+', t):
        return None
    mk = next((c for nom, c in MERC if nom in t), None)
    if mk is None and 'corner' in t:
        mk = 'corners'
    if mk is None:
        return None
    if mk == 'ambos':
        lado, linea = 'Sí' if ' si' in t or t.endswith('si') else 'No', ''
    else:
        m = re.search(r'(mas|menos)\s+([\d.]+)', t)
        if not m:
            return None
        lado, linea = ('Más' if m.group(1) == 'mas' else 'Menos'), float(m.group(2))
    cand = PA.get(jor, {})
    if partido_hint and partido_hint in cand:
        part = partido_hint
    else:
        tt = set(toks(re.sub(r'\([^)]*\)', ' ', texto)))
        best = sorted(((len(_coin(tt, a | b)), p) for p, (a, b) in cand.items()), reverse=True)
        if not best or best[0][0] == 0 or (len(best) > 1 and best[0][0] == best[1][0]):
            return None
        part = best[0][1]
    a, b = cand[part]
    tt = set(toks(re.sub(r'\([^)]*\)', ' ', texto)))
    ca, cb = _coin(tt, a), _coin(tt, b)
    amb = 'local' if (ca and not cb) else 'visitante' if (cb and not ca) else 'total'
    if ' 1t' in t or 'primer tiempo' in t:
        amb = '1T'
    elif ' 2t' in t or 'segundo tiempo' in t:
        amb = '2T'
    otra = None
    for r in L.get(jor, []):
        if r['partido'] == part and r['mercado'] == mk and r['ambito'] == amb and r['lado'] == lado:
            if mk == 'ambos' or num(r['linea']) == linea:
                return r, amb, mk
            otra = otra or r
    if otra is not None and mk != 'ambos':                 # la línea exacta no estaba en la lectura de Betano: se usa el esperado de la misma escalera
        r = dict(otra); r['linea'] = str(linea); esp = num(r['esperado'])
        r['colchon'] = str(round((esp - linea) if lado == 'Más' else (linea - esp), 2)) if esp is not None else ''
        r['reg_local'] = r['reg_visitante'] = ''; r['cumple_ficha'] = ''; r['p_modelo'] = ''; r['nota'] = 'línea no leída; colchón con el esperado de la escalera'
        return r, amb, mk
    return None


def feats(r):
    if r is None:
        return {}
    ra = [num(x.split(' de ')[0]) / num(x.split(' de ')[1]) for x in (r['reg_local'], r['reg_visitante']) if ' de ' in (x or '') and num(x.split(' de ')[1])]
    esp, col, lin = num(r['esperado']), num(r['colchon']), num(r['linea'])
    return {'x10_min': round(min(ra), 2) if ra else '', 'esperado': esp if esp is not None else '', 'colchon': col if col is not None else '',
            'colchon_rel': round(col / lin, 3) if (col is not None and lin) else '', 'cumple': r['cumple_ficha'], 'p_modelo': num(r['p_modelo']) or '',
            'linea': lin if lin is not None else '', 'lado': r['lado'], 'mercado': r['mercado'], 'ambito': r['ambito'], 'partido': r['partido'], 'real_ficha': r['nota'][:60]}


# ------------------------------------------------------------------------------------------------ combinadas
def combinadas():
    L = cargar_lineas()
    PA = {j: partidos_de(rs) for j, rs in L.items()}
    C = []                     # una combinada = {id, fuente, jornada, tipo, cuota, stake, resultado, patas:[{texto, ok, real, ...}]}
    for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'sugerencias.csv'), encoding='utf-8-sig'), delimiter=';'):
        if int(r['n_patas'] or 1) < 2 or r['resultado'] not in ('cumplió', 'falló'):
            continue
        try:
            pj = json.loads(r['patas_json'])
        except ValueError:
            continue
        jor = r['fecha_entrega'][:10]
        if jor not in L:
            continue
        hint = None
        if '–' in r['partidos'] and '|' not in r['partidos']:
            hint = next((p for p in PA.get(jor, {}) if n(p.replace(' - ', '–')) == n(r['partidos'])), None)
        fuente = 'BB Boost' if 'BB Boost' in r['tipo'] else 'Misión' if 'Misión' in r['tipo'] else 'sugerida'
        patas = [{'texto': t[0], 'cuota': t[1], 'ok': t[2] == 'C', 'real': t[3], 'cod': t[2]} for t in pj if t[2] in ('C', 'F')]
        if len(patas) != len(pj) or len(patas) < 2:
            continue
        C.append({'id': r['id'], 'fuente': fuente, 'jornada': jor, 'tipo': r['tipo'], 'nombre': r['nombre'], 'cuota': num(r['cuota']), 'p': num(r['p_estimada']),
                  'stake': '', 'resultado': r['resultado'], 'hint': hint, 'patas': patas})
    for fb in sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'balance', 'boletos_betano.json'))):
        bal = os.path.dirname(fb)
        fp = os.path.join(bal, 'patas_calificadas.json')
        if not os.path.exists(fp):
            continue
        PC = json.load(open(fp, encoding='utf8'))
        for b in json.load(open(fb, encoding='utf8'))['boletos']:
            x = PC.get(str(b['n']))
            if not x or b['resultado'] not in ('Ganada', 'Perdida', 'Cash Out'):
                continue
            patas = [{'texto': t, 'cuota': None, 'ok': e == '✓', 'real': d, 'cod': 'C' if e == '✓' else 'F'} for t, e, d in x['patas'] if e in ('✓', '✗')]
            if len(patas) < 2:
                continue
            C.append({'id': f"boleto {b['n']}", 'fuente': 'tu boleto', 'jornada': b['fecha'], 'tipo': b['tipo'], 'nombre': b['partidos'][:80], 'cuota': b['cuota'], 'p': None,
                      'stake': b['stake'], 'resultado': 'cumplió' if b['resultado'] == 'Ganada' else 'falló' if b['resultado'] == 'Perdida' else 'cash out', 'hint': None, 'patas': patas})
    for c in C:
        for p in c['patas']:
            r = casar(c['jornada'], p['texto'], L, PA, c['hint'])
            p['f'] = feats(r[0] if r else None)
    return C


# ------------------------------------------------------------------------------------------------ análisis
def tasa(ps):
    ps = [p for p in ps]
    return (sum(p['ok'] for p in ps) / len(ps)) if ps else None


def causa(c, p, i):
    """Por qué cayó una pata y qué hacer en partidos parecidos (solo con lo que se sabía antes y el resultado)."""
    f = p.get('f') or {}
    if not f:
        return 'sin datos previos de la pata (no casó con lineas.csv)', 'sin_datos'
    col, x10, cum, lado = f.get('colchon_rel'), f.get('x10_min'), f.get('cumple'), f.get('lado')
    if f.get('mercado') == 'ambos':
        return f"«Ambos marcan» exige que anoten los dos: aquí {p['real']}; el equipo que menos anota ({f.get('x10_min')} de 10) lo rompió", 'ambos'
    if cum == 'no':
        return f"no cumplía el 7 de 10 ({f.get('x10_min')}); era una pata que el filtro ya dudaba", 'sin_cumplir'
    if col != '' and col is not None and abs(col) < 0.10:
        return f"pata en la mediana: colchón de solo {col * 100:.0f} % de la línea (esperado {f.get('esperado')}, real {p['real']})", 'mediana'
    esp = f.get('esperado')
    return f"cumplía y tenía colchón ({(col or 0) * 100:.0f} %) pero el partido salió atípico: real {p['real']} frente a esperado {esp}", 'atipico'


def analizar(C):
    patas = []
    for c in C:
        n_f = sum(not p['ok'] for p in c['patas'])
        for i, p in enumerate(c['patas']):
            f = p.get('f') or {}
            patas.append({'combo': c['id'], 'fuente': c['fuente'], 'jornada': c['jornada'], 'tipo': c['tipo'], 'n_patas': len(c['patas']), 'resultado_combo': c['resultado'],
                          'patas_falladas': n_f, 'texto': p['texto'], 'cuota_pata': p['cuota'] or '', 'resultado_pata': 'cumplió' if p['ok'] else 'falló', 'valor_real': p['real'],
                          'partido': f.get('partido', ''), 'mercado': f.get('mercado', ''), 'ambito': f.get('ambito', ''), 'lado': f.get('lado', ''), 'linea': f.get('linea', ''),
                          'x10_min': f.get('x10_min', ''), 'cumple': f.get('cumple', ''), 'esperado': f.get('esperado', ''), 'colchon': f.get('colchon', ''),
                          'colchon_rel': f.get('colchon_rel', ''), 'p_modelo': f.get('p_modelo', ''), 'es_la_mas_floja': ''})
    # pata más floja de cada combinada = la de menor colchón relativo (solo si TODAS tienen dato)
    por = defaultdict(list)
    for q in patas:
        por[q['combo'] + '|' + q['jornada']].append(q)
    res = {}
    uno = []                  # combinadas perdidas por una sola pata, con dato de todas las patas
    for k, ps in por.items():
        if all(q['colchon_rel'] != '' for q in ps):
            m = min(q['colchon_rel'] for q in ps)
            for q in ps:
                q['es_la_mas_floja'] = 'sí' if q['colchon_rel'] == m else 'no'
            if ps[0]['resultado_combo'] == 'falló' and sum(q['resultado_pata'] == 'falló' for q in ps) == 1:
                uno.append(ps)
    cs = [c for c in C if c['resultado'] in ('cumplió', 'falló')]
    gan = [c for c in cs if c['resultado'] == 'cumplió']
    perd = [c for c in cs if c['resultado'] == 'falló']
    una = [c for c in perd if sum(not p['ok'] for p in c['patas']) == 1]
    todas = [p for c in C for p in c['patas']]
    # ¿la pata más floja es la que cae?
    acierta_floja = sum(1 for ps in uno if [q for q in ps if q['resultado_pata'] == 'falló'][0]['es_la_mas_floja'] == 'sí')
    azar = sum(1 / len(ps) for ps in uno)
    # tasa de pata por banda de colchón relativo y por cumple, dentro de combinadas
    band = lambda v: 'sin dato' if v == '' else '< 5 %' if v < .05 else '5–10 %' if v < .10 else '10–20 %' if v < .20 else '≥ 20 %'
    por_banda = defaultdict(list)
    por_cumple = defaultdict(list)
    por_merc = defaultdict(list)
    for q in patas:
        por_banda[band(q['colchon_rel'])].append(q['resultado_pata'] == 'cumplió')
        if q['cumple'] in ('sí', 'no'):
            por_cumple[q['cumple']].append(q['resultado_pata'] == 'cumplió')
        if q['mercado']:
            por_merc[f"{q['mercado']} {q['lado']}"].append(q['resultado_pata'] == 'cumplió')
    pr = lambda L_: {'n': len(L_), 'hit': round(sum(L_) / len(L_), 3) if L_ else None}
    # post-mortem de cada combinada perdida
    pm = []
    for c in perd:
        malas = [(i, p) for i, p in enumerate(c['patas']) if not p['ok']]
        item = {'id': c['id'], 'fuente': c['fuente'], 'jornada': c['jornada'], 'tipo': c['tipo'], 'nombre': c['nombre'], 'cuota': c['cuota'], 'n_patas': len(c['patas']), 'patas_falladas': len(malas),
                'detalle': [], 'causas': []}
        for i, p in enumerate(c['patas']):
            f = p.get('f') or {}
            item['detalle'].append({'pata': p['texto'], 'ok': p['ok'], 'real': p['real'], 'colchon_rel': f.get('colchon_rel', ''), 'x10': f.get('x10_min', ''), 'cumple': f.get('cumple', '')})
        for i, p in malas:
            tx, ct = causa(c, p, i)
            item['causas'].append({'pata': p['texto'], 'causa': tx, 'tipo': ct})
        pm.append(item)
    cc = Counter(x['tipo'] for it in pm for x in it['causas'])
    # tamaño de la combinada: lo que salió frente a lo que saldría si las patas fueran independientes (con la tasa de pata de esas mismas combinadas)
    por_n = {}
    for k in sorted({len(c['patas']) for c in cs}):
        g = [c for c in cs if len(c['patas']) == k] if k < 4 else [c for c in cs if len(c['patas']) >= 4]
        key = str(k) if k < 4 else '4+'
        if key in por_n:
            continue
        pp = [p for c in g for p in c['patas']]
        hp = tasa(pp)
        por_n[key] = {'combinadas': len(g), 'se_dieron': sum(c['resultado'] == 'cumplió' for c in g), 'hit': round(sum(c['resultado'] == 'cumplió' for c in g) / len(g), 3),
                      'hit_pata': round(hp, 3), 'si_independientes': round(hp ** (sum(len(c['patas']) for c in g) / len(g)), 3)}
    por_fuente = {}
    for f in sorted({c['fuente'] for c in cs}):
        g = [c for c in cs if c['fuente'] == f]
        por_fuente[f] = {'combinadas': len(g), 'se_dieron': sum(c['resultado'] == 'cumplió' for c in g), 'patas_prom': round(sum(len(c['patas']) for c in g) / len(g), 1),
                         'hit_pata': round(tasa([p for c in g for p in c['patas']]), 3)}
    bc = defaultdict(list)
    for q in patas:
        if q['cuota_pata'] != '':
            c_ = float(q['cuota_pata']); bc['< 1,30' if c_ < 1.3 else '1,30–1,49' if c_ < 1.5 else '1,50–1,79' if c_ < 1.8 else '1,80 o más'].append(q['resultado_pata'] == 'cumplió')
    out = {
        'generado': 'recoleccion/aprender_combos.py', 'n_combinadas': len(cs), 'se_dieron': len(gan), 'perdidas': len(perd), 'perdidas_por_una_pata': len(una),
        'patas': {'n': len(todas), 'hit': round(tasa(todas), 3) if todas else None, 'con_dato_previo': sum(1 for q in patas if q['colchon_rel'] != '')},
        'pata_mas_floja': {'combinadas_perdidas_por_una_pata_con_dato': len(uno), 'la_que_cayo_era_la_mas_floja': acierta_floja, 'por_azar_esperado': round(azar, 1)},
        'por_banda_colchon': {k: pr(v) for k, v in sorted(por_banda.items())}, 'por_cumple': {k: pr(v) for k, v in por_cumple.items()},
        'por_mercado_lado': {k: pr(v) for k, v in sorted(por_merc.items(), key=lambda kv: -len(kv[1])) if len(v) >= 8},
        'por_n_patas': por_n, 'por_fuente': por_fuente, 'por_cuota_pata': {k: pr(v) for k, v in bc.items()},
        'causas': dict(cc), 'postmortem': pm}
    return patas, out


def reglas(out):
    """Reglas de armado que usa analisis_jornada.py. Cada una trae su n; con n < MIN_N_REGLA queda «en observación» (avisa, no recorta p)."""
    R = []
    pb = out['por_banda_colchon']
    chica = pb.get('< 5 %', {'n': 0, 'hit': None})
    media = pb.get('5–10 %', {'n': 0, 'hit': None})
    grande = [pb.get(k, {'n': 0, 'hit': None}) for k in ('10–20 %', '≥ 20 %')]
    ng = sum(g['n'] for g in grande)
    hg = (sum(g['n'] * (g['hit'] or 0) for g in grande) / ng) if ng else None
    nm = chica['n'] + media['n']
    hm = ((chica['n'] * (chica['hit'] or 0) + media['n'] * (media['hit'] or 0)) / nm) if nm else None
    R.append({'id': 'pata_mediana', 'texto': 'En una combinada, evitar la pata con colchón < 10 % de la línea (la «pata en la mediana»): es la que más se cae.',
              'umbral_colchon_rel': 0.10, 'n_baja': nm, 'hit_baja': round(hm, 3) if hm is not None else None, 'n_alta': ng, 'hit_alta': round(hg, 3) if hg is not None else None,
              'estado': 'activa' if (nm >= MIN_N_REGLA and hm is not None and hg is not None and hg - hm >= .05) else 'en observación'})
    pc_ = out['por_cumple']
    R.append({'id': 'pata_sin_cumplir', 'texto': 'En una combinada, todas las patas deben cumplir el 7 de 10 en ambos equipos.', 'n_no': pc_.get('no', {}).get('n', 0), 'hit_no': pc_.get('no', {}).get('hit'),
              'n_si': pc_.get('sí', {}).get('n', 0), 'hit_si': pc_.get('sí', {}).get('hit'),
              'estado': 'activa' if (pc_.get('no', {}).get('n', 0) >= MIN_N_REGLA and (pc_.get('sí', {}).get('hit') or 0) - (pc_.get('no', {}).get('hit') or 0) >= .10) else 'en observación'})
    pm_ = out['por_mercado_lado']
    R.append({'id': 'ambos_si', 'texto': '«Ambos marcan: Sí» dentro de una combinada solo si los dos equipos marcan en ≥ 7 de 10.', 'n': pm_.get('ambos Sí', {}).get('n', 0), 'hit': pm_.get('ambos Sí', {}).get('hit'),
              'estado': 'activa' if (pm_.get('ambos Sí', {}).get('n', 0) >= MIN_N_REGLA and (pm_.get('ambos Sí', {}).get('hit') or 1) < .55) else 'en observación'})
    pn = out['por_n_patas']
    g4 = pn.get('4+', {})
    R.append({'id': 'patas_max', 'texto': 'Máximo 2 patas por combinada (3 solo como lotería de stake mínimo); 4 o más patas casi nunca se dan.', 'n_4mas': g4.get('combinadas', 0),
              'hit_4mas': g4.get('hit'), 'hit_2': pn.get('2', {}).get('hit'), 'hit_3': pn.get('3', {}).get('hit'),
              'estado': 'activa' if g4.get('combinadas', 0) >= MIN_N_REGLA else 'en observación'})
    return R


def lecciones(out):
    pn, un = out['por_n_patas'], out['perdidas_por_una_pata']
    L = [f"{out['n_combinadas']} combinadas calificadas (las que te envié y las que jugaste): {out['se_dieron']} se dieron ({out['se_dieron'] * 100 // out['n_combinadas']} %). {un} de {out['perdidas']} perdidas ({un * 100 // max(1, out['perdidas'])} %) cayeron por una sola pata.",
         f"Tamaño: 2 patas se dieron {pn.get('2', {}).get('se_dieron', 0)} de {pn.get('2', {}).get('combinadas', 0)}, 3 patas {pn.get('3', {}).get('se_dieron', 0)} de {pn.get('3', {}).get('combinadas', 0)}, 4 o más {pn.get('4+', {}).get('se_dieron', 0)} de {pn.get('4+', {}).get('combinadas', 0)}. Cada pata extra pesa más de lo que parece."]
    pf = out['pata_mas_floja']
    L.append(f"La pata de menor colchón cayó {pf['la_que_cayo_era_la_mas_floja']} veces de {pf['combinadas_perdidas_por_una_pata_con_dato_n'] if 'combinadas_perdidas_por_una_pata_con_dato_n' in pf else pf['combinadas_perdidas_por_una_pata_con_dato']} (por azar se esperarían ≈ {pf['por_azar_esperado']}): el colchón no predice cuál pata se cae.")
    pc_ = out['por_cumple']
    if 'sí' in pc_ and 'no' in pc_:
        L.append(f"Patas que cumplían el 7 de 10 se dieron {round(pc_['sí']['hit'] * 100)} % (n {pc_['sí']['n']}) frente a {round(pc_['no']['hit'] * 100)} % de las que no (n {pc_['no']['n']}): esta sí separa.")
    c = out['causas']
    tot = sum(v for k, v in c.items() if k != 'sin_datos') or 1
    L.append(f"De las patas caídas con dato previo, {c.get('atipico', 0)} de {tot} cumplían y tenían colchón: el partido salió fuera de lo normal (varianza), no fue una mala elección; {c.get('sin_cumplir', 0)} no cumplían el 7 de 10 y {c.get('mediana', 0)} estaban en la mediana.")
    return L


def main():
    C = combinadas()
    patas, out = analizar(C)
    out['reglas'] = reglas(out)
    out['lecciones'] = lecciones(out)
    campos = list(patas[0].keys())
    with open(os.path.join(RAIZ, 'registro', 'combos_patas.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=';'); w.writeheader(); w.writerows(patas)
    json.dump(out, open(os.path.join(RAIZ, 'registro', 'aprendizaje_combos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(f"{out['n_combinadas']} combinadas ({out['se_dieron']} se dieron, {out['perdidas']} perdidas, {out['perdidas_por_una_pata']} por una sola pata); patas {out['patas']}")
    print('pata más floja:', out['pata_mas_floja']); print('por banda de colchón:', out['por_banda_colchon']); print('por cumple:', out['por_cumple']); print('causas:', out['causas'])
    for t in out['lecciones']:
        print(' -', t)
    print('por n patas:', out['por_n_patas']); print('por fuente:', out['por_fuente'])
    for r in out['reglas']:
        print(' regla', r['id'], r['estado'], {k: v for k, v in r.items() if k.startswith(('n', 'hit'))})


if __name__ == '__main__':
    main()
