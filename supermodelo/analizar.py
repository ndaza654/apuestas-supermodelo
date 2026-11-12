# -*- coding: utf-8 -*-
"""Análisis completo de un partido: objetivos → contexto → simulación → todas las líneas de Betano → builders.

Entrada (dict o JSON):
{
  "local": "Atlético de Madrid", "visitante": "Barcelona", "liga": "LaLiga", "fecha": "2026-11-08 15:00",
  "objetivos": {"local": {"c": 5.1, "sh": 12.4, "sot": 4.3, "f": 13.5, "y": 2.4, "g": 1.3},
                "visitante": {...}},          # medias del modelo (perfiles.media_partido) sin contexto
  "sesgo": {"corners|total": 1.04, ...},      # opcional: sesgo modelo/mercado medido en la jornada
  "ficha": {...},                              # contexto.py
  "betano": {"lineas": [...], "unicos": [...], "jugadores": [...]},
  "jugadores": [{"nombre": "Lamine Yamal", "lado": "visitante", "titular": 0.95, "minutos": 85}]
}
"""
import math, itertools, json
import numpy as np
from scipy.stats import poisson
from scipy.optimize import minimize
from . import config as C, mercado as MK, mercados as MS, escenarios as ES, jugadores as JG, memoria as MEM, dependencia as DEP, proyeccion as PR
from .contexto import traducir
from .simulador import Partido

# Dispersión r de la binomial negativa con la que se lee la media de una escalera de Betano (r grande = Poisson).
# Medida con 62 164 partidos (2016–2026, 22 ligas) condicionando a los equipos y al precio (lo que sabe la casa):
#   córners equipo var/media 1,34 (r≈15), total 1,11 (r≈90); remates equipo 1,41 (r≈32), total 1,18 (r≈135);
#   al arco equipo 1,06 (r≈80), total 1,05 (r≈165); faltas ≈ Poisson; tarjetas (amarilla 1, roja 2) total 1,23 (r≈20).
# Antes (v2) se suponía más dispersión (córners total r=25 → var/media 1,4): las colas salían anchas.
R_EQUIPO = {'c': 15, 'sh': 32, 'sot': 80, 'f': 500, 'y': 40, 'off': 8, 'gk': 20, 'ti': 40, 'g': None}
R_TOTAL = {'c': 90, 'sh': 135, 'sot': 165, 'f': 400, 'y': 20, 'off': 10, 'gk': 30, 'ti': 60, 'g': None}
DEF_LIGA = {'c': 5.0, 'sh': 12.5, 'sot': 4.3, 'f': 11.8, 'y': 2.1, 'off': 1.8, 'gk': 8.0, 'ti': 20.0, 'g': 1.35}
PRIOR2STAT = {'c': ('corners_local', 'corners_visitante'), 'sh': ('remates_local', 'remates_visitante'),
              'sot': ('al_arco_local', 'al_arco_visitante'), 'f': ('faltas_local', 'faltas_visitante'),
              'y': ('tarjetas_local', 'tarjetas_visitante'), 'g': ('goles_local', 'goles_visitante')}


def defaults_liga(liga):
    """Medias por lado de la liga (prior verificado) para lo que Betano no cotiza; si no hay, el promedio genérico."""
    from . import ligas
    p = ligas.prior(liga) or {}
    out = [dict(DEF_LIGA), dict(DEF_LIGA)]
    for s, (kl, kv) in PRIOR2STAT.items():
        if p.get(kl) not in (None, '') and p.get(kv) not in (None, ''):
            out[0][s], out[1][s] = float(p[kl]), float(p[kv])
    return out, bool(p)
MKT2STAT = {'goles': 'g', 'corners': 'c', 'tarjetas': 'y', 'faltas': 'f', 'remates': 'sh', 'al_arco': 'sot',
            'fueras': 'off', 'saques_meta': 'gk', 'saques_banda': 'ti'}


