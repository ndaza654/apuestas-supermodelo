# -*- coding: utf-8 -*-
import json, html, math
P = json.load(open('picks.json', encoding='utf8'))
URL = {'turquia-belgica': 'HK2Wn3d9Guog3sitefFmQA', 'fc-barcelona-f-arsenal-fc-f': '4hJdR7Xfx8STgS9Z7tzR1h', 'costa-de-marfil-gambia': '3fCLAdkWY7u3cZMMp4m9sG', 'senegal-sudan': '4osx1HnUpnd8K8Gpqi8w7v',
       'inglaterra-croacia': 'U57WKUeiPLyMXML5yoMJk8', 'italia-francia': 'JQdPE3ZQoobNGEg3k1zr8V', 'albania-finlandia': '3zuWupniMswHXxXmFGcR6N', 'republica-checa-espana': '2AHBsVLuw6FK4tVx6LpRoY', 'montenegro-letonia': '7W39BhwcfTU1ArD18mtzZT'}
ORD = ['turquia-belgica', 'fc-barcelona-f-arsenal-fc-f', 'costa-de-marfil-gambia', 'senegal-sudan', 'inglaterra-croacia', 'italia-francia', 'albania-finlandia', 'republica-checa-espana', 'montenegro-letonia']
E = html.escape
def pk(k, sel): return next(x for x in P[k]['picks'] if x['seleccion'] == sel)
COMBOS = [
 ('Segura · 2 patas', 'Dos líneas de tarjetas con árbitros de perfil opuesto. Horarios distintos (12:00 y 14:45).',
  [('turquia-belgica', 'Tarjetas Menos 5.5'), ('italia-francia', 'Tarjetas Más 2.5')]),
 ('Media · 3 patas', 'Tres partidos de las 14:00–14:45, una idea distinta en cada uno.',
  [('republica-checa-espana', 'Tarjetas Menos 4.5'), ('senegal-sudan', 'Goles Senegal Menos 3.5'), ('italia-francia', 'Tarjetas Más 2.5')]),
 ('Exótica · 5 patas', 'Las cinco líneas de valor de la tarde. Paga cerca de 10 a 1 y gana aproximadamente 1 de cada 9 o 10 veces: jugarla con el stake más bajo.',
  [('italia-francia', 'Tarjetas Más 3.5'), ('republica-checa-espana', 'Hándicap República Checa +2.5'), ('senegal-sudan', 'Goles Menos 3.5'), ('inglaterra-croacia', 'Córners Croacia Menos 3.5'), ('montenegro-letonia', 'Tarjetas Menos 4.5')]),
]
TIPO = {'alta': 'Alta probabilidad', 'valor': 'Valor', 'extra': 'Extra'}
def fila(x):
    cls = 'pos' if x['ev'] >= 0.02 else ('neg' if x['ev'] <= -0.02 else '')
    return (f"<tr><td class='sel'><span class='tag {x['tipo']}'>{TIPO[x['tipo']]}</span><br>{E(x['seleccion'])}</td><td class='n'>{x['cuota']:.2f}</td>"
            f"<td class='n'>{x['p'] * 100:.0f} %</td><td class='n {cls}'>{x['ev'] * 100:+.1f} %</td><td class='n'><b>{x['cuota_minima']:.2f}</b></td></tr>")
cards = ''
for k in ORD:
    m = P[k]
    cards += (f"<section class='card'><header><span class='hora'>{m['hora']}</span><h2>{E(m['partido'])}</h2><span class='liga'>{E(m['liga'])}</span></header>"
              f"<p class='ver'>{E(m['veredicto'])}</p><div class='tw'><table><thead><tr><th>Línea</th><th>Cuota</th><th>Prob.</th><th>EV</th><th>Mín.</th></tr></thead><tbody>"
              + ''.join(fila(x) for x in m['picks']) + f"</tbody></table></div><a class='btn' href='https://claude.ai/artifact/{URL[k]}' target='_blank' rel='noopener'>Abrir el informe completo</a></section>")
