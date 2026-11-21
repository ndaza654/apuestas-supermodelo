# -*- coding: utf-8 -*-
"""Marca `apostada = Sí` en registro/lineas.csv para las patas de los boletos del usuario (balance).

    python3 recoleccion/marcar_apostadas.py <apostadas.json>
apostadas.json = [{"boleto": 133, "jornada": "2026-11-20", "partido": "<como en lineas.csv>", "mercado": "goles|corners|...|jugador:al_arco", "ambito": "total|local|visitante",
                   "jugador": "", "linea": "1.5", "lado": "Más|Menos"}, ...]
Imprime las patas que NO encontró en lineas.csv (la línea cambió entre la apuesta y la lectura): esas se califican con la marca de Betano (patas_calificadas.json)."""
import csv, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(arch):
    P = json.load(open(arch, encoding='utf-8'))
    ruta = os.path.join(RAIZ, 'registro', 'lineas.csv')
    with open(ruta, encoding='utf-8-sig', newline='') as f:
        rd = csv.DictReader(f, delimiter=';'); cols = rd.fieldnames; R = list(rd)
    falta = []
    for p in P:
        hit = [r for r in R if r['jornada'] == p['jornada'] and r['partido'] == p['partido'] and r['mercado'] == p['mercado'] and r['ambito'] == p['ambito']
               and (r['jugador'] or '') == (p.get('jugador') or '') and r['linea'] == str(p['linea']) and r['lado'] == p['lado']]
        if not hit:
            falta.append(p); continue
        for r in hit:
            r['apostada'] = 'Sí'
    with open(ruta, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter=';'); w.writeheader(); w.writerows(R)
    print(len(P) - len(falta), 'patas marcadas;', len(falta), 'sin fila:')
    for p in falta:
        print('  ', p)


if __name__ == '__main__':
    main(sys.argv[1])
