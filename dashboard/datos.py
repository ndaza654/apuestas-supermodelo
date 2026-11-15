# -*- coding: utf-8 -*-
"""Arma el «bundle» de datos del dashboard a partir de lo que ya hay en el repo (solo lectura; sin red).
Cada tabla es una lista de listas (columnas fijas) para que el HTML sea pequeño. La fuente de verdad sigue siendo
registro/*.csv y jornadas/*/…; este módulo nunca escribe en ellos. Lo que falta se deja en null: no se inventa."""
import os, sys, csv, json, glob, re, datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'recoleccion'))
import ficha as FI
import calificar_jugadores as CJ

STAT = {'corners': 'c', 'goles': 'g', 'tarjetas': 'y', 'remates': 'sh', 'al_arco': 'sot', 'faltas': 'f', 'fueras': 'off', 'saques_banda': 'ti', 'saques_meta': 'gk'}
RS = {'cumplió': 'C', 'falló': 'F', 'media ganada': 'MG', 'media perdida': 'MP', 'nula': 'N'}


def f(x, nd=4):
    try:
        return round(float(x), nd)
    except (TypeError, ValueError):
        return None


def real(nota):
    m = re.search(r'valor real (-?[\d.]+)', nota or '')
    return float(m.group(1)) if m else None


def rd(p, enc='utf-8-sig'):
    return list(csv.DictReader(open(p, encoding=enc), delimiter=';'))


def serie(partidos, k):
    S, M = [], []
    for m in partidos:
        if k == 'g':
            g = m.get('g')
            S.append([g[0], g[1], None, None] if g else [None] * 4)
        else:
            s, s1 = (m.get('stats') or {}).get(k), (m.get('stats_1t') or {}).get(k)
            S.append([s[0] if s else None, s[1] if s else None, s1[0] if s1 else None, s1[1] if s1 else None])
        g = m.get('g') or [None, None]
        M.append([m.get('fecha', ''), m.get('rival') or m.get('comp') or '', m.get('v') or '', g[0], g[1]])
    return S, M


def jug_resultado(path, idx):
    """jugadores_resultado_*.txt -> {pi: {jugador: [min,rem,sot,g,a,f,ent,ata,am,ro]}}"""
    out, cur = {}, None
    if not os.path.exists(path):
        return out
    for ln in open(path, encoding='utf8'):
        ln = ln.rstrip('\n')
        if ln.startswith('#'):
            cur = idx.get(ln[1:].strip())
            if cur is not None:
                out.setdefault(cur, {})
        elif ln.startswith('X|') and cur is not None:
            p = ln.split('|')
            v = [int(x) if x.lstrip('-').isdigit() else 0 for x in p[2:]]
            v += [0] * (11 - len(v))
            out[cur][p[1]] = [v[0], v[1], v[2], v[3], v[4], v[5], v[7], v[8], v[9], v[10]]
    return out


