#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Califica el «guion» que Claude escribió ANTES de cada partido (notas/<clave>.json → "guion") con el resultado real.

Uso: python3 recoleccion/calificar_guion.py jornadas/AAAA-MM-DD [resultados_por_partido.json]
     → jornadas/AAAA-MM-DD/guion_calificado.json   (y un resumen por pantalla)

Formato del guion (todo opcional salvo `predicciones`; se escribe en la recolección, antes del partido, solo con lo leído):
  "guion": {"resumen": "texto corto",
            "domina": "local|visitante|parejo",         # se califica con los remates totales (sh); empate de remates = parejo
            "ritmo":  "abierto|cerrado",                # abierto = 3 o más goles; cerrado = 2 o menos
            "predicciones": [ {"tipo": "mas_remates", "equipo": "local"}, {"tipo": "goles_mas", "linea": 2.5}, ... ]}
Tipos: mas_remates, mas_tiros_arco, mas_corners, mas_faltas, mas_tarjetas (equipo con más); gana, no_pierde (equipo);
       goles_mas / goles_menos / corners_mas / corners_menos / tarjetas_mas_que / tarjetas_menos_que (con `linea`, total del partido);
       ambos_si, ambos_no.
Los resultados salen de resultados_por_partido.json de la jornada (g, c, y, sh, sot, f, [local, visitante]). Lo que falta se marca
«sin resultado»; nada se inventa. «igual» (empate en la estadística de «equipo con más») cuenta como fallo.
Límite: mide la lectura del partido, no la ganancia; con pocos partidos por jornada son pistas, no leyes.
"""
import os, sys, json, glob

CLAVE_EQ = {'mas_remates': 'sh', 'mas_tiros_arco': 'sot', 'mas_corners': 'c', 'mas_faltas': 'f', 'mas_tarjetas': 'y'}
CLAVE_TOT = {'goles': 'g', 'corners': 'c', 'tarjetas': 'y'}


def _j(p):
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else None


def idx(eq):
    return 0 if eq == 'local' else 1


def calificar_pred(p, res):
    """→ (resultado, valor real texto). resultado ∈ cumplió / falló / sin resultado."""
    t = p.get('tipo')
    if t in CLAVE_EQ:
        k = CLAVE_EQ[t]
        if k not in res:
            return 'sin resultado', ''
        h, a = res[k]
        mi, otro = (h, a) if p.get('equipo') == 'local' else (a, h)
        return ('cumplió' if mi > otro else 'falló'), f'{h}-{a}'
    if t in ('gana', 'no_pierde'):
        if 'g' not in res:
            return 'sin resultado', ''
        h, a = res['g']
        mi, otro = (h, a) if p.get('equipo') == 'local' else (a, h)
        return ('cumplió' if (mi > otro if t == 'gana' else mi >= otro) else 'falló'), f'{h}-{a}'
    if t in ('ambos_si', 'ambos_no'):
        if 'g' not in res:
            return 'sin resultado', ''
        h, a = res['g']
        ok = (h > 0 and a > 0) if t == 'ambos_si' else not (h > 0 and a > 0)
        return ('cumplió' if ok else 'falló'), f'{h}-{a}'
    for pref, k in (('goles', 'g'), ('corners', 'c'), ('tarjetas', 'y')):
        if t and t.startswith(pref) and (t.endswith('_mas') or t.endswith('_menos') or t.endswith('_mas_que') or t.endswith('_menos_que')):
            if k not in res or p.get('linea') is None:
                return 'sin resultado', ''
            tot = res[k][0] + res[k][1]
            mas = '_mas' in t
            return ('cumplió' if (tot > p['linea'] if mas else tot < p['linea']) else 'falló'), str(tot)
    return 'sin resultado', 'tipo desconocido'


def calificar_guion(g, res):
    out = {'resumen': g.get('resumen'), 'predicciones': [], 'domina': None, 'ritmo': None}
    for p in g.get('predicciones') or []:
        r, v = calificar_pred(p, res)
        out['predicciones'].append(dict(p, resultado=r, valor_real=v))
    if g.get('domina') and 'sh' in res:
        h, a = res['sh']
        real = 'local' if h > a else 'visitante' if a > h else 'parejo'
        out['domina'] = dict(pedido=g['domina'], real=real, remates=f'{h}-{a}', resultado='cumplió' if real == g['domina'] else 'falló')
    if g.get('ritmo') and 'g' in res:
        tot = sum(res['g'])
        real = 'abierto' if tot >= 3 else 'cerrado'
        out['ritmo'] = dict(pedido=g['ritmo'], real=real, goles=tot, resultado='cumplió' if real == g['ritmo'] else 'falló')
    return out


def main(argv):
    base = argv[1]
    rp = argv[2] if len(argv) > 2 else os.path.join(base, 'resultados', 'resultados_por_partido.json')
    RES = _j(rp) or {}
    mapa = {}
    for fp in glob.glob(os.path.join(base, 'fichas', 'ficha_*.json')):
        F = _j(fp)
        if F and F.get('encuentro'):
            mapa[fp.split('ficha_')[1][:-5]] = F['encuentro']
    sal, n = {}, {'cumplió': 0, 'falló': 0, 'sin resultado': 0}
    for np_ in sorted(glob.glob(os.path.join(base, 'notas', '*.json'))):
        clave = os.path.basename(np_)[:-5]
        N = _j(np_) or {}
        if not N.get('guion'):
            continue
        res = RES.get(mapa.get(clave, '')) or RES.get(clave) or {}
        c = calificar_guion(N['guion'], res)
        sal[clave] = c
        for p in c['predicciones'] + [x for x in (c['domina'], c['ritmo']) if x]:
            n[p['resultado'] if p['resultado'] in n else 'sin resultado'] += 1
    json.dump({'jornada': os.path.basename(base.rstrip('/')), 'partidos': sal, 'resumen': n}, open(os.path.join(base, 'guion_calificado.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    tot = n['cumplió'] + n['falló']
    print(f"guiones: {len(sal)} partidos · predicciones cumplidas {n['cumplió']} de {tot}" + (f" ({n['cumplió']/tot:.0%})" if tot else '') + f" · sin resultado {n['sin resultado']}")


if __name__ == '__main__':
    main(sys.argv)
