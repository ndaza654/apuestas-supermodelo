# -*- coding: utf-8 -*-
"""Registro y aprendizaje.

Cada línea analizada (se apueste o no) queda guardada con su probabilidad de mercado, sin contexto, de la simulación y
de decisión; el tipo de partido; el guion más probable; los hechos de la ficha; los sistemas de tipsters que el partido
cumple; las alertas; y la cuota en el momento del análisis (apertura). Al cerrar el partido, `cerrar()` califica TODAS
las líneas con las estadísticas reales (no hace falta poner 1/0 a mano), anota la cuota de cierre y el CLV, y agrega el
partido a datos/partidos.csv (la base propia de cada liga: Colombia, Ecuador... que no están en las fuentes públicas).

Con eso se mide:
  · si el contexto ayuda (¿la probabilidad con contexto calibra mejor que la sin contexto?) y qué hechos ayudan,
  · qué mercados funcionan en qué tipo de partido,
  · el CLV: si la cuota tomada fue mejor que la de cierre (la señal más rápida de ventaja), y si el mercado se movió
    hacia donde decía el modelo,
  · los sistemas de tipsters con tus cuotas de Betano.
Formato: CSV con separador ';' (abre directo en Excel y Google Sheets). Lee también registros viejos (columnas que
faltan quedan vacías)."""
import csv, os, math, json, datetime as dt
from collections import defaultdict
import numpy as np

CAMPOS = ['fecha', 'hora_analisis', 'partido', 'liga', 'tipo', 'guion_principal', 'familia', 'submercado', 'seleccion',
          'cuota', 'p_mercado', 'p_sin_contexto', 'p_simulacion', 'p', 'movimiento_contexto', 'ev', 'robustez', 'etiqueta',
          'alerta', 'hechos_contexto', 'sistemas', 'tipo_apuesta', 'apostada', 'stake', 'resultado', 'cuota_cierre',
          'cuota_referencia', 'clv', 'sel']
CAMPOS_PARTIDO = ['fecha', 'liga', 'liga_clave', 'local', 'visitante', 'goles_local', 'goles_visitante', 'goles_1t_local', 'goles_1t_visitante',
                  'corners_local', 'corners_visitante', 'corners_1t_local', 'corners_1t_visitante', 'tarjetas_local',
                  'tarjetas_visitante', 'tarjetas_1t_local', 'tarjetas_1t_visitante', 'remates_local', 'remates_visitante',
                  'al_arco_local', 'al_arco_visitante', 'faltas_local', 'faltas_visitante', 'fueras_local', 'fueras_visitante',
                  'xg_local', 'xg_visitante', 'al_arco_1t_local', 'al_arco_1t_visitante', 'xg_1t_local', 'xg_1t_visitante']


def _escribir(ruta, filas, campos):
    """Agrega filas al CSV. Si el archivo ya existe con otro encabezado (registro viejo), lo reescribe con la unión de
    columnas para que nada se corra de lugar."""
    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        with open(ruta, encoding='utf-8-sig') as f:
            lector = csv.DictReader(f, delimiter=';')
            viejo = list(lector.fieldnames or [])
            if viejo != list(campos):
                previas = list(lector)
                union = list(dict.fromkeys(list(campos) + viejo))
                with open(ruta, 'w', newline='', encoding='utf-8-sig') as g:
                    w = csv.DictWriter(g, fieldnames=union, delimiter=';', extrasaction='ignore')
                    w.writeheader(); w.writerows(previas); w.writerows(filas)
                return
        campos_uso = viejo
    else:
        campos_uso = list(campos)
    nuevo = not os.path.exists(ruta) or os.path.getsize(ruta) == 0
    with open(ruta, 'a', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos_uso, delimiter=';', extrasaction='ignore')
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def _sin_tildes(t):
    import unicodedata
    return ' '.join(unicodedata.normalize('NFKD', str(t)).encode('ascii', 'ignore').decode().lower().replace(',', '.').split())