comb = ''
for tit, nota, patas in COMBOS:
    xs = [(P[k]['partido'], pk(k, s)) for k, s in patas]
    cuota = math.prod(x['cuota'] for _, x in xs); p = math.prod(x['p'] for _, x in xs); pm = math.prod((x.get('p_mercado') or x['p']) for _, x in xs)
    margen = 1 - math.prod((x.get('p_mercado') or x['p']) * x['cuota'] for _, x in xs)
    comb += (f"<section class='card combo'><header><h2>{E(tit)}</h2></header><p class='ver'>{E(nota)}</p><ul>" + ''.join(f"<li><b>{E(x['seleccion'])}</b> <span class='n'>{x['cuota']:.2f}</span><br><span class='liga'>{E(pa)}</span></li>" for pa, x in xs)
             + f"</ul><div class='kp'><div><span>Cuota combinada</span><b>{cuota:.2f}</b></div><div><span>Prob. según el modelo</span><b>{p * 100:.0f} %</b></div><div><span>Prob. según Betano sin margen</span><b>{pm * 100:.0f} %</b></div>"
             f"<div><span>Cuota justa (modelo)</span><b>{1 / p:.2f}</b></div><div><span>Margen acumulado de la casa</span><b>{margen * 100:.0f} %</b></div><div><span>EV según el modelo</span><b>{(p * cuota - 1) * 100:+.0f} %</b></div></div></section>")
