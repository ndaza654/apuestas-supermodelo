#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Historial de goleadores/goleadoras por partido (regla «Árbitro y goleador», CLAUDE.md, 19-nov-2026).

Fuente: incidentes de Flashscore de los últimos 10 partidos oficiales de cada equipo (feed `df_su_1_<mid>`: quién marcó, de penal, autogoles,
quién asistió, amarillas/rojas), guardados por el navegador en `jornadas/AAAA-MM-DD/flashscore/goles_crudo.json`
  {su: {mid: [[tipo, lado(1 local|2 visitante), minuto, nombre, url_jugador, comentario, periodo, id], ...]},
   spec: {mid: [["<clave>:L|V", "L|V (de qué lado jugó el equipo en ese partido)"]]}, meta: {mid: {f: fecha, h: local, a: visitante}}}
No necesita la tabla de jugadores de Flashscore: sirve para fútbol femenino y partidos sin estadísticas por jugador. No trae minutos jugados
ni titularidad: «sin gol en los últimos 10» NO prueba que haya jugado (se cruza con la alineación cuando existe).
Cruza con las líneas «anota» / «anota o asiste» de Betano (betano/<clave>.json → jugadores) por nombre normalizado.
Salida: jornadas/AAAA-MM-DD/goleadores/<clave>.json y .md (+ LEEME.md con la cobertura real).
Uso: python3 recoleccion/goleadores.py jornadas/AAAA-MM-DD
"""
import sys, os, json, re, unicodedata
from collections import defaultdict

TRANSLIT = str.maketrans({'ø': 'o', 'æ': 'ae', 'œ': 'oe', 'đ': 'd', 'ð': 'd', 'ł': 'l', 'ß': 'ss', 'þ': 'th', 'ı': 'i'})


def toks(s):
    s = unicodedata.normalize('NFD', (s or '').lower().translate(TRANSLIT))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return [t for t in re.split(r'[^a-z]+', s) if t]


def slug_toks(url):
    m = re.match(r'^/player/([^/]+)/', url or '')
    return toks(m.group(1).replace('-', ' ')) if m else []


def coincide(bet, fs_name, fs_url):
    """¿El nombre completo de Betano y el de Flashscore son la misma persona? Devuelve 2 (muy seguro), 1 (probable) o 0."""
    b = toks(bet)
    st = slug_toks(fs_url)
    if st and len(b) >= 2 and set(b) == set(st):
        return 2
    if st and b and set(b) <= set(st) and len(b) >= 2:
        return 2
    f = toks(fs_name)
    if not f or not b:
        return 0
    ini = [t for t in f if len(t) == 1]
    ap = [t for t in f if len(t) > 1]
    if not ap:
        return 0
    if not set(ap) <= set(b):
        return 0
    resto = [t for t in b if t not in ap]
    if ini and not all(any(r.startswith(i) for r in resto) for i in ini):
        return 0
    if len(b) == len(f) and set(b) == set(f):
        return 2
    return 1


def main(base):
    ruta = os.path.join(base, 'flashscore', 'goles_crudo.json')
    if not os.path.exists(ruta):
        print('sin goles_crudo.json: no hay historial de goleadores para', base)
        return 2
    D = json.load(open(ruta, encoding='utf-8'))
    su, spec, meta = D['su'], D['spec'], D['meta']
    alias = {}
    try:
        alias = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'alias_jugadores.json'), encoding='utf-8'))
    except Exception:
        pass
    os.makedirs(os.path.join(base, 'goleadores'), exist_ok=True)
    por_clave = defaultdict(lambda: {'L': [], 'V': []})
    for mid, sp in spec.items():
        for key, venue in sp:
            clave, lado = key.split(':')
            por_clave[clave][lado].append((mid, venue))
    resumen = []
    for clave in sorted(por_clave):
        bp = os.path.join(base, 'betano', clave + '.json')
        bet = json.load(open(bp, encoding='utf-8'))['betano'] if os.path.exists(bp) else {}
        out = {'partido': clave, 'fuente': 'Flashscore incidentes (df_su) de los últimos 10 partidos oficiales de cada equipo', 'equipos': {}}
        md = [f'# Goleadores · {clave}', '',
              'Últimos 10 partidos oficiales de cada equipo (Flashscore: quién marcó y quién asistió). No trae minutos ni titularidad: sin gol no prueba que jugó.', '']
        for lado, nom in (('L', 'local'), ('V', 'visitante')):
            partidos = sorted(por_clave[clave][lado], key=lambda x: meta[x[0]]['f'], reverse=True)
            jug = {}
            goles_eq = 0
            hist = []
            for mid, venue in partidos:
                my = '1' if venue == 'L' else '2'
                rival = meta[mid]['a'] if venue == 'L' else meta[mid]['h']
                g_mio = g_riv = 0
                anot = set()
                for e in su.get(mid, []):
                    tipo, side, minuto, nombre, url, ict, per, pid = (e + [''] * 8)[:8]
                    es_pen_gol = tipo == 'Penalty' and per != 'Penalties'
                    if tipo in ('Goal',) or es_pen_gol:
                        if side == my:
                            g_mio += 1
                            j = jug.setdefault(pid or nombre, {'nombre': nombre, 'url': url, 'goles': 0, 'penales': 0, 'asist': 0, 'amarillas': 0, 'rojas': 0, 'partidos_gol': [], 'partidos_asist': []})
                            j['goles'] += 1
                            j['penales'] += 1 if es_pen_gol else 0
                            if mid not in j['partidos_gol']:
                                j['partidos_gol'].append(mid)
                            anot.add(pid or nombre)
                        else:
                            g_riv += 1
                    elif tipo == 'Own goal':
                        if side == my:
                            g_riv += 1      # Flashscore anota el autogol en el lado del que lo marca en contra; se cuenta como gol del rival
                        else:
                            g_mio += 1
                    elif tipo == 'Assistance' and side == my:
                        j = jug.setdefault(pid or nombre, {'nombre': nombre, 'url': url, 'goles': 0, 'penales': 0, 'asist': 0, 'amarillas': 0, 'rojas': 0, 'partidos_gol': [], 'partidos_asist': []})
                        j['asist'] += 1
                        if mid not in j['partidos_asist']:
                            j['partidos_asist'].append(mid)
                    elif tipo == 'Yellow Card' and side == my:
                        j = jug.setdefault(pid or nombre, {'nombre': nombre, 'url': url, 'goles': 0, 'penales': 0, 'asist': 0, 'amarillas': 0, 'rojas': 0, 'partidos_gol': [], 'partidos_asist': []})
                        j['amarillas'] += 1
                    elif tipo == 'Red Card' and side == my:
                        j = jug.setdefault(pid or nombre, {'nombre': nombre, 'url': url, 'goles': 0, 'penales': 0, 'asist': 0, 'amarillas': 0, 'rojas': 0, 'partidos_gol': [], 'partidos_asist': []})
                        j['rojas'] += 1
                goles_eq += g_mio
                hist.append({'mid': mid, 'fecha': meta[mid]['f'], 'rival': rival, 'sede': venue, 'gf': g_mio, 'gc': g_riv, 'anotaron': sorted(anot)})
            n = len(partidos)
            # lista del equipo, de más a menos goles
            lista = sorted(jug.values(), key=lambda j: (-j['goles'], -j['asist'], j['nombre']))
            # líneas de Betano de este lado
            lineas = defaultdict(dict)
            for x in bet.get('jugadores', []):
                if x.get('lado') == nom and x['stat'] in ('anota', 'anota_o_asiste') and x.get('cuota') is not None:
                    lineas[x['jugador']][x['stat']] = x['cuota']
            filas = []
            usados = set()
            for jb, cu in lineas.items():
                mejor, ptos = None, 0
                for k, j in jug.items():
                    p = coincide(jb, j['nombre'], j['url'])
                    if p > ptos:
                        mejor, ptos = (k, j), p
                if mejor is None:
                    for k, j in jug.items():
                        if alias.get(k.split('/')[-1] if '/' in k else k) == jb:
                            mejor, ptos = (k, j), 2
                f = {'jugador': jb, 'cuotas': cu, 'coincidencia': ptos}
                if mejor:
                    k, j = mejor
                    usados.add(k)
                    f.update({'flashscore': j['nombre'], 'goles': j['goles'], 'penales': j['penales'], 'partidos_con_gol': len(j['partidos_gol']), 'asistencias': j['asist'],
                              'partidos_con_gol_o_asistencia': len(set(j['partidos_gol']) | set(j['partidos_asist'])), 'amarillas': j['amarillas'], 'n_partidos': n})
                else:
                    f.update({'goles': 0, 'penales': 0, 'partidos_con_gol': 0, 'asistencias': 0, 'partidos_con_gol_o_asistencia': 0, 'n_partidos': n,
                              'nota': 'sin gol ni asistencia en los últimos %d partidos del equipo (no se sabe si jugó)' % n})
                filas.append(f)
            filas.sort(key=lambda f: (-f['partidos_con_gol'], -f['goles'], f.get('cuotas', {}).get('anota') or 99))
            sin_linea = [j for k, j in jug.items() if k not in usados and j['goles'] > 0]
            out['equipos'][nom] = {'partidos': hist, 'goles_a_favor': goles_eq, 'jugadores_con_gol': [{'nombre': j['nombre'], 'goles': j['goles'], 'penales': j['penales'], 'partidos_con_gol': len(j['partidos_gol']), 'asistencias': j['asist']} for j in lista if j['goles'] > 0],
                                   'lineas_betano': filas, 'goleadores_sin_linea_betano': [{'nombre': j['nombre'], 'goles': j['goles'], 'partidos_con_gol': len(j['partidos_gol'])} for j in sin_linea]}
            nombre_eq = (meta[partidos[0][0]]['h'] if partidos and partidos[0][1] == 'L' else meta[partidos[0][0]]['a']) if partidos else nom
            md += [f'## {nom.capitalize()}: {nombre_eq} — {goles_eq} goles en {n} partidos', '',
                   'Marcaron (últimos 10): ' + (', '.join(f"{j['nombre']} {j['goles']}" + (f" ({j['penales']} de penal)" if j['penales'] else '') + f" en {len(j['partidos_gol'])} part." for j in lista if j['goles'] > 0) or 'nadie (sin goles registrados)'), '',
                   '| Jugador (Betano) | Anota | Anota o asiste | Goles | En cuántos partidos | Asist. | Gol o asist. en |', '|---|---|---|---|---|---|---|']
            for f in filas:
                c = f['cuotas']
                md.append(f"| {f['jugador']} | {c.get('anota', '')} | {c.get('anota_o_asiste', '')} | {f['goles']} | {f['partidos_con_gol']} de {f['n_partidos']} | {f['asistencias']} | {f['partidos_con_gol_o_asistencia']} de {f['n_partidos']} |")
            if sin_linea:
                libres = [f for f in filas if f['coincidencia'] == 0]
                def posible(j):
                    ap = [t for t in toks(j['nombre']) if len(t) > 1]
                    c = [f['jugador'] for f in libres if set(ap) & set(toks(f['jugador']))]
                    return (' (¿' + ' o '.join(c) + '?)') if c else ''
                md += ['', 'Goleadores sin línea en Betano o con nombre que no coincide: ' + ', '.join(f"{j['nombre']} {j['goles']} gol(es) en {len(j['partidos_gol'])} part." + posible(j) for j in sin_linea)]
            md.append('')
            amb = [f['jugador'] for f in filas if f['coincidencia'] == 1]
            if amb:
                md += ['Coincidencia de nombre «probable» (no segura): ' + ', '.join(amb), '']
            resumen.append((clave, nom, n, goles_eq, sum(1 for f in filas if f['coincidencia'] > 0), len(filas)))
        out['limites'] = ['Sin minutos jugados ni titularidad: no se puede calcular goles por 90.', 'Cuenta penales en juego como gol; la tanda de penales no cuenta.', 'Flashscore atribuye los autogoles al rival.']
        json.dump(out, open(os.path.join(base, 'goleadores', clave + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        open(os.path.join(base, 'goleadores', clave + '.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    ln = ['# Historial de goleadores · ' + os.path.basename(os.path.normpath(base)), '',
          'Fuente: incidentes de Flashscore de los últimos 10 partidos oficiales de cada equipo (quién marcó, de penal, asistencias, tarjetas). Leído desde el navegador y descargado como archivo, verificado con hash.', '',
          '| Partido | Equipo | Partidos | Goles a favor | Líneas Betano con coincidencia de nombre |', '|---|---|---|---|---|']
    for clave, nom, n, g, m, t in resumen:
        ln.append(f'| {clave} | {nom} | {n} | {g} | {m} de {t} |')
    ln += ['', '## Límites', '- Sin minutos ni titularidad: «sin gol» no prueba que jugó; no hay goles por 90.',
           '- Penales en juego cuentan como gol; la tanda no. Los autogoles se atribuyen al rival.',
           '- El nombre de Betano se cruza con el de Flashscore por nombre normalizado; los «probables» se marcan en cada archivo.']
    open(os.path.join(base, 'goleadores', 'LEEME.md'), 'w', encoding='utf-8').write('\n'.join(ln) + '\n')
    print('goleadores escritos:', len(resumen) // 2, 'partidos')
    for r in resumen:
        print('  %-44s %-9s goles %3d  líneas con coincidencia %d de %d' % (r[0][:44], r[1], r[3], r[4], r[5]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
