# -*- coding: utf-8 -*-
"""Informe interactivo de una jornada (HTML autónomo: sin red, sin librerías) a partir de lo que ya está en el repo.

    python3 recoleccion/informe_html.py jornadas/2026-11-14 [salida.html]

Lee    registro/lineas.csv (filas de esa jornada: TODAS las líneas, cumplan o no) + <jornada>/ranking.json
       (+ <jornada>/informes/*_resultado.json para el 1X2 del modelo, <jornada>/ESTADO.md para «Datos y límites»)
Escribe <jornada>/informe.html  (por defecto)
Es solo lectura de lo ya recolectado: no apuesta, no lee la red, no inventa datos. Lo que falta sale como vacío o «sin dato».
Reglas del proyecto que respeta: el colchón es informativo (ningún filtro lo usa por defecto, no se oculta ninguna línea por colchón);
la probabilidad del modelo es la de la línea; «cumple» = ≥ K de N en ambos equipos con K ajustable en el propio informe
(por defecto 7 de 10; si la jornada se recogió con 7 partidos, 5 de 7).
"""
import os, sys, csv, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ficha as FI

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U_COP = 3700   # CLAUDE.md: 1 u = 3.700 COP


def num(x):
    try:
        return round(float(x), 4)
    except (TypeError, ValueError):
        return None


def cargar(base):
    jor = os.path.basename(os.path.normpath(base))
    ruta = os.path.join(RAIZ, 'registro', 'lineas.csv')
    if not os.path.exists(ruta):
        raise SystemExit('No existe registro/lineas.csv: corre antes recoleccion/correr_jornada.py ' + base)
    filas = [r for r in csv.DictReader(open(ruta, encoding='utf-8-sig'), delimiter=';') if r['jornada'] == jor]
    if not filas:
        raise SystemExit(f'registro/lineas.csv no tiene filas de {jor}: corre antes `python3 recoleccion/correr_jornada.py {base}`.')
    rk = {}
    p = os.path.join(base, 'ranking.json')
    if os.path.exists(p):
        for r in json.load(open(p, encoding='utf8')):
            rk[r['partido']] = r
    res = {}
    for f in glob.glob(os.path.join(base, 'informes', '*_resultado.json')):
        try:
            d = json.load(open(f, encoding='utf8'))
        except Exception:
            continue
        res[d.get('local', '') + ' - ' + d.get('visitante', '')] = d
    estado = ''
    p = os.path.join(base, 'ESTADO.md')
    if os.path.exists(p):
        estado = open(p, encoding='utf8').read()
    return jor, filas, rk, res, estado


def datos(jor, filas, rk, res, estado):
    orden = []
    for r in filas:
        if r['partido'] not in orden:
            orden.append(r['partido'])
    orden.sort(key=lambda n: next(x['hora_partido'] for x in filas if x['partido'] == n))
    P = []
    for n in orden:
        f = next(x for x in filas if x['partido'] == n)
        k = rk.get(n, {})
        pr = k.get('probabilidades_1x2') or {}
        P.append({'n': n, 'liga': f['liga'], 'hora': f['hora_partido'], 'leido': f['cuotas_leidas'], 'estado': k.get('estado', ''),
                  'datos': k.get('datos'), 'motivos': k.get('motivos', []), 'cumplen': k.get('lineas_que_cumplen'),
                  'p1': num(pr.get('1')), 'px': num(pr.get('X')), 'p2': num(pr.get('2'))})
    idx = {n: i for i, n in enumerate(orden)}
    F = []
    for r in filas:
        F.append([idx[r['partido']], r['mercado'], r['ambito'], r['jugador'], num(r['titular']) if r['titular'] != '' else None, num(r['linea']) if r['linea'] != '' else None,
                  r['lado'], num(r['cuota']), num(r['esperado']), num(r['colchon']), r['reg_local'], r['reg_visitante'], r['directos'],
                  r['cumple_ficha'], num(r['p_modelo']), num(r['p_mercado']), num(r['ev_modelo']), r['alerta_modelo'], r['sistemas_partido'], r['nota']])
    # muestra real de esta jornada (10 con la regla actual; 7 en las recolectadas antes del 13-nov) y umbral por defecto proporcional
    nmax = 0
    for r in filas:
        for c in (r['reg_local'], r['reg_visitante']):
            m = re.search(r'de (\d+)', c or '')
            if m:
                nmax = max(nmax, int(m.group(1)))
    nmax = nmax or FI.N
    K0 = FI.CUMPLE if nmax >= FI.N else max(1, round(FI.CUMPLE * nmax / FI.N))
    MN0 = FI.MIN_N if nmax >= FI.N else max(1, round(FI.MIN_N * nmax / FI.N))
    return {'jor': jor, 'u': U_COP, 'P': P, 'F': F, 'estado': estado, 'N': nmax, 'K': K0, 'MN': MN0}


def _md(t):
    """Markdown mínimo (títulos ##, viñetas -, **negrita**) -> HTML escapado; para el bloque «Enfoque de mercados»."""
    esc = lambda x: x.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    out, lista = [], False
    for ln in t.splitlines():
        ln = ln.rstrip()
        h = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', esc(ln.lstrip('#- ').strip()))
        if ln.startswith('- '):
            if not lista:
                out.append('<ul>')
                lista = True
            out.append(f'<li>{h}</li>')
            continue
        if lista:
            out.append('</ul>')
            lista = False
        if ln.startswith('#'):
            out.append(f'<h3>{h}</h3>')
        elif ln:
            out.append(f'<p>{h}</p>')
    if lista:
        out.append('</ul>')
    return '\n'.join(out)