page = f"""<title>Líneas del 12-nov</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root{{--bg:#f4f2ec;--fg:#18201c;--mut:#5f6963;--card:#fffefb;--line:#d8d4c8;--acc:#0c6b4e;--accs:#e3f0ea;--pos:#0c6b4e;--neg:#a23b2c;--warn:#8a5a00;--warns:#f8efd8}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#101412;--fg:#e8ece8;--mut:#98a39c;--card:#181d1a;--line:#2a322d;--acc:#62d3a8;--accs:#17332a;--pos:#62d3a8;--neg:#f0907f;--warn:#e9c46a;--warns:#332a12;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#101412;--fg:#e8ece8;--mut:#98a39c;--card:#181d1a;--line:#2a322d;--acc:#62d3a8;--accs:#17332a;--pos:#62d3a8;--neg:#f0907f;--warn:#e9c46a;--warns:#332a12;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 "IBM Plex Sans",system-ui,sans-serif;padding-block:22px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:860px;margin:0 auto;display:flex;flex-direction:column;gap:16px}}
h1{{font:700 34px/1.05 "Barlow Condensed",sans-serif;text-transform:uppercase;letter-spacing:.01em;margin:0;text-wrap:balance}}
h2{{font:700 24px/1.1 "Barlow Condensed",sans-serif;text-transform:uppercase;margin:0;text-wrap:balance}}
h3{{font:600 13px/1.2 "IBM Plex Mono",monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);margin:14px 0 0}}
p{{margin:0}} .mut{{color:var(--mut)}}
.aviso{{background:var(--warns);border-left:4px solid var(--warn);border-radius:8px;padding:12px 14px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.card header{{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 12px}}
.hora{{font:500 14px "IBM Plex Mono",monospace;background:var(--accs);color:var(--acc);padding:2px 8px;border-radius:6px}}
.liga{{font:400 12px "IBM Plex Mono",monospace;color:var(--mut)}}
.ver{{color:var(--fg)}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%}}
th{{font:500 11px "IBM Plex Mono",monospace;text-transform:uppercase;letter-spacing:.06em;color:var(--mut);text-align:left;padding:6px;border-bottom:1px solid var(--line)}}
td{{padding:8px 6px;border-bottom:1px solid var(--line);vertical-align:top}} tr:last-child td{{border-bottom:0}}
.n{{font-family:"IBM Plex Mono",monospace;font-size:13px;font-variant-numeric:tabular-nums;white-space:nowrap}} td.n,th{{padding-left:4px!important;padding-right:4px!important}} .sel{{font-weight:600}}
.pos{{color:var(--pos)}} .neg{{color:var(--neg)}}
.tag{{font:500 11px "IBM Plex Mono",monospace;padding:2px 7px;border-radius:999px;border:1px solid var(--line);white-space:nowrap}} .tag.alta{{background:var(--accs);color:var(--acc);border-color:transparent}} .tag.valor{{background:var(--warns);color:var(--warn);border-color:transparent}}
.btn{{align-self:flex-start;font-weight:600;color:var(--acc);text-decoration:none;border:1px solid var(--acc);border-radius:8px;padding:8px 12px}}
.combo ul{{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:6px}}
.kp{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px}} .kp div{{background:var(--bg);border-radius:8px;padding:8px 10px;display:flex;flex-direction:column}} .kp span{{font:400 11px "IBM Plex Mono",monospace;color:var(--mut)}} .kp b{{font:500 18px "IBM Plex Mono",monospace}}
ul.plain{{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:6px}}
</style>
<main>
<p class="liga">Jueves 12 de noviembre de 2026 · horas de Bogotá · cuotas de Betano leídas a las 00:05</p>
<h1>Líneas del día y combinadas</h1>
<p>Nueve partidos analizados uno por uno con el supermodelo. En cada tarjeta: la línea de alta probabilidad, la de valor y los extras, con su cuota mínima. El informe completo de cada partido trae el enfoque de mercados, lo que calculó el modelo contra lo que espera Betano en cada estadística, y todas las líneas.</p>
<div class="aviso"><b>Cómo leerlo.</b> El modelo casi nunca se aleja del precio de Betano: la mayoría de las líneas están en su precio justo (EV cerca de 0). Donde hay EV positivo sale de una hipótesis de contexto (árbitro, bajas de hace 1–4 días, clima), no de un dato de última hora. Las cuotas son de la madrugada: <b>juega una línea solo si Betano paga la cuota mínima o más</b>, y revisa la alineación oficial una hora antes.</div>
<h3>Partidos por hora</h3>
{cards}
<h3>Combinadas entre partidos</h3>
<p class="mut">La probabilidad conjunta es el producto de las probabilidades (partidos distintos). «Según Betano sin margen» es lo que saldría si el modelo no viera ninguna ventaja: la diferencia entre las dos es todo lo que aporta el contexto.</p>
{comb}
<h3>Lo que quedó por fuera</h3>
<section class="card"><ul class="plain">
<li><b>Curazao – Panamá (19:30):</b> Betano no tenía el partido publicado a las 00:05, así que no hay cuotas ni análisis. El contexto recolectado (ida de cuartos, viento fuerte, bajas de Curazao) apunta a pocos goles y empate vivo al descanso; si aparece en Betano, mándame captura y lo corro.</li>
<li><b>Jugadores y parejas «cualquiera de los jugadores…»:</b> se analizaron en los cuatro partidos donde Betano los ofrece completos (Turquía–Bélgica, Inglaterra–Croacia, Italia–Francia, Chequia–España), con alineaciones probables. Ninguna línea llegó a su cuota mínima: el margen de Betano en jugadores es de 10 % o más.</li>
<li><b>Descanso/final:</b> analizado en los nueve partidos; ninguna opción llega a su precio justo.</li>
<li><b>Líneas de jugadores que no juegan y siguen abiertas en Betano:</b> Lukaku, Lavia, Bardakcı; Konsa, Guéhi, Lewis-Skelly, Spence; Perišić, Šutalo, Jakić; Sadílek, Barrenetxea. No tocarlas.</li>
</ul></section>
<p class="liga">Supermodelo SM-1.2 · probabilidad de decisión = 50 % simulación + 50 % mercado sin margen · 1 unidad = 3.700 COP · no es asesoría financiera.</p>
</main>"""
open('informes/resumen-12nov.html', 'w', encoding='utf8').write(page)
for tit, _, patas in COMBOS:
    xs = [pk(k, s) for k, s in patas]; c = math.prod(x['cuota'] for x in xs); p = math.prod(x['p'] for x in xs); pm = math.prod(x['p_mercado'] for x in xs)
    print(tit, f"cuota {c:.2f} p_modelo {p*100:.1f}% p_mercado {pm*100:.1f}% EV {(p*c-1)*100:+.1f}%")
print(len(page))
