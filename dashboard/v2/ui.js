/* ===== piezas de interfaz compartidas ===== */
const IC={home:'<path d="M3 10.5L12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',ball:'<circle cx="12" cy="12" r="9"/><path d="M12 7l4.5 3.3-1.7 5.2H9.2L7.5 10.3z"/>',target:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 list:'<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',ticket:'<path d="M3 9V6a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v3a3 3 0 0 0 0 6v3a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-3a3 3 0 0 0 0-6z"/><path d="M14 5v14" stroke-dasharray="2 3"/>',
 wallet:'<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M16 15h2"/>',chart:'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',send:'<path d="M21 3L10 14M21 3l-7 18-4-7-7-4z"/>',db:'<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
 doc:'<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/>',more:'<circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>',x:'<path d="M6 6l12 12M18 6L6 18"/>',back:'<path d="M15 5l-7 7 7 7"/>'};
const ic=n=>`<svg class="i" viewBox="0 0 24 24">${IC[n]||''}</svg>`;
const PAGES={},NAV=[['inicio','Inicio','home'],['partidos','Partidos','ball'],['estrategia','Mi estrategia','target'],['cupon','Cupón','ticket'],['-','Explorar'],['lineas','Todas las líneas','list'],['jugadores','Jugadores','user'],['backtest','Backtest histórico','chart'],
 ['-','Seguimiento'],['historico','Histórico','doc'],['apuestas','Mis apuestas','wallet'],['aprender','Qué funciona','chart'],['enviadas','Lo que te envié','send'],['-','Respaldo'],['datos','Datos y límites','db'],['docs','Documentos','doc']];
