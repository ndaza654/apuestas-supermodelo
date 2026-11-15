'use strict';
/* Motor común del informe v2 (variantes A «Tablero», B «Partido a partido», C «Cupón»). Solo lectura: sin red, sin librerías.
   Los datos vienen de informe_v2.py (D). Toda la regularidad («X de N») se recalcula aquí a partir de las series por partido,
   de modo que K, N, n mínimo y «en qué equipos» son ajustables sin volver a correr el pipeline. El colchón es informativo: ningún filtro lo exige por defecto. */
const D=/*DATA*/;
const V=D.variante;
const $=(s,e)=>(e||document).querySelector(s),$$=(s,e)=>[...(e||document).querySelectorAll(s)];
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const pct=x=>x==null||isNaN(x)?'–':(100*x).toFixed(0)+'%',f1=x=>x==null||isNaN(x)?'–':(+x).toFixed(1),f2=x=>x==null||isNaN(x)?'–':(+x).toFixed(2);
const sg=x=>x==null||isNaN(x)?'–':(x>0?'+':'')+(+x).toFixed(2);
const cop=n=>(n<0?'-$':'$')+Math.abs(Math.round(n)).toLocaleString('es-CO');
const LS={get(k,d){try{const v=localStorage.getItem('v2'+V+k);return v?Object.assign({},d,JSON.parse(v)):Object.assign({},d)}catch(e){return Object.assign({},d)}},
  set(k,v){try{localStorage.setItem('v2'+V+k,JSON.stringify(v))}catch(e){}}};
const MK=D.MK,AM={total:'total',local:'local',visitante:'visitante','1T':'1.er tiempo','2T':'2.º tiempo'};
const RS={C:['cumplió','ok'],F:['falló','ko'],MG:['media ganada','ok'],MP:['media perdida','ko'],N:['nula','mu']};
const sh=n=>String(n).replace(' - ',' – ');
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
/* ---------- estado ---------- */
const ST0={K:D.K,N:D.N,MN:D.MN,who:'ambos',Kj:3,Nj:5,MNj:3,cmin:1.35};
let ST=LS.get('st',ST0);ST.N=clamp(+ST.N||D.N,1,D.N);ST.K=clamp(+ST.K||D.K,1,ST.N);ST.MN=clamp(+ST.MN||D.MN,1,ST.N);
let FT=LS.get('ft',{}),FJ=LS.get('fj',{}),CUP=LS.get('cup',{x:[]}).x||[],TAB=LS.get('tab',{t:'ana'}).t,SEL={t:null,j:null},LIM={t:120,j:120,s:200};
const save=()=>{LS.set('st',ST);LS.set('ft',FT);LS.set('fj',FJ);LS.set('cup',{x:CUP});LS.set('tab',{t:TAB})};
/* ---------- datos ---------- */
const T=D.L.map((r,i)=>({i,p:r[0],m:r[1],a:r[2],s:r[3],l:r[4],c:r[5],e:r[6],co:r[7],pm:r[8],pk:r[9],ev:r[10],al:r[11],rs:r[12],rv:r[13]}));
const J=D.J.map((r,i)=>({i,p:r[0],m:r[1],j:r[2],side:r[3],ti:r[4],l:r[5],s:r[6],c:r[7],pm:r[8],pk:r[9],ev:r[10],rs:r[11],rv:r[12],es:r[13],co:r[14]}));
const hit=(v,l,s)=>{const q=Math.round(l*4)%2===1;return s==='Menos'?v<(q?l-.25:l):v>(q?l+.25:l)};
const cache=new Map();
/* serie por línea: lo que cada equipo (y los directos) hizo en esa estadística y ámbito; más reciente primero */
function vals(t){if(cache.has(t.i))return cache.get(t.i);const S=(D.SER[t.p]||{})[t.m],M=D.META[t.p]||{},o={l:[],v:[],h:[]};
 if(S)for(const side of['l','v','h'])(S[side]||[]).forEach((x,k)=>{const a=x[0],b=x[1],a1=x[2],b1=x[3];let v=null;
  if(a==null||b==null)v=null;else if(t.a==='total')v=a+b;else if(t.a==='local')v=side==='v'?b:a;else if(t.a==='visitante')v=side==='v'?a:b;
  else if(t.a==='1T')v=a1==null?null:a1+b1;else if(t.a==='2T')v=a1==null?null:(a+b)-(a1+b1);
  if(v!=null)o[side].push({v,m:(M[side]||[])[k]})});
 cache.set(t.i,o);return o}
function regT(t,n,K,MN){const V=vals(t),f=a=>{const w=a.slice(0,n),c=w.filter(x=>hit(x.v,t.l,t.s)).length;return{c,n:w.length,ok:w.length>=MN&&c>=K}};return{l:f(V.l),v:f(V.v),h:f(V.h)}}
function cumT(t,n,K,MN,who){n=n==null?ST.N:n;K=K==null?ST.K:K;MN=MN==null?ST.MN:MN;who=who||ST.who;const r=regT(t,n,K,MN);if(!r.l.n||!r.v.n)return null;
 return who==='local'?r.l.ok:who==='visitante'?r.v.ok:who==='alguno'?(r.l.ok||r.v.ok):(r.l.ok&&r.v.ok)}
const IDX={'jugador:remates':2,'jugador:al_arco':3,'jugador:faltas':8,'jugador:entradas':9};
function hv(h,m){if(IDX[m]!=null)return h[IDX[m]];if(m==='jugador:anota')return h[4]>=1?1:0;if(m==='jugador:asiste')return h[5]>=1?1:0;
 if(m==='jugador:anota_o_asiste')return(h[4]+h[5])>=1?1:0;if(m==='jugador:tarjeta')return(h[6]+h[7])>=1?1:0;return null}
