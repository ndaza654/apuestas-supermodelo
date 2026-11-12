# -*- coding: utf-8 -*-
"""Puntuación de contexto de cada partido y filtro de los partidos aptos.

Dos puntuaciones SIEMPRE juntas (decisión del usuario, 12-nov-2026): lo mínimo es mirar las dos.
  · DATOS (0–100): ¿hay con qué analizar? Mercados que Betano ofrece, 7 partidos con estadística por equipo, alineaciones,
    historial de los jugadores con línea, árbitro y directos.
  · SITUACIÓN (0–100): ¿el partido tiene un guion legible? Importancia, derbi/eliminatoria, necesidad de ganar, rotación, favorito claro,
    bajas, clima, descanso. Si la ficha trae solo valores por defecto (nadie leyó la situación) se dice «situación sin leer» y no se premia.
Estados: APTO = datos ≥ 60 y situación ≥ 45; RESERVA = datos ≥ 60 pero la situación no está leída (hay que leerla antes de decidir); NO APTO = el resto.
Ninguno se descarta en silencio: todos salen en el ranking con el motivo.
Para los aptos se corre la ficha por mercado (córners, partido, jugadores) y se cuentan las líneas que cumplen 5 de 7 en ambos equipos.

Uso:  python3 recoleccion/puntuar.py jornadas/2026-11-12/pub/entradas [carpeta_salida]
Salida: ranking.json y ranking.md en la carpeta de salida (por defecto, junto a la carpeta de entradas).
"""
import json, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ficha as FI

UMBRAL_DATOS, UMBRAL_SITUACION = 60, 45


def probs_1x2(e):
    """Probabilidades 1X2 del mercado (quitando el margen por proporción), o None."""
    for u in (e.get('betano') or {}).get('unicos', []):
        if u.get('mercado') == 'resultado':
            o = u['opciones']
            if all(k in o for k in ('1', 'X', '2')):
                inv = {k: 1.0 / o[k] for k in ('1', 'X', '2')}
                s = sum(inv.values())
                return {k: v / s for k, v in inv.items()}
    return None


def puntuar_datos(e, F):
    """F = FI.construir(e). Solo cuentan las familias de mercado que Betano ofrece en ese partido (promedio de las ofrecidas).
    Devuelve (puntos, detalle, familias)."""
    bet = e.get('betano') or {}
    lineas = bet.get('lineas', [])
    det, fam = [], {}

    def cobertura(r):
        return (min(r.get('n_local', 0), 7) + min(r.get('n_visitante', 0), 7)) / 14
    n_c = sum(1 for l in lineas if l.get('mercado') == 'corners' and l.get('ambito') in ('total', 'local', 'visitante'))
    if n_c:
        fam['córners'] = round(100 * (0.7 * cobertura(F['corners']) + 0.3 * min(1, n_c / 8)))
        det.append(f"Córners: {n_c} líneas, muestra de 7 al {cobertura(F['corners']):.0%} → {fam['córners']}")
    else:
        det.append('Córners: Betano no ofrece líneas de equipo/total')
    ofrecidas = [m for m in FI.GRUPOS['partido'] if any(l.get('mercado') == m for l in lineas)]
    if ofrecidas:
        cp = sum(cobertura(F['partido'][m]) for m in ofrecidas) / len(ofrecidas)
        fam['partido'] = round(100 * (0.7 * cp + 0.3 * len(ofrecidas) / len(FI.GRUPOS['partido'])))
        det.append(f"Partido: {len(ofrecidas)}/6 familias ofrecidas, muestra al {cp:.0%} → {fam['partido']}")
    else:
        det.append('Partido: Betano no ofrece faltas, fueras, saques, remates ni tiros al arco')
    n_j = len({j['jugador'] for j in bet.get('jugadores', [])})
    js = [j for j in F['jugadores'] if j['stat'] in ('remates', 'al_arco')]
    if any(j.get('titular') is not None for j in F['jugadores']):      # hay alineación: solo cuentan los del XI probable (regla 1)
        xi = {j['jugador'] for j in F['jugadores'] if (j.get('titular') or 0) >= 0.6}
        js = [j for j in js if j['jugador'] in xi]
        n_j = len(xi)
    if n_j and js:
        con_hist = sum(1 for j in js if j['partidos_muestra'] >= 5) / len(js)
        con_xi = sum(1 for j in js if (j.get('titular') or 0) >= 0.6) / len(js)
        fam['jugadores'] = round(100 * (0.5 * con_hist + 0.3 * con_xi + 0.2 * min(1, n_j / 20)))
        det.append(f"Jugadores: {n_j} con línea, {con_hist:.0%} con ≥5 partidos de historial, {con_xi:.0%} titulares probables → {fam['jugadores']}")
    else:
        det.append('Jugadores: Betano no ofrece líneas de jugadores' if not n_j else 'Jugadores: sin escaleras de remates/tiros al arco')
    base = sum(fam.values()) / len(fam) if fam else 0
    a = (e.get('ficha') or {}).get('arbitro') or {}
    extra_a = 5 if (a.get('tarjetas_por_partido') and (a.get('partidos') or 0) >= 5) else 0
    nh = F['corners'].get('n_directos', 0)
    extra_h = 5 if nh >= 3 else 0
    det.append(f"Árbitro con promedio: {'+5' if extra_a else '0 (sin dato)'}; directos con estadística: {nh} ({'+5' if extra_h else '0'})")
    return round(min(100, base + extra_a + extra_h)), det, fam