# ------------------------------------------------------------------ goles desde el mercado
def lambdas_mercado(bet, prior_g=None):
    """λ local y visitante que reproducen el 1X2 y las líneas de goles totales de Betano (Poisson independiente).
    Si falta uno de los dos, ajusta con lo que hay y completa con un previo suave (goles por equipo de la liga, o 1,45/1,15):
    solo 1X2 → el total sale del previo; solo goles → el reparto local/visitante sale del previo."""
    x12 = next((u for u in bet.get('unicos', []) if u.get('mercado') == 'resultado'
                and all((u.get('opciones') or {}).get(k) for k in ('1', 'X', '2'))), None)
    tot = [l for l in bet.get('lineas', []) if l.get('mercado') == 'goles' and l.get('ambito', 'total') == 'total'
           and l.get('mas') and l.get('menos') and _frac_media(l['linea'])]
    if not x12 and not tot:
        return None
    pg = prior_g or (1.45, 1.15)
    p3 = MK.devig_n([x12['opciones']['1'], x12['opciones']['X'], x12['opciones']['2']]) if x12 else None
    obj = [(l['linea'], MK.devig(l['mas'], l['menos'])) for l in tot]

    def err(v):
        a, b = np.exp(v)
        ks = np.arange(0, 12)
        ph, pa = poisson.pmf(ks, a), poisson.pmf(ks, b)
        M = np.outer(ph, pa)
        e = 0.0
        if p3:
            e += (np.tril(M, -1).sum() - p3[0]) ** 2 + (np.trace(M) - p3[1]) ** 2 + (np.triu(M, 1).sum() - p3[2]) ** 2
        else:   # sin 1X2: el reparto entre equipos lo pone el previo (débil)
            e += 0.02 * (math.log(a / b) - math.log(pg[0] / pg[1])) ** 2
        for L, p in obj:
            e += (1 - poisson.cdf(math.floor(L), a + b) - p) ** 2
        if not obj:   # sin línea de goles: el total lo pone el previo (débil)
            e += 0.002 * (a + b - sum(pg)) ** 2
        return e
    r = minimize(err, x0=np.log(pg), method='Nelder-Mead')
    return [float(x) for x in np.exp(r.x)]


def _frac_media(L):
    """Solo líneas .5 para ajustar λ (las enteras y de cuarto tienen devolución)."""
    return round(float(L) % 1, 2) == 0.5


def media_mercado(bet, mercado, ambito):
    lad = [(l['linea'], l['mas'], l['menos']) for l in bet.get('lineas', [])
           if l['mercado'] == mercado and l.get('ambito', 'total') == ambito and l.get('mas') and l.get('menos')
           and _frac_media(l['linea'])]
    if not lad:
        return None
    s = MKT2STAT[mercado]
    r = R_TOTAL[s] if ambito == 'total' else R_EQUIPO[s]
    return MK.media_implicita(lad, r if r else 1e6)


def construir_objetivos(e, aj):
    """Medias por equipo: ancladas al mercado, con una dosis del modelo de perfiles y luego el contexto."""
    bet = e.get('betano', {})
    mod = e.get('objetivos') or {}
    w = e.get('peso_modelo', C.W_MODELO_MEDIA)
    obj = [{}, {}]
    fuente = [{}, {}]
    m_mod = [{}, {}]
    for l, nom in ((0, 'local'), (1, 'visitante')):
        for s in ['c', 'sh', 'sot', 'f', 'y', 'off', 'gk', 'ti', 'g']:
            v = (mod.get(nom) or {}).get(s)
            if v is not None:
                sg = (e.get('sesgo') or {}).get(f'{s}|{nom}')
                m_mod[l][s] = v / sg if sg else v
    for mercado, s in MKT2STAT.items():
        if s == 'g':
            continue
        mt = media_mercado(bet, mercado, 'total')
        mk = [media_mercado(bet, mercado, 'local'), media_mercado(bet, mercado, 'visitante')]
        for l in (0, 1):
            mm = m_mod[l].get(s)
            if mk[l] is not None:
                obj[l][s] = mk[l] ** (1 - w) * mm ** w if mm else mk[l]
                fuente[l][s] = 'mercado + modelo' if mm else 'mercado'
        faltan = [l for l in (0, 1) if s not in obj[l]]
        if faltan and mt is not None:
            tot_mod = sum(m_mod[l].get(s, 0) for l in (0, 1))
            for l in faltan:
                otro = obj[1 - l].get(s)
                if otro is not None:
                    obj[l][s] = max(0.2, mt - otro); fuente[l][s] = 'mercado (total − rival)'
                elif m_mod[0].get(s) and m_mod[1].get(s):
                    t = mt ** (1 - w) * tot_mod ** w
                    obj[l][s] = t * m_mod[l][s] / tot_mod; fuente[l][s] = 'mercado (total) repartido por el modelo'
                else:
                    obj[l][s] = mt / 2; fuente[l][s] = 'mercado (total) a medias'
        for l in (0, 1):
            if s not in obj[l] and s in m_mod[l]:
                obj[l][s] = m_mod[l][s]; fuente[l][s] = 'modelo'
    for l in (0, 1):
        if 'g' in m_mod[l]:
            obj[l]['g'] = m_mod[l]['g']; fuente[l]['g'] = 'modelo'
    # goles: mezcla con el mercado (el más eficiente)
    dl, hay_prior = defaults_liga(e.get('liga'))
    lm = lambdas_mercado(bet, (dl[0]['g'], dl[1]['g']) if hay_prior else None)
    for l in (0, 1):
        if lm:
            if 'g' in obj[l]:
                obj[l]['g'] = C.W_MERCADO_GOLES * lm[l] + (1 - C.W_MERCADO_GOLES) * obj[l]['g']
                fuente[l]['g'] = 'mezcla mercado/modelo'
            else:
                obj[l]['g'] = lm[l]; fuente[l]['g'] = 'mercado'
        elif 'g' not in obj[l]:
            if hay_prior and 'sot' not in obj[l]:
                obj[l]['g'] = dl[l]['g']; fuente[l]['g'] = 'promedio de la liga (prior verificado)'
            else:
                obj[l]['g'] = 0.30 * obj[l].get('sot', dl[l]['sot'])   # conversión media al arco → gol
                fuente[l]['g'] = 'estimado desde tiros al arco'
        for s, v in dl[l].items():
            if s not in obj[l]:
                obj[l][s] = v; fuente[l][s] = 'promedio de la liga (prior verificado)' if hay_prior else 'promedio genérico'
    # contexto
    for l in (0, 1):
        for s in obj[l]:
            m = aj.mult[l].get(s, 1.0)
            # Varios hechos juntos no se suman sin límite: el efecto total por estadística queda en ±TOPE_CONTEXTO
            # (salvo que la ficha traiga hechos frescos, que pueden pasar el tope).
            t = C.TOPE_CONTEXTO_FRESCO if aj.frescos else C.TOPE_CONTEXTO
            obj[l][s] *= max(1 / t, min(t, m))
        obj[l]['sot'] = min(obj[l]['sot'], 0.8 * obj[l]['sh'])
        obj[l]['g'] = min(obj[l]['g'], 0.85 * obj[l]['sot'])
    return obj, fuente, lm


