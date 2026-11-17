/* ===== arranque, eventos y acciones ===== */
const cupBadge=()=>ST.cup.length?`<span class="cnt">${ST.cup.length}</span>`:'';
function shell(){$('#app').innerHTML=`<header id="top"><div class="logo" data-act="home" title="Inicio">M</div><input class="srch" id="q" type="search" placeholder="Buscar partido, jugador o página" autocomplete="off" aria-label="Buscar"><div class="sp"></div>
 <a class="btn soft hide-m" href="#/cupon" id="topcup"></a></header><div id="sres" class="card flush" style="display:none;position:fixed;top:60px;left:10px;width:min(440px,calc(100% - 20px));z-index:60;max-height:70vh;overflow:auto;box-shadow:0 8px 30px rgba(0,0,0,.2)"></div>
 <div id="shell"><nav id="nav" aria-label="Secciones"></nav><main id="main"></main></div><nav id="tabbar" aria-label="Secciones"></nav>
 <div id="ov" data-act="close"></div><aside id="dr" aria-label="Detalle"></aside><div id="tip"></div><div id="toast" role="status"></div>`}
function chrome(){const r=route(),pg=r.pg==='partido'?'partidos':r.pg;
 $('#nav').innerHTML=NAV.map(n=>n[0]==='-'?`<div class="sep">${n[1]}</div>`:`<a href="#/${n[0]}" class="${n[0]===pg?'on':''}"><span class="ic">${ic(n[2])}</span>${n[1]}${n[0]==='cupon'?cupBadge():''}</a>`).join('')+`<div class="xs mut" style="padding:16px 10px">Datos del ${esc(DB.gen)} · solo lectura. Aquí no se apuesta.</div>`;
 $('#tabbar').innerHTML=[['inicio','Inicio','home'],['partidos','Partidos','ball'],['estrategia','Estrategia','target'],['cupon','Cupón','ticket']].map(n=>`<a href="#/${n[0]}" class="${n[0]===pg?'on':''}">${ic(n[2])}${n[1]}${n[0]==='cupon'?cupBadge():''}</a>`).join('')+`<a href="#" data-act="menu" class="${['inicio','partidos','estrategia','cupon'].includes(pg)?'':'on'}">${ic('more')}Más</a>`;
 $('#topcup').innerHTML=`${ic('ticket')} Cupón ${ST.cup.length?`<b class="num">${ST.cup.length}</b>`:''}`}
function render(keep){const r=route(),ae=document.activeElement,fb=ae&&ae.dataset&&ae.dataset.bind,ss=fb?ae.selectionStart:null,sy=scrollY;
 try{$('#main').innerHTML=PAGES[r.pg].render(r.arg)}catch(e){$('#main').innerHTML=`<div class="card"><div class="empty">No se pudo mostrar esta página (${esc(e.message)}). <a href="#/inicio">Volver al inicio</a></div></div>`;console.error(e)}
 chrome();document.title=({inicio:'Inicio',partidos:'Partidos',partido:'Partido',estrategia:'Mi estrategia',cupon:'Cupón',lineas:'Líneas',jugadores:'Jugadores',backtest:'Backtest histórico',apuestas:'Mis apuestas',aprender:'Qué funciona',enviadas:'Lo que te envié',datos:'Datos',docs:'Documentos'}[r.pg]||'Mando')+' · Mando';
 if(fb){const el=$(`#main [data-bind="${fb}"]`);if(el){el.focus();try{el.setSelectionRange(ss,ss)}catch(e){}}}
 if(keep)scrollTo(0,sy);else scrollTo(0,0);if(DR&&DR.t==='line'&&$('#dr').classList.contains('on')){const st=$('#dr').scrollTop;openLine(DR.key);$('#dr').scrollTop=st}}
