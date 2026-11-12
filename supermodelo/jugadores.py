# -*- coding: utf-8 -*-
"""Mercados de jugador dentro del mismo partido simulado.

Cada jugador recibe una parte (share) de lo que hace su equipo mientras está en cancha. Como los totales del
equipo salen del simulador, la línea del jugador hereda el guion: el delantero del equipo que se adelanta y se
repliega remata menos; el portero del equipo que aguanta ataja más; el mediocampista del equipo que no tiene la
pelota hace más entradas. Y el builder "equipo Más al arco + su delantero 2+ al arco" sale correlacionado solo.

Lecciones del balance que el modelo incorpora:
  · minutos: sin titularidad confirmada la probabilidad baja (Thomas-Asante entró al 73′; Alajbegović salió al 60′).
  · rol: un mediocampista tiene poca parte de los remates al arco (Rabiot 0, Alajbegović 0).
  · entradas y faltas dependen de cuánto ataque el RIVAL, no del jugador solo.
"""
import math
import numpy as np
from scipy.stats import nbinom
from scipy.optimize import minimize_scalar

VIG_JUGADOR = 1.12   # margen típico de Betano en líneas de jugador de un solo lado (10–17 %)


def fraccion_activa(n, rng, titular=0.9, minutos=85, entra_prob=0.6, minutos_sup=22):
    """Fracción del partido (sobre 95′) que juega en cada simulación."""
    es_tit = rng.random(n) < titular
    mt = np.clip(rng.normal(minutos, 12, n), 15, 95)
    entra = rng.random(n) < entra_prob
    ms = np.clip(rng.normal(minutos_sup, 8, n), 5, 45) * entra
    return np.where(es_tit, mt, ms) / 95.0


def simular(sim, specs, rng):
    """specs: lista de dicts {'nombre','lado':'local'|'visitante','titular','minutos','portero', 'shares':{...}}.
    shares (de lo que hace el equipo en 90′): sh, sot, g, a, f, tk, y."""
    out = {}
    n = len(sim[0]['g'])
    for p in specs:
        l = 0 if p['lado'] == 'local' else 1
        R = sim[l]
        af = fraccion_activa(n, rng, p.get('titular', 0.9), p.get('minutos', 85))
        if p.get('fuera'):      # baja confirmada: no juega nada (las parejas «cualquiera de…» cuentan solo al otro)
            z = np.zeros(n, dtype=int)
            out[p['nombre']] = {k: z for k in ('remates', 'al_arco', 'anota', 'anota_o_asiste', 'asiste', 'faltas', 'entradas', 'tarjeta')}
            continue
        if p.get('portero'):
            # El portero puede traer también línea de tarjeta en Betano (12-nov): se simula con su parte de las tarjetas del
            # equipo (por defecto 2 %); el resto de estadísticas de campo quedan en cero.
            z = np.zeros(n, dtype=int)
            d = {k: z for k in ('remates', 'al_arco', 'anota', 'anota_o_asiste', 'asiste', 'faltas', 'entradas')}
            d['atajadas'] = np.round(R['sv'] * np.minimum(1, af * 95 / 90)).astype(int)
            d['tarjeta'] = rng.binomial(R['tarjetas'], np.clip(p.get('shares', {}).get('y', 0.02) * af, 0, 1))
            out[p['nombre']] = d
            continue
        s = p.get('shares', {})
        sh_s = s.get('sh', 0.15)
        sot_s = s.get('sot', sh_s)
        g_s = s.get('g', sot_s)
        b = lambda tot, sh: rng.binomial(tot, np.clip(sh * af, 0, 1))
        goles = b(R['g'], g_s)
        asist = rng.binomial(np.maximum(R['g'] - goles, 0), np.clip(s.get('a', 0.12) * af, 0, 1))
        out[p['nombre']] = {
            'remates': b(R['sh'], sh_s),
            'al_arco': b(R['sot'], sot_s),
            'anota': goles,
            'anota_o_asiste': goles + asist,
            'asiste': asist,
            'faltas': b(R['f'], s.get('f', 0.09)),
            'entradas': b(R['tk'], s.get('tk', 0.10)),
            'tarjeta': b(R['tarjetas'], s.get('y', s.get('f', 0.09))),
        }
    return out


def media_implicita_jugador(escalera, r=8.0):
    """escalera {k: cuota} de '1+, 2+, 3+...' (un solo lado): media que pone Betano, quitando ~12 % de margen."""
    ks = sorted(escalera)
    pk = [min(0.97, (1 / escalera[k]) / VIG_JUGADOR) for k in ks]
    f = lambda mu: sum((float(1 - nbinom.cdf(k - 1, r, r / (r + mu))) - p) ** 2 for k, p in zip(ks, pk))
    return float(minimize_scalar(f, bounds=(0.02, 15), method='bounded').x)


def share_desde_betano(escalera, media_equipo, minutos=85, r=8.0):
    """Parte del equipo que Betano le asigna al jugador (por 90′), a partir de su escalera y la media del equipo."""
    mu = media_implicita_jugador(escalera, r)
    return min(0.8, mu / max(media_equipo * minutos / 95.0, 1e-6))


def share_asist_desde_cuota(cuota_asiste, goles_equipo, minutos=85, vig=1.15):
    """Parte de las asistencias del equipo (≈ 0,75 de sus goles) que Betano le da al jugador a partir de «da una asistencia 1+»."""
    p = min(0.95, (1 / cuota_asiste) / vig)
    lam = -math.log(1 - p)
    return min(0.6, lam / max(0.75 * goles_equipo * minutos / 95.0, 1e-6))


def share_gol_desde_cuota(cuota_anota, goles_equipo, minutos=85, vig=1.15):
    p = min(0.95, (1 / cuota_anota) / vig)
    lam = -math.log(1 - p)
    return min(0.8, lam / max(goles_equipo * minutos / 95.0, 1e-6))
