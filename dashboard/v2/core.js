'use strict';
/* ===== datos y estado ===== */
const DB=JSON.parse(document.getElementById('db').textContent);
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const MK={corners:'Córners',goles:'Goles',tarjetas:'Tarjetas',remates:'Remates',al_arco:'Tiros al arco',faltas:'Faltas',fueras:'Fueras de juego',saques_banda:'Saques de banda',saques_meta:'Saques de meta'};
const JM={remates:'Remates',al_arco:'Tiros al arco',faltas:'Faltas cometidas',entradas:'Entradas',atajadas:'Atajadas',anota:'Anota',asiste:'Asiste',anota_o_asiste:'Anota o asiste',tarjeta:'Recibe tarjeta'};
const AMB={total:'Partido',local:'Local',visitante:'Visitante','1T':'1er tiempo','2T':'2º tiempo'};
const P=DB.P;P.forEach((p,i)=>{p.i=i;p.hh=p.hora.slice(11,16);p.an=DB.AN[i]||null;p.xi=DB.XI[i]||null});
const keyOf=x=>[P[x.p].jor,P[x.p].n,x.m,x.k==='G'?x.sd:x.a,x.j||'',x.s,x.l].join('|');
const T=DB.L.map(r=>({k:'T',p:r[0],m:r[1],a:r[2],s:r[3],l:r[4],c:r[5],e:r[6],col:r[7],pm:r[8],pk:r[9],ev:r[10],rs:r[11],real:r[12],cf:r[15],al:r[16]}));
const G=DB.J.map(r=>({k:'G',p:r[0],m:r[1],j:r[2],sd:r[3],tit:r[4],l:r[5],s:r[6],c:r[7],pm:r[8],pk:r[9],ev:r[10],e:r[11],col:r[12],rs:r[13],real:r[14],cft:r[16]}));
const ALL=T.concat(G),BYKEY=new Map();ALL.forEach(x=>{x.key=keyOf(x);BYKEY.set(x.key,x)});
const JORS=DB.jors.slice();
const jorLab=j=>{const d=new Date(j.slice(0,10)+'T12:00:00');return['dom','lun','mar','mié','jue','vie','sáb'][d.getDay()]+' '+d.getDate()+'-'+['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'][d.getMonth()]+(j.length>10?' ('+j.slice(11)+')':'')};
const jorLong=j=>{const d=new Date(j.slice(0,10)+'T12:00:00');return['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'][d.getDay()]+' '+d.getDate()+' de '+['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'][d.getMonth()]+(j.length>10?' ('+j.slice(11)+')':'')};
const bog=s=>{const d=new Date(String(s).slice(0,16).replace(' ','T')+':00Z');if(isNaN(d))return s;d.setUTCHours(d.getUTCHours()-5);return d.getUTCDate()+'-'+['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'][d.getUTCMonth()]+' '+d.toISOString().slice(11,16)+' (Bogotá)'};
const DEF={jor:(JORS.filter(j=>P.some(p=>p.jor===j&&p.est==='pend')).pop())||JORS[JORS.length-1],
 strat:{cmin:1.4,cmax:2.2,K:7,minN:7,who:'ambos',col:0,pmin:0,mks:[],lado:'',tipo:'todo',tit:true,uno:true,h2h:false},
 sede:'todos',cup:[],saved:[],bets:[],target:3,stake:7400,presets:{},tab:{},f:{ac0:1.4,ac1:2.2,lc0:1,lc1:50,jc0:1.3,jc1:3}};
