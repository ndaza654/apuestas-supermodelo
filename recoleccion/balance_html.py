# -*- coding: utf-8 -*-
"""Balance interactivo de un periodo (HTML autónomo: sin red ni librerías): mis líneas calificadas + tus boletos de Betano.

    python3 recoleccion/balance_html.py <carpeta_balance> [--jornadas 2026-11-12-noche,2026-11-13] [--picks 2026-11-12] [--boletos a.json,b.json] [--desde 2026-11-12]

Lee    registro/lineas.csv (filas de las `--jornadas` con `resultado`; las de equipo las califica `calificar_lineas.py`)
       registro/historial_lineas.csv (los picks entregados en las fechas de `--picks`, ya calificados)
       los JSON de boletos (`--boletos`; por defecto registro/boletos_9-12nov.json + <carpeta>/boletos_betano.json)
       <carpeta>/pendientes.json (lista de textos) y <carpeta>/conclusiones.html (fragmento HTML, opcional)
Escribe <carpeta>/balance.html
Solo lectura de lo ya recogido: no apuesta ni lee la red. El «cumple» se puede mover (K de N) como en el informe de jornada; las líneas sin
resultado (jugadores sin estadística, partidos en curso) quedan como PENDIENTES, nunca se dan por ganadas o perdidas.
"""
import os, sys, csv, json, re, argparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import informe_html as IH
CODIGO = {'cumplió': 'C', 'falló': 'F', 'media ganada': 'MG', 'media perdida': 'MP', 'nula': 'N'}


def num(x):
    return IH.num(x)


def cargar(a):
    base = a.carpeta if os.path.isabs(a.carpeta) else os.path.join(RAIZ, a.carpeta)
    partidos, L = [], []

    def pid(n):
        if n not in partidos:
            partidos.append(n)
        return partidos.index(n)
    for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'historial_lineas.csv'), encoding='utf-8-sig'), delimiter=';'):
        if r['fecha_analisis'] in a.picks:
            m = re.search(r'(M[aá]s|Menos|S[ií]|No)\s*([\d.]*)\s*$', r['mercado_linea'])
            L.append([r['fecha_partido'], pid(r['partido']), r['liga'], 0, r['mercado_linea'], '', m.group(1) if m else '', num(m.group(2)) if m and m.group(2) else None,
                      num(r['cuota']), num(r['p_modelo']), num(r['p_mercado']), num(r['ev']), '', '', 'pick ' + r['tipo'], CODIGO.get(r['resultado'], ''), r['apostada'], r['nota']])
    for r in csv.DictReader(open(os.path.join(RAIZ, 'registro', 'lineas.csv'), encoding='utf-8-sig'), delimiter=';'):
        if r['jornada'] in a.jornadas:
            L.append([r['hora_partido'][:10], pid(r['partido']), r['liga'], 1, r['mercado'] + (' ' + r['jugador'] if r['jugador'] else ''), r['ambito'], r['lado'], num(r['linea']),
                      num(r['cuota']), num(r['p_modelo']), num(r['p_mercado']), num(r['ev_modelo']), r['reg_local'], r['reg_visitante'], r['cumple_ficha'],
                      CODIGO.get(r['resultado'], ''), r['apostada'], r['nota']])
    B = []
    for ruta in a.boletos:
        d = json.load(open(ruta if os.path.isabs(ruta) else os.path.join(RAIZ, ruta), encoding='utf8'))
        B += [b for b in d['boletos'] if b['fecha'] >= a.desde]
    pend = []
    p = os.path.join(base, 'pendientes.json')
    if os.path.exists(p):
        pend = json.load(open(p, encoding='utf8'))
    concl = ''
    p = os.path.join(base, 'conclusiones.html')
    if os.path.exists(p):
        concl = open(p, encoding='utf8').read()
    nmax = max([int(m.group(1)) for r in L for m in [re.search(r'de (\d+)', r[12] or '')] if m] or [10])
    return base, {'P': partidos, 'L': L, 'B': B, 'pend': pend, 'concl': concl, 'u': IH.U_COP, 'N': nmax,
                  'K': max(1, round(IH.FI.CUMPLE * nmax / IH.FI.N)), 'MN': max(1, round(IH.FI.MIN_N * nmax / IH.FI.N)), 'titulo': a.titulo}


