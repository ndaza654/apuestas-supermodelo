# -*- coding: utf-8 -*-
"""Análisis del historial de boletos del usuario (4-nov en adelante): cómo se ganan, cómo se pierden (una pata o varias),
en qué mercados apuesta más y en cuáles acierta más. Solo lee lo ya guardado en el repo; no usa red.

    python3 recoleccion/analisis_historial_boletos.py            # imprime y escribe registro/analisis_historial_boletos.json

Fuentes: registro/historico_libro.json (4-8 nov: boletos y selecciones), registro/boletos_9-12nov.json + patas_calificadas_9-12nov.json,
jornadas/*/balance/boletos_betano.json + patas_calificadas.json (13-nov en adelante). Las patas se clasifican por palabras clave del texto
(familia de mercado, Más/Menos, línea) y el valor real que dejó el balance. Lo que no se puede leer queda «Otro» o sin margen: no se inventa.
Límites: un Bet Builder es UNA apuesta con varias patas (sus patas no son independientes); las apuestas gratis no son plata del usuario;
el cash out devolvió el stake; muestra pequeña (decenas de boletos): son pistas, no leyes."""
import glob, json, os, re, sys, unicodedata, collections, math

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)


def norm(s):
    return unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode()


FAM = [('corner', 'Córners'), ('tarjeta', 'Tarjetas'), ('tiros al arco', 'Tiros al arco'), ('tiro al arco', 'Tiros al arco'), ('a puerta', 'Tiros al arco'),
       ('remate', 'Remates'), ('falta', 'Faltas'), ('fuera', 'Fueras de juego'), ('saques de meta', 'Saques de meta'), ('saque de meta', 'Saques de meta'),
       ('saques de banda', 'Saques de banda'), ('atajada', 'Atajadas'), ('entrada', 'Entradas'), ('tackle', 'Entradas'), ('asist', 'Asistencia'),
       ('anota', 'Jugador anota'), ('anotar', 'Jugador anota'), ('ambos', 'Ambos marcan'), ('doble oportunidad', 'Resultado'), ('gana', 'Resultado'),
       ('empate', 'Resultado'), ('clasifica', 'Resultado'), ('hand', 'Hándicap'), ('under', 'Goles'), ('asiatico', 'Goles'), ('goles', 'Goles'), ('gol', 'Goles')]


def familia(t):
    n = norm(t)
    for k, f in FAM:
        if k in n:
            return f
    return None


def lado_linea(t):
    n = norm(t)
    m = re.search(r'(mas|menos|sobre|under|over)\s*(?:de\s*)?(\d+(?:[.,]\d+)?)', n)
    if m:
        return ('Más' if m.group(1) in ('mas', 'sobre', 'over') else 'Menos', float(m.group(2).replace(',', '.')))
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*\+', n)
    if m:
        return ('Más', float(m.group(1).replace(',', '.')) - 0.5)
    return (None, None)


def valor(v):
    m = re.search(r'-?\d+(?:[.,]\d+)?', str(v))
    return float(m.group(0).replace(',', '.')) if m else None


def cargar():
    B = []
    h = json.load(open('registro/historico_libro.json', encoding='utf-8'))
    sel = {}
    for s in h['selecciones']:
        sel.setdefault(s['boleto'], []).append(s)
    for b in h['boletos']:
        legs = []
        for s in sel.get(b['n'], []):
            ok = True if s['resultado'] in ('Ganó', 'Ganada', 'Cumplió') else False if s['resultado'] in ('Perdió', 'Perdida') else None
            legs.append(dict(txt=f"{s['familia']} {s['lado']} {s['linea']} · {s['partido']}", ok=ok, fam=s['familia'].split(' (')[0], lado=s['lado'],
                             linea=s['linea'], valor=s.get('valor_real')))
        B.append(dict(n=b['n'], fecha=b['fecha'], tipo=b['tipo'], stake=float(b['stake']), gratis=bool(b['gratis']), cuota=float(b['cuota'] or 0),
                      res=('Cash Out' if 'ash' in b['resultado'] else b['resultado']), cobrado=float(b.get('cobrado') or 0), legs=legs,
                      partidos_n=int(b.get('partidos_n') or 1)))
    d = json.load(open('registro/boletos_9-12nov.json', encoding='utf-8'))['boletos']
    P = json.load(open('registro/patas_calificadas_9-12nov.json', encoding='utf-8'))
    allb = [(x, P.get(str(x['n']))) for x in d]
    for f in sorted(glob.glob('jornadas/*/balance/boletos_betano.json')):
        P2 = json.load(open(f.replace('boletos_betano', 'patas_calificadas'), encoding='utf-8'))
        for x in json.load(open(f, encoding='utf-8'))['boletos']:
            allb.append((x, P2.get(str(x['n']))))
    for x, p in allb:
        legs = []
        txts = [t.strip() for t in re.split(r' · ', x['patas'])] if x.get('patas') else []
        pl = (p or {}).get('patas', [])
        for i, l in enumerate(pl):
            t = l[0]
            ok = True if l[1] == '✓' else False if l[1] == '✗' else None
            fam = familia(t)
            ld, ln = lado_linea(t)
            if (fam is None or ld is None) and i < len(txts) and len(txts) == len(pl):
                fam = fam or familia(txts[i])
                if ld is None:
                    ld, ln = lado_linea(txts[i])
            legs.append(dict(txt=t, ok=ok, fam=fam or 'Otro', lado=ld, linea=ln, valor=valor(l[2]) if len(l) > 2 else None))
        B.append(dict(n=x['n'], fecha=x['fecha'], tipo=x['tipo'], stake=float(x['stake']), gratis=bool(x.get('gratis')), cuota=float(x['cuota'] or 0),
                      res=x['resultado'], cobrado=float(x.get('cobrado') or 0), legs=legs,
                      partidos_n=max(1, len([t for t in re.split(r' · | \| ', x.get('partidos', '')) if t.strip()]))))
    for b in B:
        for l in b['legs']:
            l['fam'] = l.get('fam') or 'Otro'
    return B


