#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""¿El contexto separa aciertos de fallos? (medición, solo lectura; no cambia ninguna recomendación)

Uso: python3 recoleccion/medir_contexto.py   → registro/medicion_contexto.json + registro/medicion_contexto.md

Para cada línea calificada de registro/lineas.csv (resultado cumplió/falló; se excluyen nula y medias) con ficha y notas de su partido:
  · «situación»: factores que salen de las notas escritas por Claude ANTES del partido (necesita ganar, le sirve el empate, rotación,
    decisivo/derbi/nada en juego). Sin banderas en las notas no hay factor: «sin lectura».
  · «datos»: factores que salen de la ficha (esperado vs línea, quién concede, rachas, directos). Se parece al colchón.
La dirección de cada factor es + (empuja a Más) / − (a Menos). Una línea queda «a favor» si el neto empuja hacia su lado, «en contra» si
empuja al otro, «sin factor» si no hay neto. Se compara el acierto real con la probabilidad del precio (p_mercado, sin margen).
Límites: el contexto se recalcula con el código actual sobre las fichas y notas guardadas (no con lo que se vio el día); cada jornada
tiene una cobertura de notas distinta; las reglas de situación son de tipsters y medios (sin verificar).
"""
import os, sys, csv, json, glob, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import contexto_mercado as C

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MERC = C.MERC
EQUIPO = ('corners', 'goles', 'remates', 'al_arco', 'fueras')
BANDAS = [('< 1,50', 0, 1.5), ('1,50–1,99', 1.5, 2.0), ('≥ 2,00', 2.0, 99)]


def _j(p):
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else None


def f(x):
    try:
        return float(str(x).replace(',', '.'))
    except Exception:
        return None


def neto(fs, descartar=()):
    n = 0
    for d, t in fs:
        if any(t.startswith(p) for p in descartar):
            continue
        n += 1 if d == '+' else -1 if d == '-' else 0
    return n


def equipo_neto(N, lado, m):
    """Banderas de ese equipo en la nota: necesita ganar (+), le sirve el empate (−), rota (−). Solo mercados de ataque."""
    s = (N or {}).get(lado) or {}
    if m not in EQUIPO:
        return 0
    return (1 if s.get('necesita_ganar') else 0) - (1 if s.get('le_sirve_empate') else 0) - (1 if s.get('rotacion') else 0)


def apoyo(n, lado):
    """+1 si el neto empuja hacia el lado de la línea, −1 si empuja al otro, 0 si no hay."""
    if n == 0:
        return 0
    return 1 if (n > 0) == (lado == 'Más') else -1


def cargar():
    lineas = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'):
        if r['resultado'] in ('cumplió', 'falló') and r['mercado'] in MERC and r['lado'] in ('Más', 'Menos'):
            lineas[r['jornada']].append(r)
    out = []
    tabla_cob = []
    for jor, rows in sorted(lineas.items()):
        base = os.path.join(RAIZ, 'jornadas', jor)
        if not os.path.isdir(os.path.join(base, 'fichas')):
            continue
        mapa = {}
        for fp in glob.glob(os.path.join(base, 'fichas', 'ficha_*.json')):
            F = _j(fp)
            if F and F.get('encuentro'):
                mapa[F['encuentro']] = (fp.split('ficha_')[1][:-5], F)
        npart = nnotas = nflags = 0
        vistos = set()
        for r in rows:
            if r['partido'] not in mapa:
                continue
            clave, F = mapa[r['partido']]
            N = _j(os.path.join(base, 'notas', clave + '.json')) or {}
            loc, vis = [x.strip() for x in F['encuentro'].split(' - ', 1)]
            if clave not in vistos:
                vistos.add(clave)
                npart += 1
                nnotas += bool(N)
                nflags += bool(C.factores_situacion(N, 'goles', loc, vis, F) or C.factores_situacion(N, 'corners', loc, vis, F)) if N else 0
            m = r['mercado']
            fm = C.bloque(F, m)
            if not fm:
                continue
            fd = C.factores_datos(fm, m, loc, vis)
            if r['ambito'] == 'total':
                fsit = C.factores_situacion(N, m, loc, vis, F)
                ns = neto(fsit, ('Se espera', 'Se esperan', 'Árbitro'))
            elif r['ambito'] in ('local', 'visitante'):
                ns = equipo_neto(N, r['ambito'], m)
            else:
                continue
            nd = neto(fd)
            cuota, pm = f(r['cuota']), f(r['p_mercado'])
            if cuota is None or pm is None:
                continue
            out.append(dict(jornada=jor, clave=clave, mercado=m, ambito=r['ambito'], lado=r['lado'], cuota=cuota, pm=pm,
                            cumple=(r['cumple_ficha'] or '').lower().startswith('s'), hit=1 if r['resultado'] == 'cumplió' else 0,
                            sit=apoyo(ns, r['lado']), dat=apoyo(nd, r['lado']), con_notas=bool(N)))
        tabla_cob.append(dict(jornada=jor, partidos=npart, con_notas=nnotas, con_banderas=nflags))
    return out, tabla_cob


def resumen(L):
    n = len(L)
    if not n:
        return None
    h = sum(x['hit'] for x in L) / n
    p = sum(x['pm'] for x in L) / n
    se = math.sqrt(max(h * (1 - h), 1e-9) / n)
    return dict(n=n, acierto=round(h, 4), precio=round(p, 4), dif=round(h - p, 4), se=round(se, 4))


def agrupar(L, clave):
    d = collections.defaultdict(list)
    for x in L:
        d[clave(x)].append(x)
    return d


def tabla(L, nombre, clave, orden):
    g = agrupar(L, clave)
    return {nombre: {k: resumen(g[k]) for k in orden if k in g}}


def main():
    L, cob = cargar()
    ETQ = {1: 'a favor', 0: 'sin factor', -1: 'en contra'}
    R = {'lineas': len(L), 'cobertura': cob}
    for nombre, filt in (('total', lambda x: x['ambito'] == 'total'), ('equipo', lambda x: x['ambito'] != 'total')):
        S = [x for x in L if filt(x)]
        R[nombre] = {'todas': resumen(S)}
        # situación (solo partidos con banderas = lectura real de la situación)
        for campo in ('sit', 'dat'):
            R[nombre][campo] = {ETQ[k]: resumen([x for x in S if x[campo] == k]) for k in (1, 0, -1)}
            R[nombre][campo + '_cuota_1.50+'] = {ETQ[k]: resumen([x for x in S if x[campo] == k and x['cuota'] >= 1.5]) for k in (1, 0, -1)}
            R[nombre][campo + '_cumple'] = {ETQ[k]: resumen([x for x in S if x[campo] == k and x['cumple']]) for k in (1, 0, -1)}
            R[nombre][campo + '_por_mercado'] = {m: {ETQ[k]: resumen([x for x in S if x[campo] == k and x['mercado'] == m]) for k in (1, -1)}
                                                  for m in MERC if any(x['mercado'] == m for x in S)}
        R[nombre]['ambos_a_favor'] = resumen([x for x in S if x['sit'] == 1 and x['dat'] == 1])
        R[nombre]['sit_favor_dat_contra'] = resumen([x for x in S if x['sit'] == 1 and x['dat'] == -1])
        R[nombre]['sit_a_favor_cumple_1.50+'] = resumen([x for x in S if x['sit'] == 1 and x['cumple'] and x['cuota'] >= 1.5])
        R[nombre]['sit_a_favor_cumple_1.70+'] = resumen([x for x in S if x['sit'] == 1 and x['cumple'] and x['cuota'] >= 1.7])
        R[nombre]['dat_a_favor_cumple_1.50+'] = resumen([x for x in S if x['dat'] == 1 and x['cumple'] and x['cuota'] >= 1.5])
        R[nombre]['cumple_1.50+ (referencia)'] = resumen([x for x in S if x['cumple'] and x['cuota'] >= 1.5])
    json.dump(R, open(os.path.join(RAIZ, 'registro', 'medicion_contexto.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    # resumen legible
    def fila(k, v):
        if not v:
            return f"| {k} | 0 | | | |"
        return f"| {k} | {v['n']} | {v['acierto']*100:.1f} % | {v['precio']*100:.1f} % | {v['dif']*100:+.1f} (± {v['se']*100:.1f}) |"
    md = ['# ¿El contexto separa aciertos de fallos?', '', f"Líneas calificadas medidas: {len(L)} (cumplió/falló; sin nulas). Diferencia = acierto real − probabilidad del precio, en puntos; entre paréntesis un error estándar.", '']
    for nombre in ('total', 'equipo'):
        md += [f"## Líneas de {'total del partido' if nombre == 'total' else 'un equipo'}", '', '| grupo | n | acierto | precio | dif. (pts) |', '|---|---|---|---|---|', fila('todas', R[nombre]['todas'])]
        for campo, tit in (('sit', 'situación (notas)'), ('dat', 'datos (ficha)')):
            for k in ('a favor', 'sin factor', 'en contra'):
                md.append(fila(f"{tit} · {k}", R[nombre][campo][k]))
            for k in ('a favor', 'en contra'):
                md.append(fila(f"{tit} · {k} · cuota ≥ 1,50", R[nombre][campo + '_cuota_1.50+'][k]))
        for k in ('ambos_a_favor', 'sit_favor_dat_contra', 'sit_a_favor_cumple_1.50+', 'sit_a_favor_cumple_1.70+', 'dat_a_favor_cumple_1.50+', 'cumple_1.50+ (referencia)'):
            md.append(fila(k, R[nombre][k]))
        md.append('')
    md += ['## Cobertura de notas (partidos con lectura de la situación)', '', '| jornada | partidos con líneas calificadas | con notas | con banderas de situación |', '|---|---|---|---|']
    for c in cob:
        md.append(f"| {c['jornada']} | {c['partidos']} | {c['con_notas']} | {c['con_banderas']} |")
    open(os.path.join(RAIZ, 'registro', 'medicion_contexto.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
    print('\n'.join(md))


if __name__ == '__main__':
    main()
