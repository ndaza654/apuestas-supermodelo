# -*- coding: utf-8 -*-
"""Seguimiento en sombra de fuentes externas (sin apostar): StatArea, Forebet, la app de Sharpods, Ingeniero Analista,
Jeke, picks de TikTok/Telegram... Con la hora, la cuota de Betano en ese momento y el resultado.

Por qué: ninguna fuente revisada tiene un historial verificado y rentable por mercado (Tips.GG: 4 de 73 servicios con
>1.000 pronósticos en ganancia; TipsAudit: 0 de 9 baten el cierre). La única manera honesta de saber si una aporta es
medirla con NUESTRAS cuotas de Betano y contra el mercado sin margen. Regla de decisión (no de apuesta): con menos de
300 picks por fuente y mercado el error típico del ROI es ±6 pts o más; antes de eso no se concluye nada.

Archivo: sombra.csv (';'). Columnas:
  fecha; partido; liga; fuente; mercado; seleccion; prob_fuente (0–1, si la fuente da porcentaje); es_pick (Sí/No);
  cuota_betano; p_mercado (sin margen, la calcula el modelo si está la línea); cuota_cierre; resultado (1/0)
Uso:
  python3 -m supermodelo.sombra --informe sombra.csv
  python3 -m supermodelo.sombra --cerrar sombra.csv registro.csv     (copia resultados del registro por partido+selección)
"""
import csv, math, os, sys
from collections import defaultdict

CAMPOS = ['fecha', 'partido', 'liga', 'fuente', 'mercado', 'seleccion', 'prob_fuente', 'es_pick', 'cuota_betano',
          'p_mercado', 'cuota_cierre', 'resultado']


def agregar(ruta, filas):
    nuevo = not os.path.exists(ruta)
    with open(ruta, 'a', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, delimiter=';', extrasaction='ignore')
        if nuevo:
            w.writeheader()
        for r in filas:
            w.writerow(r)


def desde_analisis(A, fuente, picks, probs=None, fecha=None):
    """Arma filas de sombra a partir de un análisis: picks = nombres de selección que dio la fuente;
    probs = {seleccion: prob} si la fuente da porcentajes (StatArea, Forebet). La cuota y la p de mercado salen de A."""
    filas = []
    por_nombre = {r['seleccion']: r for r in A['lineas']}
    for nm in set(picks) | set((probs or {}).keys()):
        r = por_nombre.get(nm, {})
        filas.append(dict(fecha=fecha or A.get('fecha'), partido=A['partido'], liga=A.get('liga'), fuente=fuente,
                          mercado=r.get('submercado', ''), seleccion=nm, prob_fuente=(probs or {}).get(nm, ''),
                          es_pick='Sí' if nm in picks else 'No', cuota_betano=r.get('cuota', ''), p_mercado=r.get('p_mercado', ''),
                          cuota_cierre='', resultado=''))
    return filas


def cerrar_desde_registro(ruta_sombra, ruta_registro):
    """Copia el resultado (y la cuota de cierre) de las líneas del registro con el mismo partido y selección."""
    reg = {}
    for r in csv.DictReader(open(ruta_registro, encoding='utf-8-sig'), delimiter=';'):
        if r.get('resultado') in ('1', '0'):
            reg[(r['partido'], r['seleccion'])] = (r['resultado'], r.get('cuota_cierre', ''))
    filas = list(csv.DictReader(open(ruta_sombra, encoding='utf-8-sig'), delimiter=';'))
    n = 0
    for r in filas:
        k = (r['partido'], r['seleccion'])
        if r.get('resultado') in ('', None) and k in reg:
            r['resultado'], cc = reg[k]
            if cc and not r.get('cuota_cierre'):
                r['cuota_cierre'] = cc
            n += 1
    with open(ruta_sombra, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, delimiter=';', extrasaction='ignore')
        w.writeheader(); w.writerows(filas)
    return n


def informe(ruta, min_n=5):
    F = [r for r in csv.DictReader(open(ruta, encoding='utf-8-sig'), delimiter=';') if r.get('resultado') in ('1', '0')]
    if not F:
        return 'Sombra: sin picks cerrados todavía.'
    fl = lambda v: float(v) if v not in (None, '', 'None') else None
    g = defaultdict(list)
    for r in F:
        g[(r['fuente'], r.get('mercado') or '')].append(r)
        g[(r['fuente'], 'TODO')].append(r)
    L = [f'# Seguimiento en sombra: {len(F)} selecciones cerradas',
         '| Fuente | Mercado | n picks | Acierto | Prob. mercado media | ROI a cuota Betano | ± (95 %) | CLV | Brier fuente | Brier mercado | ¿Decidir? |',
         '|---|---|---|---|---|---|---|---|---|---|---|']
    for (fu, me), X in sorted(g.items(), key=lambda z: (z[0][0], z[0][1] != 'TODO', -len(z[1]))):
        P = [x for x in X if x.get('es_pick') == 'Sí' and fl(x.get('cuota_betano'))]
        Q = [x for x in X if fl(x.get('prob_fuente')) is not None]
        if len(P) < min_n and len(Q) < min_n:
            continue
        y = lambda x: 1 if x['resultado'] == '1' else 0
        if P:
            gan = [y(x) * fl(x['cuota_betano']) - 1 for x in P]
            m = sum(gan) / len(gan)
            sd = math.sqrt(sum((v - m) ** 2 for v in gan) / max(len(gan) - 1, 1))
            ic = 1.96 * sd / math.sqrt(len(gan))
            pm = [fl(x['p_mercado']) for x in P if fl(x.get('p_mercado')) is not None]
            clv = [fl(x['cuota_betano']) / fl(x['cuota_cierre']) - 1 for x in P if fl(x.get('cuota_cierre'))]
            ac = sum(y(x) for x in P) / len(P)
        bq = sum((fl(x['prob_fuente']) - y(x)) ** 2 for x in Q) / len(Q) if Q else None
        bm_ = [(fl(x['p_mercado']) - y(x)) ** 2 for x in Q if fl(x.get('p_mercado')) is not None]
        bm = sum(bm_) / len(bm_) if bm_ else None
        dec = 'no: muy pocos' if len(P) < 300 else ('sí: ROI > 0 con 95 %' if P and m - ic > 0 else 'sí: sin ventaja demostrada')
        f = lambda v, p=True: '—' if v is None else (f'{v * 100:.1f} %' if p else f'{v:.4f}')
        L.append(f"| {fu} | {me or '—'} | {len(P)} | {f(ac) if P else '—'} | {f(sum(pm) / len(pm)) if P and pm else '—'} | "
                 f"{f(m) if P else '—'} | {f(ic) if P else '—'} | {f(sum(clv) / len(clv)) if P and clv else '—'} | {f(bq, False)} | {f(bm, False)} | {dec} |")
    L.append('\nROI a 1 u plano con la cuota de Betano anotada al registrar el pick. «Decidir» exige ≥300 picks (error típico ±6 pts). '
             'Brier: solo si la fuente da porcentajes; si el de la fuente no baja del de mercado, sus porcentajes no aportan.')
    return '\n'.join(L)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--informe':
        print(informe(a[1]))
    elif a and a[0] == '--cerrar':
        print(f'{cerrar_desde_registro(a[1], a[2])} selecciones cerradas desde el registro')
    else:
        print(__doc__)
