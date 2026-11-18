# -*- coding: utf-8 -*-
"""Registro de TODAS las líneas analizadas de una jornada (la «base de datos» del proyecto).

Une, línea por línea, las dos lecturas que se comparan después con los resultados reales:
  · la FICHA (regularidad «X de 10», esperado, colchón, cumple) — fichas/ficha_<partido>.json
  · el MODELO SM-1.2 (p, p_mercado, p_simulacion, ev, alerta) — informes/<partido>_resultado.json
Salida: registro/lineas.csv (separador ';', UTF-8 con BOM: abre directo en Excel y Google Sheets). Una fila por línea de
Betano y lado (Más/Menos, Sí), cumpla o no. Las columnas de resultado quedan vacías; las llena el agente `calificacion`
al día siguiente (resultado real, apostada, cuota de cierre). Correr de nuevo la misma jornada reemplaza sus filas.

Uso:  python3 recoleccion/registrar_jornada.py jornadas/AAAA-MM-DD [registro/lineas.csv]
"""
import csv, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ficha as FI

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMPOS = ['jornada', 'partido', 'liga', 'hora_partido', 'cuotas_leidas', 'mercado', 'ambito', 'jugador', 'titular', 'linea', 'lado',
          'cuota', 'esperado', 'colchon', 'reg_local', 'reg_visitante', 'directos', 'cumple_ficha',
          'p_modelo', 'p_mercado', 'p_simulacion', 'ev_modelo', 'alerta_modelo', 'sistemas_partido',
          'apostada', 'stake', 'resultado', 'cuota_cierre', 'nota']
EQUIPO = ('corners', 'faltas', 'fueras', 'saques_banda', 'saques_meta', 'remates', 'al_arco', 'goles', 'tarjetas')


def _modelo(informe):
    """Índice de líneas del modelo por (mercado, ámbito, línea, lado) y (jugador, stat, k)."""
    idx = {}
    for l in (informe or {}).get('lineas', []):
        s = l.get('sel') or {}
        if s.get('mercado') == 'jugador':
            clave = ('jugador', s.get('jugador'), s.get('stat'), s.get('k'))
        else:
            clave = (s.get('mercado'), s.get('ambito'), s.get('linea'), s.get('lado'))
        idx[clave] = l
    return idx


def _p(l):
    if not l:
        return {}
    return {'p_modelo': l.get('p'), 'p_mercado': l.get('p_mercado'), 'p_simulacion': l.get('p_simulacion'),
            'ev_modelo': l.get('ev'), 'alerta_modelo': 'sí' if l.get('alerta') else ''}


def filas_de(ficha, informe, jornada):
    M = _modelo(informe)
    sis = ';'.join(s.get('id', '') for s in (informe or {}).get('sistemas', []))
    base = {'jornada': jornada, 'partido': ficha['encuentro'], 'liga': ficha.get('liga'), 'hora_partido': ficha.get('fecha'),
            'cuotas_leidas': (ficha.get('cuotas_leidas') or '').replace('Cuotas de Betano leídas ', '').split(' · ')[0], 'sistemas_partido': sis}
    out = []
    for m in EQUIPO:
        r = ficha.get('corners') if m == 'corners' else (ficha.get('partido', {}).get(m) or ficha.get(m))
        if not r:
            continue
        for l in r.get('lineas', []):
            for lado in ('mas', 'menos'):
                c = l.get(lado)
                if not c or c.get('cuota') is None:
                    continue
                f = {**base, 'mercado': m, 'ambito': l['ambito'], 'linea': l['linea'], 'lado': 'Más' if lado == 'mas' else 'Menos', 'cuota': c['cuota']}
                if 'colchon' in c:        # tiene estadística (partido completo)
                    d = c.get('directos')
                    f.update(esperado=l.get('esperado'), colchon=c['colchon'], reg_local=c['reg_local']['txt'], reg_visitante=c['reg_visitante']['txt'],
                             directos=d['txt'] if d else '', cumple_ficha='sí' if c['cumple'] else 'no')
                else:
                    f['nota'] = c.get('nota') or l.get('nota') or 'sin estadística por tiempo'
                f.update(_p(M.get((m, l['ambito'], l['linea'], lado))))
                out.append(f)
    # ambos marcan y resultado (desde el 18-nov-2026): una cuota por selección, sin línea ni colchón; lado = Sí/No o 1/X/2/1X/X2/12
    for m in ('ambos', 'resultado'):
        for r in (ficha.get('resultados') or {}).get(m, []):
            if r.get('cuota') is None:
                continue
            lado = {'si': 'Sí', 'no': 'No'}.get(r['seleccion'], r['seleccion'])
            f = {**base, 'mercado': m, 'ambito': 'total', 'linea': '', 'lado': lado, 'cuota': r['cuota']}
            if 'reg_local' in r:
                d = r.get('directos')
                f.update(reg_local=r['reg_local']['txt'], reg_visitante=r['reg_visitante']['txt'], directos=d['txt'] if d else '',
                         cumple_ficha='sí' if r['cumple'] else 'no')
            else:
                f['nota'] = r.get('nota') or 'sin muestra'
            f.update(_p(M.get((m, None, None, r['seleccion']))))
            out.append(f)
    for j in ficha.get('jugadores', []):
        filas = j.get('escalones') or [{'minimo': 1, 'cuota': j.get('cuota'), 'reg': j.get('reg'), 'colchon': None}]
        for s in filas:
            if s.get('cuota') is None:
                continue
            f = {**base, 'mercado': 'jugador:' + j['stat'], 'ambito': j.get('lado'), 'jugador': j['jugador'], 'titular': j.get('titular'),
                 'linea': s['minimo'], 'lado': 'Más' if j.get('escalones') else 'Sí', 'cuota': s['cuota'],
                 'esperado': j.get('esperado'), 'colchon': s.get('colchon'), 'reg_local': (s.get('reg') or {}).get('txt'),
                 'cumple_ficha': 'sí' if (s.get('reg') or {}).get('cumple') else ('no' if (s.get('reg') or {}).get('n', 0) >= FI.MIN_N else 'sin muestra')}
            if j.get('titular') is None:
                f['nota'] = 'sin alineación (regla 1: no se analiza)'
                f['cumple_ficha'] = 'sin alineación'
            f.update(_p(M.get(('jugador', j['jugador'], j['stat'], s['minimo']))))
            out.append(f)
    return out


def registrar(base, ruta=None):
    base = os.path.abspath(base)
    jornada = os.path.basename(base)
    ruta = ruta or os.path.join(RAIZ, 'registro', 'lineas.csv')
    nuevas = []
    for pf in sorted(glob.glob(os.path.join(base, 'fichas', 'ficha_*.json'))):
        k = os.path.basename(pf)[6:-5]
        ficha = json.load(open(pf, encoding='utf8'))
        pi = os.path.join(base, 'informes', k + '_resultado.json')
        informe = json.load(open(pi, encoding='utf8')) if os.path.exists(pi) else None
        nuevas += filas_de(ficha, informe, jornada)
    previas = []
    if os.path.exists(ruta):
        with open(ruta, encoding='utf-8-sig') as f:
            previas = [r for r in csv.DictReader(f, delimiter=';') if r.get('jornada') != jornada]
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, delimiter=';', extrasaction='ignore')
        w.writeheader()
        w.writerows(previas)
        w.writerows(nuevas)
    return len(nuevas), len(previas)


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    n, prev = registrar(argv[0], argv[1] if len(argv) > 1 else None)
    print(f'registro/lineas.csv: {n} líneas de {os.path.basename(argv[0].rstrip("/"))} (+{prev} de otras jornadas)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