let ST=JSON.parse(JSON.stringify(DEF));
try{const s=JSON.parse(localStorage.getItem('mando2')||'null');if(s){ST=Object.assign(ST,s);ST.strat=Object.assign({},DEF.strat,s.strat||{});ST.f=Object.assign({},DEF.f,s.f||{});if(!JORS.includes(ST.jor))ST.jor=DEF.jor}}catch(e){}
/* ST.strat = «tu estrategia» (la que leen Inicio, Partidos, Cupón, Líneas, Jugadores, Histórico…). ST.est = filtro de trabajo de la pestaña Mi estrategia: se mueve ahí y NO cambia las demás pestañas. */
const ensureEst=()=>{ST.est=Object.assign({},DEF.strat,ST.est||ST.strat)};ensureEst();
const sActiva=()=>location.hash.indexOf('#/estrategia')===0?ST.est:ST.strat;
const save=()=>{try{localStorage.setItem('mando2',JSON.stringify(ST))}catch(e){}};
/* ===== formato ===== */
const f2=v=>v==null?'–':v.toFixed(2).replace('.',','),f1=v=>v==null?'–':(Math.round(v*10)/10).toString().replace('.',',');
const pc=(v,d=0)=>v==null||isNaN(v)?'–':(v*100).toFixed(d).replace('.',',')+' %';
const sg=v=>v==null||isNaN(v)?'–':(v>0?'+':'')+(v*100).toFixed(1).replace('.',',')+' %';
const cop=v=>'$'+Math.round(v).toLocaleString('es-CO');
const eqName=(x)=>x.a==='local'?P[x.p].loc:x.a==='visitante'?P[x.p].vis:x.a==='1T'?'1er tiempo':x.a==='2T'?'2º tiempo':'';
const tx=x=>x.k==='G'?`${x.j} · ${JM[x.m]||x.m}${x.s==='Sí'?'':' '+x.l+'+'}`:`${MK[x.m]||x.m}${eqName(x)?' '+eqName(x):''} ${x.s} ${String(x.l).replace('.',',')}`;
const prob=x=>x.pm!=null?x.pm:(x.c?1/x.c/1.06:null);
/* ===== series por partido y regularidad ===== */
const hit=(v,l,s)=>s==='Más'?v>l:v<l,hitG=(v,l)=>v>=l;
const vc=new Map();
function valsT(t){if(vc.has(t.key))return vc.get(t.key);const Sx=(DB.SER[t.p]||{})[t.m],M=DB.META[t.p]||{},o={l:[],v:[],h:[]};
 if(Sx)for(const sd of['l','v','h'])(Sx[sd]||[]).forEach((x,k)=>{const a=x[0],b=x[1],a1=x[2],b1=x[3];let v=null;
  if(a==null||b==null)v=null;else if(t.a==='total')v=a+b;else if(t.a==='local')v=sd==='v'?b:a;else if(t.a==='visitante')v=sd==='v'?a:b;else if(t.a==='1T')v=a1==null?null:a1+b1;else if(t.a==='2T')v=a1==null?null:(a+b)-(a1+b1);
  if(v!=null)o[sd].push({v,m:(M[sd]||[])[k]||[]})});
 vc.set(t.key,o);return o}
const HI=(h,m)=>m==='remates'?h[2]:m==='al_arco'?h[3]:m==='faltas'?h[8]:m==='entradas'?h[9]:m==='atajadas'?h[10]:m==='anota'?(h[4]>=1?1:0):m==='asiste'?(h[5]>=1?1:0):m==='anota_o_asiste'?(h[4]+h[5]>=1?1:0):m==='tarjeta'?(h[6]+h[7]>=1?1:0):null;
const histOf=(p,j)=>(DB.HIS[p]||{})[j]||null;
function valsG(g){const H=histOf(g.p,g.j);if(!H)return null;const M=(DB.META[g.p]||{})[g.sd==='L'?'l':'v']||[],bd={};M.forEach(m=>bd[m[0]]=m);
 return H.filter(h=>h[1]>0).slice(0,10).map(h=>({v:HI(h,g.m),m:bd[h[0]]||[h[0]],min:h[1],h}))}
const cnt=(arr,f)=>{const w=arr.slice(0,10);return{c:w.filter(f).length,n:w.length}};
function reg(x){if(x._r)return x._r;let r;if(x.k==='G'){const V=valsG(x);r={g:V?cnt(V,o=>hitG(o.v,x.l)):{c:0,n:0}}}
 else{const V=valsT(x),f=o=>hit(o.v,x.l,x.s);r={l:cnt(V.l,f),v:cnt(V.v,f),h:cnt(V.h,f)}}return x._r=r}
const need=(K,n)=>Math.ceil(K*n/10-1e-9);
function regOk(x,S){const r=reg(x),ok=q=>q.n>=Math.min(S.minN,10)&&q.c>=need(S.K,q.n);
 if(x.k==='G')return ok(r.g);if(!r.l.n&&!r.v.n)return false;
 return S.who==='local'?ok(r.l):S.who==='visitante'?ok(r.v):S.who==='alguno'?(ok(r.l)||ok(r.v)):(ok(r.l)&&ok(r.v))}
