# -*- coding: utf-8 -*-
"""Informe interactivo v2 de una jornada: tres diseños (A «Tablero», B «Partido a partido», C «Cupón») con el mismo motor.

    python3 recoleccion/informe_v2.py jornadas/2026-11-14 [A|B|C|ABC]

Lee    registro/lineas.csv (todas las líneas, con p, EV y, si ya hay, resultado) + <jornada>/entradas/ + <jornada>/flashscore/
       (las series por partido de cada equipo y los directos: de ahí sale el «X de N» que el HTML recalcula al mover K, N y n mínimo)
       <jornada>/jugadores/*.json (historial por jugador, si se recolectó) · registro/sugerencias.csv · <jornada>/enfoque.md y reanalisis*.md
       <jornada>/balance/ (boletos, patas calificadas, pendientes) · <jornada>/resultados/estado_partidos.json (final / en juego / por jugar)
Escribe <jornada>/informe_v2_A.html, _B.html y _C.html. Autónomos: sin red ni librerías. Solo lectura de lo ya recogido.
Reglas del proyecto: el colchón es informativo y no oculta ninguna línea; «cumple» = al menos K de los últimos N en el/los equipos elegidos
(por defecto 7 de 10, y 5 de 7 si la jornada se recogió con 7 partidos); el EV se informa pero no manda; nada se inventa: lo que falta sale como «sin muestra».
"""
import os, sys, csv, json, glob, re, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ficha as FI
import informe_html as IH
import calificar_jugadores as CJ

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plantillas_v2')
STAT = {'corners': 'c', 'goles': 'g', 'tarjetas': 'y', 'remates': 'sh', 'al_arco': 'sot', 'faltas': 'f', 'fueras': 'off', 'saques_banda': 'ti', 'saques_meta': 'gk'}
MK = {'corners': 'Córners', 'goles': 'Goles', 'tarjetas': 'Tarjetas (pts)', 'remates': 'Remates', 'al_arco': 'Tiros al arco', 'faltas': 'Faltas', 'fueras': 'Fueras de juego',
      'saques_banda': 'Saques de banda', 'saques_meta': 'Saques de meta'}
MKJ = {'jugador:remates': 'Remates', 'jugador:al_arco': 'Tiros al arco', 'jugador:faltas': 'Faltas cometidas', 'jugador:entradas': 'Entradas', 'jugador:anota': 'Anota',
       'jugador:asiste': 'Asiste', 'jugador:anota_o_asiste': 'Anota o asiste', 'jugador:tarjeta': 'Tarjeta', 'jugador:atajadas': 'Atajadas'}
RS = {'cumplió': 'C', 'falló': 'F', 'media ganada': 'MG', 'media perdida': 'MP', 'nula': 'N'}
NOMBRE = {'A': 'A · Tablero (oscuro, filtros a la izquierda, detalle a la derecha)', 'B': 'B · Partido a partido (papel, agrupado por partido en orden de hora)',
          'C': 'C · Cupón (claro, tarjetas y cupón siempre a la vista)'}


def f(x):
    try:
        return round(float(x), 4)
    except (TypeError, ValueError):
        return None


def real(nota):
    m = re.search(r'valor real (-?[\d.]+)', nota or '')
    return float(m.group(1)) if m else None


def serie_equipo(partidos, k):
    """[[a_favor, en_contra, a_favor_1T, en_contra_1T]] más reciente primero; la meta va aparte, alineada."""
    S, M = [], []
    for m in partidos:
        if k == 'g':
            g = m.get('g')
            S.append([g[0], g[1], None, None] if g else [None, None, None, None])
        else:
            s, s1 = (m.get('stats') or {}).get(k), (m.get('stats_1t') or {}).get(k)
            S.append([s[0] if s else None, s[1] if s else None, s1[0] if s1 else None, s1[1] if s1 else None])
        g = m.get('g') or [None, None]
        M.append([m.get('fecha', ''), m.get('rival') or m.get('comp') or '', m.get('v') or '', g[0], g[1]])
    return S, M


