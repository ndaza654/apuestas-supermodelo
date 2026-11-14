# -*- coding: utf-8 -*-
"""Une lo recolectado de un partido en la ENTRADA que leen el modelo y las fichas.

Entradas:  betano/<clave>.json   (recoleccion/betano.py: {meta, betano})
           flashscore/<clave>.json (recoleccion/flashscore_extraer.js: contexto del partido)  [opcional]
           jugadores/<clave>.json (historial por jugador de la alineación probable, de Flashscore)  [opcional]
           alineaciones/<clave>.json (Flashscore: XI probable y bajas; formato compacto de alineaciones/LEEME.md)  [opcional]
           clima/clima.json y clasificacion/clasificacion.json (Open-Meteo y tablas de Flashscore, por clave)  [opcional]
           notas/<clave>.json    (lectura de la situación hecha por Claude: importancia, motivación, rotación… ver NOTAS_EJEMPLO)  [opcional]
Salida:    entradas/<clave>.json
Lo que falta se deja VACÍO y se declara en ficha.dudas / ficha.faltan; nunca se rellena con supuestos.

Uso:  python3 recoleccion/armar_entrada.py jornadas/2026-11-13 [clave ...]
"""
import json, os, sys, glob, re, unicodedata, datetime as dt

H2H_ANOS = 5          # los directos más viejos que esto no cuentan (cambiar aquí si se quiere otra ventana)

NOTAS_EJEMPLO = {'importancia': 'alta|normal|baja', 'derbi': False, 'eliminatoria': None,
                 'local': {'motivacion': 'normal|alta|baja', 'rotacion': False, 'necesita_ganar': False, 'estilo': []},
                 'visitante': {'motivacion': 'normal|alta|baja', 'rotacion': False, 'necesita_ganar': False, 'estilo': []},
                 'bajas': [], 'dudas': [], 'fuentes': []}


def _json(base, rel):
    p = os.path.join(base, rel)
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else {}


def _equipo(n=None):
    base = {'estilo': [], 'estilo_nuevo': False, 'marcador': 'normal', 'rotacion': False, 'motivacion': 'normal',
            'necesita_ganar': False, 'perfil_corners': {}, 'propositivo': None, 'dias_descanso': None, 'viaje_largo': False}
    base.update(n or {})
    return base


def forma_de(partidos):
    """[fecha, rival, v, [gf,gc], stats] (o dict) → lista de partidos en el formato de ficha.forma (más reciente primero)."""
    out = []
    for p in partidos:
        if isinstance(p, dict):
            fecha, rival, v, g, st, comp = p['fecha'], p['rival'], p['v'], p['g'], p.get('stats', {}), p.get('comp', '')
        else:
            fecha, rival, v, g, st = p[:5]
            comp = ''
        stats = {k: list(x) for k, x in st.items()}
        stats['g'] = list(g)
        out.append({'v': v, 'fecha': fecha, 'rival': rival, 'comp': comp, 'stats': stats})
    return out


def h2h_de(directos, hoy=None, anos=H2H_ANOS):
    """Directos con estadística; si se da `hoy` (AAAA-MM-DD) se descartan los de más de `anos` años."""
    out = []
    corte = None
    if hoy and anos:
        y, m, d = map(int, hoy[:10].split('-'))
        corte = f'{y - anos:04d}-{m:02d}-{d:02d}'
    for d in directos:
        fecha, g, st = (d['fecha'], d['g'], d.get('stats', {})) if isinstance(d, dict) else d[:3]
        if corte and fecha < corte:
            continue
        if st:                                                    # solo los directos con alguna estadística sirven a la ficha
            out.append({'fecha': fecha, 'stats': {k: list(x) for k, x in st.items()} | {'g': list(g)}})
    return out


def _norm(x):
    x = unicodedata.normalize('NFD', x or '')
    return re.sub(r'[^a-z0-9 ]+', ' ', ''.join(c for c in x if unicodedata.category(c) != 'Mn').lower().replace('đ', 'd').replace('ł', 'l')).split()


def coincide(nombre_flashscore, nombre_betano):
    """«Verbruggen B.» ≈ «Bart Verbruggen»; «van Hecke J. P.» ≈ «Jan Paul van Hecke» (apellido al final y misma inicial)."""
    t = _norm(nombre_flashscore)
    iniciales = []
    while t and len(t[-1]) == 1:
        iniciales.insert(0, t.pop())
    b = _norm(nombre_betano)
    if not t or not b:
        return False
    if b[-len(t):] != t:
        return False
    resto = b[:-len(t)]
    return not iniciales or (bool(resto) and resto[0][0] == iniciales[0])


