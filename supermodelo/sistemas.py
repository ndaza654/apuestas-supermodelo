# -*- coding: utf-8 -*-
"""Sistemas de tipsters (Ingeniero Analista, Jeke, Sharpods): qué partidos los cumplen y cómo les fue con cuotas reales.

NO filtran ni mueven probabilidades: etiquetan el partido para que el registro mida, con TUS datos y TUS cuotas de
Betano, si el sistema aporta algo. El historial viene de la auditoría con 160 000+ partidos con cuota (38 ligas,
ago-2012 → 2026; datos/sistemas_historial.json): ninguno superó el margen a cuota media; con la mejor cuota del
mercado varios quedan cerca de 0 %, o sea que el precio que se toma (CLV) pesa más que el filtro.

Condiciones que necesitan datos fuera de las cuotas (rachas, H2H, centros, árbitro) se leen de la ficha si están:
  ficha["rachas"] = {"local": {"btts_seguidos": 2, "victorias_seguidas": 0}, "visitante": {...}}
  ficha["h2h_empates_ult5"] = 2
  ficha["ultimo_tabla"] = "local" | "visitante" | null
"""
import json, os
from . import ligas

RUTA = os.path.join(os.path.dirname(__file__), '..', 'datos', 'sistemas_historial.json')
_H = None


def _historial():
    global _H
    if _H is None:
        try:
            d = json.load(open(RUTA, encoding='utf-8'))
            _H = {x['sistema']: x for x in d.get('sistemas', []) + d.get('ambos', [])}
        except OSError:
            _H = {}
    return _H


def _txt_hist(clave):
    h = _historial().get(clave)
    if not h:
        return 'sin historial con cuotas (medir en el registro)'
    if 'roi' in h:
        t = (f"{h['n']} partidos: acierto {h['acierto'] * 100:.1f} % contra {h['implicita'] * 100:.1f} % del precio; "
             f"ROI {h['roi'] * 100:+.1f} % ± {h['ic95'] * 100:.1f}")
        if h.get('roi_cuota_max') is not None:
            t += f" (con la mejor cuota {h['roi_cuota_max'] * 100:+.1f} %)"
        return t
    return (f"{h['n']} partidos: Ambos Sí {h['acierto'] * 100:.1f} % contra {h['estimada_mercado'] * 100:.1f} % que ya da el precio "
            f"({h['dif_pts']:+.1f} pts ± {h['ic95_pts']:.1f})")


def _cuotas(e):
    bet = e.get('betano') or {}
    x12 = next((u['opciones'] for u in bet.get('unicos', []) if u.get('mercado') == 'resultado'), {}) or {}
    amb = next((u['opciones'] for u in bet.get('unicos', []) if u.get('mercado') == 'ambos'), {}) or {}
    lin = {(l['mercado'], l.get('ambito', 'total'), float(l['linea'])): l for l in bet.get('lineas', []) if l.get('linea') is not None}
    g = lambda m, a, L, lado: (lin.get((m, a, L)) or {}).get(lado)
    return dict(h=x12.get('1'), x=x12.get('X'), a=x12.get('2'), o25=g('goles', 'total', 2.5, 'mas'), u25=g('goles', 'total', 2.5, 'menos'),
                o15=g('goles', 'total', 1.5, 'mas'), o15_1t=g('goles', '1T', 1.5, 'mas'), btts=amb.get('si'))


