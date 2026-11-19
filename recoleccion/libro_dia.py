# -*- coding: utf-8 -*-
"""Agrega/reconstruye hojas de un día en registro/libro_apuestas.xlsx (memoria acumulada).

    python3 recoleccion/libro_dia.py lineas  AAAA-MM-DD            # hoja «Líneas DD-mmm» (solo cumplió/falló; las «nula» y pendientes no se listan)
    python3 recoleccion/libro_dia.py sugeridas AAAA-MM-DD          # hoja «Sugeridas DD-mmm» desde registro/sugerencias.csv
    python3 recoleccion/libro_dia.py boletos "<nombre hoja>" "<título>" "<nota>" <boletos_betano.json> <patas_calificadas.json> <desde_n>
Reconstruye la hoja si ya existe (conserva su posición). Formato igual al de las hojas del 17-nov. Requiere openpyxl.
"""
import csv, json, os, sys
import openpyxl
from openpyxl.styles import Font

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = os.path.join(RAIZ, 'registro', 'libro_apuestas.xlsx')
MES = {'11': 'nov'}


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x or None


def hoja(wb, nombre, despues=None):
    if nombre in wb.sheetnames:
        i = wb.sheetnames.index(nombre); del wb[nombre]; return wb.create_sheet(nombre, i)
    i = wb.sheetnames.index(despues) + 1 if despues in wb.sheetnames else len(wb.sheetnames)
    return wb.create_sheet(nombre, i)


def lineas(wb, dia, despues):
    rows = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'))
    L = [r for r in rows if r['jornada'] == dia and r['resultado'] in ('cumplió', 'falló')]
    d, m = dia[8:], MES.get(dia[5:7], dia[5:7])
    ws = hoja(wb, f'Líneas {int(d)}-{m}', despues)
    n_eq = sum(1 for r in L if not r['mercado'].startswith('jugador'))
    ws['A1'] = f'Líneas de la jornada del {int(d)}-{m} calificadas ({n_eq} de equipo y {len(L) - n_eq} de jugador; anuladas por «no jugó» y sin resultado no se listan; actualizado el 19-nov)'
    ws['A1'].font = Font(bold=True, size=11)
    ws['A2'] = 'Fuente: registro/lineas.csv (calificar_lineas.py + calificar_jugadores.py con Flashscore; jornadas/%s/resultados/). «Cumple» = ≥ 7 de 10 en ambos.' % dia
    ws.append([])
    ws.append(['Jornada', 'Partido', 'Mercado', 'Ámbito', 'Línea', 'Lado', 'Cuota', 'p modelo', 'p mercado', 'EV', 'Local', 'Visitante', 'Cumple', 'Resultado', 'Acierto (1/0)', 'Valor real / fuente'])
    for c in ws[4]:
        c.font = Font(bold=True)
    for r in L:
        m_ = r['mercado'] + (' · ' + r['jugador'] if r['jugador'] else '')
        ws.append([r['jornada'], r['partido'], m_, r['ambito'], num(r['linea']), r['lado'], num(r['cuota']), num(r['p_modelo']), num(r['p_mercado']), num(r['ev_modelo']),
                   r['reg_local'] or None, r['reg_visitante'] or None, r['cumple_ficha'] or None, r['resultado'], 1 if r['resultado'] == 'cumplió' else 0, r['nota']])
    ws.freeze_panes = 'A5'
    ws.auto_filter.ref = f'A4:P{ws.max_row}'
    print(ws.title, len(L), 'líneas')


def sugeridas(wb, dia, despues):
    rows = list(csv.DictReader(open(os.path.join(RAIZ, 'registro', 'sugerencias.csv'), encoding='utf-8-sig'), delimiter=';'))
    L = [r for r in rows if r['fecha_entrega'] == dia]
    d, m = dia[8:], MES.get(dia[5:7], dia[5:7])
    ws = hoja(wb, f'Sugeridas {int(d)}-{m}', despues)
    cols = ['id', 'fecha_entrega', 'hora', 'entrega', 'tipo', 'nombre', 'partidos', 'n_patas', 'cuota', 'p_estimada', 'resultado', 'detalle_patas', 'patas_que_fallaron', 'familia_fallo', 'jugada', 'nota', 'fuente']
    ws.append(cols)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in L:
        ws.append([num(r[c]) if c in ('n_patas', 'cuota', 'p_estimada') else (r[c] or None) for c in cols])
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f'A1:Q{ws.max_row}'
    print(ws.title, len(L), 'sugerencias')


def boletos(wb, nombre, titulo, nota, bol, patas, desde, despues):
    B = [b for b in json.load(open(bol, encoding='utf-8'))['boletos'] if b['n'] >= desde]
    P = json.load(open(patas, encoding='utf-8'))
    ws = hoja(wb, nombre, despues)
    ws['A1'] = titulo; ws['A1'].font = Font(bold=True, size=11)
    ws['A2'] = nota
    ws.append([])
    ws.append(['N.º', 'Fecha', 'Tipo', 'Stake', 'Gratis', 'Cuota', 'Resultado', 'Cobrado', 'Neto', 'Partidos', 'Patas', 'Qué falló'])
    for c in ws[4]:
        c.font = Font(bold=True)
    for b in B:
        q = P.get(str(b['n']), {})
        ws.append([b['n'], b['fecha'], b['tipo'], b['stake'], 'sí' if b.get('gratis') else 'no', b['cuota'], b['resultado'], b['cobrado'], b['cobrado'] - b['stake'], b['partidos'], b['patas'], q.get('falla', '')])
    n = len(B)
    ws.append([])
    ws.append(['Total', None, None, f'=SUM(D5:D{4 + n})', None, None, None, f'=SUM(H5:H{4 + n})', f'=SUM(I5:I{4 + n})'])
    for c in ws[ws.max_row]:
        c.font = Font(bold=True)
    for col, w in zip('ABCDEFGHIJKL', (6, 12, 15, 10, 7, 7, 10, 10, 10, 50, 70, 70)):
        ws.column_dimensions[col].width = w
    print(ws.title, n, 'boletos')


if __name__ == '__main__':
    wb = openpyxl.load_workbook(LIBRO)
    a = sys.argv[1]
    if a == 'lineas':
        lineas(wb, sys.argv[2], 'Líneas 17-nov' if sys.argv[2] != '2026-11-17' else 'Líneas 16-nov')
    elif a == 'sugeridas':
        sugeridas(wb, sys.argv[2], 'Sugeridas 17-nov' if sys.argv[2] != '2026-11-17' else 'Líneas 17-nov')
    elif a == 'boletos':
        boletos(wb, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], int(sys.argv[7]), 'Boletos 17-nov')
    wb.save(LIBRO)