function hist(j){const H=(D.HIS[j.p]||{})[j.j];return H||null}
function pvals(j){const H=hist(j);if(!H)return null;return H.filter(x=>x[1]>0).map(x=>({v:hv(x,j.m),m:x})).filter(x=>x.v!=null)}
function cumJ(j,n,K,MN){n=n==null?ST.Nj:n;K=K==null?ST.Kj:K;MN=MN==null?ST.MNj:MN;const a=pvals(j);if(!a)return null;const w=a.slice(0,n),c=w.filter(x=>x.v>=j.l).length;return{c,n:w.length,ok:w.length>=MN&&c>=K}}
/* ---------- gráficos (SVG sin librerías) ---------- */
function bars(arr,l,s,n,o){o=o||{};const w=o.w||230,h=o.h||74,pad=15;if(!arr.length)return`<div class="nod" style="width:${w}px;height:${h}px">sin muestra</div>`;
 const a=arr.map((x,k)=>({...x,k})).reverse(),mx=Math.max(l*1.3,...a.map(x=>x.v),1),bw=Math.min(24,(w-10)/a.length-3),H=h-pad-11;
 const y=v=>pad+H-(v/mx)*H;let g='';
 a.forEach((x,i)=>{const X=6+i*(bw+3),ok=s==='J'?x.v>=l:hit(x.v,l,s),fuera=x.k>=n,yy=y(x.v),m=x.m||[];
  const tip=o.player?`${m[0]||''} · ${m[1]||''}′ · ${x.v}`:`${m[0]||''} vs ${m[1]||''}${m[2]?' ('+m[2]+')':''} ${m[3]!=null?m[3]+'-'+m[4]+' ·':''} ${x.v}`;
  g+=`<g opacity="${fuera?.35:1}"><title>${esc(tip)}</title><rect x="${X}" y="${yy}" width="${bw}" height="${Math.max(1,pad+H-yy)}" rx="2" class="${ok?'bo':'bk'}"/><text x="${X+bw/2}" y="${yy-2}" text-anchor="middle" class="bt">${x.v%1?f1(x.v):x.v}</text></g>`});
 const yl=y(l);g+=`<line x1="2" x2="${w-2}" y1="${yl}" y2="${yl}" class="bl"/><text x="${w-3}" y="${yl-2}" text-anchor="end" class="bl2">${l}</text>`;
 return`<svg class="bars" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img">${g}</svg>`}
function gauge(t){if(t.e==null)return'<div class="mut small">esperado: sin dato</div>';const lo=Math.min(t.l,t.e)*.7,hi=Math.max(t.l,t.e)*1.3||1,X=v=>6+(v-lo)/(hi-lo)*188;
 const good=t.s==='Menos'?t.e<t.l:t.e>t.l;
 return`<svg viewBox="0 0 200 34" width="200" height="34" class="gauge"><rect x="6" y="14" width="188" height="6" rx="3" class="gb"/><rect x="${Math.min(X(t.l),X(t.e))}" y="14" width="${Math.abs(X(t.e)-X(t.l))}" height="6" class="${good?'gg':'gr'}"/>
 <line x1="${X(t.l)}" x2="${X(t.l)}" y1="8" y2="26" class="bl"/><text x="${X(t.l)}" y="6" text-anchor="middle" class="bt">línea ${t.l}</text><circle cx="${X(t.e)}" cy="17" r="5" class="gd"/><text x="${X(t.e)}" y="33" text-anchor="middle" class="bt">esperado ${f2(t.e)}</text></svg>`}
/* ---------- piezas ---------- */
const P=i=>D.P[i];
const stBadge=p=>p.est==='final'?`<span class="pill fin">final ${p.g[0]}-${p.g[1]}</span>`:p.est==='vivo'?`<span class="pill liv">en juego ${p.g[0]}-${p.g[1]}${p.min?' · '+esc(p.min):''}</span>`:'<span class="pill">por jugar</span>';
function rsBadge(x){if(x.rs&&RS[x.rs])return`<span class="pill ${RS[x.rs][1]}">${RS[x.rs][0]}${x.rv!=null?' · real '+x.rv:''}</span>`;const p=P(x.p);return p.est==='final'?'<span class="pill mu">sin calificar</span>':p.est==='vivo'?'<span class="pill liv">en juego</span>':''}
const lbl=t=>`${MK[t.m]||t.m}${t.a==='total'?'':' · '+AM[t.a]} ${t.s} ${t.l}`;
const lblJ=j=>`${j.j} · ${(D.MKJ[j.m]||j.m)} ${j.s==='Sí'?'sí':j.l+' o más'}`;
const chip=(r,txt)=>r.n?`<span class="xn ${r.ok?'y':''}">${txt} ${r.c}/${r.n}</span>`:`<span class="xn">${txt} –</span>`;
function cumBadge(c){return c===true?'<span class="pill ok">cumple</span>':c===false?'<span class="pill no">no cumple</span>':'<span class="pill mu">sin muestra</span>'}
function inCup(k){return CUP.includes(k)}
const kT=t=>'T'+t.i,kJ=j=>'J'+j.i;
function cardT(t,full){const p=P(t.p),r=regT(t,ST.N,ST.K,ST.MN),c=cumT(t),V=vals(t);
 return`<div class="lc ${c===true?'cum':''}" data-k="${kT(t)}"><div class="lh"><div><b>${esc(lbl(t))}</b><div class="mut small">${esc(sh(p.n))} · ${esc(p.hora)} ${stBadge(p)}</div></div><div class="od">${f2(t.c)}<small>${inCup(kT(t))?'en cupón':'cuota'}</small></div></div>
 <div class="mx"><span>p ${pct(t.pm)}</span><span class="${t.ev>0?'ok':''}">EV ${t.ev==null?'–':(t.ev*100).toFixed(0)+'%'}</span><span>esp. ${f2(t.e)}</span><span class="${t.co>=0?'ok':'bad'}">colchón ${sg(t.co)}</span>${cumBadge(c)}${rsBadge(t)}</div>
 <div class="xr">${chip(r.l,'L')}${chip(r.v,'V')}${r.h.n?chip(r.h,'directos'):''}</div>
 ${full?`<div class="ch"><div><div class="cl">${esc(D.P[t.p].loc)} · últimos ${Math.min(ST.N,V.l.length)}</div>${bars(V.l,t.l,t.s,ST.N)}</div><div><div class="cl">${esc(D.P[t.p].vis)} · últimos ${Math.min(ST.N,V.v.length)}</div>${bars(V.v,t.l,t.s,ST.N)}</div>${V.h.length?`<div><div class="cl">Directos (${V.h.length})</div>${bars(V.h,t.l,t.s,99)}</div>`:''}</div>${gauge(t)}`
 :`<div class="ch mini"><div>${bars(V.l,t.l,t.s,ST.N,{w:130,h:46})}</div><div>${bars(V.v,t.l,t.s,ST.N,{w:130,h:46})}</div></div>`}
 <div class="ac"><button class="b" data-add="${kT(t)}">${inCup(kT(t))?'Quitar del cupón':'Añadir al cupón'}</button><button class="b" data-det="${kT(t)}">${full?'Ocultar':'Ver detalle'}</button></div></div>`}
