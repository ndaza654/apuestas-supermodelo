# -*- coding: utf-8 -*-
"""Traduce cualquier selección de Betano a un evento sobre los partidos simulados.

Una selección es un dict:
  {'mercado': 'corners', 'ambito': 'total'|'local'|'visitante'|'1T'|'2T', 'lado': 'mas'|'menos', 'linea': 9.5}
  {'mercado': 'ambos', 'lado': 'si'|'no'}
  {'mercado': 'resultado', 'lado': '1'|'X'|'2'|'1X'|'X2'|'12'}
  {'mercado': 'mas_que', 'stat': 'corners'|'tarjetas', 'lado': 'local'|'visitante'|'empate'}
  {'mercado': 'ambos_n_tarjetas', 'n': 2, 'lado': 'si'|'no'}
  {'mercado': 'jugador', 'jugador': 'Nombre', 'stat': 'remates'|'al_arco'|'anota'|'anota_o_asiste'|'asiste'|'faltas'|'entradas'|'atajadas', 'k': 2}
  {'mercado': 'htft', 'lado': '1/1'|'1/X'|…|'2/2'}      (resultado al descanso / resultado final; 1 = local, X = empate, 2 = visitante)
  {'mercado': 'htft_o', 'lado': '1'|'X'|'2'}              («Resultado medio tiempo o tiempo completo»: ese resultado en el descanso O al final)
  {'mercado': 'resultado_1t'|'resultado_2t', 'lado': '1'|'X'|'2'}   (resultado de cada tiempo por separado)
  {'mercado': 'pareja', 'jugadores': ['A', 'B'], 'stat': 'asiste'|'anota'|'anota_o_asiste'|'tarjeta'}   («cualquiera de los jugadores…»)
Mercados de estadística: goles, corners, tarjetas, faltas, remates, al_arco, fueras, saques_meta, saques_banda, atajadas.
"""
import numpy as np

STAT = {'goles': 'g', 'corners': 'c', 'tarjetas': 'tarjetas', 'faltas': 'f', 'remates': 'sh', 'al_arco': 'sot',
        'fueras': 'off', 'saques_meta': 'gk', 'saques_banda': 'ti', 'atajadas': 'sv', 'entradas': 'tk'}
PRIMER_T = {'g': 'g1', 'c': 'c1', 'tarjetas': 'tarj1', 'sh': 'sh1', 'sot': 'sot1', 'f': 'f1', 'off': 'off1', 'gk': 'gk1', 'ti': 'ti1'}
FAMILIA = {'goles': 'goles', 'ambos': 'ambos', 'resultado': 'resultado', 'corners': 'corners', 'tarjetas': 'tarjetas',
           'faltas': 'faltas', 'remates': 'remates', 'al_arco': 'al_arco', 'fueras': 'fueras', 'saques_meta': 'saques_meta',
           'saques_banda': 'saques_banda', 'atajadas': 'jugador', 'mas_que': 'especial', 'ambos_n_tarjetas': 'tarjetas',
           'jugador': 'jugador', 'handicap': 'resultado', 'htft': 'resultado', 'htft_o': 'resultado',
           'resultado_1t': 'resultado', 'resultado_2t': 'resultado', 'pareja': 'pareja'}


def valor(sim, mercado, ambito):
    """Valor simulado de la estadística para el ámbito pedido (array)."""
    s = STAT[mercado]
    R = sim
    if ambito == 'local':
        return R[0][s]
    if ambito == 'visitante':
        return R[1][s]
    if ambito in ('1T', '2T'):
        k = PRIMER_T[s]
        primero = R[0][k] + R[1][k]
        return primero if ambito == '1T' else (R[0][s] + R[1][s] - primero)
    return R[0][s] + R[1][s]


