#!/usr/bin/env python3
"""Informe completo de un partido, ordenado por PROBABILIDAD (no por valor contra la cuota).

Uso: python3 recoleccion/informe_completo.py jornadas/AAAA-MM-DD <clave> [sofascore.json]

Lee (todo en el repo, sin red):
  betano/<clave>.json            cuotas y mercados que Betano ofrece hoy
  fichas/ficha_<clave>.json      regularidad X de 7 (equipos) y esperado
  informes/<clave>_resultado.json  modelo (p, p_mercado, resultado, builders)
  flashscore/<clave>.json        alineación probable de Flashscore (para compararla)
  jugadores/<clave>_sofascore.json  alineación predicha + últimos 7 de cada jugador, equipos y árbitro (Sofascore)
  notas/<clave>_enfoque.md       bloque «Enfoque de mercados» y lectura del partido (escrito a mano)
Escribe informes_completos/<clave>.md

Reglas del proyecto: primero lo que Betano ofrece; jugadores solo con alineación probable/confirmada (fuente y hora);
el colchón y el EV se informan pero no mandan; lo que falta se dice.
"""
import csv, difflib, itertools, json, math, os, sys, unicodedata
from statistics import mean

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(s):
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    for a, b in (('đ', 'd'), ('ł', 'l'), ('ø', 'o'), ('ć', 'c'), ('-', ' '), ('.', ' '), ("'", '')):
        s = s.replace(a, b)
    return ' '.join(s.split())


def apellido(s):
    t = norm(s).split()
    return t[-1] if t else ''


def pois_ge(lam, k):
    return 1 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))


def pct(x):
    return f'{100 * x:.0f} %'


IDX = {'atajadas': 13, 'remates': 2, 'al_arco': 3, 'anota': 4, 'asiste': 5, 'faltas': 6, 'entradas': 7, 'tarjeta': 9}
NOMBRE = {'atajadas': 'Atajadas', 'remates': 'Remates', 'al_arco': 'Tiros al arco', 'anota': 'Anota', 'asiste': 'Asiste', 'faltas': 'Faltas cometidas',
          'entradas': 'Entradas', 'tarjeta': 'Tarjeta', 'anota_o_asiste': 'Anota o asiste'}
VOLUMEN = ('remates', 'al_arco', 'faltas', 'entradas')
NOM_MERC = {'goles': 'Goles', 'corners': 'Córners', 'tarjetas': 'Tarjetas', 'remates': 'Remates', 'al_arco': 'Tiros al arco', 'faltas': 'Faltas', 'fueras': 'Fueras de juego', 'saques_banda': 'Saques de banda', 'saques_meta': 'Saques de meta'}
RAROS = ('anota', 'asiste', 'anota_o_asiste', 'tarjeta')


def cargar(jornada, clave, sofa_path=None):
    j = lambda *p: os.path.join(jornada, *p)
    d = {'clave': clave}
    d['bet'] = json.load(open(j('betano', clave + '.json')))
    d['ficha'] = json.load(open(j('fichas', f'ficha_{clave}.json')))
    d['modelo'] = json.load(open(j('informes', f'{clave}_resultado.json')))
    d['fs'] = json.load(open(j('flashscore', clave + '.json')))
    d['sofa'] = json.load(open(sofa_path or j('jugadores', f'{clave}_sofascore.json')))
    enf = j('notas', f'{clave}_enfoque.md')
    d['enfoque'] = open(enf, encoding='utf-8').read() if os.path.exists(enf) else '_(sin enfoque escrito)_'
    meta = d['bet']['meta']
    d['loc'], d['vis'] = meta['local'], meta['visitante']
    rows = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
    d['reg'] = [r for r in rows if r['jornada'] == os.path.basename(jornada.rstrip('/')) and r['partido'] == f"{d['loc']} - {d['vis']}"]
    return d


