# -*- coding: utf-8 -*-
"""Auditoría interactiva de TODO lo que Claude sugirió (sencillas, combinadas, Bet Builder, en vivo), pata por pata (HTML autónomo, sin red).

    python3 recoleccion/sugerencias.py            # arma/actualiza registro/sugerencias.csv (califica con los resultados del repo)
    python3 recoleccion/auditoria_html.py [salida.html] [--conclusiones archivo.html]

Lee registro/sugerencias.csv. Filtros por entrega, tipo, resultado, nº de patas, cuota, probabilidad, jugada, familia que falló y texto;
el resumen se recalcula con el filtro. Solo lectura: no apuesta.
"""
import argparse, csv, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'recoleccion'))
import informe_html as IH

ESTILO = re.search(r'<style>(.*?)</style>', IH.PLANTILLA, re.S).group(1)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def cargar(ruta_csv, ruta_concl):
    filas = list(csv.DictReader(open(ruta_csv, encoding='utf-8-sig'), delimiter=';'))
    S = []
    for r in filas:
        S.append({'id': r['id'], 'f': r['fecha_entrega'], 'h': r['hora'], 'e': r['entrega'], 't': r['tipo'], 'n': r['nombre'], 'pa': r['partidos'],
                  'k': int(r['n_patas']), 'c': num(r['cuota']), 'p': num(r['p_estimada']), 'r': r['resultado'], 'l': json.loads(r['patas_json']),
                  'ff': r['familia_fallo'], 'j': r['jugada'], 'no': r['nota'], 'fu': r['fuente']})
    concl = open(ruta_concl, encoding='utf8').read() if ruta_concl and os.path.exists(ruta_concl) else ''
    return {'S': S, 'concl': concl}


PLANTILLA = r'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Auditoría de sugerencias</title><style>__CSS__
.kpi{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}.kpi div{background:var(--chip);border-radius:8px;padding:8px}.kpi b{display:block;font-size:18px}
.pos{color:var(--acc);font-weight:600}.neg{color:var(--bad);font-weight:600}.concl li{margin:6px 0}
.sc{border:1px solid var(--line);border-radius:10px;padding:10px;margin:8px 0;background:var(--card)}.sc.c{border-left:5px solid var(--acc)}.sc.f{border-left:5px solid var(--bad)}.sc.o{border-left:5px solid var(--warn)}
.leg{display:flex;gap:8px;align-items:baseline;padding:2px 0}.leg .m{width:22px;text-align:center;font-weight:700}.leg.c .m{color:var(--acc)}.leg.f .m{color:var(--bad)}
.hd{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:baseline;margin-bottom:4px}.small{font-size:12px}</style></head><body>
<h1>Auditoría · todo lo que Claude sugirió</h1><div class="sub" id="sub"></div>
<div class="card"><div class="filters" id="flt"></div></div><nav id="nav"></nav><div id="app"></div>
<script>
const D=/*DATA*/;
const $=(s,e)=>(e||document).querySelector(s),pct=x=>x==null||isNaN(x)?'–':(100*x).toFixed(0)+'%',f2=x=>x==null?'–':(+x).toFixed(2);
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const RES={'cumplió':'c','falló':'f'};const MK={C:'✓',MG:'✓½',F:'✗',MP:'✗½',N:'–',U:'?'};
let TAB='res',F={e:'',t:'',r:'',k:'',cmin:'',cmax:'',pmin:'',j:'',ff:'',q:'',solo:'1'};
const uniq=a=>[...new Set(a)];
$('#sub').textContent=D.S.length+' sugerencias mías calificadas con resultados reales (equipo: Flashscore; jugador: Sofascore) · hora de Bogotá · solo lectura: no apuesta. Pocas observaciones y muy dependientes entre sí: son pistas, no leyes.';
function flt(){const E=uniq(D.S.map(s=>s.e)),T=uniq(D.S.map(s=>s.t)),FF=uniq(D.S.flatMap(s=>s.ff?s.ff.split(' | '):[]));
 const sel=(id,lab,opts,v)=>`<label>${lab}<select id="${id}"><option value="">todos</option>${opts.map(o=>`<option ${o===v?'selected':''}>${esc(o)}</option>`).join('')}</select></label>`;
 $('#flt').innerHTML=sel('fe','Entrega',E,F.e)+sel('ft','Tipo',T,F.t)+sel('fr','Resultado',['cumplió','falló','parcial','sin verificar','anulada'],F.r)+
 `<label>Patas<select id="fk"><option value="">todas</option><option ${F.k==='1'?'selected':''} value="1">1 (sencilla)</option><option ${F.k==='2'?'selected':''} value="2">2</option><option ${F.k==='3'?'selected':''} value="3">3</option><option ${F.k==='4+'?'selected':''} value="4+">4 o más</option></select></label>`+
 `<label>Cuota ≥<input id="fc1" type="number" step="0.1" style="width:70px" value="${F.cmin}"></label><label>Cuota ≤<input id="fc2" type="number" step="0.1" style="width:70px" value="${F.cmax}"></label><label>p estimada ≥ (%)<input id="fp" type="number" style="width:70px" value="${F.pmin}"></label>`+
 `<label>¿La jugaste?<select id="fj"><option value="">todas</option><option ${F.j==='si'?'selected':''} value="si">sí (variante)</option></select></label>`+sel('ff','Familia que falló',FF,F.ff)+
 `<label>Buscar<input id="fq" value="${esc(F.q)}" placeholder="partido, pata, jugador"></label>`;
 $('#flt').onchange=$('#flt').oninput=()=>{F.e=$('#fe').value;F.t=$('#ft').value;F.r=$('#fr').value;F.k=$('#fk').value;F.cmin=$('#fc1').value;F.cmax=$('#fc2').value;F.pmin=$('#fp').value;F.j=$('#fj').value;F.ff=$('#ff').value;F.q=$('#fq').value;draw(true)}}