ESTILO = re.search(r'<style>(.*?)</style>', IH.PLANTILLA, re.S).group(1)
PLANTILLA = r'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Balance __TIT__</title><style>__CSS__
.kpi{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}.kpi div{background:var(--chip);border-radius:8px;padding:8px}.kpi b{display:block;font-size:18px}
.pos{color:var(--acc);font-weight:600}.neg{color:var(--bad);font-weight:600}.concl li{margin:6px 0}</style></head><body>
<h1>Balance · <span id="tit"></span></h1><div class="sub" id="sub"></div>
<div class="card" id="kbar"></div><nav id="nav"></nav><div id="app"></div>
<script>
const D=/*DATA*/;
const $=(s,e)=>(e||document).querySelector(s),pct=x=>x==null||isNaN(x)?'–':(100*x).toFixed(0)+'%',f2=x=>x==null?'–':(+x).toFixed(2),cop=x=>(x<0?'-$':'$')+Math.abs(Math.round(x)).toLocaleString('es-CO');
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const RN={C:'cumplió',F:'falló',MG:'media ganada',MP:'media perdida',N:'nula','':'pendiente'};
let K=D.K,MN=D.MN,MODO='ambos',TAB='res',Fl={},Fb={},LIM=200;
$('#tit').textContent=D.titulo;
$('#sub').textContent=D.L.length.toLocaleString('es-CO')+' líneas mías (hay '+D.L.filter(r=>r[15]).length.toLocaleString('es-CO')+' ya calificadas) · '+D.B.length+' boletos tuyos · hora de Bogotá · solo lectura: no apuesta. Las conclusiones son pistas, no leyes: la muestra es pequeña.';
const rg=s=>{const m=/(\d+)\s*de\s*(\d+)/.exec(s||'');return m?[+m[1],+m[2]]:null};
function cum(r,k){k=k==null?K:k;if(r[3]!==1||r[14]==='sin alineación')return null;const a=rg(r[12]),b=rg(r[13]);if(!a)return null;
 if(r[3]===1&&(r[4]||'').startsWith('jugador')){return a[1]>=MN&&a[0]>=k}
 if(!b)return null;const t=x=>x[1]>=MN&&x[0]>=k;return MODO==='local'?t(a):MODO==='visitante'?t(b):MODO==='alguno'?(t(a)||t(b)):(t(a)&&t(b))}
const fam=r=>r[3]===0?(r[4].replace(/\s*(Más|Menos|Sí|No)\s*[\d.]*\s*$/,'')):((r[4]||'').startsWith('jugador')?'jugador':r[4]+(r[5]&&r[5]!=='total'&&r[5]!=='local'&&r[5]!=='visitante'?' '+r[5]:''));
/* estadística de un conjunto de líneas: solo las calificadas */
function st(rows){let n=0,c=0,mg=0,mp=0,nu=0,ps=0,br=0,roi=0,pend=0,np=0;for(const r of rows){const x=r[15];if(!x){pend++;continue}if(x==='N'){nu++;continue}
 if(x==='MG'){mg++;roi+=((r[8]||1)-1)/2;continue}if(x==='MP'){mp++;roi-=0.5;continue}
 n++;const y=x==='C'?1:0;c+=y;roi+=y?(r[8]||1)-1:-1;if(r[9]!=null){ps+=r[9];br+=(r[9]-y)**2;np++}}
 return{n,c,mg,mp,nu,pend,real:n?c/n:null,p:np?ps/np:null,brier:np?br/np:null,roi}}
