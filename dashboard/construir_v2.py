#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dashboard v2 («Mando», blanco y azul). Un solo HTML autónomo (sin red) con los datos del repo.
Uso: python3 dashboard/construir_v2.py [salida.html] [jornada ...]   (sin jornadas: todo el registro)
Fuentes: dashboard/datos.py (registro/*.csv, jornadas/*) + lo de abajo (análisis, alineaciones, estrategia). Nada se inventa."""
import os, sys, json, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import datos

SRC = ['core.js', 'charts.js', 'ui.js', 'pag_inicio.js', 'pag_partido.js', 'pag_estrategia.js', 'pag_cupon.js', 'pag_bb.js', 'pag_aprender.js', 'pag_historico.js', 'pag_datos.js', 'pag_backtest.js', 'app.js']


def extras(d):
    AN, XI, EST = {}, {}, {}
    for i, p in enumerate(d['P']):
        base = os.path.join(datos.RAIZ, 'jornadas', p['jor'])
        if p.get('slug'):
            fa = os.path.join(base, 'alineaciones', p['slug'] + '.json')
            if os.path.exists(fa):
                a = json.load(open(fa, encoding='utf8'))
                pr = a.get('probables') or a.get('confirmadas') or {}
                XI[i] = {'tipo': a.get('tipo', ''), 'leida': a.get('lectura_utc', ''), 'L': [x[0] for x in pr.get('L', [])], 'V': [x[0] for x in pr.get('V', [])]}
    for j in d['jors']:
        base = os.path.join(datos.RAIZ, 'jornadas', j)
        fa = os.path.join(base, 'analisis.json')
        if os.path.exists(fa):
            A = json.load(open(fa, encoding='utf8'))
            for x in A.get('partidos', []):
                for i, p in enumerate(d['P']):
                    if p['jor'] == j and p['n'] == x['n']:
                        AN[i] = {k: x.get(k) for k in ('p1', 'px', 'p2', 'alertas', 'enfoque', 'bajas', 'dudas', 'xi', 'tabla', 'clima', 'estado', 'familias_alerta')}
        fe = os.path.join(base, 'estrategia.json')
        if os.path.exists(fe):
            EST[j] = json.load(open(fe, encoding='utf8'))
    BB = {}
    for j in d['jors']:
        fb = os.path.join(datos.RAIZ, 'jornadas', j, 'bb', 'bb_boost_resumen.json')
        if os.path.exists(fb):
            BB[j] = json.load(open(fb, encoding='utf8'))
    d.update({'AN': AN, 'XI': XI, 'EST': EST, 'BB': BB})
    d['BT'] = backtest(d)
    return d


def backtest(d):
    """Explorador del backtest (pruebas/backtest/): HTML autónomo con la pestaña «Hoy» de la última jornada con análisis. Sin los datos compactos no hay página."""
    import importlib.util
    B = os.path.join(datos.RAIZ, 'pruebas', 'backtest')
    if not os.path.exists(os.path.join(B, 'datos.json')):
        return None
    sp = importlib.util.spec_from_file_location('bt_construir', os.path.join(B, 'construir.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    hoy = None
    for j in sorted(d['jors'], reverse=True):
        fa = os.path.join(datos.RAIZ, 'jornadas', j, 'analisis.json')
        if os.path.exists(fa):
            A = json.load(open(fa, encoding='utf8'))
            if A.get('lineas_cumplen'):
                hoy = {'jornada': j, 'lineas': [{k: v for k, v in x.items() if k != 'real'} for x in A['lineas_cumplen']]}
                break
    pv = os.path.join(datos.RAIZ, 'registro', 'validacion_tasas.json')
    return m.construir(hoy, json.load(open(pv, encoding='utf8')) if os.path.exists(pv) else None)


def main(a):
    out = a[1] if len(a) > 1 else os.path.join(AQUI, 'v2', 'dashboard.html')
    jors = a[2:] or None
    d = extras(datos.construir(jors))
    js = '\n'.join(open(os.path.join(AQUI, 'v2', f), encoding='utf8').read() for f in SRC)
    css = open(os.path.join(AQUI, 'v2', 'estilo.css'), encoding='utf8').read()
    blob = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<title>Mando · apuestas</title><style>' + css + '</style></head><body><div id="app"></div>'
            '<script id="db" type="application/json">' + blob + '</script><script>' + js + '</script></body></html>')
    open(out, 'w', encoding='utf8').write(html)
    print(out, len(html) // 1024, 'KB', len(d['P']), 'partidos', len(d['L']), 'líneas de equipo', len(d['J']), 'de jugador')


if __name__ == '__main__':
    main(sys.argv)
