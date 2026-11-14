# -*- coding: utf-8 -*-
"""Ficha por mercado para los 3 mercados de prueba: CÓRNERS, ESTADÍSTICAS DE PARTIDO y ESTADÍSTICAS DE JUGADORES.

Entrada : una «entrada» del supermodelo (el mismo JSON que usa `python3 -m supermodelo`), con
          ficha.forma (últimos partidos de cada equipo con sus estadísticas), ficha.jugadores_hist,
          betano.lineas / betano.jugadores y, si existe, ficha.h2h (directos con estadísticas).
Salida  : <salida>/ficha_<clave>.json (completo) y ficha_<clave>.md (resumen legible).

Reglas fijas del usuario (12-nov-2026; muestra ampliada el 13-nov-2026):
  * Muestra: últimos 10 partidos de cada equipo, combinados y en cualquier sede, + directos (los que existan, 6 como máximo).
  * Regularidad: cuántas veces de esos 10 se cumplió la línea. Cumple con 7 de 10 o más (n mínimo 7; proporcional al 5 de 7 anterior).
    Los umbrales están en las constantes N, N_H2H, MIN_N y CUMPLE de abajo (único lugar donde cambiarlos).
  * Colchón: esperado por los datos menos la línea de Betano. Es INFORMATIVO: no se descarta ninguna línea por él.
  * Objetivo: probabilidad de que la línea se cumpla, no valor contra Betano.

Uso:  python3 recoleccion/ficha.py <entrada.json> [carpeta_salida]
"""
import glob, json, os, re, sys, unicodedata

N = 10           # partidos por equipo (los últimos oficiales, cualquier sede)
N_H2H = 6        # directos: 6 como máximo (si hay menos, los que haya)
MIN_N = 7        # muestra mínima para poder decir «cumple»
CUMPLE = 7       # veces de N que debe cumplirse la línea
REGLA = (N, MIN_N, CUMPLE)   # la regla vigente; fijar_muestra() la adapta a una jornada recogida con menos partidos


def muestra_de(carpeta):
    """Mayor número de partidos por equipo en las entradas de una jornada (la muestra con la que se recogió). 0 si no hay forma."""
    nmax = 0
    for p in glob.glob(os.path.join(carpeta, '*.json')):
        try:
            forma = ((json.load(open(p, encoding='utf8')).get('ficha') or {}).get('forma') or {})
        except (ValueError, AttributeError):
            continue
        for lado in ('local', 'visitante'):
            nmax = max(nmax, len(forma.get(lado) or []))
    return nmax


def fijar_muestra(nmax):
    """Una jornada recogida con menos partidos que la regla (p. ej. 7 antes del 13-nov) se declara «muestra de nmax» y usa el umbral
    proporcional (7 de 10 -> 5 de 7, n mínimo 5): el mismo cálculo que hace informe_html.py. Con nmax >= 10 (o 0) vale la regla."""
    global N, MIN_N, CUMPLE
    n0, m0, c0 = REGLA
    if nmax and nmax < n0:
        N, MIN_N, CUMPLE = nmax, max(1, round(m0 * nmax / n0)), max(1, round(c0 * nmax / n0))
    else:
        N, MIN_N, CUMPLE = n0, m0, c0
    return N, MIN_N, CUMPLE

# mercado de Betano -> clave de estadística en ficha.forma[].stats  ([a favor, en contra])
MERCADOS = {
    'corners':      ('c',   'Córners'),
    'faltas':       ('f',   'Faltas'),
    'fueras':       ('off', 'Fueras de juego'),
    'saques_banda': ('ti',  'Saques de banda'),
    'saques_meta':  ('gk',  'Saques de meta'),
    'remates':      ('sh',  'Remates'),
    'al_arco':      ('sot', 'Tiros al arco'),
    'goles':        ('g',   'Goles'),
    'tarjetas':     ('y',   'Tarjetas (solo amarillas)'),
}
# avisos que viajan con la ficha (límites honestos de la fuente)
NOTAS = {'tarjetas': 'Betano cuenta en puntos (amarilla 1, roja 2); Flashscore solo trae amarillas, así que la serie queda POR DEBAJO si hubo rojas. '
                     'Tómalo con cuidado en líneas ajustadas.',
         'goles': 'Los goles de la muestra son del partido completo (90 min + descuento); sin goles por tiempo no hay ficha de 1T/2T.'}
GRUPOS = {'corners': ['corners'],
          'partido': ['faltas', 'fueras', 'saques_banda', 'saques_meta', 'remates', 'al_arco']}

