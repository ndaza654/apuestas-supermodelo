# -*- coding: utf-8 -*-
"""Guiones del partido. Cada partido simulado cae en un solo guion; así se ve qué línea aguanta en cuál.

Por qué existe: en el balance del 4–8 nov la mayoría de las selecciones perdidas no fallaron por el promedio del
equipo, sino porque el partido tomó un guion que la línea no soportaba (Medellín marcó al 16′ y se replegó;
Toulouse se adelantó al 45+1′ y dejó de rematar; Palmeiras ganaba 4-1 al 36′ y bajó el ritmo). Medir la
probabilidad de la línea DENTRO de cada guion separa las líneas robustas de las que dependen de un solo guion.
"""
import numpy as np
from . import config as C

GUIONES = [
    'Expulsión antes del 70′',
    'Sorpresa: gana el no favorito',
    'Partido abierto (ambos marcan y 3+ goles)',
    'Favorito golpea temprano y gana',
    'Favorito gana en partido trabado',
    'Empate',
]


def favorito(sim):
    """Equipo con más probabilidad de ganar en la simulación (0 local, 1 visitante)."""
    d = sim[0]['g'] - sim[1]['g']
    return 0 if (d > 0).mean() >= (d < 0).mean() else 1


def asignar(sim):
    fav = favorito(sim)
    gf, gd = sim[fav]['g'], sim[1 - fav]['g']
    tot = gf + gd
    n = len(gf)
    lab = np.full(n, 5, dtype=np.int8)                        # empate por defecto
    gana_fav = gf > gd
    temprano = (sim['primer_eq'] == fav) & (sim['primer_min'] <= C.GOL_TEMPRANO_MIN)
    lab[gana_fav] = 4
    lab[gana_fav & temprano] = 3
    lab[(gf > 0) & (gd > 0) & (tot >= 3)] = 2
    lab[gd > gf] = 1
    lab[sim['roja_min'] < 70] = 0
    return lab, fav


def tabla(sim):
    lab, fav = asignar(sim)
    p = np.bincount(lab, minlength=len(GUIONES)) / len(lab)
    return lab, fav, p


def por_guion(ev, lab, p_guion):
    """P(evento | guion) para cada guion con peso relevante, y la robustez (mínimo entre guiones relevantes)."""
    out = {}
    for i, nombre in enumerate(GUIONES):
        m = lab == i
        if m.sum() < 200:
            continue
        out[nombre] = float(ev[m].mean())
    rel = [out[GUIONES[i]] for i in range(len(GUIONES)) if p_guion[i] >= C.UMBRAL_ESCENARIO_RELEVANTE and GUIONES[i] in out]
    rob = min(rel) if rel else float(ev.mean())
    mejor = max(out, key=out.get) if out else None
    peor = min(out, key=out.get) if out else None
    return out, rob, mejor, peor


def tipo_de_partido(sim, lam_total=None):
    """Etiqueta del tipo de partido ANTES de jugarse (para aprender qué mercados funcionan en cada tipo)."""
    d = sim[0]['g'] - sim[1]['g']
    pf = max((d > 0).mean(), (d < 0).mean())
    fuerza = 'Favorito claro' if pf >= 0.60 else ('Favorito leve' if pf >= 0.45 else 'Parejo')
    g = (sim[0]['g'] + sim[1]['g']).mean() if lam_total is None else lam_total
    gol = 'abierto' if g >= 2.9 else ('cerrado' if g <= 2.3 else 'medio')
    duro = (sim[0]['f'] + sim[1]['f']).mean() + 3 * (sim[0]['tarjetas'] + sim[1]['tarjetas']).mean()
    dureza = 'caliente' if duro >= 39 else ('limpio' if duro <= 31 else 'normal')
    return f'{fuerza} · {gol} · {dureza}'
