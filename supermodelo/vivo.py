# -*- coding: utf-8 -*-
"""En vivo: el mismo motor del previo, jugado desde el minuto y el estado actuales.

Lección del balance 4–8 nov: en vivo se perdieron 10 de 13 boletos (−95.370) cuando se entraba por reacción. Aquí el
vivo es la continuación del plan previo: se ve la probabilidad previa de la línea, la de ahora, el EV con la cuota que
muestra Betano en vivo y la cuota mínima. Las medias del partido son las del previo (precio + contexto); lo observado
(remates, córners, faltas) actualiza el ritmo y la producción de cada equipo con un previo gamma (lo visto pesa más
cuanto más minutos van, sin borrar el previo). Ingeniero Analista (#33, #83, #289): la regresión del xG/tiros al arco
del 1T es la idea de fondo de sus sistemas en vivo; aquí entra como lo observado que actualiza la intensidad.

Uso:  python3 -m supermodelo.vivo partido.json vivo.json
vivo.json = {"estado": {"mitad": 2, "minuto": 60, "goles": [0, 0], "corners": [5, 2], "remates": [12, 4],
                        "al_arco": [4, 1], "faltas": [8, 10], "amarillas": [1, 2], "rojas": [0, 0], "rojas_directas": [0, 0],
                        "goles_1t": [0, 0], "corners_1t": [3, 1], "amarillas_1t": [0, 1]},
Tarjetas: 'amarillas' = amarillas mostradas (incluida la 2.ª de una expulsión); 'rojas' = todas; 'rojas_directas' = directas.
En el 2.º tiempo hay que dar lo del 1T (goles_1t, corners_1t, amarillas_1t): sin eso las líneas de 1T/2T no son confiables.
             "betano_vivo": {"lineas": [{"mercado": "goles", "ambito": "total", "linea": 0.5, "mas": 1.40, "menos": 2.75}],
                             "unicos": [{"mercado": "resultado", "opciones": {"1": 2.6, "X": 2.2, "2": 5.0}}]}}
"""
import json, sys
import numpy as np
from . import config as C, mercado as MK, mercados as MS
from .analizar import analizar, construir_objetivos
from .contexto import traducir
from .simulador import Partido

W_MERCADO_VIVO = 0.5   # en vivo la cuota se mueve con lo que pasa: se mezcla mitad y mitad si hay dos lados


