"""
Genera val/backtest_estrategia.html — informe compacto del backtest.
"""
import json, os

LIGA_NOMBRES = {
    'E0':'Premier League','SP1':'La Liga','D1':'Bundesliga',
    'I1':'Serie A','F1':'Ligue 1','BRA':'Brasileirao'
}
MERCADO_LABEL = {
    'goles_1.5':'Goles >1.5','goles_2.5':'Goles >2.5','goles_3.5':'Goles >3.5',
    'corners_8.5':'Córners >8.5','corners_9.5':'Córners >9.5','corners_10.5':'Córners >10.5',
    'remates_20':'Remates >20','remates_25':'Remates >25',
    'arco_8':'Tiros arco >8','arco_10':'Tiros arco >10',
    'faltas_20':'Faltas >20','faltas_24':'Faltas >24',
    'tarj_2':'Tarjetas pts >2','tarj_3':'Tarjetas pts >3','tarj_4':'Tarjetas pts >4',
}

def color(pct, n):
    if n < 50 or pct is None: return '#888','#fff'
    if pct >= 75: return '#1a7a4a','#fff'
    if pct >= 65: return '#2d9f5c','#fff'
    if pct >= 55: return '#6abf69','#000'
    if pct >= 45: return '#f0c040','#000'
    return '#c0392b','#fff'

def td(d):
    n = d['n']; p = d['acierto_pct']
    if n == 0: return '<td class="empty">—</td>'
    bg,fg = color(p,n)
    return f'<td style="background:{bg};color:{fg}" title="{n} partidos">{p:.0f}%<small> {n}</small></td>'

with open('val/backtest_estrategia.json') as f:
    data = json.load(f)

res = data['resumen']
by_liga = data['por_liga']
cfg = data['config']

buckets = ['ambos','solo_local','solo_visita','ninguno']
bucket_label = {'ambos':'Ambos ≥7/10','solo_local':'Solo local','solo_visita':'Solo visita','ninguno':'Ninguno'}

# tabla global
rows_global = []
for lname, bkts in sorted(res.items()):
    rows_global.append(f"""<tr>
      <td class="lname">{MERCADO_LABEL.get(lname,lname)}</td>
      {''.join(td(bkts[b]) for b in buckets)}
    </tr>""")

# tablas por liga
liga_tabs = []
liga_content = []
for liga in sorted(by_liga):
    nombre = LIGA_NOMBRES.get(liga, liga)
    rows = []
    for lname in sorted(by_liga[liga]):
        rows.append(f"""<tr>
          <td class="lname">{MERCADO_LABEL.get(lname,lname)}</td>
          {''.join(td(by_liga[liga][lname][b]) for b in buckets)}
        </tr>""")
    liga_tabs.append(f'<button class="ltab" data-liga="{liga}">{nombre}</button>')
    liga_content.append(f"""<div class="lsec" id="liga-{liga}" style="display:none">
      <table class="bt"><thead><tr>
        <th>Mercado</th>{''.join(f'<th>{bucket_label[b]}</th>' for b in buckets)}
      </tr></thead><tbody>{''.join(rows)}</tbody></table>
    </div>""")

HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Backtest estrategia 7/10 — 5 grandes + Brasil</title>
<style>
body{{font-family:system-ui,sans-serif;background:#0f1117;color:#e0e0e0;margin:0;padding:16px}}
h1{{font-size:1.3rem;margin:0 0 4px}}
.sub{{color:#888;font-size:.85rem;margin-bottom:16px}}
.info{{background:#1a1f2e;border-radius:8px;padding:12px 16px;font-size:.85rem;margin-bottom:16px;line-height:1.6}}
.legend{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}}
.leg{{padding:3px 10px;border-radius:4px;font-size:.8rem}}
table.bt{{border-collapse:collapse;width:100%;font-size:.85rem}}
table.bt th{{background:#1e2535;padding:8px 10px;text-align:center;font-weight:600;font-size:.8rem}}
table.bt th:first-child{{text-align:left}}
table.bt td{{padding:7px 10px;text-align:center;border-bottom:1px solid #1e2535}}
table.bt td.lname{{text-align:left;font-weight:500;white-space:nowrap}}
table.bt td.empty{{color:#555}}
table.bt small{{font-size:.7rem;opacity:.7}}
.tabs{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px}}
button.tab,button.ltab{{background:#1e2535;border:none;color:#e0e0e0;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.82rem}}
button.tab.active,button.ltab.active{{background:#2d4a7a;color:#fff}}
.section{{display:none}}.section.active{{display:block}}
</style>
</head>
<body>
<h1>📊 Backtest estrategia 7 de 10</h1>
<div class="sub">
  5 grandes ligas europeas + Brasileirao · {sum(len(d['ambos']['acierto_pct'] and [1] or []) for d in res.values() if True):,} análisis ·
  Regla: ≥{cfg['UMBRAL_CUMPLE']} de {cfg['N']} partidos anteriores con la línea cumplida
</div>

<div class="info">
  <strong>Cómo leer esto:</strong> cada celda muestra el % de partidos donde la línea se dio,
  y entre paréntesis cuántos partidos. <em>Ambos ≥7/10</em> = ambos equipos tenían regularidad.
  <em>Solo local / Solo visita</em> = solo uno tenía regularidad.
  <em>Ninguno</em> = ninguno cumplía el filtro.<br>
  <strong>Esperado sin filtro:</strong> la cuota de Betano implica un %. El filtro sirve si <em>Ambos</em> supera claramente a <em>Ninguno</em>.
</div>

<div class="legend">
  <span class="leg" style="background:#1a7a4a;color:#fff">≥75% muy regular</span>
  <span class="leg" style="background:#2d9f5c;color:#fff">65–74% regular</span>
  <span class="leg" style="background:#6abf69;color:#000">55–64% moderado</span>
  <span class="leg" style="background:#f0c040;color:#000">45–54% débil</span>
  <span class="leg" style="background:#c0392b;color:#fff">&lt;45% no sirve</span>
</div>

<div class="tabs">
  <button class="tab active" data-sec="global">Resumen global</button>
  <button class="tab" data-sec="ligas">Por liga</button>
</div>

<div id="global" class="section active">
  <table class="bt">
    <thead><tr>
      <th>Mercado</th>
      {''.join(f'<th>{bucket_label[b]}</th>' for b in buckets)}
    </tr></thead>
    <tbody>{''.join(rows_global)}</tbody>
  </table>
</div>

<div id="ligas" class="section">
  <div class="tabs" id="liga-tabs">
    {''.join(liga_tabs)}
  </div>
  {''.join(liga_content)}
</div>

<script>
document.querySelectorAll('.tab').forEach(btn=>{{
  btn.addEventListener('click',()=>{{
    document.querySelectorAll('.tab').forEach(b=>b.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.sec).classList.add('active');
  }});
}});
(function(){{
  const first = document.querySelector('.ltab');
  if(first) {{
    first.classList.add('active');
    document.getElementById('liga-'+first.dataset.liga).style.display='block';
  }}
  document.querySelectorAll('.ltab').forEach(btn=>{{
    btn.addEventListener('click',()=>{{
      document.querySelectorAll('.ltab').forEach(b=>b.classList.remove('active'));
      document.querySelectorAll('.lsec').forEach(s=>s.style.display='none');
      btn.classList.add('active');
      document.getElementById('liga-'+btn.dataset.liga).style.display='block';
    }});
  }});
}})();
</script>
</body>
</html>"""

os.makedirs('val', exist_ok=True)
with open('val/backtest_estrategia.html','w') as f:
    f.write(HTML)
print("OK → val/backtest_estrategia.html")
