"""Arma el informe autónomo: plantilla.html + motor.js + datos.json -> backtest.html
Uso: python3 -I pruebas/backtest/construir.py [salida.html]   (antes: preparar_datos.py)"""
import os, sys
B = os.path.dirname(os.path.abspath(__file__))
lee = lambda n: open(os.path.join(B, n), encoding='utf-8').read()
html = lee('plantilla.html').replace('/*__MOTOR__*/', lee('motor.js')).replace('/*__DATOS__*/', lee('datos.json'))
dst = sys.argv[1] if len(sys.argv) > 1 else os.path.join(B, 'backtest.html')
open(dst, 'w', encoding='utf-8').write(html)
print(dst, round(len(html.encode()) / 1e6, 2), 'MB')
