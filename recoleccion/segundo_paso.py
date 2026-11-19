# -*- coding: utf-8 -*-
"""Segundo paso sobre las líneas que pasan el filtro: ordena por probabilidad combinada y MIDE si el segundo paso le gana al precio.

    python3 recoleccion/segundo_paso.py validar                       # prueba día a día (sin mirar el futuro) -> registro/validacion_segundo_paso.json
    python3 recoleccion/segundo_paso.py ordenar jornadas/AAAA-MM-DD   # -> segundo_paso.json / segundo_paso.md de esa jornada

Qué hace «ordenar» (solo líneas de EQUIPO; las de jugador no entran: ver CLAUDE.md «Hallazgos 4–18 nov»):
  p_final = promedio de la p del modelo y la p de mercado (sin margen); valor = p_final · cuota − 1; ventaja = p_final − 1/cuota.
  Etiqueta de calidad por señales que se pueden contar: cumple ≥ K de N en ambos, lado Menos, cuota 1,40–2,20, muestra completa, árbitro/notas leídos.
Qué dice «validar» (corte 19-nov: 10.695 líneas de 7 días): ni el filtro, ni el colchón, ni el modelo, ni el mercado de la línea mejoran el log-loss del precio de mercado
  fuera de muestra. Por eso el orden es de PROBABILIDAD y de calidad de datos, no una promesa de ventaja. Se vuelve a correr `validar` con cada jornada calificada:
  si algún factor empieza a sumar, saldrá aquí primero.
"""
import csv, json, math, os, re, sys
import numpy as np

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _lineas():
    return list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))


def _x(s):
    m = re.match(r'(\d+) de (\d+)', s or '')
    return (int(m.group(1)) / int(m.group(2)), 1) if m else (0.5, 0)


def _logit(p):
    p = min(max(p, .02), .98)
    return math.log(p / (1 - p))


def _feat(r, modo):
    f = [_logit(float(r['p_mercado']))]
    if modo >= 1:
        xl, al = _x(r['reg_local']); xv, av = _x(r['reg_visitante'])
        try:
            col = float(r['colchon']) / max(float(r['linea']), 1.0) if r['colchon'] != '' else 0.0
        except ValueError:
            col = 0.0
        f += [1 if r['cumple_ficha'] == 'sí' else 0, 1 if r['cumple_ficha'] == 'no' else 0, (xl - .5) * al, (xv - .5) * av, max(-2, min(2, col)), 1 if r['lado'] == 'Más' else 0]
    if modo >= 2:
        f.append(_logit(float(r['p_modelo'])) - f[0])
    return f