const upd=()=>{save();render(true)};
const parseV=v=>v==='true'?true:v==='false'?false:/^-?\d+(\.\d+)?$/.test(v)?+v:v;
function download(name,text,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type:type||'text/plain'}));a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500)}
const now=()=>{const d=new Date();return d.toLocaleDateString('es-CO',{day:'numeric',month:'short'})+' '+d.toTimeString().slice(0,5)};
const ACT={home(){go('inicio')},close(){closeDr()},line(el){openLine(el.dataset.key)},menu(el,e){e.preventDefault();$('#nav').classList.toggle('open')},
 cup(el){const k=el.dataset.key,i=ST.cup.indexOf(k);if(i>=0){ST.cup.splice(i,1);toast('Quitada del cupón')}else{ST.cup.push(k);toast('Añadida al cupón')}upd()},
 pv(el){ST.pv=ST.pv||{};const k=el.dataset.k;ST.pv[k]=k==='l'?+el.dataset.v:el.dataset.v;if(k!=='l')delete ST.pv.l;upd()},
 preset(el){const pr=Object.assign({},PRE,ST.presets||{})[el.dataset.n];if(pr){Object.assign(ST.est,{mks:[],lado:'',tipo:'todo'},pr);toast('Filtro: '+el.dataset.n);upd()}},
 savepre(){const n=(getp('f.pname','')||'').trim();if(!n){toast('Escribe un nombre para el filtro');return}ST.presets=ST.presets||{};ST.presets[n]=JSON.parse(JSON.stringify(ST.est));setp('f.pname','');toast('Filtro guardado');upd()},
 auto(){const S0=route().pg==='estrategia'?ST.est:ST.strat,rows=stratRows(ST.jor,S0).filter(x=>P[x.p].est!=='final'),pool=rows.length?rows:stratRows(ST.jor,S0),seen=new Set(),keys=[];let c=1;
  for(const x of pool){if(seen.has(x.p))continue;seen.add(x.p);keys.push(x.key);c*=x.c;if(c>=(ST.target||3))break}
  if(!keys.length){toast('Ninguna línea pasa tu filtro en esta jornada');return}ST.cup=keys;save();toast(c>=(ST.target||3)?'Combinada armada: cuota '+f2(c):'No alcanzó la cuota; quedó en '+f2(c));if(route().pg==='cupon')render();else go('cupon')},
 usarest(){ST.strat=JSON.parse(JSON.stringify(ST.est));toast('Las demás pestañas ahora usan este filtro');upd()},
 volverest(){ST.est=JSON.parse(JSON.stringify(ST.strat));toast('Filtro vuelto al de las demás pestañas');upd()},
 clearf(el){const d={'f.lr':'','f.le':'','f.lk0':'','f.lk1':'','f.ls':'','f.lm':'','f.la':'','f.lp':''};String(el.dataset.keys||'').split(',').forEach(k=>{if(k in d)setp(k,d[k])});upd()},
 loadcup(el){const ks=JSON.parse(el.dataset.keys).filter(k=>BYKEY.has(k));ST.cup=ks;save();toast(ks.length+' patas cargadas');if(route().pg==='cupon')render();else go('cupon')},
 clearcup(){ST.cup=[];toast('Cupón vacío');upd()},
 copy(){const t=cupText(cupInfo(ST.cup));(navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(t):Promise.reject()).then(()=>toast('Copiado'),()=>{download('cupon.txt',t);toast('Descargado como texto')})},
 savecup(){const n=(getp('f.cname','')||'').trim()||'Cupón '+now();ST.saved=ST.saved||[];ST.saved.unshift({n,keys:ST.cup.slice(),ts:now()});setp('f.cname','');toast('Cupón guardado');upd()},
 delsaved(el){ST.saved.splice(+el.dataset.i,1);upd()},
 bet(){const inf=cupInfo(ST.cup);if(!inf.legs.length)return;if(!(ST.stake>0)){toast('Escribe cuánto apostaste');return}const cr=+getp('f.creal',0)||inf.c;ST.bets=ST.bets||[];ST.bets.unshift({n:(getp('f.cname','')||'').trim()||'Cupón de '+inf.legs.length+' patas',keys:ST.cup.slice(),stake:ST.stake,cuota:Math.round(cr*100)/100,ts:now()});setp('f.creal','');setp('f.cname','');ST.cup=[];save();toast('Anotada en Mis apuestas');go('apuestas')},
 betman(el){const b=ST.bets[+el.dataset.i];if(b){if(el.dataset.v)b.man=el.dataset.v;else delete b.man;upd()}},delbet(el){ST.bets.splice(+el.dataset.i,1);toast('Apuesta borrada');upd()},
 export(){download('mando_mis_datos.json',JSON.stringify(ST),'application/json');toast('Copia descargada')},
 csv(){const R=PAGES.lineas._R||[],h=['jornada','hora','partido','mercado','ambito','lado','linea','cuota','p','reg_local','reg_visitante','directos','esperado','colchon','sentido','pasa_estrategia','resultado','valor_real'];
  const rows=R.map(x=>{const r=reg(x),p=P[x.p];return[p.jor,p.hh,p.n,MK[x.m],x.a,x.s,x.l,x.c,prob(x)!=null?prob(x).toFixed(4):'',regTxt(r.l),regTxt(r.v),regTxt(r.h),x.e==null?'':x.e,x.col==null?'':x.col,sentido(x),pasa(x,ST.strat)?'si':'no',x.rs||'',x.real==null?'':x.real].map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(';')});
  download('lineas_filtradas.csv','﻿'+h.join(';')+'\n'+rows.join('\n'),'text/csv');toast(rows.length+' líneas descargadas')},
 more(el){setp('f.lim.'+el.dataset.id,+el.dataset.n);upd()},
 sres(el){$('#sres').style.display='none';$('#q').value='';const k=el.dataset.k,v=el.dataset.v;if(k==='p')go('partido/'+v);else if(k==='g'){setp('f.jq',v);setp('f.jj','');setp('f.jh','0');setp('f.jm','');save();if(route().pg==='jugadores')render();else go('jugadores')}else if(k==='d')go('docs/'+v);else go(v)}};
