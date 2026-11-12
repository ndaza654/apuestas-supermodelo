# -*- coding: utf-8 -*-
"""Suma de verificación (la misma del navegador) para comprobar que un archivo pasó sin errores: python3 verificar_hash.py archivo [hash_esperado]"""
import sys
def h(s):
    x = 0
    for c in s:
        o = ord(c)
        if o > 0xFFFF:                      # JS cuenta pares sustitutos
            o -= 0x10000
            for u in (0xD800 + (o >> 10), 0xDC00 + (o & 0x3FF)):
                x = (x * 31 + u) & 0xFFFFFFFF
        else:
            x = (x * 31 + o) & 0xFFFFFFFF
    return x
if __name__ == '__main__':
    t = open(sys.argv[1], encoding='utf8').read().rstrip('\n')
    r = h(t)
    ok = '' if len(sys.argv) < 3 else ('  OK' if str(r) == sys.argv[2] else '  ¡NO COINCIDE! esperado ' + sys.argv[2])
    print(r, len(t), ok)
