# -*- coding: utf-8 -*-
"""Informe individual en HTML (formato de los informes del 9-nov + la hoja de partido de Toulouse–Estrasburgo).

Secciones: veredicto (líneas con valor, builder, jugadores y riesgo, lo que no haría) · lectura y alineaciones · proyección
del partido (media esperada del modelo contra lo que espera Betano) · boletos · guiones · mejores líneas de jugador ·
mercados con la «media esperada» en cada bloque (goles, córners, tarjetas, remates, faltas, saques) · resultado y
especiales · jugadores · contexto · límites.

Todo sale del análisis. Lo que el chat escriba a mano va opcional en la entrada bajo "informe": {...} (veredicto, accion,
chips, lectura, boletos, tabla, formas, h2h, datos, evitar, limites, checklist, notas, alineaciones, jugadores_notas,
acento). Con historial en la entrada, el informe suma las columnas que lo necesitan:
  · "forma": {"local": [partidos], "visitante": [partidos]} (mismo formato que perfiles.py) → a favor / en contra y
    «veces que salió Más»;
  · "jugadores_hist": {"Nombre": {"pos": "...", "partidos": [{"min": 90, "remates": 2, "al_arco": 1, ...}]}} → por 90′,
    histórico de 60′ o más y barras.
La probabilidad que se usa para decidir es la de decisión del modelo (50 % simulación + 50 % mercado sin margen, más el
contexto). Tema claro fijo (como en los informes anteriores).
"""
import html as _html
import re
from . import config as C
from . import proyeccion as PR

CSS = """
:root{color-scheme:light;--bg:#fbfbf8;--panel:#fff;--ink:#1d2420;--mute:#5f6b64;--line:#e1e5e0;--soft:#f2f4f0;--acc:#1f5f4a;--accs:#e6f1ec;--pos:#13784a;--neg:#a23c3c;--negs:#fbecec;--poss:#e9f5ee;--warn:#8a6a12;--warns:#fbf3dc;--neu:#8a6a12;--risk:#b5531a;
--fd:"Barlow Condensed","Arial Narrow",sans-serif;--fb:"IBM Plex Sans",system-ui,sans-serif;--fm:"IBM Plex Mono",ui-monospace,monospace}
html,body{background:var(--bg);color:var(--ink)} body{font-family:var(--fb);font-size:14px;line-height:1.55;margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-block:22px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:28px}
table.tp td:first-child{min-width:230px}
h3.sub3{margin:18px 0 8px}
h1,h2,h3,h4,h5{font-family:var(--fd);margin:0;text-wrap:balance;letter-spacing:.01em}
h1{font-size:clamp(30px,6vw,50px);text-transform:uppercase;line-height:1} h2{font-size:26px;text-transform:uppercase} h3{font-size:19px;text-transform:uppercase;color:var(--acc)}
h5{font-size:14px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute)}
.eyebrow{font-family:var(--fm);font-size:12px;color:var(--mute);letter-spacing:.02em}
.hero{background:var(--accs);border:1px solid var(--line);border-top:6px solid var(--acc);border-radius:6px;padding:20px;display:flex;flex-direction:column;gap:12px}
.hero p{margin:0;max-width:82ch}
.meta{display:flex;flex-wrap:wrap;gap:6px 18px;color:var(--mute);font-size:13px} .meta b{color:var(--ink);font-weight:600}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-family:var(--fm);font-size:11.5px;padding:2px 8px;border-radius:3px;border:1px solid var(--line);background:var(--panel);color:var(--ink);white-space:nowrap}
.chip.g{background:var(--poss);border-color:#bfe0cd;color:var(--pos)} .chip.r{background:var(--negs);border-color:#ecc7c7;color:var(--neg)} .chip.y{background:var(--warns);border-color:#e8d9a6;color:var(--warn)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:10px 12px;min-width:0}
.kpi span{display:block;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mute)}
.kpi b{font-family:var(--fm);font-size:20px;font-weight:500} .kpi small{display:block;color:var(--mute);font-size:12px}
.pos{color:var(--pos)} .neg{color:var(--neg)} .mute{color:var(--mute)}
section{display:flex;flex-direction:column;gap:12px}
.box{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:16px 18px;min-width:0}
.box.key{border-left:5px solid var(--acc)} .box.warn{border-left:5px solid var(--warn);background:var(--warns)}
.box.main{border-top:4px solid var(--acc)} .box.risk{border-top:4px solid var(--risk)} .box.risk h3{color:var(--risk)}
.box ol,.box ul{margin:8px 0 0;padding-left:20px} .box li{margin-bottom:7px}
.box p{margin:6px 0 0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px} .grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.verdict{display:grid;grid-template-columns:1.25fr 1fr;gap:18px} .col{display:flex;flex-direction:column;gap:18px;min-width:0}
@media(max-width:900px){.grid2,.grid3,.verdict{grid-template-columns:1fr}}
.bb{list-style:none;padding:0;margin:10px 0 0;display:flex;flex-direction:column;gap:10px}
.box ul.bb{padding-left:0}
.bb li{display:grid;grid-template-columns:1fr auto;gap:2px 12px;padding-bottom:10px;border-bottom:1px dashed var(--line);margin:0}
.bb li:last-child{border-bottom:0;padding-bottom:0}
.bb li p{grid-column:1/-1;margin:0;color:var(--mute);font-size:13px} .bb .o{font-family:var(--fm);font-weight:500;font-size:16px}
.tot{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:12px;font-family:var(--fm);font-size:13px;color:var(--mute)} .tot b{font-size:17px;color:var(--acc)}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:6px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums} caption{text-align:left;padding:8px 10px;font-family:var(--fd);font-size:16px;text-transform:uppercase;color:var(--acc)}
th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
thead th{font-family:var(--fd);font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--mute);background:var(--soft);white-space:nowrap}
td.n,td.num{font-family:var(--fm);white-space:nowrap;font-size:13px} td.s{font-size:13px;min-width:170px} td.l{font-size:12px;color:var(--mute);min-width:150px}
tr.sub th{background:var(--accs);font-family:var(--fd);font-size:16px;color:var(--ink);text-transform:uppercase;letter-spacing:.02em}
tr.sub .mu{font-family:var(--fm);font-size:12px;color:var(--mute);text-transform:none;margin-left:8px;letter-spacing:0}
td.ln{font-family:var(--fm);white-space:nowrap;font-weight:500} td.side{white-space:nowrap;font-family:var(--fm);font-size:12.5px} td.side b{font-size:14px} td.side small{display:block;color:var(--mute);font-size:11px}
td.hist{font-family:var(--fm);font-size:11.5px;color:var(--mute);min-width:150px} td.note{min-width:260px;max-width:460px;font-size:13px}
.ev{font-family:var(--fm);font-weight:500} .ev.pos{color:var(--pos)} .ev.neg{color:var(--neg)} .ev.neu{color:var(--neu)}
.cp{display:inline-block;font-family:var(--fd);font-size:12px;text-transform:uppercase;letter-spacing:.05em;padding:0 6px;border-radius:3px;margin-left:4px;white-space:nowrap}
.cp.valor{background:var(--pos);color:#fff} .cp.riesgo{background:#fbe6d6;color:var(--risk);border:1px solid #efc3a2} .cp.justa{border:1px solid var(--line);color:var(--mute)} .cp.dud{border:1px solid #e3cf95;color:var(--neu)} .cp.no{color:var(--neg);border:1px solid var(--line)}
tr.good td:first-child{border-left:4px solid var(--pos)} tr.bad td:first-child{border-left:4px solid var(--neg)} tr.mid td:first-child{border-left:4px solid var(--warn)}
tr.me td{background:var(--accs);font-weight:500}
.filter{display:flex;gap:10px;align-items:center;font-size:13px;color:var(--mute)}
body.only table.mk tr:not([data-v]):not(.sub){display:none}
.tk{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px;display:flex;flex-direction:column;gap:10px;min-width:0}
.tk.win{border-top:4px solid var(--pos)} .tk.mid{border-top:4px solid var(--warn)} .tk.lose{border-top:4px solid var(--neg)}
.tk header{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start;justify-content:space-between}
.tk h4{font-size:20px;text-transform:uppercase} .tk .sub{margin:0;font-size:12.5px;color:var(--mute)}
.legs{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:4px}
.legs li{font-family:var(--fm);font-size:13px;padding:4px 8px;background:var(--soft);border-radius:4px}
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(105px,1fr));gap:8px}
.nums div{background:var(--soft);border-radius:4px;padding:6px 8px} .nums span{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--mute)} .nums b{font-family:var(--fm);font-weight:500;font-size:16px}
.tk p{margin:0;font-size:13px}
.bars{display:flex;flex-direction:column;gap:7px}
.bar{display:grid;grid-template-columns:minmax(120px,300px) 1fr 52px;gap:10px;align-items:center;font-size:13px}
.bar i{display:block;height:9px;background:var(--acc);border-radius:5px} .bar div{background:var(--soft);border-radius:5px;overflow:hidden} .bar b{font-family:var(--fm);font-weight:500;text-align:right}
@media(max-width:560px){.bar{grid-template-columns:1fr 52px}.bar div{grid-column:1/-1;order:3}}
details{background:var(--panel);border:1px solid var(--line);border-radius:6px}
details>summary{cursor:pointer;padding:10px 14px;font-family:var(--fd);font-size:17px;text-transform:uppercase;color:var(--acc);list-style:revert}
nav.jump{display:flex;flex-wrap:wrap;gap:6px} nav.jump a{font-family:var(--fd);text-transform:uppercase;font-size:14px;color:var(--ink);text-decoration:none;border:1px solid var(--line);padding:3px 10px;border-radius:3px;background:var(--panel)}
nav.jump a:hover,nav.jump a:focus-visible{border-color:var(--acc);outline:none}
.method{color:var(--mute);font-size:13px;max-width:82ch;margin:0}
.res{display:inline-block;width:20px;text-align:center;font-family:var(--fm);font-size:12px;border-radius:3px;color:#fff}
.res.G{background:var(--pos)} .res.E{background:#8a8f8c} .res.P{background:var(--neg)}
.lineups{display:grid;grid-template-columns:1fr 1fr;gap:18px} @media(max-width:700px){.lineups{grid-template-columns:1fr}}
.lineups p{margin:6px 0 0;font-size:13px} .muted{color:var(--mute)}
.pls{display:grid;grid-template-columns:repeat(auto-fill,minmax(520px,1fr));gap:14px} @media(max-width:520px){.pls{grid-template-columns:1fr}}
.pl{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px;display:flex;flex-direction:column;gap:10px;min-width:0}
.pl header{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline} .pl h4{font-size:20px;text-transform:uppercase}
.pl .ps{font-family:var(--fd);font-size:13px;text-transform:uppercase;color:var(--acc)} .pl .min{font-size:12px;color:var(--mute);width:100%}
.rates{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.rates div{background:var(--soft);border-radius:4px;padding:6px 8px;display:flex;flex-wrap:wrap;gap:0 4px;align-items:baseline}
.rates span{width:100%;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--mute)}
.rates b{font-family:var(--fm);font-size:13px;font-weight:500} .rates strong{font-family:var(--fm);font-size:15px;color:var(--acc)} .rates em{font-style:normal;font-size:11px;color:var(--mute)}
.hits{display:flex;flex-direction:column;gap:4px;font-family:var(--fm);font-size:12px} .hits .hl{margin:0;font-family:var(--fb);font-size:12px;color:var(--mute)}
.hits div{display:flex;gap:4px;align-items:center;flex-wrap:wrap} .hits span{width:104px;color:var(--mute);font-family:var(--fb);font-size:11.5px}
.hits i{font-style:normal;display:inline-flex;gap:4px;padding:1px 6px;border-radius:3px;background:linear-gradient(90deg,var(--accs) calc(var(--f)*100%),var(--soft) 0);border:1px solid var(--line)}
.hits i em{font-style:normal;color:var(--mute)}
.pnote{margin:0;font-size:13px;border-left:3px solid var(--acc);padding-left:8px}
table.pt td,table.pt th{padding:5px 6px;font-size:12px} table.pt td{font-family:var(--fm)} table.pt thead th{white-space:normal;font-size:12px} table.pt tr.hl td{background:#f3faf5}
.lbs{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
.lb{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:12px} .lb ol{margin:6px 0 0;padding-left:18px} .lb li{font-size:13px;margin:0} .lb b{font-family:var(--fm);margin-left:6px} .lb em{font-style:normal;color:var(--mute);font-family:var(--fm);font-size:12px;margin-left:6px}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
@media(max-width:520px){.rates{grid-template-columns:repeat(2,minmax(0,1fr))}}
"""