const celda=s=>`<td class="n">${s.n}</td><td class="n">${s.c}</td><td class="n ${s.real!=null&&s.p!=null&&s.real<s.p-0.05?'bad':''}">${pct(s.real)}</td><td class="n">${pct(s.p)}</td><td class="n">${s.real!=null&&s.p!=null?(100*(s.real-s.p)).toFixed(0)+' pts':'–'}</td><td class="n ${s.roi>=0?'pos':'neg'}">${s.n?s.roi.toFixed(1)+' u':'–'}</td>`;
const TH='<th class="n">Líneas</th><th class="n">Cumplieron</th><th class="n">% real</th><th class="n">p modelo</th><th class="n">real − p</th><th class="n">1 u en cada una</th>';
function grupo(rows,keyf,orden){const m={};rows.forEach(r=>{const k=keyf(r);(m[k]=m[k]||[]).push(r)});return Object.keys(m).sort(orden||((a,b)=>m[b].length-m[a].length)).map(k=>[k,m[k],st(m[k])])}
function kbar(){const B=$('#kbar'),ks=[];for(let i=Math.max(1,D.N-5);i<=D.N;i++)ks.push(i);
 B.innerHTML=`<div class="filters"><label>«Cumple» = al menos<input type="number" id="kk" min="1" max="${D.N}" value="${K}" style="width:64px"></label><label>de ${D.N} · n mínimo<input type="number" id="kmn" min="1" max="${D.N}" value="${MN}" style="width:64px"></label><label>En<select id="kmodo"><option value="ambos" ${MODO==='ambos'?'selected':''}>ambos equipos</option><option value="local" ${MODO==='local'?'selected':''}>solo el local</option><option value="visitante" ${MODO==='visitante'?'selected':''}>solo el visitante</option><option value="alguno" ${MODO==='alguno'?'selected':''}>cualquiera</option></select></label><label>Atajos<span>${ks.map(k=>`<button class="b small ${K===k?'on':''}" data-k="${k}" style="margin-right:4px">${k}</button>`).join('')}</span></label></div><div class="small mut" style="margin-top:6px">Mueve el mínimo para ver si «cumplir» separa aciertos de fallos. Solo aplica a las líneas del pipeline con muestra (los 38 picks del 12-nov no traen regularidad).</div>`;
 B.onchange=()=>{K=Math.max(1,Math.min(D.N,+$('#kk').value||K));MN=Math.max(1,Math.min(D.N,+$('#kmn').value||MN));MODO=$('#kmodo').value;kbar();draw(true)};
 B.onclick=e=>{const k=e.target.dataset.k;if(k){K=+k;kbar();draw(true)}}}
const TABS=[['res','Resumen'],['lin','Líneas mías'],['bol','Tus apuestas'],['pen','Pendientes'],['con','Conclusiones']];
function nav(){$('#nav').innerHTML=TABS.map(([k,t])=>`<button class="${TAB===k?'on':''}" data-k="${k}">${t}</button>`).join('');$('#nav').onclick=e=>{const k=e.target.dataset.k;if(k){TAB=k;draw()}}}
function draw(keep){const A=$('#app');A.oninput=A.onchange=A.onclick=null;nav();const y=window.scrollY;({res:vRes,lin:vLin,bol:vBol,pen:vPen,con:vCon})[TAB]();window.scrollTo(0,keep?y:0)}
function vRes(){
 const all=D.L,S=st(all),pip=all.filter(r=>r[3]===1),pk=all.filter(r=>r[3]===0);
 const bo=D.B,real=bo.filter(b=>!b.gratis),ap=real.reduce((a,b)=>a+b.stake,0),co=bo.reduce((a,b)=>a+b.cobrado,0),gan=real.filter(b=>b.resultado==='Ganada').length;
 let h=`<div class="card"><h2>Panorama</h2><div class="kpi"><div>Líneas calificadas<b>${S.n+S.mg+S.mp+S.nu}</b></div><div>% que cumplió<b>${pct(S.real)}</b></div><div>p media del modelo<b>${pct(S.p)}</b></div><div>Error² (Brier)<b>${S.brier==null?'–':S.brier.toFixed(3)}</b></div><div>Pendientes<b>${S.pend}</b></div><div>Boletos tuyos<b>${bo.length}</b></div><div>Ganados (dinero real)<b>${gan} de ${real.length}</b></div><div>Neto en pesos<b class="${co-ap>=0?'pos':'neg'}">${cop(co-ap)}</b></div><div>ROI<b class="${co-ap>=0?'pos':'neg'}">${ap?pct((co-ap)/ap):'–'}</b></div></div><p class="small mut">«1 u en cada una» = lo que daría poner 1 unidad en CADA línea (cumpla o no): mide si la línea paga, no lo que tú apostaste. Las apuestas gratis no cuentan como dinero apostado.</p></div>`;
 const c1=pip.filter(r=>cum(r)===true),c0=pip.filter(r=>cum(r)===false);
 h+=`<div class="card"><h2>¿Separa «cumple» (≥ ${K} de ${D.N}) los aciertos de los fallos?</h2><div class="tw"><table><tr><th>Grupo</th>${TH}</tr><tr><td>Cumple</td>${celda(st(c1))}</tr><tr><td>No cumple</td>${celda(st(c0))}</tr></table></div><p class="small mut">Si «cumple» sirviera, su % real estaría por encima del de «no cumple». Más y Menos de una misma línea se compensan entre sí: mira también por mercado y lado abajo.</p></div>`;
 const por=(t,rows,keyf)=>`<div class="card"><h2>${t}</h2><div class="tw"><table><tr><th>Grupo</th>${TH}</tr>${grupo(rows,keyf).filter(g=>g[2].n+g[2].mg+g[2].mp>0).map(([k,rs,s])=>`<tr><td>${esc(k)}</td>${celda(s)}</tr>`).join('')}</table></div></div>`;
 h+=por('Por familia de mercado y lado (solo calificadas)',all,r=>fam(r)+(r[6]?' · '+r[6]:''));
 const tr=[[0,.3,'< 30 %'],[.3,.5,'30–50 %'],[.5,.7,'50–70 %'],[.7,.85,'70–85 %'],[.85,1.01,'≥ 85 %']];
 h+=`<div class="card"><h2>Calibración: cuando el modelo dijo X %, ¿qué pasó?</h2><div class="tw"><table><tr><th>Tramo de p</th>${TH}</tr>${tr.map(([a,b,t])=>{const rs=all.filter(r=>r[9]!=null&&r[9]>=a&&r[9]<b);return `<tr><td>${t}</td>${celda(st(rs))}</tr>`}).join('')}</table></div></div>`;
 h+=por('Por día del partido',all,r=>r[0]);
 h+=por('Por origen',all,r=>r[3]===0?'picks que te entregué (12-nov)':'líneas del pipeline (todas las de Betano)');
 $('#app').innerHTML=h}
