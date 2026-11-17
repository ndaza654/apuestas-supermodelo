#!/usr/bin/env python3
"""Opta Player Stats (Betting Showcase) → historial por jugador y por equipo.

Entrada : jornadas/AAAA-MM-DD/opta/opta_nl_crudo.json  (lo baja el navegador; ver recoleccion/README.md)
Salida  : jornadas/AAAA-MM-DD/jugadores/<clave>.json     mismo formato que jugadores_decod.py (Flashscore)
          jornadas/AAAA-MM-DD/equipos/<clave>.json      estadística de equipo por partido, columnas Opta completas
          jornadas/AAAA-MM-DD/opta/LEEME.md             cobertura real

Fila de jugador: [mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas, entradas, atajadas, entradas_tot]
Opta resumen: G,A,TR,TA,Crn,S,SOnT,BS,P,C,E,O,FC,FR,SAV (remates S, a puerta SOnT, bloqueados BS, pases P, E entradas,
FC faltas cometidas, FR faltas recibidas). «C» sin confirmar (¿despejes o centros?): se guarda tal cual en `opta`.
Uso: python3 recoleccion/opta_decod.py jornadas/2026-11-17
"""
import json, re, sys, os, unicodedata
from collections import defaultdict

MESES = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
         'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}
COLS_SUM = ['G', 'A', 'TR', 'TA', 'Crn', 'S', 'SOnT', 'BS', 'P', 'C', 'E', 'O', 'FC', 'FR', 'SAV']