# ---------- nombres ----------
def norm(s):
    s = str(s).replace('ı', 'i').replace('İ', 'I').replace('ø', 'o').replace('Ø', 'O').replace('ł', 'l').replace('đ', 'd').replace('ß', 'ss')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9 ]+', ' ', s).strip()

def mismo(a, b):
    ta, tb = norm(a).split(), norm(b).split()
    if not ta or not tb:
        return False
    s, l = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    en = lambda t: any(t == x or (len(t) == 1 and x.startswith(t)) for x in l)
    return all(en(t) for t in s) and (len(s) > 1 or len(l) == 1 or s[-1] == l[-1])

def buscar(nombre, lista):
    c = [x for x in lista if mismo(nombre, x)]
    if len(c) == 1:
        return c[0]
    ex = [x for x in c if norm(x) == norm(nombre)]
    return ex[0] if ex else None

# ---------- series de estadísticas ----------
def media(v):
    return sum(v) / len(v) if v else None

def serie(forma, clave, n=N):
    """[(a_favor, en_contra), ...] de los últimos n partidos (más reciente primero) que traen la estadística."""
    out = []
    for m in (forma or [])[:n]:
        p = (m.get('stats') or {}).get(clave)
        if p and len(p) == 2 and p[0] is not None and p[1] is not None:
            out.append((float(p[0]), float(p[1])))
    return out

def serie_h2h(h2h, clave):
    """Directos con estadísticas: lista de {fecha, comp, stats:{clave:[local_actual, visitante_actual]}} ya orientada."""
    out = []
    for m in (h2h or [])[:N_H2H]:
        p = (m.get('stats') or {}).get(clave)
        if p and len(p) == 2 and p[0] is not None and p[1] is not None:
            out.append((float(p[0]), float(p[1])))
    return out

def cuenta(valores, linea, lado):
    """Veces que la línea se cumplió POR COMPLETO. Más: valor > línea; Menos: valor < línea (las líneas enteras con empate no cuentan).
    Líneas asiáticas (.25 / .75): son dos medias líneas; cuenta solo la victoria completa (Más: valor > línea+0.25; Menos: valor < línea−0.25).
    Con valor justo en medio hay media ganancia o media pérdida: no se cuenta como cumplida."""
    cuarto = round(linea * 4) % 2 == 1
    if lado == 'mas':
        lim = linea + 0.25 if cuarto else linea
        return sum(1 for v in valores if v > lim)
    lim = linea - 0.25 if cuarto else linea
    return sum(1 for v in valores if v < lim)

def reg(x, n):
    return {'x': x, 'n': n, 'txt': f'{x} de {n}', 'cumple': (n >= MIN_N and x >= CUMPLE)}

# ---------- ficha de equipo (córners y partido) ----------
def ficha_estadistica(e, mercado):
    clave, titulo = MERCADOS[mercado]
    F = (e.get('ficha') or {})
    forma = F.get('forma') or {}
    sl, sv = serie(forma.get('local'), clave), serie(forma.get('visitante'), clave)
    sh = serie_h2h(F.get('h2h'), clave)
    lineas = [l for l in (e.get('betano') or {}).get('lineas', []) if l.get('mercado') == mercado]
    res = {'mercado': mercado, 'titulo': titulo, 'n_local': len(sl), 'n_visitante': len(sv), 'n_directos': len(sh)}
    if mercado in NOTAS:
        res['nota'] = NOTAS[mercado]
    if len(sl) < 1 or len(sv) < 1:
        res['aviso'] = 'sin estadísticas suficientes en los últimos partidos'
        res['lineas'] = []
        return res
    Fl, Cl = media([a for a, _ in sl]), media([b for _, b in sl])
    Fv, Cv = media([a for a, _ in sv]), media([b for _, b in sv])
    exp_l, exp_v = (Fl + Cv) / 2, (Fv + Cl) / 2
    res.update(esperado={'local': round(exp_l, 2), 'visitante': round(exp_v, 2), 'total': round(exp_l + exp_v, 2)},
               promedios={'local_a_favor': round(Fl, 2), 'local_en_contra': round(Cl, 2),
                          'visitante_a_favor': round(Fv, 2), 'visitante_en_contra': round(Cv, 2)},
               series={'local': [list(x) for x in sl], 'visitante': [list(x) for x in sv], 'directos': [list(x) for x in sh]})
    tot_l, tot_v, tot_h = [a + b for a, b in sl], [a + b for a, b in sv], [a + b for a, b in sh]
    filas = []
    for l in sorted(lineas, key=lambda z: (z['ambito'], z['linea'])):
        amb, h = l['ambito'], l['linea']
        if amb == 'total':
            exp, vl, vv, vh = exp_l + exp_v, tot_l, tot_v, tot_h
        elif amb == 'local':
            exp, vl, vv, vh = exp_l, [a for a, _ in sl], [b for _, b in sv], [a for a, _ in sh]
        elif amb == 'visitante':
            exp, vl, vv, vh = exp_v, [b for _, b in sl], [a for a, _ in sv], [b for _, b in sh]
        else:   # 1T / 2T: las series son de partido completo
            filas.append({'ambito': amb, 'linea': h, 'mas': {'cuota': l.get('mas')}, 'menos': {'cuota': l.get('menos')},
                          'nota': 'sin estadística por tiempo en la muestra'})
            continue
        fila = {'ambito': amb, 'linea': h, 'esperado': round(exp, 2)}
        for lado, cuota in (('mas', l.get('mas')), ('menos', l.get('menos'))):
            if cuota is None:
                continue
            colch = exp - h if lado == 'mas' else h - exp
            rl, rv = reg(cuenta(vl, h, lado), len(vl)), reg(cuenta(vv, h, lado), len(vv))
            rh = reg(cuenta(vh, h, lado), len(vh)) if vh else None
            fila[lado] = {'cuota': cuota, 'colchon': round(colch, 2), 'reg_local': rl, 'reg_visitante': rv, 'directos': rh,
                          'cumple': bool(rl['cumple'] and rv['cumple'])}
        filas.append(fila)
    res['lineas'] = filas
    return res