def guardar(A, ruta, apostadas=(), stakes=None, ficha=None, entrada=None, tipo_apuesta='simple'):
    """Agrega todas las líneas del análisis al CSV. `apostadas`: nombres de selección que jugaste."""
    ap_norm = {_sin_tildes(x): x for x in (apostadas or []) if str(x).strip()}
    nombres = {_sin_tildes(r['seleccion']) for r in A['lineas']}
    no_encontradas = [v for k, v in ap_norm.items() if k not in nombres]
    apostadas = {r['seleccion'] for r in A['lineas'] if _sin_tildes(r['seleccion']) in ap_norm}
    hechos = ','.join(_hechos(ficha or {}) + _etiquetas_precio(entrada, ficha)) if (ficha or entrada) else ''
    sist = ','.join(s['id'] for s in A.get('sistemas') or [])
    guion = max(A['guiones'], key=A['guiones'].get)
    hora = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
    filas = []
    for r in A['lineas']:
        filas.append(dict(fecha=A.get('fecha'), hora_analisis=hora, partido=A['partido'], liga=A.get('liga'), tipo=A['tipo'],
                          guion_principal=guion, familia=r['familia'], submercado=r.get('submercado', r['familia']),
                          seleccion=r['seleccion'], cuota=r['cuota'], p_mercado=r['p_mercado'], p_sin_contexto=r['p_sin_contexto'],
                          p_simulacion=r.get('p_simulacion'), p=r['p'], movimiento_contexto=r['movimiento_contexto'], ev=r.get('ev'),
                          robustez=r['robustez'], etiqueta=r['etiqueta'], alerta=r.get('alerta') or '', hechos_contexto=hechos,
                          sistemas=sist, tipo_apuesta=tipo_apuesta if r['seleccion'] in apostadas else '',
                          apostada='Sí' if r['seleccion'] in apostadas else 'No', stake=(stakes or {}).get(r['seleccion'], ''),
                          resultado='', cuota_cierre='', cuota_referencia='', clv='',
                          sel=json.dumps(r['sel'], ensure_ascii=False)))
    _escribir(ruta, filas, CAMPOS)
    return no_encontradas


def guardar_combo(ruta, A, combo, apostado=True, stake='', tipo_apuesta='combo', sels=None):
    """Un boleto combinado (salida de combos.evaluar) como una fila propia: familia 'combo', p = probabilidad ajustada."""
    guion = max(A['guiones'], key=A['guiones'].get)
    _escribir(ruta, [dict(fecha=A.get('fecha'), hora_analisis=dt.datetime.now().strftime('%Y-%m-%d %H:%M'), partido=A['partido'],
                          liga=A.get('liga'), tipo=A['tipo'], guion_principal=guion, familia='combo',
                          submercado=f"combo {len(combo['patas'])} patas", seleccion=' + '.join(combo['patas']),
                          cuota=combo.get('cuota'), p_mercado='', p_sin_contexto='', p_simulacion=combo.get('p_sim'),
                          p=combo.get('p_ajust'), movimiento_contexto='', ev=combo.get('ev_ajust'), robustez=combo.get('robustez'),
                          etiqueta=combo.get('estado', ''), alerta=' · '.join(combo.get('avisos') or []), hechos_contexto='',
                          sistemas='', tipo_apuesta=tipo_apuesta, apostada='Sí' if apostado else 'No', stake=stake,
                          resultado='', cuota_cierre='', cuota_referencia='', clv='',
                          sel=json.dumps(sels if sels is not None else [x['sel'] for x in A['lineas'] if x['seleccion'] in combo['patas']],
                                         ensure_ascii=False))], CAMPOS)