def analisis(base, d):
    """Pestaña «Análisis»: <jornada>/analisis.json (de analisis_jornada.py) + <jornada>/enfoque.md (lo escribe Claude). Sin ellos no hay pestaña."""
    p = os.path.join(base, 'analisis.json')
    if not os.path.exists(p):
        return None
    A = json.load(open(p, encoding='utf8'))
    pidx = {x['n']: i for i, x in enumerate(d['P'])}
    lado = {'Más': 'Más', 'Menos': 'Menos'}
    idx = {(r[0], r[1], r[2], r[5], r[6]): i for i, r in enumerate(d['F']) if r[3] in ('', None)}

    def fila(c):
        return idx.get((pidx.get(c['partido']), c['mercado'], c['ambito'], num(c['linea']), lado.get(c['lado'], c['lado'])))

    S = []
    for et, lista in (('protección', A.get('proteccion', [])), ('sencilla 1,50–1,99', A.get('sencillas', []))):
        for c in lista:
            S.append({'t': et, 'h': c['hora'], 'n': c['partido'], 'x': c['texto'], 'm': c['mercado'], 'c': c['cuota'], 'p': c['p'], 'pr': c['p_rec'],
                      'L': c['L'], 'V': c['V'], 'D': c['D'], 'col': c.get('colchon'), 'real': c['real'], 'i': [fila(c)]})
    for c in A.get('combinadas', []):
        S.append({'t': 'combinada de 2 patas', 'h': c['hora'], 'n': c['partido'], 'x': c['texto'], 'm': ' + '.join(x['mercado'] for x in c['patas']), 'c': c['cuota'],
                  'p': c['p_ajust'], 'pr': c['p_rec'], 'L': ' · '.join(x['L'] for x in c['patas']), 'V': ' · '.join(x['V'] for x in c['patas']),
                  'D': ' · '.join(x['D'] or '–' for x in c['patas']), 'col': None,
                  'real': f"simulación {c['p_sim']:.0%}, ajustada {c['p_ajust']:.0%}, recortada {A['reglas']['recorte_combo']:.0%}; correlación {c.get('correlacion')}; guion común: {c.get('guion')}; pata más frágil: {c.get('fragil')}",
                  'i': [fila(x) for x in c['patas']]})
    lot = A.get('loteria')
    if lot:
        S.append({'t': 'lotería (stake mínimo)', 'h': min(x['hora'] for x in lot['patas']), 'n': 'varios (3 partidos)', 'x': lot['texto'], 'm': 'varios', 'c': lot['cuota'],
                  'p': lot['p'], 'pr': lot['p_rec'], 'L': '', 'V': '', 'D': '', 'col': None, 'real': 'tres patas de partidos distintos: producto de sus p recortadas',
                  'i': [fila(x) for x in lot['patas']]})
    e = os.path.join(base, 'enfoque.md')
    return {'hecho': A.get('hecho'), 'leidas': A.get('cuotas_leidas'), 'muestra': A.get('muestra'), 'cumple': A.get('cumple'), 'reglas': A.get('reglas'),
            'real': A.get('real'), 'P': A.get('partidos'), 'S': S, 'saltados': A.get('combos_saltados_por_alerta', []), 'n_cumplen': A.get('n_cumplen'),
            'jh': A.get('n_jugadores_con_historial'), 'enfoque': _md(open(e, encoding='utf8').read()) if os.path.exists(e) else ''}


