# -*- coding: utf-8 -*-
"""Informe en Markdown de un análisis (para pegar en el chat del proyecto o guardar junto al registro)."""


def _colchon(z):
    """Distancia entre la media simulada y la línea, en desviaciones típicas (+ = a favor de la selección)."""
    return '—' if z is None else f'{z:+.1f}'


def _pct(x):
    return '—' if x is None else f'{x * 100:.0f} %'


NOMBRE_FAMILIA = {'goles': 'Goles', 'ambos': 'Ambos marcan', 'resultado': 'Resultado y hándicap', 'corners': 'Córners',
                  'tarjetas': 'Tarjetas', 'faltas': 'Faltas', 'remates': 'Remates', 'al_arco': 'Tiros al arco',
                  'fueras': 'Fueras de lugar', 'saques_meta': 'Saques de meta', 'saques_banda': 'Saques de banda',
                  'jugador': 'Jugadores', 'pareja': 'Parejas de jugadores', 'especial': 'Quién saca más'}


def lectura_por_mercado(L, lin, cuota_min=1.25):
    """Para cada mercado: la línea que mejor encaja con ESTE partido (probabilidad y robustez, sin ser cara),
    el guion donde brilla y el guion que la mata. Es la lectura del partido mercado por mercado, no una regla."""
    filas = []
    for fam in NOMBRE_FAMILIA:
        cand = [r for r in lin if r['familia'] == fam and r['cuota'] >= cuota_min and r['ev'] >= -0.06]
        if not cand:
            continue
        r = max(cand, key=lambda r: 0.5 * r['p'] + 0.5 * r['robustez'] + 0.5 * max(0.0, r['ev']))
        pg = r.get('por_guion') or {}
        bri = f"{r['mejor_guion']} ({_pct(pg.get(r['mejor_guion']))})" if r.get('mejor_guion') else '—'
        mat = f"{r['peor_guion']} ({_pct(pg.get(r['peor_guion']))})" if r.get('peor_guion') else '—'
        rob = '(lo define el marcador)' if fam in ('goles', 'ambos', 'resultado') else _pct(r['robustez'])
        filas.append(f"| {NOMBRE_FAMILIA[fam]} | {r['seleccion']} | {r['cuota']:.2f} | {_pct(r['p'])} | {rob} | "
                     f"{bri} | {mat} | {r['etiqueta']} |")
    if not filas:
        return
    L.append('## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)')
    L.append('| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |')
    L.append('|---|---|---|---|---|---|---|---|')
    L.extend(filas)
    L.append('')
    L.append('Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.')
    L.append('')


