# -*- coding: utf-8 -*-
"""Lectores de cuotas: formato de las plantillas (bt_*.txt, pl_*.txt), formato del kit v1 y JSON propio.
Todos devuelven la misma estructura que usa analizar.py:
  {'lineas': [{'mercado','ambito','linea','mas','menos'}], 'unicos': [...], 'jugadores': [...]}"""
import re

MK_PLANTILLA = {'goals': 'goles', 'corn': 'corners', 'cards': 'tarjetas', 'sh': 'remates', 'sot': 'al_arco',
                'fouls': 'faltas', 'off': 'fueras', 'gk': 'saques_meta', 'ti': 'saques_banda'}
AMB_PLANTILLA = {'tot': 'total', 'C': 'local', 'B': 'visitante', '1H': '1T', '2H': '2T'}
MK_V1 = {'corn': 'corners', 'shots': 'remates', 'sot': 'al_arco', 'fouls': 'faltas', 'yel': 'tarjetas'}
AMB_V1 = {'tot': 'total', 'H': 'local', 'A': 'visitante'}


def desde_plantilla(ruta_bt, ruta_pl=None):
    out = {'lineas': [], 'unicos': [], 'jugadores': []}
    for ln in open(ruta_bt, encoding='utf8'):
        f = ln.strip().split('|')
        if not f or not f[0]:
            continue
        if f[0] == 'T':
            base, amb = f[1].split('_', 1)
            lad = {}
            for tok in f[2].split():
                lado = tok[0]; L, o = tok[1:].split('@')
                lad.setdefault(float(L), [None, None])[0 if lado == 'M' else 1] = float(o)
            for L, (o, u) in sorted(lad.items()):
                out['lineas'].append(dict(mercado=MK_PLANTILLA[base], ambito=AMB_PLANTILLA[amb], linea=L, mas=o, menos=u))
        elif f[0] == 'O':
            ops = dict((x.rsplit('@', 1)[0], float(x.rsplit('@', 1)[1])) for x in re.findall(r'(\S.*?@[\d.]+)(?=\s|$)', f[2]))
            if f[1] == '1X2':
                out['unicos'].append(dict(mercado='resultado', opciones={'1': ops['1'], 'X': ops['Empate'], '2': ops['2']}))
            elif f[1] == 'BTTS':
                out['unicos'].append(dict(mercado='ambos', opciones={'si': ops['Sí'], 'no': ops['No']}))
            elif f[1] in ('more_cards', 'more_corn'):
                st = 'tarjetas' if f[1] == 'more_cards' else 'corners'
                o = {'local': ops.get('1'), 'visitante': ops.get('2')}
                if 'X' in ops or 'Empate' in ops:
                    o['empate'] = ops.get('X', ops.get('Empate'))
                out['unicos'].append(dict(mercado='mas_que', stat=st, opciones=o))
            elif f[1] == 'both_2card':
                out['unicos'].append(dict(mercado='ambos_n_tarjetas', n=2, opciones={'si': ops['Sí'], 'no': ops['No']}))
    if ruta_pl:
        stat = {'SH': 'remates', 'SOT': 'al_arco', 'FC': 'faltas', 'TK': 'entradas', 'SV': 'atajadas'}
        for ln in open(ruta_pl, encoding='utf8'):
            f = ln.rstrip('\n').split('|')
            if f[0] != 'P':
                continue
            nom, lado = f[1], ('local' if f[2] == 'H' else 'visitante')
            for fld in f[3:]:
                if '=' not in fld:
                    continue
                k, v = fld.split('=', 1)
                if k in stat:
                    esc = {int(x.split('+@')[0]): float(x.split('@')[1]) for x in v.split()}
                    out['jugadores'].append(dict(jugador=nom, lado=lado, stat=stat[k], escalera=esc))
                elif k in ('G', 'GA', 'CARD'):
                    st = {'G': 'anota', 'GA': 'anota_o_asiste', 'CARD': 'tarjeta'}[k]
                    out['jugadores'].append(dict(jugador=nom, lado=lado, stat=st, cuota=float(v)))
    return out


def desde_kit_v1(escaleras):
    """escaleras = {'stat|scope': [[linea, mas, menos], ...]} (ladders_5nov.json)"""
    out = {'lineas': [], 'unicos': [], 'jugadores': []}
    for clave, filas in escaleras.items():
        s, sc = clave.split('|')
        for L, o, u in filas:
            out['lineas'].append(dict(mercado=MK_V1[s], ambito=AMB_V1[sc], linea=L, mas=o, menos=u))
    return out
