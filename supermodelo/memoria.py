# -*- coding: utf-8 -*-
"""Memoria propia: lo que pasó con las líneas que NOSOTROS sugerimos (balance 4–8 nov, 151 líneas calificadas).

Sirve para AVISAR, no para mover la probabilidad: el sesgo de selección es real (sugerimos las líneas que el modelo
viejo "veía con valor", y esas rindieron peor que el precio), así que ajustar con esto toda la probabilidad
castigaría líneas que nadie eligió. En cambio, cuando una línea que el modelo marca con valor cae en un grupo donde
el historial propio quedó claramente por debajo del precio, el informe lo dice con las cifras.

Una nota sale solo si el grupo tiene >= MIN_N casos y se aleja >= MIN_DIF puntos de la probabilidad implícita.
El grupo se actualiza con registro.informe() cuando haya más datos propios."""
import json, os

RUTA = os.path.join(os.path.dirname(__file__), '..', 'datos', 'memoria_propia.json')
MIN_N = 6
MIN_DIF = 0.15
_MEM = None


def cargar():
    global _MEM
    if _MEM is None:
        try:
            _MEM = json.load(open(RUTA, encoding='utf-8'))
        except OSError:
            _MEM = {}
    return _MEM


def notas(familia, lado, submercado, cuota, ev):
    """Devuelve una lista de textos cortos; vacía si no hay nada que advertir. Solo para líneas con EV positivo."""
    mem, out = cargar(), []
    if ev < 0.03:
        return out
    g = (mem.get('familia_lado') or {}).get(f'{familia}|{lado}')
    if g and g['n'] >= MIN_N:
        real = g['aciertos'] / g['n']
        if real <= g['implicita'] - MIN_DIF:
            out.append(f"Historial propio en contra ({familia} {lado}: {g['aciertos']}/{g['n']} contra {g['implicita'] * 100:.0f} % del precio)")
    sub = submercado or ''
    rol = mem.get('rol_equipo') or {}
    if sub.split(' ')[0] in ('remates', 'al_arco', 'corners') and ' favorito ' in f' {sub} ' and 'no favorito' not in sub and sub.endswith('Menos'):
        r = rol.get('volumen_menos_equipo_que_gano')
        if r:
            out.append(f"Línea contra el guion del favorito (Menos de un equipo que ganó: {r['aciertos']}/{r['n']})")
    if sub.split(' ')[0] in ('remates', 'al_arco', 'corners') and 'no favorito' in sub and sub.endswith('Más'):
        r = rol.get('volumen_mas_equipo_que_perdio')
        if r:
            out.append(f"Línea contra el guion (Más de un equipo que perdió: {r['aciertos']}/{r['n']})")
    return out


def nota_liga(liga):
    """Aviso suave por liga, solo si hay muestra y la diferencia es grande. El país sale de ligas.codigo (así 'Serie A' de
    Brasil o de Ecuador no recibe el historial de Italia)."""
    from . import ligas
    mem = (cargar().get('pais') or {})
    pais = {'I1': 'ITALIA', 'I2': 'ITALIA', 'MEX': 'MÉXICO', 'SP1': 'ESPAÑA', 'SP2': 'ESPAÑA'}.get(ligas.codigo(liga))
    if pais and pais in mem:
        g = mem[pais]
        if g['n'] >= 10 and abs(g['aciertos'] / g['n'] - g['implicita']) >= 0.15:
            return f"Liga con historial propio atípico ({pais}: {g['aciertos']}/{g['n']} contra {g['implicita'] * 100:.0f} % del precio)"
    return None
