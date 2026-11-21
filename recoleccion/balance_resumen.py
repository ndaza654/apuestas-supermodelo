# -*- coding: utf-8 -*-
"""Cifras para las conclusiones de un balance: calibración del modelo, acierto de «cumple», por mercado/lado, sugerencias y boletos.

    python3 recoleccion/balance_resumen.py <jornada>[,<jornada2>] <carpeta_balance>
Solo lectura de registro/lineas.csv, registro/sugerencias.csv y <carpeta>/boletos_betano.json + patas_calificadas.json. Imprime texto para pegar en conclusiones.html."""
import csv, json, os, sys, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main(jors, carpeta):
    jors = jors.split(',')
    L = [r for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';') if r['jornada'] in jors]
    res = [r for r in L if r['resultado'] in ('cumplió', 'falló')]
    print('líneas', len(L), '· resueltas', len(res), '· nulas', sum(r['resultado'] == 'nula' for r in L), '· sin resultado', sum(r['resultado'] == '' for r in L))
    for ambito, etq in (('equipo', lambda r: not r['jugador']), ('jugador', lambda r: bool(r['jugador']))):
        S = [r for r in res if etq(r)]
        print(f'\n== {ambito}: {len(S)} resueltas, acierto {sum(r["resultado"] == "cumplió" for r in S) / max(1, len(S)):.1%}')
        if ambito == 'equipo':
            for c in ('sí', 'no'):
                T = [r for r in S if r['cumple_ficha'] == c]
                print(f'  cumple={c}: {sum(r["resultado"] == "cumplió" for r in T)}/{len(T)} = {sum(r["resultado"] == "cumplió" for r in T) / max(1, len(T)):.1%}')
            g = collections.defaultdict(lambda: [0, 0])
            for r in S:
                if r['cumple_ficha'] == 'sí':
                    k = (r['mercado'], r['lado']); g[k][1] += 1; g[k][0] += r['resultado'] == 'cumplió'
            print('  cumple=sí por mercado-lado:', {k: f'{a}/{b}' for k, (a, b) in sorted(g.items()) if b >= 15})
        bins = [(0, .35), (.35, .5), (.5, .65), (.65, .8), (.8, 1.01)]
        for a, b in bins:
            T = [r for r in S if f(r['p_modelo']) is not None and a <= f(r['p_modelo']) < b]
            if T:
                real = sum(r['resultado'] == 'cumplió' for r in T) / len(T); pm = sum(f(r['p_modelo']) for r in T) / len(T)
                print(f'  p modelo {a:.0%}–{min(b, 1):.0%}: n={len(T)} modelo {pm:.1%} real {real:.1%} ({(real - pm) * 100:+.1f} pts)')
    for et, fl in (('apostadas por ti', lambda r: r['apostada'] == 'Sí'),):
        T = [r for r in res if fl(r)]
        print(f'\n{et}: {sum(r["resultado"] == "cumplió" for r in T)}/{len(T)} patas')
        for c in ('sí', 'no'):
            U = [r for r in T if r['cumple_ficha'] == c]
            print(f'  cumple={c}: {sum(r["resultado"] == "cumplió" for r in U)}/{len(U)}')
    S = [r for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'sugerencias.csv'), encoding='utf-8-sig'), delimiter=';') if r['fecha_entrega'] in jors]
    c = collections.Counter((r['tipo'], r['resultado']) for r in S)
    print('\nsugerencias:', dict(c))


if __name__ == '__main__':
    main(*sys.argv[1:3])