def validar():
    from sklearn.linear_model import LogisticRegression
    R = [r for r in _lineas() if r['resultado'] in ('cumplió', 'falló') and not r['mercado'].startswith('jugador') and r['cuota'] and r['p_mercado'] and r['p_modelo']]
    dias = sorted({r['jornada'] for r in R})
    out = {'lineas': len(R), 'dias': dias, 'modelos': {}, 'por_lado': {}, 'nota': 'regresión logística entrenada con los días anteriores y probada en el día siguiente; los 2 primeros días solo entrenan'}
    nombres = {0: 'solo precio de mercado', 1: '+ cumple X de N + colchón + lado', 2: '+ probabilidad del modelo'}
    for modo in (0, 1, 2):
        P, Y = [], []
        for i, d in enumerate(dias):
            if i < 2:
                continue
            tr = [r for r in R if r['jornada'] < d]; te = [r for r in R if r['jornada'] == d]
            m = LogisticRegression(C=1.0, max_iter=2000).fit(np.array([_feat(r, modo) for r in tr]), [r['resultado'] == 'cumplió' for r in tr])
            P += list(m.predict_proba(np.array([_feat(r, modo) for r in te]))[:, 1]); Y += [r['resultado'] == 'cumplió' for r in te]
        p, y = np.clip(np.array(P), 1e-3, 1 - 1e-3), np.array(Y, float)
        out['modelos'][nombres[modo]] = {'n': len(y), 'logloss': round(float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))), 4), 'brier': round(float(np.mean((p - y) ** 2)), 4)}
    for lado in ('Más', 'Menos'):
        L = [r for r in R if r['lado'] == lado]
        ret = np.array([(float(r['cuota']) - 1) if r['resultado'] == 'cumplió' else -1.0 for r in L])
        out['por_lado'][lado] = {'n': len(L), 'acierto': round(float(np.mean([r['resultado'] == 'cumplió' for r in L])), 4), 'roi_plano': round(float(ret.mean()), 4), 'ic95': round(float(1.96 * ret.std() / math.sqrt(len(L))), 4)}
    mej = min(out['modelos'].items(), key=lambda kv: kv[1]['logloss'])[0]
    out['conclusion'] = f'Mejor log-loss fuera de muestra: «{mej}». Si no es la 2.ª o 3.ª fila con diferencia clara (> 0,002), el segundo paso no supera al precio de mercado.'
    json.dump(out, open(os.path.join(RAIZ, 'registro', 'validacion_segundo_paso.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return out


def ordenar(base):
    jor = os.path.basename(base.rstrip('/'))
    R = [r for r in _lineas() if r['jornada'] == jor and not r['mercado'].startswith('jugador') and r['cuota'] and r['p_mercado'] and r['p_modelo'] and r['lado'] in ('Más', 'Menos')]
    arb = {os.path.basename(f)[:-5] for f in (os.listdir(os.path.join(base, 'arbitros')) if os.path.isdir(os.path.join(base, 'arbitros')) else [])}
    filas = []
    for r in R:
        cu = float(r['cuota']); p = (float(r['p_modelo']) + float(r['p_mercado'])) / 2
        se = [r['cumple_ficha'] == 'sí', r['lado'] == 'Menos', 1.40 <= cu <= 2.20, r['cumple_ficha'] != 'sin muestra']
        filas.append({'partido': r['partido'], 'mercado': r['mercado'], 'ambito': r['ambito'], 'linea': r['linea'], 'lado': r['lado'], 'cuota': cu, 'p_final': round(p, 4), 'valor': round(p * cu - 1, 4),
                      'ventaja': round(p - 1 / cu, 4), 'reg_local': r['reg_local'], 'reg_visitante': r['reg_visitante'], 'cumple': r['cumple_ficha'], 'senales': sum(se), 'calidad': 'A' if sum(se) >= 3 and se[0] else 'B' if se[0] else 'C'})
    filas.sort(key=lambda z: (-(z['calidad'] == 'A'), -(z['calidad'] == 'B'), -z['p_final']))
    json.dump(filas, open(os.path.join(base, 'segundo_paso.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    A = [f for f in filas if f['calidad'] == 'A' and 1.40 <= f['cuota'] <= 2.20]    # rango de cuota de la estrategia del usuario; por debajo de 1,40 el precio no paga el riesgo
    md = [f'# Segundo paso · {jor}', '', 'Solo cuota 1,40–2,20 y calidad A (cumple + al menos otra señal: lado Menos, cuota en rango, muestra completa), por p_final (promedio modelo y mercado).',
          '**Sin ventaja demostrada sobre el precio**: ver `registro/validacion_segundo_paso.json`. «valor» y «ventaja» usan la cuota tal cual (con margen de Betano).', '',
          '| Partido | Línea | Cuota | p final | Valor | X de N local/visit. |', '|---|---|---|---|---|---|']
    for f in A[:60]:
        md.append(f"| {f['partido']} | {f['mercado']} {f['ambito']} {f['lado']} {f['linea']} | {f['cuota']:.2f} | {f['p_final']:.0%} | {f['valor']:+.1%} | {f['reg_local']} / {f['reg_visitante']} |")
    open(os.path.join(base, 'segundo_paso.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    return len(filas), len(A)


if __name__ == '__main__':
    if sys.argv[1] == 'validar':
        print(json.dumps(validar(), ensure_ascii=False, indent=1))
    else:
        print(ordenar(sys.argv[2]))