# ---------- ficha de jugadores ----------
JUG = {   # stat de Betano -> (clave en jugadores_hist.partidos, descripción)
    'remates': ('remates', 'Remates'), 'al_arco': ('al_arco', 'Tiros al arco'), 'entradas': ('entradas', 'Entradas'),
    'faltas': ('faltas', 'Faltas cometidas'), 'atajadas': ('atajadas', 'Atajadas'),
}
SI_NO = {   # stat de una sola cuota -> función sobre un partido del historial (cumplido sí/no)
    'anota': lambda p: p.get('goles', 0) >= 1,
    'asiste': lambda p: p.get('asist', 0) >= 1,
    'anota_o_asiste': lambda p: (p.get('goles', 0) + p.get('asist', 0)) >= 1,
    'tarjeta': lambda p: p.get('tarjeta', 0) >= 1,
}

def ficha_jugadores(e):
    F = e.get('ficha') or {}
    hist = F.get('jugadores_hist') or {}
    info = {j['nombre']: j for j in e.get('jugadores', [])}
    out = []
    for lin in (e.get('betano') or {}).get('jugadores', []):
        nom, stat = lin['jugador'], lin['stat']
        hn = buscar(nom, list(hist.keys()))
        pj = (hist.get(hn) or {}).get('partidos', [])[:N] if hn else []
        jn = buscar(nom, list(info.keys()))
        titular, minutos = (info[jn].get('titular'), info[jn].get('minutos')) if jn else (None, None)
        base = {'jugador': nom, 'lado': lin.get('lado'), 'stat': stat, 'titular': titular, 'minutos_esperados': minutos,
                'partidos_muestra': len(pj), 'sin_historial': not pj}
        if stat in JUG and lin.get('escalera'):
            clave = JUG[stat][0]
            jugados = [p for p in pj if (p.get('min') or 0) > 0]
            por90 = None
            tot_min = sum(p.get('min') or 0 for p in jugados)
            if tot_min > 0:
                por90 = sum(p.get(clave, 0) or 0 for p in jugados) * 90.0 / tot_min
            esp = (por90 * minutos / 90.0) if (por90 is not None and minutos) else None
            filas = []
            for k, cuota in sorted(lin['escalera'].items(), key=lambda kv: int(kv[0])):
                k = int(k)
                x = sum(1 for p in jugados if (p.get(clave, 0) or 0) >= k)
                filas.append({'minimo': k, 'cuota': cuota, 'reg': reg(x, len(jugados)),
                              'colchon': None if esp is None else round(esp - (k - 0.5), 2)})
            out.append({**base, 'por_90': None if por90 is None else round(por90, 2),
                        'esperado': None if esp is None else round(esp, 2), 'escalones': filas})
        elif stat in SI_NO:
            jugados = [p for p in pj if (p.get('min') or 0) > 0]
            x = sum(1 for p in jugados if SI_NO[stat](p))
            out.append({**base, 'cuota': lin.get('cuota') or (lin.get('escalera') or {}).get('1'), 'reg': reg(x, len(jugados))})
    return out