const route=()=>{const h=(location.hash||'#/inicio').slice(2).split('/');return{pg:PAGES[h[0]]?h[0]:'inicio',arg:h.slice(1).map(decodeURIComponent)}};
const go=h=>{location.hash='#/'+h};
function setp(path,val){const ks=path.split('.');let o=ST;for(let i=0;i<ks.length-1;i++)o=o[ks[i]]=o[ks[i]]||{};o[ks[ks.length-1]]=val}
function getp(path,d){let o=ST;for(const k of path.split('.')){if(o==null)return d;o=o[k]}return o==null?d:o}
/* controles declarativos */
const chip=(path,val,lab,extra)=>`<button class="chip ${String(getp(path,''))===String(val)?'on':''}" data-set="${path}" data-val="${esc(val)}">${lab}${extra?`<small>${extra}</small>`:''}</button>`;
const tchip=(path,val,lab)=>`<button class="chip ${(getp(path,[])||[]).includes(val)?'on':''}" data-tog="${path}" data-val="${esc(val)}">${lab}</button>`;
const sel=(path,opts,lab)=>`<label class="f">${lab}<select data-bind="${path}">${opts.map(o=>{const[v,t]=Array.isArray(o)?o:[o,o];return`<option value="${esc(v)}" ${String(getp(path,''))===String(v)?'selected':''}>${esc(t)}</option>`}).join('')}</select></label>`;
const num=(path,lab,step,min,max)=>`<label class="f">${lab}<input type="number" data-bind="${path}" data-num step="${step||1}" ${min!=null?`min="${min}"`:''} ${max!=null?`max="${max}"`:''} value="${getp(path,'')}"></label>`;
const txt=(path,lab,ph)=>`<label class="f">${lab}<input type="search" data-bind="${path}" placeholder="${esc(ph||'')}" value="${esc(getp(path,''))}"></label>`;
const jorChips=(path,todas)=>`<div class="chips">${todas?chip(path,'','Todas'):''}${JORS.map(j=>chip(path,j,jorLab(j))).join('')}</div>`;
function toast(t){const e=$('#toast');e.textContent=t;e.style.display='block';clearTimeout(toast.t);toast.t=setTimeout(()=>e.style.display='none',2200)}
/* markdown mínimo */
function md(t){const out=[];let tb=[],ul=false;const inl=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/`([^`]+)`/g,'<code>$1</code>');
 const ft=()=>{if(tb.length){const rows=tb.filter(r=>!/^\s*\|?\s*:?-{2,}/.test(r)).map(r=>r.trim().replace(/^\||\|$/g,'').split('|'));out.push('<div class="tw"><table><tr>'+rows[0].map(c=>`<th>${inl(c.trim())}</th>`).join('')+'</tr>'+rows.slice(1).map(r=>'<tr>'+r.map(c=>`<td>${inl(c.trim())}</td>`).join('')+'</tr>').join('')+'</table></div>');tb=[]}},fu=()=>{if(ul){out.push('</ul>');ul=false}};
 String(t).split('\n').forEach(ln=>{if(/^\s*\|/.test(ln)){fu();tb.push(ln);return}ft();const h=ln.match(/^(#{1,4})\s+(.*)/);if(h){fu();out.push(`<h3>${inl(h[2])}</h3>`);return}
  const li=ln.match(/^\s*(?:[-*]|\d+\.)\s+(.*)/);if(li){if(!ul){out.push('<ul>');ul=true}out.push(`<li>${inl(li[1])}</li>`);return}fu();if(ln.trim())out.push(`<p>${inl(ln)}</p>`)});ft();fu();return'<div class="md">'+out.join('')+'</div>'}
/* resultado de una línea */
const rsTag=x=>x.rs==='C'?`<span class="tag ok">✓ se dio${x.real!=null?' ('+x.real+')':''}</span>`:x.rs==='F'?`<span class="tag bad">✗ no se dio${x.real!=null?' ('+x.real+')':''}</span>`:x.rs==='N'?'<span class="tag">nula</span>':x.rs?`<span class="tag warn">${x.rs==='MG'?'media ganada':'media perdida'}</span>`:'';
const regTxt=q=>q.n?`${q.c}/${q.n}`:'–';
function regCell(x){const r=reg(x);if(x.k==='G'){const V=valsG(x);return V&&V.length?`${pips(V,o=>hitG(o.v,x.l))} <b class="num">${regTxt(r.g)}</b>`:`<span class="mut xs">${histOf(x.p,x.j)?'sin minutos':DB.HIS[x.p]?'sin partidos en los últimos 10':'sin historial'}</span>`}
 const V=valsT(x),f=o=>hit(o.v,x.l,x.s);if(!V.l.length&&!V.v.length)return'<span class="mut xs">sin serie</span>';
 return`<span title="${esc(P[x.p].loc)}">${pips(V.l,f)} <b class="num">${regTxt(r.l)}</b></span> &nbsp;<span title="${esc(P[x.p].vis)}">${pips(V.v,f)} <b class="num">${regTxt(r.v)}</b></span>${r.h.n?` <span class="mut xs num">H2H ${regTxt(r.h)}</span>`:''}`}
const addBtn=x=>`<button class="btn add ${inCup(x)?'in':''}" data-act="cup" data-key="${esc(x.key)}" title="${inCup(x)?'Quitar del cupón':'Añadir al cupón'}" aria-label="cupón">${inCup(x)?'✓':'+'}</button>`;
/* fila de línea (sirve en móvil y escritorio) */
function li(x,o){o=o||{};const p=P[x.p],s=sentido(x);return`<div class="srow" data-act="line" data-key="${esc(x.key)}">
 <div class="score" style="--v:${s}" title="Índice de sentido (solo ordena)"><span>${s}</span></div>
 <div style="flex:1;min-width:0"><div class="b">${esc(tx(x))} <span class="num" style="color:var(--blue)">@${f2(x.c)}</span></div>
 ${o.noP?'':`<div class="xs mut">${esc(p.n)} · ${p.hh}${x.k==='G'&&x.tit!=null?(x.tit>=.7?' · titular probable':' · no está en el XI probable'):''}</div>`}
 <div class="sm" style="margin-top:3px">${regCell(x)} <span class="mut xs num">${x.col!=null?'· colchón '+(x.col>0?'+':'')+f1(x.col):''} · p ${pc(prob(x))}${x.pm==null?'≈':''}</span> ${rsTag(x)}</div></div>${addBtn(x)}</div>`}
const listLi=(rows,o)=>rows.length?rows.map(x=>li(x,o)).join(''):`<div class="empty">${(o&&o.empty)||'Ninguna línea con este filtro.'}</div>`;
/* cajón */
function drawer(html){$('#dr').innerHTML=`<button class="btn x" data-act="close" aria-label="Cerrar">${ic('x')}</button>`+html;$('#dr').classList.add('on');$('#ov').classList.add('on');$('#dr').scrollTop=0}
function closeDr(){$('#dr').classList.remove('on');$('#ov').classList.remove('on');DR=null}
let DR=null;
function chartTitle(x,sd){const p=P[x.p],eq=sd==='l'?p.loc:p.vis,u=(MK[x.m]||x.m).toLowerCase();
 if(sd==='h')return`Enfrentamientos directos: ${u}${x.a==='total'?' del partido':x.a==='1T'?' en el 1er tiempo':x.a==='2T'?' en el 2º tiempo':''}`;
 if(x.a==='total')return`${eq}: ${u} totales en sus partidos`;if(x.a==='1T'||x.a==='2T')return`${eq}: ${u} en el ${AMB[x.a].toLowerCase()} de sus partidos`;
 const propio=(x.a==='local')===(sd==='l');return`${eq}: ${u} ${propio?'que hace':'que le hacen (concede)'}`}
function lineCharts(x){if(x.k==='G'){const V=valsG(x);if(!V)return`<div class="card"><div class="empty">No hay historial de ${esc(x.j)} en los últimos 10 partidos de su equipo.</div></div>`;
  const r=reg(x).g,avg=V.reduce((a,o)=>a+o.v,0)/Math.max(V.length,1),mins=V.reduce((a,o)=>a+o.min,0)/Math.max(V.length,1);
  return`<div class="card"><div class="hd"><h3 style="margin:0">${esc(x.j)}: ${esc((JM[x.m]||x.m).toLowerCase())} por partido</h3><div class="sp"></div><span class="tag blue">${regTxt(r)} cumple</span></div>
  ${matchBars(V,{line:x.l,ge:true,lineLab:x.l+' o más',unit:JM[x.m]||x.m})}<div class="xs mut">Solo partidos con minutos. Promedio ${f1(avg)} en ${f1(mins)} min por partido. Debajo de cada barra: rival, sede y marcador de su equipo.</div></div>`}
 const V=valsT(x),r0=reg(x),cond=ST.sede==='cond',f=o=>hit(o.v,x.l,x.s),one=(sd)=>{let a=sd==='h'?V.h.map(o=>({v:o.v,m:[o.m[0],'','',o.m[3],o.m[4]]})):V[sd];if(cond&&sd!=='h')a=a.filter(o=>o.m[2]===(sd==='l'?'L':'V'));const r={[sd]:cond&&sd!=='h'?cnt(a,f):r0[sd]};if(sd==='h'&&!a.length)return`<div class="card"><h3>Enfrentamientos directos</h3><div class="empty sm">No hay directos con estadística en la muestra.</div></div>`;
  const avg=a.length?a.reduce((s,o)=>s+o.v,0)/a.length:null;
  return`<div class="card"><div class="hd"><h3 style="margin:0">${esc(chartTitle(x,sd))}</h3><div class="sp"></div><span class="tag ${r[sd].n&&r[sd].c>=need(ST.strat.K,r[sd].n)?'blue':''}">${regTxt(r[sd])} cumple</span></div>
  ${matchBars(a,{line:x.l,side:x.s,lineLab:x.s+' '+String(x.l).replace('.',','),unit:MK[x.m],lab:sd==='h'?(o=>(o.m[0]||'').slice(2,4)?"'"+(o.m[0]||'').slice(2,4):'·'):null})}${avg!=null?`<div class="xs mut">Promedio ${f1(avg)} en ${a.length} partidos${sd!=='h'?'. Debajo de cada barra: rival, sede (L/V) y marcador':''}.</div>`:''}</div>`};
 return one('l')+one('v')+one('h')}
const sedeChips=()=>`<div class="chips">${chip('sede','todos','Todos sus partidos')}${chip('sede','cond','Solo en su condición (local en casa, visitante fuera)')}</div>`;
function openLine(key){const x=BYKEY.get(key);if(!x)return;DR={t:'line',key};const p=P[x.p],sibs=ALL.filter(y=>y.k===x.k&&y.p===x.p&&y.m===x.m&&(x.k==='G'?y.j===x.j:(y.a===x.a&&y.s===x.s))).sort((a,b)=>a.l-b.l);
 const otro=x.k==='T'?T.find(y=>y.p===x.p&&y.m===x.m&&y.a===x.a&&y.l===x.l&&y.s!==x.s):null;
 drawer(`<div class="card"><div class="xs mut"><a href="#/partido/${x.p}" data-act="close">${esc(p.n)}</a> · ${jorLab(p.jor)} ${p.hh}</div><h2 style="margin:4px 0 10px">${esc(tx(x))}</h2>
 <div class="chips scroll" style="margin-bottom:10px">${sibs.map(y=>`<button class="chip ${y===x?'on':''}" data-act="line" data-key="${esc(y.key)}">${x.k==='G'?y.l+'+':String(y.l).replace('.',',')}<small>@${f2(y.c)}</small></button>`).join('')}${otro?`<button class="chip" data-act="line" data-key="${esc(otro.key)}">ver ${otro.s}<small>@${f2(otro.c)}</small></button>`:''}</div>
 <div class="kpis" style="grid-template-columns:repeat(auto-fit,minmax(92px,1fr));margin-bottom:10px">
  <div class="kpi"><div class="v num">${f2(x.c)}</div><div class="l">cuota</div></div><div class="kpi"><div class="v num">${pc(prob(x))}</div><div class="l">p ${x.pm==null?'(solo cuota)':'modelo'}</div></div>
  <div class="kpi"><div class="v num">${x.e!=null?f1(x.e):'–'}</div><div class="l">esperado</div></div><div class="kpi"><div class="v num" style="color:${x.col>0?'var(--ok)':x.col<0?'var(--bad)':'inherit'}">${x.col!=null?(x.col>0?'+':'')+f1(x.col):'–'}</div><div class="l">colchón</div></div>
  <div class="kpi"><div class="v num">${sentido(x)}</div><div class="l">sentido</div></div></div>
 <div class="row">${rsTag(x)}${pasa(x,ST.strat)?'<span class="tag blue">pasa tu estrategia</span>':'<span class="tag">no pasa tu estrategia</span>'}${x.al?`<span class="tag warn">alerta del modelo</span>`:''}<div class="sp"></div>
 <button class="btn ${inCup(x)?'':'pri'}" data-act="cup" data-key="${esc(x.key)}">${inCup(x)?'Quitar del cupón':'Añadir al cupón'}</button></div></div>
 ${x.k==='T'?`<div style="margin-bottom:10px">${sedeChips()}</div>`:''}${lineCharts(x)}
 <div class="card sm mut"><b>Cómo leerlo.</b> Azul = el partido cumplió esta línea; gris = no. La raya punteada es la línea de Betano. «Esperado» = (lo que hace un equipo + lo que concede el rival) ÷ 2, sumado para el total; «colchón» = distancia entre el esperado y la línea a tu favor. ${x.m==='tarjetas'?'Tarjetas: Betano cuenta puntos (roja = 2) y aquí solo hay amarillas.':''}${x.k==='G'&&x.m==='entradas'?'Entradas: aquí son las ganadas; Betano cuenta todas.':''}</div>`)}
/* tooltip */
function tipInit(){const t=$('#tip');const show=(e)=>{const el=e.target.closest&&e.target.closest('[data-tip]');if(!el){t.style.display='none';return}t.innerHTML=el.dataset.tip;t.style.display='block';const cx=e.touches?e.touches[0].clientX:e.clientX,cy=e.touches?e.touches[0].clientY:e.clientY,w=t.offsetWidth,h=t.offsetHeight;
  t.style.left=Math.max(6,Math.min(innerWidth-w-6,cx-w/2))+'px';t.style.top=(cy-h-14<6?cy+18:cy-h-14)+'px'};
 document.addEventListener('mousemove',show);document.addEventListener('touchstart',show,{passive:true});document.addEventListener('scroll',()=>t.style.display='none',true)}
/* tabla ordenable genérica: cols [{h, v:x=>valor, f:x=>html, r?}] */
function table(id,rows,cols,o){o=o||{};const st=getp('f.sort.'+id,null),lim=getp('f.lim.'+id,o.lim||100);let rs=rows.slice();
 if(st){const c=cols[st.c];if(c&&c.v)rs.sort((a,b)=>{const x=c.v(a),y=c.v(b);return(x==null)-(y==null)||(x>y?1:x<y?-1:0)*(st.d)})}
 return`<div class="tw"><table><tr>${cols.map((c,i)=>`<th class="${c.r?'r':''} ${st&&st.c===i?'sorted':''}" ${c.v?`data-sort="${id}" data-col="${i}"`:''}>${c.h}${st&&st.c===i?(st.d>0?' ▲':' ▼'):''}</th>`).join('')}</tr>
 ${rs.slice(0,lim).map(x=>`<tr ${o.row?o.row(x):''}>${cols.map(c=>`<td class="${c.r?'r num':''}">${c.f(x)}</td>`).join('')}</tr>`).join('')}</table></div>
 ${rs.length>lim?`<div class="c" style="padding:10px"><button class="btn" data-act="more" data-id="${id}" data-n="${lim+200}">Mostrar más (${rs.length-lim} restantes)</button></div>`:''}${rs.length?'':`<div class="empty">${o.empty||'Nada con este filtro.'}</div>`}`}
