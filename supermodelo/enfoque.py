# -*- coding: utf-8 -*-
"""Enfoque de mercados por contexto (regla del usuario, 11-nov-2026).

Antes de mirar líneas, el modelo lee el partido y dice en palabras QUÉ MERCADOS le quedan bien al contexto y cuáles no
("este partido es mejor para córners que para tarjetas"). Con eso el análisis a fondo se concentra donde el contexto ayuda.

No es la tabla de guiones con probabilidades (esa sigue en el informe como herramienta de robustez). No cambia ninguna
probabilidad ni EV: es una hipótesis que orienta el análisis; si el número dice otra cosa, manda el número.
Cada razón sale de un hecho de la ficha o de la media esperada del modelo; si falta el dato, el mercado queda «sin señal».
Los umbrales están en config.py (ENFOQUE_*).
"""
from . import config as C
from . import ligas

ESTADOS = ('favorece', 'neutro', 'en contra', 'sin señal')


def _m(A, mercado, ambito='total', campo='modelo'):
    for r in A.get('medias') or []:
        if r['mercado'] == mercado and r['ambito'] == ambito:
            return r.get(campo)
    return None


def _entrada(fam, titulo, estado, porque, lado=None, ambito=None):
    return dict(familia=fam, mercado=titulo, estado=estado, lado=lado, ambito=ambito, porque=porque)