E = _html.escape

MERCADOS_PAR = ('goles', 'corners', 'tarjetas', 'remates', 'al_arco', 'faltas', 'fueras', 'saques_meta', 'saques_banda')
SECCIONES = [('m0', 'Goles', ['goles']), ('m1', 'Córners', ['corners']), ('m2', 'Tarjetas', ['tarjetas']),
             ('m3', 'Remates y tiros al arco', ['remates', 'al_arco']), ('m4', 'Faltas y fueras de lugar', ['faltas', 'fueras']),
             ('m5', 'Saques de meta y de banda', ['saques_meta', 'saques_banda'])]
BASE = {'goles': 'Goles', 'corners': 'Córners', 'tarjetas': 'Tarjetas', 'remates': 'Remates', 'al_arco': 'Tiros al arco',
        'faltas': 'Faltas', 'fueras': 'Fueras de lugar', 'saques_meta': 'Saques de meta', 'saques_banda': 'Saques de banda'}
TOTAL = {'goles': 'Goles del partido', 'corners': 'Córners totales', 'tarjetas': 'Tarjetas totales', 'remates': 'Remates (partido)',
         'al_arco': 'Tiros al arco (partido)', 'faltas': 'Faltas totales', 'fueras': 'Fueras de lugar (partido)',
         'saques_meta': 'Saques de meta (partido)', 'saques_banda': 'Saques de banda (partido)'}
ORDEN_AMB = ['total', 'local', 'visitante', '1T', '2T']


# ------------------------------------------------------------------ utilidades
def pct(x, d=0):
    return '—' if x is None else f'{x * 100:.{d}f} %'


def pc0(x):
    return '—' if x is None else f'{x * 100:.0f}%'


def chip(t, c=''):
    return f'<span class="chip {c}">{E(t)}</span>'


def evs(ev):
    return f"<span class='ev {'pos' if ev >= 0.03 else 'neg' if ev <= -0.03 else 'neu'}'>{ev * 100:+.0f}%</span>"


def veredicto(r):
    """Etiqueta corta de una línea: Valor / Riesgo (cuota ≥ 2.40 con valor) / Frágil / Justa / No."""
    et = r['etiqueta']
    if 'Valor frágil' in et:
        return 'Frágil', 'dud'
    if 'Valor' in et:
        return ('Riesgo', 'riesgo') if r['cuota'] >= 2.40 else ('Valor', 'valor')
    return ('Justa', 'justa') if r['ev'] >= -0.02 else ('No', 'no')


def titulo_grupo(m, a, loc, vis):
    if a == 'total':
        return TOTAL[m]
    return {'local': f'{BASE[m]} {loc}', 'visitante': f'{BASE[m]} {vis}', '1T': f'{BASE[m]} 1er tiempo', '2T': f'{BASE[m]} 2º tiempo'}[a]


def fnum(x, d=1):
    return '—' if x is None else f'{x:.{d}f}'


def rango(x):
    return f'{x:g}'


def f1(x):
    return f'{x:.1f}'


def indice_medias(A):
    return {(r['mercado'], r['ambito']): r for r in A.get('medias') or []}


def pares(L):
    d = {}
    for r in L:
        s = r['sel']
        if s['mercado'] in MERCADOS_PAR and 'linea' in s and s.get('lado') in ('mas', 'menos'):
            d.setdefault((s['mercado'], s.get('ambito', 'total')), {}).setdefault(s['linea'], {})[s['lado']] = r
    return d


def _notas(D, *rs):
    out = []
    for r in rs:
        if r and (D.get('notas') or {}).get(r['seleccion']):
            out.append(E(D['notas'][r['seleccion']]))
    return out