def construir(base, variante):
    jor = os.path.basename(os.path.normpath(base))
    filas = [r for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';') if r['jornada'] == jor]
    if not filas:
        raise SystemExit(f'registro/lineas.csv no tiene filas de {jor}: corre antes correr_jornada.py')
    orden = sorted({r['partido']: r['hora_partido'] for r in filas}.items(), key=lambda kv: (kv[1], kv[0]))
    nombres = [n for n, _ in orden]
    idx = {n: i for i, n in enumerate(nombres)}
    # entradas -> slug y equipos
    slug, equipos = {}, {}
    for p in glob.glob(os.path.join(base, 'entradas', '*.json')):
        d = json.load(open(p, encoding='utf8'))
        n = f"{d['local']} - {d['visitante']}"
        slug[n] = os.path.basename(p)[:-5]
        equipos[n] = (d['local'], d['visitante'], d.get('liga', ''))
    estado = {}
    pe = os.path.join(base, 'resultados', 'estado_partidos.json')
    if os.path.exists(pe):
        estado = {k: v for k, v in json.load(open(pe, encoding='utf8')).items() if not k.startswith('_')}
    P, SER, META, nmax, nh = [], {}, {}, 0, 0
    for n, hora in orden:
        i = idx[n]
        loc, vis, liga = equipos.get(n, (n.split(' - ')[0], n.split(' - ')[-1], ''))
        e = estado.get(n, {})
        P.append({'n': n, 'liga': liga or next(r['liga'] for r in filas if r['partido'] == n), 'hora': hora[11:16], 'est': e.get('estado', 'pend'), 'g': e.get('g', [0, 0]), 'min': e.get('min', ''), 'loc': loc, 'vis': vis})
        fp = os.path.join(base, 'flashscore', (slug.get(n) or '') + '.json')
        if not os.path.exists(fp):
            continue
        fs = json.load(open(fp, encoding='utf8'))
        forma, h2h = fs.get('forma', {}), fs.get('h2h', [])
        nmax = max(nmax, len(forma.get('local', [])), len(forma.get('visitante', [])))
        nh = max(nh, len(h2h))
        SER[i], META[i] = {}, {}
        for lado, clave in (('l', 'local'), ('v', 'visitante')):
            lista = forma.get(clave, [])[:FI.N]
            for mk, k in STAT.items():
                s, m = serie_equipo(lista, k)
                SER[i].setdefault(mk, {})[lado] = s
            META[i][lado] = serie_equipo(lista, 'c')[1]
        for mk, k in STAT.items():
            s, _ = serie_equipo(h2h[:FI.N_H2H], k)
            SER[i][mk]['h'] = s
        META[i]['h'] = [[m.get('fecha', ''), m.get('comp', ''), '', (m.get('g') or [None, None])[0], (m.get('g') or [None, None])[1]] for m in h2h[:FI.N_H2H]]
    nmax = nmax or FI.N
    K0 = FI.CUMPLE if nmax >= FI.N else max(1, round(FI.CUMPLE * nmax / FI.N))
    MN0 = FI.MIN_N if nmax >= FI.N else max(1, round(FI.MIN_N * nmax / FI.N))
    L, Jr = [], []
    for r in filas:
        i = idx[r['partido']]
        rs = RS.get(r['resultado'], '')
        if r['mercado'].startswith('jugador:'):
            Jr.append([i, r['mercado'], r['jugador'], 'L' if r['ambito'] == 'local' else 'V', f(r['titular']), f(r['linea']), r['lado'], f(r['cuota']), f(r['p_modelo']), f(r['p_mercado']),
                       f(r['ev_modelo']), rs, real(r['nota']), f(r['esperado']), f(r['colchon'])])
        elif r['mercado'] in STAT and r['lado'] in ('Más', 'Menos') and r['linea'] != '':
            L.append([i, r['mercado'], r['ambito'], r['lado'], f(r['linea']), f(r['cuota']), f(r['esperado']), f(r['colchon']), f(r['p_modelo']), f(r['p_mercado']), f(r['ev_modelo']),
                      r['alerta_modelo'], rs, real(r['nota'])])
    # historial por jugador (Flashscore), casado con el nombre de Betano
    HIS, con_hist = {}, []
    for p in glob.glob(os.path.join(base, 'jugadores', '*.json')):
        sl = os.path.basename(p)[:-5]
        n = next((k for k, v in slug.items() if v == sl), None)
        if n is None:
            continue
        H = json.load(open(p, encoding='utf8'))
        salida = {}
        betano_n = sorted({x[2] for x in Jr if x[0] == idx[n]})
        for fs_n, d in H.items():
            j = CJ.casar_flashscore(fs_n, betano_n)
            if j and d.get('p'):
                salida[j] = [[x[1]] + x[2:11] for x in d['p']]
        if salida:
            HIS[idx[n]] = salida
            con_hist.append(sh_(n))
    # análisis, sugerencias, balance
    enf = ''
    pe_ = os.path.join(base, 'enfoque.md')
    if os.path.exists(pe_):
        enf = IH._md(open(pe_, encoding='utf8').read())
    rean = [{'t': (open(r, encoding='utf8').readline().lstrip('# ').strip() or os.path.basename(r)), 'h': IH._md(''.join(open(r, encoding='utf8').readlines()[1:]))}
            for r in sorted(glob.glob(os.path.join(base, 'reanalisis*.md')))]
    SUG = []
    ps = os.path.join(RAIZ, 'registro', 'sugerencias.csv')
    if os.path.exists(ps):
        for r in csv.DictReader(open(ps, encoding='utf-8-sig'), delimiter=';'):
            if r['fecha_entrega'] != jor:
                continue
            g = 'tarde (reanálisis 14:05/14:12)' if 'tarde' in r['entrega'] else 'mañana (informe de las 23:10)'
            SUG.append([r['hora'] or '', g, r['tipo'], r['nombre'], r['partidos'], f(r['cuota']), f(r['p_estimada']), r['resultado'], (r['detalle_patas'] or '')[:400]])
    BAL = None
    pb = os.path.join(base, 'balance', 'boletos_betano.json')
    if os.path.exists(pb):
        BAL = json.load(open(pb, encoding='utf8'))
        pc = os.path.join(base, 'balance', 'patas_calificadas.json')
        PC = json.load(open(pc, encoding='utf8')) if os.path.exists(pc) else {}
        for b in BAL['boletos']:
            b['pc'] = PC.get(str(b['n']))
        pp = os.path.join(base, 'balance', 'pendientes.json')
        BAL['pendientes'] = json.load(open(pp, encoding='utf8')) if os.path.exists(pp) else []
        BAL.pop('fuente', None)
    estado_txt = open(os.path.join(base, 'ESTADO.md'), encoding='utf8').read() if os.path.exists(os.path.join(base, 'ESTADO.md')) else ''
    ahora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))).strftime('%d-%b %H:%M')
    leidas = max(r['cuotas_leidas'] for r in filas)
    D = {'variante': variante, 'jor': jor, 'titulo': f'Informe de la jornada {jor}', 'sub': f'{len(L):,} líneas de equipo · {len(Jr):,} de jugador · {len(nombres)} partidos · muestra de {nmax} por equipo · hora de Bogotá · solo lectura'.replace(',', '.'),
         'generado': f'Generado {ahora} (Bogotá) · diseño {NOMBRE[variante]} · cuotas más recientes leídas {leidas[:16].replace("T", " ")} UTC', 'N': nmax, 'NH': nh, 'K': K0, 'MN': MN0, 'MK': MK, 'MKJ': MKJ,
         'P': P, 'L': L, 'J': Jr, 'SER': SER, 'META': META, 'HIS': HIS, 'A': {'enfoque': enf, 'rean': rean}, 'SUG': SUG, 'BAL': BAL, 'estado': estado_txt,
         'nota_j': ('Historial por jugador (Flashscore) recolectado solo para: ' + (', '.join(con_hist) if con_hist else 'ningún partido') + '. En los demás partidos las líneas de jugador salen «historial no recolectado». '
                    'Las «nula» son jugadores que no jugaron (Betano anula la línea).')}
    return D