ACT.btdl=()=>{download('backtest_regla_x_de_n.html',DB.BT,'text/html');toast('Descargado')};
let _pl=null;
function search(q){q=q.trim().toLowerCase();const box=$('#sres');if(q.length<2){box.style.display='none';return}
 if(!_pl){const m=new Map();G.forEach(x=>{if(!m.has(x.j))m.set(x.j,x.p)});_pl=[...m.entries()]}
 const row=(k,v,t,s,tag)=>`<div class="srow" data-act="sres" data-k="${k}" data-v="${esc(v)}"><div style="flex:1;min-width:0"><div class="b sm">${esc(t)}</div><div class="xs mut">${esc(s)}</div></div><span class="tag">${tag}</span></div>`;
 const out=P.filter(p=>p.n.toLowerCase().includes(q)).slice(0,6).map(p=>row('p',p.i,p.n,jorLab(p.jor)+' · '+p.hh+' · '+p.liga,'partido'))
  .concat(_pl.filter(e=>e[0].toLowerCase().includes(q)).slice(0,6).map(e=>row('g',e[0],e[0],P[e[1]].n,'jugador')))
  .concat(NAV.filter(n=>n[0]!=='-'&&n[1].toLowerCase().includes(q)).map(n=>row('n',n[0],n[1],'Ir a la página','página')))
  .concat(DB.docs.map((d,i)=>[d,i]).filter(e=>e[0][1].toLowerCase().includes(q)).slice(0,4).map(e=>row('d',e[1],e[0][1].replace(/\*\*/g,''),e[0][0],'documento')));
 box.innerHTML=out.join('')||'<div class="empty sm">Nada con «'+esc(q)+'». Prueba con el nombre de un equipo o un jugador.</div>';box.style.display='block'}
let _deb=null;
function boot(){shell();tipInit();
 document.addEventListener('click',e=>{const s=e.target.closest('[data-sort]');if(s){const id=s.dataset.sort,c=+s.dataset.col,cur=getp('f.sort.'+id,null);setp('f.sort.'+id,{c,d:cur&&cur.c===c?-cur.d:-1});upd();return}
  const a=e.target.closest('[data-act]');if(a){if(a.tagName==='A'&&a.dataset.act==='close'){closeDr();return}if(ACT[a.dataset.act]){ACT[a.dataset.act](a,e);return}}
  const st=e.target.closest('[data-set]');if(st){setp(st.dataset.set,parseV(st.dataset.val));if(st.dataset.set==='jor'||st.dataset.set==='tab.partido'){save();render(st.dataset.set!=='jor'||true)}else upd();return}
  const tg=e.target.closest('[data-tog]');if(tg){const arr=(getp(tg.dataset.tog,[])||[]).slice(),v=tg.dataset.val,i=arr.indexOf(v);if(i>=0)arr.splice(i,1);else arr.push(v);setp(tg.dataset.tog,arr);upd();return}
  if(!e.target.closest('#sres')&&e.target.id!=='q')$('#sres').style.display='none';if(e.target.closest('#nav a'))$('#nav').classList.remove('open')});
 const onBind=e=>{const el=e.target;if(el.id==='q'){if(e.type==='input')search(el.value);return}if(el.dataset.actChange==='import'&&e.type==='change'){const f=el.files[0];if(!f)return;const rd=new FileReader();rd.onload=()=>{try{const s=JSON.parse(rd.result);if(!s||typeof s!=='object'||!s.strat)throw 0;ST=Object.assign(JSON.parse(JSON.stringify(DEF)),s);if(!JORS.includes(ST.jor))ST.jor=DEF.jor;ensureEst();save();toast('Copia cargada');render()}catch(x){toast('Ese archivo no es una copia de Mando')}};rd.readAsText(f);return}
  if(!el.dataset||!el.dataset.bind)return;const isNum='num'in el.dataset;if(isNum&&e.type==='input')return;let v=el.value;if(isNum){if(v===''||isNaN(+v))return;v=+v}setp(el.dataset.bind,v);
  if(e.type==='input'){clearTimeout(_deb);_deb=setTimeout(upd,220)}else upd()};
 document.addEventListener('input',onBind);document.addEventListener('change',onBind);
 document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeDr();$('#sres').style.display='none'}if(e.key==='Enter'&&e.target.id==='q'){const f=$('#sres .srow');if(f)f.click()}if(e.key==='/'&&!/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)){e.preventDefault();$('#q').focus()}});
 addEventListener('hashchange',()=>{closeDr();$('#nav').classList.remove('open');render()});render()}
boot();
