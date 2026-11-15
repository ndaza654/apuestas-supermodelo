#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del histórico del dashboard: lo extraído del libro (4–8 nov) cuadra con lo que el propio libro declara
y `dashboard/datos.py` lo suma al resto sin perder ni duplicar boletos. Uso: python3 pruebas/test_dashboard.py"""
import os, sys, json, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'dashboard'))
sys.path.insert(0, os.path.join(RAIZ, 'recoleccion'))
import datos

OK = 0


def ok(c, msg):
    global OK
    assert c, msg
    OK += 1


H = json.load(open(os.path.join(RAIZ, 'registro', 'historico_libro.json'), encoding='utf8'))
bol, sel = H['boletos'], H['selecciones']
real = [b for b in bol if not b['gratis']]
ok(len(bol) == 51 and len(real) == 48, 'el libro declara 48 boletos con dinero y 3 gratis')
ok(sum(b['cobrado'] for b in bol) - sum(b['stake'] for b in real) == 74625, 'neto del 4 al 8-nov: +74.625 (lección 2 del libro)')
ok(sum(1 for b in real if b['cobrado'] > 0) == 13, '13 boletos con dinero cobraron')
ok(sum(1 for b in real if b['vivo']) == 13 and sum(1 for b in real if b['vivo'] and b['resultado'] == 'Ganada') == 3, 'en vivo: 3 de 13')
ok([b['stake'] for b in real if b['stake'] > 30000] and all(b['resultado'] == 'Perdida' for b in real if b['stake'] > 30000), 'los boletos de más de 30.000 se perdieron todos')
c = collections.Counter(s['resultado'] for s in sel)
ok(c['Ganó'] == 110 and c['Perdió'] + c['Ganó'] == 185, '110 de 185 selecciones')
ok(len(H['partidos']) == 72 and len(H['lecciones']) >= 22 and len(H['reglas']) == 13, 'partidos, lecciones y reglas')

d = datos.construir()
nums = [b[0] for b in d['B']]
ok(len(nums) == len(set(nums)), 'sin boletos duplicados')
ok(all(len(b) == 13 for b in d['B']), 'cada boleto trae sus 13 campos')
ok(sum(1 for b in d['B'] if b[1][:10] <= '2026-11-08') == 51, 'los 51 boletos del 4 al 8 entran al dashboard')
ok({b[7] for b in d['B']} <= {'Ganada', 'Perdida', 'Cash out'}, 'resultados normalizados (Cash out)')
ok(d['HIST'] and len(d['HIST']['sel']) == 186 and all(len(x) == 17 for x in d['HIST']['sel']), 'selecciones con su tamaño de grupo')
solo = [x for x in d['HIST']['sel'] if x[16] == 1]
ok(len(solo) == 53, '53 selecciones con precio propio; en un Bet Builder la cuota de la pata es la del grupo')
ok(all(len(h) == 10 for h in d['HL']), 'picks 9–12 con su tipo')
cortos = datos.construir(['2026-11-13'])
ok(cortos['HIST'] is None and all(b[1][:10] == '2026-11-13' for b in cortos['B']), 'los datos cortos no cargan el histórico completo')
print(OK, 'pruebas del histórico del dashboard superadas')