def sh_(n):
    return n.replace(' - ', ' – ')


def pagina(D, variante):
    css = open(os.path.join(PLANT, 'base.css'), encoding='utf8').read() + '\n' + open(os.path.join(PLANT, 'tema_' + variante.lower() + '.css'), encoding='utf8').read()
    js = open(os.path.join(PLANT, 'motor.js'), encoding='utf8').read()
    datos = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    js = js.replace('/*DATA*/', datos, 1)
    return (f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n<title>Informe v2 · {NOMBRE[variante]}</title>\n<style>{css}</style></head><body>\n'
            '<h1 id="titulo"></h1><div class="sub" id="sub"></div><nav id="nav"></nav><div id="app"></div><div id="badge" data-tab="cu" hidden></div>\n<script>' + js + '</script></body></html>\n')


def main(argv):
    base = argv[1] if os.path.isabs(argv[1]) else os.path.join(RAIZ, argv[1])
    vs = (argv[2] if len(argv) > 2 else 'ABC').upper()
    for v in vs:
        D = construir(base, v)
        salida = os.path.join(base, f'informe_v2_{v}.html')
        open(salida, 'w', encoding='utf8').write(pagina(D, v))
        print(f'{salida}: {len(D["L"])} líneas de equipo, {len(D["J"])} de jugador, {os.path.getsize(salida) / 1024:.0f} KB')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    main(sys.argv)
