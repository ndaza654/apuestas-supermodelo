'use strict';
/* ===== Biblioteca común: datos, estado, estadística y gráficos (solo lectura, sin red, sin librerías) ===== */
const DB=/*DATA*/;
const $=(s,e)=>(e||document).querySelector(s),$$=(s,e)=>[...(e||document).querySelectorAll(s)];
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const nz=s=>String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
const pct=(x,d)=>x==null||isNaN(x)?'–':(100*x).toFixed(d||0)+'%',f1=x=>x==null||isNaN(x)?'–':(+x).toFixed(1),f2=x=>x==null||isNaN(x)?'–':(+x).toFixed(2),f3=x=>x==null||isNaN(x)?'–':(+x).toFixed(3);
const sg=x=>x==null||isNaN(x)?'–':(x>0?'+':'')+(+x).toFixed(2),spct=x=>x==null||isNaN(x)?'–':(x>0?'+':'')+(100*x).toFixed(0)+'%';
const cop=n=>(n<0?'-$':'$')+Math.abs(Math.round(n)).toLocaleString('es-CO');
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),sh=n=>String(n).replace(' - ',' – ');
const LSget=(k,d)=>{try{const v=localStorage.getItem('dbx.'+CFG.id+'.'+k);return v?Object.assign({},d,JSON.parse(v)):Object.assign({},d)}catch(e){return Object.assign({},d)}};
const LSset=(k,v)=>{try{localStorage.setItem('dbx.'+CFG.id+'.'+k,JSON.stringify(v))}catch(e){}};
const MK={corners:'Córners',goles:'Goles',tarjetas:'Tarjetas (pts)',remates:'Remates',al_arco:'Tiros al arco',faltas:'Faltas',fueras:'Fueras de juego',saques_banda:'Saques de banda',saques_meta:'Saques de meta'};
const MKJ={remates:'Remates',al_arco:'Tiros al arco',faltas:'Faltas cometidas',entradas:'Entradas',anota:'Anota',asiste:'Asiste',anota_o_asiste:'Anota o asiste',tarjeta:'Tarjeta',atajadas:'Atajadas'};
const AM={total:'total',local:'local',visitante:'visitante','1T':'1.er tiempo','2T':'2.º tiempo'};
const RSN={C:['se dio','ok'],F:['falló','ko'],MG:['media ganada','ok'],MP:['media perdida','ko'],N:['nula (no jugó)','mu']};
/* ---- tablas ---- */
const P=DB.P;
const T=DB.L.map((r,i)=>({i,t:'T',p:r[0],m:r[1],a:r[2],s:r[3],l:r[4],c:r[5],e:r[6],co:r[7],pm:r[8],pk:r[9],ev:r[10],rs:r[11],rv:r[12],stk:r[13],cc:r[14],cf:r[15],al:r[16],lei:r[17]}));
const G=DB.J.map((r,i)=>({i,t:'G',p:r[0],m:r[1],j:r[2],side:r[3],ti:r[4],l:r[5],s:r[6],c:r[7],pm:r[8],pk:r[9],ev:r[10],e:r[11],co:r[12],rs:r[13],rv:r[14],stk:r[15],nt:r[16]}));
const BOL=DB.B.map(r=>({n:r[0],fecha:r[1],hora:r[2],tipo:r[3],stake:r[4],gratis:r[5],cuota:r[6],res:r[7],cob:r[8],partidos:r[9],patas:r[10],pc:r[11]}));
const SUG=DB.S.map(r=>({id:r[0],fecha:r[1],hora:r[2],ent:r[3],tipo:r[4],nombre:r[5],partidos:r[6],patas:r[7],c:r[8],p:r[9],res:r[10],det:r[11],fam:r[12],fuente:r[13],pj:r[14]}));
const DOCS=DB.docs.map((r,i)=>({i,rel:r[0],t:r[1],tipo:r[2],jor:r[3],txt:r[4]}));
const lineaDe=k=>k[0]==='T'?T[+k.slice(1)]:G[+k.slice(1)];
/* ---- estado persistente ---- */
const ST=LSget('st',{K:DB.K,N:DB.N,MN:DB.MN,who:'ambos'});ST.N=clamp(+ST.N||DB.N,1,DB.N);ST.K=clamp(+ST.K||DB.K,1,ST.N);ST.MN=clamp(+ST.MN||DB.MN,1,ST.N);
const S={};const pgState=(k,d)=>{S[k]=LSget('pg.'+k,d);return S[k]};const saveS=k=>LSset('pg.'+k,S[k]);
let CUP=LSget('cup',{x:[]}).x||[];const saveCup=()=>LSset('cup',{x:CUP});
const inCup=k=>CUP.includes(k);
/* ---- regularidad «X de N» (se recalcula con las series por partido) ---- */
const hit=(v,l,s)=>{const q=Math.round(l*4)%2===1;return s==='Menos'?v<(q?l-.25:l):v>(q?l+.25:l)};
const vcache=new Map();
function vals(t){if(vcache.has(t.i))return vcache.get(t.i);const Sx=(DB.SER[t.p]||{})[t.m],M=DB.META[t.p]||{},o={l:[],v:[],h:[]};
 if(Sx)for(const side of['l','v','h'])(Sx[side]||[]).forEach((x,k)=>{const a=x[0],b=x[1],a1=x[2],b1=x[3];let v=null;
  if(a==null||b==null)v=null;else if(t.a==='total')v=a+b;else if(t.a==='local')v=side==='v'?b:a;else if(t.a==='visitante')v=side==='v'?a:b;else if(t.a==='1T')v=a1==null?null:a1+b1;else if(t.a==='2T')v=a1==null?null:(a+b)-(a1+b1);
  if(v!=null)o[side].push({v,m:(M[side]||[])[k]})});
 vcache.set(t.i,o);return o}