function vLin(){
 const F=Fl,rows=D.L.map((r,i)=>[r,i]),mset=[...new Set(D.L.map(fam))].sort(),dset=[...new Set(D.L.map(r=>r[0]))].sort();
 $('#app').innerHTML=`<div class="card"><div class="filters"><label>Día<select id="fd"><option value="">todos</option>${dset.map(x=>`<option ${F.d===x?'selected':''}>${x}</option>`).join('')}</select></label><label>Partido<select id="fp"><option value="">todos</option>${D.P.map((p,i)=>`<option value="${i}" ${F.p===i?'selected':''}>${esc(p)}</option>`).join('')}</select></label><label>Mercado<select id="fm"><option value="">todos</option>${mset.map(x=>`<option ${F.m===x?'selected':''}>${esc(x)}</option>`).join('')}</select></label><label>Lado<select id="fl"><option value="">todos</option><option ${F.l==='Más'?'selected':''}>Más</option><option ${F.l==='Menos'?'selected':''}>Menos</option><option ${F.l==='Sí'?'selected':''}>Sí</option><option ${F.l==='No'?'selected':''}>No</option></select></label><label>Origen<select id="fo"><option value="">todos</option><option value="0" ${F.o==='0'?'selected':''}>picks entregados</option><option value="1" ${F.o==='1'?'selected':''}>pipeline</option></select></label><label>Resultado<select id="fr"><option value="">todos</option>${['C','F','MG','MP','N','P'].map(x=>`<option value="${x}" ${F.r===x?'selected':''}>${x==='P'?'pendiente':RN[x]}</option>`).join('')}</select></label><label>Cumple<select id="fk"><option value="">todos</option><option value="s" ${F.k==='s'?'selected':''}>sí (mínimo de arriba)</option><option value="n" ${F.k==='n'?'selected':''}>no</option><option value="x" ${F.k==='x'?'selected':''}>sin dato</option></select></label><label>Cuota ≥<input type="number" id="fc" step="0.05" value="${F.c??''}"></label><label>p modelo ≥<input type="number" id="fpm" step="0.05" value="${F.pm??''}"></label><label>Apostada<select id="fa"><option value="">todas</option><option value="s" ${F.a==='s'?'selected':''}>sí</option></select></label><label>Buscar<input type="search" id="fq" value="${esc(F.q||'')}"></label><label><span>&nbsp;</span><button class="b" id="fx">Limpiar</button></label></div></div><div id="agg" class="card small"></div><div class="tw"><table id="tb"></table></div><button class="b" id="mas" style="margin:8px 0">Mostrar más</button>`;
 const get=()=>{F.d=$('#fd').value||undefined;F.p=$('#fp').value===''?undefined:+$('#fp').value;F.m=$('#fm').value||undefined;F.l=$('#fl').value||undefined;F.o=$('#fo').value||undefined;F.r=$('#fr').value||undefined;F.k=$('#fk').value||undefined;F.c=$('#fc').value===''?undefined:+$('#fc').value;F.pm=$('#fpm').value===''?undefined:+$('#fpm').value;F.a=$('#fa').value||undefined;F.q=$('#fq').value.trim().toLowerCase()||undefined};
 const ok=r=>{if(F.d&&r[0]!==F.d)return 0;if(F.p!=null&&r[1]!==F.p)return 0;if(F.m&&fam(r)!==F.m)return 0;if(F.l&&r[6]!==F.l)return 0;if(F.o!=null&&String(r[3])!==F.o)return 0;if(F.r){if(F.r==='P'){if(r[15])return 0}else if(r[15]!==F.r)return 0}
  if(F.k){const c=cum(r);if(F.k==='s'&&c!==true)return 0;if(F.k==='n'&&c!==false)return 0;if(F.k==='x'&&c!==null)return 0}
  if(F.c!=null&&!(r[8]>=F.c))return 0;if(F.pm!=null&&!(r[9]>=F.pm))return 0;if(F.a&&r[16]!=='Sí')return 0;if(F.q&&!(D.P[r[1]]+' '+r[4]).toLowerCase().includes(F.q))return 0;return 1};
 const paint=()=>{get();const L=rows.filter(([r])=>ok(r)),s=st(L.map(x=>x[0]));
  $('#agg').innerHTML=`<b>${L.length.toLocaleString('es-CO')}</b> líneas en el filtro · calificadas ${s.n+s.mg+s.mp+s.nu} · cumplieron ${s.c} (<b>${pct(s.real)}</b> real vs ${pct(s.p)} que decía el modelo) · 1 u en cada una: <b class="${s.roi>=0?'pos':'neg'}">${s.roi.toFixed(1)} u</b> · pendientes ${s.pend}`;
  $('#tb').innerHTML='<tr><th>Día</th><th>Partido</th><th>Línea</th><th class="n">Cuota</th><th class="n">p</th><th class="n">EV</th><th>Local</th><th>Visit.</th><th>Cumple</th><th>Resultado</th><th>Origen</th></tr>'+L.slice(0,LIM).map(([r])=>{const c=cum(r);return `<tr><td>${r[0]}</td><td>${esc(D.P[r[1]])}</td><td>${esc(r[3]===0?r[4]:r[4]+(r[5]&&!(r[4]||'').startsWith('jugador')?' '+r[5]:'')+' '+r[6]+' '+(r[7]??''))}</td><td class="n">${f2(r[8])}</td><td class="n">${pct(r[9])}</td><td class="n ${r[11]<0?'bad':''}">${pct(r[11])}</td><td>${esc(r[12])}</td><td>${esc(r[13])}</td><td>${c===true?'<span class="ok">sí</span>':c===false?'no':'–'}</td><td class="${r[15]==='C'?'ok':r[15]==='F'?'bad':'mut'}">${RN[r[15]]}</td><td class="small mut">${r[3]===0?esc(r[14]):'pipeline'}${r[16]==='Sí'?' · apostada':''}</td></tr>`}).join('');
  $('#mas').hidden=L.length<=LIM};
 $('#app').oninput=paint;$('#app').onchange=paint;$('#app').onclick=e=>{const t=e.target;if(t.id==='mas'){LIM+=300;paint()}if(t.id==='fx'){Fl={};vLin()}};paint()}
