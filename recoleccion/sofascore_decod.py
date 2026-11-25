# -*- coding: utf-8 -*-
"""Pasa lo que emite `sfExportar()` de sofascore_extraer.js a los archivos de la jornada (fuente principal de equipo y jugadores desde el 25-nov-2026;
Flashscore/ESPN/Opta quedan de respaldo y de contraste).
Uso: python3 recoleccion/sofascore_decod.py jornadas/AAAA-MM-DD <export.json>
Escribe, por partido sin error:
  sofascore/<clave>.json              forma (10+10) y h2h con el MISMO formato que flashscore/<clave>.json, + árbitro, estadio, once y ausentes
  jugadores_sofascore/<clave>.json    historial por jugador (filas: las 13 de jugadores_decod + faltas_recibidas, centros, xA, rating), nombres «Apellido I.»
  alineaciones_sofascore/<clave>.json once probable/oficial y ausentes con la forma de alineaciones/<clave>.json de Flashscore
  sofascore/LEEME.md y sofascore/contraste.json  cobertura real, qué faltó y cuánto difiere de Flashscore en los partidos que ambos traen
Nada se inventa: lo que Sofascore no devolvió queda vacío y se declara."""
import sys, os, json, re, unicodedata

PARTICULAS = {'van', 'de', 'da', 'dos', 'das', 'do', 'von', 'del', 'di', 'le', 'la', 'el', 'al', 'bin', 'ten', 'ter', 'der', 'den', 'du', 'des', 'zu', 'af', 'op'}
CLAVES_CONTRASTE = ['c', 'sh', 'sot', 'f', 'off', 'ti', 'gk', 'y']


def corto(nombre):
    """«Hervé Koffi» → «Koffi H.»; «Jan Paul van Hecke» → «van Hecke J.» (formato de Flashscore, el que entiende armar_entrada.coincide)."""
    t = (nombre or '').replace('.', ' ').split()
    if len(t) <= 1:
        return nombre or ''
    k = len(t) - 1
    while k > 1 and t[k - 1].lower() in PARTICULAS:
        k -= 1
    return ' '.join(t[k:]) + ' ' + t[0][0] + '.'


def jugadores_flat(q):
    out = {}
    for lado in ('local', 'visitante'):
        for nombre, d in (q.get('jugadores', {}).get(lado) or {}).items():
            k = corto(nombre)
            n = 2
            while k in out and out[k]['pid'] != d['pid']:
                k = f'{corto(nombre)} #{n}'
                n += 1
            out[k] = {'lado': d['lado'], 'pos': d['pos'], 'pid': 's' + str(d['pid']), 'nombre': nombre, 'p': d['p']}
    return out


def alineacion_flashscore(q):
    """alineacion de Sofascore → forma de alineaciones/<clave>.json (probables L/V = [nombre, num, pid, es_portero]; bajas = [nombre, pid, motivo])."""
    a = q.get('alineacion')
    if not a or not a['local']['xi']:
        return None
    pr = lambda l: [[corto(n), '', 's' + pid, 1 if pos == 'G' else 0] for n, pid, pos in l['xi']]
    ba = lambda l: [[corto(n), 's' + pid, ('duda' if tipo == 'doubtful' else 'baja') + (f' (Sofascore: {razon})' if razon else '')] for n, pid, tipo, razon in l['ausentes']]
    return {'mid': q.get('mid'), 'tipo': 'Alineaciones ' + ('oficiales' if a['confirmada'] else 'probables') + ' (Sofascore)',
            'lectura_utc': (a.get('leida') or '')[:16] + 'Z', 'probables': {'L': pr(a['local']), 'V': pr(a['visitante'])},
            'bajas': {'L': ba(a['local']), 'V': ba(a['visitante'])}, 'formacion': {'L': a['local']['formacion'], 'V': a['visitante']['formacion']},
            'fuente': 'Sofascore /api/v1/event/<id>/lineups'}