def texto_valor(r):
    pm = r.get('p_mercado')
    s = f"Prob. {pct(r['p'])}" + (f" (mercado {pct(pm)}, simulación {pct(r.get('p_simulacion'))})" if pm is not None else '')
    s += f" · EV {r['ev'] * 100:+.0f} %. Cuota mínima {r['cuota_minima']:.2f}"
    if r.get('mejor_guion'):
        s += f". Brilla si {r['mejor_guion']}"
    if r.get('peor_guion'):
        s += f"; la mata si {r['peor_guion']}"
    if r.get('movimiento_contexto') and abs(r['movimiento_contexto']) >= 0.03:
        s += f". El contexto la mueve {r['movimiento_contexto'] * 100:+.0f} pts"
    return s + '.'


def lectura_par(m, linea, mas, menos, med, D):
    """Texto de la columna Lectura de una línea con sus dos lados: lo que dice la media esperada y dónde hay valor."""
    out = _notas(D, mas, menos)
    pmas = mas['p'] if mas else (1 - menos['p'] if menos else None)
    if med and pmas is not None:
        mu = med['modelo']
        p_lado = max(pmas, 1 - pmas)
        lado = 'Más' if pmas >= 0.5 else 'Menos'
        if p_lado < 0.56:
            t = f'Media esperada {f1(mu)}, casi sobre la línea: moneda al aire.'
        elif p_lado >= 0.80:
            t = f'La media esperada ({f1(mu)}) queda lejos de {linea:g}: el lado {lado} es casi seguro, paga muy poco y el otro es lotería.'
        else:
            t = f'Media esperada {f1(mu)}: el lado {lado} es el probable.'
        bt = med.get('betano')
        if bt is not None and abs(mu - bt) >= max(0.15, 0.06 * bt):
            t += f' Betano espera {f1(bt)}.'
        out.append(E(t))
    con = [(n, x) for n, x in (('Más', mas), ('Menos', menos)) if x and 'Valor' in x['etiqueta']]
    if con:
        for n, x in con:
            out.append(f"<b>{n}:</b> {E(texto_valor(x))}")
    else:
        out.append('Los dos lados llevan el margen de la casa.')
    for x in (mas, menos):
        if x and x.get('alerta'):
            out.append(f"<span class='neg'>⚠ {E(x['alerta'])}</span>")
            break
    mem = sorted({t for x in (mas, menos) if x for t in (x.get('memoria') or [])})
    if mem:
        out.append(f"<span class='muted'>{E(' · '.join(mem))}</span>")
    return ' '.join(out)


def celda_lado(r):
    if not r:
        return "<td class='side'>—</td>"
    t, c = veredicto(r)
    dev = f" <small>devuelve {r['devolucion'] * 100:.0f}%</small>" if r.get('asiatica') and r.get('devolucion') is not None else ''
    return (f"<td class='side'><b>{r['cuota']:.2f}</b> {pc0(r['p'])} {evs(r['ev'])} <span class='cp {c}'>{t}</span>"
            f"<small>mín. {r['cuota_minima']:.2f} · rob. {pc0(r['robustez'])}</small>{dev}</td>")


def tabla_mercado(A, e, D, mercados, forma, loc, vis):
    P, M = pares(A['lineas']), indice_medias(A)
    grupos = [(m, a) for m in mercados for a in ORDEN_AMB if (m, a) in P]
    if not grupos:
        return ''
    hist_txt = {}
    for m, a in grupos:
        for linea in P[(m, a)]:
            hist_txt[(m, a, linea)] = PR.forma_hits(forma, m, a, linea, loc, vis)
    hay = any(hist_txt.values())
    ncol = 5 if hay else 4
    trs = []
    for m, a in grupos:
        med = M.get((m, a))
        mu = ''
        if med:
            mu = f"media esperada {f1(med['modelo'])}"
            if med.get('betano') is not None:
                mu += f" · Betano {f1(med['betano'])}"
            if med.get('sin_contexto') is not None and abs(med['modelo'] - med['sin_contexto']) >= 0.15:
                mu += f" · sin ficha {f1(med['sin_contexto'])}"
            mu += f" · 80 %: {rango(med['p10'])}–{rango(med['p90'])}"
        trs.append(f"<tr class='sub'><th colspan='{ncol}'>{E(titulo_grupo(m, a, loc, vis))} <span class='mu'>{E(mu)}</span></th></tr>")
        for linea in sorted(P[(m, a)]):
            mas, menos = P[(m, a)][linea].get('mas'), P[(m, a)][linea].get('menos')
            valor = any(x and veredicto(x)[1] in ('valor', 'riesgo') for x in (mas, menos))
            h = f"<td class='hist'>{E(hist_txt[(m, a, linea)] or '—')}</td>" if hay else ''
            trs.append(f"<tr{' data-v' if valor else ''}><td class='ln'>{linea:g}</td>{celda_lado(mas)}{celda_lado(menos)}{h}"
                       f"<td class='note'>{lectura_par(m, linea, mas, menos, med, D)}</td></tr>")
    head = ("<th>Línea</th><th>Más · cuota · prob · EV</th><th>Menos · cuota · prob · EV</th>"
            + ('<th>Veces que salió Más</th>' if hay else '') + '<th>Lectura</th>')
    return f"<div class='tw'><table class='mk'><thead><tr>{head}</tr></thead><tbody>{''.join(trs)}</tbody></table></div>"


def tabla_especiales(A, D):
    rows = []
    for r in A['lineas']:
        if r['sel']['mercado'] not in ('resultado', 'ambos', 'handicap', 'mas_que', 'ambos_n_tarjetas', 'resultado_1t', 'resultado_2t', 'htft_o', 'htft'):
            continue
        pm = r.get('p_mercado')
        if pm is not None and abs(r['p'] - pm) < 0.02:
            t = f"Modelo {pct(r['p'])} = mercado."
        elif pm is not None:
            t = f"Modelo {pct(r['p'])}, mercado {pct(pm)}."
        else:
            t = f"Modelo {pct(r['p'])}."
        t += ' ' + ('Con valor: ' + texto_valor(r) if 'Valor' in r['etiqueta'] else 'Sin valor.')
        nt = ' '.join(_notas(D, r))
        mem = (f" <span class='muted'>{E(' · '.join(r['memoria']))}</span>") if r.get('memoria') else ''
        al = f" <span class='neg'>⚠ {E(r['alerta'])}</span>" if r.get('alerta') else ''
        t_, c_ = veredicto(r)
        rows.append(f"<tr><td>{E(r['seleccion'])}</td><td class='num'><b>{r['cuota']:.2f}</b></td><td class='num'>{pc0(r['p'])}</td>"
                    f"<td class='num'>{pc0(pm)}</td><td>{evs(r['ev'])}</td><td class='num'>{r['cuota_minima']:.2f}</td>"
                    f"<td class='note'>{nt + ' ' if nt else ''}{E(t)}{mem}{al} <span class='cp {c_}'>{t_}</span></td></tr>")
    if not rows:
        return ''
    return ("<div class='tw'><table><thead><tr><th>Mercado</th><th>Cuota</th><th>Prob.</th><th>Mercado sin margen</th><th>EV</th>"
            f"<th>Cuota mín.</th><th>Lectura</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>")


def tabla_parejas(A, D):
    """«Cualquiera de los jugadores…»: una fila por pareja, ordenadas por EV dentro de cada tipo."""
    TIT = {'asiste': 'Cualquiera da una asistencia', 'anota_o_asiste': 'Cualquiera anota o asiste',
           'anota': 'Cualquiera anota en cualquier momento', 'tarjeta': 'Cualquiera recibe una tarjeta'}
    out = ''
    for stat, tit in TIT.items():
        rs = sorted([r for r in A['lineas'] if r['sel']['mercado'] == 'pareja' and r['sel']['stat'] == stat], key=lambda r: -r['ev'])
        if not rs:
            continue
        rows = []
        for r in rs:
            t_, c_ = veredicto(r)
            al = (f" <span class='neg'>⚠ {'baja confirmada: no apostar' if 'baja confirmada' in r['alerta'] else E(r['alerta'])}</span>"
                  if r.get('alerta') else '')
            nm = ' o '.join(E(x) for x in r['sel']['jugadores'])
            rows.append(f"<tr><td>{nm}</td><td class='num'><b>{r['cuota']:.2f}</b></td><td class='num'>{pc0(r['p'])}</td>"
                        f"<td class='num'>{pc0(r['p_simulacion'])}</td><td class='num'>{pc0(r.get('p_mercado'))}</td><td>{evs(r['ev'])}</td>"
                        f"<td class='num'>{r['cuota_minima']:.2f}</td><td><span class='cp {c_}'>{t_}</span>{al}</td></tr>")
        out += (f"<h3 class='sub3'>{tit}</h3><div class='tw'><table class='tp'><thead><tr><th>Pareja</th><th>Cuota</th><th>Prob.</th><th>Simulación</th>"
                f"<th>Mercado sin margen</th><th>EV</th><th>Cuota mín.</th><th></th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>")
    return out


