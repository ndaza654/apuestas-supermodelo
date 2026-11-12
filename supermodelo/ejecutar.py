# -*- coding: utf-8 -*-
"""Uso (desde la carpeta del paquete):
  python3 -m supermodelo partido.json                      → informe .md, .html y .json junto a la entrada
  python3 -m supermodelo partido.json --registro registro.csv [--apostadas "Gana X;Córners Más 9.5"]
      (los combos de la entrada con "apostado": true también se guardan en el registro y se califican al cerrar)
  python3 -m supermodelo --combos partido.json combos.json  → combos con la cuota real del cupón (stress, margen, estado)
  python3 -m supermodelo --vivo partido.json vivo.json      → en vivo desde el estado actual
  python3 -m supermodelo --cerrar registro.csv "Local - Visitante" real.json [cierres.json] [--partidos ruta.csv] [--referencia ref.json]
                                                           → califica todas las líneas con las estadísticas reales y guarda
                                                             el partido en la base propia (por defecto datos/partidos.csv)
  python3 -m supermodelo --informe registro.csv            → aprendizaje: qué mercados y contextos funcionan
  python3 -m supermodelo --balance registro.csv [--desde 2026-11-01] [--hasta 2026-11-08]
  python3 -m supermodelo --sombra sombra.csv               → fuentes externas medidas en sombra
"""
import sys, json, os, datetime as dt
from . import registro


def _existe(ruta):
    if not os.path.exists(ruta):
        print(f'No encuentro el archivo: {ruta}')
        return False
    return True


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__); return
    for op in ('--informe', '--balance', '--sombra'):
        if op in argv and not _existe(argv[argv.index(op) + 1]):
            return
    if '--informe' in argv:
        print(registro.informe(argv[argv.index('--informe') + 1])); return
    if '--balance' in argv:
        from .balance import balance
        d = dt.date.fromisoformat(argv[argv.index('--desde') + 1]) if '--desde' in argv else None
        h = dt.date.fromisoformat(argv[argv.index('--hasta') + 1]) if '--hasta' in argv else None
        print(balance(argv[argv.index('--balance') + 1], d, h)); return
    if '--sombra' in argv:
        from .sombra import informe
        print(informe(argv[argv.index('--sombra') + 1])); return
    if '--combos' in argv:
        from .combos import main as cm
        i = argv.index('--combos'); cm(argv[i + 1:i + 3] + (['--registro', argv[argv.index('--registro') + 1]] if '--registro' in argv else [])); return
    if '--vivo' in argv:
        from .vivo import evaluar_vivo, markdown as md_vivo
        i = argv.index('--vivo')
        e = json.load(open(argv[i + 1], encoding='utf8')); v = json.load(open(argv[i + 2], encoding='utf8'))
        V = evaluar_vivo(e, v); print(md_vivo(V))
        json.dump(V, open(argv[i + 2].rsplit('.', 1)[0] + '_resultado.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1, default=str)
        return
    if '--cerrar' in argv:
        i = argv.index('--cerrar')
        ruta, partido, real = argv[i + 1], argv[i + 2], json.load(open(argv[i + 3], encoding='utf8'))
        cierres = json.load(open(argv[i + 4], encoding='utf8')) if len(argv) > i + 4 and not argv[i + 4].startswith('--') else None
        rp = argv[argv.index('--partidos') + 1] if '--partidos' in argv else None   # por defecto datos/partidos.csv
        ref = json.load(open(argv[argv.index('--referencia') + 1], encoding='utf8')) if '--referencia' in argv else None
        ok, sin = registro.cerrar(ruta, partido, real, cierres, referencia=ref, ruta_partidos=rp)
        print(f'{ok} líneas calificadas; {sin} sin dato para calificar (faltan esas estadísticas en real.json)'); return
    from .analizar import analizar
    from .reporte import markdown
    ruta = argv[0]
    e = json.load(open(ruta, encoding='utf8'))
    A = analizar(e, devolver_sim=True)
    S = A.pop('_S')
    if e.get('combos'):   # combos con la cuota del cupón dentro de la entrada: [{"nombre", "patas", "cuota"}]
        from .combos import evaluar as ev_combo, cartera
        A['combos'] = []
        for c in e['combos']:
            r = ev_combo(A, S, c['patas'], c.get('cuota'), c.get('nombre'))
            r['_sels'] = [x['sel'] for x in A['lineas'] if x['seleccion'] in r.get('patas', [])]
            r['apostado'], r['stake'] = bool(c.get('apostado')), c.get('stake', '')
            A['combos'].append(r)
        A['cartera'] = cartera(A['combos'])
        for r in A['combos']:
            r.pop('_sels', None)
    base = os.path.splitext(ruta)[0]
    open(base + '_informe.md', 'w', encoding='utf8').write(markdown(A))
    json.dump(A, open(base + '_resultado.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1, default=str)
    try:
        from .reporte_html import html
        open(base + '_informe.html', 'w', encoding='utf8').write(html(A, e))
    except Exception as ex:   # el HTML es un extra: si falla, el análisis sigue
        print(f'(no se pudo generar el HTML: {ex})', file=sys.stderr)
    if '--registro' in argv:
        ap = argv[argv.index('--apostadas') + 1].split(';') if '--apostadas' in argv else ()
        falta = registro.guardar(A, argv[argv.index('--registro') + 1], apostadas=ap, ficha=e.get('ficha'), entrada=e)
        if falta:
            print('Aviso: estas apostadas no coinciden con ninguna selección del informe (no se marcaron): ' + '; '.join(falta),
                  file=sys.stderr)
        for c in A.get('combos') or []:
            if c.get('apostado') and not c.get('error'):
                registro.guardar_combo(argv[argv.index('--registro') + 1], A, c, apostado=True, stake=c.get('stake', ''))
    print(markdown(A))


if __name__ == '__main__':
    main(sys.argv[1:])
