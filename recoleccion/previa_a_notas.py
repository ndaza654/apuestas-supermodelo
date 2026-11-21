#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Completa `notas/<clave>.json` con la previa que Flashscore publica en la página del partido (jornadas/<día>/paginas/<clave>.txt) y las bajas de
`alineaciones/<clave>.json`. Solo hechos leídos y atribuidos a Flashscore; no se inventa motivación. Uso: python3 recoleccion/previa_a_notas.py jornadas/AAAA-MM-DD [HH:MM]"""
import sys, os, re, json, glob


def bloques(txt):
    L = [x.strip() for x in txt.split('\n')]
    if 'FLASHSCORE PREVIEW' not in L:
        return None
    i = L.index('FLASHSCORE PREVIEW') + 1
    out, cur, sec = {}, [], 'intro'
    heads = ('Match News and Current Form', 'Head-to-Head History', 'Win Probability', 'Hot Stats and Streaks', 'Predicted Lineups', 'Predicted lineups')
    for x in L[i:]:
        if x in heads:
            out[sec] = [p for p in cur if p]
            sec, cur = x, []
        elif re.match(r'^(Advertisement|SHOW MORE|MATCH|ODDS|H2H|Opta by StatsPerform)$', x) or x.startswith('Odds '):
            continue
        else:
            cur.append(x)
        if len(out) > 6:
            break
    out[sec] = [p for p in cur if p]
    return out


def main(dia, hora):
    for f in sorted(glob.glob(f'{dia}/paginas/*.txt')):
        k = os.path.basename(f)[:-4]
        pn = f'{dia}/notas/{k}.json'
        if not os.path.exists(pn):
            continue
        n = json.load(open(pn, encoding='utf8'))
        b = bloques(open(f, encoding='utf8').read())
        src = f'Flashscore, previa y alineaciones del partido (leído 21-nov ~{hora} Bogotá)'
        partes = []
        if b:
            intro = ' '.join(b.get('intro', []))[:420]
            if intro:
                partes.append('Previa de Flashscore: ' + intro)
            hot = [p for p in b.get('Hot Stats and Streaks', []) if len(p) > 25][:3]
            if hot:
                partes.append('Datos destacados (Flashscore): ' + ' '.join(hot))
            mn = [p for p in b.get('Match News and Current Form', []) if len(p) > 60]
            for rol, p in zip(('local', 'visitante'), mn[:2]):
                n.setdefault(rol, {})
                prev = n[rol].get('animo', '')
                n[rol]['animo'] = (prev + ' ' if prev else '') + 'Previa Flashscore: ' + p[:520]
            n['previa'] = {'intro': b.get('intro', []), 'h2h': b.get('Head-to-Head History', []), 'datos': b.get('Hot Stats and Streaks', [])}
        else:
            partes.append('Flashscore no publicó previa de este partido (situación sin leer).')
        pa = f'{dia}/alineaciones/{k}.json'
        if os.path.exists(pa):
            a = json.load(open(pa, encoding='utf8'))
            for rol, lado in (('local', 'L'), ('visitante', 'V')):
                bj = a.get('bajas', {}).get(lado) or []
                if bj:
                    n.setdefault(rol, {})
                    n[rol]['animo'] = (n[rol].get('animo', '') + ' ' if n[rol].get('animo') else '') + 'Bajas según Flashscore: ' + ', '.join(f'{x[0]} ({x[2]})' for x in bj) + '.'
            n['onces'] = (a.get('tipo') or 'Alineaciones') + ' de Flashscore (pestaña Lineups), leído ~' + hora + ' Bogotá.'
        if partes:
            n['se_juega'] = (n.get('se_juega', '') + ' ' + ' '.join(partes)).strip()
        fu = n.setdefault('fuentes', [])
        if src not in fu:
            fu.append(src)
        json.dump(n, open(pn, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        print(k, '| previa' if b else '| sin previa', '|', len(n.get('se_juega', '')))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '07:45')