# ------------------------------------------------------------------ evaluación de líneas
# Qué familias toca cada tipo de hecho fresco (para la alerta de contexto).
_TODAS = {'goles', 'ambos', 'resultado', 'corners', 'tarjetas', 'faltas', 'remates', 'al_arco', 'fueras', 'saques_meta',
          'saques_banda', 'especial', 'jugador'}
FRESCO_FAMILIAS = {'bajas': {'goles', 'ambos', 'resultado', 'remates', 'al_arco', 'corners', 'jugador', 'especial'},
                   'rotacion': _TODAS, 'estilo': _TODAS, 'motivacion': _TODAS, 'clima': {'goles', 'ambos', 'resultado', 'corners', 'al_arco'},
                   'arbitro': {'tarjetas', 'faltas', 'especial'}}


def _etiqueta(p, p_base, cuota, rob):
    t = []
    mov = p - p_base
    if p >= C.P_ALTA and rob >= C.ROBUSTEZ_ALTA:
        t.append('Alta probabilidad')
    if mov >= C.MOV_CONTEXTO:
        t.append(f'Contexto a favor (+{mov * 100:.0f} pts)')
    elif mov <= -C.MOV_CONTEXTO:
        t.append(f'Contexto en contra ({mov * 100:.0f} pts)')
    ev = MK.ev(p, cuota)
    if ev >= 0.03 and p - 1 / cuota >= 0.02:
        t.append('Valor' if rob >= 0.30 else 'Valor frágil (depende de un guion)')
    if not t:
        t.append('Justa' if ev >= -0.05 else 'Cara')
    elif ev < -0.05 and not any(x.startswith('Valor') for x in t):
        t.append('cuota por debajo de la justa')
    return ' · '.join(t)