def contraste(sofa, fs):
    """Compara, por (fecha, marcador), los partidos que traen Sofascore y Flashscore: diferencias absolutas en cada estadística común."""
    res = {'partidos_comunes': 0, 'celdas': 0, 'iguales': 0, 'dif_1': 0, 'dif_mayor': 0, 'mayores': []}
    for lado in ('local', 'visitante'):
        idx = {(e['fecha'], tuple(e['g'])): e for e in (fs.get('forma') or {}).get(lado, [])}
        for e in sofa['forma'][lado]:
            o = idx.get((e['fecha'], tuple(e['g'])))
            if not o:
                continue
            res['partidos_comunes'] += 1
            for k in CLAVES_CONTRASTE:
                a, b = e['stats'].get(k), o['stats'].get(k)
                if not a or not b:
                    continue
                for i in (0, 1):
                    res['celdas'] += 1
                    d = abs(a[i] - b[i])
                    if d == 0:
                        res['iguales'] += 1
                    elif d <= 1:
                        res['dif_1'] += 1
                    else:
                        res['dif_mayor'] += 1
                        res['mayores'].append(f"{e['fecha']} {e['rival']} {k}[{i}] Sofascore {a[i]} · Flashscore {b[i]}")
    return res


def main(jor, export):
    q = json.load(open(export, encoding='utf8'))
    Q = q['Q']
    for d in ('sofascore', 'jugadores_sofascore', 'alineaciones_sofascore'):
        os.makedirs(os.path.join(jor, d), exist_ok=True)
    filas, ctr = [], {}
    for clave, d in sorted(Q.items()):
        if d.get('error'):
            filas.append(f"| {clave} | — | — | — | — | {d['error']} |")
            continue
        sal = {k: v for k, v in d.items() if k != 'jugadores'}
        jug = jugadores_flat(d)
        sal['jugadores_n'] = len(jug)
        json.dump(sal, open(os.path.join(jor, 'sofascore', clave + '.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
        json.dump(jug, open(os.path.join(jor, 'jugadores_sofascore', clave + '.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
        al = alineacion_flashscore(d)
        if al:
            json.dump(al, open(os.path.join(jor, 'alineaciones_sofascore', clave + '.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
        fsf = os.path.join(jor, 'flashscore', clave + '.json')
        if os.path.exists(fsf):
            ctr[clave] = contraste(d, json.load(open(fsf, encoding='utf8')))
        nl, nv = len(d['forma']['local']), len(d['forma']['visitante'])
        sin_st = sum(1 for l in ('local', 'visitante') for e in d['forma'][l] if not e['stats'])
        c = ctr.get(clave)
        filas.append(f"| {clave} | {nl}/{nv} | {len(d['h2h'])} | {len([1 for j in jug.values() if len(j['p']) >= 5])}/{len(jug)} | "
                     f"{'oficial' if d.get('alineacion', {}).get('confirmada') else ('probable' if d.get('alineacion') else 'sin publicar')} · árbitro {d['arbitro'] or 'sin anunciar'} | "
                     + (f"contraste {c['iguales']}/{c['celdas']} iguales, {c['dif_mayor']} con diferencia > 1" if c else 'sin Flashscore para contrastar')
                     + (f"; {sin_st} partidos sin estadísticas" if sin_st else '') + ' |')
    json.dump(ctr, open(os.path.join(jor, 'sofascore', 'contraste.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    L = ['# Sofascore — cobertura de la recolección', '',
         f"Fuente: Sofascore `/api/v1` desde una pestaña de www.sofascore.com · generado {q.get('generado', '')[:16]}Z · partidos oficiales terminados, últimos 10 de cada equipo.", '',
         '| partido | forma L/V | directos | jugadores con ≥5 apariciones / total | once · árbitro | contraste con Flashscore |', '|---|---|---|---|---|---|'] + filas
    L += ['', '**Límites que se declaran:** API no oficial de Sofascore (puede cambiar o bloquear); el marcador y los datos de jugadores de Betano se liquidan con Opta, que no es esta fuente;',
          'el árbitro viene de Sofascore (ficha corta: partidos, amarillas, rojas): las faltas por partido del árbitro siguen en ValueStats; «entradas» = entradas totales y ganadas de Sofascore (Betano cuenta totales);',
          'las tarjetas por jugador salen de los incidentes del partido; una fila de jugador solo existe si jugó minutos. Diferencias > 1 con Flashscore se listan en `contraste.json`.']
    open(os.path.join(jor, 'sofascore', 'LEEME.md'), 'w', encoding='utf8').write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