def construir():
    filas = rd(os.path.join(RAIZ, 'registro', 'lineas.csv'))
    jors = sorted({r['jornada'] for r in filas})
    claves = sorted({(r['jornada'], r['partido']): r['hora_partido'] for r in filas}.items(), key=lambda kv: (kv[1], kv[0]))
    idx, P = {}, []
    for (j, n), hora in claves:
        idx[(j, n)] = len(P)
        P.append({'jor': j, 'n': n, 'hora': hora, 'liga': next(r['liga'] for r in filas if r['jornada'] == j and r['partido'] == n)})
    # estado, slug, disponibilidad
    SER, META, HIS, JR = {}, {}, {}, {}
    nmax = 0
    by_name = {}
    for j in jors:
        base = os.path.join(RAIZ, 'jornadas', j)
        est = {}
        pe = os.path.join(base, 'resultados', 'estado_partidos.json')
        if os.path.exists(pe):
            est = {k: v for k, v in json.load(open(pe, encoding='utf8')).items() if not k.startswith('_')}
        slug = {}
        for p in glob.glob(os.path.join(base, 'entradas', '*.json')):
            d = json.load(open(p, encoding='utf8'))
            slug[f"{d['local']} - {d['visitante']}"] = (os.path.basename(p)[:-5], d['local'], d['visitante'])
        clima = {}
        pc = os.path.join(base, 'clima', 'clima.json')
        if os.path.exists(pc):
            clima = json.load(open(pc, encoding='utf8'))
        graded = {}
        for r in filas:
            if r['jornada'] == j and r['resultado'] and r['resultado'] != 'nula':
                graded[r['partido']] = graded.get(r['partido'], 0) + 1
        for (jj, n), i in idx.items():
            if jj != j:
                continue
            p = P[i]
            sl, loc, vis = slug.get(n, (None, n.split(' - ')[0], n.split(' - ')[-1]))
            p.update({'slug': sl, 'loc': loc, 'vis': vis})
            e = est.get(n)
            p['est'] = e['estado'] if e else ('final' if graded.get(n) else 'pend')
            p['g'] = e['g'] if e and e['estado'] != 'pend' else None
            p['min'] = e.get('min', '') if e else ''
            D = {k: 0 for k in 'BFARCJE'}
            fsj = None
            if sl:
                D['B'] = int(os.path.exists(os.path.join(base, 'betano', sl + '.json')))
                fp = os.path.join(base, 'flashscore', sl + '.json')
                D['F'] = int(os.path.exists(fp))
                D['A'] = int(os.path.exists(os.path.join(base, 'alineaciones', sl + '.json')))
                D['J'] = int(os.path.exists(os.path.join(base, 'jugadores', sl + '.json')))
                D['C'] = int(any(sl in k or k in sl for k in clima))
                D['E'] = int(os.path.exists(os.path.join(base, 'entradas', sl + '.json')))
                if D['F']:
                    fsj = json.load(open(fp, encoding='utf8'))
                    D['R'] = int(bool(fsj.get('arbitro')))
                    p['arb'] = fsj.get('arbitro') or ''
                    p['estadio'] = fsj.get('estadio') or ''
            p['dat'] = D
            p['gradas'] = graded.get(n, 0)
            if fsj:
                forma, h2h = fsj.get('forma', {}), fsj.get('h2h', [])
                nmax = max(nmax, len(forma.get('local', [])), len(forma.get('visitante', [])))
                SER[i], META[i] = {}, {}
                for lado, clave in (('l', 'local'), ('v', 'visitante')):
                    lista = forma.get(clave, [])[:FI.N]
                    for mk, k in STAT.items():
                        s, m = serie(lista, k)
                        SER[i].setdefault(mk, {})[lado] = s
                    META[i][lado] = serie(lista, 'c')[1]
                for mk, k in STAT.items():
                    SER[i][mk]['h'] = serie(h2h[:FI.N_H2H], k)[0]
                META[i]['h'] = [[m.get('fecha', ''), m.get('comp', ''), '', (m.get('g') or [None, None])[0], (m.get('g') or [None, None])[1]] for m in h2h[:FI.N_H2H]]
            # historial de jugadores (Flashscore) casado con los nombres de Betano
            pj = os.path.join(base, 'jugadores', (sl or '_') + '.json')
            if os.path.exists(pj):
                H = json.load(open(pj, encoding='utf8'))
                nombres = sorted({r['jugador'] for r in filas if r['jornada'] == j and r['partido'] == n and r['jugador']})
                sal = {}
                for fs_n, d in H.items():
                    b = CJ.casar_flashscore(fs_n, nombres)
                    if b and d.get('p'):
                        sal[b] = [[x[1]] + x[2:11] for x in d['p']]
                if sal:
                    HIS[i] = sal
        nm = {k[1]: v for k, v in idx.items() if k[0] == j}
        for fp in glob.glob(os.path.join(base, 'jugadores_resultado', '*.txt')):
            for k, v in jug_resultado(fp, nm).items():
                JR[k] = v
    # líneas
    L, Jg = [], []
    for r in filas:
        i = idx[(r['jornada'], r['partido'])]
        rs = RS.get(r['resultado'], '')
        cf = {'sí': 1, 'no': 0}.get(r['cumple_ficha'])
        if r['mercado'].startswith('jugador:'):
            Jg.append([i, r['mercado'][8:], r['jugador'], 'L' if r['ambito'] == 'local' else 'V', f(r['titular']), f(r['linea']), r['lado'], f(r['cuota']), f(r['p_modelo']), f(r['p_mercado']),
                       f(r['ev_modelo']), f(r['esperado']), f(r['colchon']), rs, real(r['nota']), f(r['stake'], 0), r['cumple_ficha'][:40]])
        elif r['mercado'] in STAT and r['lado'] in ('Más', 'Menos') and r['linea'] != '':
            L.append([i, r['mercado'], r['ambito'], r['lado'], f(r['linea']), f(r['cuota']), f(r['esperado']), f(r['colchon']), f(r['p_modelo']), f(r['p_mercado']), f(r['ev_modelo']),
                      rs, real(r['nota']), f(r['stake'], 0), f(r['cuota_cierre']), cf, r['alerta_modelo'], r['cuotas_leidas'][:16]])
    # boletos
    bol = {}
    for p in [os.path.join(RAIZ, 'registro', 'boletos_9-12nov.json')] + sorted(glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'balance', 'boletos_betano.json'))):
        d = json.load(open(p, encoding='utf8'))
        for b in d['boletos']:
            bol[b['n']] = b
    pcs = {}
    for p in glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'balance', 'patas_calificadas.json')):
        pcs.update(json.load(open(p, encoding='utf8')))
    B = []
    for n in sorted(bol):
        b = bol[n]
        B.append([n, b.get('fecha', ''), b.get('hora', ''), b.get('tipo', ''), b.get('stake', 0), b.get('gratis', False), b.get('cuota', 0), b.get('resultado', ''), b.get('cobrado', 0),
                  b.get('partidos', ''), b.get('patas', ''), pcs.get(str(n))])
    abiertas = []
    for p in glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'balance', 'pendientes.json')):
        abiertas += json.load(open(p, encoding='utf8'))
    # sugerencias
    S = []
    for r in rd(os.path.join(RAIZ, 'registro', 'sugerencias.csv')):
        try:
            pj = json.loads(r['patas_json']) if r.get('patas_json') else []
        except ValueError:
            pj = []
        S.append([r['id'], r['fecha_entrega'], r['hora'], r['entrega'], r['tipo'], r['nombre'], r['partidos'], r['patas'], f(r['cuota']), f(r['p_estimada']), r['resultado'], r['detalle_patas'][:300],
                  r['familia_fallo'], r['fuente'], pj])
    # histórico 9–12 nov (picks entregados antes del pipeline)
    HL = []
    for r in rd(os.path.join(RAIZ, 'registro', 'historial_lineas.csv')):
        HL.append([r['fecha_partido'], r['partido'], r['mercado_linea'], f(r['cuota']), f(r['p_modelo']), f(r['p_mercado']), f(r['ev']), RS.get(r['resultado'], ''), r['modelo'][:60]])
    # documentos
    docs = []
    pat = (glob.glob(os.path.join(RAIZ, 'entregas', '**', '*.md'), recursive=True) + glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'ESTADO.md')) + glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'enfoque.md'))
           + glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'reanalisis*.md')) + glob.glob(os.path.join(RAIZ, 'jornadas', '*', 'informe_final.md')) + glob.glob(os.path.join(RAIZ, 'docs', '*.md'))
           + [os.path.join(RAIZ, x) for x in ('registro/BITACORA.md', 'CLAUDE.md', 'GUIA_RAPIDA.md', 'MODELO_README.md')])
    for p in sorted(set(pat)):
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf8').read()
        rel = os.path.relpath(p, RAIZ)
        m = re.match(r'(?:jornadas|entregas)/(\d{4}-\d{2}-\d{2}[^/]*)', rel)
        titulo = next((ln.lstrip('# ').strip() for ln in t.splitlines() if ln.strip()), rel)[:120]
        tipo = 'entrega' if rel.startswith('entregas') else 'estado' if rel.endswith('ESTADO.md') else 'enfoque/reanálisis' if ('enfoque' in rel or 'reanalisis' in rel) else 'informe' if 'informe' in rel else 'proyecto'
        docs.append([rel, titulo, tipo, m.group(1) if m else '', t[:60000]])
    htmls = [[os.path.relpath(p, RAIZ), os.path.getsize(p) // 1024] for p in sorted(glob.glob(os.path.join(RAIZ, 'entregas', '**', '*.html'), recursive=True))]
    metodos = rd(os.path.join(RAIZ, 'registro', 'metodos.csv'))
    estados = {j: open(os.path.join(RAIZ, 'jornadas', j, 'ESTADO.md'), encoding='utf8').read()[:6000] for j in jors if os.path.exists(os.path.join(RAIZ, 'jornadas', j, 'ESTADO.md'))}
    nmax = nmax or FI.N
    ahora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))).strftime('%d-%b-%Y %H:%M')
    return {'gen': ahora, 'jors': jors, 'P': P, 'L': L, 'J': Jg, 'SER': SER, 'META': META, 'HIS': HIS, 'JR': JR, 'B': B, 'abiertas': abiertas, 'S': S, 'HL': HL, 'docs': docs, 'htmls': htmls,
            'metodos': [[m['fecha'], m['modelo_o_forma'], m['que_se_entrego'][:200], m['medido'][:300], m['limites'][:200]] for m in metodos], 'estados': estados,
            'N': nmax, 'NH': FI.N_H2H, 'K': FI.CUMPLE if nmax >= FI.N else max(1, round(FI.CUMPLE * nmax / FI.N)), 'MN': FI.MIN_N if nmax >= FI.N else max(1, round(FI.MIN_N * nmax / FI.N)), 'UNIT': 3700}


if __name__ == '__main__':
    d = construir()
    print({k: (len(v) if hasattr(v, '__len__') else v) for k, v in d.items()})
    print(len(json.dumps(d, ensure_ascii=False, separators=(',', ':'))) // 1024, 'KB')