# ---------- contexto para los criterios que se juzgan (no se calculan) ----------
def contexto(e):
    F = e.get('ficha') or {}
    return {'arbitro': (F.get('arbitro') or {}).get('nombre'), 'clima': (F.get('clima') or {}).get('texto') if isinstance(F.get('clima'), dict) else F.get('clima'), 'tabla': F.get('tabla'),
            'derbi': F.get('derbi'), 'importancia': F.get('importancia'),
            'local': {k: (F.get('local') or {}).get(k) for k in ('estilo', 'motivacion', 'rotacion', 'necesita_ganar', 'perfil_corners')},
            'visitante': {k: (F.get('visitante') or {}).get(k) for k in ('estilo', 'motivacion', 'rotacion', 'necesita_ganar', 'perfil_corners')},
            'bajas': [f"{b.get('jugador')} ({b.get('lado')}, {b.get('posicion')}, {b.get('horas_desde_noticia')} h)" for b in (F.get('bajas') or [])],
            'dudas': F.get('dudas'), 'fuentes': F.get('fuentes')}

def _tabla_txt(t):
    if not t:
        return 'sin dato'
    f = lambda x: f"{x['pos']}.º {x['equipo']} {x['pts']} pts en {x['pj']} PJ (DG {x['dg']:+d}){' · ' + x['grupo'] if x.get('grupo') else ''}"
    return ' | '.join(f"{k}: {f(v)}" for k, v in t.items())

def construir(e):
    return {'encuentro': f"{e.get('local')} - {e.get('visitante')}", 'liga': e.get('liga'), 'fecha': e.get('fecha'),
            'cuotas_leidas': e.get('cuotas_leidas'),
            'regla': {'muestra': f'últimos {N} de cada equipo (cualquier sede) + hasta {N_H2H} directos', 'cumple': f'{CUMPLE} de {N} (n mínimo {MIN_N})', 'directos': f'hasta {N_H2H}',
                      'colchon': 'informativo: esperado − línea'},
            'corners': ficha_estadistica(e, 'corners'),
            'partido': {m: ficha_estadistica(e, m) for m in GRUPOS['partido']},
            'goles': ficha_estadistica(e, 'goles'),
            'tarjetas': ficha_estadistica(e, 'tarjetas'),
            'jugadores': ficha_jugadores(e),
            'contexto': contexto(e)}

# ---------- Markdown ----------
def _f(x, d=1):
    return '—' if x is None else (f'{x:+.{d}f}' if isinstance(x, (int, float)) else str(x))

def _celda(c):
    if not c:
        return '—'
    s = f"@{c['cuota']} · col {_f(c.get('colchon'))} · L {c['reg_local']['txt']} · V {c['reg_visitante']['txt']}"
    if c.get('directos'):
        s += f" · D {c['directos']['txt']}"
    return s + (' ✓' if c['cumple'] else '')

def md_estadistica(r):
    L = [f"### {r['titulo']}"]
    if r.get('nota'):
        L.append(f"_{r['nota']}_")
    if r.get('aviso'):
        return '\n'.join(L + [f"_{r['aviso']}_", ''])
    es, pr = r['esperado'], r['promedios']
    L.append(f"Muestra: local {r['n_local']}, visitante {r['n_visitante']}, directos {r['n_directos']}. "
             f"Esperado: local {es['local']}, visitante {es['visitante']}, **total {es['total']}** "
             f"(local {pr['local_a_favor']} a favor / {pr['local_en_contra']} en contra; visitante {pr['visitante_a_favor']} / {pr['visitante_en_contra']}).")
    for amb in ('total', 'local', 'visitante'):
        fs = [f for f in r['lineas'] if f['ambito'] == amb]
        if not fs:
            continue
        L += ['', f'**{amb}**', '', '| Línea | Más | Menos |', '|---|---|---|']
        for f in fs:
            L.append(f"| {f['linea']} | {_celda(f.get('mas'))} | {_celda(f.get('menos'))} |")
    L.append('')
    return '\n'.join(L)