def markdown(A, max_lineas=25):
    L = []
    L.append(f"# {A['partido']}")
    if A.get('liga') or A.get('fecha'):
        L.append(f"{A.get('liga') or ''} · {A.get('fecha') or ''}")
    L.append('')
    L.append(f"**Tipo de partido:** {A['tipo']} · **Favorito:** {A['favorito']} · "
             f"primer gol: local {_pct(A['p_primer_gol']['local'])}, visitante {_pct(A['p_primer_gol']['visitante'])}, "
             f"nadie {_pct(A['p_primer_gol']['nadie'])} · gol del favorito antes del 35′: {_pct(A['p_gol_temprano_favorito'])}")
    L.append('')
    if A.get('liga_base'):
        L.append(f"**Base de la liga:** {A['liga_base']}")
        L.append('')
    if A.get('alertas'):
        L.append('## ⚠ Alertas (revisar antes de usar las líneas marcadas)')
        for a in A['alertas']:
            L.append(f'- {a}')
        L.append('')
    if A.get('enfoque'):
        from .enfoque import markdown as _enf_md
        L.extend(_enf_md(A['enfoque'], A['enfoque_resumen']))
    L.append('## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)')
    L.append('| Guion | Probabilidad |')
    L.append('|---|---|')
    for g, p in sorted(A['guiones'].items(), key=lambda x: -x[1]):
        L.append(f'| {g} | {_pct(p)} |')
    L.append('')
    if A.get('contexto'):
        L.append('## Lo que cambió el contexto')
        for n in A['contexto']:
            L.append(f'- {n}')
        L.append('')
    if A.get('historial_vs_mercado'):
        L.append('**Historial contra mercado (diferencia ≥15 %, revisar el dato o buscar el porqué):** ' +
                 ', '.join(f'{k} ×{v}' for k, v in A['historial_vs_mercado'].items()))
        L.append('')
    L.append('## Medias esperadas (con contexto)')
    L.append('| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |')
    L.append('|---|---|---|---|---|---|---|')
    for lado in ('local', 'visitante'):
        o = A['objetivos'][lado]
        L.append(f"| {lado} | {o['g']:.2f} | {o['sh']:.1f} | {o['sot']:.1f} | {o['c']:.1f} | {o['f']:.1f} | {o['y']:.1f} |")
    L.append('')
    if A.get('medias'):
        nombres = {'goles': 'Goles', 'corners': 'Córners', 'tarjetas': 'Tarjetas (amarilla 1, roja 2)', 'remates': 'Remates', 'al_arco': 'Tiros al arco',
                   'faltas': 'Faltas', 'fueras': 'Fueras de lugar', 'saques_meta': 'Saques de meta', 'saques_banda': 'Saques de banda',
                   'atajadas': 'Atajadas del portero'}
        idx = {(r['mercado'], r['ambito']): r for r in A['medias']}
        L.append('## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)')
        L.append('| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |')
        L.append('|---|---|---|---|---|---|')
        for m, nm in nombres.items():
            celdas = []
            for a in ('total', 'local', 'visitante', '1T', '2T'):
                r = idx.get((m, a))
                if not r:
                    celdas.append('—')
                    continue
                bt = f" ({r['betano']:.1f})" if r.get('betano') is not None else ''
                celdas.append(f"{r['modelo']:.1f}{bt} · {r['p10']:g}–{r['p90']:g}")
            if any(c != '—' for c in celdas):
                L.append(f"| {nm} | " + ' | '.join(celdas) + ' |')
        L.append('')
    lin = A['lineas']
    def tabla(titulo, filas):
        if not filas:
            return
        L.append(f'## {titulo}')
        L.append('| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |')
        L.append('|---|---|---|---|---|---|---|---|---|---|---|---|')
        for r in filas:
            L.append(f"| {r['seleccion']} | {r['cuota']:.2f} | {_pct(r['p'])} | {_pct(r['p_mercado'])} | {_pct(r['p_sin_contexto'])} | "
                     f"{r['movimiento_contexto'] * 100:+.0f} pts | {r['ev'] * 100:+.0f} % | {_pct(r['robustez'])} | {_colchon(r.get('colchon_z'))} | {r['cuota_minima']:.2f} | "
                     f"{r['peor_guion'] or '—'} | {r['etiqueta']} |")
        L.append('')
    alta = sorted([r for r in lin if 'Alta probabilidad' in r['etiqueta'] and r['cuota'] >= 1.25], key=lambda r: -r['p'])[:max_lineas]
    ctx = sorted([r for r in lin if 'Contexto a favor' in r['etiqueta']], key=lambda r: -r['movimiento_contexto'])[:max_lineas]
    val = sorted([r for r in lin if 'Valor' in r['etiqueta']], key=lambda r: -r['ev'])[:max_lineas]
    lectura_por_mercado(L, lin)
    tabla('Alta probabilidad y robustas (aguantan en los guiones principales)', alta)
    tabla('Donde el contexto mueve la línea a tu favor', ctx)
    tabla('Con valor según el modelo', val)
    if val:
        L.append('Kelly ¼ (dato informativo, no una orden de stake): ' + '; '.join(
            f"{x['seleccion']} {x.get('kelly_cuarto', 0) * 100:.1f} % de la banca" for x in val[:8]) +
            '. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.')
        L.append('')
    if A.get('sistemas'):
        L.append('## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)')
        L.append('| Sistema | Regla | Selección que propone | Historial con cuotas reales |')
        L.append('|---|---|---|---|')
        for x in A['sistemas']:
            L.append(f"| {x['fuente']} | {x['regla']} | {x['seleccion']} | {x['historial']} |")
        L.append('')
    if A.get('combos'):
        from .combos import tabla_md
        L.append('## Combos con la cuota del cupón')
        L.append(tabla_md(A['combos']))
        if (A.get('cartera') or {}).get('aviso'):
            L.append('')
            L.append('⚠ ' + A['cartera']['aviso'])
        L.append('')
    if A.get('builders'):
        L.append('## Builders del mismo guion')
        L.append('| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |')
        L.append('|---|---|---|---|---|---|---|---|---|---|')
        for b in A['builders']:
            L.append(f"| {' + '.join(b['patas'])} | {_pct(b['p'])} | {_pct(b.get('p_sim'))} | {_pct(b.get('p_stress'))} | {b['cuota_justa']:.2f} | {b['cuota_minima']:.2f} | "
                     f"{b['correlacion']} | {_pct(b.get('margen_acumulado'))} | {b['guion_comun']} | {_pct(b['robustez'])} |")
            if b.get('avisos'):
                L.append(f"| ↳ {' · '.join(b['avisos'])} |  |  |  |  |  |  |  |  |  |")
        L.append('')
        L.append('Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la '
                 'dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de '
                 'lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.')
        L.append('')
        L.append('Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). '
                 'Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.')
        L.append('')
        L.append('Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. '
                 'Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.')
    return '\n'.join(L)