def _etiquetas_precio(entrada, ficha=None):
    """Etiquetas de precio y de perfil para MEDIR (no para decidir)."""
    out = []
    bet = (entrada or {}).get('betano') or {}
    for u in bet.get('unicos', []):
        if u.get('mercado') == 'resultado':
            o = u.get('opciones', {})
            if o.get('1') and o['1'] <= 1.50: out.append('precio:local<=1.50')
            elif o.get('2') and o['2'] <= 1.50: out.append('precio:visitante<=1.50')
            if o.get('X') and o['X'] >= 3.60: out.append('precio:empate>=3.60')
    for l in bet.get('lineas', []):
        if l.get('mercado') == 'goles' and l.get('ambito') == 'total' and l.get('linea') == 2.5 and l.get('mas') and l['mas'] <= 1.45:
            out.append('precio:O2.5<=1.45')
        if l.get('mercado') == 'goles' and l.get('ambito') == '1T' and l.get('linea') == 1.5 and l.get('mas') and l['mas'] <= 2.15:
            out.append('precio:1T_O1.5<=2.15')
    f = ficha or {}
    for j in f.get('jugadores') or []:
        if j.get('popular'): out.append('jugador_popular:' + str(j.get('nombre', '')))
    for lado in ('local', 'visitante'):
        e = f.get(lado) or {}
        pc = e.get('perfil_corners') or {}
        if pc.get('centros_pj') and pc['centros_pj'] >= 20: out.append(f'{lado}:centros>=20')
        if pc.get('territorio_pct') and pc['territorio_pct'] >= 55: out.append(f'{lado}:territorio>=55')
        if e.get('propositivo'): out.append(f'{lado}:propositivo')
    return out


def _hechos(ficha):
    out = []
    if ficha.get('derbi'): out.append('derbi')
    if ficha.get('importancia', 'normal') != 'normal': out.append('importancia_' + str(ficha['importancia']))
    if (ficha.get('arbitro') or {}).get('tarjetas_por_partido') or (ficha.get('arbitro') or {}).get('amarillas_por_partido'): out.append('arbitro')
    cl = ficha.get('clima') or {}
    if cl.get('lluvia'): out.append('lluvia')
    if cl.get('viento_fuerte'): out.append('viento')
    if cl.get('temperatura') is not None and cl['temperatura'] >= 30: out.append('calor>=30')
    if ficha.get('eliminatoria'): out.append('eliminatoria')
    if ficha.get('fecha_fifa'): out.append('fecha_fifa')
    if ficha.get('ultimo_tabla'): out.append(f"ultimo_tabla:{ficha['ultimo_tabla']}")
    if ficha.get('info_tardia'): out.append('info_tardia')
    if ficha.get('bajas'): out.append('bajas_detalle')
    cp = ficha.get('consenso_publico') or {}
    if cp.get('lado') and (cp.get('pct') or 0) >= 70: out.append(f"consenso_publico:{cp['lado']}")
    for lado in ('local', 'visitante'):
        e = ficha.get(lado) or {}
        out += [f'{lado}:{x}' for x in (e.get('estilo') or [])]
        for k in ('marcador', 'motivacion'):
            if e.get(k) and e[k] != 'normal': out.append(f'{lado}:{e[k]}')
        for k in ('bajas_ataque', 'bajas_defensa'):
            if e.get(k): out.append(f'{lado}:{k}')
        for k in ('rotacion', 'necesita_ganar', 'viaje_largo', 'fecha_fifa'):
            if e.get(k): out.append(f'{lado}:{k}')
        if e.get('dias_descanso') is not None and e['dias_descanso'] <= 3: out.append(f'{lado}:descanso<=3')
        xg = e.get('xg_menos_goles')   # xG − goles recientes: >0 = merece más de lo que marca (regresión)
        if xg is not None and abs(xg) >= 0.3: out.append(f"{lado}:{'infra' if xg > 0 else 'sobre'}_rinde_xg")
    for t in ficha.get('frescos') or []:
        out.append('fresco:' + t)
    return out