const rows=()=>D.S.filter(s=>(!F.e||s.e===F.e)&&(!F.t||s.t===F.t)&&(!F.r||s.r===F.r)&&(!F.k||(F.k==='4+'?s.k>=4:s.k===+F.k))&&(F.cmin===''||(s.c!=null&&s.c>=+F.cmin))&&(F.cmax===''||(s.c!=null&&s.c<=+F.cmax))&&(F.pmin===''||(s.p!=null&&s.p*100>=+F.pmin))&&(!F.j||s.j)&&(!F.ff||s.ff.includes(F.ff))&&(!F.q||(s.n+' '+s.pa+' '+s.l.map(l=>l[0]).join(' ')).toLowerCase().includes(F.q.toLowerCase())));
/* resumen de un conjunto: solo cumplió/falló cuentan para el %; ROI a 1 u con la cuota (techo/estimada si es combinada) */
function st(R){const x=R.filter(s=>s.r==='cumplió'||s.r==='falló');let ps=0,np=0,roi=0,nr=0,br=0;x.forEach(s=>{const y=s.r==='cumplió'?1:0;if(s.p!=null){ps+=s.p;br+=(s.p-y)**2;np++}if(s.c!=null){nr++;roi+=y?s.c-1:-1}});
 const c=x.filter(s=>s.r==='cumplió').length;return{n:x.length,c,real:x.length?c/x.length:null,p:np?ps/np:null,brier:np?br/np:null,roi,nr,otros:R.length-x.length}}
