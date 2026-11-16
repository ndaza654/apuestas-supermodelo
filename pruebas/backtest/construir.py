"""Arma el informe autónomo: plantilla.html + motor.js + datos.json -> backtest.html
Uso: python3 -I pruebas/backtest/construir.py [salida.html]   (antes: preparar_datos.py). El dashboard lo importa con construir(hoy, val)."""
import os, sys
B = os.path.dirname(os.path.abspath(__file__))
lee = lambda n: open(os.path.join(B, n), encoding='utf-8').read()
import json


def construir(hoy=None, val=None):
    """Devuelve el HTML autónomo. hoy = {'jornada':..., 'lineas':[...]} y val = validacion_tasas.json son opcionales (pestaña «Hoy» y prueba con líneas jugadas)."""
    j = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return (lee('plantilla.html').replace('/*__MOTOR__*/', lee('motor.js')).replace('/*__DATOS__*/', lee('datos.json'))
            .replace('/*__HOY__*/', j(hoy) if hoy else 'null').replace('/*__VAL__*/', j(val) if val else 'null'))


def principal():
    R = os.path.dirname(os.path.dirname(B))
    pv = os.path.join(R, 'registro', 'validacion_tasas.json')
    val = json.load(open(pv, encoding='utf-8')) if os.path.exists(pv) else None
    return construir(None, val)


if __name__ == '__main__':
    html = principal()
    dst = sys.argv[1] if len(sys.argv) > 1 else os.path.join(B, 'backtest.html')
    open(dst, 'w', encoding='utf-8').write(html)
    print(dst, round(len(html.encode()) / 1e6, 2), 'MB')