# ------------------------------------------------------------------ cierre automático
def _sim_real(real):
    """Convierte las estadísticas reales del partido al formato del simulador (arrays de largo 1)."""
    a = lambda v: np.array([int(v)])
    g2 = lambda k: (real.get(k) or [0, 0])
    R = [{}, {}]
    for l in (0, 1):
        R[l]['g'] = a(g2('goles')[l]); R[l]['g1'] = a(g2('goles_1t')[l])
        R[l]['c'] = a(g2('corners')[l]); R[l]['c1'] = a(g2('corners_1t')[l])
        # Convención (la misma en vivo): 'amarillas' = amarillas mostradas, incluida la 2.ª de una expulsión; 'rojas' = todas;
        # 'rojas_directas' = las directas. Si no viene 'rojas_directas', se suponen directas todas las rojas. Puntos de Betano:
        # amarillas + rojas + directas (doble amarilla 1+1+1 = 3; roja directa 2). Lo más seguro: dar 'tarjetas_betano'.
        am, ro = g2('amarillas')[l], g2('rojas')[l]
        rd = (real.get('rojas_directas') or real.get('rojas') or [0, 0])[l]
        tarj = real.get('tarjetas_betano')
        R[l]['tarjetas'] = a(tarj[l]) if tarj else a(am + ro + rd)
        t1 = real.get('tarjetas_betano_1t')
        r1 = (real.get('rojas_1t') or [0, 0])[l]
        rd1 = (real.get('rojas_directas_1t') or real.get('rojas_1t') or [0, 0])[l]
        R[l]['tarj1'] = a(t1[l]) if t1 else a((real.get('amarillas_1t') or [0, 0])[l] + r1 + rd1)
        R[l]['y'] = a(am); R[l]['r'] = a(ro)
        R[l]['sh'] = a(g2('remates')[l]); R[l]['sh1'] = a(g2('remates_1t')[l])
        R[l]['sot'] = a(g2('al_arco')[l]); R[l]['sot1'] = a(g2('al_arco_1t')[l])
        R[l]['f'] = a(g2('faltas')[l]); R[l]['f1'] = a(g2('faltas_1t')[l])
        R[l]['off'] = a(g2('fueras')[l]); R[l]['gk'] = a(g2('saques_meta')[l]); R[l]['ti'] = a(g2('saques_banda')[l])
        R[l]['tk'] = a(g2('entradas')[l])
    for l in (0, 1):
        R[l]['sv'] = a((real.get('atajadas') or [None, None])[l]) if (real.get('atajadas') or [None, None])[l] is not None else R[1 - l]['sot'] - R[1 - l]['g']
    sim = {0: R[0], 1: R[1], 'lados': R}
    jug = {}
    for nm, st in (real.get('jugadores') or {}).items():
        jug[nm] = {k: np.array([int(v)]) for k, v in st.items()}
    return sim, jug


def _hay_dato(real, sel):
    from . import mercados as MS
    m = sel.get('mercado')
    clave = {'goles': 'goles', 'corners': 'corners', 'tarjetas': 'amarillas', 'faltas': 'faltas', 'remates': 'remates',
             'al_arco': 'al_arco', 'fueras': 'fueras', 'saques_meta': 'saques_meta', 'saques_banda': 'saques_banda',
             'ambos': 'goles', 'resultado': 'goles', 'handicap': 'goles', 'atajadas': 'al_arco', 'ambos_n_tarjetas': 'amarillas'}.get(m)
    if m == 'mas_que':
        clave = {'corners': 'corners', 'tarjetas': 'amarillas'}.get(sel.get('stat'))
    if m == 'jugador':
        return sel.get('jugador') in (real.get('jugadores') or {}) and sel.get('stat') in real['jugadores'][sel['jugador']]
    if m == 'tarjetas' and real.get('tarjetas_betano'):
        return True
    if sel.get('ambito') in ('1T', '2T') and m in ('goles', 'corners', 'tarjetas', 'remates', 'al_arco', 'faltas'):
        c1 = {'goles': 'goles_1t', 'corners': 'corners_1t', 'tarjetas': 'amarillas_1t', 'remates': 'remates_1t',
              'al_arco': 'al_arco_1t', 'faltas': 'faltas_1t'}[m]
        if m == 'tarjetas' and real.get('tarjetas_betano_1t'):
            return True
        return real.get(c1) is not None and real.get(clave) is not None
    return clave is not None and real.get(clave) is not None