const ratio=x=>{const r=reg(x);if(x.k==='G')return r.g.n?r.g.c/r.g.n:null;if(!r.l.n||!r.v.n)return null;return Math.min(r.l.c/r.l.n,r.v.c/r.v.n)};
const rel=x=>x.col==null||!x.l?null:x.col/Math.max(x.l,1);
const clamp=v=>Math.max(0,Math.min(1,v));
/* Índice de sentido 0–100: solo ordena (regularidad 45, colchón 25, probabilidad 20, directos 10). No es una probabilidad. */
function sentido(x){if(x._s!=null)return x._s;const ra=ratio(x),re=rel(x),p=prob(x);if(ra==null)return x._s=0;
 const nn=x.k==='G'?reg(x).g.n:Math.min(reg(x).l.n,reg(x).v.n),fn=clamp(nn/7);
 let s=(x.k==='G'?55:45)*clamp((ra-.4)/.6)*fn+25*clamp((re||0)/.3)+20*clamp(((p||.5)-.4)/.4);
 if(x.k==='T'){const h=reg(x).h;s+=h.n>=2?10*h.c/h.n:5;if(x.m==='tarjetas'&&x.s==='Menos')s-=8}return x._s=Math.round(s)}
function pasa(x,S){if(x.c==null||x.c<S.cmin||x.c>S.cmax)return false;
 if(S.tipo==='equipo'&&x.k!=='T')return false;if(S.tipo==='jugador'&&x.k!=='G')return false;
 if(S.mks.length&&!S.mks.includes((x.k==='G'?'j:':'')+x.m))return false;if(S.lado&&x.k==='T'&&x.s!==S.lado)return false;
 if(x.k==='G'&&S.tit&&!(x.tit>=.7))return false;if(!regOk(x,S))return false;
 if(S.col>-1){const r=rel(x);if(x.k==='G'&&x.col==null){}else if(r==null||!(S.col===0?r>0:r*100>=S.col))return false}
 if(S.h2h&&x.k==='T'){const h=reg(x).h;if(h.n>=2&&h.c/h.n<.5)return false}
 if(S.pmin&&!((prob(x)||0)*100>=S.pmin))return false;return true}
function unoPor(rows){const best=new Map();rows.forEach(x=>{const k=x.p+'|'+x.m+'|'+(x.k==='G'?x.j:x.a);const b=best.get(k);if(!b||sentido(x)>sentido(b)||(sentido(x)===sentido(b)&&x.c>b.c))best.set(k,x)});return[...best.values()]}
/* ===== agregados sobre líneas resueltas ===== */
const resuelta=x=>x.rs==='C'||x.rs==='F';
function agg(rows){let n=0,w=0,ip=0,pl=0,ps=0;rows.forEach(x=>{if(!resuelta(x)||!x.c)return;n++;const g=x.rs==='C';if(g)w++;ip+=1/x.c;pl+=g?x.c-1:-1;ps+=prob(x)||0});
 return{n,w,hit:n?w/n:null,imp:n?ip/n:null,roi:n?pl/n:null,pm:n?ps/n:null}}
const enJor=(x,j)=>!j||P[x.p].jor===j;
/* ===== cupón ===== */
const inCup=x=>ST.cup.includes(x.key);
function cupInfo(keys){const legs=keys.map(k=>BYKEY.get(k)).filter(Boolean);let c=1,p=1;legs.forEach(x=>{c*=x.c;p*=prob(x)||0});
 const byP={};legs.forEach(x=>(byP[x.p]=byP[x.p]||[]).push(x));const avis=[];
 Object.values(byP).forEach(g=>{if(g.length>1)avis.push(`${g.length} patas de ${P[g[0].p].n}: Betano recalcula el precio y pueden ir juntas (no es el producto).`);
  for(let i=0;i<g.length;i++)for(let k=i+1;k<g.length;k++){const a=g[i],b=g[k];if(a.k==='T'&&b.k==='T'&&a.m===b.m&&a.a===b.a){avis.push(a.s!==b.s?`Contradicción o cobertura: ${tx(a)} y ${tx(b)}.`:`Misma idea dos veces: ${tx(a)} y ${tx(b)} (una ya incluye a la otra).`)}}});
 legs.forEach(x=>{if(x.k==='T'&&x.m==='tarjetas'&&x.s==='Menos')avis.push(`${tx(x)}: Betano cuenta la roja como 2 puntos y el historial solo trae amarillas; es más frágil de lo que muestra la regularidad.`);if(x.k==='G'&&!(x.tit>=.7))avis.push(`${x.j} no aparece en el XI probable.`)});
 const st=legs.every(resuelta)&&legs.length?(legs.every(x=>x.rs==='C')?'Ganada':'Perdida'):legs.some(x=>x.rs==='F')?'Perdida':'Pendiente';
 return{legs,c,p,avis,st,multi:Object.keys(byP).length,falladas:legs.filter(x=>x.rs==='F').length,perdidas:keys.length-legs.length}}
