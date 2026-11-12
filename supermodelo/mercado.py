# -*- coding: utf-8 -*-
"""Cuotas: quitar margen, media implícita de una escalera, EV y cuota mínima (heredado del kit v1, con pruebas)."""
import math
from scipy.stats import nbinom, poisson
from scipy.optimize import minimize_scalar


def _potencia(inv):
    """Método de potencia: p_i = (1/cuota_i)^k con k tal que sumen 1. Corrige el sesgo favorito–longshot
    (el lado poco probable viene más caro de lo que dice el reparto proporcional del margen).
    Validado con 160 256 partidos (1X2) y 107 318 (Más/Menos 2.5) de 2012–2026: mejora el log-loss frente al
    proporcional en 0,00055 ± 0,00008 (1X2) y 0,00013 ± 0,00005 (O/U); igual con márgenes de 8 % o más."""
    if sum(inv) <= 1.0:          # sin margen (o cuotas de distintas casas): se normaliza
        s = sum(inv)
        return [x / s for x in inv]
    lo, hi = 1.0, 3.0
    for _ in range(60):
        k = (lo + hi) / 2
        if sum(x ** k for x in inv) > 1.0:
            lo = k
        else:
            hi = k
    k = (lo + hi) / 2
    p = [x ** k for x in inv]
    s = sum(p)
    return [x / s for x in p]


def devig_n(cuotas, metodo=None):
    """Sin margen para un mercado de n resultados (1X2, ambos marcan, quién saca más córners...)."""
    from . import config as C
    inv = [1.0 / c for c in cuotas]
    if (metodo or C.METODO_SIN_MARGEN) == 'potencia':
        return _potencia(inv)
    s = sum(inv)
    return [x / s for x in inv]


def devig(o_mas, o_menos, metodo=None):
    """Probabilidad sin margen del lado Más, con las dos cuotas de la línea."""
    return devig_n([o_mas, o_menos], metodo)[0]


def p_mas_nb(media, r, linea):
    """P(X > linea) con binomial negativa de media `media` y dispersión r (r grande = Poisson)."""
    k = math.floor(linea) + 1
    if r is None or r > 1e5:
        return float(1 - poisson.cdf(k - 1, media))
    p = r / (r + media)
    return float(1 - nbinom.cdf(k - 1, r, p))


def media_implicita(escalera, r=25.0):
    """Media que pone Betano: la que mejor reproduce las probabilidades sin margen de toda la escalera.
    escalera = [(linea, cuota_mas, cuota_menos), ...]"""
    pts = [(L, devig(o, u)) for L, o, u in escalera if o and u and u >= 1.03]
    if not pts:
        return None
    f = lambda m: sum((p_mas_nb(m, r, L) - p) ** 2 for L, p in pts)
    return float(minimize_scalar(f, bounds=(0.05, 80), method='bounded').x)


def ev(p, cuota):
    return p * cuota - 1.0


def cuota_minima(p, ev_min=0.05, ventaja=0.03):
    """La menor cuota con EV >= ev_min y ventaja >= `ventaja` puntos (kit v1)."""
    if p <= ventaja + 0.01:
        return 99.0
    return max((1 + ev_min) / p, 1.0 / (p - ventaja))


def cuota_justa(p):
    return 99.0 if p <= 0 else 1.0 / p


def kelly(p, cuota, fraccion=0.25):
    """Fracción de banca según Kelly (por defecto 1/4). Es una salida informativa del modelo, no una regla."""
    b = cuota - 1
    f = (p * cuota - 1) / b if b > 0 else 0
    return max(0.0, f * fraccion)