def puntuar_situacion(e):
    F = e.get('ficha') or {}
    L, V = F.get('local') or {}, F.get('visitante') or {}
    pts, razones, leidas = 50.0, [], 0

    def suma(v, txt, lectura=True):
        """lectura=False: señal derivada de las cuotas o del modelo; ajusta el puntaje pero NO cuenta como «situación leída»."""
        nonlocal pts, leidas
        pts += v
        leidas += 1 if lectura else 0
        razones.append(f"{'+' if v >= 0 else ''}{v} {txt}")
    imp = F.get('importancia')
    if imp == 'alta': suma(15, 'importancia alta')
    elif imp == 'baja': suma(-15, 'importancia baja')
    if F.get('derbi'): suma(10, 'derbi')
    if F.get('eliminatoria'): suma(5, 'eliminatoria')
    if L.get('necesita_ganar') or V.get('necesita_ganar'): suma(10, 'un equipo necesita ganar')
    if L.get('rotacion') or V.get('rotacion'): suma(-15, 'rotación esperada')
    if 'baja' in (L.get('motivacion'), V.get('motivacion')): suma(-15, 'motivación baja')
    if 'alta' in (L.get('motivacion'), V.get('motivacion')): suma(8, 'motivación alta')
    p = probs_1x2(e)
    if p:
        if max(p['1'], p['2']) >= 0.60: suma(10, f"favorito claro ({max(p['1'], p['2']):.0%}, según cuotas)", lectura=False)
        elif max(p['1'], p['2']) <= 0.42: suma(5, 'partido parejo (según cuotas)', lectura=False)
    pc = [(x.get('perfil_corners') or {}) for x in (L, V)]
    if any((c.get('centros_pj') and c.get('centros_media_liga') and c['centros_pj'] >= 1.2 * c['centros_media_liga']) for c in pc):
        suma(8, 'un equipo centra mucho más que la media de su liga (córners)', lectura=False)
    fuertes = [b for b in (F.get('bajas') or []) if (b.get('peso') or 0) >= 0.3 and b.get('confirmada')]
    if fuertes: suma(-min(10, 5 * len(fuertes)), f"{len(fuertes)} baja(s) importante(s) confirmada(s)")
    if F.get('dudas'):                                              # las dudas restan, pero no cuentan como «situación leída»
        pts -= min(9, 3 * len(F['dudas']))
        razones.append(f"-{min(9, 3 * len(F['dudas']))} {len(F['dudas'])} duda(s) abierta(s) en la ficha")
    cl = F.get('clima') or {}
    if cl.get('lluvia') == 'fuerte' or cl.get('viento_fuerte'): suma(-8, 'clima que frena el juego')
    if any((x.get('dias_descanso') is not None and x['dias_descanso'] <= 3) for x in (L, V)): suma(-5, 'descanso ≤ 3 días')
    if L.get('viaje_largo') or V.get('viaje_largo'): suma(-5, 'viaje largo')
    sin_leer = (leidas == 0) or (not F)
    if sin_leer:                                                   # nadie leyó la situación: no hay puntuación que dar
        razones.insert(0, 'sin señales de situación en la ficha (todo por defecto): hay que leer tabla, motivación, rotación y previa')
        return None, razones, True
    return round(max(0, min(100, pts))), razones, False


def estado_de(d, s, sin_leer):
    if d is None: return 'no ofrece'
    if d >= UMBRAL_DATOS and s is not None and s >= UMBRAL_SITUACION: return 'apto'
    if d >= UMBRAL_DATOS and sin_leer: return 'reserva'          # datos suficientes, falta leer la situación
    return 'no apto'