const th='<th class="n">Sugerencias</th><th class="n">Se dieron</th><th class="n">% real</th><th class="n">p que dije</th><th class="n">real − p</th><th class="n">1 u en cada una</th><th class="n">sin calificar</th>';
const cl=s=>`<td class="n">${s.n}</td><td class="n">${s.c}</td><td class="n">${pct(s.real)}</td><td class="n">${pct(s.p)}</td><td class="n ${s.real!=null&&s.p!=null&&s.real<s.p-0.08?'bad':''}">${s.real!=null&&s.p!=null?(100*(s.real-s.p)).toFixed(0)+' pts':'–'}</td><td class="n ${s.roi>=0?'pos':'neg'}">${s.nr?s.roi.toFixed(1)+' u':'–'}</td><td class="n">${s.otros}</td>`;
function grp(R,kf,ord){const m={};R.forEach(s=>{(Array.isArray(kf(s))?kf(s):[kf(s)]).forEach(k=>(m[k]=m[k]||[]).push(s))});return Object.keys(m).sort(ord||((a,b)=>m[b].length-m[a].length)).map(k=>[k,st(m[k])])}
const tb=(R,kf,lab,ord)=>`<h3>${lab}</h3><div class="tw"><table><tr><th>${lab}</th>${th}</tr>${grp(R,kf,ord).map(([k,s])=>`<tr><td>${esc(k)}</td>${cl(s)}</tr>`).join('')}</table></div>`;
const tipoG=s=>s.k===1?'sencilla':(s.t.includes('Bet Builder')?'Bet Builder':(s.t.includes('mismo partido')?'combinada del mismo partido':'combinada entre partidos'));
const cuotaG=s=>s.c==null?'sin cuota':s.c<2?'1.00–1.99':s.c<3?'2.00–2.99':s.c<5?'3.00–4.99':s.c<9?'5.00–8.99':'9 o más';
const pG=s=>s.p==null?'sin p':s.p<.3?'< 30 %':s.p<.5?'30–49 %':s.p<.65?'50–64 %':s.p<.8?'65–79 %':'80 % o más';
function legStats(R){const m={};R.forEach(s=>{if(s.k<2&&s.t==='sencilla')return;s.l.forEach(l=>{const f=l[4];(m[f]=m[f]||[0,0]);if(l[2]==='C'||l[2]==='MG'){m[f][0]++;m[f][1]++}else if(l[2]==='F'||l[2]==='MP')m[f][1]++})});return m}
function vRes(){const R=rows(),t=st(R);
 let h=`<div class="card"><h2>Resumen del filtro actual</h2><div class="kpi"><div><span class="mut">Sugerencias</span><b>${R.length}</b></div><div><span class="mut">Se dieron</span><b>${t.c} de ${t.n}</b></div><div><span class="mut">% real</span><b>${pct(t.real)}</b></div><div><span class="mut">p que dije (media)</span><b>${pct(t.p)}</b></div><div><span class="mut">1 u en cada una</span><b class="${t.roi>=0?'pos':'neg'}">${t.nr?t.roi.toFixed(1)+' u':'–'}</b></div></div>
 <p class="small mut">«1 u en cada una» = lo que daría poner 1 unidad en cada sugerencia a su cuota (en combinadas la cuota es el producto de las cuotas sueltas o un precio estimado mío: un techo, no el cupón real). «p que dije» = la probabilidad con la que la presenté. «sin calificar» = parciales (asiáticas), sin verificar o anuladas: no cuentan como ganadas ni perdidas.</p></div>`;
 h+=`<div class="card">${tb(R,tipoG,'Tipo')}${tb(R,s=>s.e,'Entrega')}${tb(R,s=>s.k===1?'1 pata':s.k+' patas','Patas',(a,b)=>parseInt(a)-parseInt(b))}${tb(R,cuotaG,'Cuota',(a,b)=>a.localeCompare(b))}${tb(R,pG,'p que dije',(a,b)=>a.localeCompare(b))}</div>`;
 const lg=legStats(R);h+=`<div class="card"><h3>Patas sueltas dentro de combinadas, por familia</h3><div class="tw"><table><tr><th>Familia</th><th class="n">Patas</th><th class="n">Se dieron</th><th class="n">%</th></tr>${Object.keys(lg).sort((a,b)=>lg[b][1]-lg[a][1]).map(k=>`<tr><td>${esc(k)}</td><td class="n">${lg[k][1]}</td><td class="n">${lg[k][0]}</td><td class="n">${pct(lg[k][0]/lg[k][1])}</td></tr>`).join('')}</table></div>
 <p class="small mut">Una combinada falla si falla cualquier pata; esta tabla mira cada pata por separado (no cuenta las «sin verificar»).</p></div>`;
 const fl=R.filter(s=>s.r==='falló'&&s.k>1);const one=fl.filter(s=>s.l.filter(l=>l[2]==='F'||l[2]==='MP').length===1);
 h+=`<div class="card"><h3>Qué tumbó a las combinadas que fallaron</h3><p>${fl.length} combinadas fallaron; <b>${one.length}</b> por una sola pata (la «pata débil»). Pata que falló, por familia (cuántas combinadas tumbó): ${Object.entries(fl.flatMap(s=>s.ff?s.ff.split(' | '):[]).reduce((a,k)=>(a[k]=(a[k]||0)+1,a),{})).sort((a,b)=>b[1]-a[1]).map(([k,v])=>esc(k)+' '+v).join(' · ')||'–'}.</p></div>`;
 $('#app').innerHTML=h}
