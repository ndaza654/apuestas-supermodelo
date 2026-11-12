# -*- coding: utf-8 -*-
"""Arma, para cada partido del 12-nov, la ENTRADA del supermodelo (cuotas de Betano + ficha de contexto + historial) y un
CONTEXTO en Markdown con los hechos y sus fuentes. Uso: python3 construir.py  → pub/entradas/<clave>.json, pub/contexto/<clave>.md, pub/plan.json"""
import json, os, re, sys, datetime as dt
sys.path.insert(0, '/home/claude/nov12')
import lib, config as CF
BASE = '/home/claude/nov12'; PUB = BASE + '/pub'
REFS, METEO = lib.refs(), lib.meteo()
POS = {'G': 'Portero', 'D': 'Defensa', 'M': 'Mediocampista', 'F': 'Delantero'}
SEL = ['UEFA Nations League', 'World Cup Qual. UEFA', 'EURO, Qualification', 'EURO', 'International Friendly Games', 'FIFA World Cup', "UEFA Women's Champions League", "Women's Euro"]
MKT = {'c': 'corners', 'sh': 'remates', 'sot': 'al_arco', 'f': 'faltas', 'y': 'tarjetas', 'off': 'fueras', 'gk': 'saques_meta', 'ti': 'saques_banda'}
ES = lambda n: CF.NOMBRES.get(n, n)

def media_torneo(prefijo):
    """Tarjetas (puntos Betano) y córners por partido en la muestra recolectada de un torneo (partidos únicos)."""
    vistos, ys, cs = set(), [], []
    for k in CF.P:
        S = lib.sofa(k)
        if not S: continue
        for sd, eq in (('H', S['home']), ('A', S['away'])):
            for m in S['forma'][sd]:
                if not m['comp'].startswith(prefijo): continue
                idp = (m['fecha'], tuple(sorted([eq, m['rival']])))
                if idp in vistos: continue
                vistos.add(idp)
                s = lib.stats_modelo(m)
                if 'y' in s: ys.append(sum(s['y']))
                if 'c' in s: cs.append(sum(s['c']))
    return (lib.media(ys), len(ys), lib.media(cs), len(cs))

def arbitro(cfg, S):
    r = S.get('ref') if S else None
    if not r: return {'nombre': '', 'amarillas_por_partido': None, 'rojas_por_partido': None, 'tarjetas_por_partido': None, 'partidos': None, 'media_liga': None}, 'Árbitro: sin dato publicado.'
    d = REFS.get(cfg.get('ref') or '', {})
    n = sum(d[t]['partidos'] for t in SEL if t in d); am = sum(d[t]['amarillas'] for t in SEL if t in d); ro = sum(d[t]['rojas'] + d[t]['dobles'] for t in SEL if t in d)
    fem = 'Champions League' in cfg['liga'] and 'Femenina' in cfg['liga']
    ml, nml, _, _ = media_torneo("UEFA Women's Champio" if fem else 'UEFA Nations League')
    car = f"{r['amarillas'] / max(r['partidos'], 1):.2f} amarillas y {(r['rojas'] + r['dobles']) / max(r['partidos'], 1):.2f} rojas por partido en {r['partidos']} partidos de toda su carrera"
    if n >= 5 and not fem:
        a = dict(nombre=f"{r['nombre']} ({r['pais']})", amarillas_por_partido=round(am / n, 2), rojas_por_partido=round(ro / n, 2), tarjetas_por_partido=round((am + 2 * ro) / n, 2), partidos=n,
                 media_liga=ml, nota=f"Promedio en {n} partidos " + ('de UWCL y Eurocopa femenina' if fem else 'de selecciones (Liga de Naciones, eliminatorias, Eurocopa, amistosos)') + f"; carrera: {car}. Media de referencia = {ml} puntos de tarjeta por partido en {nml} partidos de la muestra recolectada del torneo (no es la media oficial).")
        nl = d.get('UEFA Nations League')
        txt = (f"Árbitro {a['nombre']}: {a['amarillas_por_partido']} amarillas y {a['rojas_por_partido']} rojas por partido en {n} partidos de este tipo"
               + (f" ({nl['amarillas'] / nl['partidos']:.1f} amarillas en {nl['partidos']} de Liga de Naciones)" if nl and nl['partidos'] else '') + f"; en toda su carrera {car}. Referencia de la muestra: {ml} puntos por partido.")
    else:
        a = dict(nombre=f"{r['nombre']} ({r['pais']})", amarillas_por_partido=round(r['amarillas'] / max(r['partidos'], 1), 2), rojas_por_partido=round((r['rojas'] + r['dobles']) / max(r['partidos'], 1), 2),
                 partidos=None, media_liga=None, nota='Solo promedio de carrera (otra competición): sin efecto en el modelo.')
        a['tarjetas_por_partido'] = None
        txt = f"Árbitro {a['nombre']}: {car} (sin muestra suficiente en este torneo: no entra al modelo)."
    return a, txt