def calcular(A, e):
    ficha = (e or {}).get('ficha') or {}
    loc, vis = A['partido'].split(' - ', 1) if ' - ' in A['partido'] else ('Local', 'Visitante')
    pr = A.get('p_resultado') or {}
    fav_lado = 'local' if A.get('favorito_lado', 0) == 0 else 'visitante'
    nom_fav = loc if fav_lado == 'local' else vis
    pf = pr.get(fav_lado)
    dom = 'claro' if (pf or 0) >= C.ENFOQUE_FAV_CLARO else ('leve' if (pf or 0) >= C.ENFOQUE_FAV_LEVE else 'parejo')
    imp = ficha.get('importancia', 'normal')
    elim = ficha.get('eliminatoria')
    ida = bool(elim) and (elim.get('global_local', 0) or 0) == (elim.get('global_visitante', 0) or 0)
    fl, fv = ficha.get('local') or {}, ficha.get('visitante') or {}
    p = ligas.prior((e or {}).get('liga')) or {}
    out = []

    # ------------------------------------------------------------ goles del partido
    g = _m(A, 'goles')
    razones, lado = [], None
    if g is not None:
        if g >= C.ENFOQUE_GOLES_ALTO:
            lado = 'mas'; razones.append('el modelo espera un partido de muchos goles')
        elif g <= C.ENFOQUE_GOLES_BAJO:
            lado = 'menos'; razones.append('el modelo espera un partido de pocos goles')
    if dom == 'parejo' and (imp in ('alta', 'final') or fl.get('necesita_ganar') or fv.get('necesita_ganar')):
        razones.append('parejo y con mucho en juego: se cuidan'); lado = lado or 'menos'
    if ida:
        razones.append('eliminatoria igualada / ida: nadie quiere abrirse'); lado = lado or 'menos'
    cl = ficha.get('clima') or {}
    if cl.get('lluvia') in ('fuerte', 'moderada', True, 'si', 'sí') or cl.get('viento_fuerte'):
        razones.append('clima que frena el juego'); lado = 'menos' if lado != 'mas' else lado
    if fl.get('rotacion') or fv.get('rotacion'):
        razones.append('hay rotación: baja la producción')
    est = 'favorece' if lado else 'neutro'
    out.append(_entrada('goles', f"Goles del partido ({'Más' if lado == 'mas' else 'Menos'})" if lado else 'Goles del partido',
                        est, '; '.join(razones) or 'ni muchos ni pocos goles esperados', lado, 'total'))

    # ------------------------------------------------------------ goles 1.er tiempo / empate al descanso
    if lado == 'menos' or ida or dom == 'parejo':
        out.append(_entrada('goles', '1.er tiempo (Menos) y empate al descanso', 'favorece',
                            'partidos que se miden o parejos arrancan despacio', 'menos', '1T'))

    # ------------------------------------------------------------ ambos marcan
    gl, gv = _m(A, 'goles', 'local'), _m(A, 'goles', 'visitante')
    if gl is not None and gv is not None:
        minimo = min(gl, gv)
        if minimo < C.ENFOQUE_EQUIPO_FLOJO:
            out.append(_entrada('ambos', 'Ambos marcan', 'en contra',
                                f"{loc if gl < gv else vis} marca poco en este partido", 'si'))
        elif minimo >= C.ENFOQUE_EQUIPO_ANOTA and lado != 'menos':
            out.append(_entrada('ambos', 'Ambos marcan', 'favorece', 'los dos tienen producción para marcar', 'si'))
        else:
            out.append(_entrada('ambos', 'Ambos marcan', 'neutro', 'sin ventaja clara para ninguna de las dos opciones'))

    # ------------------------------------------------------------ favorito / hándicap / equipo
    if dom == 'claro':
        out.append(_entrada('resultado', f'Hándicap y victoria de {nom_fav}', 'favorece',
                            'favorito claro: manda en el marcador y en el territorio', 'local' if fav_lado == 'local' else 'visitante'))
        out.append(_entrada('goles', f'Goles de {nom_fav} (Más)', 'favorece', 'favorito claro contra rival que sufre', 'mas', fav_lado))
        out.append(_entrada('remates', f'Remates / tiros al arco de {nom_fav}', 'favorece', 'el que domina remata más', 'mas', fav_lado))
    elif dom == 'parejo':
        out.append(_entrada('resultado', 'Hándicap y victoria', 'en contra', 'partido parejo: ningún equipo manda'))
        out.append(_entrada('resultado', 'Empate / doble oportunidad / HT-FT X', 'favorece', 'sin dominador claro el empate pesa más'))
    else:
        out.append(_entrada('resultado', 'Resultado / hándicap', 'neutro', f'{nom_fav} favorito leve: el precio ya lo recoge'))

    # ------------------------------------------------------------ córners
    cm, cl_, cv_ = _m(A, 'corners'), _m(A, 'corners', 'local'), _m(A, 'corners', 'visitante')
    ref = p.get('corners_x_partido') or _m(A, 'corners', 'total', 'betano')
    razones, lado_c, est_c = [], None, 'neutro'
    if cm is None:
        out.append(_entrada('corners', 'Córners', 'sin señal', 'el modelo no tiene media de córners'))
    else:
        if ref:
            if cm >= ref + C.ENFOQUE_CORNERS_DIF:
                lado_c = 'mas'; razones.append('se espera claramente por encima de lo normal de la liga / del precio')
            elif cm <= ref - C.ENFOQUE_CORNERS_DIF:
                lado_c = 'menos'; razones.append('se espera claramente por debajo de lo normal')
        else:
            razones.append('no hay base de la liga para comparar')
        dif = (cl_ or 0) - (cv_ or 0)
        if abs(dif) >= C.ENFOQUE_CORNERS_EQUIPO:
            quien = loc if dif > 0 else vis
            out.append(_entrada('corners', f'Córners de {quien} (Más) / Más córners: {quien}', 'favorece',
                                f'{quien} empuja más y el rival se encierra o cede territorio', 'mas', 'local' if dif > 0 else 'visitante'))
        if dom == 'claro':
            razones.append('si el favorito marca pronto, sus córners se apagan; si el rival forzara, suben')
        if fl.get('rotacion') or fv.get('rotacion'):
            razones.append('rotación: el control sigue, pero baja el empuje')
        estilos = set(fl.get('estilo') or []) | set(fv.get('estilo') or [])
        if 'bloque_bajo' in estilos and dom != 'parejo':
            razones.append('hay bloque bajo: el rival acumula córners')
            if lado_c is None:
                lado_c = 'mas'
        if ('centros' in estilos or 'balon_parado' in estilos) and lado_c != 'menos':
            razones.append('juego de centros / balón parado')
        if lado_c:
            est_c = 'favorece'
        elif not ref:
            est_c = 'sin señal'
        out.append(_entrada('corners', f"Córners totales ({'Más' if lado_c == 'mas' else 'Menos'})" if lado_c else 'Córners totales',
                            est_c, '; '.join(razones) or 'ni a favor ni en contra', lado_c, 'total'))

    # ------------------------------------------------------------ tarjetas y faltas
    arb = ficha.get('arbitro') or {}
    tp, ml = arb.get('tarjetas_por_partido'), arb.get('media_liga') or p.get('tarjetas_betano_x_partido')
    if tp is None and arb.get('amarillas_por_partido') is not None:
        tp = (arb.get('amarillas_por_partido') or 0) + 2 * (arb.get('rojas_por_partido') or 0)
    pts, razones = 0, []
    if ficha.get('derbi'):
        pts += 1; razones.append('derbi / rivalidad')
    if tp and ml:
        r = tp / ml
        if r >= C.ENFOQUE_ARBITRO_ALTO:
            pts += 1; razones.append('árbitro que saca más tarjetas que la liga')
        elif r <= C.ENFOQUE_ARBITRO_BAJO:
            pts -= 1; razones.append('árbitro de pocas tarjetas')
    else:
        razones.append('árbitro sin dato')
    if imp in ('alta', 'final') or (fl.get('necesita_ganar') and fv.get('necesita_ganar')):
        pts += 1; razones.append('los dos se juegan algo importante')
    if dom == 'parejo':
        pts += 1; razones.append('parejo: más duelos y más faltas')
    if dom == 'claro':
        pts -= 1; razones.append('favorito claro: poca fricción y, si hay goleada, menos tarjetas')
    if fl.get('motivacion') == 'baja' or fv.get('motivacion') == 'baja':
        pts -= 1; razones.append('alguien sin nada en juego')
    if tp is None and not ficha.get('derbi') and imp == 'normal' and dom == 'leve':
        est_t = 'sin señal'
    else:
        est_t = 'favorece' if pts >= 2 else ('en contra' if pts <= -1 else 'neutro')
    if est_t == 'en contra':     # el contexto pide pocas tarjetas: se ofrece el lado Menos, no un «en contra» ambiguo
        for fam, nom in (('tarjetas', 'Tarjetas (Menos)'), ('faltas', 'Faltas (Menos)')):
            out.append(_entrada(fam, nom, 'favorece', '; '.join(razones), 'menos', 'total'))
    else:
        lado_t = 'mas' if est_t == 'favorece' else None
        out.append(_entrada('tarjetas', 'Tarjetas y faltas' + (' (Más)' if lado_t else ''), est_t,
                            '; '.join(razones) or 'árbitro cerca de la media y sin otros factores de fricción', lado_t, 'total'))

    # ------------------------------------------------------------ jugadores
    jug = ficha.get('jugadores') or (e or {}).get('jugadores') or []
    dudas = [j for j in jug if (j.get('titular') or 0) < 0.8 and not j.get('fuera')]
    if fl.get('rotacion') or fv.get('rotacion'):
        out.append(_entrada('jugador', 'Líneas de jugador', 'en contra', 'hay rotación: sin once confirmado no se sabe quién juega'))
    elif dudas:
        out.append(_entrada('jugador', 'Líneas de jugador', 'neutro', f'{len(dudas)} jugadores con titularidad dudosa: esperar el once'))
    elif jug:
        out.append(_entrada('jugador', 'Líneas de jugador', 'neutro', 'se pueden mirar con la alineación de la ficha'))
    return out