# ------------------------------------------------------------------ proyección
FILAS_PROY = [('Goles', 'goles', 'g', 2), ('xG', None, 'xg', 2), ('Remates', 'remates', 'sh', 1), ('Tiros al arco', 'al_arco', 'sot', 1),
              ('Córners', 'corners', 'c', 1), ('Faltas', 'faltas', 'f', 1), ('Tarjetas (amarilla 1, roja 2)', 'tarjetas', 'y', 1),
              ('Fueras de lugar', 'fueras', 'off', 1), ('Saques de banda', 'saques_banda', 'ti', 1),
              ('Saques de meta', 'saques_meta', 'gk', 1), ('Atajadas del portero', 'atajadas', None, 1)]


def tabla_proyeccion(A, forma, loc, vis):
    M = indice_medias(A)
    hay_forma = bool(forma)
    rows = []
    for nombre, m, st, d in FILAS_PROY:
        fm = PR.forma_media(forma, st) if (hay_forma and st) else None
        if m is None and not fm:
            continue
        hl = hv = '—'
        if fm:
            if 'local' in fm:
                hl = f"{fm['local'][0]:.{d}f} / {fm['local'][1]:.{d}f} <small>({fm['local'][2]})</small>"
            if 'visitante' in fm:
                hv = f"{fm['visitante'][0]:.{d}f} / {fm['visitante'][1]:.{d}f} <small>({fm['visitante'][2]})</small>"
        if m:
            ml, mv, mt = M.get((m, 'local')), M.get((m, 'visitante')), M.get((m, 'total'))
            cl = f"<b>{fnum(ml and ml['modelo'], d)}</b>"
            cv = f"<b>{fnum(mv and mv['modelo'], d)}</b>"
            if mt:
                ct = f"<b>{fnum(mt['modelo'], d)}</b>"
                if mt.get('sin_contexto') is not None and abs(mt['modelo'] - mt['sin_contexto']) >= 0.15:
                    ct += f" <small>(sin ficha {mt['sin_contexto']:.{d}f})</small>"
            else:
                ct = '—'
            bt = mt and mt.get('betano')
            if bt is not None:
                bs = f"total {bt:.{d}f}"
                bl, bv = ml and ml.get('betano'), mv and mv.get('betano')
                if bl is not None and bv is not None:
                    bs += f" (equipos {bl:.{d}f} / {bv:.{d}f})"
                dif = mt['modelo'] - bt
                dif_c = f"<span class='ev {'pos' if dif > 0.08 * bt else 'neg' if dif < -0.08 * bt else 'neu'}'>{dif:+.{d}f}</span>"
            else:
                bs, dif_c = ('sin mercado' if m != 'atajadas' else 'ver líneas de portero'), '—'
        else:
            cl = cv = ct = dif_c = '—'
            bs = 'sin mercado'
        rows.append(f"<tr><td>{E(nombre)}</td>" + (f"<td class='num'>{hl}</td><td class='num'>{hv}</td>" if hay_forma else '')
                    + f"<td class='num'>{cl}</td><td class='num'>{cv}</td><td class='num'>{ct}</td><td class='num'>{bs}</td><td class='num'>{dif_c}</td></tr>")
    head = ('<th>Estadística</th>' + (f'<th>{E(loc)} a favor / en contra (casa)</th><th>{E(vis)} a favor / en contra (fuera)</th>' if hay_forma else '')
            + f'<th>{E(loc)} hoy</th><th>{E(vis)} hoy</th><th>Total hoy</th><th>Lo que espera Betano</th><th>Modelo − Betano</th>')
    nota = ('«Hoy» = media esperada del modelo: promedio de los partidos simulados con el contexto de la ficha (la simulación parte del precio de '
            'Betano sin margen). «Lo que espera Betano» = la media que reproduce su escalera de cuotas sin margen. '
            'Si las dos coinciden, el modelo no ve nada que el precio no sepa; una diferencia que no explica un hecho fresco pide revisar el dato.')
    if hay_forma:
        nota += ' A favor / en contra = promedio de los últimos partidos oficiales en la condición de hoy (local en casa, visitante fuera); entre paréntesis, cuántos partidos.'
    return f"<div class='tw'><table><thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div><p class='method'>{nota}</p>"


# ------------------------------------------------------------------ jugadores
def _jug_lineas(A):
    """[(nombre, texto del mercado, r)] de las líneas de jugador (incluye atajadas)."""
    out = []
    for r in A['lineas']:
        s = r['sel']
        if s['mercado'] == 'jugador':
            nm = s['jugador']
            out.append((nm, r['seleccion'][len(nm):].strip(), r))
        elif s['mercado'] == 'atajadas':
            mt = re.match(r'^(.*?) (atajadas \d+\+)$', r['seleccion'])
            if mt:
                out.append((mt.group(1), mt.group(2), r))
    return out


def _lado_jugador(e, nombre):
    for jb in ((e or {}).get('betano') or {}).get('jugadores', []):
        if jb['jugador'] == nombre:
            return jb.get('lado', 'local')
    return 'local'


def _abrev(nombre):
    return nombre


def _hist_txt(h, stat, k):
    if not h:
        return '—'
    v = PR.jug_hits(h, stat, k)
    return f'{round(v[0] / v[1] * 100)}% <small>({v[1]})</small>' if v and v[1] else '—'


def _stat_de_texto(txt):
    """(stat, k) a partir del texto del mercado de jugador («remates 3+», «anota», «atajadas 5+»…)."""
    mp = {'remates': 'remates', 'tiros al arco': 'al_arco', 'anota o asiste': 'anota_o_asiste', 'asiste': 'asiste', 'anota': 'anota',
          'faltas cometidas': 'faltas', 'entradas': 'entradas', 'atajadas': 'atajadas', 'recibe tarjeta': 'tarjeta'}
    mt = re.match(r'^(.*?)(?: (\d+)\+)?$', txt.strip())
    nm = mt.group(1) if mt else txt
    return mp.get(nm), int(mt.group(2)) if mt and mt.group(2) else 1


def tabla_mejores_jugadores(A, e, hist, limite=12):
    js = _jug_lineas(A)
    if not js:
        return ''
    js = sorted(js, key=lambda x: -x[2]['ev'])[:limite]
    hay = bool(hist)
    rows = []
    for nm, txt, r in js:
        tag = 'Loc' if _lado_jugador(e, nm) == 'local' else 'Vis'
        h = None
        if hay:
            f = PR.buscar_jugador(hist, nm)
            h = f[1] if f else None
        stat, k = _stat_de_texto(txt)
        t_, c_ = veredicto(r)
        rows.append(f"<tr><td>{E(nm)} <small>{tag}</small></td><td>{E(txt)}</td><td class='num'><b>{r['cuota']:.2f}</b></td>"
                    f"<td class='num'>{pc0(r['p'])}</td>" + (f"<td class='num'>{_hist_txt(h, stat, k)}</td>" if hay else '')
                    + f"<td>{evs(r['ev'])}</td><td class='num'>{r['cuota_minima']:.2f}</td><td><span class='cp {c_}'>{t_}</span></td></tr>")
    return ("<div class='tw'><table><thead><tr><th>Jugador</th><th>Mercado</th><th>Cuota</th><th>Prob.</th>"
            + ('<th>Histórico 60′+</th>' if hay else '') + "<th>EV</th><th>Cuota mín.</th><th></th></tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table></div>"
            "<p class='method'>Ordenadas por EV. «Riesgo» = cuota de 2.40 o más con valor: para una parte pequeña de lo que juegas. "
            "La probabilidad ya incluye titularidad y minutos esperados de la ficha.</p>")


LB = [('Más remates esperados', 'remates', 'remates', 1), ('Más tiros al arco esperados', 'al_arco', 'al_arco', 1),
      ('Más entradas esperadas', 'entradas', 'entradas', 1), ('Más faltas cometidas', 'faltas', 'faltas', 1),
      ('Más probables de anotar', 'anota', 'p_anota', 0)]