def unidades_falta(l):
    """Cuántas unidades le faltaron/sobraron a una pata caída (Más: faltó; Menos: se pasó). None si no se puede."""
    v, ln, ld = l.get('valor'), l.get('linea'), l.get('lado')
    if v is None or ln is None or ld is None:
        return None
    try:
        v = float(v); ln = float(ln)
    except (TypeError, ValueError):
        return None
    u = (math.ceil(ln) - v) if ld == 'Más' else (v - math.floor(ln))
    return u if u >= 1 else None


def pct(a, b):
    return round(100 * a / b, 1) if b else None


def dinero(b):
    return (0 if b['gratis'] else b['stake']), b['cobrado']


def agrupa(B, clave):
    g = collections.defaultdict(lambda: dict(n=0, gan=0, co=0, per=0, stake=0.0, cobr=0.0))
    for b in B:
        k = clave(b)
        s, c = dinero(b)
        x = g[k]; x['n'] += 1; x['stake'] += s; x['cobr'] += c
        x['gan'] += b['res'] == 'Ganada'; x['co'] += b['res'] == 'Cash Out'; x['per'] += b['res'] == 'Perdida'
    out = {}
    for k, x in g.items():
        out[k] = dict(boletos=x['n'], ganadas=x['gan'], cash_out=x['co'], perdidas=x['per'], acierto=pct(x['gan'], x['n']), apostado=round(x['stake']),
                      cobrado=round(x['cobr']), neto=round(x['cobr'] - x['stake']), roi=pct(x['cobr'] - x['stake'], x['stake']))
    return out


def npatas(b):
    return len([l for l in b['legs'] if l['ok'] is not None]) or len(b['legs'])


def banda_cuota(c):
    return '< 2' if c < 2 else '2–3' if c < 3 else '3–5' if c < 5 else '5–8' if c < 8 else '8+'