def resumen(enf):
    fav = [x['mercado'] for x in enf if x['estado'] == 'favorece']
    con = [x['mercado'] for x in enf if x['estado'] == 'en contra']
    t = 'Enfoque: ' + ('mirar primero ' + ', '.join(fav) if fav else 'ningún mercado destaca por contexto')
    if con:
        t += '. Poco favorecidos: ' + ', '.join(con)
    return t + '.'


def etiquetar(lineas, enf):
    """Marca cada línea con el enfoque de su mercado: 'a favor', 'en contra' o None (no cambia ninguna probabilidad)."""
    for r in lineas:
        s = r['sel']
        marca = None
        for x in enf:
            if x['familia'] != r['familia'] or x['estado'] not in ('favorece', 'en contra'):
                continue
            if x['lado'] is not None and s.get('lado') not in (x['lado'], None) and r['familia'] not in ('resultado',):
                continue
            if x['ambito'] in ('local', 'visitante', '1T') and s.get('ambito') != x['ambito']:
                continue
            marca = 'a favor' if x['estado'] == 'favorece' else 'en contra'
            if marca == 'a favor':
                break
        r['enfoque'] = marca
        if marca:
            r['etiqueta'] += ' · ' + ('★ enfoque a favor' if marca == 'a favor' else 'enfoque en contra')


def html(enf, resumen_txt, esc=lambda x: x):
    simb = {'favorece': ('✅ favorece', 'ok'), 'neutro': ('➖ neutro', ''), 'en contra': ('⛔ en contra', 'no'), 'sin señal': ('❔ sin señal', '')}
    filas = ''.join(f"<tr class='{simb[x['estado']][1]}'><td>{esc(x['mercado'])}</td><td>{simb[x['estado']][0]}</td><td>{esc(x['porque'])}</td></tr>"
                    for x in sorted(enf, key=lambda x: ESTADOS.index(x['estado'])))
    return (f"<section id='enfoque'><h2>Enfoque de mercados</h2><div class='box key'><p><b>{esc(resumen_txt)}</b></p>"
            f"<div class='tw'><table><thead><tr><th>Mercado</th><th>Encaje con el contexto</th><th>Por qué</th></tr></thead><tbody>{filas}</tbody></table></div>"
            "<p class='method'>Hipótesis para decidir dónde analizar a fondo, leída del contexto de la ficha y de la media esperada del modelo. "
            "No cambia ninguna probabilidad: si el número dice otra cosa, manda el número.</p></div></section>")


def markdown(enf, resumen_txt):
    L = ['## Enfoque de mercados (qué mercados le quedan bien al contexto)', resumen_txt, '',
         '| Mercado | Encaje | Por qué |', '|---|---|---|']
    simb = {'favorece': '✅ favorece', 'neutro': '➖ neutro', 'en contra': '⛔ en contra', 'sin señal': '❔ sin señal'}
    for x in sorted(enf, key=lambda x: ESTADOS.index(x['estado'])):
        L.append(f"| {x['mercado']} | {simb[x['estado']]} | {x['porque']} |")
    L += ['', 'Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.', '']
    return L