# ---------- tarjetas (Sofascore) ----------
def tarjetas_sofa(d):
    S = d['sofa']
    T, R = S['T'], S.get('R', [])
    def m(rows, i):
        v = [r[i] for r in rows if r[i] is not None]
        return (mean(v), len(v)) if v else (None, 0)
    hf, nhf = m(T['h'], 5); hc, _ = m(T['h'], 6); af, naf = m(T['a'], 5); ac, _ = m(T['a'], 6)
    ry, nry = m(R, 3)
    exp_h = (hf + ac) / 2 if hf is not None and ac is not None else None
    exp_a = (af + hc) / 2 if af is not None and hc is not None else None
    tot_eq = exp_h + exp_a
    tot = 0.65 * tot_eq + 0.35 * ry if ry is not None else tot_eq
    esc = tot / tot_eq
    return dict(hf=hf, hc=hc, af=af, ac=ac, exp_h=exp_h * esc, exp_a=exp_a * esc, tot=tot, tot_eq=tot_eq, ref_mean=ry, ref_n=nry,
                serie_h=[r[5] for r in T['h']], serie_a=[r[5] for r in T['a']],
                serie_hc=[r[6] for r in T['h']], serie_ac=[r[6] for r in T['a']], ref_serie=[r[3] for r in R])


# ---------- jugadores ----------
def emparejar(d):
    """Casa nombres de Betano con los de Sofascore (por apellido y similitud). Devuelve {nombre_betano: nombre_sofa}."""
    sofa = list(d['sofa']['P'].keys())
    out = {}
    for x in d['bet']['betano']['jugadores']:
        n = x['jugador']
        if n in out:
            continue
        ini = norm(n).split()[0][:1]
        cand = [s for s in sofa if apellido(s) == apellido(n) and norm(s).split()[0][:1] == ini]
        if len(cand) != 1:
            best = max(sofa, key=lambda s: difflib.SequenceMatcher(None, norm(s), norm(n)).ratio())
            cand = [best] if difflib.SequenceMatcher(None, norm(best), norm(n)).ratio() >= 0.8 else []
        if len(cand) == 1:
            out[n] = cand[0]
    return out


def sep_nombre(n):
    """«van Hecke J. P.» -> (['van','hecke'], 'j')."""
    t = norm(n).split()
    k = len(t)
    while k > 1 and len(t[k - 1]) == 1:
        k -= 1
    ini = t[k][:1] if k < len(t) else ''
    return [x for x in t[:k] if len(x) > 1], ini


def en_flashscore(d):
    """Once probables de Flashscore (12-nov) como pares (apellido normalizado, inicial); formato «Apellido I.»."""
    try:
        pr = d['fs']['lineups']['probables']
        out = set()
        for lado in ('L', 'V'):
            for p in pr[lado]:
                ap, ini = sep_nombre(p['n'])
                for x in ap:
                    out.add((x, ini))
        return out
    except Exception:
        return set()


def parecido(a, b):
    return a == b or difflib.SequenceMatcher(None, a, b).ratio() >= 0.85


def coincide_fs(sn, fsset):
    t = norm(sn).split()
    return any(parecido(x, y) and (ini in ('', t[0][:1])) for x in t[1:] if len(x) > 1 for (y, ini) in fsset)


def lado_fav(d):
    p = d['modelo']['p_resultado']
    if abs(p['local'] - p['visitante']) < 0.10:
        return None
    return 'L' if p['local'] > p['visitante'] else 'V'


ADJ_FAV = {'atajadas': 0.85, 'remates': 1.10, 'al_arco': 1.10, 'anota': 1.10, 'asiste': 1.10, 'anota_o_asiste': 1.10, 'faltas': 0.90, 'entradas': 0.85, 'tarjeta': 0.90}
ADJ_DOG = {'atajadas': 1.15, 'remates': 0.85, 'al_arco': 0.85, 'anota': 0.85, 'asiste': 0.85, 'anota_o_asiste': 0.85, 'faltas': 1.10, 'entradas': 1.15, 'tarjeta': 1.15}