def clima(cfg):
    hs = METEO.get(cfg.get('meteo') or '', [])
    if not hs: return {'lluvia': None, 'viento_fuerte': False, 'temperatura': None}, 'Clima: sin dato.'
    mm = max(h['lluvia_mm'] for h in hs); v = max(h['viento'] for h in hs); rf = max(h['rafagas'] for h in hs); t = round(sum(h['temp'] for h in hs) / len(hs), 1)
    ll = 'fuerte' if mm >= 1.5 else ('moderada' if mm >= 0.5 else ('ligera' if mm > 0 else 'no'))
    c = dict(lluvia=ll, viento_fuerte=bool(v >= 30 or rf >= 55), temperatura=t, lluvia_mm_h=mm, viento_kmh=v, rafagas_kmh=rf, humedad=hs[0]['humedad'], fuente='open-meteo (pronóstico leído 12-nov 00:35)')
    return c, f"Clima a la hora del partido ({cfg['meteo'].split(' (')[0]}): {t} °C, lluvia {ll} (máx. {mm} mm/h), viento {v:.0f} km/h con ráfagas de {rf:.0f}, humedad {hs[0]['humedad']} %."

def perfil(ms, media_cr):
    of = [m for m in ms if lib.OFICIAL(m)] or ms
    R = lib.resumen_forma(of)
    est = []
    pos = R.get('pos', (None,))[0]
    if pos is not None:
        if pos >= 58: est.append('posesion')
        if pos <= 43: est += ['bloque_bajo', 'contragolpe']
    cr = R.get('cr', (None,))[0]
    if cr is not None and media_cr and cr >= 1.2 * media_cr: est.append('centros')
    xg = [m['xg'][0] - m['g'][0] for m in of if 'xg' in m and None not in m['xg']]
    ult = dt.date.fromisoformat(ms[0]['fecha']) if ms else None
    d = dict(estilo=est, estilo_nuevo=False, marcador='normal', rotacion=False, motivacion='normal', necesita_ganar=False,
             perfil_corners=dict(centros_pj=cr, centros_media_liga=media_cr, territorio_pct=None), propositivo=(pos >= 52) if pos is not None else None,
             dias_descanso=(dt.date(2026, 11, 12) - ult).days if ult else None, viaje_largo=False, fecha_fifa=True, xg_menos_goles=lib.media(xg))
    return d, R

def rachas(ms):
    v = b = 0
    for m in ms:
        if m['g'][0] > m['g'][1]: v += 1
        else: break
    for m in ms:
        if m['g'][0] > 0 and m['g'][1] > 0: b += 1
        else: break
    return dict(btts_seguidos=b, victorias_seguidas=v)

def hay_linea_equipo(bet, mercado, lado):
    return any(l['mercado'] == mercado and l['ambito'] == lado and l.get('mas') and l.get('menos') and round(l['linea'] % 1, 2) == 0.5 for l in bet.get('lineas', []))

def objetivos(bet, RL, RV):
    """Medias por equipo desde la forma (a favor del equipo y en contra del rival) SOLO para lo que Betano no cotiza por equipo."""
    out = {'local': {}, 'visitante': {}}
    for s, mk in MKT.items():
        for lado, A, Bv in (('local', RL, RV), ('visitante', RV, RL)):
            if hay_linea_equipo(bet, mk, lado): continue
            a, b = A.get(s), Bv.get(s)
            if a and b and a[2] >= 3 and b[2] >= 3: out[lado][s] = round((a[0] + b[1]) / 2, 2)
    return out

def nombres_xi(txt):
    txt = re.sub(r'\(.*?\)', '', txt)
    return [x.strip() for x in re.split(r'[;,]', txt) if x.strip()]