def evaluar(S, sel, cuota, p_mkt, nombre, fam):
    """S: dict con sim (con contexto), base (sin contexto), lab, pg, jug, jug_base."""
    asi = MS.es_asiatica(sel)
    dev = None
    if asi:
        # Línea con devolución (entera, de cuarto, hándicap asiático): se trabaja con la prob. «efectiva» (EV = p·cuota − 1).
        pa_c = MS.partes_asiaticas(S['sim'], sel)
        pa_b = pa_c if S['base'] is S['sim'] else MS.partes_asiaticas(S['base'], sel)
        pc, dev = MS.p_efectiva(pa_c, cuota)
        pb, _ = MS.p_efectiva(pa_b, cuota)
        if p_mkt is not None:
            p_mkt = MS.p_efectiva_mercado(p_mkt, pa_b, cuota)
        ev_c = np.logical_and.reduce([g for _, g, _ in pa_c])   # gana entera (para guiones)
        ev_b = ev_c
    else:
        ev_c = MS.evento(S['sim'], sel, S.get('jug'))
        ev_b = ev_c if S['base'] is S['sim'] else MS.evento(S['base'], sel, S.get('jug_base'))
        pc, pb = float(ev_c.mean()), float(ev_b.mean())
    w = C.W_MERCADO.get(fam, 0.3)
    p_base = (1 - w) * pb + w * p_mkt if p_mkt is not None else pb
    p = float(np.clip(p_base + (pc - pb), 0.005, 0.995))
    pg_d, rob, mejor, peor = ES.por_guion(ev_c, S['lab'], S['pg'])
    rob = min(1.0, rob * (p / pc)) if pc > 0 else rob
    if fam in C.FAMILIAS_DEL_MARCADOR:
        # Los guiones se definen por el marcador: la "robustez" de goles, ambos marcan o resultado sería tautológica
        # (Gana el local muere en el guion "Sorpresa" por definición). Para estas familias manda la probabilidad.
        rob = p
    z = None
    if 'linea' in sel and sel['mercado'] in MS.STAT:
        x = MS.valor(S['sim'], sel['mercado'], sel.get('ambito', 'total')) if sel['mercado'] != 'atajadas' else \
            S['sim'][0 if sel['ambito'] == 'local' else 1]['sv']
        sd = float(x.std()) or 1.0
        z = ((x.mean() - sel['linea']) if sel['lado'] == 'mas' else (sel['linea'] - x.mean())) / sd
    alerta = None
    if p_mkt is not None and fam not in ('jugador', 'pareja'):
        # La simulación SIN contexto contra el mercado: ningún hecho fresco explica esa diferencia → nunca se apaga.
        if abs(pb - p_mkt) >= C.ALERTA_DISCREPANCIA:
            alerta = (f'Revisar: la simulación sin contexto se aleja {abs(pb - p_mkt) * 100:.0f} pts del mercado '
                      '(¿línea mal copiada, equipo cambiado o dato viejo?)')
        elif abs(p - p_base) >= C.ALERTA_CONTEXTO and not (set(S.get('frescos') or []) & FRESCO_FAMILIAS.get(fam, set())):
            alerta = f'Revisar: el contexto mueve {abs(p - p_base) * 100:.0f} pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?)'
    return dict(seleccion=nombre, sel=sel, familia=fam, cuota=cuota, alerta=alerta, p_simulacion=round(pc, 4),
                asiatica=asi, devolucion=None if dev is None else round(dev, 4),
                p_mercado=None if p_mkt is None else round(p_mkt, 4), p_sin_contexto=round(p_base, 4), p=round(p, 4),
                movimiento_contexto=round(p - p_base, 4), ev=round(MK.ev(p, cuota), 4),
                cuota_justa=round(MK.cuota_justa(p), 2), cuota_minima=round(MK.cuota_minima(p, 0.03, 0.02), 2),
                kelly_cuarto=round(MK.kelly(p, cuota, 0.25), 4),
                robustez=round(rob, 3), mejor_guion=mejor, peor_guion=peor,
                por_guion={k: round(v if fam in C.FAMILIAS_DEL_MARCADOR or pc <= 0 else min(1.0, v * p / pc), 3) for k, v in pg_d.items()},
                colchon_z=None if z is None else round(float(z), 2),
                etiqueta=_etiqueta(p, p_base, cuota, rob) + (f' · asiática: devuelve {dev * 100:.0f} %' if asi else '')
                + (' · ⚠ ' + alerta if alerta else ''), _ev=ev_c, _pc=pc)


MARGEN_UN_LADO = 1.07
PARTICION = {'resultado': {'1', 'X', '2'}, 'ambos': {'si', 'no'}, 'ambos_n_tarjetas': {'si', 'no'},
             'mas_que': {'local', 'visitante', 'empate'}, 'handicap': {'local', 'empate', 'visitante'},
             'resultado_1t': {'1', 'X', '2'}, 'resultado_2t': {'1', 'X', '2'},
             'htft': {f'{a}/{b}' for a in '1X2' for b in '1X2'}}