def md_jugadores(lst):
    L = ['## Jugadores (solo líneas que cumplen la regularidad; el JSON trae todas)', '',
         'Formato: jugador — stat: mínimo @cuota · colchón · X de n (titular p)', '']
    hay = False
    for j in sorted(lst, key=lambda z: (z['lado'] or '', z['jugador'])):
        tit = '' if j['titular'] is None else f" (titular {j['titular']:.2f})"
        if 'escalones' in j:
            for s in j['escalones']:
                if s['reg']['cumple']:
                    hay = True
                    L.append(f"- {j['jugador']} — {j['stat']}: {s['minimo']}+ @{s['cuota']} · col {_f(s['colchon'])} · {s['reg']['txt']}{tit}")
        elif j['reg']['cumple']:
            hay = True
            L.append(f"- {j['jugador']} — {j['stat']}: Sí @{j['cuota']} · {j['reg']['txt']}{tit}")
    if not hay:
        L.append(f'_Ninguna línea de jugador cumple {CUMPLE} de {N} con muestra suficiente._')
    return '\n'.join(L) + '\n'

def resumen(F, cuota_min=1.20):
    """Líneas de equipo que cumplen la regularidad en ambos equipos (con cuota >= cuota_min para no llenar el resumen de líneas de 1.03)."""
    filas = []
    bloques = [('Córners', F['corners'])] + [(r['titulo'], r) for r in F['partido'].values()]
    for tit, r in bloques:
        for f in r.get('lineas', []):
            for lado in ('mas', 'menos'):
                c = f.get(lado)
                if c and c.get('cumple') and c['cuota'] >= cuota_min:
                    filas.append((tit, f['ambito'], lado.capitalize(), f['linea'], c['cuota'], c['colchon'], c['reg_local']['txt'], c['reg_visitante']['txt']))
    return filas

def md_resumen(F):
    filas = resumen(F)
    L = [f'## Resumen: líneas de equipo que cumplen {CUMPLE} de {N} en AMBOS equipos (cuota ≥ 1.20; las demás están en las tablas)', '']
    if not filas:
        return '\n'.join(L + ['_Ninguna._', ''])
    L += ['| Mercado | Ámbito | Línea | Cuota | Colchón | Local | Visitante |', '|---|---|---|---|---|---|---|']
    for t, a, lado, h, q, col, rl, rv in sorted(filas, key=lambda z: (z[0], z[1], z[4])):
        lado = {'Mas': 'Más'}.get(lado, lado)
        L.append(f'| {t} | {a} | {lado} {h} | {q} | {_f(col)} | {rl} | {rv} |')
    return '\n'.join(L + [''])

def markdown(F):
    L = [f"# Ficha — {F['encuentro']}", f"{F['liga']} · {F['fecha']} · cuotas leídas: {F.get('cuotas_leidas')}", '',
         f"Reglas: muestra = {F['regla']['muestra']}; cumple = {F['regla']['cumple']}; colchón = {F['regla']['colchon']}.",
         'Lectura: «col» = colchón; «L»/«V» = veces que se cumplió la línea en los últimos partidos del local/visitante; «D» = directos; ✓ = cumple en ambos.', '',
         md_resumen(F), '## Córners', '', md_estadistica(F['corners']), '## Estadísticas del partido', '']
    for m in GRUPOS['partido']:
        L.append(md_estadistica(F['partido'][m]))
    L += ['## Goles y tarjetas (para los agentes de goles-resultado y tarjetas; no entran en el ranking)', '',
          md_estadistica(F['goles']), md_estadistica(F['tarjetas'])]
    L.append(md_jugadores(F['jugadores']))
    c = F['contexto']
    L += ['## Contexto para juzgar los criterios no numéricos', '', f"- Árbitro: {c['arbitro']}; derbi: {c['derbi']}; importancia: {c['importancia']}; clima: {c['clima']}",
          f"- Tabla (Flashscore, antes de la jornada): {_tabla_txt(c.get('tabla'))}",
          f"- Local: {c['local']}", f"- Visitante: {c['visitante']}", f"- Bajas: {'; '.join(c['bajas']) or 'ninguna anotada'}",
          f"- Dudas: {c['dudas']}", '']
    return '\n'.join(L)

def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    ruta = argv[1]
    sal = argv[2] if len(argv) > 2 else os.path.dirname(os.path.abspath(ruta))
    e = json.load(open(ruta, encoding='utf8'))
    fijar_muestra(muestra_de(os.path.dirname(os.path.abspath(ruta))))   # muestra real de la jornada (las entradas de la misma carpeta)
    F = construir(e)
    clave = os.path.splitext(os.path.basename(ruta))[0]
    os.makedirs(sal, exist_ok=True)
    json.dump(F, open(os.path.join(sal, f'ficha_{clave}.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    open(os.path.join(sal, f'ficha_{clave}.md'), 'w', encoding='utf8').write(markdown(F))
    print(f'ficha_{clave}.md / .json en {sal}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