def slug(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def fecha_iso(txt):
    m = re.match(r'(\d+) de (\w+) de (\d{4})', txt)
    return '%s-%02d-%02d' % (m.group(3), MESES[m.group(2)], int(m.group(1))) if m else ''


def nombre_fs(n):
    """«A. Isak» → «Isak A.» (formato Flashscore/Betano del repo)."""
    n = re.sub(r'^(Starter|Suplente)\s+', '', n.strip())
    m = re.match(r'^((?:[A-ZÁÉÍÓÚÑ]\.\s*)+)(.+)$', n)
    if m:
        return '%s %s' % (m.group(2).strip(), m.group(1).strip())
    return n


def num(x):
    try:
        return float(str(x).replace(',', '.'))
    except ValueError:
        return 0.0


def main(carpeta):
    d = json.load(open(os.path.join(carpeta, 'opta', 'opta_nl_crudo.json'), encoding='utf-8'))
    Q, UP, D = d['Q'], d['UP'], d['D']
    os.makedirs(os.path.join(carpeta, 'jugadores'), exist_ok=True)
    os.makedirs(os.path.join(carpeta, 'equipos'), exist_ok=True)
    # por partido jugado: filas de equipo y de jugador, minutos por nombre
    jug_por_partido, eq_por_partido, falta = {}, {}, []
    for q in Q:
        s, p = D.get('D|%s|sum' % q['id']), D.get('D|%s|pts' % q['id'])
        if not s or not s.get('ok'):
            falta.append(q['id'] + ':sum')
            continue
        mins = {}
        if p and p.get('ok'):
            for lado in ('home', 'away'):
                for fila in p[lado][1:]:
                    c = fila.split('|')
                    mins[(lado, nombre_fs(c[0]))] = (num(c[4]), c[1])
        else:
            falta.append(q['id'] + ':pts')
        fecha = fecha_iso(q['d'])
        jug_por_partido[q['id']] = {}
        for lado in ('home', 'away'):
            filas = s[lado][1:]
            tot = [f for f in filas if f.startswith('Total|')]
            for f in filas:
                c = f.split('|')
                if c[0] == 'Total':
                    continue
                n = nombre_fs(c[0])
                v = [int(num(x)) for x in c[1:16]]
                z = dict(zip(COLS_SUM, v))
                mn, pos = mins.get((lado, n), (None, ''))
                mn = int(mn) if mn is not None else None
                jug_por_partido[q['id']].setdefault(lado, {})[n] = {'fecha': fecha, 'min': mn, 'pos': pos, **z}
            if tot:
                z = dict(zip(COLS_SUM, [int(num(x)) for x in tot[0].split('|')[1:16]]))
                eq_por_partido.setdefault(q['id'], {})[lado] = z
    # por partido de mañana
    cobertura = []
    for u in UP:
        clave = slug(u['h']) + '-' + slug(u['a'])
        pv = D.get('D|%s|prev' % u['id'], {})
        meta = pv.get('meta', '')
        arb = re.search(r'Árbitro(.+)$', meta)
        res_j, res_e = {}, {'local': u['h'], 'visitante': u['a'], 'arbitro': arb.group(1).strip() if arb else None,
                            'hdr': pv.get('hdr'), 'partidos': {'L': [], 'V': []}}
        for lado_up, equipo in (('L', u['h']), ('V', u['a'])):
            n_part = 0
            for q in sorted(Q, key=lambda x: fecha_iso(x['d']), reverse=True):
                if equipo not in (q['h'], q['a']) or q['id'] not in jug_por_partido:
                    continue
                n_part += 1
                lado_q = 'home' if q['h'] == equipo else 'away'
                otro = 'away' if lado_q == 'home' else 'home'
                fecha = fecha_iso(q['d'])
                te, tr = eq_por_partido.get(q['id'], {}).get(lado_q), eq_por_partido.get(q['id'], {}).get(otro)
                res_e['partidos'][lado_up].append({'mid': q['id'], 'fecha': fecha, 'local': q['h'], 'visitante': q['a'],
                                                   'marcador': q.get('sc'), 'equipo_es_local': lado_q == 'home',
                                                   'a_favor': te, 'en_contra': tr})
                for n, z in jug_por_partido[q['id']].get(lado_q, {}).items():
                    r = res_j.setdefault(n, {'lado': lado_up, 'pos': z['pos'], 'pid': '', 'p': [], 'opta': []})
                    if z['pos'] and not r['pos']:
                        r['pos'] = z['pos']
                    r['p'].append([q['id'], z['fecha'], z['min'] if z['min'] is not None else 0, z['S'], z['SOnT'], z['G'],
                                   z['A'], z['TA'], z['TR'], z['FC'], z['E'], z['SAV'], z['E']])
                    r['opta'].append([q['id'], z['fecha'], z['min'], z['pos'], z['FR'], z['BS'], z['Crn'], z['C'], z['O'], z['P']])
            cobertura.append((clave, equipo, n_part))
        json.dump(res_j, open(os.path.join(carpeta, 'jugadores', clave + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump(res_e, open(os.path.join(carpeta, 'equipos', clave + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    sin_min = sum(1 for m in jug_por_partido.values() for l in m.values() for z in l.values() if z['min'] is None)
    tot_j = sum(1 for m in jug_por_partido.values() for l in m.values() for z in l.values())
    ln = ['# Opta · Nations League (jugadores y equipos)', '',
          'Fuente: optaplayerstats.statsperform.com (Betting Showcase), leído del DOM renderizado desde el navegador el 16-nov-2026 ~22:30-23:00 Bogotá. '
          'Se tomaron los partidos de Nations League 2026/27 ya jugados de los 16 equipos (resumen del partido + puntos Opta con minutos).', '',
          '| Partido | Equipo | Partidos NL leídos | de los 10 oficiales |', '|---|---|---|---|']
    for clave, eq, n in cobertura:
        ln.append('| %s | %s | %d | faltan %d (clasificatorios/amistosos: otra fuente) |' % (clave, eq, n, 10 - n))
    ln += ['', 'Filas de jugador leídas: %d (sin minutos: %d). Páginas con error: %s.' % (tot_j, sin_min, falta or 'ninguna'), '',
           '## Límites',
           '- Solo cubre Nations League: cada equipo tiene 5 de sus últimos 10 partidos oficiales; los otros 5 faltan.',
           '- Remates = S; a puerta = SOnT; entradas = E; faltas cometidas = FC; faltas recibidas = FR (solo en `opta`, no en `p`).',
           '- Columna «C» del resumen Opta sin confirmar (despejes o centros).',
           '- Nombres en formato «Apellido I.» convertidos desde «I. Apellido»; pueden diferir de Betano (revisar con alias_jugadores.json).',
           '- Lo recogido pasó por el navegador y se descargó como archivo; el crudo está en opta/opta_nl_crudo.json.']
    open(os.path.join(carpeta, 'opta', 'LEEME.md'), 'w', encoding='utf-8').write('\n'.join(ln) + '\n')
    print('\n'.join(ln[6:6 + len(cobertura)]))
    print('jugadores', tot_j, 'sin min', sin_min, 'faltas', falta)


if __name__ == '__main__':
    main(sys.argv[1])