function vBol(){
 const F=Fb,rows=D.B,tset=[...new Set(rows.map(b=>b.tipo))],dset=[...new Set(rows.map(b=>b.fecha))].sort();
 $('#app').innerHTML=`<div class="card"><div class="filters"><label>Día<select id="bd"><option value="">todos</option>${dset.map(x=>`<option ${F.d===x?'selected':''}>${x}</option>`).join('')}</select></label><label>Tipo<select id="bt"><option value="">todos</option>${tset.map(x=>`<option ${F.t===x?'selected':''}>${x}</option>`).join('')}</select></label><label>Resultado<select id="br"><option value="">todos</option><option ${F.r==='Ganada'?'selected':''}>Ganada</option><option ${F.r==='Perdida'?'selected':''}>Perdida</option></select></label><label>Stake ≥<input type="number" id="bs" step="2500" value="${F.s??''}"></label><label>Dinero<select id="bg"><option value="">todo</option><option value="r" ${F.g==='r'?'selected':''}>solo real</option><option value="g" ${F.g==='g'?'selected':''}>solo gratis</option></select></label><label>Buscar<input type="search" id="bq" value="${esc(F.q||'')}"></label></div></div><div id="bagg" class="card small"></div><div class="tw"><table id="bt2"></table></div>`;
 const get=()=>{F.d=$('#bd').value||undefined;F.t=$('#bt').value||undefined;F.r=$('#br').value||undefined;F.s=$('#bs').value===''?undefined:+$('#bs').value;F.g=$('#bg').value||undefined;F.q=$('#bq').value.trim().toLowerCase()||undefined};
 const paint=()=>{get();const L=rows.filter(b=>(!F.d||b.fecha===F.d)&&(!F.t||b.tipo===F.t)&&(!F.r||b.resultado===F.r)&&(F.s==null||b.stake>=F.s)&&(!F.g||(F.g==='g')===b.gratis)&&(!F.q||(b.partidos+' '+b.patas).toLowerCase().includes(F.q)));
  const re=L.filter(b=>!b.gratis),ap=re.reduce((a,b)=>a+b.stake,0),co=L.reduce((a,b)=>a+b.cobrado,0),g=re.filter(b=>b.resultado==='Ganada').length;
  $('#bagg').innerHTML=`<b>${L.length}</b> boletos · dinero real ${re.length} · ganados ${g} (${re.length?pct(g/re.length):'–'}) · apostado ${cop(ap)} · cobrado ${cop(co)} · neto <b class="${co-ap>=0?'pos':'neg'}">${cop(co-ap)}</b> · ROI ${ap?pct((co-ap)/ap):'–'} · «cobrado» incluye lo ganado con apuestas gratis`;
  $('#bt2').innerHTML='<tr><th>#</th><th>Día</th><th>Tipo</th><th class="n">Stake</th><th class="n">Cuota</th><th>Resultado</th><th class="n">Cobrado</th><th class="n">Neto</th><th>Partidos</th><th>Patas</th></tr>'+L.map(b=>`<tr><td>${b.n}</td><td>${b.fecha}</td><td>${esc(b.tipo)}</td><td class="n">${cop(b.stake)}${b.gratis?' (gratis)':''}</td><td class="n">${f2(b.cuota)}</td><td class="${b.resultado==='Ganada'?'ok':'bad'}">${b.resultado}</td><td class="n">${cop(b.cobrado)}</td><td class="n ${b.cobrado-(b.gratis?0:b.stake)>=0?'pos':'neg'}">${cop(b.cobrado-(b.gratis?0:b.stake))}</td><td style="white-space:normal;min-width:220px">${esc(b.partidos)}</td><td style="white-space:normal;min-width:260px">${esc(b.patas)}</td></tr>`).join('')};
 $('#app').oninput=paint;$('#app').onchange=paint;paint()}