def jugadores(d):
    S = d['sofa']['P']
    mp = emparejar(d)
    fav = lado_fav(d)
    fs = en_flashscore(d)
    res = []
    for x in d['bet']['betano']['jugadores']:
        sn = mp.get(x['jugador'])
        if not sn:
            continue
        p = S[sn]
        rows = p['r']
        tot = sum(r[1] for r in rows)
        if tot <= 0:
            continue
        st = x['stat']
        if st == 'atajadas' and any(len(r) <= 13 for r in rows):
            continue
        val = [(r[4] + r[5]) if st == 'anota_o_asiste' else r[IDX[st]] for r in rows]
        if any(v is None for v in val):
            continue
        rate = sum(val) / tot * 90
        lado = p['l']
        f = 1.0 if fav is None else (ADJ_FAV[st] if lado == fav else ADJ_DOG[st])
        arr = [r[1] for r in rows if r[1] >= 60]
        if p['pos'] == 'G':
            m, nota = 90, ''
        elif len(arr) >= 4:
            m, nota = max(75, min(90, mean(arr))), ''
        else:
            m, nota = 65, 'pocos minutos recientes'
        lam = rate * f * m / 90
        ks = [(1, x['cuota'])] if 'cuota' in x else [(int(a), c) for a, c in x['escalera'].items()]
        for k, c in ks:
            fr = sum(1 for v in val if v >= k)
            pois = pois_ge(lam, k)
            fq = (fr + 0.5) / (len(val) + 1)
            mk = 1 / c
            w = (0.25, 0.15, 0.60) if st in RAROS else (0.35, 0.35, 0.30)
            res.append(dict(j=x['jugador'], sn=sn, st=st, k=k, c=c, mk=mk, pois=pois, fr=fr, n=len(val), pe=w[0] * pois + w[1] * fq + w[2] * mk,
                            lado=lado, lam=lam, nota=nota, m=m, fs=coincide_fs(sn, fs)))
    return res


def tabla_jug(rows, n=12, solo_cuota=None):
    out = ['| Jugador | Línea @cuota | X de 7 | p estimada | Mercado (1/cuota) | Notas |', '|---|---|---|---|---|---|']
    for r in sorted(rows, key=lambda r: -r['pe'])[:n]:
        notas = []
        if r['nota']:
            notas.append(r['nota'])
        notas.append('también en Flashscore' if r['fs'] else 'solo Sofascore')
        out.append(f"| {r['sn']} ({r['lado']}) | {NOMBRE[r['st']]} {r['k']}+ @{r['c']} | {r['fr']} de {r['n']} | **{pct(r['pe'])}** | {pct(r['mk'])} | {'; '.join(notas)} |")
    return '\n'.join(out)


# ---------- líneas de equipo ----------
def f2(x):
    try:
        return float(x)
    except Exception:
        return None


def lineas_equipo(d, familia, ambitos=('total', 'local', 'visitante'), lo=0.40, hi=0.90, n=9):
    rows = [r for r in d['reg'] if r['mercado'] == familia and r['ambito'] in ambitos and r['p_modelo']]
    out = []
    for amb in ambitos:
        rr = [r for r in rows if r['ambito'] == amb and lo <= f2(r['p_modelo']) <= hi]
        if not rr:
            continue
        rr.sort(key=lambda r: -f2(r['p_modelo']))
        out.append(f"**{ {'total': 'Total del partido', 'local': d['loc'], 'visitante': d['vis']}[amb] }**\n")
        out.append(f"| Línea | Cuota | p modelo | p mercado | Esperado (ficha) | Colchón | {d['loc']} (X de 7) | {d['vis']} (X de 7) | Directos | Cumple 5/7 |")
        out.append('|---|---|---|---|---|---|---|---|---|---|')
        for r in rr[:n]:
            out.append(f"| {r['lado']} {r['linea']} | {r['cuota']} | **{pct(f2(r['p_modelo']))}** | {pct(f2(r['p_mercado']) or 0)} | {r['esperado'] or '—'} | {r['colchon'] or '—'} | {r['reg_local'] or '—'} | {r['reg_visitante'] or '—'} | {r['directos'] or '—'} | {r['cumple_ficha'] or '—'} |")
        out.append('')
    return '\n'.join(out) if out else '_Betano no ofrece esta familia en este partido, o ninguna línea cae entre 40 % y 96 %._\n'