def _opciones_unico(u):
    """(selección, cuota, prob. de mercado) de cada opción de un mercado único, sin suponer que las opciones presentes
    forman una partición: 1X2 completo → sin margen entre los tres (y la doble oportunidad se deriva de ahí); opciones que
    sí forman una partición (ambos sí/no, hándicap de 3 opciones, más córners con empate) → sin margen entre ellas;
    hándicap de 2 opciones → sin margen entre las dos (asiático si h es entero o de cuarto); el resto (una opción sola,
    doble oportunidad sin el 1X2, «quién saca más» sin empate) → margen típico de un lado."""
    ops = {k: v for k, v in (u.get('opciones') or {}).items() if v}
    base = {kk: vv for kk, vv in u.items() if kk != 'opciones'}
    m = u.get('mercado')
    out, pm = [], {}
    if m == 'resultado':
        if all(k in ops for k in ('1', 'X', '2')):
            p1, px, p2 = MK.devig_n([ops['1'], ops['X'], ops['2']])
            pm = {'1': p1, 'X': px, '2': p2, '1X': p1 + px, 'X2': px + p2, '12': p1 + p2}
        elif all(k in ops for k in ('1X', 'X2', '12')):
            inv = {k: 1 / ops[k] for k in ('1X', 'X2', '12')}
            s = sum(inv.values()) / 2.0      # cada resultado aparece dos veces en las tres dobles oportunidades
            pm = {k: v / s for k, v in inv.items()}
    elif m == 'handicap' and set(ops) == {'local', 'visitante'}:
        p = MK.devig_n([ops['local'], ops['visitante']])
        pm = {'local': p[0], 'visitante': p[1]}
        base['asiatico'] = True
    elif m in PARTICION and set(ops) == PARTICION[m]:
        ks = sorted(ops)
        pm = dict(zip(ks, MK.devig_n([ops[k] for k in ks])))
    elif m in ('ambos', 'ambos_n_tarjetas') and set(ops) == {'si', 'no'}:
        pm = dict(zip(['si', 'no'], MK.devig_n([ops['si'], ops['no']])))
    for k, c in ops.items():
        p = pm.get(k)
        if p is None:
            p = min(0.97, (1 / c) / MARGEN_UN_LADO)
        out.append((dict(base, lado=k), c, p))
    return out


def _specs_jugadores(e, bet, obj):
    """Un spec por jugador: titularidad y minutos salen de la ficha (alineación confirmada o PROBABLE; sin dato → 0,85 y 82′).
    Los jugadores que solo aparecen en la ficha (p. ej. una pareja «cualquiera de…» con alguien sin líneas) entran con
    partes por defecto. Una baja confirmada ('fuera': true) no juega nada."""
    specs = {}
    info = {j.get('nombre'): j for j in (e.get('jugadores') or []) if j}

    def nuevo(nm, lado):
        i = info.get(nm) or {}
        sp = specs.setdefault(nm, dict(nombre=nm, lado=lado, titular=i.get('titular') if i.get('titular') is not None else 0.85,
                                       minutos=i.get('minutos') or 82, shares={}))
        if i.get('fuera'):
            sp['fuera'] = True
        return sp
    for jb in bet.get('jugadores', []):
        nm, lado = jb['jugador'], jb.get('lado', 'local')
        l = 0 if lado == 'local' else 1
        sp = nuevo(nm, lado)
        mins, st = sp['minutos'], jb['stat']
        if st in ('anota', 'anota_o_asiste', 'tarjeta', 'asiste') and 'escalera' in jb and not jb.get('cuota'):
            jb = dict(jb, cuota=jb['escalera'].get(1) or min(jb['escalera'].values()))   # «anota 1+» = anota
        if st == 'atajadas':
            sp['portero'] = True
        elif 'escalera' in jb and st in ('remates', 'al_arco', 'faltas', 'entradas'):
            clave = {'remates': 'sh', 'al_arco': 'sot', 'faltas': 'f', 'entradas': 'tk'}[st]
            sp['shares'][clave] = JG.share_desde_betano(jb['escalera'], obj[l].get(clave, 16.0), mins)
        elif st == 'anota':
            sp['shares']['g'] = JG.share_gol_desde_cuota(jb['cuota'], obj[l]['g'], mins)
        elif st == 'asiste':
            sp['shares']['a'] = JG.share_asist_desde_cuota(jb['cuota'], obj[l]['g'], mins)
        elif st == 'anota_o_asiste':
            sp['_ga'] = jb['cuota']
        elif st == 'tarjeta':
            p = min(0.9, (1 / jb['cuota']) / 1.15)
            sp['shares']['y'] = min(0.6, -math.log(1 - p) / max(obj[l]['y'] * mins / 95, 1e-6))
    for nm, i in info.items():     # jugadores de la ficha sin líneas propias (aparecen en parejas)
        if nm not in specs and i.get('lado') in ('local', 'visitante'):
            nuevo(nm, i['lado'])
    for sp in specs.values():
        if '_ga' in sp:
            l = 0 if sp['lado'] == 'local' else 1
            tot = JG.share_gol_desde_cuota(sp.pop('_ga'), obj[l]['g'], sp['minutos'])
            g = sp['shares'].get('g', 0.6 * tot)
            sp['shares']['g'] = g
            if 'a' not in sp['shares']:
                sp['shares']['a'] = max(0.02, tot - g)
    return list(specs.values())