def jugadores_de(lu, betano, hora_lectura=''):
    """Alineación probable de Flashscore → `jugadores` del modelo (solo titulares anunciados y bajas; el resto no se inventa)."""
    out, sin_casar = [], []
    if not lu or not lu.get('probables'):
        return out, sin_casar
    nombres = {(j['jugador'], j.get('lado')) for j in betano.get('jugadores', [])}
    fuente = f"Flashscore «{lu.get('tipo') or 'alineaciones probables'}»" + (f' leída {hora_lectura}' if hora_lectura else '')
    for lado_fs, lado in (('L', 'local'), ('V', 'visitante')):
        for p in lu['probables'].get(lado_fs, []):
            cas = [n for n, ld in nombres if coincide(p['n'], n) and (ld in (lado, lado[0].upper(), None))]
            if cas:
                out.append({'nombre': cas[0], 'lado': lado, 'titular': 0.9, 'minutos': 80, 'fuentes_xi': '1/1', 'fuente': fuente})
            else:
                sin_casar.append(p['n'])
        for p in lu.get('bajas', {}).get(lado_fs, []):
            cas = [n for n, ld in nombres if coincide(p['n'], n)]
            for n in cas[:1]:
                choque = [j for j in out if j['nombre'] == n and not j.get('fuera')]
                out[:] = [j for j in out if j not in choque]          # la baja manda sobre el XI probable
                out.append({'nombre': n, 'lado': lado, 'titular': 0.0, 'minutos': 0, 'fuera': True, 'conflicto_xi': bool(choque),
                            'fuente': fuente + ' · baja: ' + (p.get('motivo') or '') + (' · figura también en el XI probable (Flashscore se contradice)' if choque else '')})
    return out, sin_casar


def hist_de(jug, betano):
    """Historial por jugador de Flashscore (jugadores/<clave>.json) → ficha.jugadores_hist con los nombres de Betano.
    Cada aparición: [mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas, entradas] (la más reciente primero).
    Solo cuenta lo jugado dentro de los últimos 7 partidos oficiales del equipo; el resto no se inventa."""
    out, sin = {}, []
    nombres = sorted({j['jugador'] for j in betano.get('jugadores', [])})
    for fs_n, d in (jug or {}).items():
        cas = [n for n in nombres if coincide(fs_n, n)]
        if len(cas) != 1:
            if d.get('p'):
                sin.append(fs_n)
            continue
        partidos = []
        for a in d['p']:
            mid, fecha, mn, sh, sot, g, asi, am, ro, fa, en = a
            partidos.append({'fecha': fecha, 'mid': mid, 'min': mn, 'remates': sh, 'al_arco': sot, 'goles': g, 'asist': asi,
                             'tarjeta': (am or 0) + (ro or 0), 'faltas': fa, 'entradas': en})
        out[cas[0]] = {'pos': d.get('pos'), 'partidos': partidos}
    return out, sin


LECTURA_ALINEACIONES = 'vie 13-nov ~19:15-19:45 Bogotá'
FILA = re.compile(r'^(\d+)\.\s+(.+?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+:\d+)\s+(-?\d+)\s+(\d+)\b')


def lineups_de(al):
    """alineaciones/<clave>.json (compacto) → la forma que lee jugadores_de(); None si Flashscore no tiene la pestaña."""
    if not al or al.get('sin_pestana') or not al.get('probables', {}).get('L'):
        return None
    p = lambda a: [{'n': x[0], 'num': x[1], 'pid': x[2], 'gk': bool(x[3])} for x in a]
    b = lambda a: [{'n': x[0], 'pid': x[1], 'motivo': x[2]} for x in a]
    return {'tipo': al.get('tipo'), 'probables': {k: p(v) for k, v in al['probables'].items()},
            'bajas': {k: b(v) for k, v in al.get('bajas', {}).items()}}


GENERICAS = {'real', 'club', 'fc', 'cf', 'cd', 'ud', 'sc', 'sp', 'de', 'del', 'la', 'el', 'atletico', 'atl', 'deportivo', 'dep', 'ii', 'b', 'sad', 'rcd'}