function regT(t,n,K,MN){const V=vals(t),f=a=>{const w=a.slice(0,n),c=w.filter(x=>hit(x.v,t.l,t.s)).length;return{c,n:w.length,ok:w.length>=MN&&c>=K}};return{l:f(V.l),v:f(V.v),h:f(V.h)}}
function cumT(t,n,K,MN,who){n=n==null?ST.N:n;K=K==null?ST.K:K;MN=MN==null?ST.MN:MN;who=who||ST.who;const r=regT(t,n,K,MN);if(!r.l.n||!r.v.n)return t.cf==null?null:t.cf===1;
 return who==='local'?r.l.ok:who==='visitante'?r.v.ok:who==='alguno'?(r.l.ok||r.v.ok):(r.l.ok&&r.v.ok)}
const HI=(j,m)=>{const h=j;return m==='remates'?h[2]:m==='al_arco'?h[3]:m==='faltas'?h[8]:m==='entradas'?h[9]:m==='atajadas'?(h[10]==null?null:h[10]):m==='anota'?(h[4]>=1?1:0):m==='asiste'?(h[5]>=1?1:0):m==='anota_o_asiste'?((h[4]+h[5])>=1?1:0):m==='tarjeta'?((h[6]+h[7])>=1?1:0):null};
const hist=g=>(DB.HIS[g.p]||{})[g.j]||null;
function pvals(g){const H=hist(g);if(!H)return null;return H.filter(x=>x[1]>0).map(x=>({v:HI(x,g.m),m:x})).filter(x=>x.v!=null)}
function cumG(g,n,K,MN){n=n==null?(S.jug?S.jug.Nj:10):n;K=K==null?(S.jug?S.jug.Kj:7):K;MN=MN==null?(S.jug?S.jug.MNj:7):MN;const a=pvals(g);if(!a)return null;const w=a.slice(0,n),c=w.filter(x=>x.v>=g.l).length;return{c,n:w.length,ok:w.length>=MN&&c>=K}}
/* ---- estadística ---- */
const isG=x=>x.rs==='C'||x.rs==='F'||x.rs==='MG'||x.rs==='MP';
const retOf=x=>x.rs==='C'?x.c-1:x.rs==='F'?-1:x.rs==='MG'?(x.c-1)/2:x.rs==='MP'?-.5:null;
const wilson=(c,n,z)=>{z=z||1.96;if(!n)return[null,null];const p=c/n,d=1+z*z/n,m=(p+z*z/(2*n))/d,h=z*Math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d;return[m-h,m+h]};
function agg(rows){let n=0,h=0,ps=0,pk=0,pn=0,u=0,kn=0;const byP={};for(const x of rows){if(!isG(x))continue;n++;if(x.rs==='C'||x.rs==='MG')h++;if(x.pm!=null){ps+=x.pm;pn++}if(x.pk!=null){pk+=x.pk;kn++}const r=retOf(x);u+=r;(byP[x.p]=byP[x.p]||[]).push(r)}
 const[lo,hi]=wilson(h,n);return{n,h,real:n?h/n:null,p:pn?ps/pn:null,pk:kn?pk/kn:null,roi:n?u/n:null,u,lo,hi,byP,np:Object.keys(byP).length}}
