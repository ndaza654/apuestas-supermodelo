# -*- coding: utf-8 -*-
"""Genera el informe de auditoría (HTML autónomo + Markdown) a partir de aud_hallazgos.py.
    python3 aud_informe.py <salida.html> <salida.md> "<fecha y hora Bogotá>" <commit>"""
import json, re, sys, html as _h
import aud_hallazgos as A

out_html, out_md, cuando, commit = sys.argv[1:5]
SEV = ['crítico', 'alto', 'medio', 'bajo', 'bien']
CAMPOS = ['id', 'sev', 'area', 'titulo', 'que', 'evidencia', 'importa', 'hacer', 'esfuerzo', 'veredicto']
HS = [dict(zip(CAMPOS, h)) for h in A.H]
b = lambda t: re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', _h.escape(t))
cnt = lambda s: sum(1 for h in HS if h['sev'] == s)
LEIDO = ('Se leyó: CLAUDE.md, recoleccion/README.md, BITACORA, ESTADO e INDICE; registro/ completo (lineas.csv, sugerencias.csv, historial, libro); '
         'el código de supermodelo/ y recoleccion/; agentes, skills y documentos de la raíz; el inventario de archivos versionados. '
         'No se leyó: los JSON crudos de flashscore/ y betano/, el historial de git anterior al 12-nov ni las páginas de Betano y Flashscore.')

# ------------------------------------------------------------------ Markdown
M = [f'# Auditoría del repo apuestas-supermodelo', '',
     f'- **Fecha y hora:** {cuando} (Bogotá).', f'- **Commit auditado:** `{commit}` (rama `recoleccion/2026-11-14`).', f'- **Alcance:** {LEIDO}',
     '- **Reproducir las cifras:** scripts y salidas en `jornadas/2026-11-14/auditoria/`.', '',
     '## Conclusión en 10 líneas', ''] + [f'{i}. {t}' for i, t in enumerate(A.RESUMEN, 1)] + ['', '## Semáforo por área', '', '| Área | Estado | Lectura |', '|---|---|---|']
M += [f"| {k} · {A.AREAS[k]} | {A.SEMAFORO[k][0]} | {A.SEMAFORO[k][1]} |" for k in A.AREAS]
M += ['', f"## Hallazgos ({len(HS)}: {cnt('crítico')} críticos, {cnt('alto')} altos, {cnt('medio')} medios, {cnt('bajo')} bajos, {cnt('bien')} cosas que están bien)", '']
for tit, filtro in (('Lo malo (críticos y altos)', lambda h: h['sev'] in ('crítico', 'alto')), ('Lo que se puede mejorar (medios y bajos)', lambda h: h['sev'] in ('medio', 'bajo')),
                    ('Lo que está bien', lambda h: h['sev'] == 'bien')):
    M += [f'### {tit}', '']
    for h in sorted([h for h in HS if filtro(h)], key=lambda h: (SEV.index(h['sev']), h['id'])):
        M += [f"#### {h['id']} · {h['titulo']}", '', f"- **Severidad:** {h['sev']} · **Área:** {h['area']} ({A.AREAS[h['area']]}) · **Veredicto:** {h['veredicto']} · **Esfuerzo:** {h['esfuerzo']}",
              f"- **Qué pasa:** {h['que']}", f"- **Evidencia:** {h['evidencia']}", f"- **Por qué importa:** {h['importa']}", f"- **Qué hacer:** {h['hacer']}", '']
M += ['## Plan priorizado', '']
for tit, items in A.PLAN:
    M += [f'### {tit}', ''] + [f'{i}. {t}' for i, t in enumerate(items, 1)] + ['']
M += ['## Límites de esta auditoría', ''] + [f'- {t}' for t in A.LIMITES] + ['']
open(out_md, 'w', encoding='utf8').write('\n'.join(M))