PLANTILLA = r'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Informe __JOR__</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--fg:#14181f;--mut:#5b6573;--line:#dfe3e9;--acc:#0a6b4f;--acc2:#e8f3ee;--bad:#b3261e;--warn:#9a6700;--chip:#eef1f5}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f1318;--card:#171c23;--fg:#e8ecf1;--mut:#9aa6b4;--line:#2a313b;--acc:#4cc59a;--acc2:#16302a;--bad:#ff8a80;--warn:#f2c14e;--chip:#222a34;color-scheme:dark}}
:root[data-theme=dark]{--bg:#0f1318;--card:#171c23;--fg:#e8ecf1;--mut:#9aa6b4;--line:#2a313b;--acc:#4cc59a;--acc2:#16302a;--bad:#ff8a80;--warn:#f2c14e;--chip:#222a34;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding-left:max(14px,env(safe-area-inset-left,0px));padding-right:max(14px,env(safe-area-inset-right,0px))}
h1{font-size:20px;margin:14px 0 2px}h2{font-size:15px;margin:0 0 8px}.sub{color:var(--mut);margin-bottom:10px}
nav{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0;position:sticky;top:0;background:var(--bg);padding:6px 0;z-index:5}
nav button,.chip,button.b{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;padding:6px 11px;cursor:pointer;font:inherit}
nav button.on,.chip.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px;margin-bottom:10px;min-width:0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
.pill{display:inline-block;border-radius:99px;padding:1px 8px;font-size:12px;background:var(--chip)}.apto{background:var(--acc2);color:var(--acc)}.res{background:var(--chip)}.no{color:var(--bad)}
.filters{display:flex;flex-wrap:wrap;gap:8px;align-items:end}.filters label{display:flex;flex-direction:column;font-size:12px;color:var(--mut);gap:2px}
select,input{font:inherit;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:6px;padding:5px 7px;min-width:0}input[type=number]{width:78px}input[type=search]{width:170px}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--card)}table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:5px 8px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}th{cursor:pointer;color:var(--mut);position:sticky;top:0;background:var(--card)}td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
tr:hover td{background:var(--acc2)}.ok{color:var(--acc);font-weight:600}.mut{color:var(--mut)}.bad{color:var(--bad)}.warn{color:var(--warn)}
.bar{height:10px;border-radius:5px;background:var(--acc);display:inline-block;vertical-align:middle}.bar2{background:var(--warn)}
.row{display:flex;gap:10px;align-items:center;margin:3px 0}.row .t{flex:0 0 190px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.row .v{flex:1;min-width:0}
pre{white-space:pre-wrap;word-break:break-word;font:12.5px/1.5 ui-monospace,Menlo,monospace}.small{font-size:12px}
.enf h3{font-size:14px;margin:12px 0 4px}.enf p,.enf ul{margin:4px 0;max-width:95ch}.enf ul{padding-left:20px}.enf li{margin:3px 0}
@media(max-width:560px){.row .t{flex-basis:110px}}
</style></head><body>
<h1>Informe interactivo · <span id="jor"></span></h1>
<div class="sub" id="sub"></div>
<div class="card" id="kbar"></div>
<nav id="nav"></nav><div id="app"></div>
<script>
const D=/*DATA*/;
const $=(s,e)=>(e||document).querySelector(s),pct=x=>x==null?'–':(100*x).toFixed(0)+'%',f2=x=>x==null?'–':(+x).toFixed(2);
const MERC=[...new Set(D.F.map(r=>r[1]))].sort(),AMB=[...new Set(D.F.map(r=>r[2]))].sort();
const bog=s=>{try{return new Date(s).toLocaleString('es-CO',{timeZone:'America/Bogota',day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false})}catch(e){return s}};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let K=D.K,MN=D.MN,MODO='ambos',TF={tp:0.7,tc:1.3,tm:'',ts:false},TAB=D.A?'ana':'res',FA={},SEL=new Set(),CUP=[],stake=1,sortK={l:['p',-1],j:['c',-1]},LIM={l:200,j:200},Fil={l:{},j:{}};
const isJ=r=>r[1].startsWith('jugador:');
const rg=s=>{const m=/(\d+)\s*de\s*(\d+)/.exec(s||'');return m?[+m[1],+m[2]]:null};
/* «cumple» dinámico: true / false / null (sin muestra o sin alineación). Equipo: ambos equipos (o el modo elegido) con ≥k veces y n ≥ MN. Jugador: su historial. */
function cum(r,k){k=k==null?K:k;if(r[13]==='sin alineación')return null;const a=rg(r[10]);
 if(isJ(r)){return a?(a[1]>=MN&&a[0]>=k):null}
 const b=rg(r[11]);if(!a||!b)return null;const t=x=>x[1]>=MN&&x[0]>=k;
 return MODO==='local'?t(a):MODO==='visitante'?t(b):MODO==='alguno'?(t(a)||t(b)):(t(a)&&t(b))}
const cumTxt=r=>{const c=cum(r);return c===true?'<span class="ok">sí</span>':c===false?'no':esc(r[13]==='sí'||r[13]==='no'?'sin muestra':r[13])};
function kbar(){const B=$('#kbar'),ks=[];for(let i=Math.max(1,D.N-5);i<=D.N;i++)ks.push(i);
 B.innerHTML=`<div class="filters"><label>«Cumple» = al menos<input type="number" id="kk" min="1" max="${D.N}" value="${K}" style="width:64px"></label><label>de ${D.N} partidos · n mínimo<input type="number" id="kmn" min="1" max="${D.N}" value="${MN}" style="width:64px"></label><label>En<select id="kmodo"><option value="ambos" ${MODO==='ambos'?'selected':''}>ambos equipos</option><option value="local" ${MODO==='local'?'selected':''}>solo el local</option><option value="visitante" ${MODO==='visitante'?'selected':''}>solo el visitante</option><option value="alguno" ${MODO==='alguno'?'selected':''}>cualquiera de los dos</option></select></label><label>Atajos<span>${ks.map(k=>`<button class="b small ${K===k?'on':''}" data-k="${k}" style="margin-right:4px">${k}</button>`).join('')}</span></label></div><div class="small mut" style="margin-top:6px">Cambia el mínimo y todo el informe se recalcula (resumen, mejores líneas, tablas y cupón). Es solo un filtro de lectura: el colchón sigue siendo informativo y ninguna línea se oculta por él.</div>`;
 const ch=()=>{K=Math.max(1,Math.min(D.N,+$('#kk').value||K));MN=Math.max(1,Math.min(D.N,+$('#kmn').value||MN));MODO=$('#kmodo').value;kbar();draw(true)};
 B.oninput=null;B.onchange=ch;B.onclick=e=>{const k=e.target.dataset.k;if(k){K=+k;kbar();draw(true)}}}
const nm=r=>isJ(r)?r[3]+' · '+r[1].slice(8):r[1]+(r[2]!=='total'?' '+r[2]:'');
$('#jor').textContent=D.jor;
$('#sub').textContent=D.P.length+' partidos · '+D.F.length.toLocaleString('es-CO')+' líneas de Betano (cumplan o no) · hora de Bogotá · 1 u = $'+D.u.toLocaleString('es-CO')+' COP. Solo lectura: el informe no apuesta.';
const TABS=[...(D.A?[['ana','Análisis']]:[]),['res','Resumen'],['l','Líneas de equipo'],['j','Jugadores'],['cup','Cupón'],['dat','Datos y límites']];
function nav(){$('#nav').innerHTML=TABS.map(([k,t])=>`<button class="${TAB===k?'on':''}" data-k="${k}">${t}${k==='cup'&&CUP.length?' ('+CUP.length+')':''}</button>`).join('');$('#nav').onclick=e=>{const k=e.target.dataset.k;if(k){TAB=k;draw()}}}
function draw(keep){const A=$('#app');A.oninput=A.onchange=A.onclick=null;nav();const y=window.scrollY;({ana:vAna,res:vRes,l:()=>vTab('l'),j:()=>vTab('j'),cup:vCup,dat:vDat})[TAB]();window.scrollTo(0,keep?y:0)}
function vRes(){
 const n=D.P.length,cm=D.P.map((_,i)=>D.F.filter(r=>r[0]===i&&!isJ(r)&&cum(r)===true).length),mx=Math.max(1,...cm);
 let h=`<div class="card"><h2>Cuántas líneas de equipo cumplen (≥ ${K} de ${D.N}, ${{ambos:'en ambos',local:'en el local',visitante:'en el visitante',alguno:'en alguno de los dos'}[MODO]}) por partido</h2>`+D.P.map((p,i)=>`<div class="row"><span class="t">${esc(p.n)}</span><span class="v"><span class="bar" style="width:${Math.max(2,82*cm[i]/mx)}%"></span> ${cm[i]}</span></div>`).join('')+`<p class="small mut">«Cumple» es un criterio de tipsters sin resultados verificados; el objetivo es la probabilidad de la línea.</p></div>`;
 const KS=[];for(let k=Math.max(1,D.N-5);k<=D.N;k++)KS.push(k);
 h+=`<div class="card"><h2>¿Cuántas líneas de equipo cumplen con otro mínimo? (por partido)</h2><div class="tw"><table><tr><th>Partido</th>${KS.map(k=>`<th class="n" style="${k===K?'color:var(--acc)':''}">≥ ${k} de ${D.N}</th>`).join('')}</tr>${D.P.map((p,i)=>`<tr><td>${esc(p.n)}</td>${KS.map(k=>`<td class="n ${k===K?'ok':''}">${D.F.filter(r=>r[0]===i&&!isJ(r)&&cum(r,k)===true).length}</td>`).join('')}</tr>`).join('')}</table></div><p class="small mut">Haz clic en un atajo de arriba para usar ese mínimo en todo el informe.</p></div>`;
 h+=`<div class="card"><h2>Mejores líneas del día (filtra y haz clic para agregar al cupón)</h2><div class="filters"><label>p modelo ≥<input type="number" id="tp" value="${TF.tp}" step="0.05" min="0" max="1"></label><label>Cuota ≥<input type="number" id="tc" value="${TF.tc}" step="0.05"></label><label>Mercado<select id="tm"><option value="">todos</option>${MERC.filter(m=>!m.startsWith('jugador')).map(m=>`<option ${TF.tm===m?'selected':''}>${m}</option>`).join('')}</select></label><label><span>&nbsp;</span><span><input type="checkbox" id="ts" ${TF.ts?'checked':''}> solo «cumple»</span></label></div><div id="top"></div></div>`;
 h+=`<div class="grid">`+D.P.map((p,i)=>`<div class="card"><b>${esc(p.n)}</b><div class="small mut">${esc(p.liga)} · ${bog(p.hora.replace(' ','T')+'-05:00')} Bogotá</div><div style="margin:6px 0"><span class="pill ${p.estado==='apto'?'apto':'res'}">${esc(p.estado||'sin ranking')}</span> <span class="small mut">datos ${p.datos??'–'}</span></div>${p.p1!=null?`<div class="small">1X2 modelo: <b>${pct(p.p1)}</b> · ${pct(p.px)} · ${pct(p.p2)}</div>`:''}<div class="small mut">${(p.motivos||[]).map(esc).join(' · ')}</div><button class="b small" data-p="${i}" style="margin-top:6px">Ver sus líneas</button></div>`).join('')+`</div>`;
 $('#app').innerHTML=h;
 const top=()=>{const tp=+$('#tp').value,tc=+$('#tc').value,m=$('#tm').value,s=$('#ts').checked;TF={tp,tc,tm:m,ts:s};
  const L=D.F.map((r,i)=>[r,i]).filter(([r])=>!isJ(r)&&r[14]!=null&&r[14]>=tp&&(r[7]||0)>=tc&&(!m||r[1]===m)&&(!s||cum(r)===true)).sort((a,b)=>b[0][14]-a[0][14]).slice(0,15);
  $('#top').innerHTML=L.length?`<div class="tw"><table><tr><th>Partido</th><th>Línea</th><th class="n">Cuota</th><th class="n">p</th><th class="n">EV</th><th>Cumple</th><th></th></tr>${L.map(([r,i])=>`<tr><td>${esc(D.P[r[0]].n)}</td><td>${esc(nm(r))} ${r[6]} ${r[5]??''}</td><td class="n">${f2(r[7])}</td><td class="n ok">${pct(r[14])}</td><td class="n ${r[16]<0?'bad':''}">${pct(r[16])}</td><td>${cumTxt(r)}</td><td><button class="b small" data-add="${i}">+</button></td></tr>`).join('')}</table></div>`:'<p class="mut">Ninguna línea cumple esos filtros.</p>'};
 ['tp','tc','tm','ts'].forEach(id=>$('#'+id).oninput=top);top();
 $('#app').onclick=e=>{const a=e.target.dataset.add,p=e.target.dataset.p;if(a!=null){add(+a)}if(p!=null){Fil.l={p:+p};TAB='l';draw()}}}
function add(i){if(!CUP.includes(i)){CUP.push(i);nav()}}
/* Pestaña «Análisis»: enfoque de mercados, «real hasta hoy» y sugerencias con las reglas de la auditoría (analisis_jornada.py) */
const NM={corners:'Córners',goles:'Goles',tarjetas:'Tarjetas',al_arco:'Tiros al arco',remates:'Remates',faltas:'Faltas',fueras:'Fueras de juego',saques_meta:'Saques de meta',saques_banda:'Saques de banda'};
const hh=s=>(s||'').slice(11,16);
function vAna(){const A=D.A,R=A.real,g=R.global_cumple;
 const rt=(o,f)=>Object.entries(o).map(([k,v])=>`<tr><td>${esc(f?f(k):k)}</td><td class="n">${v.n}</td><td class="n">${v.aciertos}</td><td class="n ${v.real!=null&&v.dicho!=null&&v.real<v.dicho-0.03?'bad':'ok'}">${pct(v.real)}</td><td class="n">${pct(v.dicho)}</td>${v.factor!=null?`<td class="n">× ${(+v.factor).toFixed(2)}</td>`:'<td></td>'}</tr>`).join('');
 const th='<tr><th>Grupo</th><th class="n">n</th><th class="n">Se dieron</th><th class="n">Real</th><th class="n">Dicho</th><th class="n">Recorte de p</th></tr>';
 let h=`<div class="card"><h2>Enfoque de mercados</h2><p class="small mut">Hecho: ${esc(A.hecho||'')} (Bogotá) · Cuotas: Betano, leídas ${A.leidas&&A.leidas.length?bog(A.leidas[0])+' a '+bog(A.leidas[1]):'sin dato'} (Bogotá), sin releer · Muestra de ${A.muestra} partidos por equipo: «cumple» = ${A.cumple} de ${A.muestra} en ambos · ${A.n_cumplen} líneas de equipo cumplen · jugadores con historial: ${A.jh||0} líneas.</p><div class="enf">${A.enfoque||'<p class="mut">Esta jornada no tiene enfoque.md.</p>'}</div></div>`;
 h+=`<div class="card"><h2>Sugerencias (reglas de la auditoría)</h2><p class="small mut">p recortada = p del modelo × el menor factor real (mercado-lado y banda de cuota). «Protección» = cuota &lt; ${f2(A.reglas.cuota_proteccion)}: se da, no paga. Combinadas: 2 patas del mismo partido, cada una ≥ ${pct(A.reglas.p_min)} recortada; conjunta de la simulación recortada ${pct(A.reglas.recorte_combo)}; la cuota es el producto (techo). El «+» lleva las patas al cupón.</p><div class="filters"><label>Tipo<select id="at"><option value="">todos</option>${[...new Set(A.S.map(s=>s.t))].map(t=>`<option ${FA.t===t?'selected':''}>${esc(t)}</option>`).join('')}</select></label><label>Partido<select id="an"><option value="">todos</option>${D.P.map(p=>`<option ${FA.n===p.n?'selected':''}>${esc(p.n)}</option>`).join('')}</select></label><label>Mercado<select id="am"><option value="">todos</option>${Object.keys(NM).filter(m=>A.S.some(s=>s.m.includes(m))).map(m=>`<option value="${m}" ${FA.m===m?'selected':''}>${NM[m]}</option>`).join('')}</select></label><label>p recortada ≥<input type="number" id="ap" step="0.05" min="0" max="1" value="${FA.p??''}"></label><label>Cuota ≥<input type="number" id="ac" step="0.05" value="${FA.c??''}"></label><label>Buscar<input type="search" id="aq" value="${esc(FA.q||'')}"></label><span class="small mut" id="acnt"></span></div><div class="tw" style="margin-top:8px"><table id="atb"></table></div></div>`;
 h+=`<div class="card"><h2>Real hasta hoy (lo que de verdad se dio)</h2><p class="small mut">Líneas de equipo con «cumple» ya calificadas: ${g.aciertos} de ${g.n} (${pct(g.real)} real contra ${pct(g.dicho)} dicho) en ${R.partidos} partidos. Muestra chica y con líneas del mismo partido correlacionadas: es un aviso, no una prueba.</p><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr))"><div class="tw"><table><tr><th colspan="6">Por mercado y lado (con «cumple»)</th></tr>${th}${rt(R.mercado_lado,k=>{const [m,l]=k.split('|');return (NM[m]||m)+' '+l})}</table></div><div><div class="tw"><table><tr><th colspan="6">Por banda de cuota (con «cumple»)</th></tr>${th}${rt(R.banda_cuota)}</table></div><div class="tw" style="margin-top:10px"><table><tr><th colspan="6">Mis sugerencias auditadas (4–13 nov)</th></tr>${th}${rt(R.sugerencias)}</table></div></div></div></div>`;
 h+=`<div class="card"><h2>Situación por partido (lo que hay en las fichas)</h2><div class="grid">${A.P.map(p=>`<div class="card" style="margin:0"><b>${hh(p.hora)} · ${esc(p.n)}</b><div class="small mut">${esc(p.liga)}</div><div class="small">1X2 modelo: <b>${pct(p.p1)}</b> · ${pct(p.px)} · ${pct(p.p2)}</div><div class="small">Tabla: ${esc(p.tabla)}</div><div class="small">Árbitro: ${esc(p.arbitro)} (sin estadísticas) · XI: ${esc(p.xi)}</div><div class="small mut">${esc(p.clima)}</div><div class="small">Cumplen: ${p.cumplen} (${Object.entries(p.cumplen_por_mercado).map(([m,n])=>(NM[m]||m)+' '+n).join(', ')||'ninguna'})</div>${p.familias_alerta.length?`<div class="small warn">⚠ Alerta del modelo en ${p.familias_alerta.map(m=>NM[m]||m).join(', ')}: la simulación se aleja del mercado</div>`:''}<div class="small mut">${esc(p.enfoque)}</div></div>`).join('')}</div></div>`;
 $('#app').innerHTML=h;
 const paint=()=>{FA={t:$('#at').value||undefined,n:$('#an').value||undefined,m:$('#am').value||undefined,p:$('#ap').value===''?undefined:+$('#ap').value,c:$('#ac').value===''?undefined:+$('#ac').value,q:$('#aq').value.trim().toLowerCase()||undefined,s:FA.s};
  let L=A.S.map((s,i)=>[s,i]).filter(([s])=>(!FA.t||s.t===FA.t)&&(!FA.n||s.n===FA.n||s.x.includes(FA.n))&&(!FA.m||s.m.includes(FA.m))&&(FA.p==null||s.pr>=FA.p)&&(FA.c==null||s.c>=FA.c)&&(!FA.q||(s.n+' '+s.x+' '+s.t).toLowerCase().includes(FA.q)));
  const [sk,sd]=FA.s||['pr',-1],kf={h:s=>s.h+s.n,c:s=>s.c,p:s=>s.p,pr:s=>s.pr,ev:s=>s.pr*s.c-1,t:s=>s.t}[sk];L.sort((a,b)=>{const x=kf(a[0]),y=kf(b[0]);return(x>y?1:x<y?-1:0)*sd});
  $('#acnt').textContent=L.length+' de '+A.S.length+' sugerencias';const ar=k=>sk===k?(sd<0?' ▼':' ▲'):'';
  $('#atb').innerHTML=`<tr><th data-s="h">Hora · partido · sugerencia${ar('h')}</th><th data-s="t">Tipo${ar('t')}</th><th class="n" data-s="c">Cuota${ar('c')}</th><th class="n" data-s="p">p modelo${ar('p')}</th><th class="n" data-s="pr">p recortada${ar('pr')}</th><th class="n" data-s="ev">EV con p recortada${ar('ev')}</th><th>Local</th><th>Visit.</th><th>Directos</th><th></th></tr>`+(L.length?L.map(([s,i])=>`<tr><td style="white-space:normal;min-width:210px;max-width:520px"><div class="small mut">${hh(s.h)} · ${esc(s.n)}</div><b>${esc(s.x)}</b><div class="small mut">Real hasta hoy: ${esc(s.real)}</div></td><td><span class="pill ${s.t==='protección'?'apto':''}">${esc(s.t)}</span></td><td class="n">${f2(s.c)}</td><td class="n">${pct(s.p)}</td><td class="n ok">${pct(s.pr)}</td><td class="n ${s.pr*s.c-1<0?'bad':''}">${pct(s.pr*s.c-1)}</td><td>${esc(s.L)}</td><td>${esc(s.V)}</td><td>${esc(s.D||'–')}</td><td><button class="b small" data-sg="${i}">+</button></td></tr>`).join(''):'<tr><td colspan="10" class="mut">Ninguna sugerencia pasa esos filtros.</td></tr>')};
 $('#app').oninput=paint;$('#app').onchange=paint;
 $('#app').onclick=e=>{const t=e.target;if(t.dataset.sg!=null){A.S[+t.dataset.sg].i.forEach(i=>{if(i!=null)add(i)});t.textContent='✓'}if(t.dataset.s){const k=t.dataset.s,c=FA.s||['pr',-1];FA.s=c[0]===k?[k,-c[1]]:[k,-1];paint()}};
 paint()}
function vTab(w){
 const F=Fil[w],rows=D.F.map((r,i)=>[r,i]).filter(([r])=>w==='j'?isJ(r):!isJ(r));
 const mset=[...new Set(rows.map(([r])=>r[1]))].sort(),aset=[...new Set(rows.map(([r])=>r[2]))].sort();
 let h=`<div class="card"><div class="filters"><label>Partido<select id="fp"><option value="">todos</option>${D.P.map((p,i)=>`<option value="${i}" ${F.p===i?'selected':''}>${esc(p.n)}</option>`).join('')}</select></label><label>Mercado<select id="fm"><option value="">todos</option>${mset.map(m=>`<option ${F.m===m?'selected':''}>${m}</option>`).join('')}</select></label><label>Ámbito<select id="fa"><option value="">todos</option>${aset.map(m=>`<option ${F.a===m?'selected':''}>${m}</option>`).join('')}</select></label><label>Lado<select id="fl"><option value="">ambos</option><option ${F.l==='Más'?'selected':''}>Más</option><option ${F.l==='Menos'?'selected':''}>Menos</option></select></label><label>Cuota min<input type="number" id="fc1" step="0.05" value="${F.c1??''}"></label><label>Cuota máx<input type="number" id="fc2" step="0.05" value="${F.c2??''}"></label>${w==='l'?`<label>p modelo ≥<input type="number" id="fpm" step="0.05" value="${F.pm??''}"></label><label>EV ≥<input type="number" id="fev" step="0.05" value="${F.ev??''}"></label>`:`<label>Titular<select id="ft"><option value="">todos</option><option value="1" ${F.t==='1'?'selected':''}>solo titulares probables (≥50 %)</option></select></label>`}<label>Cumple<select id="fk"><option value="">todos</option><option value="sí" ${F.k==='sí'?'selected':''}>sí (según el mínimo de arriba)</option><option value="no" ${F.k==='no'?'selected':''}>no</option><option value="sin" ${F.k==='sin'?'selected':''}>sin muestra / sin alineación</option></select></label><label>Buscar<input type="search" id="fq" value="${esc(F.q||'')}" placeholder="${w==='j'?'jugador':'texto'}"></label><label><span>&nbsp;</span><button class="b" id="fx">Limpiar</button></label></div></div><div id="cnt" class="small mut" style="margin:6px 0"></div><div class="tw"><table id="tb"></table></div><button class="b" id="mas" style="margin:8px 0">Mostrar más</button>`;
 $('#app').innerHTML=h;
 const get=()=>{F.p=$('#fp').value===''?undefined:+$('#fp').value;F.m=$('#fm').value||undefined;F.a=$('#fa').value||undefined;F.l=$('#fl').value||undefined;F.c1=$('#fc1').value===''?undefined:+$('#fc1').value;F.c2=$('#fc2').value===''?undefined:+$('#fc2').value;if(w==='l'){F.pm=$('#fpm').value===''?undefined:+$('#fpm').value;F.ev=$('#fev').value===''?undefined:+$('#fev').value}else F.t=$('#ft').value||undefined;F.k=$('#fk').value||undefined;F.q=$('#fq').value.trim().toLowerCase()||undefined};
 const COLS=w==='l'?[['Partido','n',r=>esc(D.P[r[0]].n),null],['Mercado','m',r=>esc(nm(r)),null],['Lado','lado',r=>r[6]+' '+(r[5]??''),null],['Cuota','c',r=>f2(r[7]),r=>r[7]],['p modelo','p',r=>pct(r[14]),r=>r[14]],['p mercado','pm',r=>pct(r[15]),r=>r[15]],['EV','ev',r=>`<span class="${r[16]<0?'bad':''}">${pct(r[16])}</span>`,r=>r[16]],['Esperado','e',r=>f2(r[8]),r=>r[8]],['Colchón','co',r=>f2(r[9]),r=>r[9]],['Local','rl',r=>esc(r[10]),null],['Visit.','rv',r=>esc(r[11]),null],['Cumple','k',cumTxt,null],['Alerta','al',r=>esc(r[17]),null]]
  :[['Partido','n',r=>esc(D.P[r[0]].n),null],['Jugador','jug',r=>esc(r[3])+(r[4]>=0.5?' <span class="mut small">XI '+Math.round(100*r[4])+'%</span>':' <span class="mut small">(sin XI)</span>'),null],['Mercado','m',r=>esc(r[1].slice(8)),null],['Línea','lado',r=>r[6]+' '+(r[5]??''),null],['Cuota','c',r=>f2(r[7]),r=>r[7]],['Historial','rl',r=>esc(r[10]),null],['Cumple','k',cumTxt,null],['Sistemas','s',r=>esc(r[18]),null]];
 const ok=r=>{if(F.p!=null&&r[0]!==F.p)return 0;if(F.m&&r[1]!==F.m)return 0;if(F.a&&r[2]!==F.a)return 0;if(F.l&&r[6]!==F.l)return 0;if(F.c1!=null&&!(r[7]>=F.c1))return 0;if(F.c2!=null&&!(r[7]<=F.c2))return 0;if(F.pm!=null&&!(r[14]>=F.pm))return 0;if(F.ev!=null&&!(r[16]>=F.ev))return 0;if(F.t&&!(r[4]>=0.5))return 0;if(F.k){const c=cum(r);if(F.k==='sin'){if(c!==null)return 0}else if(F.k==='sí'){if(c!==true)return 0}else if(c!==false)return 0}if(F.q&&!(D.P[r[0]].n+' '+nm(r)).toLowerCase().includes(F.q))return 0;return 1};
 const key={c:r=>r[7],p:r=>r[14],pm:r=>r[15],ev:r=>r[16],e:r=>r[8],co:r=>r[9],n:r=>D.P[r[0]].n,m:r=>nm(r),jug:r=>r[3],k:r=>cum(r)===true?2:cum(r)===false?1:0,rl:r=>r[10],lado:r=>r[5]};
 const paint=()=>{get();let L=rows.filter(([r])=>ok(r));const [sk,sd]=sortK[w],kf=key[sk];if(kf)L.sort((a,b)=>{const x=kf(a[0]),y=kf(b[0]);if(x==null&&y==null)return 0;if(x==null)return 1;if(y==null)return -1;return(x>y?1:x<y?-1:0)*sd});
  $('#cnt').textContent=L.length.toLocaleString('es-CO')+' líneas'+(L.length>LIM[w]?' (se muestran '+LIM[w]+')':'');
  $('#tb').innerHTML='<tr>'+COLS.map(c=>`<th data-s="${c[1]}" class="${c[3]?'n':''}">${c[0]}${sortK[w][0]===c[1]?(sortK[w][1]<0?' ▼':' ▲'):''}</th>`).join('')+'<th></th></tr>'+L.slice(0,LIM[w]).map(([r,i])=>'<tr>'+COLS.map(c=>`<td class="${c[3]?'n':''}">${c[2](r)}</td>`).join('')+`<td><button class="b small" data-add="${i}">${CUP.includes(i)?'✓':'+'}</button></td></tr>`).join('');
  $('#mas').hidden=L.length<=LIM[w]};
 $('#app').oninput=paint;$('#app').onchange=paint;
 $('#app').onclick=e=>{const t=e.target;if(t.dataset.add!=null){add(+t.dataset.add);t.textContent='✓'}if(t.dataset.s){const k=t.dataset.s;sortK[w]=sortK[w][0]===k?[k,-sortK[w][1]]:[k,-1];paint()}if(t.id==='mas'){LIM[w]+=300;paint()}if(t.id==='fx'){Fil[w]={};vTab(w)}};
 paint()}
function vCup(){
 const L=CUP.map(i=>D.F[i]);let c=1,p=1,tp=true;L.forEach(r=>{c*=r[7]||1;if(r[14]==null)tp=false;else p*=r[14]});
 const dup=new Set(),rep=new Set();L.forEach(r=>{if(dup.has(r[0]))rep.add(r[0]);dup.add(r[0])});
 const ret=stake*D.u*c;
 let h=`<div class="card"><h2>Cupón (${L.length} patas)</h2>${L.length?`<div class="tw"><table><tr><th>Partido</th><th>Línea</th><th class="n">Cuota</th><th class="n">p modelo</th><th></th></tr>${L.map((r,k)=>`<tr><td>${esc(D.P[r[0]].n)}</td><td>${esc(nm(r))} ${r[6]} ${r[5]??''}</td><td class="n">${f2(r[7])}</td><td class="n">${pct(r[14])}</td><td><button class="b small" data-del="${k}">×</button></td></tr>`).join('')}</table></div>`:'<p class="mut">Agrega líneas con «+» desde las otras pestañas.</p>'}`;
 if(L.length){h+=`<p><b>Cuota total ${c.toFixed(2)}</b> · probabilidad ${tp?'≈ '+pct(p)+' (si las patas fueran independientes)':'sin dato en alguna pata'} · cuota justa ${tp&&p>0?(1/p).toFixed(2):'–'}</p>${rep.size?`<p class="warn small">⚠ Hay patas del mismo partido (${[...rep].map(i=>esc(D.P[i].n)).join(', ')}): están correlacionadas, el producto no es la probabilidad real y Betano puede pagar distinto en Bet Builder. Úsalo como referencia.</p>`:''}<div class="filters"><label>Stake (unidades)<input type="number" id="stk" min="0" step="0.5" value="${stake}"></label><label>Stake COP<input type="text" readonly id="scop" value="$${(stake*D.u).toLocaleString('es-CO')}"></label><label>Retorno si acierta<input type="text" readonly id="sret" value="$${Math.round(ret).toLocaleString('es-CO')}"></label><label><span>&nbsp;</span><button class="b" id="cp">Copiar cupón</button></label><label><span>&nbsp;</span><button class="b" id="vc">Vaciar</button></label></div><p class="small mut">Es solo una calculadora: tú decides y apuestas en Betano; este informe no apuesta.</p>`}
 $('#app').innerHTML=h+'</div>';
 $('#app').onclick=e=>{const t=e.target;if(t.dataset.del!=null){CUP.splice(+t.dataset.del,1);draw();return}if(t.id==='vc'){CUP=[];draw()}if(t.id==='cp'){const tx=L.map(r=>`${D.P[r[0]].n} · ${nm(r)} ${r[6]} ${r[5]??''} @${f2(r[7])}`).join('\n')+`\nCuota total ${c.toFixed(2)}`;(navigator.clipboard?navigator.clipboard.writeText(tx):Promise.reject()).then(()=>t.textContent='Copiado ✓').catch(()=>{const a=document.createElement('textarea');a.value=tx;document.body.append(a);a.select();try{document.execCommand('copy');t.textContent='Copiado ✓'}catch(_){t.textContent='Selecciona y copia'}a.remove()})}};
 const s=$('#stk');if(s)s.oninput=()=>{stake=Math.max(0,+s.value||0);$('#scop').value='$'+(stake*D.u).toLocaleString('es-CO');$('#sret').value='$'+Math.round(stake*D.u*c).toLocaleString('es-CO')}}
function vDat(){$('#app').innerHTML=`<div class="card"><h2>Datos y límites</h2><p class="small mut">Texto de ESTADO.md de la jornada: qué se recolectó y qué se declaró sin dato (no se rellena con supuestos).</p><pre>${esc(D.estado||'Esta jornada no tiene ESTADO.md.')}</pre></div>`}
kbar();draw();
</script></body></html>'''


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    base = argv[0]
    jor, filas, rk, res, estado = cargar(base)
    d = datos(jor, filas, rk, res, estado)
    d['A'] = analisis(base, d)
    js = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    html = PLANTILLA.replace('__JOR__', jor).replace('/*DATA*/', js)
    out = argv[1] if len(argv) > 1 else os.path.join(base, 'informe.html')
    open(out, 'w', encoding='utf8').write(html)
    print(f'{out}: {len(d["P"])} partidos, {len(d["F"])} líneas, {len(html)//1024} KB')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