def tablas_lider(A, hist):
    JE = A.get('jugadores_esperado') or {}
    out = []
    for titulo, stat, key, d in LB:
        xs = [(nm, j) for nm, j in JE.items() if stat in (j.get('con_linea') or []) and j.get(key) is not None and not j.get('portero')]
        xs = sorted(xs, key=lambda x: -x[1][key])[:6]
        if not xs:
            continue
        li = ''
        for nm, j in xs:
            f = PR.buscar_jugador(hist, nm) if hist else None
            p90 = PR.jug_por90(f[1], stat) if f else None
            val = f"{j[key] * 100:.0f}%" if d == 0 else f"{j[key]:.1f}"
            li += (f"<li><span>{E(nm)} <small>{'Loc' if j['lado'] == 'local' else 'Vis'}</small></span><b>{val}</b>"
                   + (f"<em>{p90:.1f}/90</em>" if p90 is not None else '') + '</li>')
        out.append(f"<div class='lb'><h4>{titulo}</h4><ol>{li}</ol></div>")
    return f"<div class='lbs'>{''.join(out)}</div>" if out else ''


def tarjetas_jugadores(A, e, hist, D, loc, vis):
    JE = A.get('jugadores_esperado') or {}
    lin = {}
    for nm, txt, r in _jug_lineas(A):
        lin.setdefault(nm, []).append((txt, r))
    if not lin:
        return ''
    mostrar = [('remates', 'Remates', 'remates', 1), ('al_arco', 'Al arco', 'al_arco', 1), ('entradas', 'Entradas', 'entradas', 1),
               ('faltas', 'Faltas hechas', 'faltas', 1), ('anota', 'Anota', 'p_anota', 0), ('anota_o_asiste', 'Anota o asiste', 'p_anota_o_asiste', 0), ('asiste', 'Asiste', 'asiste', 1),
               ('tarjeta', 'Recibe tarjeta', 'p_tarjeta', 0), ('atajadas', 'Atajadas', 'atajadas', 1)]
    ficha_j = {j.get('nombre'): j for j in ((e or {}).get('ficha') or {}).get('jugadores') or [] if j}
    por_lado = {'local': [], 'visitante': []}
    for nm in lin:
        por_lado[_lado_jugador(e, nm)].append(nm)
    html_out = ''
    for lado, nom in (('local', loc), ('visitante', vis)):
        tarj = ''
        for nm in por_lado[lado]:
            j = JE.get(nm) or {}
            f = PR.buscar_jugador(hist, nm) if hist else None
            h = f[1] if f else None
            fj = ficha_j.get(nm) or {}
            minu = j.get('minutos') or fj.get('minutos')
            tit = j.get('titular') or fj.get('titular')
            enc = f"~{minu:g}′ esperados" if minu else ''
            enc += f" · titular {tit * 100:.0f}%" if tit else ''
            if h:
                nj = len([p for p in h.get('partidos') or [] if isinstance(p.get('min'), (int, float)) and p['min'] >= 60])
                enc += f" · {nj} partidos de 60′+ en su historial"
            pos = E((h or {}).get('pos') or ('Portero' if j.get('portero') else ''))
            stats_linea = [st for st in (j.get('con_linea') or [])]
            rates = ''
            for st, lab, key, d in mostrar:
                if st not in stats_linea or j.get(key) is None:
                    continue
                hoy = f"{j[key] * 100:.0f}%" if d == 0 else f"{j[key]:.1f}"
                p90 = PR.jug_por90(h, st) if (h and d == 1) else None
                rates += (f"<div><span>{lab}</span>" + (f"<b>{p90:.1f}</b><em>/90</em>" if p90 is not None else '')
                          + f"<strong>{hoy}</strong><em>hoy</em></div>")
            barras = ''
            if h:
                for st, lab, key, d in mostrar:
                    ks = sorted({_stat_de_texto(t)[1] for t, r in lin[nm] if _stat_de_texto(t)[0] == st})
                    ks = [k for k in ks if k >= 1][:4] if st not in ('anota', 'anota_o_asiste', 'tarjeta') else [1]
                    celdas = ''
                    for k in ks:
                        v = PR.jug_hits(h, st, k)
                        if v and v[1]:
                            celdas += f"<i style='--f:{v[0] / v[1]:.2f}'><em>{k}+</em>{v[0]}/{v[1]}</i>"
                    if celdas and st in stats_linea:
                        barras += f"<div><span>{lab}</span>{celdas}</div>"
                if barras:
                    barras = f"<div class='hits'><p class='hl'>En sus partidos de 60′ o más:</p>{barras}</div>"
            nota = (D.get('jugadores_notas') or {}).get(nm)
            filas = ''
            for txt, r in sorted(lin[nm], key=lambda x: (_stat_de_texto(x[0])[0] or '', _stat_de_texto(x[0])[1])):
                st, k = _stat_de_texto(txt)
                t_, c_ = veredicto(r)
                filas += (f"<tr class='{'hl' if c_ in ('valor', 'riesgo') else ''}'><td>{E(txt)}</td><td><b>{r['cuota']:.2f}</b></td>"
                          f"<td>{pc0(r.get('p_mercado'))}</td><td>{pc0(r['p'])}</td>" + (f"<td>{_hist_txt(h, st, k)}</td>" if h else '')
                          + f"<td>{evs(r['ev'])}</td><td>{r['cuota_minima']:.2f}</td><td><span class='cp {c_}'>{t_}</span></td></tr>")
            tarj += (f"<article class='pl'><header><h4>{E(nm)}</h4><span class='ps'>{pos}</span><span class='min'>{E(enc)}</span></header>"
                     + (f"<div class='rates'>{rates}</div>" if rates else '') + barras
                     + (f"<p class='pnote'>{E(nota)}</p>" if nota else '')
                     + "<div class='tw'><table class='pt'><thead><tr><th>Mercado Betano</th><th>Cuota</th><th>Casa</th><th>Modelo</th>"
                     + ('<th>Histórico 60′+</th>' if h else '') + f"<th>EV</th><th>Mín.</th><th></th></tr></thead><tbody>{filas}</tbody></table></div></article>")
        if tarj:
            html_out += f"<h3>{E(nom)}</h3><div class='pls'>{tarj}</div>"
    return html_out


# ------------------------------------------------------------------ barras, tablas, boletos
def bars(d):
    items = sorted(d.items(), key=lambda kv: -kv[1])
    mx = max(v for _, v in items) or 1
    return "<div class='bars'>" + ''.join(
        f"<div class='bar'><span>{E(k)}</span><div><i style='width:{v / mx * 100:.0f}%'></i></div><b>{v * 100:.0f} %</b></div>" for k, v in items) + '</div>'


def _enfoque_html(A):
    if not A.get('enfoque'):
        return ''
    from .enfoque import html as _h
    return _h(A['enfoque'], A['enfoque_resumen'], E)


def tbl(head, rows, cls_fn=None, cap=None, nums=()):
    th = ''.join(f'<th>{E(h)}</th>' for h in head)
    body = ''
    for r in rows:
        c = cls_fn(r) if cls_fn else ''
        body += f"<tr class='{c}'>" + ''.join(f"<td class='{'n' if j in nums else ''}'>{x}</td>" for j, x in enumerate(r)) + '</tr>'
    capt = f'<caption>{E(cap)}</caption>' if cap else ''
    return f"<div class='tw'><table>{capt}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>"


def res_badge(r):
    return f"<span class='res {r}'>{r}</span>"


def boleto(b):
    cls = {'valor': 'win', 'justo': 'mid', 'evitar': 'lose'}.get(b['estado'], 'mid')
    txt = {'valor': 'Con valor', 'justo': 'Precio justo', 'evitar': 'Evitar', 'armar': 'Armar en Betano'}.get(b['estado'], '')
    chc = {'valor': 'g', 'justo': 'y', 'evitar': 'r'}.get(b['estado'], '')
    legs = ''.join(f'<li>{E(x)}</li>' for x in b['patas'])
    nums = ''.join(f'<div><span>{E(k)}</span><b>{E(str(v))}</b></div>' for k, v in b['nums'])
    return (f"<article class='tk {cls}'><header><div><h4>{E(b['nombre'])}</h4><p class='sub'>{E(b.get('sub', ''))}</p></div>"
            f"<div class='chips'>{chip(txt, chc)}{''.join(chip(t, c) for t, c in b.get('chips', []))}</div></header>"
            f"<ul class='legs'>{legs}</ul><div class='nums'>{nums}</div><p>{b.get('texto', '')}</p></article>")


