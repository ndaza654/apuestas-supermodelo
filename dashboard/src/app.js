'use strict';
/* ===== Armazón: ruteo, navegación por diseño, eventos, panel de detalle ===== */
const GROUPS=[['Explorar',['hoy','lineas','partido','jugadores','buscar']],['Mis datos',['apuestas','sugerencias','cupon']],['Evaluar',['resultados','honestidad','laboratorio','banca']],['Biblioteca',['informes']],['Sistema',['salud','automatizacion','decisiones']]];
const ICON={hoy:'◉',lineas:'☰',partido:'⚽',jugadores:'👤',buscar:'⌕',apuestas:'🎫',sugerencias:'💡',cupon:'🧾',resultados:'✔',honestidad:'⚖',laboratorio:'⚗',banca:'💰',informes:'📚',salud:'♥',automatizacion:'⚙',decisiones:'☑'};
const TIT={hoy:'Hoy',lineas:'Líneas',partido:'Partido',jugadores:'Jugadores',buscar:'Buscar',apuestas:'Mis apuestas',sugerencias:'Sugerencias',cupon:'Cupón',resultados:'Resultados',honestidad:'Honestidad',laboratorio:'Laboratorio',banca:'Banca y riesgo',informes:'Informes',salud:'Salud de datos',automatizacion:'Automatización',decisiones:'Decisiones'};
const NODET=['hoy','lineas','partido','buscar'];
let route=CFG.home,fopen={},menuOpen=false;
const UI=pgState('ui',{theme:CFG.theme,det:'',fopen:{}});if(!['dark','light'].includes(UI.theme))UI.theme=CFG.theme;
function go(r){location.hash='#/'+r}
function parseHash(){const h=location.hash.replace(/^#\/?/,''),[r,q]=h.split('?');route=PG[r]?r:CFG.home;const pr={};(q||'').split('&').filter(Boolean).forEach(kv=>{const[k,v]=kv.split('=');pr[k]=decodeURIComponent(v||'')});return pr}
function applyParams(pr){if(pr.p!=null){if(route==='lineas'){Fl.p=pr.p;Fl.jor='';saveS('lin')}else if(route==='partido'){S.par.p=pr.p;saveS('par')}else if(route==='jugadores'){Fj.p=pr.p;Fj.view='lineas';saveS('jug')}}if(pr.q!=null&&route==='buscar'){S.bus.q=pr.q;saveS('bus')}}
function navHTML(){const cur=route;
 if(CFG.nav==='side')return GROUPS.map(([g,ps])=>`<div class="ng"><div class="ngt">${g}</div>${ps.map(p=>`<a href="#/${p}" class="ni ${cur===p?'on':''}"><i>${ICON[p]}</i><span>${TIT[p]}</span>${p==='cupon'&&CUP.length?`<em>${CUP.length}</em>`:''}</a>`).join('')}</div>`).join('');
 if(CFG.nav==='bottom'){const main=['hoy','lineas','apuestas','cupon'];return`<div class="bn">${main.map(p=>`<a href="#/${p}" class="bi ${cur===p?'on':''}"><i>${ICON[p]}</i><span>${TIT[p]}</span>${p==='cupon'&&CUP.length?`<em>${CUP.length}</em>`:''}</a>`).join('')}<a class="bi ${!main.includes(cur)?'on':''}" data-act="menu"><i>☰</i><span>Más</span></a></div>${menuOpen?`<div class="menu" data-act="menu"><div class="mbox">${GROUPS.map(([g,ps])=>`<div class="ngt">${g}</div><div class="mgrid">${ps.map(p=>`<a href="#/${p}" class="mi ${cur===p?'on':''}"><i>${ICON[p]}</i><span>${TIT[p]}</span></a>`).join('')}</div>`).join('')}</div></div>`:''}`}
 const grp=GROUPS.find(g=>g[1].includes(cur))||GROUPS[0];return`<div class="tn1">${GROUPS.map(([g,ps])=>`<a href="#/${ps[0]}" class="tg ${g===grp[0]?'on':''}">${g}</a>`).join('')}</div><div class="tn2">${grp[1].map(p=>`<a href="#/${p}" class="t2 ${cur===p?'on':''}">${TIT[p]}${p==='cupon'&&CUP.length?` (${CUP.length})`:''}</a>`).join('')}</div>`}
function detG(g){const p=P[g.p],H=hist(g);return`<div class="det"><div class="dh"><h3>${esc(lblG(g))}</h3><button class="b x" data-act="closedet">✕</button></div>${cardG(g)}${H?`<div class="tw"><table class="mini"><tr><th>Fecha</th><th class="n">Min</th><th class="n">Rem.</th><th class="n">Arco</th><th class="n">Gol</th><th class="n">Asist.</th><th class="n">Faltas</th><th class="n">Entr.</th><th class="n">Tarj.</th></tr>${H.map(h=>`<tr><td>${esc(h[0])}</td><td class="n">${h[1]}</td><td class="n">${h[2]}</td><td class="n">${h[3]}</td><td class="n">${h[4]}</td><td class="n">${h[5]}</td><td class="n">${h[8]}</td><td class="n">${h[9]}</td><td class="n">${h[6]+h[7]}</td></tr>`).join('')}</table></div>`:'<div class="mut small">Sin historial recolectado para este jugador.</div>'}</div>`}
function detHTML(){const k=UI.det;if(!k||!NODET.includes(route))return'';const x=lineaDe(k);if(!x)return'';return x.t==='T'?detT(x,true):detG(x)}
function renderDet(){const h=detHTML();$('#det').innerHTML=h;document.body.classList.toggle('det-open',!!h)}
function badge(){const b=$('#cupb');if(!b)return;const I=CUP.length?cupInfo(CUP):null;b.hidden=!CUP.length;b.textContent=I?`Cupón ${CUP.length} · ${f2(I.od)}`:'';$$('.ni em,.bi em').forEach(e=>e.textContent=CUP.length)}
function filtersHTML(pg){const f=pg.f?pg.f():'';if(!f)return'';const open=fopen[route]!=null?fopen[route]:CFG.filtersOpen;return`<details class="fpanel" data-fr="${route}" ${open?'open':''}><summary>Filtros y criterio</summary>${f}</details>`}
function render(){const pr=parseHash();applyParams(pr);const pg=PG[route];document.body.className=`sh-${CFG.id.toLowerCase()} ${UI.theme} r-${route}`;
 $('#nav').innerHTML=navHTML();$('#ptitle').textContent=pg.t;$('#pf').innerHTML=filtersHTML(pg);$('#pm').innerHTML=pg.m();renderDet();badge();$('#gq').value=route==='buscar'?S.bus.q:$('#gq').value;window.scrollTo(0,0)}
function soft(){const pg=PG[route];$('#pm').innerHTML=pg.m();renderDet();badge()}
function full(){const y=window.scrollY,pg=PG[route];$('#pf').innerHTML=filtersHTML(pg);$('#pm').innerHTML=pg.m();renderDet();$('#nav').innerHTML=navHTML();badge();window.scrollTo(0,y)}
const NUMK=new Set(['cmin','cmax','pmin','pmax','evmin','comin','comax','timin','hmin','bank','unit','frac','pct','odds','roi','stake','Kj','Nj','MNj']);
function setPf(el,ev){const[pgk,...rest]=el.dataset.pf.split('.'),k=rest.join('.');const st=S[pgk];if(!st)return;let v=el.type==='checkbox'?el.checked:el.value;
 if(el.type==='number'&&v!=='')v=+v;if(k.startsWith('ck.')){st.ok[k.slice(3)]=el.checked}else st[k]=v;if(k==='one')st[k]=v==='true';if(['cmin','cmax','pmin','pmax','evmin','comin','comax','timin','hmin'].includes(k)&&v==='')st[k]='';
 if(pgk==='lin')st.lim=100;if(pgk==='jug')st.lim=100;saveS(pgk);if(pgk==='cup'&&k==='stake'){soft();return}
 if(pgk==='bus'){soft();return}
 if(ev==='change'&&el.tagName==='SELECT')full();else soft()}
function setSt(el,ev){const k=el.dataset.st;ST[k]=k==='who'?el.value:clamp(+el.value||1,1,k==='N'?DB.N:99);if(k==='N'){ST.K=clamp(ST.K,1,ST.N);ST.MN=clamp(ST.MN,1,ST.N)}if(k==='K')ST.K=clamp(ST.K,1,ST.N);if(k==='MN')ST.MN=clamp(ST.MN,1,ST.N);LSset('st',ST);if(ev==='change')full();else soft()}
document.addEventListener('input',e=>{const el=e.target;if(el.dataset.pf&&el.type!=='checkbox'&&el.tagName!=='SELECT')setPf(el,'input');else if(el.dataset.st&&el.tagName!=='SELECT')setSt(el,'input')});
document.addEventListener('change',e=>{const el=e.target;if(el.dataset.pf)setPf(el,'change');else if(el.dataset.st)setSt(el,'change')});
document.addEventListener('toggle',e=>{const d=e.target;if(d.classList&&d.classList.contains('fpanel')){fopen[d.dataset.fr]=d.open}},true);
function exportCSV(){const{r}=filtLin();downloadCSV('lineas_filtradas.csv',[['jornada','partido','hora','mercado','ambito','lado','linea','cuota','p_modelo','p_mercado','ev','esperado','colchon','cumple','resultado','valor_real']].concat(r.map(t=>{const c=cumT(t);return[P[t.p].jor,P[t.p].n,P[t.p].hora,t.m,t.a,t.s,t.l,t.c,t.pm,t.pk,t.ev,t.e,t.co,c===true?'sí':c===false?'no':'',t.rs,t.rv]})))}
document.addEventListener('click',e=>{const el=e.target.closest('[data-act],[data-go]');if(!el)return;const d=el.dataset;
 if(d.go){e.preventDefault();go(d.go);return}
 const a=d.act;
 if(a==='menu'){menuOpen=!menuOpen;$('#nav').innerHTML=navHTML();return}
 if(a==='atj'){const[k,n]=d.v.split(',').map(Number);ST.N=n;ST.K=k;ST.MN=clamp(ST.MN,1,n);LSset('st',ST);full();return}
 if(a==='det'){if(e.target.closest('button[data-act="cup"]'))return;UI.det=d.k;saveS('ui');if(d.go2){go(d.go2);return}soft();return}
 if(a==='closedet'){UI.det='';saveS('ui');soft();return}
 if(a==='cup'){e.stopPropagation();const k=d.k,i=CUP.indexOf(k);if(i>=0)CUP.splice(i,1);else CUP.push(k);saveCup();if(route==='cupon')full();else soft();return}
 if(a==='more'){if(d.v==='lin')Fl.lim+=150;else if(d.v==='jug')Fj.lim+=150;else if(d.v==='sug')S.sug.lim+=150;else if(d.v==='doc')S.doc.lim+=100;soft();return}
 if(a==='csv'){exportCSV();return}
 if(a==='clrlin'){const s=Fl.saved,m=Fl.mode;Object.assign(Fl,FL0,{saved:s,mode:m});saveS('lin');full();return}
 if(a==='clrjug'){Object.assign(Fj,FJ0,{view:Fj.view});saveS('jug');full();return}
 if(a==='clrlab'){const s=S.lab.saved;Object.assign(S.lab,{tipo:'T',jor:'',m:'',a:'',s:'',cmin:1.35,cmax:'',pmin:'',pmax:'',evmin:'',comin:'',comax:'',c:'',al:'',saved:s});saveS('lab');full();return}
 if(a==='savef'){const n=($('#svname').value||'').trim()||'filtro '+(Fl.saved.length+1),F=Object.assign({},Fl);delete F.saved;Fl.saved.push({name:n,F,st:Object.assign({},ST)});saveS('lin');soft();return}
 if(a==='applyf'){const s=Fl.saved[+d.v];Object.assign(Fl,s.F);Object.assign(ST,s.st);LSset('st',ST);saveS('lin');full();return}
 if(a==='delf'){Fl.saved.splice(+d.v,1);saveS('lin');soft();return}
 if(a==='savelab'){const n=($('#labname').value||'').trim()||'criterio '+(S.lab.saved.length+1),F=Object.assign({},S.lab);delete F.saved;S.lab.saved.push({name:n,F,st:Object.assign({},ST)});saveS('lab');soft();return}
 if(a==='applylab'){const s=S.lab.saved[+d.v];Object.assign(S.lab,s.F);Object.assign(ST,s.st);LSset('st',ST);saveS('lab');full();return}
 if(a==='dellab'){S.lab.saved.splice(+d.v,1);saveS('lab');soft();return}
 if(a==='cupclr'){CUP.length=0;saveCup();full();return}
 if(a==='cupsave'){const n=($('#cupname').value||'').trim()||'cupón '+(S.cup.saved.length+1);S.cup.saved.push({name:n,k:CUP.slice()});saveS('cup');full();return}
 if(a==='cuprest'){CUP.length=0;S.cup.saved[+d.v].k.forEach(k=>CUP.push(k));saveCup();full();return}
 if(a==='cupdel'){S.cup.saved.splice(+d.v,1);saveS('cup');full();return}
 if(a==='cupcopy'){const I=cupInfo(CUP),tx=I.L.map(x=>sh(P[x.p].n)+' · '+lblX(x)+' @'+f2(x.c)).join('\n')+'\nCuota total '+f2(I.od);try{navigator.clipboard.writeText(tx)}catch(er){}el.textContent='Copiado';return}
 if(a==='doc'){S.doc.sel=d.v||'';saveS('doc');if(d.go2){go(d.go2);return}soft();return}
 if(a==='tolineas'){Fl.q=S.bus.q;Fl.jor='';Fl.p='';saveS('lin');go('lineas');return}
 if(a==='theme'){UI.theme=UI.theme==='dark'?'light':'dark';saveS('ui');document.body.classList.remove('dark','light');document.body.classList.add(UI.theme);return}
 if(a==='cuppage'){go('cupon');return}});
$('#gq').addEventListener('keydown',e=>{if(e.key==='Enter'){S.bus.q=e.target.value;saveS('bus');if(route==='buscar')soft();else go('buscar')}});
$('#gq').addEventListener('input',e=>{if(route==='buscar'){S.bus.q=e.target.value;saveS('bus');soft()}});
document.addEventListener('keydown',e=>{if(e.key==='/'&&!/INPUT|SELECT|TEXTAREA/.test((document.activeElement||{}).tagName||'')){e.preventDefault();$('#gq').focus()}if(e.key==='Escape'&&UI.det){UI.det='';soft()}});
window.addEventListener('hashchange',()=>{menuOpen=false;render()});
$('#gen').textContent='Datos del repo al '+DB.gen+' (Bogotá) · prototipo de solo lectura';
render();
