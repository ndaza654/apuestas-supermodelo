#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contexto por partido y por mercado (lo que NO es la serie de números): qué se juega, cómo llega cada equipo, árbitro, onces,
y para cada mercado qué factores empujan hacia Más y cuáles hacia Menos en ESTE partido.

Uso: python3 recoleccion/contexto_mercado.py jornadas/AAAA-MM-DD   → jornadas/AAAA-MM-DD/contexto/<clave>.json  (lo lee el dashboard)

Dos fuentes, siempre separadas:
  1. Datos del repo: fichas/ficha_<clave>.json (promedios, esperado, directos), flashscore/<clave>.json (resultados recientes, árbitro), alineaciones/.
  2. Lectura de la situación hecha por Claude en la recolección: notas/<clave>.json  (ver NOTAS abajo). Sin notas, la parte de situación sale como
     «sin leer» y los factores de mercado quedan solo con datos: no se inventa motivación ni necesidad.
Los criterios (por qué algo empuja un mercado) son reglas generales de tipsters y medios, SIN resultados verificados: orientan, no prueban.

NOTAS (jornadas/<día>/notas/<clave>.json), todos los campos opcionales:
  {"se_juega": "texto corto", "tabla": "texto corto", "importancia": "alta|normal|baja", "decisivo": true, "derbi": false, "nada_en_juego": false,
   "local":     {"necesita_ganar": true, "le_sirve_empate": false, "rotacion": false, "animo": "texto corto"},
   "visitante": {...igual...},
   "arbitro": "texto corto si se leyó algo del árbitro", "onces": "texto corto", "fuentes": ["Flashscore tabla 13:50"]}