def _boletos_auto(A):
    out = []
    for c in A.get('combos') or []:
        if c.get('error'):
            continue
        out.append(dict(nombre=c['nombre'], sub='Combo con la cuota del cupón', estado=c.get('estado', 'armar'), patas=c['patas'],
                        nums=[('Cupón', c.get('cuota', '—')), ('Prob. ajustada', pct(c['p_ajust'])), ('Prob. sim.', pct(c['p_sim'])),
                              ('EV ajust.', '—' if c.get('ev_ajust') is None else f"{c['ev_ajust'] * 100:+.1f} %"),
                              ('Stress', '—' if c.get('ev_stress') is None else f"{c['ev_stress'] * 100:+.1f} %"), ('Cuota mínima', c['cuota_minima'])],
                        chips=[('Correlación ' + str(c['correlacion']), '')] + ([('Avisos', 'y')] if c.get('avisos') else []),
                        texto=E(' · '.join(c.get('avisos') or [])) + (f" Pata más frágil: {E(c['pata_mas_fragil'])}." if c.get('pata_mas_fragil') else '')))
    for b in (A.get('builders') or [])[:6]:
        out.append(dict(nombre=' + '.join(b['patas']), sub=f"Guion común: {b.get('guion_comun') or '—'}", estado='armar', patas=b['patas'],
                        nums=[('Prob. ajustada', pct(b['p'])), ('Si una pata −5 pts', pct(b.get('p_stress'))), ('Cuota justa', b['cuota_justa']),
                              ('Cuota mínima', b['cuota_minima']), ('Correlación', b['correlacion']), ('Margen acumulado', pct(b.get('margen_acumulado')))],
                        chips=[('Avisos', 'y')] if b.get('avisos') else [],
                        texto=('Juega solo si el cupón de Betano muestra la cuota mínima o más. ' + E(' · '.join(b.get('avisos') or [])))))
    return out


# ------------------------------------------------------------------ veredicto, meta y alineaciones
def _meta(A, e, D):
    L = A['lineas']
    res = {r['sel'].get('lado'): r for r in L if r['sel']['mercado'] == 'resultado'}
    sp = []
    est = D.get('estadio') or (e or {}).get('estadio') or ((e or {}).get('ficha') or {}).get('estadio')
    if est:
        sp.append(f"Estadio <b>{E(est)}</b>")
    arb = D.get('arbitro')
    ar = ((e or {}).get('ficha') or {}).get('arbitro') or {}
    if not arb and ar.get('nombre'):
        arb = ar['nombre']
        if ar.get('amarillas_por_partido') is not None:
            arb += f" · {ar['amarillas_por_partido']:g} amarillas/partido" + (f" ({ar['partidos']} partidos)" if ar.get('partidos') else '')
    if arb:
        sp.append(f"Árbitro <b>{E(arb)}</b>")
    if all(k in res for k in ('1', 'X', '2')):
        sp.append(f"1X2 <b>{res['1']['cuota']:.2f} · {res['X']['cuota']:.2f} · {res['2']['cuota']:.2f}</b>")
    g25 = next((r for r in L if r['sel']['mercado'] == 'goles' and r['sel'].get('ambito', 'total') == 'total' and r['sel'].get('linea') == 2.5
                and r['sel']['lado'] == 'mas'), None)
    g25m = next((r for r in L if r['sel']['mercado'] == 'goles' and r['sel'].get('ambito', 'total') == 'total' and r['sel'].get('linea') == 2.5
                 and r['sel']['lado'] == 'menos'), None)
    if g25 and g25m:
        sp.append(f"Goles 2.5 <b>{g25['cuota']:.2f} / {g25m['cuota']:.2f}</b>")
    bt = next((r for r in L if r['sel']['mercado'] == 'ambos' and r['sel']['lado'] == 'si'), None)
    if bt:
        sp.append(f"Ambos marcan <b>{bt['cuota']:.2f}</b>")
    if D.get('cuotas_leidas') or (e or {}).get('cuotas_leidas'):
        sp.append(E(D.get('cuotas_leidas') or e['cuotas_leidas']))
    return f"<div class='meta'>{''.join(f'<span>{x}</span>' for x in sp)}</div>" if sp else ''


def _verdict(A, e, D, loc, vis):
    L = A['lineas']
    nota = lambda r: (D.get('notas') or {}).get(r['seleccion'])

    def li(r, extra=''):
        t_, c_ = veredicto(r)
        return (f"<li><b>{E(r['seleccion'])}</b><span class='o'>{r['cuota']:.2f}</span>"
                f"<p>{E(nota(r)) + ' ' if nota(r) else ''}{E(texto_valor(r))}{extra} <span class='cp {c_}'>{t_}</span></p></li>")
    val = sorted([r for r in L if 'Valor' in r['etiqueta'] and not r.get('alerta') and r['familia'] != 'jugador'], key=lambda r: -r['ev'])[:4]
    izq = (f"<div class='box main'><h3>Líneas de equipo con valor</h3><ul class='bb'>{''.join(li(r) for r in val)}</ul></div>" if val else
           "<div class='box main'><h3>Líneas de equipo con valor</h3><p>Ninguna línea de equipo o partido con valor: el precio de Betano ya refleja lo que sabe el modelo.</p></div>")
    bs = [c for c in (A.get('combos') or []) if not c.get('error') and c.get('estado') == 'valor']
    b = None
    if bs:
        c = bs[0]
        b = (c['nombre'], c['patas'], f"Cupón {c.get('cuota', '—')} · prob. ajustada {pct(c['p_ajust'])} · cuota mínima {c['cuota_minima']}", ' · '.join(c.get('avisos') or []))
    elif A.get('builders'):
        c = A['builders'][0]
        b = (' + '.join(c['patas']), c['patas'], f"Prob. ajustada {pct(c['p'])} · cuota justa {c['cuota_justa']} · cuota mínima {c['cuota_minima']} · correlación {c['correlacion']}",
             'Betano descuenta la correlación: juégalo solo si el cupón llega a la cuota mínima. ' + ' · '.join(c.get('avisos') or []))
    if b:
        izq += (f"<div class='box'><h3>Bet builder sugerido</h3><ul class='bb'>{''.join(f'<li><b>{E(x)}</b></li>' for x in b[1])}</ul>"
                f"<div class='tot'><span>{E(b[2])}</span></div><p class='method' style='margin-top:8px'>{E(b[3])}</p></div>")
    jug = sorted([x for x in _jug_lineas(A) if 'Valor' in x[2]['etiqueta'] and not x[2].get('alerta')], key=lambda x: -x[2]['ev'])[:4]
    der = ''
    if jug:
        items = ''.join(f"<li><b>{E(nm)} {E(txt)}</b><span class='o'>{r['cuota']:.2f}</span><p>{E((D.get('notas') or {}).get(r['seleccion'], ''))} {E(texto_valor(r))} "
                        f"<span class='cp {veredicto(r)[1]}'>{veredicto(r)[0]}</span></p></li>" for nm, txt, r in jug)
        der += f"<div class='box risk'><h3>Para tu estilo: jugadores y riesgo</h3><ul class='bb'>{items}</ul></div>"
    evitar = D.get('evitar') or _evitar_auto(A)
    der += f"<div class='box'><h3>Lo que no haría</h3><ul>{''.join(f'<li>{x}</li>' for x in evitar)}</ul></div>"
    return f"<div class='verdict'><div class='col'>{izq}</div><div class='col'>{der}</div></div>"


def _evitar_auto(A):
    L = A['lineas']
    out = [f"{E(r['seleccion'])} ({r['cuota']:.2f}): EV {r['ev'] * 100:+.0f} %." for r in
           sorted([r for r in L if r['cuota'] >= 1.25 and r['familia'] != 'jugador'], key=lambda r: r['ev'])[:3]]
    for r in L:
        if r.get('alerta'):
            out.append(f"{E(r['seleccion'])}: {E(r['alerta'])}")
            break
    M = indice_medias(A)
    sin = []
    for m in ('goles', 'corners', 'tarjetas', 'remates', 'faltas'):
        x = M.get((m, 'total'))
        if x and x.get('betano') and abs(x['modelo'] - x['betano']) <= 0.04 * x['betano']:
            sin.append(f"{BASE[m].lower()} (modelo {x['modelo']:g}, Betano {x['betano']:g})")
    if sin:
        out.append('Sin señal en ' + ', '.join(sin) + ': la media esperada es igual a la que pone Betano.')
    res = {r['sel'].get('lado'): r for r in L if r['sel']['mercado'] == 'resultado'}
    if all(k in res for k in ('1', 'X', '2')) and all(abs(res[k]['p'] - (res[k].get('p_mercado') or res[k]['p'])) < 0.02 for k in ('1', 'X', '2')):
        out.append(f"1X2: modelo y mercado coinciden ({pct(res['1']['p'])} · {pct(res['X']['p'])} · {pct(res['2']['p'])}).")
    return out