def jugadores(cfg, bet, S):
    """Titularidad de cada jugador con línea en Betano, a partir de las alineaciones PROBABLES de varias fuentes."""
    info, log = [], []
    por_lado = {'local': [], 'visitante': []}
    porteros = set()
    for j in bet.get('jugadores', []):
        if j['jugador'] not in por_lado[j['lado']]: por_lado[j['lado']].append(j['jugador'])
        if j['stat'] == 'atajadas': porteros.add(j['jugador'])
    for p in bet.get('parejas', []):
        pass
    for lado, sd in (('local', 'H'), ('visitante', 'A')):
        nombres = por_lado[lado]
        fuentes = {}
        if S and S['xi'][sd]: fuentes[CF.SF] = [p['nombre'] for p in S['xi'][sd] if p['xi']]
        for f, txt in (cfg['xi'].get(lado) or {}).items(): fuentes[f] = nombres_xi(txt)
        cuenta = {n: 0 for n in nombres}
        for f, lst in fuentes.items():
            for x in lst:
                b = lib.buscar(x, nombres)
                if b: cuenta[b] += 1
                elif nombres: log.append(f'{lado}: «{x}» ({f.split(" (")[0]}) no tiene línea en Betano o no se pudo emparejar')
        miss = {m['nombre']: m for m in (S['miss'][sd] if S else [])}
        jh = {p['nombre']: p for p in (S['jh'][sd] if S else [])}
        nf = len(fuentes)
        for n in nombres:
            k = cuenta[n]
            if nf == 0:
                h = lib.buscar(n, list(jh))
                if h:
                    ps = [p for p in jh[h]['partidos'] if p['i'] < 6]
                    tit = round(0.15 + 0.7 * sum(p['min'] >= 60 for p in ps) / 6, 2)
                else: tit = 0.2
            else:
                fr = k / nf
                tit = (0.9 if nf >= 3 else 0.85 if nf == 2 else 0.7) if fr == 1 else (0.6 if fr >= 0.5 else (0.35 if fr > 0 else 0.12))
            d = dict(nombre=n, lado=lado, titular=tit, minutos=90 if n in porteros else 82, fuentes_xi=f'{k}/{nf}')
            mm = lib.buscar(n, list(miss))
            if any(lib.mismo(n, x) for x in cfg.get('fuera', [])) or (mm and miss[mm]['tipo'] == 'missing'):
                d.update(titular=0.0, minutos=0, fuera=True, motivo=(miss[mm]['motivo'] if mm else 'baja según las noticias'))
            elif mm and miss[mm]['tipo'] == 'doubtful':
                d.update(titular=round(tit * 0.4, 2), duda=miss[mm]['motivo'])
            info.append(d)
    return info, log

def hist_jugadores(bet, S):
    out = {}
    if not S: return out
    nombres = {j['jugador'] for j in bet.get('jugadores', [])}
    for sd in ('H', 'A'):
        F = S['forma'][sd]
        for p in S['jh'][sd]:
            b = lib.buscar(p['nombre'], sorted(nombres))
            if not b: continue
            ps = []
            for x in p['partidos']:
                m = F[x['i']] if x['i'] < len(F) else {}
                d = {k: (int(v) if float(v).is_integer() else v) for k, v in x.items() if k != 'i'}
                d.update(fecha=m.get('fecha'), rival=m.get('rival'), comp=m.get('comp'))
                ps.append(d)
            out[b] = dict(pos=POS.get(p['pos'], p['pos']), partidos=ps, nota='Últimos partidos con su selección/club en Sofascore (no todos sus partidos de club).')
    return out