def cerrar(ruta, partido, real, cierres=None, referencia=None, ruta_partidos=None, liga=None, fecha=None, local=None, visitante=None):
    """Califica las líneas abiertas de `partido` con las estadísticas reales y anota cuota de cierre y CLV.
    real: {"goles": [2, 0], "goles_1t": [1, 0], "corners": [6, 3], "corners_1t": [3, 1], "amarillas": [2, 3], "rojas": [0, 0],
           "rojas_directas": [0, 0], "amarillas_1t": [1, 1], "remates": [14, 8], "al_arco": [6, 2], "faltas": [10, 14],
           "fueras": [2, 1], "xg": [1.8, 0.6], "jugadores": {"Nombre": {"remates": 3, "al_arco": 1, "anota": 1}}}
    cierres / referencia: {seleccion: cuota} de Betano a la hora del partido / de una casa afilada (Pinnacle) si se tiene.
    Devuelve (calificadas, sin_dato)."""
    from . import mercados as MS
    from .mercados import evento
    if not os.path.exists(ruta):
        return 0, 0
    with open(ruta, encoding='utf-8-sig') as f:
        filas = list(csv.DictReader(f, delimiter=';'))
    campos = list(dict.fromkeys(CAMPOS + (list(filas[0].keys()) if filas else [])))
    sim, jug = _sim_real(real)
    n_ok = n_sin = 0
    meta = None
    for r in filas:
        if r.get('partido') != partido:
            continue
        meta = meta or r
        try:
            sel = json.loads(r['sel']) if r.get('sel') else _sel_desde_nombre(r)
        except ValueError:
            sel = _sel_desde_nombre(r)
        if cierres and r['seleccion'] in cierres:
            r['cuota_cierre'] = cierres[r['seleccion']]
        if referencia and r['seleccion'] in referencia:
            r['cuota_referencia'] = referencia[r['seleccion']]
        if r.get('cuota_cierre') and r.get('cuota'):
            try:
                r['clv'] = round(float(r['cuota']) / float(r['cuota_cierre']) - 1, 4)
            except (ValueError, ZeroDivisionError):
                pass
        if r.get('resultado') not in (None, ''):
            continue
        if isinstance(sel, list):          # combo: gana si ganan todas las patas
            if not sel or not all(s and _hay_dato(real, s) for s in sel):
                n_sin += 1
                continue
            try:
                y = all(bool(evento(sim, s, jug)[0]) for s in sel)
            except Exception:
                n_sin += 1
                continue
            r['resultado'] = '1' if y else '0'
            n_ok += 1
            continue
        if sel is None or not _hay_dato(real, sel):
            n_sin += 1
            continue
        try:
            if MS.es_asiatica(sel):        # entera / de cuarto / hándicap asiático: devolución y medias
                partes = [(w, bool(g[0]), bool(dv[0])) for w, g, dv in MS.partes_asiaticas(sim, sel)]
                res = sum(w * (1 if g else (0 if dv else -1)) for w, g, dv in partes)
                r['resultado'] = {1: '1', -1: '0', 0: 'Nula', 0.5: 'Media ganada', -0.5: 'Media perdida'}[round(res * 2) / 2]
                n_ok += 1
                continue
            y = bool(evento(sim, sel, jug)[0])
        except Exception:
            n_sin += 1
            continue
        r['resultado'] = '1' if y else '0'
        n_ok += 1
    with open(ruta, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=';', extrasaction='ignore')
        w.writeheader()
        w.writerows(filas)
    if meta is None:
        print(f'Aviso: no encontré «{partido}» en {ruta} (el nombre debe ser exactamente el del registro, p. ej. "Local - Visitante").')
    # base propia de partidos
    if meta is not None or (local and visitante):
        lo, vi = (local, visitante) if local else (meta['partido'].split(' - ', 1) + [''])[:2]
        # Por defecto la base propia va a datos/partidos.csv del paquete: es la que lee ligas.prior() para mezclar con el prior.
        from . import ligas
        rp = ruta_partidos or ligas.RUTA_PROPIA
        g = lambda k, l: (real.get(k) or [None, None])[l]
        tb = real.get('tarjetas_betano')
        from . import ligas as _lg
        lg = liga or (meta or {}).get('liga')
        fila = dict(fecha=fecha or (meta or {}).get('fecha'), liga=lg, liga_clave=_lg.clave(lg), local=lo, visitante=vi)
        for k in ('goles', 'goles_1t', 'corners', 'corners_1t', 'remates', 'al_arco', 'faltas', 'fueras', 'xg', 'al_arco_1t', 'xg_1t'):
            fila[f'{k}_local'], fila[f'{k}_visitante'] = g(k, 0), g(k, 1)
        for l, lado in ((0, 'local'), (1, 'visitante')):
            fila[f'tarjetas_{lado}'] = int(sim[l]['tarjetas'][0]) if (tb or real.get('amarillas') is not None) else None
            fila[f'tarjetas_1t_{lado}'] = int(sim[l]['tarj1'][0]) if (real.get('tarjetas_betano_1t') or real.get('amarillas_1t') is not None) else None
        ya = False
        if os.path.exists(rp):
            for x in csv.DictReader(open(rp, encoding='utf-8-sig'), delimiter=';'):
                if (x.get('fecha'), x.get('local'), x.get('visitante')) == (str(fila['fecha']), lo, vi):
                    ya = True
                    break
        if not ya:
            _escribir(rp, [fila], CAMPOS_PARTIDO)
    return n_ok, n_sin


