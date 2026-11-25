#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué mercados ofrece Betano por liga, aprendido de TODAS las recolecciones (jornadas/*/betano/*.json).
Sirve para planear la recolección: si una liga trae estadísticas de jugador (remates, tiros al arco, entradas, faltas,
atajadas, asistencias) hay que traer el historial por jugador; si trae tarjetas, el árbitro pesa; si no, no.
  python3 recoleccion/mercados_por_liga.py            → registro/mercados_betano_por_liga.json + .md
  python3 recoleccion/mercados_por_liga.py "Liga"     → imprime lo que se sabe de esa liga
Cuenta por liga: partidos vistos, en cuántos aparece cada familia (líneas de equipo por mercado/ámbito, únicos, estadísticas
de jugador, goleador, tarjeta de jugador, parejas) y la última fecha vista. Es lo que Betano ofreció la noche anterior:
el día del partido puede abrir más mercados (sobre todo de jugador, con los onces)."""
import glob, json, os, sys, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAT_JUG = {'remates', 'al_arco', 'entradas', 'faltas', 'atajadas', 'asiste', 'faltas_recibidas', 'anota_o_asiste'}


def familias(b):
    f = set()
    for l in b.get('lineas', []):
        f.add(f"{l['mercado']}:{l.get('ambito', 'total')}")
    for u in b.get('unicos', []) or []:
        f.add('unico:' + str(u.get('mercado') if isinstance(u, dict) else u))
    for j in b.get('jugadores', []) or []:
        st = j.get('stat') or j.get('mercado')
        f.add('jugador:' + str(st))
    if b.get('parejas'):
        f.add('parejas')
    return f


def construir():
    L = collections.defaultdict(lambda: {'partidos': 0, 'con_stat': 0, 'familias': collections.Counter(), 'ultima': '', 'ejemplos': []})
    for f in sorted(glob.glob(os.path.join(RAIZ, 'jornadas/*/betano/*.json'))):
        try:
            d = json.load(open(f, encoding='utf8'))
        except Exception:
            continue
        m, b = d.get('meta', {}), d.get('betano', {})
        liga = (m.get('liga') or '?').strip()
        jor = f.split('/')[-3]
        x = L[liga]; x['partidos'] += 1; x['ultima'] = max(x['ultima'], jor)
        if len(x['ejemplos']) < 3:
            x['ejemplos'].append(f"{jor} {m.get('local')}–{m.get('visitante')}")
        fs = familias(b)
        for fa in fs:
            x['familias'][fa] += 1
        x['con_stat'] += any(f.startswith('jugador:') and f.split(':', 1)[1] in STAT_JUG for f in fs)
    out = {}
    for liga, x in sorted(L.items()):
        n = x['partidos']; fam = {k: round(v / n, 2) for k, v in sorted(x['familias'].items())}
        stat = sorted({k.split(':', 1)[1] for k in fam if k.startswith('jugador:') and k.split(':', 1)[1] in STAT_JUG})
        out[liga] = {'partidos_vistos': n, 'ultima_jornada': x['ultima'], 'ejemplos': x['ejemplos'],
                     'jugador_estadistica': stat, 'goleador': fam.get('jugador:anota', 0), 'tarjeta_jugador': fam.get('jugador:tarjeta', 0),
                     'tarjetas_equipo': max([v for k, v in fam.items() if k.startswith('tarjetas:')] or [0]),
                     'corners': max([v for k, v in fam.items() if k.startswith('corners:')] or [0]),
                     'con_jugador_estadistica': round(x['con_stat'] / n, 2),
                     'necesita_historial_jugador': bool(stat), 'familias': fam}
    json.dump(out, open(os.path.join(RAIZ, 'registro/mercados_betano_por_liga.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    md = ['# Mercados que ofrece Betano por liga (aprendido de las recolecciones)', '',
          'Se regenera con `python3 recoleccion/mercados_por_liga.py`. Fracción = en qué parte de los partidos vistos apareció la familia la noche anterior '
          '(el día del partido Betano puede abrir más, sobre todo de jugador). Regla: si una liga trae estadística de jugador en la mayoría de partidos, '
          'traer el historial por jugador aunque esa noche no salga; si la trae pocas veces, releer Betano el día del partido y traerlo solo si aparece.', '',
          '| Liga | Partidos | Córners | Tarjetas equipo | Goleador | Tarjeta jugador | Partidos con estadística de jugador | Cuáles (→ historial por jugador) | Última |', '|---|---|---|---|---|---|---|---|---|']
    for liga, o in sorted(out.items(), key=lambda kv: -kv[1]['partidos_vistos']):
        md.append(f"| {liga} | {o['partidos_vistos']} | {o['corners']:.0%} | {o['tarjetas_equipo']:.0%} | {o['goleador']:.0%} | {o['tarjeta_jugador']:.0%} | {o['con_jugador_estadistica']:.0%} | {', '.join(o['jugador_estadistica']) or '—'} | {o['ultima_jornada']} |")
    open(os.path.join(RAIZ, 'registro/mercados_betano_por_liga.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
    return out


if __name__ == '__main__':
    o = construir()
    if len(sys.argv) > 1:
        q = sys.argv[1].lower()
        for k, v in o.items():
            if q in k.lower():
                print(k, json.dumps({a: b for a, b in v.items() if a != 'familias'}, ensure_ascii=False))
    else:
        print(len(o), 'ligas')