def evaluar_vivo(e, v, n=C.N_SIM, seed=C.SEED + 3):
    loc, vis = e.get('local', 'Local'), e.get('visitante', 'Visitante')
    ficha = dict(e['ficha'], _liga=e.get('liga')) if e.get('ficha') else None
    aj = traducir(ficha)
    obj, _, _ = construir_objetivos(e, aj)
    est = v['estado']
    avisos = []
    mitad = int(est.get('mitad', 2 if est.get('minuto', 0) > 45 else 1))
    if mitad == 2:
        for clave, txt in (('goles_1t', 'goles'), ('corners_1t', 'córners'), ('amarillas_1t', 'amarillas')):
            if est.get(clave) is None and est.get(clave.replace('_1t', '')) is not None:
                avisos.append(f'Falta «{clave}»: los {txt} del 1T se suponen ' + ('iguales al marcador actual' if clave == 'goles_1t'
                              else 'repartidos por minutos') + '; las líneas de 1T y 2T de ese mercado pueden salir mal.')
    if est.get('rojas') and any(est['rojas']) and est.get('rojas_directas') is None:
        avisos.append('Falta «rojas_directas»: se suponen directas (2 puntos de Betano cada una).')
    P = Partido(obj, aj, n=n, seed=seed, estado=est)
    sim = P.res
    previo = analizar(e, n=max(6000, n // 3), seed=seed, builders=False)
    pre = {r['seleccion']: r for r in previo['lineas']}
    bet = v.get('betano_vivo') or {}
    out = []
    def fila(sel, cuota, p_mkt):
        nm = MS.nombre(sel, loc, vis)
        ev_ = MS.evento(sim, sel)
        ps = float(ev_.mean())
        p = ps if p_mkt is None else (1 - W_MERCADO_VIVO) * ps + W_MERCADO_VIVO * p_mkt
        p = float(np.clip(p, 0.003, 0.997))
        r0 = pre.get(nm)
        out.append(dict(seleccion=nm, sel=sel, cuota=cuota, p_simulacion=round(ps, 4), p_mercado=None if p_mkt is None else round(p_mkt, 4),
                        p=round(p, 4), ev=round(MK.ev(p, cuota), 4), cuota_justa=round(MK.cuota_justa(p), 2),
                        cuota_minima=round(MK.cuota_minima(p, 0.03, 0.02), 2), p_previa=None if r0 is None else r0['p'],
                        plan_previo=None if r0 is None else f"en el previo: {r0['etiqueta']} ({r0['p'] * 100:.0f} %)"))
    for l in bet.get('lineas', []):
        base = dict(mercado=l['mercado'], ambito=l.get('ambito', 'total'), linea=l['linea'])
        pm = MK.devig(l['mas'], l['menos']) if l.get('mas') and l.get('menos') else None
        for lado, c in (('mas', l.get('mas')), ('menos', l.get('menos'))):
            if c:
                fila(dict(base, lado=lado), c, None if pm is None else (pm if lado == 'mas' else 1 - pm))
    for u in bet.get('unicos', []):
        ops = [k for k, c in u['opciones'].items() if c]
        probs = MK.devig_n([u['opciones'][k] for k in ops])
        for k, pm in zip(ops, probs):
            fila({kk: vv for kk, vv in u.items() if kk != 'opciones'} | {'lado': k}, u['opciones'][k], pm)
    marc = est.get('goles', [0, 0])
    resumen = dict(minuto=est.get('minuto'), mitad=est.get('mitad'), marcador=f'{marc[0]}-{marc[1]}',
                   goles_restantes_esperados=round(float((sim[0]['g'] + sim[1]['g']).mean() - sum(marc)), 2),
                   corners_restantes_esperados=round(float((sim[0]['c'] + sim[1]['c']).mean() - sum(est.get('corners', [0, 0]))), 2)
                   if est.get('corners') else None,
                   p_final={'1': round(float((sim[0]['g'] > sim[1]['g']).mean()), 3), 'X': round(float((sim[0]['g'] == sim[1]['g']).mean()), 3),
                            '2': round(float((sim[0]['g'] < sim[1]['g']).mean()), 3)})
    medias = []
    for clave, stat, nm in (('goles', 'g', 'Goles'), ('corners', 'c', 'Córners'), ('remates', 'sh', 'Remates'), ('al_arco', 'sot', 'Tiros al arco'),
                            ('faltas', 'f', 'Faltas')):
        fin = float((sim[0][stat] + sim[1][stat]).mean())
        jug = est.get(clave)
        medias.append(dict(mercado=nm, final=round(fin, 1), jugado=None if jug is None else sum(jug),
                           restante=None if jug is None else round(fin - sum(jug), 1)))
    resumen['medias_finales'] = medias
    sin_dato_2t = {'goles': 'goles_1t', 'corners': 'corners_1t', 'tarjetas': 'amarillas_1t'}
    for x in out:
        k = sin_dato_2t.get(x['sel'].get('mercado'))
        if mitad == 2 and k and x['sel'].get('ambito') in ('1T', '2T') and est.get(k) is None:
            x['aviso'] = f'sin {k}: no confiable'
    return dict(partido=f'{loc} - {vis}', estado=est, resumen=resumen, avisos=avisos, lineas=sorted(out, key=lambda r: -r['ev']))


def markdown(V):
    r = V['resumen']
    L = [f"# En vivo: {V['partido']} · {r['marcador']} al {r['minuto']}′",
         f"Goles que faltan (esperados): {r['goles_restantes_esperados']}" + (f" · córners que faltan: {r['corners_restantes_esperados']}" if r['corners_restantes_esperados'] is not None else '')
         + f" · final: local {r['p_final']['1'] * 100:.0f} %, empate {r['p_final']['X'] * 100:.0f} %, visitante {r['p_final']['2'] * 100:.0f} %", '',
         *[f'⚠ {a}' for a in V.get('avisos') or []], '',
         '**Media final esperada del partido** (con lo que ya pasó): ' + ' · '.join(
             f"{m['mercado']} {m['final']}" + (f" (van {m['jugado']}, faltan {m['restante']})" if m['jugado'] is not None else '') for m in r.get('medias_finales') or []), '',
         '| Selección | Cuota en vivo | Prob. ahora | Simulación | Mercado | Prob. previa | EV | Cuota mínima | Plan previo |',
         '|---|---|---|---|---|---|---|---|---|']
    f = lambda x: '—' if x is None else f'{x * 100:.0f} %'
    for x in V['lineas']:
        L.append(f"| {x['seleccion']} | {x['cuota']:.2f} | {f(x['p'])} | {f(x['p_simulacion'])} | {f(x['p_mercado'])} | {f(x['p_previa'])} | "
                 f"{x['ev'] * 100:+.0f} % | {x['cuota_minima']:.2f} | {x['plan_previo'] or 'no estaba en el análisis previo'}{(' · ⚠ ' + x['aviso']) if x.get('aviso') else ''} |")
    L.append('\nEn vivo solo como continuación del plan: que el guion que se esperaba se esté dando y que la cuota esté en la mínima o más. '
             'Si la línea no estaba en el plan previo, es una entrada por reacción (la que más perdió en el balance).')
    return '\n'.join(L)


if __name__ == '__main__':
    e = json.load(open(sys.argv[1], encoding='utf8'))
    v = json.load(open(sys.argv[2], encoding='utf8'))
    V = evaluar_vivo(e, v)
    print(markdown(V))
    json.dump(V, open(sys.argv[2].rsplit('.', 1)[0] + '_resultado.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1, default=str)