function detT(t){const p=P(t.p),V=vals(t),r=regT(t,ST.N,ST.K,ST.MN);const row=(nm,a,rr)=>`<div class="dr"><div class="cl"><b>${esc(nm)}</b> · ${rr.n?rr.c+' de '+rr.n+' cumplen la línea':'sin muestra'} ${rr.n?(rr.ok?'<span class="pill ok">regular</span>':'<span class="pill no">no regular</span>'):''}</div>${bars(a,t.l,t.s,ST.N,{w:300,h:92})}
 <div class="small mut">${a.slice(0,ST.N).map(x=>(x.m?esc(x.m[0].slice(5))+' '+esc(x.m[1]):'')+': <b>'+x.v+'</b>').join(' · ')}</div></div>`;
 return`<div class="det"><h3>${esc(lbl(t))} <span class="od2">@ ${f2(t.c)}</span></h3><div class="mut">${esc(sh(p.n))} · ${esc(p.liga)} · ${esc(p.hora)} ${stBadge(p)} ${rsBadge(t)}</div>
 <div class="kp"><div>p modelo<b>${pct(t.pm)}</b></div><div>p mercado<b>${pct(t.pk)}</b></div><div>EV<b class="${t.ev>0?'ok':''}">${t.ev==null?'–':(t.ev*100).toFixed(0)+'%'}</b></div><div>Esperado<b>${f2(t.e)}</b></div><div>Colchón<b class="${t.co>=0?'ok':'bad'}">${sg(t.co)}</b></div><div>Cumple (${ST.K}/${ST.N})<b>${cumBadge(cumT(t))}</b></div></div>
 ${gauge(t)}${row(p.loc+' (últimos '+Math.min(ST.N,V.l.length)+')',V.l,r.l)}${row(p.vis+' (últimos '+Math.min(ST.N,V.v.length)+')',V.v,r.v)}${V.h.length?row('Enfrentamientos directos',V.h,r.h):''}
 ${t.al?`<div class="warn small">Alerta del modelo: ${esc(t.al)}</div>`:''}
 <div class="small mut">Verde = la línea se cumple por completo en ese partido; rojo = no; atenuado = fuera de los últimos ${ST.N}. Línea punteada = línea de Betano. Colchón = esperado − línea (Más) o línea − esperado (Menos): informativo.</div>
 <div class="ac"><button class="b pri" data-add="${kT(t)}">${inCup(kT(t))?'Quitar del cupón':'Añadir al cupón'}</button></div></div>`}
function cardJ(j,full){const p=P(j.p),c=cumJ(j),a=pvals(j);
 return`<div class="lc ${c&&c.ok?'cum':''}" data-k="${kJ(j)}"><div class="lh"><div><b>${esc(lblJ(j))}</b><div class="mut small">${esc(sh(p.n))} · ${esc(p.hora)} ${stBadge(p)} · ${j.side==='L'?'local':'visitante'}${j.ti!=null?' · titular '+pct(j.ti):''}</div></div><div class="od">${f2(j.c)}<small>cuota</small></div></div>
 <div class="mx"><span>p ${pct(j.pm)}</span><span class="${j.ev>0?'ok':''}">EV ${j.ev==null?'–':(j.ev*100).toFixed(0)+'%'}</span><span>esp. ${j.es==null?'–':f2(j.es)}</span>${j.co!=null?`<span class="${j.co>=0?'ok':'bad'}">colchón ${sg(j.co)}</span>`:''}${c?(c.ok?'<span class="pill ok">regular</span>':'<span class="pill no">no regular</span>'):'<span class="pill mu">sin historial</span>'}${rsBadge(j)}</div>
 <div class="xr">${c?`<span class="xn ${c.ok?'y':''}">historial ${c.c}/${c.n}</span>`:'<span class="xn">historial no recolectado</span>'}</div>
 ${a&&a.length?`<div class="ch"><div>${bars(a,j.l,'J',ST.Nj,{w:full?300:150,h:full?92:50,player:1})}</div></div>`:''}
 ${full&&a&&a.length?histTabla(j):''}
 <div class="ac"><button class="b" data-add="${kJ(j)}">${inCup(kJ(j))?'Quitar del cupón':'Añadir al cupón'}</button><button class="b" data-det="${kJ(j)}">${full?'Ocultar':'Ver detalle'}</button></div></div>`}
function histTabla(j){const H=hist(j);return`<div class="tw"><table class="mini"><tr><th>Fecha</th><th class="n">Min</th><th class="n">Remates</th><th class="n">Al arco</th><th class="n">Goles</th><th class="n">Asist.</th><th class="n">Faltas</th><th class="n">Entradas</th><th class="n">Tarj.</th></tr>${H.map(h=>`<tr><td>${esc(h[0])}</td><td class="n">${h[1]}</td><td class="n">${h[2]}</td><td class="n">${h[3]}</td><td class="n">${h[4]}</td><td class="n">${h[5]}</td><td class="n">${h[8]}</td><td class="n">${h[9]}</td><td class="n">${h[6]+h[7]}</td></tr>`).join('')}</table></div>`}
/* ---------- filtros ---------- */
const sel=(id,k,opts,v,t)=>`<label>${t}<select data-f="${k}" id="${id}">${opts.map(([a,b])=>`<option value="${esc(a)}" ${String(v)===String(a)?'selected':''}>${esc(b)}</option>`).join('')}</select></label>`;
const num=(k,v,t,st,ph)=>`<label>${t}<input type="number" step="${st||0.05}" data-f="${k}" value="${v==null?'':v}" placeholder="${ph||''}"></label>`;
const partOpts=[['','todos los partidos'],...D.P.map((p,i)=>[i,p.hora+' '+sh(p.n)])];
function kbar(){const n=D.N;const tabla=[];
 return`<div class="kb"><b>«Cumple» =</b> al menos <input type="number" min="1" max="${ST.N}" data-s="K" value="${ST.K}"> de los últimos <input type="number" min="1" max="${D.N}" data-s="N" value="${ST.N}"> partidos <span class="mut small">(hay ${D.N} por equipo) · n mínimo</span> <input type="number" min="1" max="${ST.N}" data-s="MN" value="${ST.MN}">
 en <select data-s="who">${[['ambos','ambos equipos'],['local','solo el local'],['visitante','solo el visitante'],['alguno','cualquiera de los dos']].map(([a,b])=>`<option value="${a}" ${ST.who===a?'selected':''}>${b}</option>`).join('')}</select>
 <span class="atj">${[[7,10],[6,10],[5,7],[4,5],[3,3]].filter(([k,n])=>n<=D.N).map(([k,n])=>`<button class="chipb ${ST.K===k&&ST.N===n?'on':''}" data-atj="${k},${n}">${k} de ${n}</button>`).join('')}</span></div>`}