def fila_de(tabla, equipo):
    """Fila de la tabla (texto de Flashscore) que corresponde al equipo; None si no hay UNA sola que case.
    1.º nombres contenidos uno en el otro («Querétaro» ⊂ «Queretaro FC»); 2.º, si no, una palabra distintiva en común
    («Sporting de Gijón» ↔ «Real Sporting»). Si hay duda (0 o varias filas) no se adivina."""
    t = set(_norm(equipo))
    filas = [(m, set(_norm(m.group(2)))) for m in (FILA.match(f) for f in tabla.get('filas', [])) if m]
    hallados = [m for m, n in filas if n and t and (n <= t or t <= n)]
    if len(hallados) != 1:
        hallados = [m for m, n in filas if (n & t) - GENERICAS]
    if len(hallados) != 1:
        return None
    m = hallados[0]
    cab = (tabla.get('cab') or '').split(' | ')
    grupo = cab[1] if len(cab) > 1 and cab[1].upper().startswith('GRUPO') else ''
    return {'pos': int(m.group(1)), 'equipo': m.group(2), 'pj': int(m.group(3)), 'g': int(m.group(4)), 'e': int(m.group(5)), 'p': int(m.group(6)),
            'gf_gc': m.group(7), 'dg': int(m.group(8)), 'pts': int(m.group(9)), 'grupo': grupo}


def clima_de(c):
    """clima.json[clave] → dict de la ficha (lo que leen el modelo y el puntuador). Las tres horas son inicio, +1 h y +2 h (UTC).
    temperatura = la de la hora de inicio; lluvia «fuerte» solo si ≥ 7,6 mm/h (umbral OMM de lluvia intensa) y viento fuerte si ≥ 30 km/h:
    umbrales fijos y objetivos; lo demás se deja como dato en `texto` para que lo juzgue el análisis."""
    if not c or not c.get('horas_utc') or not c['horas_utc'][0]:
        return None
    hs = [h for h in c['horas_utc'] if h]
    t, hum, pp, mm, v, cod = hs[0][1:7]
    mm_max, v_max, pp_max = max(h[4] for h in hs), max(h[5] for h in hs), max(h[3] for h in hs)
    texto = (f"{t:g} °C al inicio, humedad {hum} %, prob. de lluvia máx. {pp_max} %, lluvia máx. {mm_max:g} mm/h, viento máx. {v_max:g} km/h "
             f"(código OMM al inicio {cod}) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio")
    return {'temperatura': t, 'lluvia': 'fuerte' if mm_max >= 7.6 else None, 'viento_fuerte': v_max >= 30,
            'lluvia_mm_max': mm_max, 'prob_lluvia_max': pp_max, 'viento_kmh_max': v_max, 'texto': texto}