def construir(key):
    cfg = CF.P[key]; S = lib.sofa(key)
    pb = f'{BASE}/betano/{key}.json'
    B = json.load(open(pb, encoding='utf8')) if os.path.exists(pb) else None
    bet = B['betano'] if B else dict(lineas=[], unicos=[], jugadores=[], parejas=[])
    loc, vis = (B['meta']['local'], B['meta']['visitante']) if B else (ES(S['home']), ES(S['away']))
    todos_cr = [m['cr'][0] for k in CF.P for sd in ('H', 'A') for m in ((lib.sofa(k) or {'forma': {'H': [], 'A': []}})['forma'][sd]) if 'cr' in m and m['cr'][0] is not None]
    mcr = lib.media(todos_cr)
    PL, RL = perfil(S['forma']['H'], mcr); PV, RV = perfil(S['forma']['A'], mcr)
    PL.update(cfg.get('loc') or {}); PV.update(cfg.get('vis') or {})
    club = 'Champions' in cfg['liga']
    if club: PL['fecha_fifa'] = PV['fecha_fifa'] = False
    arb, arb_txt = arbitro(cfg, S); cl, cl_txt = clima(cfg)
    info, log = jugadores(cfg, bet, S)
    forma = {}
    for lado, sd in (('local', 'H'), ('visitante', 'A')):
        ms = [m for m in S['forma'][sd] if lib.OFICIAL(m) and 'sh' in m]
        if len(ms) < 4: ms = [m for m in S['forma'][sd] if 'sh' in m or 'c' in m]
        forma[lado] = [dict(v=m['v'], fecha=m['fecha'], rival=ES(m['rival']), comp=m['comp'], stats=lib.stats_modelo(m)) for m in ms]
    emp5 = sum(1 for h in S['h2h'][:5] if h['marcador'].split('-')[0] == h['marcador'].split('-')[1])
    est = S.get('estadio') or {}
    estadio = f"{est.get('nombre', '')} ({est.get('ciudad', '')})" if est.get('nombre') else None
    if key == 'costa-de-marfil-gambia': estadio = 'Stade de la Paix (Bouaké)'
    ficha = dict(derbi=False, importancia=cfg['importancia'], eliminatoria=cfg.get('eliminatoria'), ultimo_tabla=None, arbitro=arb, clima=cl, fecha_fifa=not club,
                 local=PL, visitante=PV, bajas=cfg['bajas'], rachas={'local': rachas(S['forma']['H']), 'visitante': rachas(S['forma']['A'])}, h2h_empates_ult5=emp5,
                 consenso_publico=None, info_tardia=[], estadio=estadio, forma=forma, jugadores_hist=hist_jugadores(bet, S), frescos=[],
                 fuentes=['Betano.co (API de la página del partido, todas las pestañas)', 'Sofascore (API: evento, alineación probable, bajas, forma con estadísticas, árbitro, tabla)', 'open-meteo.com (clima)'] + cfg['fuentes'],
                 dudas=cfg['dudas'] + log[:12])
    # ---- bloque de datos para el informe HTML (lo demás del informe lo escribe la fase 2 después del análisis)
    pf = S.get('pf') or [{}, {}]
    letras = {S['home']: list(pf[0].get('forma', '')), S['away']: list(pf[1].get('forma', ''))}
    tabla = [[r['pos'], ES(r['equipo']), r['pj'], f"{r['g']}-{r['e']}-{r['p']}", f"{r['gf']}:{r['gc']}", f"{r['gf'] - r['gc']:+d}", r['pts'], letras.get(r['equipo'], [])] for r in S['tabla']]
    h2h = [[h['fecha'], h['comp'], f"{ES(h['local'])} – {ES(h['visitante'])}", h['marcador'].replace('-', '–')] for h in reversed(S['h2h'])]
    formas = []
    for nom, sd in ((loc, 'H'), (vis, 'A')):
        rows = []
        for m in S['forma'][sd][:10]:
            g = m['g']; res = 'W' if g[0] > g[1] else ('L' if g[0] < g[1] else 'D')
            rows.append([m['fecha'], m['comp'], f"{'vs' if m['v'] == 'H' else 'en'} {ES(m['rival'])}", f"{int(g[0])}–{int(g[1])}", res])
        formas.append([f'{nom}: últimos {len(rows)} partidos', rows])
    def al(lado, sd, nom):
        fs = dict(cfg['xi'].get(lado) or {})
        if S['xi'][sd]: fs[CF.SF + (f" · {S['form_xi'][0 if sd == 'H' else 1]}" if S['form_xi'][0 if sd == 'H' else 1] else '')] = ', '.join(p['nombre'] for p in S['xi'][sd] if p['xi'])
        if not fs: return None
        bj = '; '.join(f"{m['nombre']} ({'fuera' if m['tipo'] == 'missing' else 'duda'}: {m['motivo'].replace('_', ' ')})" for m in S['miss'][sd])
        return dict(titulo=f'{nom} · alineación PROBABLE (no confirmada)', texto=' ‖ '.join(f'{f}: {t}' for f, t in fs.items()), bajas=('Bajas y dudas: ' + bj) if bj else '')
    alin = {k: v for k, v in (('local', al('local', 'H', loc)), ('visitante', al('visitante', 'A', vis))) if v}
    def linea_forma(nom, R, n):
        f = lambda k, t: (f"{t} {R[k][0]:g} a favor / {R[k][1]:g} en contra" if k in R else None)
        partes = [x for x in (f('g', 'goles'), f('xg', 'xG'), f('sh', 'remates'), f('sot', 'al arco'), f('c', 'córners'), f('y', 'amarillas'), f('f', 'faltas'), f('off', 'fueras de lugar'), f('cr', 'centros')) if x]
        return f"{nom}, medias de sus últimos partidos oficiales con estadística ({n}): " + '; '.join(partes) + (f"; posesión {R['pos'][0]:g} %" if 'pos' in R else '') + '.'
    nL = len([m for m in S['forma']['H'] if lib.OFICIAL(m)]); nV = len([m for m in S['forma']['A'] if lib.OFICIAL(m)])
    datos = [cfg['juega'], arb_txt, cl_txt, linea_forma(loc, RL, nL), linea_forma(vis, RV, nV)] + cfg['datos']
    informe = dict(titulo_pagina=f'{loc} – {vis}', tabla=tabla, h2h=h2h, formas=formas, datos=datos)
    if alin: informe['alineaciones'] = alin
    ent = dict(local=loc, visitante=vis, liga=cfg['liga'], fecha=f"2026-11-12 {cfg['hora']}", betano=bet, jugadores=info, ficha=ficha, informe=informe,
               estadio=(estadio or '') + f" · {cfg['hora']} hora de Bogotá", cuotas_leidas=('Cuotas de Betano leídas el 12-nov 00:05 (Bogotá) · ' + str(B['meta']['n_mercados']) + ' mercados en la página') if B else 'SIN CUOTAS DE BETANO (el partido no estaba publicado)')
    ob = objetivos(bet, RL, RV)
    if ob['local'] or ob['visitante']: ent['objetivos'] = ob; ent['objetivos_nota'] = 'Medias por equipo sacadas de la forma (a favor propio + en contra del rival) SOLO para estadísticas que Betano no cotiza por equipo en este partido.'
    os.makedirs(PUB + '/entradas', exist_ok=True); os.makedirs(PUB + '/contexto', exist_ok=True)
    json.dump(ent, open(f'{PUB}/entradas/{key}.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    # ---- contexto en Markdown
    fam = {}
    for l in bet['lineas']: fam[l['mercado']] = fam.get(l['mercado'], 0) + 1
    M = [f'# {loc} – {vis} · contexto recolectado (12-nov-2026)', '', f"**{cfg['liga']}** · jueves 12-nov, {cfg['hora']} hora de Bogotá · {estadio or 'estadio sin dato'}", '',
         '## Qué se juega', cfg['juega'], '', '## Mercados que ofrece Betano en este partido (leídos 12-nov 00:05)']
    if B:
        M += [f"- {B['meta']['n_mercados']} mercados en la página. Líneas Más/Menos guardadas: " + ', '.join(f'{k} {v}' for k, v in fam.items()) + '.',
              '- Mercados únicos: ' + ', '.join(sorted({u['mercado'] + (f" {u.get('stat', '')}" if u.get('stat') else '') for u in bet['unicos']})) + '.',
              f"- Jugadores con línea: {len({j['jugador'] for j in bet['jugadores']})} ({', '.join(sorted({j['stat'] for j in bet['jugadores']})) or 'ninguno'}). Parejas «cualquiera de los jugadores…»: {len(bet['parejas'])}."]
    else: M += ['- **Betano no tenía el partido publicado: no hay cuotas.**']
    M += ['', '## Árbitro y clima', '- ' + arb_txt, '- ' + cl_txt, '', '## Tabla', '| # | Equipo | PJ | G-E-P | Goles | Pts |', '|---|---|---|---|---|---|']
    M += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[6]} |" for r in tabla]
    M += ['', '## Forma (medias a favor / en contra)', '- ' + linea_forma(loc, RL, nL), '- ' + linea_forma(vis, RV, nV),
          f"- Estilo inferido de esas medias (no confirmado): {loc}: {', '.join(PL['estilo']) or 'sin rasgo marcado'}; {vis}: {', '.join(PV['estilo']) or 'sin rasgo marcado'}. Media de centros de la muestra: {mcr}.", '']
    for nom, sd in ((loc, 'H'), (vis, 'A')):
        M += [f'### {nom}: últimos partidos', '| Fecha | Torneo | C/F | Rival | Goles | 1T | xG | Remates | Al arco | Córners (1T) | Faltas | Amarillas (1T) | Rojas | Fueras | Centros | Posesión |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for m in S['forma'][sd]:
            p = lambda k: ('–'.join(f'{x:g}' for x in m[k]) if k in m and None not in m[k] else '')
            M.append(f"| {m['fecha']} | {m['comp']} | {'C' if m['v'] == 'H' else 'F'} | {ES(m['rival'])} | {p('g')} | {p('ht')} | {p('xg')} | {p('sh')} | {p('sot')} | {p('c')} ({p('c1')}) | {p('f')} | {p('y')} ({p('y1')}) | {p('r')} | {p('off')} | {p('cr')} | {m.get('pos', '')} |")
        M.append('')
    M += ['## Enfrentamientos directos'] + [f"- {h[0]} · {h[1]} · {h[2]} {h[3]}" for h in h2h] + ['']
    M += ['## Bajas'] + [f"- {b['jugador']} ({b['lado']}, {b['posicion']}): {b.get('motivo', '')}{'' if b['confirmada'] else ' — sin confirmar'}" for b in cfg['bajas']] or ['- Sin bajas informadas.']
    M += ['- Sofascore: ' + '; '.join(f"{m['nombre']} ({'fuera' if m['tipo'] == 'missing' else 'duda'}, {m['motivo'].replace('_', ' ')})" for sd in ('H', 'A') for m in S['miss'][sd])] if (S['miss']['H'] or S['miss']['A']) else []
    M += ['', '## Alineaciones probables (no confirmadas)']
    for lado, nom in (('local', loc), ('visitante', vis)):
        if lado in alin: M += [f"- **{nom}:** " + alin[lado]['texto']]
        else: M += [f'- **{nom}:** sin alineación probable en las fuentes consultadas.']
    if info:
        M += ['', '### Titularidad estimada de los jugadores con línea en Betano', 'Regla: en todas las fuentes 0,85–0,9 · en la mitad o más 0,6 · en alguna 0,35 · en ninguna 0,12 · baja = fuera. Sin fuentes: según sus minutos en los últimos 6 partidos.']
        for lado, nom in (('local', loc), ('visitante', vis)):
            js = sorted([j for j in info if j['lado'] == lado], key=lambda j: -j['titular'])
            M.append(f"- **{nom}:** " + ', '.join(f"{j['nombre']} {'FUERA' if j.get('fuera') else j['titular']}" for j in js))
    M += ['', '## Datos sueltos'] + [f'- {d}' for d in cfg['datos']] + ['', '## Dudas (lo que no se pudo confirmar)'] + [f'- {d}' for d in ficha['dudas']] + ['', '## Fuentes'] + [f'- {f}' for f in ficha['fuentes']]
    open(f'{PUB}/contexto/{key}.md', 'w', encoding='utf8').write('\n'.join(M) + '\n')
    return dict(clave=key, orden=cfg['orden'], partido=f'{loc} – {vis}', hora_bogota=cfg['hora'], liga=cfg['liga'], entrada=f'entradas/{key}.json', contexto=f'contexto/{key}.md',
                betano=bool(B), mercados_betano=B['meta']['n_mercados'] if B else 0, jugadores_con_linea=len(info), parejas=len(bet['parejas']), avisos_emparejamiento=len(log))

if __name__ == '__main__':
    plan = []
    for k in sorted(CF.P, key=lambda k: CF.P[k]['orden']):
        if lib.sofa(k) is None: print('sin datos de Sofascore:', k); continue
        r = construir(k); plan.append(r)
        print(f"{r['orden']:2d} {r['hora_bogota']} {r['partido']:38s} betano={r['betano']} mercados={r['mercados_betano']:3d} jug={r['jugadores_con_linea']:2d} parejas={r['parejas']:2d} avisos={r['avisos_emparejamiento']}")
    json.dump(dict(estado='recolección terminada', actualizado=dt.datetime.now().isoformat(timespec='minutes'), nota='Horas en Bogotá (UTC−5). Analizar en este orden.', partidos=plan),
              open(PUB + '/plan.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