function kconteo(rows){const out=[];for(let k=1;k<=ST.N;k++){let c=0;for(const t of rows)if(cumT(t,ST.N,k,Math.min(ST.MN,ST.N),ST.who)===true)c++;out.push(`<button class="chipb ${k===ST.K?'on':''}" data-atj="${k},${ST.N}">${k}/${ST.N}: ${c}</button>`)}return`<div class="kc"><span class="mut small">Líneas que cumplen con cada K (con los demás filtros):</span> ${out.join('')}</div>`}
function fT(){const F=FT;return`<div class="fgrid">${sel('ft_p','p',partOpts,F.p||'','Partido')}${sel('ft_m','m',[['','todos'],...Object.keys(MK).map(k=>[k,MK[k]])],F.m||'','Mercado')}${sel('ft_a','a',[['','todos'],...Object.keys(AM).map(k=>[k,AM[k]])],F.a||'','Ámbito')}${sel('ft_s','s',[['','Más y Menos'],['Más','Más'],['Menos','Menos']],F.s||'','Lado')}
 ${num('cmin',F.cmin,'Cuota ≥',0.05,'1.35')}${num('cmax',F.cmax,'Cuota ≤',0.05)}${num('pmin',F.pmin,'p modelo ≥',0.05,'0.6')}${num('evmin',F.evmin,'EV ≥',0.01)}${num('comin',F.comin,'Colchón ≥',0.25)}${num('comax',F.comax,'Colchón ≤',0.25)}
 ${sel('ft_c','c',[['','Cumple: todas'],['si','Solo las que cumplen'],['no','Solo las que no'],['nd','Sin muestra']],F.c||'','Regularidad')}${sel('ft_r','r',[['','Resultado: todos'],['G','Ya calificadas'],['C','Cumplieron'],['F','Fallaron'],['P','Sin resultado']],F.r||'','Resultado')}
 <label>Buscar<input type="search" data-f="q" value="${esc(F.q||'')}" placeholder="córners, Portugal…"></label>${sel('ft_o','o',[['p','Mayor p modelo'],['c','Mayor cuota'],['co','Mayor colchón'],['ev','Mayor EV'],['h','Hora del partido']],F.o||'p','Ordenar')}
 <button class="b" data-clr="t">Limpiar</button></div>`}
function fJ(){const F=FJ;return`<div class="fgrid">${sel('fj_p','p',partOpts,F.p||'','Partido')}${sel('fj_m','m',[['','todos'],...Object.keys(D.MKJ).map(k=>[k,D.MKJ[k]])],F.m||'','Mercado')}${sel('fj_side','side',[['','ambos equipos'],['L','local'],['V','visitante']],F.side||'','Equipo')}
 ${num('cmin',F.cmin,'Cuota ≥',0.05,'1.35')}${num('cmax',F.cmax,'Cuota ≤',0.05)}${num('pmin',F.pmin,'p modelo ≥',0.05)}${num('evmin',F.evmin,'EV ≥',0.01)}${num('timin',F.timin,'Titular ≥',0.1,'0.7')}${num('hmin',F.hmin,'Partidos de historial ≥',1,'3')}
 ${sel('fj_c','c',[['','Regularidad: todas'],['si','Regulares'],['no','No regulares'],['nd','Sin historial']],F.c||'','Historial')}${sel('fj_r','r',[['','Resultado: todos'],['G','Ya calificadas (sin nulas)'],['C','Cumplieron'],['F','Fallaron'],['N','Nulas (no jugó)'],['P','Sin resultado']],F.r||'','Resultado')}
 <label>Buscar<input type="search" data-f="q" value="${esc(F.q||'')}" placeholder="jugador, remates…"></label>${sel('fj_o','o',[['p','Mayor p modelo'],['c','Mayor cuota'],['ev','Mayor EV'],['r','Mejor historial'],['h','Hora del partido']],F.o||'p','Ordenar')}<button class="b" data-clr="j">Limpiar</button></div>
 <div class="kb"><b>Historial regular</b> = al menos <input type="number" min="1" max="10" data-s="Kj" value="${ST.Kj}"> de los últimos <input type="number" min="1" max="10" data-s="Nj" value="${ST.Nj}"> partidos jugados · n mínimo <input type="number" min="1" max="10" data-s="MNj" value="${ST.MNj}"></div>`}
function filtT(){const F=FT,q=(F.q||'').toLowerCase();let r=T.filter(t=>{if(F.p!==''&&F.p!=null&&t.p!==+F.p)return 0;if(F.m&&t.m!==F.m)return 0;if(F.a&&t.a!==F.a)return 0;if(F.s&&t.s!==F.s)return 0;
  if(F.cmin!=null&&F.cmin!==''&&!(t.c>=+F.cmin))return 0;if(F.cmax!=null&&F.cmax!==''&&!(t.c<=+F.cmax))return 0;if(F.pmin!=null&&F.pmin!==''&&!(t.pm>=+F.pmin))return 0;if(F.evmin!=null&&F.evmin!==''&&!(t.ev>=+F.evmin))return 0;
  if(F.comin!=null&&F.comin!==''&&!(t.co!=null&&t.co>=+F.comin))return 0;if(F.comax!=null&&F.comax!==''&&!(t.co!=null&&t.co<=+F.comax))return 0;
  if(F.r==='G'&&!t.rs)return 0;if(F.r==='P'&&t.rs)return 0;if((F.r==='C'||F.r==='F')&&t.rs!==F.r)return 0;
  if(q&&!(sh(P(t.p).n)+' '+lbl(t)).toLowerCase().includes(q))return 0;return 1});
 const base=r;if(F.c){r=r.filter(t=>{const c=cumT(t);return F.c==='si'?c===true:F.c==='no'?c===false:c===null})}
 const o=F.o||'p',key={p:t=>-(t.pm||0),c:t=>-(t.c||0),co:t=>-(t.co==null?-99:t.co),ev:t=>-(t.ev==null?-99:t.ev),h:t=>P(t.p).hora+String(t.p).padStart(2,'0')}[o];
 r=r.slice().sort((a,b)=>{const x=key(a),y=key(b);return x<y?-1:x>y?1:0});return{r,base}}
function filtJ(){const F=FJ,q=(F.q||'').toLowerCase();let r=J.filter(j=>{if(F.p!==''&&F.p!=null&&j.p!==+F.p)return 0;if(F.m&&j.m!==F.m)return 0;if(F.side&&j.side!==F.side)return 0;
  if(F.cmin!=null&&F.cmin!==''&&!(j.c>=+F.cmin))return 0;if(F.cmax!=null&&F.cmax!==''&&!(j.c<=+F.cmax))return 0;if(F.pmin!=null&&F.pmin!==''&&!(j.pm>=+F.pmin))return 0;if(F.evmin!=null&&F.evmin!==''&&!(j.ev>=+F.evmin))return 0;
  if(F.timin!=null&&F.timin!==''&&!(j.ti!=null&&j.ti>=+F.timin))return 0;
  if(F.r==='G'&&!(j.rs&&j.rs!=='N'))return 0;if(F.r==='P'&&j.rs)return 0;if((F.r==='C'||F.r==='F'||F.r==='N')&&j.rs!==F.r)return 0;
  if(q&&!(sh(P(j.p).n)+' '+lblJ(j)).toLowerCase().includes(q))return 0;
  const c=cumJ(j);if(F.hmin!=null&&F.hmin!==''&&!(c&&c.n>=+F.hmin))return 0;if(F.c==='si'&&!(c&&c.ok))return 0;if(F.c==='no'&&!(c&&!c.ok))return 0;if(F.c==='nd'&&c)return 0;return 1});
 const o=F.o||'p',key={p:j=>-(j.pm||0),c:j=>-(j.c||0),ev:j=>-(j.ev==null?-99:j.ev),r:j=>{const c=cumJ(j);return c&&c.n?-c.c/c.n-c.n/100:9},h:j=>P(j.p).hora+String(j.p).padStart(2,'0')}[o];
 r=r.slice().sort((a,b)=>{const x=key(a),y=key(b);return x<y?-1:x>y?1:0});return r}