const mulberry=a=>()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296};
function bootRoi(byP,B){B=B||400;const g=Object.values(byP);if(g.length<3)return[null,null];const rnd=mulberry(7),out=[];for(let b=0;b<B;b++){let s=0,m=0;for(let k=0;k<g.length;k++){const x=g[(rnd()*g.length)|0];m+=x.length;for(let q=0;q<x.length;q++)s+=x[q]}out.push(s/m)}out.sort((a,b)=>a-b);return[out[(B*.025)|0],out[(B*.975)|0]]}
function scores(rows){let n=0,bm=0,bk=0,lm=0,lk=0;for(const x of rows){if(!(x.rs==='C'||x.rs==='F')||x.pm==null||x.pk==null)continue;const y=x.rs==='C'?1:0,e=1e-4,pm=clamp(x.pm,e,1-e),pk=clamp(x.pk,e,1-e);n++;bm+=(pm-y)**2;bk+=(pk-y)**2;lm+=-(y?Math.log(pm):Math.log(1-pm));lk+=-(y?Math.log(pk):Math.log(1-pk))}return{n,bm:bm/n,bk:bk/n,lm:lm/n,lk:lk/n}}
function calib(rows,key,nb){nb=nb||10;const bins=Array.from({length:nb},()=>({n:0,c:0,ps:0}));for(const x of rows){if(!(x.rs==='C'||x.rs==='F')||x[key]==null)continue;const b=bins[Math.min(nb-1,Math.floor(x[key]*nb))];b.n++;b.c+=x.rs==='C'?1:0;b.ps+=x[key]}return bins.map((b,i)=>{const[lo,hi]=wilson(b.c,b.n);return{i,n:b.n,c:b.c,p:b.n?b.ps/b.n:(i+.5)/nb,y:b.n?b.c/b.n:null,lo,hi}})}
/* ---- gráficos SVG ---- */
function bars(arr,l,s,n,o){o=o||{};const w=o.w||230,h=o.h||74,pad=15;if(!arr.length)return`<div class="nod" style="width:${w}px;height:${h}px">sin muestra</div>`;
 const a=arr.map((x,k)=>({...x,k})).reverse(),mx=Math.max(l*1.3,...a.map(x=>x.v),1),bw=Math.min(24,(w-10)/a.length-3),H=h-pad-11,y=v=>pad+H-(v/mx)*H;let g='';
 a.forEach((x,i)=>{const X=6+i*(bw+3),ok=s==='J'?x.v>=l:hit(x.v,l,s),fuera=x.k>=n,yy=y(x.v),m=x.m||[];
  const tip=o.player?`${m[0]||''} · ${m[1]||''}′ · ${x.v}`:`${m[0]||''} ${m[1]||''}${m[2]?' ('+m[2]+')':''} ${m[3]!=null?m[3]+'-'+m[4]+' ·':''} ${x.v}`;
  g+=`<g opacity="${fuera?.35:1}"><title>${esc(tip)}</title><rect x="${X}" y="${yy}" width="${bw}" height="${Math.max(1,pad+H-yy)}" rx="2" class="${ok?'bo':'bk'}"/><text x="${X+bw/2}" y="${yy-2}" text-anchor="middle" class="bt">${x.v%1?f1(x.v):x.v}</text></g>`});
 const yl=y(l);g+=`<line x1="2" x2="${w-2}" y1="${yl}" y2="${yl}" class="bl"/><text x="${w-3}" y="${yl-2}" text-anchor="end" class="bl2">${l}</text>`;
 return`<svg class="bars" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img">${g}</svg>`}