def _sel_desde_nombre(r):
    """Reconstruye la selección desde el nombre guardado (el registro guarda el nombre legible)."""
    import re
    nm = r['seleccion']
    if r.get('familia') == 'combo' or ' + ' in nm:
        return None
    loc, vis = (r['partido'].split(' - ', 1) + [''])[:2]
    t = nm
    m = re.match(r'^(Goles|Córners|Tarjetas|Faltas|Remates|Tiros al arco|Fueras de lugar|Saques de meta|Saques de banda|Atajadas)(.*) (Más|Menos) ([\d.]+)$', t)
    if m:
        merc = {'Goles': 'goles', 'Córners': 'corners', 'Tarjetas': 'tarjetas', 'Faltas': 'faltas', 'Remates': 'remates',
                'Tiros al arco': 'al_arco', 'Fueras de lugar': 'fueras', 'Saques de meta': 'saques_meta',
                'Saques de banda': 'saques_banda', 'Atajadas': 'atajadas'}[m.group(1)]
        amb = m.group(2).strip()
        ambito = {'': 'total', '1.er tiempo': '1T', '2.º tiempo': '2T', loc: 'local', vis: 'visitante'}.get(amb, 'total')
        return dict(mercado=merc, ambito=ambito, lado='mas' if m.group(3) == 'Más' else 'menos', linea=float(m.group(4)))
    if t.startswith('Ambos marcan: '):
        return dict(mercado='ambos', lado='si' if t.endswith('Sí') else 'no')
    res = {f'Gana {loc}': '1', 'Empate': 'X', f'Gana {vis}': '2', f'{loc} o empate': '1X', f'{vis} o empate': 'X2', 'No hay empate': '12'}
    if t in res:
        return dict(mercado='resultado', lado=res[t])
    m = re.match(r'^Hándicap (.*) ([+-][\d.]+)$', t)
    if m:
        return dict(mercado='handicap', lado='local' if m.group(1) == loc else 'visitante', h=float(m.group(2)))
    m = re.match(r'^Más (corners|tarjetas): (.*)$', t)
    if m:
        quien = {loc: 'local', vis: 'visitante', 'empate': 'empate'}.get(m.group(2))
        return dict(mercado='mas_que', stat=m.group(1), lado=quien) if quien else None
    m = re.match(r'^Ambos (\d)\+ tarjetas: (Sí|No)$', t)
    if m:
        return dict(mercado='ambos_n_tarjetas', n=int(m.group(1)), lado='si' if m.group(2) == 'Sí' else 'no')
    m = re.match(r'^(.*) (remates|tiros al arco|faltas cometidas|entradas|atajadas) (\d+)\+$', t)
    if m:
        st = {'remates': 'remates', 'tiros al arco': 'al_arco', 'faltas cometidas': 'faltas', 'entradas': 'entradas', 'atajadas': 'atajadas'}[m.group(2)]
        return dict(mercado='jugador', jugador=m.group(1), stat=st, k=int(m.group(3)))
    m = re.match(r'^(.*) (anota o asiste|anota|recibe tarjeta)$', t)
    if m:
        st = {'anota o asiste': 'anota_o_asiste', 'anota': 'anota', 'recibe tarjeta': 'tarjeta'}[m.group(2)]
        return dict(mercado='jugador', jugador=m.group(1), stat=st, k=1)
    return None