/* resumen de un conjunto: líneas ya calificadas, % real contra p y 1 unidad plana */
function agg(rows,solo){let n=0,c=0,ps=0,pk=0,roi=0,np=0;for(const x of rows){if(!x.rs||x.rs==='N')continue;if(x.rs==='MG'){roi+=(x.c-1)/2;continue}if(x.rs==='MP'){roi-=.5;continue}n++;const y=x.rs==='C'?1:0;c+=y;roi+=y?x.c-1:-1;if(x.pm!=null){ps+=x.pm;np++}if(x.pk!=null)pk+=x.pk}
 return{n,c,real:n?c/n:null,p:np?ps/np:null,pk:n?pk/n:null,roi:n?roi/n:null}}
const aggTxt=a=>a.n?`<b>${a.c}/${a.n}</b> (${pct(a.real)}) · p modelo ${pct(a.p)} · p mercado ${pct(a.pk)} · <span class="${a.roi>=0?'ok':'bad'}">1 u plana ${a.roi>=0?'+':''}${(a.roi*100).toFixed(0)}%</span>`:'<span class="mut">ninguna calificada</span>';
/* ---------- cupón ---------- */
function lineaDe(k){const i=+k.slice(1);return k[0]==='T'?T[i]:J[i]}
function cupTxt(k){const x=lineaDe(k);return k[0]==='T'?lbl(x):lblJ(x)}
function renderCup(){const L=CUP.map(lineaDe),n=L.length;const od=L.reduce((a,x)=>a*x.c,1),pj=L.reduce((a,x)=>a*(x.pm==null?1:x.pm),1),stk=LS.get('stk',{v:10000}).v;
 const porP={};L.forEach(x=>porP[x.p]=(porP[x.p]||0)+1);const mismo=Object.entries(porP).filter(([k,v])=>v>1);
 const av=[];if(n&&L.some(x=>x.c<1.35))av.push('Hay patas con cuota < 1,35.');if(n>=3)av.push('3 o más patas: es lotería (stake mínimo).');
 mismo.forEach(([p,v])=>{av.push(`${v} patas de ${sh(P(+p).n)}: la p conjunta real es distinta del producto (las patas del mismo partido se correlacionan).`);if(v>=3){const ok=L.filter(x=>x.p==+p).every(x=>x.c>=1.5)&&L.filter(x=>x.p==+p).reduce((a,x)=>a*x.c,1)>=5;av.push(`Bet Builder de ${sh(P(+p).n)}: ${ok?'cumple':'NO cumple'} la condición de Betano (≥3 patas, cada una ≥1,50 y cuota total ≥5).`)}});
 return`<div class="card"><h2>Cupón (${n} ${n===1?'pata':'patas'})</h2>${n?`<div class="tw"><table class="mini">${L.map((x,i)=>`<tr><td>${esc(sh(P(x.p).n))}</td><td>${esc(CUP[i][0]==='T'?lbl(x):lblJ(x))}</td><td class="n">${f2(x.c)}</td><td class="n">${pct(x.pm)}</td><td><button class="b" data-add="${CUP[i]}">quitar</button></td></tr>`).join('')}</table></div>
 <div class="kp"><div>Cuota total<b>${f2(od)}</b></div><div>p conjunta (producto)<b>${pct(pj)}</b></div><div>EV estimado<b class="${pj*od-1>=0?'ok':'bad'}">${((pj*od-1)*100).toFixed(0)}%</b></div><div>Cuota justa<b>${pj?f2(1/pj):'–'}</b></div></div>
 <label class="stk">Apuesta (COP) <input type="number" step="500" id="stk" value="${stk}"></label> <span id="gan"></span>
 ${av.map(a=>`<div class="warn small">⚠ ${esc(a)}</div>`).join('')}<div class="ac"><button class="b" data-cup="copy">Copiar texto</button><button class="b" data-cup="clr">Vaciar</button></div>`
 :'<p class="mut">Añade líneas desde «Equipos» o «Jugadores». El cupón no apuesta nada: solo arma la cuenta. Quien decide y apuesta eres tú.</p>'}</div>`}
/* ---------- vistas ---------- */
function vAna(){const A=D.A;let h='';
 h+=`<div class="card enf"><h2>Enfoque de mercados</h2>${A.enfoque||'<p class="mut">Sin enfoque.md en esta jornada.</p>'}</div>`;
 h+=(A.rean||[]).map(x=>`<div class="card enf"><details><summary><b>${esc(x.t)}</b></summary>${x.h}</details></div>`).join('');
 h+=vSug();return h}
function vSug(){const S=D.SUG;if(!S.length)return'';window.FS=window.FS||{};const FS=window.FS;const q=(FS.q||'').toLowerCase();
 const rows=S.filter(s=>(!FS.r||(FS.r==='P'?s[7]==='pendiente':s[7]===FS.r))&&(!FS.g||s[1]===FS.g)&&(!q||(s[3]+' '+s[4]).toLowerCase().includes(q)));
 const gr={};S.forEach(s=>{const k=s[1]+' · '+s[2];const x=gr[k]||(gr[k]={n:0,c:0,roi:0});if(s[7]==='cumplió'||s[7]==='falló'){x.n++;if(s[7]==='cumplió'){x.c++;x.roi+=s[5]-1}else x.roi-=1}});
 return`<div class="card"><h2>Mis sugerencias del día y cómo salieron</h2><div class="tw"><table class="mini"><tr><th>Entrega · tipo</th><th class="n">Calificadas</th><th class="n">Se dieron</th><th class="n">%</th><th class="n">1 u plana</th></tr>${Object.entries(gr).map(([k,x])=>`<tr><td>${esc(k)}</td><td class="n">${x.n}</td><td class="n">${x.c}</td><td class="n">${x.n?pct(x.c/x.n):'–'}</td><td class="n ${x.roi>=0?'ok':'bad'}">${x.n?(x.roi>=0?'+':'')+(x.roi/x.n*100).toFixed(0)+'%':'–'}</td></tr>`).join('')}</table></div>
 <div class="filters"><label>Resultado<select data-sf="r"><option value="">todos</option><option value="cumplió" ${FS.r==='cumplió'?'selected':''}>se dieron</option><option value="falló" ${FS.r==='falló'?'selected':''}>fallaron</option><option value="P" ${FS.r==='P'?'selected':''}>pendientes</option></select></label><label>Entrega<select data-sf="g"><option value="">todas</option>${[...new Set(S.map(s=>s[1]))].map(g=>`<option ${FS.g===g?'selected':''}>${esc(g)}</option>`).join('')}</select></label><label>Buscar<input type="search" data-sf="q" value="${esc(FS.q||'')}"></label></div>
 <div class="tw"><table class="mini"><tr><th>Hora</th><th>Tipo</th><th>Sugerencia</th><th>Partido(s)</th><th class="n">Cuota</th><th class="n">p</th><th>Resultado</th><th>Detalle por pata</th></tr>${rows.slice(0,LIM.s).map(s=>`<tr><td>${esc(s[0])}</td><td>${esc(s[2])}</td><td>${esc(s[3])}</td><td>${esc(s[4])}</td><td class="n">${f2(s[5])}</td><td class="n">${pct(s[6])}</td><td><span class="pill ${s[7]==='cumplió'?'ok':s[7]==='falló'?'ko':'mu'}">${esc(s[7])}</span></td><td class="small">${esc(s[8])}</td></tr>`).join('')}</table></div>${rows.length>LIM.s?`<button class="b" data-more="s">ver más</button>`:''}</div>`}
