# -*- coding: utf-8 -*-
"""Candidatas para armar combinadas de una VENTANA de partidos con las cuotas releídas (sin tocar registro/lineas.csv).

    python3 recoleccion/combos_ventana.py jornadas/AAAA-MM-DD <clave1,clave2,...> [salida.json]

Toma las filas de registro/lineas.csv de esos partidos (p del modelo, «cumple», X de 10…), reemplaza la cuota por la de jornadas/<día>/betano/<clave>.json (la relectura más reciente),
recalcula EV = p × cuota − 1 y aplica las reglas de analisis_jornada.py (p recortada con el «real hasta hoy», protección < 1,50, sencilla 1,50–1,99, sin alertas del modelo).
Escribe un JSON con las candidatas y las combinadas de 2 patas del mismo partido; las combinadas entre partidos las arma Claude a partir de esa lista (patas de partidos distintos son independientes: cuota = producto)."""
import csv, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
import analisis_jornada as AJ


def cuota_nueva(b, r):
    lado = r['lado']
    if r['mercado'] in ('resultado', 'ambos'):
        for u in b['unicos']:
            if u['mercado'] == r['mercado']:
                return u['opciones'].get(lado)
        return None
    for l in b['lineas']:
        if l['mercado'] == r['mercado'] and l['ambito'] == r['ambito'] and r['linea'] != '' and abs(l['linea'] - float(r['linea'])) < 1e-9:
            return l['mas'] if lado == 'Más' else l['menos']
    return None


def main(base, claves, salida=None):
    base = base.rstrip('/'); jor = os.path.basename(base)
    claves = claves.split(',')
    L = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
    nombres = {}
    for c in claves:
        m = json.load(open(os.path.join(base, 'betano', c + '.json'), encoding='utf8'))['meta']
        nombres[f"{m['local']} - {m['visitante']}"] = (c, json.load(open(os.path.join(base, 'betano', c + '.json'), encoding='utf8'))['betano'], m['cuotas_leidas'])
    J, cambios = [], []
    for r in L:
        if r['jornada'] != jor or r['partido'] not in nombres:
            continue
        c, b, leidas = nombres[r['partido']]
        nueva = cuota_nueva(b, r)
        if nueva is None:
            continue                                   # la línea ya no está ofrecida: no se sugiere
        vieja = AJ.num(r['cuota'])
        r = dict(r); r['cuota'] = str(nueva); r['cuotas_leidas'] = leidas
        p = AJ.num(r['p_modelo'])
        if p is not None:
            r['ev_modelo'] = str(round(p * nueva - 1, 4))
        if vieja and abs(nueva - vieja) / vieja >= 0.05 and r['cumple_ficha'] == 'sí':
            cambios.append([r['partido'], AJ.texto(r), vieja, nueva])
        J.append(r)
    S = [s for s in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'sugerencias.csv'), encoding='utf-8-sig'), delimiter=';') if s['fecha_entrega'] < jor]
    REAL = AJ.real_hasta_hoy([r for r in L if r['jornada'] < jor], S)
    cands = AJ.candidatas(J, REAL)
    prot, sen = AJ.sencillas(cands)
    P = AJ.partidos(base, J, cands)
    alertas = {p['n']: p['familias_alerta'] for p in P}
    com, saltados = AJ.combinadas(base, prot, alertas)
    A = {'jornada': jor, 'claves': claves, 'cuotas_leidas': sorted({v[2] for v in nombres.values()}), 'n_filas': len(J), 'cambios_cumple': cambios,
         'candidatas': [{k: v for k, v in c.items() if k != 'clave'} for c in cands], 'proteccion': [c['texto'] + ' | ' + c['partido'] for c in prot], 'sencillas': [c['texto'] + ' | ' + c['partido'] for c in sen],
         'combinadas_mismo_partido': com, 'saltados': saltados, 'alertas': alertas}
    salida = salida or os.path.join(base, 'combos_ventana.json')
    json.dump(A, open(salida, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(f'{len(J)} filas · {len(cands)} cumplen · {len(prot)} protecciones · {len(sen)} sencillas · {len(com)} combis mismo partido · {len(cambios)} cuotas que cumplían se movieron ≥5 %')


if __name__ == '__main__':
    main(*sys.argv[1:4])