def evaluar(e):
    F = FI.construir(e)
    d, ddet, fam = puntuar_datos(e, F)
    s, sdet, sin_leer = puntuar_situacion(e)
    filas = FI.resumen(F)
    por_mercado = {}
    for t, amb, lado, h, q, col, rl, rv in filas:
        por_mercado[t] = por_mercado.get(t, 0) + 1
    jug_ok = [j for j in F['jugadores'] if j['stat'] in ('remates', 'al_arco') and any(x['reg']['cumple'] for x in j.get('escalones', []))]
    cumplen = {'córners': por_mercado.get('Córners', 0), 'partido': sum(v for k, v in por_mercado.items() if k != 'Córners'), 'jugadores': len(jug_ok)}
    mercados = {f: {'datos': fam.get(f), 'estado': estado_de(fam.get(f), s, sin_leer), 'cumplen': cumplen[f]} for f in ('córners', 'partido', 'jugadores')}
    orden = {'apto': 3, 'reserva': 2, 'no apto': 1, 'no ofrece': 0}
    estado = max((m['estado'] for m in mercados.values()), key=lambda x: orden[x])
    motivos = []
    if s is not None and s < UMBRAL_SITUACION: motivos.append(f'situación {s} < {UMBRAL_SITUACION}')
    if sin_leer: motivos.append('situación sin leer')
    for f, m in mercados.items():
        if m['estado'] == 'no apto' and m['datos'] is not None and m['datos'] < UMBRAL_DATOS: motivos.append(f"{f}: datos {m['datos']} < {UMBRAL_DATOS}")
        if m['estado'] == 'no ofrece': motivos.append(f'{f}: Betano no lo ofrece')
    return {'partido': F['encuentro'], 'liga': e.get('liga'), 'fecha': e.get('fecha'), 'datos': d, 'situacion': s, 'estado': estado,
            'apto': estado == 'apto', 'mercados': mercados, 'familias_datos': fam, 'motivos': motivos, 'detalle_datos': ddet,
            'detalle_situacion': sdet, 'lineas_que_cumplen': len(filas), 'por_mercado': por_mercado, 'jugadores_que_cumplen': len(jug_ok),
            'probabilidades_1x2': probs_1x2(e)}


def _m(m):
    return 'no lo ofrece' if m['datos'] is None else f"{m['estado']} ({m['datos']} · {m['cumplen']})"


def markdown(R):
    L = ['# Ranking de partidos por contexto', '',
         f'Apto = datos ≥ {UMBRAL_DATOS} **y** situación ≥ {UMBRAL_SITUACION}; reserva = datos suficientes y situación sin leer. «Cumplen» = líneas de equipo con 5 de 7 en ambos equipos y cuota ≥ 1.20, '
         'más jugadores con algún escalón que cumple. Los no aptos se muestran con su motivo; nada se descarta en silencio.', '',
         '| # | Partido | Situación | Estado | Córners (datos · cumplen) | Partido (datos · cumplen) | Jugadores (datos · cumplen) | Motivo |', '|---|---|---|---|---|---|---|---|']
    for i, r in enumerate(R, 1):
        L.append(f"| {i} | {r['partido']} | {'sin leer' if r['situacion'] is None else r['situacion']} | {r['estado']} | {_m(r['mercados']['córners'])} | {_m(r['mercados']['partido'])} | {_m(r['mercados']['jugadores'])} | {'; '.join(r['motivos'])} |")
    L.append('')
    for r in R:
        L += [f"## {r['partido']} ({r['liga']})", f"Datos {r['datos']} · Situación {'sin leer' if r['situacion'] is None else r['situacion']} · por mercado: {r['por_mercado'] or 'ninguna línea cumple'}", '',
              '**Datos:** ' + ' | '.join(r['detalle_datos']), '', '**Situación:** ' + '; '.join(r['detalle_situacion']), '']
    return '\n'.join(L)


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    carpeta = argv[0]
    salida = argv[1] if len(argv) > 1 else os.path.join(carpeta, '..')
    R = []
    for p in sorted(glob.glob(os.path.join(carpeta, '*.json'))):
        R.append(evaluar(json.load(open(p, encoding='utf8'))))
    orden = {'apto': 3, 'reserva': 2, 'no apto': 1, 'no ofrece': 0}
    R.sort(key=lambda r: (orden[r['estado']], sum(m['cumplen'] for m in r['mercados'].values()), r['datos']), reverse=True)
    os.makedirs(salida, exist_ok=True)
    json.dump(R, open(os.path.join(salida, 'ranking.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    open(os.path.join(salida, 'ranking.md'), 'w', encoding='utf8').write(markdown(R))
    for r in R:
        print(f"{r['partido'][:36]:36s} situación={'  -' if r['situacion'] is None else format(r['situacion'], '3d')} {r['estado']:8s} córners={_m(r['mercados']['córners'])} | partido={_m(r['mercados']['partido'])} | jug={_m(r['mercados']['jugadores'])}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