function listaT(rows,sel){const a=rows.slice(0,LIM.t);
 if(V==='A')return`<div class="tw"><table class="tb"><tr><th>Hora</th><th>Partido</th><th>Línea</th><th class="n">Cuota</th><th class="n">p</th><th class="n">EV</th><th class="n">Esp.</th><th class="n">Colch.</th><th>L</th><th>V</th><th>Dir.</th><th>Cumple</th><th>Resultado</th></tr>${a.map(t=>{const r=regT(t,ST.N,ST.K,ST.MN),c=cumT(t);return`<tr data-k="${kT(t)}" class="${SEL.t===t.i?'sel':''}"><td>${esc(P(t.p).hora)}</td><td>${esc(sh(P(t.p).n))}</td><td>${esc(lbl(t))}</td><td class="n">${f2(t.c)}</td><td class="n">${pct(t.pm)}</td><td class="n ${t.ev>0?'ok':''}">${t.ev==null?'–':(t.ev*100).toFixed(0)+'%'}</td><td class="n">${f2(t.e)}</td><td class="n ${t.co>=0?'ok':'bad'}">${sg(t.co)}</td><td>${r.l.n?r.l.c+'/'+r.l.n:'–'}</td><td>${r.v.n?r.v.c+'/'+r.v.n:'–'}</td><td>${r.h.n?r.h.c+'/'+r.h.n:'–'}</td><td>${cumBadge(c)}</td><td>${rsBadge(t)}</td></tr>`}).join('')}</table></div>`;
 if(V==='B'){const g={};a.forEach(t=>(g[t.p]=g[t.p]||[]).push(t));return Object.keys(g).sort((x,y)=>P(x).hora<P(y).hora?-1:P(x).hora>P(y).hora?1:x-y).map(p=>`<details class="mt" ${Object.keys(g).length<=3?'open':''}><summary><b>${esc(P(p).hora)} · ${esc(sh(P(p).n))}</b> ${stBadge(P(p))}<span class="mut"> · ${g[p].length} líneas · ${g[p].filter(t=>cumT(t)===true).length} cumplen</span></summary><div class="cards">${g[p].map(t=>cardT(t,SEL.t===t.i)).join('')}</div></details>`).join('')}
 return`<div class="cards">${a.map(t=>cardT(t,SEL.t===t.i)).join('')}</div>`}
function listaJ(rows){const a=rows.slice(0,LIM.j);
 if(V==='A')return`<div class="tw"><table class="tb"><tr><th>Hora</th><th>Partido</th><th>Jugador y línea</th><th class="n">Cuota</th><th class="n">p</th><th class="n">EV</th><th class="n">Esp.</th><th>Historial</th><th>Resultado</th></tr>${a.map(j=>{const c=cumJ(j);return`<tr data-k="${kJ(j)}" class="${SEL.j===j.i?'sel':''}"><td>${esc(P(j.p).hora)}</td><td>${esc(sh(P(j.p).n))}</td><td>${esc(lblJ(j))}</td><td class="n">${f2(j.c)}</td><td class="n">${pct(j.pm)}</td><td class="n ${j.ev>0?'ok':''}">${j.ev==null?'–':(j.ev*100).toFixed(0)+'%'}</td><td class="n">${j.es==null?'–':f2(j.es)}</td><td>${c?c.c+'/'+c.n+(c.ok?' ✓':''):'no recolectado'}</td><td>${rsBadge(j)}</td></tr>`}).join('')}</table></div>`;
 if(V==='B'){const g={};a.forEach(j=>(g[j.p]=g[j.p]||[]).push(j));return Object.keys(g).sort((x,y)=>P(x).hora<P(y).hora?-1:1).map(p=>`<details class="mt"><summary><b>${esc(P(p).hora)} · ${esc(sh(P(p).n))}</b> ${stBadge(P(p))}<span class="mut"> · ${g[p].length} líneas</span></summary><div class="cards">${g[p].map(j=>cardJ(j,SEL.j===j.i)).join('')}</div></details>`).join('')}
 return`<div class="cards">${a.map(j=>cardJ(j,SEL.j===j.i)).join('')}</div>`}
function vEq(){const{r,base}=filtT(),a=agg(r);
 return{fbar:kbar()+fT(),sum:`<div class="card sumr"><b>${r.length.toLocaleString('es-CO')}</b> ${r.length===1?'línea':'líneas'} (de ${T.length.toLocaleString('es-CO')}) · calificadas: ${aggTxt(a)}</div>${kconteo(base)}`,list:r.length?listaT(r)+(r.length>LIM.t?`<button class="b" data-more="t">Ver más (${LIM.t} de ${r.length})</button>`:''):'<p class="mut">Ninguna línea con estos filtros.</p>',det:SEL.t!=null?detT(T[SEL.t]):'<div class="det mut">Toca una línea para ver sus gráficos: el valor de cada partido de la muestra contra la línea, el esperado y el colchón.</div>'}}
function vJu(){const r=filtJ(),a=agg(r),conH=r.filter(j=>hist(j)).length;
 return{fbar:fJ(),sum:`<div class="card sumr"><b>${r.length.toLocaleString('es-CO')}</b> líneas de jugador (${conH.toLocaleString('es-CO')} con historial) · calificadas (sin nulas): ${aggTxt(a)}<div class="mut small">${D.nota_j}</div></div>`,list:r.length?listaJ(r)+(r.length>LIM.j?`<button class="b" data-more="j">Ver más (${LIM.j} de ${r.length})</button>`:''):'<p class="mut">Ninguna línea con estos filtros.</p>',det:SEL.j!=null?(()=>{const j=J[SEL.j];return`<div class="det">${cardJ(j,true)}</div>`})():'<div class="det mut">Toca una línea para ver el historial por partido del jugador.</div>'}}
