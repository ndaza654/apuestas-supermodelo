# -*- coding: utf-8 -*-
"""Une lo recolectado de un partido en la ENTRADA que leen el modelo y las fichas.

Entradas:  betano/<clave>.json   (recoleccion/betano.py: {meta, betano})
           flashscore/<clave>.json (recoleccion/flashscore_extraer.js: contexto del partido)  [opcional]
           notas/<clave>.json    (lectura de la situación hecha por Claude: importancia, motivación, rotación… ver NOTAS_EJEMPLO)  [opcional]
Salida:    entradas/<clave>.json
Lo que falta se deja VACÍO y se declara en ficha.dudas / ficha.faltan; nunca se rellena con supuestos.

Uso:  python3 recoleccion/armar_entrada.py jornadas/2026-11-13 [clave ...]
"""
import json, os, sys, glob, datetime as dt

NOTAS_EJEMPLO = {'importancia': 'alta|normal|baja', 'derbi': False, 'eliminatoria': None,
                 'local': {'motivacion': 'normal|alta|baja', 'rotacion': False, 'necesita_ganar': False, 'estilo': []},
                 'visitante': {'motivacion': 'normal|alta|baja', 'rotacion': False, 'necesita_ganar': False, 'estilo': []},
                 'bajas': [], 'dudas': [], 'fuentes': []}


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


def h2h_de(directos):
    out = []
    for d in directos:
        fecha, g, st = (d['fecha'], d['g'], d.get('stats', {})) if isinstance(d, dict) else d[:3]
        if st:                                                    # solo los directos con alguna estadística sirven a la ficha
            out.append({'fecha': fecha, 'stats': {k: list(x) for k, x in st.items()} | {'g': list(g)}})
    return out


def armar(b, fs=None, notas=None):
    meta, bet = b['meta'], b['betano']
    notas = notas or {}
    ini = dt.datetime.fromisoformat(meta['inicio_utc'].replace('Z', '+00:00')) - dt.timedelta(hours=5)     # hora de Bogotá
    faltan, dudas = [], list(notas.get('dudas', []))
    ficha = {'derbi': notas.get('derbi', False), 'importancia': notas.get('importancia', 'normal'), 'eliminatoria': notas.get('eliminatoria'),
             'local': _equipo(notas.get('local')), 'visitante': _equipo(notas.get('visitante')),
             'bajas': notas.get('bajas', []), 'dudas': dudas, 'fuentes': notas.get('fuentes', []), 'jugadores_hist': notas.get('jugadores_hist', {})}
    if fs:
        ficha['forma'] = {'local': forma_de(fs['forma']['local']), 'visitante': forma_de(fs['forma']['visitante'])}
        ficha['h2h'] = h2h_de(fs.get('h2h', []))
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
    if not notas.get('jugadores_hist'):
        faltan.append('historial por jugador (remates, tiros al arco): sin él los mercados de jugadores no se pueden filtrar')
    ficha['faltan'] = faltan
    jugadores = notas.get('jugadores', [])
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
        e = armar(b, cargar('flashscore', k), cargar('notas', k))
        json.dump(e, open(os.path.join(base, 'entradas', k + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
        print(f"{k:34s} forma={len(e['ficha']['forma']['local'])}/{len(e['ficha']['forma']['visitante'])} h2h={len(e['ficha'].get('h2h', []))} faltan={len(e['ficha']['faltan'])}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