"""
import os, sys, json, glob

MERC = ['corners', 'goles', 'tarjetas', 'remates', 'al_arco', 'faltas', 'fueras', 'saques_banda', 'saques_meta']
UNICOS = ['ambos', 'resultado']   # una sola cuota por selección (desde el 18-nov-2026); salen de ficha['resultados']
NOM = {'corners': 'córners', 'goles': 'goles', 'tarjetas': 'tarjetas', 'remates': 'remates', 'al_arco': 'tiros al arco', 'faltas': 'faltas',
       'fueras': 'fueras de juego', 'saques_banda': 'saques de banda', 'saques_meta': 'saques de meta', 'ambos': 'ambos marcan', 'resultado': 'resultado'}


def _j(p):
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else None


def n1(x):
    return ('%.1f' % x).replace('.', ',')


def linea_principal(fm):
    """La línea total de Betano más pareja (Más y Menos con la cuota más cercana)."""
    best = None
    for l in fm.get('lineas', []):
        if l.get('ambito') != 'total':
            continue
        a, b = (l.get('mas') or {}).get('cuota'), (l.get('menos') or {}).get('cuota')
        if a and b:
            d = abs(a - b)
            if best is None or d < best[0]:
                best = (d, l['linea'])
    return best[1] if best else None


def bloque(F, m):
    if m in ('corners', 'goles', 'tarjetas'):
        return F.get(m)
    return (F.get('partido') or {}).get(m)


def racha(lista):
    """Últimos 5 (el primero es el más reciente): texto G/E/P y goles."""
    r, gf, gc = [], 0, 0
    for x in lista[:5]:
        g = x.get('g')
        if not g or g[0] is None:
            continue
        r.append('G' if g[0] > g[1] else 'E' if g[0] == g[1] else 'P')
        gf += g[0]
        gc += g[1]
    return r, gf, gc


def factores_datos(fm, m, loc, vis):
    """Factores que salen solo de la ficha. Cada uno: [dir, texto] con dir '+' (empuja a Más), '-' (a Menos) o '=' (para tener en cuenta)."""
    out = []
    if not fm:
        return out
    E, P = fm.get('esperado') or {}, fm.get('promedios') or {}
    L = linea_principal(fm)
    tot = E.get('total')
    if tot is not None and L is not None:
        margen = max(0.4, 0.05 * L)
        if tot - L >= margen:
            out.append(['+', f"Los datos esperan {n1(tot)} {NOM[m]} y la línea principal de Betano es {n1(L)}."])
        elif L - tot >= margen:
            out.append(['-', f"Los datos esperan {n1(tot)} {NOM[m]}, por debajo de la línea principal de Betano ({n1(L)})."])
        else:
            out.append(['=', f"Lo esperado ({n1(tot)}) está pegado a la línea principal de Betano ({n1(L)}): no hay margen por los datos."])
    la, lc, va, vc = (P.get(k) for k in ('local_a_favor', 'local_en_contra', 'visitante_a_favor', 'visitante_en_contra'))
    if None not in (la, lc, va, vc):
        # ¿quién lo genera? producción de uno contra lo que concede el otro
        for eq, hace, riv, concede in ((loc, la, vis, vc), (vis, va, loc, lc)):
            if hace and concede and hace >= 1.25 * concede and hace - concede >= 0.8:
                out.append(['=', f"{eq} suele hacer {n1(hace)}, pero {riv} solo concede {n1(concede)}: algo tiene que ceder."])
            elif hace and concede and concede >= 1.25 * hace and concede - hace >= 0.8:
                out.append(['=', f"{riv} concede {n1(concede)} por partido y {eq} hace {n1(hace)}: {eq} puede salir por encima de lo suyo."])
    S = fm.get('series') or {}
    for eq, k in ((loc, 'local'), (vis, 'visitante')):
        s = [a + b for a, b in (S.get(k) or []) if a is not None and b is not None]
        if len(s) >= 7:
            rec, todo = sum(s[:3]) / 3, sum(s) / len(s)
            if todo and rec >= 1.2 * todo:
                out.append(['+', f"Los partidos de {eq} vienen subiendo: {n1(rec)} en los últimos 3 contra {n1(todo)} de promedio."])
            elif todo and rec <= 0.8 * todo:
                out.append(['-', f"Los partidos de {eq} vienen bajando: {n1(rec)} en los últimos 3 contra {n1(todo)} de promedio."])
    d = [a + b for a, b in (S.get('directos') or []) if a is not None and b is not None]
    if len(d) >= 2 and L is not None:
        md = sum(d) / len(d)
        if md >= L + 1:
            out.append(['+', f"En sus {len(d)} directos recientes hubo {n1(md)} de promedio."])
        elif md <= L - 1:
            out.append(['-', f"En sus {len(d)} directos recientes hubo solo {n1(md)} de promedio."])
    return out


def _x(R, clave, sel, lado):
    """(x, n) de la regularidad guardada en ficha['resultados'][clave] para la selección; lado = 'reg_local' | 'reg_visitante' | 'directos'."""
    for f in (R or {}).get(clave) or []:
        if f.get('seleccion') == sel and f.get(lado):
            return f[lado]['x'], f[lado]['n']
    return None


def factores_unicos(N, m, loc, vis, F):
    """Factores de «ambos marcan» y «resultado»: datos de la ficha (cuántas veces pasó en los últimos partidos de cada equipo) + situación."""
    out = []
    R = F.get('resultados') or {}
    N = N or {}
    sl, sv = N.get('local') or {}, N.get('visitante') or {}
    dec = N.get('decisivo') or N.get('importancia') == 'alta'
    if m == 'ambos':
        a, b = _x(R, 'ambos', 'si', 'reg_local'), _x(R, 'ambos', 'si', 'reg_visitante')
        if a and b:
            for eq, (x, n) in ((loc, a), (vis, b)):
                if n and x / n >= 0.7:
                    out.append(['+', f"En {x} de sus últimos {n} partidos de {eq} marcaron los dos equipos."])
                elif n and x / n <= 0.4:
                    out.append(['-', f"En solo {x} de sus últimos {n} partidos de {eq} marcaron los dos equipos."])
        d = _x(R, 'ambos', 'si', 'directos')
        if d and d[1] >= 2:
            out.append(['+' if d[0] / d[1] >= 0.6 else '-' if d[0] / d[1] <= 0.34 else '=', f"En los directos: marcaron ambos en {d[0]} de {d[1]}."])
        for eq, s in ((loc, sl), (vis, sv)):
            if s.get('necesita_ganar'):
                out.append(['+', f"{eq} necesita ganar: si no va por delante, el partido se abre y el rival encuentra espacios."])
            if s.get('le_sirve_empate'):
                out.append(['-', f"A {eq} le sirve el empate: puede cerrarse y dejar a uno en cero."])
            if s.get('rotacion'):
                out.append(['=', f"{eq} rota titulares: sus promedios se hicieron con otro once."])
        if dec:
            out.append(['-', "Partido decisivo: los primeros tiempos suelen ser más cerrados; el «sí» llega tarde."])
    elif m == 'resultado':
        gl, gv = _x(R, 'resultado', '1', 'reg_local'), _x(R, 'resultado', '2', 'reg_visitante')
        if gl and gv:
            out.append(['=', f"{loc} ganó {gl[0]} de sus últimos {gl[1]}; {vis} ganó {gv[0]} de sus últimos {gv[1]}."])
        el, ev = _x(R, 'resultado', 'X', 'reg_local'), _x(R, 'resultado', 'X', 'reg_visitante')
        if el and ev:
            out.append(['=', f"Empates: {loc} {el[0]} de {el[1]}, {vis} {ev[0]} de {ev[1]}."])
        d = _x(R, 'resultado', '1', 'directos'), _x(R, 'resultado', '2', 'directos'), _x(R, 'resultado', 'X', 'directos')
        if all(d) and d[0][1] >= 2:
            out.append(['=', f"En los {d[0][1]} directos: {loc} ganó {d[0][0]}, {vis} ganó {d[1][0]}, empates {d[2][0]}."])
        for eq, s in ((loc, sl), (vis, sv)):
            if s.get('necesita_ganar'):
                out.append(['+', f"{eq} necesita ganar: va a por el partido (favorece la victoria suya y el «sin empate»)."])
            if s.get('le_sirve_empate'):
                out.append(['+', f"A {eq} le sirve el empate: sube el peso del empate y de la doble oportunidad a su favor."])
            if s.get('rotacion'):
                out.append(['-', f"{eq} rota titulares: baja su nivel esperado contra lo que dicen los últimos partidos."])
        if N.get('derbi'):
            out.append(['=', "Es un clásico o derbi: la forma pesa menos y el empate gana peso."])
    return out


def factores_situacion(N, m, loc, vis, F):
    """Factores que salen de la lectura de la situación (notas). Sin notas no hay ninguno."""
    out = []
    if not N:
        return out
    lados = (('local', loc, vis), ('visitante', vis, loc))
    dec, derbi, nada = N.get('decisivo') or N.get('importancia') == 'alta', N.get('derbi'), N.get('nada_en_juego') or N.get('importancia') == 'baja'
    for k, eq, riv in lados:
        s = N.get(k) or {}
        if s.get('necesita_ganar'):
            if m == 'corners':
                out.append(['+', f"{eq} necesita ganar: empuja, centra más y suma córners, sobre todo si llega empatando o perdiendo al final."])
            elif m == 'goles':
                out.append(['+', f"{eq} necesita ganar: si no va por delante, el partido se abre en el segundo tiempo."])
            elif m in ('remates', 'al_arco'):
                out.append(['+', f"{eq} necesita ganar: más llegadas y más {NOM[m]} suyos."])
            elif m == 'fueras':
                out.append(['+', f"{eq} necesita ganar y atacará más: más carreras al espacio y más fueras de juego suyos."])
            elif m == 'saques_meta':
                out.append(['+', f"{eq} necesita ganar: más remates desviados suyos son más saques de meta de {riv}."])
            elif m in ('tarjetas', 'faltas'):
                out.append(['+', f"{eq} necesita ganar: {riv} cortará contragolpes y tiempo con faltas tácticas."])
        if s.get('le_sirve_empate'):
            if m == 'corners':
                out.append(['-', f"A {eq} le sirve el empate: puede ceder la pelota y generar menos córners propios."])
            elif m == 'goles':
                out.append(['-', f"A {eq} le sirve el empate: no tiene por qué arriesgar, sobre todo en el primer tiempo."])
            elif m in ('remates', 'al_arco'):
                out.append(['-', f"A {eq} le sirve el empate: menos necesidad de atacar, menos {NOM[m]} suyos."])
        if s.get('rotacion'):
            if m in ('goles', 'remates', 'al_arco', 'corners'):
                out.append(['-', f"{eq} rota titulares: su promedio de {NOM[m]} se hizo con otro once."])
            else:
                out.append(['=', f"{eq} rota titulares: los promedios se hicieron con otro once."])
    if m in ('tarjetas', 'faltas'):
        if dec:
            out.append(['+', "Partido decisivo: más tensión, más protestas y más faltas tácticas."])
        if derbi:
            out.append(['+', "Es un clásico o derbi: suele subir la pierna fuerte."])
        if nada:
            out.append(['-', "No hay nada en juego: suele bajar la intensidad."])
        if N.get('arbitro'):
            out.append(['=', 'Árbitro: ' + N['arbitro']])
        elif texto_arbitro(F.get('arbitro')):
            out.append(['=', 'Árbitro: ' + texto_arbitro(F.get('arbitro'))])
    if m == 'tarjetas':
        fa = bloque(F, 'faltas')
        if fa and (fa.get('esperado') or {}).get('total') is not None:
            t = fa['esperado']['total']
            if t >= 26:
                out.append(['+', f"Se esperan muchas faltas ({n1(t)}): más ocasiones de amarilla."])
            elif t <= 21:
                out.append(['-', f"Se esperan pocas faltas ({n1(t)}): menos ocasiones de amarilla."])
    if m == 'corners':
        re = bloque(F, 'remates')
        if re and (re.get('esperado') or {}).get('total') is not None and re['esperado']['total'] >= 28:
            out.append(['+', f"Se espera mucho remate ({n1(re['esperado']['total'])}): los córners suelen acompañar."])
    if m == 'goles' and dec:
        out.append(['=', "Partido decisivo: los primeros tiempos suelen ser más cerrados de lo que dicen los promedios."])
    return out


def texto_arbitro(A):
    """Frase con lo leído del árbitro (ficha.arbitro, de ValueStats); '' si no hay estadísticas."""
    if not A or A.get('amarillas_pp') is None:
        return ''
    c = lambda v: ('%.2f' % v).rstrip('0').rstrip('.').replace('.', ',')
    t = f"{A.get('nombre')} (ValueStats): en sus últimos {A.get('muestra_n')} partidos {c(A['amarillas_pp'])} amarillas y {c(A['rojas_pp'])} rojas por partido"
    if A.get('puntos_pp_muestra') is not None:
        t += f" ({c(A['puntos_pp_muestra'])} puntos Betano)"
    if A.get('penales_muestra') is not None:
        t += f"; {A['penales_muestra']} penales en esos partidos"
    if A.get('amarillas_pp_historial') is not None:
        t += f"; historial de {A.get('partidos')} partidos: {c(A['amarillas_pp_historial'])} amarillas por partido"
    if A.get('supera'):
        t += f"; la muestra superó 3,5 tarjetas en {c(A['supera']['3.5'])} %, 4,5 en {c(A['supera']['4.5'])} % y 5,5 en {c(A['supera']['5.5'])} %"
    if A.get('faltas_pp_muestra') is not None:
        t += f"; faltas pitadas por partido: {c(A['faltas_pp_muestra'])}"
        if A.get('fueras_juego_pp_muestra') is not None:
            t += f", fueras de juego {c(A['fueras_juego_pp_muestra'])}"
    return t + '.'


def contexto_de(base, clave):
    F = _j(os.path.join(base, 'fichas', f'ficha_{clave}.json'))
    if not F:
        return None
    if not F.get('arbitro'):    # la ficha de mercado no copia el árbitro: viene de la entrada (ficha.arbitro, ValueStats)
        F['arbitro'] = ((_j(os.path.join(base, 'entradas', clave + '.json')) or {}).get('ficha') or {}).get('arbitro')
    N = _j(os.path.join(base, 'notas', clave + '.json')) or {}
    FS = _j(os.path.join(base, 'flashscore', clave + '.json')) or {}
    AL = _j(os.path.join(base, 'alineaciones', clave + '.json')) or {}
    loc, vis = [x.strip() for x in F['encuentro'].split(' - ', 1)]
    part, falta = [], []
    part.append(['Qué se juega', N.get('se_juega') or 'Sin leer: no se revisó qué hay en juego en este partido.'])
    if not N.get('se_juega'):
        falta.append('qué se juega')
    if N.get('tabla'):
        part.append(['Tabla', N['tabla']])
    else:
        falta.append('tabla')
    for k, eq in (('local', loc), ('visitante', vis)):
        r, gf, gc = racha((FS.get('forma') or {}).get(k) or [])
        s = N.get(k) or {}
        txt = []
        if r:
            txt.append(f"últimos {len(r)}: {' '.join(reversed(r))} (del más antiguo al más reciente), {gf} goles a favor y {gc} en contra")
        marcas = [t for c, t in (('necesita_ganar', 'necesita ganar'), ('le_sirve_empate', 'le sirve el empate'), ('rotacion', 'rota titulares')) if s.get(c)]
        if marcas:
            txt.append(', '.join(marcas))
        if s.get('animo'):
            txt.append(s['animo'])
        part.append([f'Cómo llega {eq}', ('; '.join(txt) + '.') if txt else 'Sin datos de resultados recientes.'])
    arb = FS.get('arbitro')
    ta = texto_arbitro(F.get('arbitro'))
    part.append(['Árbitro', ta or ((f"{arb}. " if arb else 'Sin anunciar. ') + (N.get('arbitro') or 'Sin promedio de tarjetas ni de faltas: no se recolectó.'))])
    if not N.get('arbitro') and not ta:
        falta.append('estadísticas del árbitro')
    if AL.get('probables', {}).get('L'):
        nb = len((AL.get('bajas') or {}).get('L') or []), len((AL.get('bajas') or {}).get('V') or [])
        part.append(['Onces', f"{AL.get('tipo') or 'Alineaciones'} de Flashscore. Bajas: {loc} {nb[0]}, {vis} {nb[1]}." + (' ' + N['onces'] if N.get('onces') else '')])
    else:
        part.append(['Onces', 'Sin alineación publicada: los mercados de jugador no se recomiendan.'])
        falta.append('alineaciones')
    mercados = {}
    for m in MERC:
        fm = bloque(F, m)
        if not fm or not fm.get('lineas'):
            continue
        fs = factores_situacion(N, m, loc, vis, F) + factores_datos(fm, m, loc, vis)
        if m == 'tarjetas':
            fs.append(['=', 'La serie solo cuenta amarillas; Betano cuenta puntos (roja = 2).'])
        mercados[m] = fs
    for m in UNICOS:
        if (F.get('resultados') or {}).get(m):
            mercados[m] = factores_unicos(N, m, loc, vis, F)
    return {'partido': part, 'mercados': mercados, 'con_notas': bool(N), 'falta': falta, 'fuentes': N.get('fuentes') or [],
            'criterios': 'Reglas generales de tipsters y medios, sin resultados verificados: orientan, no prueban.'}


def main(argv):
    base = argv[0]
    os.makedirs(os.path.join(base, 'contexto'), exist_ok=True)
    n = 0
    for p in sorted(glob.glob(os.path.join(base, 'fichas', 'ficha_*.json'))):
        clave = os.path.basename(p)[6:-5]
        c = contexto_de(base, clave)
        if c:
            json.dump(c, open(os.path.join(base, 'contexto', clave + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
            n += 1
            print(f"{clave:34s} notas {'sí' if c['con_notas'] else 'NO'} · mercados {len(c['mercados'])} · factores {sum(len(v) for v in c['mercados'].values())}")
    print(n, 'contextos escritos en', os.path.join(base, 'contexto'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