function vRe(){const cmin=ST.cmin==null?1.35:ST.cmin,G=T.filter(t=>t.rs&&t.rs!=='N'&&t.c>=cmin);let h='';const B=D.BAL;
 if(B&&B.boletos.length){const real=B.boletos.filter(b=>!b.gratis),ap=real.reduce((a,b)=>a+b.stake,0),co=B.boletos.reduce((a,b)=>a+b.cobrado,0);
  h+=`<div class="card"><h2>Tus apuestas (Betano → Mis apuestas, solo lectura)</h2><div class="kp"><div>Boletos<b>${B.boletos.length}</b></div><div>Apostado<b>${cop(ap)}</b></div><div>Cobrado<b>${cop(co)}</b></div><div>Neto<b class="${co-ap>=0?'ok':'bad'}">${cop(co-ap)}</b></div></div>
  <div class="tw"><table class="mini"><tr><th>#</th><th>Día</th><th>Tipo</th><th class="n">Stake</th><th class="n">Cuota</th><th>Resultado</th><th class="n">Cobrado</th><th>Patas</th><th>Qué pasó</th></tr>${B.boletos.map(b=>`<tr><td>${b.n}</td><td>${esc(b.fecha.slice(5))}</td><td>${esc(b.tipo)}</td><td class="n">${cop(b.stake)}</td><td class="n">${f2(b.cuota)}</td><td><span class="pill ${b.resultado==='Ganada'?'ok':b.resultado==='Perdida'?'ko':'mu'}">${esc(b.resultado)}</span></td><td class="n">${cop(b.cobrado)}</td><td class="small" style="white-space:normal">${(b.pc&&b.pc.patas?b.pc.patas:[]).map(p=>`<span class="pata ${p[1]==='✓'?'ok':p[1]==='✗'?'ko':'mu'}" title="${esc(p[2])}">${esc(p[1])} ${esc(p[0])}</span>`).join(' ')||esc(b.patas)}</td><td class="small" style="white-space:normal">${esc(b.pc?b.pc.falla:'')}</td></tr>`).join('')}</table></div>
  ${(B.pendientes||[]).map(x=>`<div class="warn small">Pendiente: ${esc(x)}</div>`).join('')}</div>`}
 const grp=(titulo,keyf,ord)=>{const m={};G.forEach(t=>{const k=keyf(t);(m[k]=m[k]||[]).push(t)});const ks=Object.keys(m).sort(ord||((a,b)=>m[b].length-m[a].length));
  return`<div class="card"><h2>${titulo}</h2><div class="tw"><table class="mini"><tr><th>Grupo</th><th class="n">Líneas</th><th class="n">Se dieron</th><th class="n">% real</th><th class="n">p mercado</th><th class="n">real − mercado</th><th class="n">1 u plana</th><th>Partidos</th><th></th></tr>${ks.map(k=>{const a=agg(m[k]),d=a.real-a.pk;return`<tr><td>${esc(k)}</td><td class="n">${a.n}</td><td class="n">${a.c}</td><td class="n">${pct(a.real)}</td><td class="n">${pct(a.pk)}</td><td class="n ${d>=0?'ok':'bad'}">${d>=0?'+':''}${(d*100).toFixed(0)} pts</td><td class="n ${a.roi>=0?'ok':'bad'}">${a.roi>=0?'+':''}${(a.roi*100).toFixed(0)}%</td><td class="n">${new Set(m[k].map(t=>t.p)).size}</td><td><span class="bar" style="width:${Math.round(a.real*100)}px"></span><span class="bar2" style="width:${Math.round(a.pk*100)}px"></span></td></tr>`}).join('')}</table></div></div>`};
 h+=`<div class="card"><h2>Criterios: ¿qué separó los aciertos de los fallos?</h2><div class="filters"><label>Solo líneas con cuota ≥<input type="number" step="0.05" data-s="cmin" value="${cmin}"></label></div><div class="small mut">Con la definición actual de «cumple»: al menos ${ST.K} de los últimos ${ST.N} (n mínimo ${ST.MN}, ${({ambos:'ambos equipos',local:'solo local',visitante:'solo visitante',alguno:'cualquiera'})[ST.who]}). Barra verde = % real; barra ámbar = p del mercado (sin margen). Un día, partidos y líneas correlacionadas: pistas, no leyes. ${G.length.toLocaleString('es-CO')} líneas calificadas con cuota ≥ ${cmin}.</div></div>`;
 h+=grp('Cumple contra no cumple',t=>{const c=cumT(t);return c===true?'Cumple':c===false?'No cumple':'Sin muestra'},(a,b)=>a<b?-1:1);
 h+=grp('Por mercado y lado',t=>(MK[t.m]||t.m)+' '+t.s);
 h+=grp('Por colchón (informativo)',t=>t.co==null?'sin colchón':t.co<0?'negativo':t.co<.5?'0 a 0,5':t.co<1?'0,5 a 1':t.co<2?'1 a 2':'más de 2',(a,b)=>a<b?-1:1);
 h+=grp('Por banda de cuota',t=>t.c<1.5?'1,35–1,49':t.c<2?'1,50–1,99':t.c<3?'2,00–2,99':'3,00 o más',(a,b)=>a<b?-1:1);
 h+=grp('Calibración: p del modelo',t=>t.pm==null?'sin p':(Math.floor(t.pm*10)*10)+'–'+(Math.floor(t.pm*10)*10+10)+' %',(a,b)=>a<b?-1:1);
 h+=grp('Por partido',t=>sh(P(t.p).n));
 const GJ=J.filter(j=>j.rs&&j.rs!=='N'&&j.c>=cmin);const m={};GJ.forEach(j=>{const c=cumJ(j),k=(D.MKJ[j.m]||j.m)+' · '+(c?(c.ok?'historial regular':'historial no regular'):'sin historial');(m[k]=m[k]||[]).push(j)});
 h+=`<div class="card"><h2>Jugadores (sin las nulas)</h2><div class="tw"><table class="mini"><tr><th>Grupo</th><th class="n">Líneas</th><th class="n">Se dieron</th><th class="n">% real</th><th class="n">p mercado</th><th class="n">1 u plana</th></tr>${Object.keys(m).sort().map(k=>{const a=agg(m[k]);return`<tr><td>${esc(k)}</td><td class="n">${a.n}</td><td class="n">${a.c}</td><td class="n">${pct(a.real)}</td><td class="n">${pct(a.pk)}</td><td class="n ${a.roi>=0?'ok':'bad'}">${a.roi>=0?'+':''}${(a.roi*100).toFixed(0)}%</td></tr>`}).join('')}</table></div></div>`;
 return h}