def _alineaciones(e, D, loc, vis):
    if D.get('alineaciones'):
        al = D['alineaciones']
        return ("<div class='lineups'>" + ''.join(
            f"<div class='box'><h3>{E(al[l].get('titulo') or n)}</h3><p>{E(al[l].get('texto', ''))}</p>"
            + (f"<p class='muted'>{E(al[l]['bajas'])}</p>" if al[l].get('bajas') else '') + '</div>'
            for l, n in (('local', loc), ('visitante', vis)) if al.get(l)) + '</div>')
    f = (e or {}).get('ficha') or {}
    bajas = f.get('bajas') or []
    if not bajas:
        return ''
    out = ''
    for l, n in (('local', loc), ('visitante', vis)):
        bs = [b for b in bajas if b.get('lado') == l]
        txt = '; '.join(
            f"{b.get('jugador', '?')} ({b.get('posicion') or 'posición ?'}, reemplazo: {b.get('reemplazo') or '?'}, "
            f"{'confirmada' if b.get('confirmada') else 'sin confirmar'}"
            + (f", hace {b['horas_desde_noticia']:g} h" if b.get('horas_desde_noticia') is not None else '') + ')' for b in bs)
        out += f"<div class='box'><h3>{E(n)} · bajas</h3><p>{E(txt) if txt else 'Sin bajas informadas en la ficha.'}</p></div>"
    return f"<div class='lineups'>{out}</div>"


