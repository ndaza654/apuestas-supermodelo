"""Regularidad ajustada por rival (propuesta aprobada el 23-nov-2026). SIN VALIDAR todavía: informativa, no cambia ninguna p.

Idea: cada partido pasado de un equipo se reescala a «cómo habría salido contra el rival de hoy» con los ratings de rival que
salen de los últimos 10 partidos de cada rival (datos_ligas/<liga>_<fecha>.json, hecho con recoleccion/ratings_rivales.js):
  prod_hoy_i = prod_i × concede(rival de hoy) / concede(rival de aquel partido)            (producción propia)
  total_hoy_i = prod_i × concede(rival hoy)/concede(R_i) + cont_i × produce(rival hoy)/produce(R_i)   (total del partido)
Los rivales sin rating comparable (otra división o sin datos) se excluyen del ajustado y se declara el n.
Uso:  python3 recoleccion/ajuste_rival.py <datos_ligas/..json> <flashscore/<clave>.json>
"""
import json, sys, statistics as st

MERCADOS = {'sot': 'Tiros al arco', 'sh': 'Remates', 'c': 'Córners', 'f': 'Faltas', 'off': 'Fueras de juego', 'y': 'Tarjetas (puntos)', 'ti': 'Saques de banda', 'gk': 'Saques de meta', 'g': 'Goles'}
TOPE = (0.5, 2.0)


def cargar(path):
    d = json.load(open(path, encoding='utf8'))
    return d['equipos']


def _serie(filas, m):
    """[(fav, cont)] de los partidos con dato del mercado m."""
    out = []
    for f in filas:
        if m == 'g':
            out.append((f[3], f[4]))
        elif f[6] and m in f[6]:
            out.append((f[6][m][0], f[6][m][1]))
    return out


def primera_division(filas):
    comps = [f[2] for f in filas]
    return sum(1 for c in comps if c in ('Premier League', 'EFL Cup', 'FA Cup', 'Champions League', 'Europa League', 'Conference League')) >= 6 and not any(c in ('League One', 'Championship') for c in comps[:5])


def rating(equipos, nombre, m, excluir_mid=None):
    """(produce, concede, n) del equipo en el mercado m (media de sus últimos 10). excluir_mid: se quita ese partido (el del equipo que se está ajustando: evita circularidad)."""
    f = equipos.get(nombre)
    if not f:
        return None
    if excluir_mid:
        f = [x for x in f if x[5] != excluir_mid]
    s = _serie(f, m)
    if len(s) < 5:
        return None
    return (sum(a for a, _ in s) / len(s), sum(b for _, b in s) / len(s), len(s))


def media_liga(equipos, m):
    pr = [rating(equipos, t, m) for t, f in equipos.items() if primera_division(f)]
    pr = [x for x in pr if x]
    return (sum(x[0] for x in pr) / len(pr), len(pr)) if pr else (None, 0)


def _clip(x):
    return max(TOPE[0], min(TOPE[1], x))


def ajustar(equipos, partidos, hoy_rival, m, ambito):
    """partidos = lista de la ficha (forma de un equipo: dicts con rival, stats, g…). Devuelve lista de (valor_ajustado, valor_crudo, rival, usado)."""
    rh = rating(equipos, hoy_rival, m)
    out = []
    for p in partidos:
        if m == 'g':
            fav, cont = p['g'][0], p['g'][1]
        else:
            s = p.get('stats', {}).get(m)
            if not s:
                continue
            fav, cont = s[0], s[1]
        crudo = {'local': fav, 'visitante': fav, 'total': fav + cont}[ambito] if ambito != 'rival' else cont
        rr = rating(equipos, p['rival'], m, excluir_mid=p.get('mid'))
        ok = rh and rr and primera_division(equipos.get(p['rival'], [])) and rr[1] > 0 and rr[0] > 0
        if not ok:
            out.append((None, crudo, p['rival'], False)); continue
        f_def = _clip(rh[1] / rr[1])
        if ambito in ('local', 'visitante'):
            adj = fav * f_def
        else:
            adj = fav * f_def + cont * _clip(rh[0] / rr[0])
        out.append((adj, crudo, p['rival'], True))
    return out


def x_de(serie, linea, lado, ajustado=True):
    v = [a if ajustado else c for a, c, _, ok in serie if (ok or not ajustado)]
    if not v:
        return 0, 0
    if lado == 'Más':
        return sum(1 for x in v if x > linea), len(v)
    return sum(1 for x in v if x < linea), len(v)


if __name__ == '__main__':
    eq = cargar(sys.argv[1]); fs = json.load(open(sys.argv[2], encoding='utf8'))
    L, V = fs['local'], fs['visitante']
    print('Local', L, '| visitante', V)
    for m, nom in MERCADOS.items():
        ml, n = media_liga(eq, m); rl, rv = rating(eq, L, m), rating(eq, V, m)
        if not rl or not rv: continue
        al = ajustar(eq, fs['forma']['local'], V, m, 'local'); av = ajustar(eq, fs['forma']['visitante'], L, m, 'visitante')
        f = lambda s: (sum(a for a, _, _, ok in s if ok) / max(1, sum(1 for x in s if x[3])), sum(c for _, c, _, _ in s) / len(s), sum(1 for x in s if x[3]))
        fl, fv = f(al), f(av)
        print(f'{nom:18s} liga {ml:5.2f} | {L}: hace {rl[0]:.2f} concede {rl[1]:.2f} · ajustado hoy {fl[0]:.2f} (crudo {fl[1]:.2f}, n {fl[2]}) | {V}: hace {rv[0]:.2f} concede {rv[1]:.2f} · ajustado hoy {fv[0]:.2f} (crudo {fv[1]:.2f}, n {fv[2]})')


def serie(equipos, partidos, opp_hoy, m, tipo):
    """Serie ajustada «a cómo habría salido contra opp_hoy». tipo: 'prop' (lo que produce el equipo), 'conc' (lo que concede el equipo), 'total' (total del partido).
    Devuelve [(valor_ajustado|None, valor_crudo, rival, usado)]."""
    rh = rating(equipos, opp_hoy, m)
    out = []
    for p in partidos:
        if m == 'g':
            fav, cont = p['g'][0], p['g'][1]
        else:
            s_ = p.get('stats', {}).get(m)
            if not s_:
                continue
            fav, cont = s_[0], s_[1]
        crudo = {'prop': fav, 'conc': cont, 'total': fav + cont}[tipo]
        rr = rating(equipos, p['rival'], m, excluir_mid=p.get('mid'))
        if not (rh and rr and primera_division(equipos.get(p['rival'], [])) and rr[0] > 0 and rr[1] > 0):
            out.append((None, crudo, p['rival'], False)); continue
        if tipo == 'prop':
            adj = fav * _clip(rh[1] / rr[1])
        elif tipo == 'conc':
            adj = cont * _clip(rh[0] / rr[0])
        else:
            adj = fav * _clip(rh[1] / rr[1]) + cont * _clip(rh[0] / rr[0])
        out.append((adj, crudo, p['rival'], True))
    return out


def conteo(sr, linea, lado):
    """(cumple, n) sobre los partidos con ajuste; y (cumple, n) crudo."""
    aj = [a for a, c, r, ok in sr if ok]
    cr = [c for a, c, r, ok in sr]
    f = (lambda v: v > linea) if lado == 'Más' else (lambda v: v < linea)
    return (sum(1 for v in aj if f(v)), len(aj)), (sum(1 for v in cr if f(v)), len(cr))