function gauge(t){if(t.e==null)return'<div class="mut small">esperado: sin dato</div>';const lo=Math.min(t.l,t.e)*.7,hi=Math.max(t.l,t.e)*1.3||1,X=v=>6+(v-lo)/(hi-lo)*188,good=t.s==='Menos'?t.e<t.l:t.e>t.l;
 return`<svg viewBox="0 0 200 36" width="200" height="36" class="gauge"><rect x="6" y="14" width="188" height="6" rx="3" class="gb"/><rect x="${Math.min(X(t.l),X(t.e))}" y="14" width="${Math.abs(X(t.e)-X(t.l))}" height="6" class="${good?'gg':'gr'}"/><line x1="${X(t.l)}" x2="${X(t.l)}" y1="8" y2="26" class="bl"/><text x="${X(t.l)}" y="6" text-anchor="middle" class="bt">línea ${t.l}</text><circle cx="${X(t.e)}" cy="17" r="5" class="gd"/><text x="${X(t.e)}" y="34" text-anchor="middle" class="bt">esperado ${f2(t.e)}</text></svg>`}
function lineChart(series,o){o=o||{};const w=o.w||640,h=o.h||220,L=44,R=10,Tp=12,Bt=24;const all=series.flatMap(s=>s.y.filter(v=>v!=null));if(!all.length)return'<div class="nod" style="height:80px">sin datos</div>';
 let mn=Math.min(...all,o.zero===false?Infinity:0),mx=Math.max(...all,o.zero===false?-Infinity:0);if(mn===mx){mn-=1;mx+=1}const nmax=Math.max(...series.map(s=>s.y.length)),X=i=>L+(nmax<2?0:i/(nmax-1)*(w-L-R)),Y=v=>Tp+(1-(v-mn)/(mx-mn))*(h-Tp-Bt);
 let g='';for(let k=0;k<=4;k++){const v=mn+(mx-mn)*k/4;g+=`<line x1="${L}" x2="${w-R}" y1="${Y(v)}" y2="${Y(v)}" class="gl"/><text x="${L-4}" y="${Y(v)+3}" text-anchor="end" class="bt">${o.fmt?o.fmt(v):v.toFixed(1)}</text>`}
 if(mn<0&&mx>0)g+=`<line x1="${L}" x2="${w-R}" y1="${Y(0)}" y2="${Y(0)}" class="bl"/>`;
 series.forEach((s,k)=>{const pts=s.y.map((v,i)=>v==null?null:[X(i),Y(v)]).filter(Boolean);if(!pts.length)return;g+=`<polyline points="${pts.map(p=>p.map(x=>x.toFixed(1)).join(',')).join(' ')}" class="ln l${k%5}" fill="none"/>`});
 if(o.labels)o.labels.forEach((t,i)=>{if(t&&i%Math.max(1,Math.ceil(nmax/8))===0)g+=`<text x="${X(i)}" y="${h-8}" text-anchor="middle" class="bt">${esc(t)}</text>`});
 return`<svg class="lc" viewBox="0 0 ${w} ${h}" width="100%" style="max-width:${w}px" role="img">${g}</svg>${series.length>1?`<div class="lg">${series.map((s,k)=>`<span><i class="lk l${k%5}"></i>${esc(s.name)}</span>`).join('')}</div>`:''}`}