# ------------------------------------------------------------------ lectura e informe
def _leer(ruta, solo_cerradas=True):
    with open(ruta, encoding='utf-8-sig') as f:
        filas = list(csv.DictReader(f, delimiter=';'))
    out = []
    for r in filas:
        if solo_cerradas and r.get('resultado') not in ('1', '0', 'Ganó', 'Perdió'):
            continue
        y = 1 if r.get('resultado') in ('1', 'Ganó') else 0
        g = lambda k: float(r[k]) if r.get(k) not in (None, '', 'None') else None
        out.append(dict(r, y=y, pm=g('p_mercado'), p0=g('p_sin_contexto'), p1=g('p'), mov=g('movimiento_contexto'),
                        cuota_f=g('cuota'), cierre=g('cuota_cierre'), stake_f=g('stake')))
    return out


def informe(ruta, min_n=10):
    """Calibración (Brier) de mercado, sin contexto y con contexto, por grupo; CLV; sistemas; alertas.
    "Acierto real" contra "Prob. media" dice si el modelo es optimista o pesimista en ese grupo; Brier más bajo = mejor."""
    F = [x for x in _leer(ruta) if x.get('familia') != 'combo']
    if not F:
        return 'Sin líneas cerradas todavía.'
    def brier(k, X):
        X = [x for x in X if x[k] is not None]
        return (sum((x[k] - x['y']) ** 2 for x in X) / len(X), len(X)) if X else (None, 0)
    def bloque(nombre, clave):
        g = defaultdict(list)
        for x in F:
            for k in (clave(x) if callable(clave) else [x.get(clave)]):
                if k:
                    g[k].append(x)
        lin = [f'\n### {nombre}', '| Grupo | n | Acierto real | Prob. media | Brier mercado | Brier sin contexto | Brier con contexto | ¿Contexto ayuda? |',
               '|---|---|---|---|---|---|---|---|']
        filas_ok = [(k, X) for k, X in sorted(g.items(), key=lambda z: -len(z[1])) if len(X) >= min_n]
        if not filas_ok:
            return ''
        for k, X in filas_ok:
            bm, _ = brier('pm', X); b0, _ = brier('p0', X); b1, _ = brier('p1', X)
            ayuda = '—' if b0 is None or b1 is None else ('Sí' if b1 < b0 - 0.002 else ('No' if b1 > b0 + 0.002 else 'Igual'))
            f = lambda b: '—' if b is None else f'{b:.4f}'
            lin.append(f"| {k} | {len(X)} | {sum(x['y'] for x in X) / len(X):.0%} | {sum(x['p1'] for x in X) / len(X):.0%} | "
                       f"{f(bm)} | {f(b0)} | {f(b1)} | {ayuda} |")
        return '\n'.join(lin)
    movidas = [x for x in F if x['mov'] is not None and abs(x['mov']) >= 0.03]
    sub = lambda x: x.get('submercado') or x['familia']
    out = [f'# Registro: {len(F)} líneas cerradas', bloque('Por familia de mercado', 'familia'),
           bloque('Por mercado fino (mercado, ámbito, dirección)', lambda x: [sub(x)]),
           bloque('Por tipo de partido', 'tipo'), bloque('Por guion más probable', 'guion_principal'),
           bloque('Qué mercado va bien en qué tipo de partido (mercado fino × tipo)', lambda x: [f"{sub(x)} · {x['tipo']}"]),
           bloque('Qué mercado va bien en qué tipo de partido (familia × fuerza del favorito)',
                  lambda x: [f"{x['familia']} · {x['tipo'].split(' · ')[0]}"]),
           bloque('Por liga', 'liga'),
           bloque('Por hecho de contexto (solo líneas que el contexto movió ≥3 pts)',
                  lambda x: (x.get('hechos_contexto') or 'sin hechos').split(',') if x in movidas else []),
           bloque('Por sistema de tipster que el partido cumple (todas las líneas del partido)',
                  lambda x: [s for s in (x.get('sistemas') or '').split(',') if s]),
           bloque('Líneas con alerta (el modelo se alejó mucho del mercado)', lambda x: ['con alerta'] if x.get('alerta') else [])]
    # CLV: ¿el mercado se movió hacia el modelo?
    C = [x for x in F if x['cierre'] and x['cuota_f'] and x['pm'] is not None]
    if len(C) >= min_n:
        mov_mod = [x['p1'] - x['pm'] for x in C]
        mov_mkt = [1 / x['cierre'] - 1 / x['cuota_f'] for x in C]
        n = len(C)
        mx, my = sum(mov_mod) / n, sum(mov_mkt) / n
        sx = math.sqrt(sum((a - mx) ** 2 for a in mov_mod) / n) or 1e-9
        sy = math.sqrt(sum((b - my) ** 2 for b in mov_mkt) / n) or 1e-9
        r = sum((a - mx) * (b - my) for a, b in zip(mov_mod, mov_mkt)) / n / sx / sy
        val = [x for x in C if x['p1'] * x['cuota_f'] - 1 >= 0.03]
        clv_val = sum(x['cuota_f'] / x['cierre'] - 1 for x in val) / len(val) if val else None
        out.append(f"\n### CLV de todas las líneas con cuota de cierre ({n})\n- Correlación entre lo que el modelo veía distinto del "
                   f"mercado y cómo se movió la cuota: {r:+.2f} (positiva = el mercado fue hacia el modelo: señal de ventaja).\n"
                   + (f"- CLV medio de las líneas que el modelo marcaba con valor ({len(val)}): {clv_val:+.1%}." if val else ''))
    ap = [x for x in _leer(ruta) if x.get('apostada') == 'Sí']
    if ap:
        pl = sum((x['cuota_f'] - 1) * (x['stake_f'] or 1) if x['y'] else -(x['stake_f'] or 1) for x in ap)
        st = sum(x['stake_f'] or 1 for x in ap)
        clv = [x['cuota_f'] / x['cierre'] - 1 for x in ap if x['cierre']]
        out.append(f"\n### Apostadas: {len(ap)} · acierto {sum(x['y'] for x in ap) / len(ap):.0%} · resultado {pl:+.1f} (stake total {st:.1f}, "
                   f"ROI {pl / st:+.1%})" + (f" · CLV medio {sum(clv) / len(clv):+.1%} ({len(clv)} con cuota de cierre)" if clv else ''))
    return "\n".join(x for x in out if x)