def evaluar(e):
    """Lista de sistemas que el partido cumple: [{id, fuente, regla, seleccion, historial}]."""
    q = _cuotas(e)
    f = e.get('ficha') or {}
    ra = f.get('rachas') or {}
    rl, rv = ra.get('local') or {}, ra.get('visitante') or {}
    cod = ligas.codigo(e.get('liga'))
    pri = ligas.prior(e.get('liga')) or {}
    out = []

    def add(id_, fuente, regla, sel, clave_hist=None):
        out.append(dict(id=id_, fuente=fuente, regla=regla, seleccion=sel, historial=_txt_hist(clave_hist) if clave_hist else 'sin historial con cuotas (medir en el registro)'))
    h, x, a = q['h'], q['x'], q['a']
    if h and h <= 1.50 and q['o15_1t'] and q['o15_1t'] <= 2.15:
        add('IA400', 'Ingeniero Analista #400', 'local ≤1,50 y 1T Más 1.5 ≤2,15', 'Goles Más 2.5', 'IA #400: local ≤1,50 → Más 2.5 (sin el filtro 1T, no está en datos)')
    if h and x and h <= 1.50 and x >= 4.10:
        add('IA453', 'Ingeniero Analista #453', 'local ≤1,50 y empate ≥4,10', 'Goles Más 2.5', 'IA #453: local ≤1,50 y empate ≥4,10 → Más 2.5')
    if x and x >= 3.60:
        add('IA14', 'Ingeniero Analista #5/#14', 'empate ≥3,60 (señal de goles)', 'Goles Más 2.5', 'IA #5/#14: empate ≥3,60 → Más 2.5')
    if x and 2.90 <= x <= 3.20:
        add('IA5U', 'Ingeniero Analista #5', 'empate 2,90–3,20 (señal de pocos goles)', 'Goles Menos 2.5', 'IA #5: empate 2,90–3,20 → Menos 2.5')
    if h and a and h >= 2.0 and a >= 2.0 and (q['o15'] is None or q['o15'] > 1.40):
        add('IA26', 'Ingeniero Analista #26', 'parejo (ambos ≥2,00) y Más 1.5 >1,40', 'Goles Menos 2.5', 'IA #26: ambos ≥2,00 (parejo) → Menos 2.5')
    if cod == 'D1' and x and 3.60 <= x <= 4.33 and h and a and h >= 2.0 and a >= 2.0:
        h2h = f.get('h2h_empates_ult5')
        if h2h is not None and h2h >= 2:
            add('IA45', 'Ingeniero Analista #45', 'Bundesliga, empate 3,60–4,33, ambos ≥2,00, ≥2 empates en los últimos 5 H2H', 'Empate',
                'IA #45 completo: + ≥2 empates en los últimos 5 H2H → Empate')
        else:
            add('IA45p', 'Ingeniero Analista #45 (sin H2H)', 'Bundesliga, empate 3,60–4,33, ambos ≥2,00', 'Empate', 'IA #45: Bundesliga, empate 3,60–4,33, ambos ≥2,00 → Empate')
    if x and x <= 3.40 and h and a and h >= 2.0 and a >= 2.0 and not ((rl.get('victorias_seguidas') or 0) >= 2 or (rv.get('victorias_seguidas') or 0) >= 2):
        add('IA420', 'Ingeniero Analista #420', 'empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas', 'Empate',
            'IA #420: empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas → Empate (todas las ligas)')
    if x and a and x >= 3.90 and a <= 2.00:
        if (rl.get('btts_seguidos') or 0) >= 2:
            add('IA429', 'Ingeniero Analista #429', 'empate ≥3,90, visitante ≤2,00, local con 2 Ambos Sí seguidos', 'Ambos marcan: Sí',
                'IA #429: empate ≥3,90, visitante ≤2,00, local con 2 BTTS seguidos → Ambos Sí')
        else:
            add('IA429p', 'Ingeniero Analista #429 (sin racha)', 'empate ≥3,90, visitante ≤2,00', 'Ambos marcan: Sí', 'IA #429 sin la racha')
    if q['o25'] and q['o25'] <= 1.80 and (q['btts'] is None or q['btts'] <= 1.75) and (pri.get('pct_ambos_marcan') or 0) >= 0.55:
        add('IA16', 'Ingeniero Analista #16', 'liga con Ambos Sí ≥55 %, Más 2.5 ≤1,80 y Ambos Sí ≤1,75', 'Ambos marcan: Sí', 'IA #16 (parcial): Más 2.5 ≤1,80 → Ambos Sí')
    if q['o25'] and q['o25'] <= 1.45:
        add('IA313', 'Ingeniero Analista #313', 'Más 2.5 ≤1,45 → gol en el 1.er tiempo', 'Goles 1.er tiempo Más 0.5')
    cl = (f.get('local') or {}).get('perfil_corners') or {}
    cv = (f.get('visitante') or {}).get('perfil_corners') or {}
    if (cl.get('centros_pj') or 0) >= 20 and (cv.get('centros_pj') or 0) >= 20:
        add('IA415', 'Ingeniero Analista #415', 'ambos equipos con ≥20 centros por partido', 'Córners Más (línea 9–10)')
    arb = f.get('arbitro') or {}
    pts = sum([bool(arb.get('tarjetas_por_partido') and arb.get('media_liga') and arb['tarjetas_por_partido'] > arb['media_liga']),
               bool(f.get('derbi')), bool((f.get('local') or {}).get('necesita_ganar') and (f.get('visitante') or {}).get('necesita_ganar')),
               f.get('importancia') in ('alta', 'final')])
    if pts >= 3:
        add('IA456', 'Ingeniero Analista #456', f'{pts} de 4 señales de tarjetas (árbitro, rivalidad, ambos necesitan, importancia)', 'Tarjetas Más')
    ult = f.get('ultimo_tabla')
    if ult in ('local', 'visitante'):
        clave = 'Jeke: contra el último (último de visita → gana el local)' if ult == 'visitante' else 'Jeke: contra el último (último de local → gana el visitante)'
        add('JEKE_ULT', 'JekeDeportivas', f'el {ult} es último de la tabla', f"Gana {'local' if ult == 'visitante' else 'visitante'}", clave)
    return out