# ------------------------------------------------------------------ HTML
D = {'H': HS, 'areas': A.AREAS}
PL = r'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Auditoría del repo</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--fg:#14181f;--mut:#5b6573;--line:#dfe3e9;--acc:#0a6b4f;--acc2:#e8f3ee;--bad:#b3261e;--bad2:#fbeceb;--warn:#8a5a00;--warn2:#fdf3dc;--chip:#eef1f5}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f1318;--card:#171c23;--fg:#e8ecf1;--mut:#9aa6b4;--line:#2a313b;--acc:#4cc59a;--acc2:#16302a;--bad:#ff8a80;--bad2:#3a1d1b;--warn:#f2c14e;--warn2:#3a2f14;--chip:#222a34;color-scheme:dark}}
:root[data-theme=dark]{--bg:#0f1318;--card:#171c23;--fg:#e8ecf1;--mut:#9aa6b4;--line:#2a313b;--acc:#4cc59a;--acc2:#16302a;--bad:#ff8a80;--bad2:#3a1d1b;--warn:#f2c14e;--warn2:#3a2f14;--chip:#222a34;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding:0 max(16px,env(safe-area-inset-right,0px)) 40px max(16px,env(safe-area-inset-left,0px))}
main{max-width:980px;margin:0 auto}h1{font-size:22px;margin:18px 0 4px}h2{font-size:17px;margin:26px 0 10px}h3{font-size:15px;margin:0 0 6px}
.sub{color:var(--mut);font-size:13px}.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;margin-bottom:10px;min-width:0}
ol,ul{margin:6px 0;padding-left:22px}li{margin:5px 0}
.sem{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.dot{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:7px;vertical-align:baseline}.rojo{background:var(--bad)}.ámbar{background:var(--warn)}.verde{background:var(--acc)}
.pill{display:inline-block;border-radius:99px;padding:1px 9px;font-size:12px;background:var(--chip);white-space:nowrap}
.s-crítico{background:var(--bad2);color:var(--bad);font-weight:600}.s-alto{background:var(--warn2);color:var(--warn);font-weight:600}.s-bien{background:var(--acc2);color:var(--acc);font-weight:600}
.filters{display:flex;flex-wrap:wrap;gap:8px;align-items:end;position:sticky;top:0;background:var(--bg);padding:8px 0;z-index:3}
.filters label{display:flex;flex-direction:column;font-size:12px;color:var(--mut);gap:2px}
select,input{font:inherit;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:6px;padding:6px 8px;min-width:0;max-width:100%}input[type=search]{width:180px}
button{font:inherit;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 11px;cursor:pointer}
.h dl{display:grid;grid-template-columns:120px 1fr;gap:4px 12px;margin:8px 0 0}.h dt{color:var(--mut);font-size:13px}.h dd{margin:0;overflow-wrap:anywhere}
.h .top{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:4px}.id{font-variant-numeric:tabular-nums;color:var(--mut);font-size:13px}
@media(max-width:560px){.h dl{grid-template-columns:1fr}.h dt{margin-top:6px}.filters{position:static}}
</style></head><body><main>
<h1>Auditoría del repo apuestas-supermodelo</h1>
<div class="sub">__CUANDO__ (Bogotá) · commit auditado <code>__COMMIT__</code> · rama recoleccion/2026-11-14</div>
<div class="card" style="margin-top:12px"><h3>Conclusión en 10 líneas</h3><ol>__RESUMEN__</ol></div>
<h2>Semáforo por área</h2><div class="sem">__SEM__</div>
<h2>Hallazgos</h2>
<div class="filters"><label>Severidad<select id="fs"><option value="">todas</option>__OPSEV__</select></label><label>Área<select id="fa"><option value="">todas</option>__OPAREA__</select></label><label>Veredicto<select id="fv"><option value="">todos</option>__OPVER__</select></label><label>Buscar<input type="search" id="fq" placeholder="palabra o ID"></label><button id="fx">Quitar filtros</button><span class="sub" id="cnt"></span></div>
<div id="lista"></div>
<h2>Plan priorizado</h2>__PLAN__
<h2>Límites de esta auditoría</h2><div class="card"><p class="sub">__LEIDO__</p><ul>__LIM__</ul><p class="sub">Las cifras se reproducen con los scripts de <code>jornadas/2026-11-14/auditoria/</code>.</p></div>
</main><script>
const D=/*DATA*/;const $=s=>document.querySelector(s);
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const ORD=['crítico','alto','medio','bajo','bien'];
function pinta(){const s=$('#fs').value,a=$('#fa').value,v=$('#fv').value,q=$('#fq').value.trim().toLowerCase();
 const L=D.H.filter(h=>(!s||h.sev===s)&&(!a||h.area===a)&&(!v||h.veredicto===v)&&(!q||(h.id+' '+h.titulo+' '+h.que+' '+h.evidencia+' '+h.hacer).toLowerCase().includes(q))).sort((x,y)=>ORD.indexOf(x.sev)-ORD.indexOf(y.sev)||x.id.localeCompare(y.id,'es',{numeric:true}));
 $('#cnt').textContent=L.length+' de '+D.H.length+' hallazgos';
 $('#lista').innerHTML=L.length?L.map(h=>`<div class="card h"><div class="top"><span class="id">${esc(h.id)}</span><span class="pill s-${esc(h.sev)}">${esc(h.sev)}</span><span class="pill">${esc(D.areas[h.area])}</span><span class="pill">${esc(h.veredicto)}</span>${h.esfuerzo!=='—'?`<span class="pill">esfuerzo ${esc(h.esfuerzo)}</span>`:''}</div><h3>${esc(h.titulo)}</h3><div>${esc(h.que)}</div><dl><dt>Evidencia</dt><dd>${esc(h.evidencia)}</dd><dt>Por qué importa</dt><dd>${esc(h.importa)}</dd><dt>Qué hacer</dt><dd>${esc(h.hacer)}</dd></dl></div>`).join(''):'<div class="card sub">Ningún hallazgo pasa esos filtros.</div>'}
['fs','fa','fv','fq'].forEach(id=>{$('#'+id).oninput=pinta;$('#'+id).onchange=pinta});
$('#fx').onclick=()=>{['fs','fa','fv','fq'].forEach(id=>$('#'+id).value='');pinta()};
document.querySelectorAll('[data-area]').forEach(e=>e.onclick=()=>{$('#fa').value=e.dataset.area;$('#fs').value='';$('#fv').value='';$('#fq').value='';pinta();$('#lista').scrollIntoView({block:'start'})});
pinta();
</script></body></html>'''
sem = ''.join(f'<div class="card" style="margin:0"><h3><span class="dot {A.SEMAFORO[k][0]}"></span>{k} · {_h.escape(A.AREAS[k])}</h3><div>{_h.escape(A.SEMAFORO[k][1])}</div>'
              f'<div style="margin-top:8px"><button data-area="{k}">Ver sus {sum(1 for h in HS if h["area"] == k)} hallazgos</button></div></div>' for k in A.AREAS)
plan = ''.join(f'<div class="card"><h3>{_h.escape(t)}</h3><ol>' + ''.join(f'<li>{_h.escape(x)}</li>' for x in items) + '</ol></div>' for t, items in A.PLAN)
vers = sorted({h['veredicto'] for h in HS})
html = (PL.replace('__CUANDO__', _h.escape(cuando)).replace('__COMMIT__', _h.escape(commit))
        .replace('__RESUMEN__', ''.join(f'<li>{b(t)}</li>' for t in A.RESUMEN)).replace('__SEM__', sem)
        .replace('__OPSEV__', ''.join(f'<option value="{s}">{s} ({cnt(s)})</option>' for s in SEV))
        .replace('__OPAREA__', ''.join(f'<option value="{k}">{k} · {_h.escape(v)}</option>' for k, v in A.AREAS.items()))
        .replace('__OPVER__', ''.join(f'<option>{v}</option>' for v in vers))
        .replace('__PLAN__', plan).replace('__LEIDO__', _h.escape(LEIDO)).replace('__LIM__', ''.join(f'<li>{_h.escape(t)}</li>' for t in A.LIMITES))
        .replace('/*DATA*/', json.dumps(D, ensure_ascii=False).replace('</', '<\\/')))
open(out_html, 'w', encoding='utf8').write(html)
print(out_html, len(html) // 1024, 'KB ·', len(HS), 'hallazgos:', {s: cnt(s) for s in SEV})
