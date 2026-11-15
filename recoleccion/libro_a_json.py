#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrae del libro `registro/libro_apuestas.xlsx` los datos CRUDOS del 4 al 8-nov (boletos, selecciones, partidos con
estadísticas finales, banca, lecciones y reglas) a `registro/historico_libro.json`, que es lo que lee el dashboard.
Así el dashboard (y el flujo de GitHub Pages) no necesita Excel. Solo toma celdas con valor: las fórmulas del libro no se leen.
Uso: python3 recoleccion/libro_a_json.py   (vuelve a escribir el JSON; el libro sigue siendo la fuente)."""
import os, sys, json, datetime
import openpyxl

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = os.path.join(RAIZ, 'registro', 'libro_apuestas.xlsx')
SALIDA = os.path.join(RAIZ, 'registro', 'historico_libro.json')


def v(c):
    if isinstance(c, datetime.datetime):
        return c.strftime('%Y-%m-%d') if (c.hour, c.minute, c.second) == (0, 0, 0) else c.strftime('%Y-%m-%d %H:%M')
    if isinstance(c, float) and c == int(c):
        return int(c)
    if isinstance(c, str):
        c = c.strip()
        return c if c != '' else None
    return c


def filas(ws, cabecera_fila):
    """Devuelve dicts {columna: valor} desde la fila siguiente a la cabecera, sin celdas de fórmula (=...)."""
    rows = list(ws.iter_rows(values_only=True))
    cab = [str(c).strip() if c is not None else '' for c in rows[cabecera_fila - 1]]
    out = []
    for r in rows[cabecera_fila:]:
        d = {}
        for h, c in zip(cab, r):
            if not h:
                continue
            c = v(c)
            if isinstance(c, str) and c.startswith('='):
                c = None
            d[h] = c
        out.append(d)
    return out


def main():
    wb = openpyxl.load_workbook(LIBRO, data_only=False)
    H = {'fuente': 'registro/libro_apuestas.xlsx (hojas Boletos, Selecciones, Partidos, Banca, Lecciones, Reglas)',
         'extraido': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), 'periodo': '2026-11-04 a 2026-11-08'}
    # Boletos 4–8 (cabecera en la fila 4)
    bol = []
    for d in filas(wb['Boletos'], 4):
        if not isinstance(d.get('#'), (int, float)) and not str(d.get('#') or '').isdigit():
            continue
        if not d.get('Código Betano'):
            continue
        bol.append({'n': int(d['#']), 'codigo': str(d['Código Betano']), 'fecha': d['Fecha'], 'hora': d['Hora'], 'tipo': d['Tipo de boleto'],
                    'partidos_n': d['Nº partidos'], 'selecciones_n': d['Nº selecciones'], 'cuota': d['Cuota'], 'stake': d['Stake (COP)'],
                    'gratis': d['Apuesta gratis'] == 'Sí', 'vivo': d['En vivo'] == 'Sí', 'resultado': d['Resultado'], 'cobrado': d['Cobrado (COP)'] or 0,
                    'partidos': d['Partidos'], 'ligas': d['Ligas'], 'mercados': d['Mercados incluidos'], 'etiqueta': d['Diagnóstico (etiqueta)'],
                    'que_paso': d['Qué pasó'], 'mejor': d['Cómo armarlo mejor']})
    H['boletos'] = bol
    # Selecciones (cabecera fila 4)
    sel = []
    for d in filas(wb['Selecciones'], 4):
        if not d.get('Código Betano') or not d.get('Partido'):
            continue
        sel.append({'n': d['#'], 'boleto': d['Boleto #'], 'codigo': str(d['Código Betano']), 'fecha': d['Fecha'], 'partido': d['Partido'], 'liga': d['Liga'],
                    'marcador': d['Marcador final'], 'mercado_betano': d['Mercado (Betano)'], 'seleccion': d['Selección'], 'familia': d['Familia de mercado'],
                    'ambito': d['Ámbito'], 'lado': d['Lado'], 'linea': d['Línea'], 'valor_real': d['Valor real (Flashscore)'], 'resultado': d['Resultado'],
                    'cuota_pata': d['Cuota de la pata'], 'tipo_boleto': d['Tipo de boleto'], 'vivo': d['En vivo'] == 'Sí'})
    H['selecciones'] = sel
    # Partidos con estadísticas finales (cabecera fila 4)
    par = []
    for d in filas(wb['Partidos'], 4):
        if not d.get('Partido') or not d.get('Fecha'):
            continue
        par.append({k: d.get(k) for k in ('Fecha', 'Partido', 'Liga', 'Marcador', 'Descanso', 'Árbitro', 'xG', 'Posesión %', 'Remates', 'Al arco', 'Córners', 'Córners 1T',
                                          'Faltas', 'Amarillas', 'Rojas', 'Fueras de lugar', 'Saques de meta', 'Saques de banda', 'Atajadas', 'Total córners',
                                          'Total tarjetas', 'Total faltas', 'Total remates', 'Goles y expulsiones', 'Titular Flashscore')})
    H['partidos'] = par
    # Banca (cabecera fila 4): movimientos hasta «Bonos»
    ban, extra = [], {}
    for d in filas(wb['Banca'], 4):
        f = d.get('Fecha y hora')
        if f and isinstance(f, str) and f[:2] == '20' and d.get('Tipo'):
            ban.append({'fecha': f, 'tipo': d['Tipo'], 'codigo': str(d['Código de apuesta']) if d.get('Código de apuesta') else None, 'monto': d['Monto (COP)'], 'saldo': d['Saldo después (COP)']})
        elif f in ('Bonos', 'Saldo final calculado', 'Saldo que muestra Betano', 'Diferencia'):
            extra[f] = {k: x for k, x in d.items() if k != 'Fecha y hora' and x is not None}
    H['banca'] = ban
    H['banca_cierre'] = extra
    # Lecciones y reglas (texto)
    lec = []
    for d in filas(wb['Lecciones'], 4):
        vals = [x for x in d.values() if x is not None]
        if not vals:
            continue
        num = d.get('#')
        if isinstance(num, (int, float)) or str(num or '').isdigit():
            lec.append({'n': int(num), 'tema': d.get('Tema'), 'leccion': d.get('Lección'), 'evidencia': d.get('Evidencia (4–8 nov)'), 'hacer': d.get('Qué hacer desde ya')})
        else:   # filas de la «Auditoría de sugerencias»: título en «#», hallazgo en «Tema», qué hacer en «Lección»
            lec.append({'n': None, 'tema': str(num), 'leccion': d.get('Tema'), 'evidencia': None, 'hacer': d.get('Lección')})
    H['lecciones'] = lec
    H['reglas'] = [{'n': d['#'], 'regla': d['Regla'], 'porque': d['Por qué (dato del periodo)']} for d in filas(wb['Reglas'], 4) if d.get('Regla')]
    with open(SALIDA, 'w', encoding='utf-8') as f:
        json.dump(H, f, ensure_ascii=False, indent=1)
    print(SALIDA, {k: len(x) for k, x in H.items() if isinstance(x, list)})


if __name__ == '__main__':
    main()