function vDa(){return`<div class="card"><h2>Datos y límites</h2><pre>${esc(D.estado)}</pre></div><div class="card"><h2>Esta versión</h2><ul><li>${esc(D.generado)}</li><li>Muestra recolectada: ${D.N} partidos por equipo y hasta ${D.NH} directos. Con 10 partidos el «cumple» por defecto pasa a 7 de 10.</li><li>Series por partido con valores de Flashscore (córners, remates, tiros al arco, faltas, fueras, saques, tarjetas en puntos y goles; el primer tiempo cuando Flashscore lo trae).</li><li>Las líneas de 2.º tiempo se calculan como partido completo − primer tiempo.</li><li>Colchón = esperado − línea (Más) o línea − esperado (Menos): informativo, no oculta ninguna línea.</li><li>Solo lectura: no apuesta ni lee la red. Quien decide y apuesta eres tú.</li></ul></div>`}
/* ---------- armado de la página ---------- */
const TABS=[['ana','Análisis'],['eq','Equipos'],['ju','Jugadores'],['re','Resultados'],['cu','Cupón'],['da','Datos y límites']];
let CURV=null;
function paintNav(){$('#nav').innerHTML=TABS.map(([k,t])=>`<button class="${TAB===k?'on':''}" data-tab="${k}">${t}${k==='cu'&&CUP.length?' ('+CUP.length+')':''}</button>`).join('')}
function shell(v){ // v = {fbar,sum,list,det}
 if(V==='A')return`<div class="wrapA"><aside class="side" id="fbar">${v.fbar}</aside><main><div id="sum">${v.sum}</div><div id="lst">${v.list}</div></main><aside class="dpane" id="det">${v.det}</aside></div>`;
 if(V==='B')return`<div class="topb" id="fbar">${v.fbar}</div><div id="sum">${v.sum}</div><div id="lst">${v.list}</div>`;
 return`<div class="wrapC"><div><details class="fdet" open><summary>Filtros</summary><div id="fbar">${v.fbar}</div></details><div id="sum">${v.sum}</div><div id="lst">${v.list}</div></div><aside class="tk" id="tk">${renderCup()}</aside></div>`}
function draw(){paintNav();let h='',v=null;const y=window.scrollY;
 if(TAB==='eq'){v=vEq();h=shell(v)}else if(TAB==='ju'){v=vJu();h=shell(v)}else if(TAB==='ana')h=vAna();else if(TAB==='re')h=vRe();else if(TAB==='cu')h=renderCup();else h=vDa();
 $('#app').innerHTML=h;$('#badge').textContent=CUP.length?`Cupón: ${CUP.length} · ${f2(CUP.reduce((a,k)=>a*lineaDe(k).c,1))}`:'';$('#badge').hidden=!CUP.length;ganancia();window.scrollTo(0,y)}
function repaintList(){ // repinta solo resumen, lista y detalle (los filtros conservan el foco)
 if(TAB!=='eq'&&TAB!=='ju'){draw();return}const v=TAB==='eq'?vEq():vJu();const s=$('#sum'),l=$('#lst'),d=$('#det');if(!s||!l){draw();return}s.innerHTML=v.sum;l.innerHTML=v.list;if(d)d.innerHTML=v.det;const t=$('#tk');if(t)t.innerHTML=renderCup();paintNav();$('#badge').textContent=CUP.length?`Cupón: ${CUP.length} · ${f2(CUP.reduce((a,k)=>a*lineaDe(k).c,1))}`:'';$('#badge').hidden=!CUP.length;ganancia()}
function ganancia(){const g=$('#gan'),s=$('#stk');if(!g||!s)return;const od=CUP.map(lineaDe).reduce((a,x)=>a*x.c,1);g.innerHTML=`Devolvería <b>${cop(+s.value*od)}</b> (ganancia ${cop(+s.value*(od-1))})`}
function toggleCup(k){const i=CUP.indexOf(k);if(i>=0)CUP.splice(i,1);else CUP.push(k);save()}
document.addEventListener('click',e=>{const el=e.target.closest('[data-tab],[data-add],[data-det],[data-atj],[data-clr],[data-more],[data-cup],tr[data-k]');if(!el)return;const d=el.dataset;
 if(d.tab){TAB=d.tab;save();draw();window.scrollTo(0,0);return}
 if(d.add){toggleCup(d.add);if(TAB==='cu')draw();else repaintList();return}
 if(d.det||(el.tagName==='TR'&&d.k)){const k=d.det||d.k,i=+k.slice(1),o=k[0]==='T'?'t':'j';SEL[o]=SEL[o]===i&&d.det?null:i;repaintList();return}
 if(d.atj){const[k,n]=d.atj.split(',').map(Number);ST.N=n;ST.K=k;ST.MN=clamp(ST.MN,1,n);save();draw();return}
 if(d.clr){if(d.clr==='t')FT={};else FJ={};save();draw();return}
 if(d.more){LIM[d.more]+=150;if(d.more==='s')draw();else repaintList();return}
 if(d.cup==='clr'){CUP=[];save();draw();return}
 if(d.cup==='copy'){const L=CUP.map(lineaDe),od=L.reduce((a,x)=>a*x.c,1);const tx=L.map((x,i)=>sh(P(x.p).n)+' · '+cupTxt(CUP[i])+' @'+f2(x.c)).join('\n')+'\nCuota total '+f2(od);try{navigator.clipboard.writeText(tx)}catch(er){}return}});
function onIn(e){const el=e.target,d=el.dataset;
 if(d.f!=null){const F=TAB==='ju'?FJ:FT;let v=el.value;F[d.f]=v===''?'':(el.type==='number'?+v:v);save();LIM.t=LIM.j=120;repaintList();return}
 if(d.s!=null){const k=d.s;if(k==='cmin'&&e.type==='input')return;ST[k]=(el.type==='number')?+el.value:el.value;if(k==='N'){ST.N=clamp(ST.N,1,D.N);ST.K=clamp(ST.K,1,ST.N);ST.MN=clamp(ST.MN,1,ST.N)}if(k==='K')ST.K=clamp(ST.K,1,ST.N);if(k==='MN')ST.MN=clamp(ST.MN,1,ST.N);save();
  if(e.type==='change'||k==='who'||k==='cmin')draw();else repaintList();return}
 if(d.sf!=null){if(e.type==='input')return;window.FS=window.FS||{};window.FS[d.sf]=el.value;draw();return}
 if(el.id==='stk'){LS.set('stk',{v:+el.value});ganancia()}}
document.addEventListener('input',e=>{if(e.target.matches('input[data-f],input[data-s]'))onIn(e);if(e.target.id==='stk')onIn(e)});
document.addEventListener('change',e=>{if(e.target.matches('select,input[data-s],input[data-f],input[data-sf]'))onIn(e);if(e.target.id==='stk')onIn(e)});
$('#titulo').textContent=D.titulo;$('#sub').textContent=D.sub;
if(!TABS.some(t=>t[0]===TAB))TAB='ana';
draw();
