#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Completa `notas/<clave>.json` con lo que la página del partido en Flashscore trae como HECHOS: bajas y dudas (bloques «WILL NOT PLAY» y
«QUESTIONABLE», sin los «Off the roster»), once probable (aviso) y, si existe `previa_resumen.json` (lo escribe Claude PARAFRASEANDO la previa,
nunca copiándola), las marcas de situación y los datos de la previa que importan al mercado.

Uso: python3 recoleccion/notas_previa.py jornadas/AAAA-MM-DD
previa_resumen.json: {"<clave>": {"previa": "texto propio y corto", "bajas_clave": "quién y de qué equipo, solo lo leído",
                       "local": {"necesita_ganar": true, "le_sirve_empate": false, "rotacion": false}, "visitante": {...},
                       "importancia": "alta|normal|baja", "decisivo": false}}
Solo suma; no pisa lo que paginas_a_notas.py ya dejó (tabla, forma, árbitro)."""
import sys, os, re, json, glob


def bajas(txt):
    L = [x.strip() for x in txt.split('\n') if x.strip()]
    out = {'no_juega': [], 'duda': []}
    for clave, tag in (('WILL NOT PLAY', 'no_juega'), ('QUESTIONABLE', 'duda')):
        if clave not in L:
            continue
        i = L.index(clave) + 1
        while i + 1 < len(L) and L[i] not in ('QUESTIONABLE', 'COACHES', 'TV CHANNEL', 'MATCH INFORMATION'):
            nom, mot = L[i], L[i + 1]
            if mot not in ('QUESTIONABLE', 'COACHES'):
                if mot.lower() != 'off the roster':
                    out[tag].append(f'{nom} ({mot})')
                i += 2
            else:
                i += 1
    return out


def main(dia):
    res = {}
    rp = os.path.join(dia, 'previa_resumen.json')
    if os.path.exists(rp):
        res = json.load(open(rp, encoding='utf8'))
    for f in sorted(glob.glob(f'{dia}/paginas/*.txt')):
        k = os.path.basename(f)[:-4]
        npth = f'{dia}/notas/{k}.json'
        if not os.path.exists(npth):
            continue
        n = json.load(open(npth, encoding='utf8'))
        txt = open(f, encoding='utf8').read()
        b = bajas(txt)
        if b['no_juega'] or b['duda']:
            partes = []
            if b['no_juega']:
                partes.append('No juegan (Flashscore): ' + '; '.join(b['no_juega']))
            if b['duda']:
                partes.append('Dudas: ' + '; '.join(b['duda']))
            n['bajas_flashscore'] = ' · '.join(partes) + '. (La lista junta a los dos equipos.)'
        else:
            n['bajas_flashscore'] = 'Flashscore no publicó lista de bajas para este partido (sin leer).'
        n['onces'] = 'Once probable/oficial: sin publicar todavía (oficial ~1 h antes); releer entonces.' if 'PREDICTED LINEUPS' not in txt else 'Once PROBABLE de Flashscore leído; el oficial sale ~1 h antes del partido.'
        r = res.get(k)
        if r:
            for c in ('importancia', 'decisivo', 'derbi', 'nada_en_juego'):
                if c in r:
                    n[c] = r[c]
            if r.get('previa'):
                n['se_juega'] = (n.get('se_juega', '') + ' Previa (resumen propio de lo leído en Flashscore): ' + r['previa']).strip()
            if r.get('bajas_clave'):
                n['bajas_clave'] = r['bajas_clave']
            for rol in ('local', 'visitante'):
                if r.get(rol):
                    n.setdefault(rol, {}).update(r[rol])
        n.setdefault('fuentes', []).append('Flashscore previa y bajas (misma lectura)')
        json.dump(n, open(npth, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        print(k, len(b['no_juega']), 'bajas', len(b['duda']), 'dudas', 'previa' if r else '-')


if __name__ == '__main__':
    main(sys.argv[1])