def evento(sim, sel, jugadores=None):
    m = sel['mercado']
    R = sim
    if m in STAT and m != 'atajadas':
        x = valor(R, m, sel.get('ambito', 'total'))
        return x > sel['linea'] if sel['lado'] == 'mas' else x < sel['linea']
    if m == 'atajadas':     # atajadas del portero de un equipo
        x = R[0 if sel['ambito'] == 'local' else 1]['sv']
        return x > sel['linea'] if sel['lado'] == 'mas' else x < sel['linea']
    if m == 'ambos':
        e = (R[0]['g'] > 0) & (R[1]['g'] > 0)
        return e if sel['lado'] == 'si' else ~e
    if m == 'resultado':
        d = R[0]['g'] - R[1]['g']
        return {'1': d > 0, 'X': d == 0, '2': d < 0, '1X': d >= 0, 'X2': d <= 0, '12': d != 0}[sel['lado']]
    if m == 'handicap':     # h es el hándicap del LOCAL (p. ej. -1): local gana si d + h > 0, empate si d + h == 0
        d = R[0]['g'] - R[1]['g']
        v = d + sel['h']
        return {'local': v > 0, 'empate': v == 0, 'visitante': v < 0}[sel['lado']]
    if m == 'mas_que':
        s = STAT[sel['stat']]
        a, b = R[0][s], R[1][s]
        return {'local': a > b, 'visitante': b > a, 'empate': a == b}[sel['lado']]
    if m == 'ambos_n_tarjetas':
        n = sel.get('n', 2)
        e = (R[0]['tarjetas'] >= n) & (R[1]['tarjetas'] >= n)
        return e if sel['lado'] == 'si' else ~e
    if m == 'jugador':
        x = jugadores[sel['jugador']][sel['stat']]
        return x >= sel.get('k', 1)
    if m in ('htft', 'htft_o', 'resultado_1t', 'resultado_2t'):
        d1 = R[0]['g1'] - R[1]['g1']
        d = R[0]['g'] - R[1]['g']
        d2 = d - d1
        r3 = lambda x: {'1': x > 0, 'X': x == 0, '2': x < 0}
        if m == 'resultado_1t':
            return r3(d1)[sel['lado']]
        if m == 'resultado_2t':
            return r3(d2)[sel['lado']]
        if m == 'htft_o':
            return r3(d1)[sel['lado']] | r3(d)[sel['lado']]
        a, b = sel['lado'].split('/')
        return r3(d1)[a] & r3(d)[b]
    if m == 'pareja':
        e = None
        for nm in sel['jugadores']:
            x = jugadores[nm][sel['stat']] >= 1
            e = x if e is None else (e | x)
        return e
    raise ValueError(f'mercado desconocido: {m}')


def nombre(sel, local='Local', visit='Visitante'):
    m = sel['mercado']
    amb = {'total': '', 'local': ' ' + local, 'visitante': ' ' + visit, '1T': ' 1.er tiempo', '2T': ' 2.º tiempo'}
    nm = {'goles': 'Goles', 'corners': 'Córners', 'tarjetas': 'Tarjetas', 'faltas': 'Faltas', 'remates': 'Remates',
          'al_arco': 'Tiros al arco', 'fueras': 'Fueras de lugar', 'saques_meta': 'Saques de meta',
          'saques_banda': 'Saques de banda', 'atajadas': 'Atajadas'}
    if m in nm:
        lado = 'Más' if sel['lado'] == 'mas' else 'Menos'
        return f"{nm[m]}{amb.get(sel.get('ambito', 'total'), '')} {lado} {sel['linea']}"
    if m == 'ambos':
        return f"Ambos marcan: {'Sí' if sel['lado'] == 'si' else 'No'}"
    if m == 'resultado':
        return {'1': f'Gana {local}', 'X': 'Empate', '2': f'Gana {visit}', '1X': f'{local} o empate',
                'X2': f'{visit} o empate', '12': 'No hay empate'}[sel['lado']]
    if m == 'handicap':
        if sel['lado'] == 'empate':
            return f"Hándicap empate ({local} {sel['h']:+g})"
        return f"Hándicap {local} {sel['h']:+g}" if sel['lado'] == 'local' else f"Hándicap {visit} {-sel['h']:+g}"
    if m == 'mas_que':
        quien = {'local': local, 'visitante': visit, 'empate': 'empate'}[sel['lado']]
        return f"Más {sel['stat']}: {quien}"
    if m == 'ambos_n_tarjetas':
        return f"Ambos {sel.get('n', 2)}+ tarjetas: {'Sí' if sel['lado'] == 'si' else 'No'}"
    if m in ('htft', 'htft_o', 'resultado_1t', 'resultado_2t'):
        q = {'1': local, 'X': 'Empate', '2': visit}
        if m == 'htft':
            a, b = sel['lado'].split('/')
            return f"Descanso/final: {q[a]} / {q[b]}"
        if m == 'htft_o':
            return f"Descanso o final: {q[sel['lado']]}"
        return f"{'1.er' if m == 'resultado_1t' else '2.º'} tiempo: {q[sel['lado']]}"
    if m == 'pareja':
        t = {'asiste': 'da una asistencia', 'anota': 'anota', 'anota_o_asiste': 'anota o asiste', 'tarjeta': 'recibe tarjeta'}[sel['stat']]
        return f"{' o '.join(sel['jugadores'])} ({t})"
    if m == 'jugador':
        txt = {'remates': 'remates', 'al_arco': 'tiros al arco', 'anota': 'anota', 'anota_o_asiste': 'anota o asiste', 'asiste': 'asiste',
               'faltas': 'faltas cometidas', 'entradas': 'entradas', 'atajadas': 'atajadas', 'tarjeta': 'recibe tarjeta'}[sel['stat']]
        k = '' if sel['stat'] in ('anota', 'anota_o_asiste', 'tarjeta') else f" {sel.get('k', 1)}+"
        return f"{sel['jugador']} {txt}{k}"
    return str(sel)