def modelo_lineas(d, ini=None, contiene=None, n=12):
    out = []
    for l in d['modelo']['lineas']:
        if ini and not l['seleccion'].startswith(ini):
            continue
        if contiene and contiene not in l['seleccion']:
            continue
        out.append(l)
    return sorted(out, key=lambda l: -l['p'])[:n]


# ---------- combinaciones ----------
def patas(d, jug, tj):
    P = []
    for r in d['reg']:
        if r['mercado'].startswith('jugador') or not r['p_modelo']:
            continue
        c, p = f2(r['cuota']), f2(r['p_modelo'])
        if c is None or c < 1.5 or p < 0.45 or r['ambito'] in ('1T', '2T'):
            continue
        if r['mercado'] == 'tarjetas' and tj:
            p = (tj.get((r['ambito'], r['lado'], f2(r['linea'])), p) + p) / 2  # promedio Sofascore/modelo (conservador)
        amb = {'total': 'total', 'local': d['loc'], 'visitante': d['vis']}[r['ambito']]
        P.append(dict(nombre=f"{NOM_MERC.get(r['mercado'], r['mercado'])} {amb} {r['lado']} {r['linea']}", c=c, p=p, slot=('eq', r['mercado'], r['ambito'])))
    for l in d['modelo']['lineas']:
        if l['seleccion'].startswith('Ambos marcan') and l['cuota'] >= 1.5 and l['p'] >= 0.45:
            P.append(dict(nombre=l['seleccion'], c=l['cuota'], p=l['p'], slot=('ambos',)))
        if l['seleccion'] in (f"Gana {d['loc']}", f"Gana {d['vis']}") and l['cuota'] >= 1.5 and l['p'] >= 0.45:
            P.append(dict(nombre=l['seleccion'], c=l['cuota'], p=l['p'], slot=('res',)))
    for r in jug:
        if r['c'] >= 1.5 and r['pe'] >= 0.50 and r['st'] in VOLUMEN + ('anota_o_asiste',) and not r['nota']:
            P.append(dict(nombre=f"{r['sn']} {NOMBRE[r['st']]} {r['k']}+", c=r['c'], p=r['pe'], slot=('j', r['sn'])))
    return sorted(P, key=lambda x: -x['p'])[:46]


def triples(P, minprod=5.3):
    out = []
    for a, b, c in itertools.combinations(P, 3):
        if len({a['slot'], b['slot'], c['slot']}) < 3:
            continue
        prod = a['c'] * b['c'] * c['c']
        if prod < minprod or prod > 14:
            continue
        out.append((a['p'] * b['p'] * c['p'], prod, [a['nombre'], b['nombre'], c['nombre']]))
    out.sort(key=lambda t: -t[0])
    # evita repetir la misma pata mil veces
    res, usos = [], {}
    for t in out:
        if all(usos.get(n, 0) < 3 for n in t[2]):
            res.append(t)
            for n in t[2]:
                usos[n] = usos.get(n, 0) + 1
        if len(res) >= 8:
            break
    return res


