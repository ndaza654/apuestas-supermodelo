# -*- coding: utf-8 -*-
"""Genera los tres prototipos del dashboard (HTML autónomos, sin red ni librerías) con los datos del repo.
    python3 dashboard/construir_prototipos.py
Salida: dashboard/prototipos/dashboard_A_mando.html, dashboard_B_movil.html, dashboard_C_laboratorio.html"""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import datos
SRC = os.path.join(AQUI, 'src')
CFGS = {
    'A': dict(id='A', name='Mando', slug='A_mando', home='hoy', lineasMode='tabla', hoy='grid', nav='side', theme='dark', filtersOpen=True),
    'B': dict(id='B', name='Móvil', slug='B_movil', home='hoy', lineasMode='tarjetas', hoy='timeline', nav='bottom', theme='light', filtersOpen=False),
    'C': dict(id='C', name='Laboratorio', slug='C_laboratorio', home='laboratorio', lineasMode='pivote', hoy='lab', nav='top', theme='light', filtersOpen=True),
}
def leer(n):
    return open(os.path.join(SRC, n), encoding='utf8').read()
def main(jornadas=None, solo=None, salida=None, titulo='prototipo'):
    D = datos.construir(jornadas)
    bundle = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    js = {n: leer(n + '.js') for n in ('lib', 'pages1', 'pages2', 'pages3', 'app')}
    js['lib'] = js['lib'].replace('/*DATA*/', bundle, 1)
    out = salida or os.path.join(AQUI, 'prototipos')
    os.makedirs(out, exist_ok=True)
    for k, c in CFGS.items():
        if solo and k not in solo:
            continue
        css = leer('base.css') + '\n' + leer(f'tema_{k.lower()}.css')
        cfg = json.dumps(c, ensure_ascii=False)
        html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#0c1117">
<title>Dashboard de apuestas · {titulo} {k} «{c['name']}»</title><style>{css}</style></head><body>
<div id="app"><div id="nav"></div><div class="wrap"><header class="top"><h1>Apuestas · <span id="ptitle"></span></h1><span class="sp"></span><input id="gq" type="search" placeholder="Buscar en todo ( / )" aria-label="Buscar"><button class="b sm" data-act="theme" title="Claro / oscuro">◐</button><button id="cupb" data-go="cupon" hidden></button></header>
<div class="content"><div class="body"><div class="main"><div id="pf"></div><div id="pm"></div></div><aside id="det"></aside></div></div><div id="gen"></div></div></div>
<script>const CFG={cfg};</script><script>{js['lib']}
{js['pages1']}
{js['pages2']}
{js['pages3']}
{js['app']}</script></body></html>'''
        p = os.path.join(out, f'dashboard_{c["slug"]}.html')
        open(p, 'w', encoding='utf8').write(html)
        print(p, os.path.getsize(p) // 1024, 'KB')
if __name__ == '__main__':
    # python3 dashboard/construir_prototipos.py                 → los tres prototipos con todos los datos
    # python3 dashboard/construir_prototipos.py --prueba A      → solo A, «datos cortos»: balance 12 y 13-nov + jornada 15-nov
    if '--prueba' in sys.argv:
        k = sys.argv[sys.argv.index('--prueba') + 1] if len(sys.argv) > sys.argv.index('--prueba') + 1 else 'A'
        main(['2026-11-12-noche', '2026-11-13', '2026-11-15'], solo=[k], salida=os.path.join(AQUI, 'prueba'), titulo='prueba')
    else:
        main()