def submercado(sel, fav=None):
    """Clave fina del mercado para aprender: mercado + ámbito + dirección, y del lado del favorito o del no favorito.
    Ejemplos: 'corners total Más', 'corners favorito Más', 'goles 1T Menos', 'jugador remates', 'resultado favorito'.
    fav: 0 (local) o 1 (visitante)."""
    m = sel['mercado']
    def quien(lado):
        if lado not in ('local', 'visitante') or fav is None:
            return {'local': 'local', 'visitante': 'visitante'}.get(lado, lado)
        return 'favorito' if (lado == 'local') == (fav == 0) else 'no favorito'
    if m == 'pareja':
        return f"pareja {sel['stat']}"
    if m in ('htft', 'htft_o', 'resultado_1t', 'resultado_2t'):
        return m
    if m == 'jugador':
        return f"jugador {sel['stat']}"
    if m == 'atajadas':
        return 'jugador atajadas'
    if 'linea' in sel:
        amb = sel.get('ambito', 'total')
        amb = quien(amb) if amb in ('local', 'visitante') else amb
        return f"{m} {amb} {'Más' if sel['lado'] == 'mas' else 'Menos'}"
    if m in ('ambos', 'ambos_n_tarjetas'):
        return f"{m} {'Sí' if sel['lado'] == 'si' else 'No'}"
    if m == 'resultado':
        lad = sel['lado']
        if fav is None:
            return f'resultado {lad}'
        f1, f2 = ('1', '2') if fav == 0 else ('2', '1')
        return {f1: 'resultado favorito', f2: 'resultado no favorito', 'X': 'resultado empate',
                '12': 'resultado sin empate'}.get(lad, 'resultado doble oportunidad ' +
                                                    ('favorito' if f1 in lad else 'no favorito'))
    if m == 'handicap':
        return 'handicap empate' if sel['lado'] == 'empate' else f"handicap {quien(sel['lado'])}"
    if m == 'mas_que':
        return f"más {sel['stat']} {quien(sel['lado'])}"
    return m


def familia(sel):
    return FAMILIA.get(sel['mercado'], 'especial')


# ------------------------------------------------------------------ líneas asiáticas (enteras y de cuarto)
def _frac(v):
    return round(abs(float(v)) % 1, 2)


def es_asiatica(sel):
    """Línea con devolución posible: entera (2.0) o de cuarto (2.25, 2.75); también el hándicap de 2 opciones con h entero
    o de cuarto. Con .5 no hay devolución."""
    if sel.get('mercado') in STAT and 'linea' in sel and sel['mercado'] != 'atajadas':
        return _frac(sel['linea']) in (0.0, 0.25, 0.75)
    if sel.get('mercado') == 'handicap' and sel.get('asiatico') and sel.get('lado') in ('local', 'visitante'):
        return _frac(sel['h']) in (0.0, 0.25, 0.75)
    return False


def _partes(v):
    return [(v - 0.25, 0.5), (v + 0.25, 0.5)] if _frac(v) in (0.25, 0.75) else [(v, 1.0)]


def partes_asiaticas(sim, sel):
    """[(peso, gana, devuelve)] con arrays booleanos. Una línea de cuarto es media apuesta en cada línea vecina."""
    out = []
    if sel['mercado'] == 'handicap':
        d = sim[0]['g'] - sim[1]['g']
        h = sel['h'] if sel['lado'] == 'local' else -sel['h']
        dd = d if sel['lado'] == 'local' else -d
        for hp, w in _partes(h):
            v = dd + hp
            out.append((w, v > 0, (v == 0) if float(hp).is_integer() else np.zeros(len(d), bool)))
        return out
    x = valor(sim, sel['mercado'], sel.get('ambito', 'total'))
    for Lp, w in _partes(sel['linea']):
        gana = x > Lp if sel['lado'] == 'mas' else x < Lp
        out.append((w, gana, (x == Lp) if float(Lp).is_integer() else np.zeros(len(x), bool)))
    return out


def p_efectiva(partes, cuota):
    """Probabilidad «efectiva» p tal que EV = p·cuota − 1, contando devoluciones y medias. Y la prob. de devolución."""
    ret = sum(w * (g.mean() * (cuota - 1) - (1 - g.mean() - dv.mean())) for w, g, dv in partes)
    dev = sum(w * dv.mean() for w, g, dv in partes)
    return (ret + 1) / cuota, dev


def p_efectiva_mercado(q, partes, cuota):
    """Lo mismo para el mercado: q = prob. sin margen de ganar SIN contar devoluciones (lo que implica la cuota)."""
    ret = sum(w * ((1 - dv.mean()) * (q * (cuota - 1) - (1 - q))) for w, g, dv in partes)
    return (ret + 1) / cuota