def main():
    B = cargar()
    R = {'periodo': f"{min(b['fecha'] for b in B)} a {max(b['fecha'] for b in B)}", 'boletos': len(B)}
    tot = agrupa(B, lambda b: 'todo')['todo']
    R['global'] = tot
    R['por_dia'] = dict(sorted(agrupa(B, lambda b: b['fecha']).items()))
    R['por_npatas'] = dict(sorted(agrupa(B, lambda b: '1' if npatas(b) == 1 else '2' if npatas(b) == 2 else '3' if npatas(b) == 3 else '4' if npatas(b) == 4 else '5+').items()))
    R['por_cuota'] = agrupa(B, lambda b: banda_cuota(b['cuota']))
    def tipo(b):
        if b['partidos_n'] > 1:
            return 'combinada entre partidos'
        return 'simple de 1 pata' if npatas(b) == 1 else 'Bet Builder (varias patas, 1 partido)'
    R['por_tipo'] = agrupa(B, tipo)
    # ---- cómo se pierden (solo boletos «Perdida» con patas calificadas)
    per = [b for b in B if b['res'] == 'Perdida' and any(l['ok'] is False for l in b['legs'])]
    caidas = collections.Counter()
    for b in per:
        k = sum(1 for l in b['legs'] if l['ok'] is False)
        caidas['1' if k == 1 else '2' if k == 2 else '3+'] += 1
    R['perdidas_por_patas_caidas'] = dict(caidas, total=len(per))
    # una pata, por n de patas del boleto
    una = [b for b in per if sum(1 for l in b['legs'] if l['ok'] is False) == 1]
    por_np = collections.defaultdict(lambda: [0, 0])
    for b in per:
        k = '1 pata' if npatas(b) == 1 else '2 patas' if npatas(b) == 2 else '3 patas' if npatas(b) == 3 else '4+ patas'
        por_np[k][0] += 1; por_np[k][1] += sum(1 for l in b['legs'] if l['ok'] is False) == 1
    R['perdidas_una_pata_segun_npatas'] = {k: dict(perdidas=v[0], por_una_pata=v[1]) for k, v in por_np.items()}
    cul = collections.Counter(); exp = collections.Counter()
    for b in una:
        l = [l for l in b['legs'] if l['ok'] is False][0]
        cul[(l['fam'], l['lado'] or '?')] += 1
    for b in B:
        for l in b['legs']:
            if l['ok'] is not None:
                exp[(l['fam'], l['lado'] or '?')] += 1
    R['pata_que_tumba_cuando_cae_una'] = [dict(mercado=f'{k[0]} {k[1]}', veces=v, de_patas_apostadas=exp[k]) for k, v in cul.most_common(14)]
    marg = collections.Counter(); ejemplos = []
    for b in una:
        l = [l for l in b['legs'] if l['ok'] is False][0]
        u = unidades_falta(l)
        marg['sin dato' if u is None else '1 unidad' if u == 1 else '2 unidades' if u == 2 else '3+ unidades'] += 1
        if u is not None and u == 1:
            ejemplos.append(f"#{b['n']} {l['txt'][:70]} (real {l['valor']})")
    R['perdidas_una_pata_margen'] = dict(marg)
    R['ejemplos_cayo_por_1_unidad'] = ejemplos[:14]
    # pérdidas «por más»: cuántas patas cayeron y cuáles
    multi = [b for b in per if sum(1 for l in b['legs'] if l['ok'] is False) >= 2]
    cm = collections.Counter()
    for b in multi:
        for l in b['legs']:
            if l['ok'] is False:
                cm[(l['fam'], l['lado'] or '?')] += 1
    R['patas_caidas_en_perdidas_multiples'] = [dict(mercado=f'{k[0]} {k[1]}', veces=v) for k, v in cm.most_common(10)]
    # ---- patas por mercado y lado
    f = collections.defaultdict(lambda: [0, 0])
    for b in B:
        for l in b['legs']:
            if l['ok'] is None:
                continue
            k = (l['fam'], l['lado'] or '?')
            f[k][0] += 1; f[k][1] += l['ok'] is True
    R['patas_por_mercado_lado'] = sorted([dict(mercado=f'{k[0]} {k[1]}', patas=v[0], acertadas=v[1], acierto=pct(v[1], v[0])) for k, v in f.items() if v[0] >= 5], key=lambda x: -x['patas'])
    ff = collections.defaultdict(lambda: [0, 0])
    for b in B:
        for l in b['legs']:
            if l['ok'] is None:
                continue
            ff[l['fam']][0] += 1; ff[l['fam']][1] += l['ok'] is True
    R['patas_por_mercado'] = sorted([dict(mercado=k, patas=v[0], acertadas=v[1], acierto=pct(v[1], v[0])) for k, v in ff.items() if v[0] >= 5], key=lambda x: -x['patas'])
    # patas por más/menos
    ml = collections.defaultdict(lambda: [0, 0])
    for b in B:
        for l in b['legs']:
            if l['ok'] is None or not l['lado']:
                continue
            ml[l['lado']][0] += 1; ml[l['lado']][1] += l['ok'] is True
    R['patas_por_lado'] = {k: dict(patas=v[0], acierto=pct(v[1], v[0])) for k, v in ml.items()}
    # ---- cómo se ganan
    gan = [b for b in B if b['res'] == 'Ganada']
    R['ganadas'] = dict(n=len(gan), patas_prom=round(sum(npatas(b) for b in gan) / max(1, len(gan)), 2), por_npatas=dict(collections.Counter(npatas(b) for b in gan)),
                        cuota_mediana=sorted(b['cuota'] for b in gan)[len(gan) // 2] if gan else None,
                        familias=collections.Counter(l['fam'] for b in gan for l in b['legs']).most_common(8),
                        lista=[dict(n=b['n'], fecha=b['fecha'], tipo=b['tipo'], cuota=b['cuota'], stake=b['stake'], cobrado=b['cobrado'], patas=npatas(b)) for b in gan])
    # mercados más apostados por boletos (presencia)
    pres = collections.Counter(); presg = collections.Counter()
    for b in B:
        fs = {l['fam'] for l in b['legs']}
        for x in fs:
            pres[x] += 1; presg[x] += b['res'] == 'Ganada'
    R['presencia_en_boletos'] = sorted([dict(mercado=k, boletos=v, ganados=presg[k], acierto=pct(presg[k], v)) for k, v in pres.items()], key=lambda x: -x['boletos'])
    # cash out
    co = [b for b in B if b['res'] == 'Cash Out']
    R['cash_out'] = dict(n=len(co), stake=round(sum(b['stake'] for b in co)), cobrado=round(sum(b['cobrado'] for b in co)))
    # misma-partido repetido (dos boletos del mismo partido)
    return R


if __name__ == '__main__':
    R = main()
    json.dump(R, open('registro/analisis_historial_boletos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({k: R[k] for k in ('periodo', 'boletos', 'global', 'por_npatas', 'por_cuota', 'por_tipo', 'perdidas_por_patas_caidas', 'perdidas_una_pata_segun_npatas', 'perdidas_una_pata_margen', 'cash_out')}, ensure_ascii=False, indent=1))