def construir(jornada, clave, sofa_path=None):
    d = cargar(jornada, clave, sofa_path)
    loc, vis = d['loc'], d['vis']
    M, S, B, fs = d['modelo'], d['sofa'], d['bet']['betano'], d['fs']
    pr = M['p_resultado']
    tc = tarjetas_sofa(d)
    jug = jugadores(d)

    # probabilidades de tarjetas con Sofascore
    tj = {}
    for r in d['reg']:
        if r['mercado'] != 'tarjetas' or r['ambito'] not in ('total', 'local', 'visitante'):
            continue
        lam = {'total': tc['tot'], 'local': tc['exp_h'], 'visitante': tc['exp_a']}[r['ambito']]
        k = math.floor(f2(r['linea'])) + 1
        pm = pois_ge(lam, k)
        tj[(r['ambito'], r['lado'], f2(r['linea']))] = pm if r['lado'] == 'Más' else 1 - pm

    L = []
    w = L.append
    w(f"# {loc} – {vis} · informe completo por probabilidad")
    w(f"{fs.get('estadio') or S['ev'].get('venue')} · {d['ficha'].get('liga')} · viernes 13-nov-2026 · **14:45 Bogotá** · árbitro {S['ev']['ref']}")
    w(f"Cuotas de Betano leídas {d['bet']['meta']['cuotas_leidas']} (UTC) · alineaciones y jugadores: Sofascore, leído {S['leido']}, predicha, **no confirmada** · **No se colocó ninguna apuesta; la decides tú.**\n")
    w('Criterio de este informe: **probabilidad de que la línea pase**, no valor contra la cuota. El EV y el colchón se muestran como información, no mandan.\n')
    w('## Enfoque de mercados')
    w(d['enfoque'].strip() + '\n')

    w('## 1. Situación y alineaciones')
    w(f"- **Modelo (cuotas + contexto):** gana {loc} {pct(pr['local'])} · empate {pct(pr['empate'])} · gana {vis} {pct(pr['visitante'])}.")
    ob = M['objetivos']
    ol, ov = ob['local'], ob['visitante']
    w(f"- **Esperados del modelo:** goles {ol['g'] + ov['g']:.2f} ({loc} {ol['g']:.2f} · {vis} {ov['g']:.2f}); córners {ol['c'] + ov['c']:.1f}; tarjetas (amarillas) {ol['y'] + ov['y']:.1f}; remates {ol['sh'] + ov['sh']:.1f}; tiros al arco {ol['sot'] + ov['sot']:.1f}; faltas {ol['f'] + ov['f']:.1f}.")
    for l in M.get('contexto', [])[:3]:
        w(f'- {l}')
    sf = S['L']
    w(f"- **Alineación predicha (Sofascore, `confirmed:false`):** {loc} ({sf['h']['form']}): " + ', '.join(sf['h']['xi']) + f". {vis} ({sf['a']['form']}): " + ', '.join(sf['a']['xi']) + '.')
    w(f"- **Bajas / dudas (Sofascore):** {loc}: " + (', '.join(sf['h']['miss']) or 'ninguna') + f" · {vis}: " + (', '.join(sf['a']['miss']) or 'ninguna') + '.')
    try:
        pr_fs = fs['lineups']['probables']
        sof_ap = {apellido(n) for n in S['P']}
        sofs = list(S['P'].keys())
        def esta(nf):
            ap, ini = sep_nombre(nf)
            return any(any(parecido(x, y) and (not ini or norm(sn).split()[0][:1] == ini) for x in ap for y in norm(sn).split()[1:]) for sn in sofs)
        solo_fs = [p['n'] for lado in ('L', 'V') for p in pr_fs[lado] if not esta(p['n'])]
        if solo_fs:
            w('- **En el once de Flashscore pero NO en el de Sofascore (sin historial recogido, no se analizan sus mercados de jugador):** ' + ', '.join(solo_fs) + '.')
        w(f"- **Alineación probable de Flashscore ({fs.get('lineups_leidas')}):** {loc}: " + ', '.join(p['n'] for p in pr_fs['L']) + f" · {vis}: " + ', '.join(p['n'] for p in pr_fs['V']) + '. **Las dos fuentes no coinciden en todo; los jugadores marcados «solo Sofascore» hay que reconfirmarlos con la alineación oficial (≈ 13:45).**')
    except Exception:
        pass
    w(f"- **Árbitro:** {S['ev']['ref']} — últimos {len(tc['ref_serie'])} partidos ({tc['ref_n']} con dato de tarjetas; Sofascore): amarillas por partido " + ', '.join(str(x) if x is not None else '–' for x in tc['ref_serie']) + (f" (promedio {tc['ref_mean']:.1f}). Torneos de la muestra: " + ', '.join(sorted({r[2] for r in S['R']})[:6]) + '. Son, sobre todo, partidos de clubes; en selecciones el promedio puede ser distinto.' if tc['ref_mean'] else '.'))
    w('')

    w('## 2. Resultado, ambos marcan y goles')
    w('| Mercado | Cuota | p modelo | p mercado |')
    w('|---|---|---|---|')
    for l in sorted([x for x in M['lineas'] if x['familia'] in ('resultado', 'ambos') and not x['seleccion'].startswith(('Hándicap', 'Descanso/final'))], key=lambda x: -x['p'])[:14]:
        w(f"| {l['seleccion']} | {l['cuota']} | **{pct(l['p'])}** | {pct(l['p_mercado'])} |")
    hs = sorted([x for x in M['lineas'] if x['seleccion'].startswith('Hándicap') and 0.45 <= x['p'] <= 0.90 and x['cuota'] >= 1.15], key=lambda x: -x['p'])[:6]
    if hs:
        w('\n**Hándicap (45–90 %, cuota ≥ 1.15)**: ' + ' · '.join(f"{x['seleccion'].replace('Hándicap ', '')} @{x['cuota']} → {pct(x['p'])}" for x in hs) + '\n')
    w('\n**Goles (líneas con 40–90 %)**\n')
    w(lineas_equipo(d, 'goles'))

    w('## 3. Córners')
    w(lineas_equipo(d, 'corners'))
    mc = [l for l in M['lineas'] if l['seleccion'].startswith('Más corners')]
    if mc:
        w('«Más córners»: ' + ' · '.join(f"{l['seleccion'].split(': ')[1]} @{l['cuota']} → {pct(l['p'])}" for l in mc) + '\n')

    w('## 4. Estadísticas del partido (remates, tiros al arco, faltas, fueras, saques)')
    algo = False
    for fam, nom in (('remates', 'Remates'), ('al_arco', 'Tiros al arco'), ('faltas', 'Faltas'), ('fueras', 'Fueras de juego'), ('saques_banda', 'Saques de banda'), ('saques_meta', 'Saques de meta')):
        if any(r['mercado'] == fam for r in d['reg']):
            algo = True
            w(f'### {nom}')
            w(lineas_equipo(d, fam, n=7))
    if not algo:
        w('**Betano no ofrece estadísticas de partido (remates, tiros al arco, faltas, fueras, saques) en este encuentro; no se inventan líneas.**\n')

    w('## 5. Tarjetas (Betano cuenta en puntos: amarilla 1, roja 2)')
    w(f"**Datos Sofascore (7 partidos de selección de cada equipo):** {loc} recibe " + ' '.join(str(x) if x is not None else '–' for x in tc['serie_h']) + f" amarillas (prom. {tc['hf']:.1f}); sus rivales {' '.join(str(x) if x is not None else '–' for x in tc['serie_hc'])} (prom. {tc['hc']:.1f}). {vis} recibe " + ' '.join(str(x) if x is not None else '–' for x in tc['serie_a']) + f" (prom. {tc['af']:.1f}); sus rivales {' '.join(str(x) if x is not None else '–' for x in tc['serie_ac'])} (prom. {tc['ac']:.1f}).")
    w(f"**Esperado:** {loc} {tc['exp_h']:.2f} · {vis} {tc['exp_a']:.2f} · total **{tc['tot']:.2f}** (equipos {tc['tot_eq']:.2f}, mezclado 65/35 con el promedio del árbitro {tc['ref_mean']:.1f}). Las rojas casi no cuentan en la muestra.\n")
    w(f"| Línea | Cuota | p con Sofascore (Poisson) | p modelo | p mercado | {loc} | {vis} | Cumple 5/7 |")
    w('|---|---|---|---|---|---|---|---|')
    filas = []
    for r in d['reg']:
        if r['mercado'] == 'tarjetas' and r['ambito'] in ('total', 'local', 'visitante'):
            ps = tj[(r['ambito'], r['lado'], f2(r['linea']))]
            filas.append((ps, r))
    for ps, r in sorted(filas, key=lambda t: -t[0]):
        if 0.30 <= ps <= 0.97:
            w(f"| {r['ambito']} {r['lado']} {r['linea']} | {r['cuota']} | **{pct(ps)}** | {pct(f2(r['p_modelo']))} | {pct(f2(r['p_mercado']) or 0)} | {r['reg_local'] or '—'} | {r['reg_visitante'] or '—'} | {r['cumple_ficha'] or '—'} |")
    tt = [r for r in d['reg'] if r['mercado'] == 'tarjetas' and r['ambito'] == 'total' and r['lado'] == 'Más' and f2(r['cuota'])]
    centro = min(tt, key=lambda r: abs(f2(r['p_mercado']) - 0.5)) if tt else None
    dmax = max((abs(ps - f2(r['p_modelo'])) for ps, r in filas), default=0)
    lect = f"\n**Lectura:** con Sofascore esperamos {tc['tot']:.1f} amarillas; el modelo, {ol['y'] + ov['y']:.1f} (incluye la importancia del partido)" + (f"; y el mercado centra el total en {centro['linea']}." if centro else '.')
    lect += (' Las dos estimaciones están a más de 15 puntos en alguna línea: confianza baja, porque la muestra de selecciones es corta y el árbitro viene de clubes.' if dmax > 0.15 else ' Las dos estimaciones van parecidas (diferencia máxima ' + f'{100 * dmax:.0f}' + ' puntos).')
    w(lect)
    otros = [l for l in M['lineas'] if l['seleccion'].startswith(('Ambos 1+ tarjetas', 'Ambos 2+ tarjetas', 'Más tarjetas'))]
    if otros:
        w('\nOtros mercados de tarjetas (modelo): ' + ' · '.join(f"{l['seleccion']} @{l['cuota']} → {pct(l['p'])}" for l in sorted(otros, key=lambda l: -l['p'])[:8]) + '.')
    tj_j = [r for r in jug if r['st'] == 'tarjeta']
    if tj_j:
        w('\n**Tarjeta individual** (una amarilla en el partido; ninguna suele pasar de ≈ 45 %):\n')
        w(tabla_jug(tj_j, 8))
    w('')

    w('## 6. Jugadores (alineación predicha por Sofascore; ver sección 1)')
    if not jug:
        w('Betano no ofrece líneas de jugadores casables con los once predichos, o no hay historial.')
    for st, nom in (('atajadas', 'Atajadas del portero'), ('al_arco', 'Tiros al arco'), ('remates', 'Remates'), ('faltas', 'Faltas cometidas'), ('entradas', 'Entradas'), ('anota', 'Anota'), ('anota_o_asiste', 'Anota o asiste'), ('asiste', 'Asiste')):
        rr = [r for r in jug if r['st'] == st]
        if rr:
            w(f'### {nom}')
            w(tabla_jug(rr, 10))
            w('')
    vol = [r for r in jug if r['st'] in VOLUMEN and r['c'] >= 1.5 and not r['nota']]
    if vol:
        w('### Las más probables con cuota ≥ 1.50 (útiles para el Boss Builder)')
        w(tabla_jug(vol, 10))
        w('')

    w('## 7. Parejas «cualquiera de los jugadores…»')
    pe = {(r['j'], r['st']): r['pe'] for r in jug if r['k'] == 1}
    fila = []
    for q in B.get('parejas') or []:
        a, b = q['jugadores']
        if (a, q['stat']) in pe and (b, q['stat']) in pe:
            p = 1 - (1 - pe[(a, q['stat'])]) * (1 - pe[(b, q['stat'])])
            fila.append((p, a, b, q['stat'], q['cuota']))
    if fila:
        w('| Pareja | Mercado | Cuota | p estimada (1 − (1−p₁)(1−p₂)) | Mercado (1/cuota) |')
        w('|---|---|---|---|---|')
        for p, a, b, st, c in sorted(fila, reverse=True)[:12]:
            w(f"| {a} o {b} | {NOMBRE[st]} | {c} | **{pct(p)}** | {pct(1 / c)} |")
        w('\nSe suma como si fueran independientes; compañeros de equipo comparten el guion, así que la probabilidad real es algo menor.\n')
    else:
        w('Betano no ofrece parejas en este partido, o los jugadores de las parejas no están en la alineación predicha.\n')

    w('## 8. Combinaciones (Bet Builder): las más probables con 3 patas ≥ 1.50')
    P = patas(d, jug, tj)
    T = triples(P)
    if T:
        w('| Trío | Producto de cuotas | Prob. conjunta (independientes) |')
        w('|---|---|---|')
        for p, prod, nm in T:
            w(f"| {' + '.join(nm)} | {prod:.2f} | **{pct(p)}** |")
        w('\n**Límite:** la probabilidad conjunta supone patas independientes y el producto de cuotas no es el precio real del builder (suele ser menor y cambia con la correlación; en las patas de tarjetas se promedió la estimación Sofascore con la del modelo). Antes de apostar, armar el trío en la página y confirmar que el total siga ≥ 5 con cada pata ≥ 1.50. **Techo realista:** el precio de un builder se parece a la cuota justa de la combinación (≈ 1/p real). Un total ≥ 5 en cuota exige, entonces, que la probabilidad real de las tres patas juntas sea ≲ 20–25 %. Las probabilidades conjuntas de la tabla solo se sostienen si el precio real fuera el producto de cuotas, lo que casi nunca ocurre con patas correlacionadas (remates, tiros al arco y gol del mismo jugador). Por eso, en la página, el total suele quedar por debajo de 5.\n')
    else:
        w('No hay tríos con patas ≥ 1.50, probabilidad ≥ 45 % y producto ≥ 5.3 con las líneas que ofrece Betano.\n')
    bs = M.get('builders') or []
    if bs:
        w('Builders del modelo (misma regla de patas ≥ 1.20, sin Boss Builder):')
        for b in bs[:4]:
            w(f"- {' + '.join(b['patas'])} → p {pct(b['p'])}, cuota justa {b['cuota_justa']}, producto de cuotas {b['producto_cuotas']}")
        w('')

    w('## 9. Qué se verificó y qué no')
    w('- **Lo que Betano no ofrece no se analiza.** Mercados de jugadores solo para los once predichos por Sofascore; los de Flashscore que no están ahí no tienen historial.')
    w('- **Muestra:** últimos 7 partidos de cada jugador (club + selección mezclados; rival y minutos distintos). La «p estimada» mezcla (a) tasa por 90 × minutos esperados (Poisson), (b) X de 7 y (c) la probabilidad implícita del mercado, con pesos elegidos por mí (35/35/30 en volumen: remates, tiros al arco, faltas, entradas, atajadas; 25/15/60 en goles, asistencias y tarjetas, porque 7 partidos son muy poco para eventos raros y el mercado pesa más; en el informe de Serbia–Alemania usé 40/40/20 y 40/20/40, aquí encogí hacia el mercado). Sin calibrar con resultados.')
    w('- **Ajuste por contexto de los jugadores:** favorito ×1,10 en remates/goles, ×0,90 en faltas y tarjetas; no favorito ×0,85 y ×1,10–1,15. Es un supuesto mío.')
    w('- **Tarjetas:** Poisson con esperado de equipos (Sofascore) mezclado con el árbitro; las tarjetas están algo menos dispersas que Poisson, así que las colas pueden sobrestimarse.')
    w('- **Las alineaciones no están confirmadas.** Reconfirmar ≈ 13:45 y releer cuotas antes de apostar.')
    w('- Los criterios de «5 de 7» vienen de tipsters y medios sin resultados verificados.')
    w(f"\nFuentes: Betano (`betano.co/cuotas-de-partido/.../{d['bet']['meta']['betano_id']}`) · Sofascore (`jugadores/{clave}_sofascore.json`) · Flashscore (últimos 7 + directos, `flashscore/{clave}.json`) · `fichas/ficha_{clave}.md` · `informes/{clave}_informe.md`.")
    return '\n'.join(L)


if __name__ == '__main__':
    jornada, clave = sys.argv[1], sys.argv[2]
    texto = construir(jornada, clave, sys.argv[3] if len(sys.argv) > 3 else None)
    os.makedirs(os.path.join(jornada, 'informes_completos'), exist_ok=True)
    out = os.path.join(jornada, 'informes_completos', clave + '.md')
    open(out, 'w', encoding='utf-8').write(texto)
    print(out, len(texto), 'caracteres')