function vPen(){$('#app').innerHTML=`<div class="card"><h2>Pendientes (no se dan por ganadas ni perdidas)</h2>${D.pend.length?'<ul>'+D.pend.map(t=>`<li>${esc(t)}</li>`).join('')+'</ul>':'<p class="mut">Nada pendiente.</p>'}<p class="small mut">Líneas mías sin calificar en este balance: ${D.L.filter(r=>!r[15]).length.toLocaleString('es-CO')} (la mayoría de jugador, que necesitan estadística por jugador, o de partidos en curso).</p></div>`}
function vCon(){$('#app').innerHTML=`<div class="card concl">${D.concl||'<p class="mut">Sin conclusiones escritas.</p>'}</div>`}
kbar();draw();
</script></body></html>'''


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('carpeta')
    ap.add_argument('--jornadas', default='')
    ap.add_argument('--picks', default='')
    ap.add_argument('--boletos', default='registro/boletos_9-12nov.json')
    ap.add_argument('--titulo', default='12 y 13 de noviembre de 2026')
    ap.add_argument('--desde', default='', help='solo boletos con fecha >= AAAA-MM-DD')
    a = ap.parse_args(argv)
    a.jornadas = [x for x in a.jornadas.split(',') if x]
    a.picks = [x for x in a.picks.split(',') if x]
    a.boletos = [x for x in a.boletos.split(',') if x]
    base, D = cargar(a)
    html = PLANTILLA.replace('__CSS__', ESTILO).replace('__TIT__', a.titulo).replace('/*DATA*/', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
    out = os.path.join(base, 'balance.html')
    open(out, 'w', encoding='utf-8').write(html)
    print(f'{out}: {len(D["L"])} líneas, {len(D["B"])} boletos, {os.path.getsize(out) // 1024} KB')


if __name__ == '__main__':
    main()
