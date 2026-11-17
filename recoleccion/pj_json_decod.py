#!/usr/bin/env python3
"""Historial por jugador de Flashscore (volcado JSON del navegador: window.__PJ + window.__spec + window.__urls) → jugadores/<clave>.json.

Une las filas de Flashscore con las que ya haya en jugadores/<clave>.json (Opta, ver opta_decod.py) por nombre normalizado.
Entrada : jornadas/AAAA-MM-DD/flashscore/jugadores_pj_crudo.json  {pj:{mid:{t,f,h,a,lh,la,P}}, spec:{mid:[[clave:L|V, lado_del_equipo_en_ese_partido]]}, errores:[...]}
Salida  : jugadores/<clave>.json (añade filas), jugadores/LEEME.md (cobertura real por equipo)
Fila    : [mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas, entradas_ganadas, atajadas, entradas_tot]
Columnas Flashscore usadas: Minutos jugados, Remates totales, Remates a puerta, Goles, Asistencias, Tarjetas amarillas/rojas, Faltas cometidas,
«Entradas ganadas» (x/y → ganadas/intentadas), «Paradas del arquero». Las demás columnas se conservan en `fs` (por jugador y partido).
Límites: Flashscore no trae faltas recibidas.
Uso: python3 recoleccion/pj_json_decod.py jornadas/AAAA-MM-DD
"""
import sys, os, json, re, unicodedata
from collections import defaultdict


TRANSLIT = str.maketrans({'ø': 'o', 'æ': 'ae', 'œ': 'oe', 'đ': 'd', 'ð': 'd', 'ł': 'l', 'ß': 'ss', 'þ': 'th', 'ı': 'i'})   # NFD no descompone ø/æ/ł: sin esto «Højlund» y «Hojlund» eran dos jugadores


def norm(s):
    s = unicodedata.normalize('NFD', s.lower().translate(TRANSLIT))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z ]+', '', s).strip()


def n0(s):
    if s is None or s in ('-', ''):
        return 0
    m = re.match(r'^(\d+(?:\.\d+)?)', str(s))
    return int(float(m.group(1))) if m else 0


def pair(s):
    if s is None or s in ('-', ''):
        return 0, 0
    m = re.match(r'^(\d+)/(\d+)', str(s))
    if m:
        return int(m.group(1)), int(m.group(2))
    q = re.match(r'^\d+', str(s))
    return (int(q.group(0)),) * 2 if q else (0, 0)


def main(c):
    raw = json.load(open(os.path.join(c, 'flashscore', 'jugadores_pj_crudo.json'), encoding='utf-8'))
    pj, spec = raw['pj'], raw['spec']
    jd = os.path.join(c, 'jugadores')
    por_clave = defaultdict(lambda: defaultdict(lambda: {'L': set(), 'V': set()}))
    leidos = defaultdict(set)
    datos = {}
    for fn in os.listdir(jd):
        if fn.endswith('.json'):
            datos[fn[:-5]] = json.load(open(os.path.join(jd, fn), encoding='utf-8'))
    nuevos = 0
    for mid, m in pj.items():
        for key, v in spec.get(mid, []):
            clave, lado = key.split(':')
            logo = m['lh'] if v == 'L' else m['la']
            d = datos.setdefault(clave, {})
            idx = {norm(n): n for n in d}
            vistos = 0
            for nombre, o in m['P'].items():
                if o.get('logo') != logo:
                    continue
                mn = n0(o.get('Minutos jugados'))
                if not mn:
                    continue
                vistos += 1
                gan, tot = pair(o.get('Entradas ganadas'))
                fila = [mid, m['f'], mn, n0(o.get('Remates totales')), n0(o.get('Remates a puerta')), n0(o.get('Goles')), n0(o.get('Asistencias')),
                        n0(o.get('Tarjetas amarillas')), n0(o.get('Tarjetas rojas')), n0(o.get('Faltas cometidas')), gan, n0(o.get('Paradas del arquero')), tot]
                k = idx.get(norm(nombre)) or nombre
                r = d.setdefault(k, {'lado': lado, 'pos': o.get('pos', ''), 'pid': o.get('pid') or '', 'p': []})
                idx[norm(nombre)] = k
                if o.get('pid') and not r.get('pid'):
                    r['pid'] = o['pid']
                if not any(x[0] == mid for x in r['p']):
                    r['p'].append(fila)
                    r.setdefault('fs', {})[mid] = {kk: vv for kk, vv in o.items() if kk not in ('pid', 'logo', 'pos')}
                    nuevos += 1
            if vistos:
                leidos[clave].add((mid, lado))
    for clave, d in datos.items():
        for r in d.values():
            r['p'].sort(key=lambda x: x[1], reverse=True)
        json.dump(d, open(os.path.join(jd, clave + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    # cobertura: partidos distintos por equipo (L/V) entre los 10 oficiales
    ln = ['# Historial por jugador · jornada 17-nov-2026', '',
          'Fuentes: **Opta** (Nations League, 5 partidos por equipo, ver `../opta/LEEME.md`) + **Flashscore** (clasificatorios del Mundial; pestaña «Estadísticas de jugadores», columnas General/Remates/Defensa/Paradas).',
          'Leído desde el navegador el 17-nov-2026 (noche del 16 en Bogotá). Cobertura real de los últimos 10 partidos oficiales de cada equipo:', '',
          '| Partido | Lado | Partidos con jugadores (de 10) | Jugadores | Sin datos en Flashscore |', '|---|---|---|---|---|']
    errores = raw.get('errores', [])
    for clave in sorted(datos):
        for lado in ('L', 'V'):
            ms = {x[0] for r in datos[clave].values() if r['lado'] == lado for x in r['p']}
            nj = sum(1 for r in datos[clave].values() if r['lado'] == lado)
            esp = {m for m, sp in spec.items() for kk, _ in sp if kk == clave + ':' + lado}
            falt = sorted(esp - {m for m, _ in [(m, l) for m in ms for l in (lado,)]})
            ln.append('| %s | %s | %d | %d | %d |' % (clave, lado, len(ms), nj, len(esp & set(falt))))
    ln += ['', 'Partidos de Flashscore sin tabla de jugadores: %d (ver `flashscore/jugadores_pj_crudo.json`, campo errores).' % len(errores), '',
           '## Límites', '- Flashscore no trae «faltas recibidas» (Opta sí: campo `opta`).',
           '- «Entradas ganadas» (Flashscore) y «E» (Opta) no son idénticas a las «entradas» de Betano.',
           '- Los partidos sin tabla se declaran, no se rellenan; esos mercados de jugador se recomiendan solo si el jugador tiene n suficiente.',
           '- Los datos pasaron por el navegador y se descargaron como archivo (sin transcripción por el chat).']
    open(os.path.join(jd, 'LEEME.md'), 'w', encoding='utf-8').write('\n'.join(ln) + '\n')
    print('filas nuevas', nuevos)


if __name__ == '__main__':
    main(sys.argv[1])