# ------------------------------------------------------------------ página
def html(A, e=None, D=None):
    e = e or {}
    D = dict(e.get('informe') or {}, **(D or {}))
    L = A['lineas']
    local, vis = (A['partido'].split(' - ', 1) + [''])[:2]
    forma = e.get('forma') or (e.get('ficha') or {}).get('forma')
    hist = e.get('jugadores_hist') or (e.get('ficha') or {}).get('jugadores_hist')
    res = {r['sel'].get('lado'): r for r in L if r['sel']['mercado'] == 'resultado'}
    o = A['objetivos']
    kp = []
    if all(k in res for k in ('1', 'X', '2')):
        for k, nm in (('1', f'Gana {local}'), ('X', 'Empate'), ('2', f'Gana {vis}')):
            kp.append((nm, pct(res[k]['p']), f"mercado {pct(res[k]['p_mercado'])} · cuota {res[k]['cuota']:.2f}"))
    M = indice_medias(A)
    gt = M.get(('goles', 'total'))
    kp.append(('Goles esperados', f"{o['local']['g']:.2f} – {o['visitante']['g']:.2f}", f"total {o['local']['g'] + o['visitante']['g']:.2f}" + (f" · Betano {gt['betano']:g}" if gt and gt.get('betano') else '')))
    ct = M.get(('corners', 'total'))
    kp.append(('Córners esperados', f"{o['local']['c'] + o['visitante']['c']:.1f}", f"Betano {ct['betano']:g}" if ct and ct.get('betano') else 'según el precio de Betano'))
    tt = M.get(('tarjetas', 'total'))
    kp.append(('Tarjetas esperadas', f"{o['local']['y'] + o['visitante']['y']:.1f}", ('amarilla 1, roja 2' + (f" · Betano {tt['betano']:g}" if tt and tt.get('betano') else ''))))
    kp.append(('Primer gol', f"{pct(A['p_primer_gol']['local'])} / {pct(A['p_primer_gol']['visitante'])}", f"nadie {pct(A['p_primer_gol']['nadie'])}"))
    kpis = ''.join(f"<div class='kpi'><span>{E(a)}</span><b>{E(b)}</b><small>{E(c)}</small></div>" for a, b, c in kp)
    val = sorted([r for r in L if 'Valor' in r['etiqueta'] and not r.get('alerta')], key=lambda r: -r['ev'])
    alta = sorted([r for r in L if 'Alta probabilidad' in r['etiqueta'] and r['cuota'] >= 1.25 and not r.get('alerta')], key=lambda r: -r['p'])
    if 'veredicto' not in D:
        if val:
            D['veredicto'] = 'Líneas con valor según el modelo: ' + '; '.join(f"{r['seleccion']} a {r['cuota']:.2f} (EV {r['ev'] * 100:+.0f} %, mín. {r['cuota_minima']:.2f})" for r in val[:3]) + '.'
        else:
            D['veredicto'] = 'Ninguna línea suelta con valor: el precio de Betano ya refleja lo que sabe el modelo.'
    if 'accion' not in D:
        D['accion'] = ('Más probables y robustas: ' + '; '.join(f"{r['seleccion']} ({pct(r['p'])}, {r['cuota']:.2f})" for r in alta[:3]) + '.') if alta else \
            'No hay líneas de alta probabilidad robustas con cuota ≥ 1,25.'
    chips = D.get('chips') or [(A['tipo'], ''), (f"Favorito: {A['favorito']}", '')]
    if A.get('alertas'):
        chips.append((f"{len(A['alertas'])} alerta(s)", 'r'))
    if A.get('sistemas'):
        chips.append((f"{len(A['sistemas'])} sistema(s) de tipsters", 'y'))
    P = pares(L)
    sec_mercados = ''
    nav_m = []
    for sid, titulo, mercados in SECCIONES:
        t = tabla_mercado(A, e, D, mercados, forma, local, vis)
        if t:
            sec_mercados += f"<section id='{sid}'><h2>{E(titulo)}</h2>{t}</section>"
            nav_m.append((sid, titulo))
    esp = tabla_especiales(A, D)
    par = tabla_parejas(A, D)
    jl = tabla_mejores_jugadores(A, e, hist)
    jug = (tablas_lider(A, hist) + tarjetas_jugadores(A, e, hist, D, local, vis)) if _jug_lineas(A) else ''
    sist = ''
    if A.get('sistemas'):
        sist = tbl(['Sistema', 'Regla', 'Propone', 'Historial con cuotas reales'],
                   [[E(x['fuente']), E(x['regla']), E(x['seleccion']), E(x['historial'])] for x in A['sistemas']],
                   cap=None)
    lectura = D.get('lectura') or [E(x) for x in (A.get('contexto') or [])]
    if A.get('liga_base'):
        lectura = lectura + [f"<b>Base de la liga.</b> {E(A['liga_base'])}"]
    bol = D.get('boletos') or _boletos_auto(A)
    alertas = ''.join(f'<li>{E(a)}</li>' for a in A.get('alertas') or [])
    extra = ''
    if D.get('tabla'):
        extra += tbl(['#', 'Equipo', 'PJ', 'G-E-P', 'GF:GC', 'DG', 'Pts', 'Forma'],
                     [[E(str(a)), E(b), c, d, ee, f, f'<b>{g}</b>', ''.join(res_badge(x) for x in h)] for a, b, c, d, ee, f, g, h in D['tabla']],
                     cls_fn=lambda r: 'me' if any(k in r[1] for k in (local, vis)) else '', nums=(0, 2, 3, 4, 5, 6), cap='Clasificación')
    for tit, rows in D.get('formas') or []:
        extra += tbl(['Fecha', 'Comp.', 'Partido', 'Marcador', ''], [[a, b, E(c), f'<b>{d}</b>', res_badge(ee)] for a, b, c, d, ee in rows], cap=tit, nums=(0, 3))
    if D.get('h2h'):
        extra += tbl(['Fecha', 'Comp.', 'Partido', 'Marcador'], [[a, b, E(c), f'<b>{d}</b>'] for a, b, c, d in D['h2h']], cap='Enfrentamientos directos', nums=(0, 3))
    datos = ''.join(f'<li>{x}</li>' for x in D.get('datos') or [])
    nav = [('veredicto', 'Veredicto')] + ([('enfoque', 'Enfoque')] if A.get('enfoque') else []) + [('proyeccion', 'Proyección'), ('boletos', 'Boletos'), ('guiones', 'Guiones')]
    if jl:
        nav.append(('jl', 'Mejores jugadores'))
    nav += nav_m
    if esp:
        nav.append(('esp', 'Resultado y especiales'))
    if par:
        nav.append(('par', 'Parejas de jugadores'))
    if jug:
        nav.append(('jug', 'Jugadores'))
    if extra or datos:
        nav.append(('contexto', 'Contexto'))
    nav.append(('limites', 'Límites'))
    nav_html = ''.join(f"<a href='#{i}'>{E(t)}</a>" for i, t in nav)
    limites = list(D.get('limites') or ['Probabilidad de decisión = 50 % simulación + 50 % mercado sin margen (método de potencia) + lo que el contexto agrega.',
                                   'La media esperada es la de la simulación con el contexto de la ficha; sin hechos frescos casi no se aleja de la que pone Betano.',
                                   'Sin hechos frescos, el modelo casi no se aleja del precio: la ventaja posible está en el contexto fresco, la línea que aguanta los guiones probables y el precio del cupón.',
                                   'Las líneas de jugador dependen de la titularidad y los minutos de la ficha.'])
    if not forma and not D.get('limites'):
        limites.append('Este informe no trae el historial reciente de los equipos («forma»): sin él no se muestran a favor / en contra ni las veces que salió Más.')
    check = D.get('checklist') or ['Confirmar alineaciones; si cambia algo, marcarlo como fresco y volver a correr el modelo.',
                                   'Leer el total del cupón (no la tarjeta «Mejores cuotas») y jugar solo a la cuota mínima o más.',
                                   'Dos boletos que dependen de la misma idea del partido cuentan como una sola apuesta.']
    titulo = D.get('titulo_pagina') or A['partido']
    acento = D.get('acento')
    css_acc = f"<style>:root{{--acc:{acento[0]};--accs:{acento[1]}}}</style>" if acento else ''
    nl, nv = len(PR._cond(forma, 'local')), len(PR._cond(forma, 'visitante'))
    como_txt = D.get('como') or (
        f"Cuotas: las de Betano de la entrada, sin margen (método de potencia). Simulación: {C.N_SIM:,} partidos minuto a minuto, anclados a ese precio, con el contexto de la ficha. "
        "<b>Media esperada</b> = promedio de esos partidos; «Betano» = la media que reproduce su escalera de cuotas sin margen; «sin ficha» = la misma simulación sin el contexto; "
        "«80 %» = el rango donde cae el 80 % de los partidos simulados. "
        f"Probabilidad de decisión = {int((1 - C.W_MERCADO['goles']) * 100)} % simulación + {int(C.W_MERCADO['goles'] * 100)} % mercado sin margen (jugadores: {int((1 - C.W_MERCADO['jugador']) * 100)} % / {int(C.W_MERCADO['jugador'] * 100)} %), más lo que el contexto agrega. EV = probabilidad × cuota − 1. "
        "Etiquetas: VALOR = EV ≥ 3 % con 2 pts de ventaja y que aguanta los guiones; RIESGO = valor con cuota de 2.40 o más; FRÁGIL = valor que depende de un solo guion; JUSTA = precio sin ventaja; NO = el precio es peor que la probabilidad. "
        + (f"Historial: {nl} partidos de {E(local)} en casa y {nv} de {E(vis)} fuera (a favor / en contra y «veces que salió Más»). " if forma else "")
        + ("Historial de jugadores: sus partidos de 60′ o más. " if hist else ""))
    como = f"<section id='como'><h2>Cómo se calculó</h2><p class='method'>{como_txt}</p></section>"
    return f"""<meta charset="utf-8">
<title>{E(titulo)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>{CSS}</style>{css_acc}
<div class="wrap">
<header class="hero" id="veredicto">
 <span class="eyebrow">{E(A.get('liga') or '')} · {E(str(A.get('fecha') or ''))}</span>
 <h1>{E(local)} – {E(vis)}</h1>
 {_meta(A, e, D)}
 <div class="chips">{''.join(chip(t, c) for t, c in chips)}</div>
 <p><b>{D['veredicto']}</b></p>
 <p>{D['accion']}</p>
</header>
<nav class="jump">{nav_html}</nav>
<div class="kpis">{kpis}</div>
{('<div class="box warn"><h5>Alertas</h5><ul>' + alertas + '</ul></div>') if alertas else ''}
{_enfoque_html(A)}
{_verdict(A, e, D, local, vis)}
<section id="lectura"><h2>Lectura del partido</h2><div class="box key"><ul>{''.join(f'<li>{x}</li>' for x in lectura)}</ul></div>{_alineaciones(e, D, local, vis)}</section>
<section id="proyeccion"><h2>Proyección del partido</h2>{tabla_proyeccion(A, forma, local, vis)}</section>
<section id="boletos"><h2>Boletos</h2><p class="method">{D.get('nota_boletos', 'Combos con cupón (si se dieron) y builders del mismo guion. La prob. ajustada lleva cada pata a su probabilidad de decisión y corrige la dependencia entre patas medida con 62 000 partidos.')}</p><div class="grid2">{''.join(boleto(b) for b in bol)}</div></section>
<section id="guiones"><h2>Guiones del partido</h2><div class="box">{bars(A['guiones'])}<p class="method">Cada guion es un tipo de partido simulado minuto a minuto. Una línea es sólida si sobrevive en los guiones probables (columna Rob. de cada línea).</p></div></section>
{('<section id="jl"><h2>Mejores líneas de jugador</h2>' + jl + '</section>') if jl else ''}
{('<label class="filter"><input type="checkbox" id="only"> Mostrar solo líneas con valor o de riesgo</label>') if sec_mercados else ''}
{sec_mercados}
{('<section id="esp"><h2>Resultado y especiales</h2>' + esp + '</section>') if esp else ''}
{('<section id="par"><h2>Cualquiera de los jugadores…</h2><p class="method">Dos jugadores en una sola apuesta: gana si CUALQUIERA de los dos cumple. La probabilidad sale de la misma simulación de jugadores (con titularidad y minutos de la ficha) mezclada con el mercado; la pareja de un jugador baja confirmada se calcula solo con la simulación.</p>' + par + '</section>') if par else ''}
{('<section id="jug"><h2>Jugadores</h2><p class="method">«Hoy» = lo que se espera del jugador en este partido: su parte de lo que hace su equipo en la simulación, por los minutos esperados de la ficha (solo en las estadísticas con línea en Betano). Con historial, /90 = su media por 90′ y las barras muestran en cuántos de sus partidos de 60′ o más llegó a cada número.</p>' + jug + '</section>') if jug else ''}
{('<section id="sistemas"><h2>Sistemas de tipsters que el partido cumple</h2><p class="method">Solo para medir, no para decidir: cada fila trae el historial real del sistema con cuotas de mercado.</p>' + sist + '</section>') if sist else ''}
{('<section id="contexto"><h2>Contexto</h2>' + extra + (('<div class="box"><h5>Datos del partido</h5><ul>' + datos + '</ul></div>') if datos else '') + '</section>') if (extra or datos) else ''}
<section id="limites"><h2>Límites</h2><div class="grid2"><div class="box"><h5>Límites</h5><ul>{''.join(f'<li>{x}</li>' for x in limites)}</ul></div>
<div class="box key"><h5>Antes de apostar</h5><ul>{''.join(f'<li>{x}</li>' for x in check)}</ul></div></div></section>
{como}
<p class="method">Método (supermodelo SM-1): simulación minuto a minuto anclada al precio de Betano sin margen (método de potencia), calibrada con 62 000 partidos reales (dispersión de córners, remates y tarjetas; Ambos Marcan y empate; efecto del marcador; dependencia entre patas). Media esperada = promedio de los partidos simulados con el contexto de la ficha; «Betano» = la media que reproduce su escalera de cuotas sin margen. EV = probabilidad de decisión × cuota − 1. Cuota mínima: la menor con EV ≥ 3 % y 2 pts de ventaja. No es asesoría financiera ni garantía de resultado.</p>
</div>
<script>try{{var c=document.getElementById('only');if(c)c.addEventListener('change',function(){{document.body.classList.toggle('only',c.checked)}})}}catch(e){{}}</script>"""