def armar(b, fs=None, notas=None, jug=None):
    meta, bet = b['meta'], b['betano']
    notas = notas or {}
    ini = dt.datetime.fromisoformat(meta['inicio_utc'].replace('Z', '+00:00')) - dt.timedelta(hours=5)     # hora de Bogotá
    faltan, dudas = [], list(notas.get('dudas', []))
    ficha = {'derbi': notas.get('derbi', False), 'importancia': notas.get('importancia', 'normal'), 'eliminatoria': notas.get('eliminatoria'),
             'local': _equipo(notas.get('local')), 'visitante': _equipo(notas.get('visitante')),
             'bajas': notas.get('bajas', []), 'dudas': dudas, 'fuentes': notas.get('fuentes', []), 'jugadores_hist': notas.get('jugadores_hist', {})}
    if fs:
        ficha['forma'] = {'local': forma_de(fs['forma']['local']), 'visitante': forma_de(fs['forma']['visitante'])}
        ficha['h2h'] = h2h_de(fs.get('h2h', []), ini.strftime('%Y-%m-%d'))
        ficha['arbitro'] = {'nombre': fs.get('arbitro') or '', 'pais': fs.get('arbitro_pais'), 'tarjetas_por_partido': None, 'partidos': None,
                            'nota': 'Nombre anunciado por Flashscore; las estadísticas del árbitro (B-Soccer) no están recolectadas.'}
        ficha['fuentes'] = ficha['fuentes'] + ['Flashscore (últimos partidos, estadísticas y H2H)']
        for av in fs.get('avisos', []):
            dudas.append('Flashscore: ' + av)
    else:
        ficha['forma'] = {'local': [], 'visitante': []}
        ficha['arbitro'] = {'nombre': '', 'tarjetas_por_partido': None, 'partidos': None}
        faltan.append('estadísticas de los últimos partidos (sin Flashscore)')
    if not notas:
        faltan.append('lectura de la situación (importancia, motivación, rotación, tabla)')
    if not ficha['jugadores_hist'] and jug:
        ficha['jugadores_hist'], sin_h = hist_de(jug, bet)
        ficha['fuentes'] = ficha['fuentes'] + ['Flashscore (estadísticas de jugadores de los últimos 7 partidos de cada selección; solo jugadores de la alineación probable)']
        if sin_h:
            dudas.append('Historial: sin casar con Betano → ' + ', '.join(sin_h))
    if not ficha['jugadores_hist']:
        faltan.append('historial por jugador (remates, tiros al arco): sin él los mercados de jugadores no se pueden filtrar')
    ficha['faltan'] = faltan
    jugadores = notas.get('jugadores', [])
    if not jugadores and fs and fs.get('lineups'):
        jugadores, sin = jugadores_de(fs['lineups'], bet, fs.get('lineups_leidas', ''))
        if sin:
            dudas.append('Alineación probable: sin casar con Betano → ' + ', '.join(sin))
        for j in jugadores:
            if j.get('conflicto_xi'):
                dudas.append(f"{j['nombre']}: Flashscore lo lista en el XI probable y también como baja; se toma como baja")
        if jugadores:
            ficha['fuentes'] = ficha['fuentes'] + ['Flashscore (alineaciones probables y bajas)']
    if not jugadores and bet.get('jugadores'):
        faltan.append('alineación probable (titularidad de cada jugador)')
    return {'local': meta['local'], 'visitante': meta['visitante'], 'liga': f"{meta['region']} {meta['liga']}",
            'fecha': ini.strftime('%Y-%m-%d %H:%M'), 'betano': bet, 'jugadores': jugadores, 'ficha': ficha,
            'estadio': (fs or {}).get('estadio') or '', 'cuotas_leidas': f"Cuotas de Betano leídas {meta['cuotas_leidas']} · {meta['n_mercados']} mercados"}


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    base = argv[0]
    claves = argv[1:] or [os.path.basename(p)[:-5] for p in sorted(glob.glob(os.path.join(base, 'betano', '*.json')))]
    os.makedirs(os.path.join(base, 'entradas'), exist_ok=True)
    cargar = lambda sub, k: json.load(open(os.path.join(base, sub, k + '.json'), encoding='utf8')) if os.path.exists(os.path.join(base, sub, k + '.json')) else None
    for k in claves:
        b = cargar('betano', k)
        if not b:
            print(f'{k}: sin betano/{k}.json'); continue
        fs = cargar('flashscore', k)
        al = cargar('alineaciones', k)
        if fs is not None and al is not None and not fs.get('lineups'):
            lu = lineups_de(al)
            if lu:
                fs['lineups'], fs['lineups_leidas'] = lu, f"{LECTURA_ALINEACIONES} · XI oficial se publica ~1 h antes del inicio"
            else:
                fs['avisos'] = list(fs.get('avisos', [])) + ['Flashscore no muestra pestaña de alineaciones para este partido: sin XI ni bajas con fuente']
        e = armar(b, fs, cargar('notas', k), cargar('jugadores', k))
        F = e['ficha']
        cl = _json(base, 'clima/clima.json').get(k)
        if clima_de(cl) and not F.get('clima'):
            F['clima'] = clima_de(cl)
            F['fuentes'] = F['fuentes'] + ['Open-Meteo (clima)']
        cs = _json(base, 'clasificacion/clasificacion.json')
        pc = (cs.get('partidos') or {}).get(k)
        if pc:
            F['fuentes'] = F['fuentes'] + ['Flashscore (clasificación)']
            tabla = {}
            for ref in pc.get('tablas', []):
                t = cs['tablas'][ref]
                for lado, nom in (('local', e['local']), ('visitante', e['visitante'])):
                    fl = fila_de(t, nom) or fila_de(t, (fs or {}).get(lado if lado == 'local' else 'visitante', ''))
                    if fl and lado not in tabla:
                        tabla[lado] = fl
            if tabla:
                F['tabla'] = tabla
            if not pc.get('tablas'):
                F['dudas'] = list(F.get('dudas') or []) + ['Sin tabla de clasificación en Flashscore (' + pc.get('nota', 'amistoso, copa o eliminatoria') + '): importancia por juzgar con el contexto de la competición']
            elif len(tabla) < 2:
                F['dudas'] = list(F.get('dudas') or []) + ['Clasificación: no se pudo casar el nombre de un equipo con la tabla de Flashscore']
        json.dump(e, open(os.path.join(base, 'entradas', k + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
        print(f"{k:34s} forma={len(e['ficha']['forma']['local'])}/{len(e['ficha']['forma']['visitante'])} h2h={len(e['ficha'].get('h2h', []))} faltan={len(e['ficha']['faltan'])}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