function calibChart(bins,o){o=o||{};const w=360,h=300,L=36,B=28,Tp=10,R=10,X=v=>L+v*(w-L-R),Y=v=>Tp+(1-v)*(h-Tp-B);let g='';
 for(let k=0;k<=5;k++){const v=k/5;g+=`<line x1="${L}" x2="${w-R}" y1="${Y(v)}" y2="${Y(v)}" class="gl"/><text x="${L-4}" y="${Y(v)+3}" text-anchor="end" class="bt">${Math.round(v*100)}</text><text x="${X(v)}" y="${h-12}" text-anchor="middle" class="bt">${Math.round(v*100)}</text>`}
 g+=`<line x1="${X(0)}" y1="${Y(0)}" x2="${X(1)}" y2="${Y(1)}" class="bl"/>`;
 bins.forEach(b=>{if(!b.n)return;const r=Math.max(3,Math.min(10,Math.sqrt(b.n)/2.2));g+=`<line x1="${X(b.p)}" x2="${X(b.p)}" y1="${Y(b.lo)}" y2="${Y(b.hi)}" class="wh"/><circle cx="${X(b.p)}" cy="${Y(b.y)}" r="${r}" class="${o.cls||'gd'}"><title>p ${pct(b.p)} · real ${pct(b.y)} · n ${b.n}</title></circle>`});
 return`<svg viewBox="0 0 ${w} ${h}" width="100%" style="max-width:${w}px" role="img">${g}<text x="${w/2}" y="${h-1}" text-anchor="middle" class="bt">probabilidad dicha (%)</text></svg>`}
const hbar=(v,mx,cls)=>`<span class="hb"><i class="${cls||''}" style="width:${clamp(mx?100*v/mx:0,0,100)}%"></i></span>`;
/* ---- piezas de interfaz ---- */
const pill=(t,c)=>`<span class="pill ${c||''}">${esc(t)}</span>`;
const stBadge=p=>p.est==='final'?`<span class="pill fin">final${p.g?` ${p.g[0]}-${p.g[1]}`:''}</span>`:p.est==='vivo'?`<span class="pill liv">en juego ${p.g?p.g[0]+'-'+p.g[1]:''}${p.min?' · '+esc(p.min):''}</span>`:'<span class="pill">por jugar</span>';
const rsBadge=x=>{if(x.rs&&RSN[x.rs])return`<span class="pill ${RSN[x.rs][1]}">${RSN[x.rs][0]}${x.rv!=null?' · real '+x.rv:''}</span>`;const p=P[x.p];return p.est==='final'?'<span class="pill mu">sin calificar</span>':p.est==='vivo'?'<span class="pill liv">en juego</span>':''};
const cumBadge=c=>c===true?'<span class="pill ok">cumple</span>':c===false?'<span class="pill no">no cumple</span>':'<span class="pill mu">sin muestra</span>';
const lbl=t=>`${MK[t.m]||t.m}${t.a==='total'?'':' · '+AM[t.a]} ${t.s} ${t.l}`;
const lblG=g=>`${g.j} · ${MKJ[g.m]||g.m} ${g.s==='Sí'?'sí':g.l+' o más'}`;
const lblX=x=>x.t==='T'?lbl(x):lblG(x);
const kOf=x=>x.t+x.i;
const chip=(r,txt)=>r.n?`<span class="xn ${r.ok?'y':''}">${txt} ${r.c}/${r.n}</span>`:`<span class="xn">${txt} –</span>`;
const jornadaTxt=j=>{const d=new Date(j.slice(0,10)+'T12:00:00');const s=d.toLocaleDateString('es-CO',{weekday:'short',day:'numeric',month:'short'});return s+(j.length>10?' (noche)':'')};
function aggRow(nombre,a,extra){const d=a.real!=null&&a.pk!=null?a.real-a.pk:null;return`<tr><td>${nombre}</td><td class="n">${a.n}</td><td class="n">${a.h}</td><td class="n">${pct(a.real)}</td><td class="n mut">${pct(a.lo)}–${pct(a.hi)}</td><td class="n">${pct(a.pk)}</td><td class="n ${d==null?'':d>=0?'ok':'bad'}">${d==null?'–':(d>=0?'+':'')+(d*100).toFixed(0)+' pts'}</td><td class="n ${a.roi==null?'':a.roi>=0?'ok':'bad'}">${spct(a.roi)}</td><td class="n mut">${a.np}</td>${extra||''}</tr>`}
const AGGH='<tr><th>Grupo</th><th class="n">Líneas</th><th class="n">Se dieron</th><th class="n">% real</th><th class="n">Intervalo 95 %</th><th class="n">p mercado</th><th class="n">real − mercado</th><th class="n">1 u plana</th><th class="n">Partidos</th></tr>';
function groupTable(rows,keyf,o){o=o||{};const m={};rows.forEach(x=>{if(!isG(x))return;const k=keyf(x);if(k==null)return;(m[k]=m[k]||[]).push(x)});const ks=Object.keys(m).sort(o.ord||((a,b)=>m[b].length-m[a].length));
 return`<div class="tw"><table class="mini">${AGGH}${ks.map(k=>aggRow(esc(k),agg(m[k]))).join('')||'<tr><td colspan="9" class="mut">sin líneas calificadas</td></tr>'}</table></div>`}