function legHtml(l){const c=l[2];return `<div class="leg ${c==='C'||c==='MG'?'c':c==='F'||c==='MP'?'f':''}"><span class="m">${MK[c]||'?'}</span><span>${esc(l[0])}${l[1]?` <span class="mut">@${l[1]}</span>`:''}${l[3]?` <span class="mut small">· ${esc(l[3])}</span>`:''}</span></div>`}
function card(s){const k=RES[s.r]||'o';return `<div class="sc ${k}"><div class="hd"><b>${esc(s.n)}</b><span class="pill ${s.r==='cumplió'?'apto':''}">${esc(s.r)}</span><span class="mut small">${esc(s.pa)}</span></div>
 <div class="small mut">${esc(s.e)}${s.h?' · '+esc(s.h):''} · ${s.k} pata${s.k>1?'s':''}${s.c!=null?' · cuota '+f2(s.c):''}${s.p!=null?' · p '+pct(s.p):''}${s.j?' · <b>'+esc(s.j)+'</b>':''}</div>${s.l.map(legHtml).join('')}${s.no?`<div class="small mut">${esc(s.no)}</div>`:''}</div>`}
const LIM={c:60,s:300};
function vCom(){const R=rows().filter(s=>s.k>1||s.t!=='sencilla').sort((a,b)=>a.f===b.f?(b.c||0)-(a.c||0):b.f.localeCompare(a.f)||0);const n=Math.min(R.length,LIM.c);
 $('#app').innerHTML=`<div class="card"><h2>Combinadas y Bet Builder (${R.length})</h2><p class="small mut">✓ se dio · ✗ falló · ? sin verificar · – anulada. Verde = la combinada entera se dio; rojo = falló.</p>${R.slice(0,n).map(card).join('')}${R.length>n?`<button class="b" id="mas">Ver más (${R.length-n})</button>`:''}</div>`;if($('#mas'))$('#mas').onclick=()=>{LIM.c+=60;vCom()}}
function vSen(){const R=rows().filter(s=>s.k===1&&s.t.includes('sencilla')||s.k===1);const n=Math.min(R.length,LIM.s);
 $('#app').innerHTML=`<div class="card"><h2>Sencillas (${R.length})</h2><div class="tw"><table><tr><th>Día</th><th>Entrega</th><th>Partido</th><th>Línea</th><th class="n">Cuota</th><th class="n">p</th><th>Resultado</th><th>Valor real</th></tr>${R.slice(0,n).map(s=>`<tr><td>${s.f}</td><td>${esc(s.e)}</td><td>${esc(s.pa)}</td><td>${esc(s.n)}</td><td class="n">${f2(s.c)}</td><td class="n">${pct(s.p)}</td><td class="${s.r==='cumplió'?'ok':s.r==='falló'?'bad':''}">${esc(s.r)}</td><td class="mut">${esc((s.l[0]||[])[3]||'')}</td></tr>`).join('')}</table></div>${R.length>n?`<button class="b" id="mas">Ver más (${R.length-n})</button>`:''}</div>`;if($('#mas'))$('#mas').onclick=()=>{LIM.s+=300;vSen()}}
function vCon(){$('#app').innerHTML=`<div class="card concl">${D.concl||'<p class="mut">Sin conclusiones escritas.</p>'}</div>`}
const TABS=[['res','Resumen'],['com','Combinadas'],['sen','Sencillas'],['con','Qué aprendimos y qué cambiar']];
function draw(keep){$('#nav').innerHTML=TABS.map(([k,t])=>`<button data-k="${k}" class="${k===TAB?'on':''}">${t}</button>`).join(' ');$('#nav').onclick=e=>{const k=e.target.dataset.k;if(k){TAB=k;draw(true)}};
 ({res:vRes,com:vCom,sen:vSen,con:vCon})[TAB]();document.querySelector('.card').style.display=(TAB==='con')?'none':''}
flt();draw();
</script></body></html>'''


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('salida', nargs='?', default=os.path.join(RAIZ, 'jornadas', '2026-11-13', 'balance', 'auditoria.html'))
    ap.add_argument('--csv', default=os.path.join(RAIZ, 'registro', 'sugerencias.csv'))
    ap.add_argument('--conclusiones', default=os.path.join(RAIZ, 'jornadas', '2026-11-13', 'balance', 'auditoria_conclusiones.html'))
    a = ap.parse_args(argv)
    D = cargar(a.csv, a.conclusiones)
    html = PLANTILLA.replace('__CSS__', ESTILO).replace('/*DATA*/', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
    open(a.salida, 'w', encoding='utf-8').write(html)
    print(f'{a.salida}: {len(D["S"])} sugerencias, {os.path.getsize(a.salida) // 1024} KB')


if __name__ == '__main__':
    main()