def analizar(e, n=C.N_SIM, seed=C.SEED, builders=True, devolver_sim=False):
    """devolver_sim=True deja la simulación en res['_S'] (para combos.py y vivo.py; no se guarda en el JSON)."""
    from .contexto import Ajustes
    from . import ligas, sistemas
    loc, vis = e.get('local', 'Local'), e.get('visitante', 'Visitante')
    for jb in (e.get('betano') or {}).get('jugadores', []):   # JSON trae las claves como texto
        if 'escalera' in jb:
            jb['escalera'] = {int(k): float(v) for k, v in jb['escalera'].items()}
    if e.get('ficha') and e['ficha'].get('jugadores') and not e.get('jugadores'):
        e['jugadores'] = e['ficha']['jugadores']
    fuera = {j['nombre'] for j in (e.get('jugadores') or []) if j and j.get('fuera')}
    ficha = dict(e['ficha'], _liga=e.get('liga')) if e.get('ficha') else None
    aj = traducir(ficha)
    obj, fuente, lm = construir_objetivos(e, aj)
    obj0, _, _ = construir_objetivos(e, Ajustes())
    hay_contexto = bool(e.get('ficha'))
    P = Partido(obj, aj, n=n, seed=seed)
    P0 = Partido(obj0, Ajustes(), n=n, seed=seed) if hay_contexto else P
    sim, base = P.res, P0.res
    lab, fav, pg = ES.tabla(sim)
    bet = e.get('betano', {})
    S = dict(sim=sim, base=base, lab=lab, pg=pg, frescos=aj.frescos)
    bet = dict(bet, jugadores=[jb for jb in bet.get('jugadores', []) if jb['jugador'] not in fuera])   # baja: sin líneas propias
    specs = _specs_jugadores(e, bet, obj0)
    if specs:
        S['jug'] = JG.simular(sim, specs, np.random.default_rng(seed + 1))
        S['jug_base'] = S['jug'] if base is sim else JG.simular(base, specs, np.random.default_rng(seed + 1))
    out = []
    vistos = set()
    for l in bet.get('lineas', []):
        sel_base = dict(mercado=l['mercado'], ambito=l.get('ambito', 'total'), linea=l['linea'])
        dos = bool(l.get('mas') and l.get('menos'))
        for lado, cuota in (('mas', l.get('mas')), ('menos', l.get('menos'))):
            if not cuota:
                continue
            sel = dict(sel_base, lado=lado)
            if dos:
                pm = MK.devig(l['mas'], l['menos'])
                pm = pm if lado == 'mas' else 1 - pm
            else:   # un solo lado: se quita un margen típico de un lado (7 %)
                pm = min(0.97, (1 / cuota) / MARGEN_UN_LADO)
            nm = MS.nombre(sel, loc, vis)
            if nm in vistos:
                continue
            vistos.add(nm)
            out.append(evaluar(S, sel, cuota, pm, nm, MS.familia(sel)))
    for u in bet.get('unicos', []):
        for sel, cuota, pm in _opciones_unico(u):
            nm = MS.nombre(sel, loc, vis)
            if nm in vistos:
                continue
            vistos.add(nm)
            out.append(evaluar(S, sel, cuota, pm, nm, MS.familia(sel)))
    for jb in bet.get('jugadores', []):
        nm, st, lado = jb['jugador'], jb['stat'], jb.get('lado', 'local')
        if st == 'atajadas':
            for k, c in sorted(jb['escalera'].items()):
                sel = dict(mercado='atajadas', ambito=lado, lado='mas', linea=k - 0.5)
                out.append(evaluar(S, sel, c, min(0.97, (1 / c) / JG.VIG_JUGADOR), f'{nm} atajadas {k}+', 'jugador'))
        elif 'escalera' in jb:
            for k, c in sorted(jb['escalera'].items()):
                sel = dict(mercado='jugador', jugador=nm, stat=st, k=k)
                out.append(evaluar(S, sel, c, min(0.97, (1 / c) / JG.VIG_JUGADOR), MS.nombre(sel), 'jugador'))
        else:
            sel = dict(mercado='jugador', jugador=nm, stat=st, k=1)
            out.append(evaluar(S, sel, jb['cuota'], min(0.95, (1 / jb['cuota']) / 1.15), MS.nombre(sel), 'jugador'))
    for pj in bet.get('parejas', []):
        sel = dict(mercado='pareja', jugadores=list(pj['jugadores']), stat=pj['stat'])
        if any(nm not in S.get('jug', {}) for nm in sel['jugadores']):
            continue     # sin ficha de alguno de los dos: no se puede evaluar
        nm = MS.nombre(sel, loc, vis)
        if nm in vistos:
            continue
        vistos.add(nm)
        bajas = [x for x in sel['jugadores'] if x in fuera]
        # Con una baja confirmada el precio de Betano no sirve de referencia (aún cuenta al que no juega): solo la simulación.
        r = evaluar(S, sel, pj['cuota'], None if bajas else min(0.95, (1 / pj['cuota']) / 1.12), nm, 'pareja')
        if bajas:
            r['alerta'] = (f"{' y '.join(bajas)} es baja confirmada: la cuota sigue abierta en Betano; si no juega la selección "
                           'puede anularse o perderse (revisa las reglas) — no apostar')
            r['etiqueta'] += ' · ⚠ ' + r['alerta']
        out.append(r)
    diff_modelo = {}
    for l, nom in ((0, 'local'), (1, 'visitante')):
        for s, v in ((e.get('objetivos') or {}).get(nom) or {}).items():
            if s in obj0[l] and fuente[l].get(s, '').startswith('mercado') and obj0[l][s] > 0:
                r = v / obj0[l][s]
                if abs(r - 1) >= 0.15:
                    diff_modelo[f'{s}|{nom}'] = round(r, 2)
    res = dict(partido=f'{loc} - {vis}', liga=e.get('liga'), fecha=e.get('fecha'),
               tipo=ES.tipo_de_partido(sim), favorito=[loc, vis][fav],
               p_resultado={'local': round(float((sim[0]['g'] > sim[1]['g']).mean()), 3),
                            'empate': round(float((sim[0]['g'] == sim[1]['g']).mean()), 3),
                            'visitante': round(float((sim[0]['g'] < sim[1]['g']).mean()), 3)},
               guiones={g: round(float(p), 3) for g, p in zip(ES.GUIONES, pg)},
               objetivos={'local': {k: round(v, 2) for k, v in obj[0].items()},
                          'visitante': {k: round(v, 2) for k, v in obj[1].items()}},
               objetivos_sin_contexto={'local': {k: round(v, 2) for k, v in obj0[0].items()},
                                       'visitante': {k: round(v, 2) for k, v in obj0[1].items()}},
               fuente_objetivos={'local': fuente[0], 'visitante': fuente[1]},
               historial_vs_mercado=diff_modelo,
               lambdas_mercado=lm, contexto=aj.notas, sensibilidad=aj.sens,
               p_primer_gol={'local': round(float((sim['primer_eq'] == 0).mean()), 3),
                             'visitante': round(float((sim['primer_eq'] == 1).mean()), 3),
                             'nadie': round(float((sim['primer_eq'] == -1).mean()), 3)},
               p_gol_temprano_favorito=round(float(((sim['primer_eq'] == fav) & (sim['primer_min'] <= C.GOL_TEMPRANO_MIN)).mean()), 3),
               liga_base=ligas.resumen(e.get('liga')), lineas=out)
    res['favorito_lado'] = int(fav)
    res['medias'] = PR.medias(S, bet, media_mercado)             # media esperada por mercado y ámbito (modelo, sin ficha, Betano)
    res['jugadores_esperado'] = PR.jugadores_esperado(S, specs, bet) if specs else {}
    res['sistemas'] = sistemas.evaluar(e)
    res['alertas'] = sorted({r['alerta'] for r in out if r.get('alerta')})
    from . import enfoque as EN
    res['enfoque'] = EN.calcular(res, e)                          # qué mercados le quedan bien al contexto (solo orienta)
    res['enfoque_resumen'] = EN.resumen(res['enfoque'])
    EN.etiquetar(out, res['enfoque'])
    nl = MEM.nota_liga(e.get('liga'))
    for r in out:
        r['submercado'] = MS.submercado(r['sel'], fav)
        lado = r['sel'].get('lado')
        ns = MEM.notas(r['familia'], lado, r['submercado'], r['cuota'], r['ev']) if lado in ('mas', 'menos') else []
        if nl and r['ev'] >= 0.03:
            ns.append(nl)
        if ns:
            r['memoria'] = ns
            r['etiqueta'] += ' · ' + ' · '.join(ns)
    if builders:
        res['builders'] = armar_builders(out, lab, pg, fav=fav)
    if devolver_sim:
        res['_S'] = S
    for r in out:
        r.pop('_ev', None); r.pop('_pc', None)
    return res