const downloadCSV=(name,rows)=>{const t=rows.map(r=>r.map(c=>{c=String(c==null?'':c);return /[;"\n]/.test(c)?'"'+c.replace(/"/g,'""')+'"':c}).join(';')).join('\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['﻿'+t],{type:'text/csv'}));a.download=name;a.click()};
/* ---- Markdown mínimo para la biblioteca ---- */
function md(t){const lines=t.split('\n');let o=[],li=false,tb=[],code=false;const inl=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<span class="lnk">$1</span>');
 const ct=()=>{if(tb.length){const rows=tb.map(r=>r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim())).filter(r=>!r.every(c=>/^:?-{2,}:?$/.test(c)));if(rows.length)o.push('<div class="tw"><table class="mini"><tr>'+rows[0].map(c=>`<th>${inl(c)}</th>`).join('')+'</tr>'+rows.slice(1).map(r=>'<tr>'+r.map(c=>`<td style="white-space:normal">${inl(c)}</td>`).join('')+'</tr>').join('')+'</table></div>');tb=[]}};
 for(const ln of lines){if(ln.startsWith('```')){ct();if(li){o.push('</ul>');li=false}code=!code;o.push(code?'<pre>':'</pre>');continue}if(code){o.push(esc(ln)+'\n');continue}
  if(ln.startsWith('|')){if(li){o.push('</ul>');li=false}tb.push(ln);continue}ct();const m=ln.match(/^(#{1,4})\s+(.*)/);
  if(m){if(li){o.push('</ul>');li=false}o.push(`<h${m[1].length+1}>${inl(m[2])}</h${m[1].length+1}>`);continue}
  if(/^\s*[-*]\s+/.test(ln)){if(!li){o.push('<ul>');li=true}o.push('<li>'+inl(ln.replace(/^\s*[-*]\s+/,''))+'</li>');continue}
  if(/^\s*\d+\.\s+/.test(ln)){if(!li){o.push('<ul>');li=true}o.push('<li>'+inl(ln.replace(/^\s*\d+\.\s+/,''))+'</li>');continue}
  if(li){o.push('</ul>');li=false}if(ln.trim())o.push('<p>'+inl(ln)+'</p>')}ct();if(li)o.push('</ul>');return o.join('')}
