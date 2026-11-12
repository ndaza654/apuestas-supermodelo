# -*- coding: utf-8 -*-
"""raw/bet_<clave>.txt (texto compacto sacado de la API de Betano) → betano/<clave>.json con el formato de la entrada del supermodelo."""
import json, os, re, sys, glob
RAW, OUT = '/home/claude/nov12/raw', '/home/claude/nov12/betano'
HT = ['1/1', '1/X', '1/2', 'X/1', 'X/X', 'X/2', '2/1', '2/X', '2/2']
def f(x): return None if x in ('-', '', None) else float(x)
def kv(txt): return [(a.rsplit('=', 1)[0], float(a.rsplit('=', 1)[1])) for a in txt.split(';') if '=' in a]
def parse(path):
    lineas, unicos, jug, parejas, meta = [], [], [], [], {}
    res = {}
    for ln in open(path, encoding='utf8').read().splitlines():
        if not ln.strip(): continue
        t = ln.split('|')
        if t[0] == 'E':
            loc, vis = [x.strip() for x in t[1].split(' - ', 1)]
            meta = dict(local=loc, visitante=vis, inicio_utc=t[2], betano_id=t[3], region=t[4], liga=t[5], n_mercados=int(t[6][2:]), cuotas_leidas=t[7].replace('leido=', ''))
        elif t[0] == 'L':
            for it in t[3].split():
                h, v = it.split(':'); mas, menos = v.split('/')
                if f(mas) is None and f(menos) is None: continue
                lineas.append(dict(mercado=t[1], ambito=t[2], linea=float(h), mas=f(mas), menos=f(menos)))
        elif t[0] == 'U':
            tp, body = t[1], '|'.join(t[2:])
            if tp == 'MRES':
                d = dict(kv(body)); res.update({'1': d['1'], 'X': d['X'], '2': d['2']})
            elif tp == 'DBLC':
                v = [c for _, c in kv(body)]
                if len(v) == 3: res.update({'1X': v[0], 'X2': v[1], '12': v[2]})
            elif tp == 'BTSC':
                v = [c for _, c in kv(body)]; unicos.append(dict(mercado='ambos', opciones={'si': v[0], 'no': v[1]}))
            elif tp in ('TWMC', 'NTYC'):
                v = [c for _, c in kv(body)]
                unicos.append(dict(mercado='mas_que', stat='corners' if tp == 'TWMC' else 'tarjetas', opciones={'local': v[0], 'empate': v[1], 'visitante': v[2]}))
            elif tp in ('4151', '4152'):
                v = [c for _, c in kv(body)]; unicos.append(dict(mercado='ambos_n_tarjetas', n=1 if tp == '4151' else 2, opciones={'si': v[0], 'no': v[1]}))
            elif tp in ('H1RS', 'H2RS', 'HOFR'):
                v = [c for _, c in kv(body)]
                unicos.append(dict(mercado={'H1RS': 'resultado_1t', 'H2RS': 'resultado_2t', 'HOFR': 'htft_o'}[tp], opciones={'1': v[0], 'X': v[1], '2': v[2]}))
            elif tp == 'HTFT':
                v = [c for _, c in kv(body)]
                if len(v) == 9: unicos.append(dict(mercado='htft', opciones=dict(zip(HT, v))))
            elif tp == 'FHMR':
                for row in body.split(';'):
                    ps = [p.split('=') for p in row.split('/')]
                    if len(ps) == 3:
                        unicos.append(dict(mercado='handicap', h=float(ps[0][0]), opciones={'local': float(ps[0][1]), 'empate': float(ps[1][1]), 'visitante': float(ps[2][1])}))
            elif tp == 'AHRF':
                d = {}
                for nm, c in kv(body):
                    lado = 'local' if nm.startswith('L ') else 'visitante'
                    h = float(nm.split('@')[1]); hl = h if lado == 'local' else -h
                    d.setdefault(hl, {})[lado] = c
                for hl, o in sorted(d.items()):
                    if len(o) == 2 and 1.35 <= min(o.values()) and max(o.values()) <= 3.3:
                        unicos.append(dict(mercado='handicap', h=hl, opciones=o))
        elif t[0] == 'P':
            # nombres con «(Equipo (F)» parten el campo: se recompone
            if len(t) > 3 and not re.match(r'^(L|V|\?)$', t[2]):
                m = re.match(r'^(.*) \((.*)$', t[1]); nm = m.group(1).strip(); team = (m.group(2) + ' (' + t[2]).strip()
                lado = 'local' if team.startswith(meta['local'][:8]) else 'visitante'; rest = t[3:]
            else:
                nm, lado, rest = t[1].strip(), {'L': 'local', 'V': 'visitante'}.get(t[2]), t[3:]
            if nm == 'Sin Goles' or lado is None: continue
            for it in rest:
                k, v = it.split('=', 1)
                esc = lambda s: {int(a.split(':')[0]): float(a.split(':')[1]) for a in s.split(',') if ':' in a}
                if k == 'an': jug.append(dict(jugador=nm, lado=lado, stat='anota', cuota=float(v)))
                elif k == 'aoa': jug.append(dict(jugador=nm, lado=lado, stat='anota_o_asiste', cuota=float(v)))
                elif k == 'tj': jug.append(dict(jugador=nm, lado=lado, stat='tarjeta', cuota=float(v)))
                elif k in ('as', 'sh', 'sot', 'tk', 'fc', 'sv'):
                    e = esc(v)
                    if e: jug.append(dict(jugador=nm, lado=lado, stat={'as': 'asiste', 'sh': 'remates', 'sot': 'al_arco', 'tk': 'entradas', 'fc': 'faltas', 'sv': 'atajadas'}[k], escalera=e))
        elif t[0] == 'R':
            for nm, c in kv('|'.join(t[2:])):
                a, b = [x.strip() for x in nm.split(' o ', 1)]
                parejas.append(dict(jugadores=[a, b], stat=t[1], cuota=c))
    if res: unicos.insert(0, dict(mercado='resultado', opciones=res))
    return meta, dict(lineas=lineas, unicos=unicos, jugadores=jug, parejas=parejas)
if __name__ == '__main__':
    for p in sorted(glob.glob(RAW + '/bet_*.txt')):
        k = os.path.basename(p)[4:-4]
        meta, bet = parse(p)
        json.dump(dict(meta=meta, betano=bet), open(f'{OUT}/{k}.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
        nj = len({j['jugador'] for j in bet['jugadores']})
        print(f"{k:32s} lineas={len(bet['lineas']):3d} unicos={len(bet['unicos']):2d} jug={nj:2d} lineas_jug={len(bet['jugadores']):3d} parejas={len(bet['parejas']):2d}")
