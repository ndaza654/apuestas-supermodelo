# -*- coding: utf-8 -*-
"""Califica las líneas de EQUIPO de `registro/lineas.csv` con los resultados reales de los partidos (balance).

    python3 recoleccion/calificar_lineas.py <jornada> <resultados.json>     (jornada = valor de la columna «jornada»)

`resultados.json` = {"<partido tal como sale en lineas.csv>": {"fuente": "...", "g":[h,a], "g1":[h,a], "c":[h,a], "c1":[h,a],
    "y":[h,a], "y1":[h,a], "sh":[h,a], "sot":[h,a], "f":[h,a], "off":[h,a], "ti":[h,a], "gk":[h,a], (opcional "sh1","sot1","off1","ti1","gk1")}}
  · y / y1 = tarjetas en PUNTOS de Betano (amarilla 1 + roja 2).  · g = goles del tiempo reglamentario (sin prórroga/penales).
  · [h, a] = local, visitante.  Lo que falte en el JSON deja la línea sin calificar («sin resultado»): no se inventa.
Escribe en lineas.csv la columna `resultado` (cumplió / falló / media ganada / media perdida / nula) y, en `nota`, el valor real.
Solo califica líneas de equipo (córners, goles, tarjetas, remates, tiros al arco, faltas, fueras, saques); las de jugador necesitan
estadística por jugador y se califican aparte. No toca las columnas apostada/stake/cuota_cierre.
"""
import csv, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAVE = {'goles': 'g', 'corners': 'c', 'tarjetas': 'y', 'remates': 'sh', 'al_arco': 'sot', 'faltas': 'f', 'fueras': 'off',
         'saques_banda': 'ti', 'saques_meta': 'gk'}


def valor(res, mercado, ambito):
    """Valor real de la estadística para el ámbito de la línea; None si el resultado no lo trae."""
    k = CLAVE.get(mercado)
    if not k or k not in res:
        return None
    h, a = res[k]
    if ambito == 'total':
        return h + a
    if ambito == 'local':
        return h
    if ambito == 'visitante':
        return a
    k1 = k + '1' if k in ('g', 'c', 'y') else k + '1'
    if ambito == '1T':
        return (res[k1][0] + res[k1][1]) if k1 in res else None
    if ambito == '2T':
        return (h + a - res[k1][0] - res[k1][1]) if k1 in res else None
    return None


def _mitad(v, linea, lado):
    """+1 gana, 0 nula (empate con la línea), -1 pierde, para una línea entera o con .5."""
    if v == linea:
        return 0
    return 1 if ((v > linea) == (lado == 'Más')) else -1


def calificar(v, linea, lado):
    """cumplió / falló / media ganada / media perdida / nula. Líneas asiáticas (.25 y .75) = dos medias líneas."""
    if round(linea * 4) % 2 == 1:                     # .25 o .75
        a, b = _mitad(v, linea - 0.25, lado), _mitad(v, linea + 0.25, lado)
        t = a + b
        return 'cumplió' if t == 2 else 'falló' if t == -2 else 'media ganada' if t == 1 else 'media perdida' if t == -1 else 'nula'
    r = _mitad(v, linea, lado)
    return 'cumplió' if r > 0 else 'falló' if r < 0 else 'nula'


def calificar_unico(res, mercado, lado):
    """Ambos marcan (Sí/No) y resultado (1/X/2/1X/X2/12) con los goles del tiempo reglamentario `g`=[h,a]. None si falta el dato."""
    if 'g' not in res:
        return None, None
    h, a = res['g']
    if mercado == 'ambos':
        ok = (h > 0 and a > 0) if lado == 'Sí' else (h == 0 or a == 0)
    else:
        r = '1' if h > a else ('2' if a > h else 'X')
        ok = {'1': r == '1', 'X': r == 'X', '2': r == '2', '1X': r in '1X', 'X2': r in 'X2', '12': r != 'X'}.get(lado)
        if ok is None:
            return None, None
    return ('cumplió' if ok else 'falló'), f'{h}-{a}'


def main(jornada, ruta_res):
    res = json.load(open(ruta_res, encoding='utf8'))
    ruta = os.path.join(RAIZ, 'registro', 'lineas.csv')
    f = open(ruta, encoding='utf-8-sig', newline='')
    rd = csv.DictReader(f, delimiter=';')
    campos, filas = rd.fieldnames, list(rd)
    f.close()
    n = g = 0
    for r in filas:
        if r['jornada'] != jornada or r['mercado'].startswith('jugador') or r['partido'] not in res:
            continue
        R = res[r['partido']]
        if r['mercado'] in ('ambos', 'resultado'):       # una sola cuota por selección (desde el 18-nov-2026)
            cal, marc = calificar_unico(R, r['mercado'], r['lado'])
            if cal:
                r['resultado'] = cal
                r['nota'] = ((r['nota'] + ' · ') if r['nota'] and 'valor real' not in r['nota'] else '') + f'valor real {marc} ({R.get("fuente", "")})'
                n += 1
                g += cal == 'cumplió'
            continue
        v = valor(R, r['mercado'], r['ambito'])
        try:
            linea = float(r['linea'])
        except ValueError:
            continue
        if v is None or r['lado'] not in ('Más', 'Menos'):
            continue
        r['resultado'] = calificar(v, linea, r['lado'])
        r['nota'] = ((r['nota'] + ' · ') if r['nota'] and 'valor real' not in r['nota'] else '') + f'valor real {v:g} ({R.get("fuente", "")})'
        n += 1
        g += r['resultado'] == 'cumplió'
    with open(ruta, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, campos, delimiter=';', lineterminator='\n')
        w.writeheader()
        w.writerows(filas)
    print(f'{jornada}: {n} líneas de equipo calificadas ({g} cumplieron)')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
