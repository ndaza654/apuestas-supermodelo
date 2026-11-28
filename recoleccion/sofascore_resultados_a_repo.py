# -*- coding: utf-8 -*-
"""Convierte el crudo de `sofascore_resultados.js` (event + statistics + lineups + incidents por partido) en lo que pide el balance:

    python3 recoleccion/sofascore_resultados_a_repo.py jornadas/AAAA-MM-DD <crudo.json> [jornada_en_lineas_csv]

Escribe en `<jornada>/resultados/`:
  · resultados_por_partido.json  (g,g1,c,c1,sh,sh1,sot,sot1,f,f1,off,off1,gk,gk1,sv,sv1,ti,ti1,y,y1,am,am1; clave = «Local - Visitante» como en lineas.csv)
  · jugadores_resultado.txt      (bloques `#<partido>` con filas lado|jugador|min|remates|al_arco|goles|asist|faltas|faltas_rec|entradas|atajadas|amarillas|rojas)
  · control_jugadores.txt        (suma de jugadores = total del equipo)
Tarjetas en PUNTOS de Betano desde los INCIDENTES: amarilla 1, roja directa 2, doble amarilla 3 (1.ª amarilla + 2 por la roja);
no cuentan las del cuerpo técnico (sin jugador) ni las mostradas después del pitazo final (time < 0; se dejan en y_con_posteriores).
"""
import csv, json, os, sys, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = {'sh': 'Total shots', 'sot': 'Shots on target', 'c': 'Corner kicks', 'f': 'Fouls', 'off': 'Offsides', 'ti': 'Throw-ins',
     'gk': 'Goal kicks', 'sv': 'Goalkeeper saves'}


def num(x):
    try:
        return int(str(x).replace('%', '').split('/')[0])
    except Exception:
        return None


def main(base, crudo, jor=None):
    jor = jor or os.path.basename(base.rstrip('/'))
    R = json.load(open(crudo, encoding='utf8'))
    nombres = {}
    for p in os.listdir(os.path.join(base, 'betano')):
        m = json.load(open(os.path.join(base, 'betano', p), encoding='utf8'))['meta']
        nombres[p[:-5]] = f"{m['local']} - {m['visitante']}"
    out, txt, ctrl = {}, [], []
    for k, v in R.items():
        nom = nombres.get(k, k)
        ev = v['ev']
        if (ev.get('status') or {}).get('type') != 'finished':
            continue
        r = {'fuente': 'Sofascore /event/<id> + /statistics + /lineups + /incidents (leído 28-nov ~00:50 Bogotá, navegador integrado)'}
        hs, as_ = ev['hs'], ev['as']
        r['g'] = [hs.get('normaltime', hs['current']), as_.get('normaltime', as_['current'])]
        r['g1'] = [hs.get('period1', 0), as_.get('period1', 0)]
        per = {s['period']: {i['name']: (num(i['home']), num(i['away'])) for g in s['groups'] for i in g['statisticsItems']} for s in v['st']}
        for key, nm in E.items():
            for suf, p in (('', 'ALL'), ('1', '1ST')):
                d = per.get(p, {})
                if nm in d:
                    r[key + suf] = list(d[nm])
                elif p in per and nm in ('Offsides',):      # Sofascore omite la fila cuando es 0 en ambos
                    r[key + suf] = [0, 0]
        # tarjetas por incidentes
        pts = {True: [0, 0, 0], False: [0, 0, 0]}   # [total, 1T, post]
        am = {True: [0, 0], False: [0, 0]}
        posteriores = {True: 0, False: 0}
        for i in v['inc']:
            if i['t'] != 'card' or not i.get('p'):
                continue
            val = {'yellow': 1, 'red': 2, 'yellowRed': 2}.get(i['c'], 0)
            lado = bool(i['tm'])
            if i['time'] is not None and i['time'] < 0:
                posteriores[lado] += val
                continue
            pts[lado][0] += val
            if i['c'] == 'yellow':
                am[lado][0] += 1
            if i['time'] <= 45:
                pts[lado][1] += val
                if i['c'] == 'yellow':
                    am[lado][1] += 1
        r['y'] = [pts[True][0], pts[False][0]]
        r['y1'] = [pts[True][1], pts[False][1]]
        r['am'] = [am[True][0], am[False][0]]
        r['am1'] = [am[True][1], am[False][1]]
        if posteriores[True] or posteriores[False]:
            r['y_con_posteriores'] = [pts[True][0] + posteriores[True], pts[False][0] + posteriores[False]]
            r['nota_tarjetas'] = 'hubo tarjetas después del pitazo final (Sofascore time<0): no cuentan en y; ver y_con_posteriores'
        out[nom] = r
        # jugadores
        tarj = collections.defaultdict(lambda: [0, 0])
        for i in v['inc']:
            if i['t'] == 'card' and i.get('p') and not (i['time'] is not None and i['time'] < 0):
                tarj[i['p']][0 if i['c'] == 'yellow' else 1] += 1
        txt.append(f'#{nom}')
        tot = {'h': [0, 0], 'a': [0, 0]}
        for lado, key in (('h', 'h'), ('a', 'a')):
            for p in v['lu'][key]:
                s = p.get('s') or {}
                mn = s.get('minutesPlayed')
                if not mn:
                    continue
                rem = (s.get('onTargetScoringAttempt', 0) or 0) + (s.get('shotOffTarget', 0) or 0) + (s.get('blockedScoringAttempt', 0) or 0)
                sot = s.get('onTargetScoringAttempt', 0) or 0
                tot[lado][0] += rem
                tot[lado][1] += sot
                a, ro = tarj.get(p['n'], [0, 0])
                txt.append('|'.join(str(x) for x in [lado, p['n'], mn, rem, sot, s.get('goals', 0), s.get('goalAssist', 0), s.get('fouls', 0),
                                                     s.get('wasFouled', 0), s.get('totalTackle', 0), s.get('saves', 0), a, ro]))
        for lado, j in (('h', 0), ('a', 1)):
            ok = (tot[lado][0] == r.get('sh', [None, None])[j], tot[lado][1] == r.get('sot', [None, None])[j])
            ctrl.append(f"{nom} [{lado}] remates jug {tot[lado][0]} vs equipo {r.get('sh', ['?', '?'])[j]} {'OK' if ok[0] else 'DIFIERE'} · al arco jug {tot[lado][1]} vs equipo {r.get('sot', ['?', '?'])[j]} {'OK' if ok[1] else 'DIFIERE'}")
    d = os.path.join(base, 'resultados')
    os.makedirs(d, exist_ok=True)
    json.dump(out, open(os.path.join(d, 'resultados_por_partido.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    head = '# 27-nov (Sofascore /api/v1 lineups + incidents; solo quienes jugaron). entradas = tackles totales de Sofascore; atajadas = saves del arquero; faltas recibidas = wasFouled.\n'
    open(os.path.join(d, 'jugadores_resultado.txt'), 'w', encoding='utf8').write(head + '\n'.join(txt) + '\n')
    open(os.path.join(d, 'control_jugadores.txt'), 'w', encoding='utf8').write('\n'.join(ctrl) + '\n')
    print(len(out), 'partidos;', sum(1 for c in ctrl if 'DIFIERE' in c), 'controles que difieren de', len(ctrl))


if __name__ == '__main__':
    main(*sys.argv[1:4])