# ------------------------------------------------------------------ builders
def armar_builders(lineas, lab, pg, max_cand=18, top=8, fav=None):
    """Combina 2–3 líneas del mismo partido. La probabilidad conjunta sale de los partidos simulados (no se
    multiplican como si fueran independientes); 'correlación' > 1 = las patas se ayudan entre sí."""
    cand = [r for r in lineas if r['p'] >= 0.55 and not r.get('asiatica')]
    mejor = {}
    for r in cand:   # una línea por mercado y ámbito: la de mejor p × cuota
        s = r['sel']
        k = (s['mercado'], s.get('ambito'), s.get('jugador'), s.get('stat'))
        if k not in mejor or r['p'] * r['cuota'] > mejor[k]['p'] * mejor[k]['cuota']:
            mejor[k] = r
    cand = sorted(mejor.values(), key=lambda r: -(r['p'] * r['cuota']))[:max_cand]
    out = []
    for n in (2, 3):
        for combo in itertools.combinations(cand, n):
            # 'Más córners: Local' y 'Córners Local Más 5.5' son casi la misma apuesta: se cuentan como el mismo mercado
            mercados = [c['sel'].get('stat') if c['sel']['mercado'] == 'mas_que' else c['sel']['mercado']
                        for c in combo if c['sel']['mercado'] != 'jugador']
            if len(set(mercados)) < len(mercados):
                continue   # dos líneas del mismo mercado (p. ej. córners totales y del local) son casi la misma apuesta
            j = np.logical_and.reduce([c['_ev'] for c in combo])
            j_sim = float(j.mean())
            if j_sim <= 0:
                continue
            prod_sim = math.prod(c['_pc'] for c in combo)
            factor = math.prod(c['p'] / c['_pc'] for c in combo if c['_pc'] > 0)
            fdep, ndep = DEP.factor([(c['sel'], c['_pc']) for c in combo], fav)
            joint = min(j_sim * factor * fdep, min(c['p'] for c in combo))
            justa = 1 / joint
            if not (1.6 <= justa <= 6.0):
                continue
            prod_cuotas = math.prod(c['cuota'] for c in combo)
            g = {nombre: float(j[lab == i].mean()) for i, nombre in enumerate(ES.GUIONES) if (lab == i).sum() > 200}
            rel = [g[ES.GUIONES[i]] * factor for i in range(len(ES.GUIONES))
                   if pg[i] >= C.UMBRAL_ESCENARIO_RELEVANTE and ES.GUIONES[i] in g]
            stress = min(joint * max(0.01, c['p'] - 0.05) / c['p'] for c in combo)
            margen = [c['p_mercado'] * c['cuota'] for c in combo if c.get('p_mercado')]
            avisos = sorted({m for c in combo for m in (c.get('memoria') or [])} | {c['alerta'] for c in combo if c.get('alerta')})
            out.append(dict(patas=[c['seleccion'] for c in combo], p=round(joint, 4), p_sim=round(j_sim, 4), cuota_justa=round(justa, 2),
                            p_stress=round(stress, 4), margen_acumulado=round(1 - math.prod(margen), 3) if margen else None,
                            avisos=avisos, ajuste_dependencia=round(fdep, 3) if ndep else None,
                            cuota_minima=round(1.03 / joint, 2), producto_cuotas=round(prod_cuotas, 2),
                            ev_si_paga_producto=round(joint * prod_cuotas - 1, 3),
                            correlacion=round(j_sim * fdep / prod_sim, 2) if prod_sim else None,
                            guion_comun=max(g, key=g.get) if g else None,
                            robustez=round(min(rel), 3) if rel else None))
    out.sort(key=lambda b: (-b['p'] * min(b['correlacion'] or 1, 1.3), -b['cuota_justa']))
    sel, usadas = [], {}
    for b in out:
        if any(usadas.get(x, 0) >= 2 for x in b['patas']):
            continue
        sel.append(b)
        for x in b['patas']:
            usadas[x] = usadas.get(x, 0) + 1
        if len(sel) >= top:
            break
    return sel
