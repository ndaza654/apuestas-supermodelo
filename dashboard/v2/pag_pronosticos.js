/* ===== Pronósticos de Flashscore: apuesta de la PREVIA (partidos con Preview) y picks de las NOTICIAS =====
   Filtros funcionales (estado en ST.f.pr*): jornada, tipo, origen (previa humana / IA), mercado, estado, cuota, búsqueda. */
const PR_MERC={resultado:'Resultado',goles:'Goles',ambos:'Ambos marcan',corners:'Córners',tarjetas:'Tarjetas',remates:'Remates',tiros_arco:'Tiros al arco'};
const prTag=r=>r==='cumplió'?'<span class="tag ok">SE DIO ✓</span>':r==='falló'?'<span class="tag bad">FALLÓ ✗</span>':'<span class="tag warn">pendiente</span>';
const prRes={'1':'Gana el local','2':'Gana el visitante','X':'Empate','1X':'Local o empate','X2':'Visitante o empate','12':'Cualquiera gana'};
const prLado=p=>!p?'–':p.mercado==='resultado'?(prRes[p.lado]||p.lado):p.mercado==='goles'?`Goles ${p.ambito||'total'} ${p.lado}${p.rango?' '+p.rango[0]+' a '+p.rango[1]:' '+f1(p.linea)}`:p.mercado==='ambos'?`Ambos marcan: ${p.lado}`:esc(p.texto||p.mercado);
function prCuenta(L){const r=L.filter(x=>x.estado==='cumplió'||x.estado==='falló');return{n:r.length,ok:r.filter(x=>x.estado==='cumplió').length,tot:L.length}}
/* aplana previas y picks de noticias en una lista única de «pronósticos» */
function prItems(){const P=DB.PRON||{},out=[];
 Object.keys(P).forEach(j=>{const e=P[j];
  (e.previas||[]).forEach(x=>{const a=x.apuesta;const patas=a?(a.patas&&a.patas.length?a.patas:[a]):[];
   out.push({id:'pv:'+j+':'+x.clave,jor:j,tipo:'previa',origen:a?'humana':(x.tipo_previa==='IA'?'IA':'sin apuesta'),partido:x.partido,liga:x.liga,hora:x.hora_bogota,
    texto:a?(a.texto||prLado(a)):'Sin apuesta: la previa solo da probabilidades',patas,mercados:[...new Set(patas.map(p=>p.mercado))],cuota:a&&a.cuota||null,casa:a&&a.casa||null,
    estado:a?(a.resultado||'pendiente'):'sin apuesta',real:a&&a.real||null,raw:x});});
  (e.noticias||[]).forEach(n=>(n.pronosticos||[]).forEach((p,i)=>{
   out.push({id:'nt:'+j+':'+n.id+':'+i,jor:j,tipo:'noticia',origen:'noticia',partido:p.partido,liga:p.liga||'',hora:p.hora_bogota,
    texto:prLado(p),patas:[p],mercados:[p.mercado],cuota:p.cuota||null,casa:p.casa||null,estado:p.resultado||'pendiente',real:p.real||null,raw:p,noticia:n});}));
 });return out}
function prFiltrar(L){const q=(getp('f.prq','')||'').toLowerCase().trim();
 const j=getp('f.prj',''),t=getp('f.prt',''),o=getp('f.pro',''),m=getp('f.prm',''),e=getp('f.pre',''),c=getp('f.prc','');
 return L.filter(x=>(!j||x.jor===j)&&(!t||x.tipo===t)&&(!o||x.origen===o)&&(!m||x.mercados.includes(m))
  &&(!e||(e==='resuelto'?(x.estado==='cumplió'||x.estado==='falló'):x.estado===e))&&(!c||(c==='con'?!!x.cuota:!x.cuota))
  &&(!q||(x.partido+' '+x.liga+' '+x.texto+' '+(x.raw.argumentos||[]).join(' ')+' '+(x.raw.argumento||'')).toLowerCase().includes(q)))}
function prFila(x){const r=x.raw,a=x.tipo==='previa'?r:null;
 const ins=r.insights?`<div class="xs mut" style="margin-top:6px">Probabilidades implícitas de las cuotas: ${[r.insights.p1!=null?'gana local '+pc(r.insights.p1):'',r.insights.p2!=null?'gana visitante '+pc(r.insights.p2):'',r.insights.over25!=null?'más de 2,5 goles '+pc(r.insights.over25):'',r.insights.ambos!=null?'ambos marcan '+pc(r.insights.ambos):''].filter(Boolean).join(' · ')}${r.insights.goles_implicitos?' · goles esperados por el mercado '+f1(r.insights.goles_implicitos):''}.</div>`:'';
 const arg=a?(r.argumentos||[]):(r.argumento?[r.argumento]:[]);
 return`<div class="card" style="margin-bottom:10px"><div class="hd"><h3 style="margin:0;font-size:15px">${esc(x.partido)}</h3><div class="sp"></div>${x.estado==='sin apuesta'?'<span class="tag">sin apuesta</span>':prTag(x.estado)}</div>
  <div class="xs mut">${esc(x.liga)} · ${esc(x.jor)} ${esc(x.hora||'')} (Bogotá) · <span class="tag">${x.tipo==='previa'?'previa '+(x.origen==='humana'?'escrita por una persona':'generada con IA'):'noticia'}</span></div>
  <div class="b" style="margin:8px 0 2px">${x.tipo==='previa'?'Apuesta de la previa: ':'Pick: '}${esc(x.texto)}</div>
  <div class="xs mut">${x.cuota?'Cuota '+f2(x.cuota)+(x.casa?' · '+esc(x.casa):''):'Sin cuota en la fuente.'}${x.real?' · real: '+esc(x.real):''}${a&&r.autor?' · autor '+esc(r.autor):''}${x.noticia?' · '+esc(x.noticia.autor)+', '+esc(x.noticia.medio):''}</div>
  ${ins}
  ${arg.length?`<details style="margin-top:8px"><summary class="sm b">Argumentos de la fuente</summary><ul class="sm" style="margin:6px 0 0 18px">${arg.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></details>`:''}
  ${a&&(r.bajas||[]).length?`<div class="xs mut" style="margin-top:6px">Bajas y dudas: ${r.bajas.map(esc).join(' · ')}</div>`:''}
  ${a&&r.nota?`<div class="xs mut" style="margin-top:6px">${esc(r.nota)}</div>`:''}
  <div class="xs mut" style="margin-top:6px"><a href="${esc(a?r.fuente:x.noticia.fuente)}" target="_blank" rel="noopener">Fuente</a>${a?' · leído '+esc(r.leido):''}</div></div>`}
function prNoticia(n){const L=n.pronosticos||[],c=prCuenta(L.map(p=>({estado:p.resultado})));
 return`<div class="card"><div class="hd"><h3 style="margin:0">${esc(n.titulo)}</h3><div class="sp"></div><span class="tag ${c.n?(c.ok*2>=c.n?'ok':'bad'):'warn'}">${c.n?c.ok+' de '+c.n+' se dieron':'sin resultados todavía'}</span></div>
 <div class="xs mut">${esc(n.autor)} · ${esc(n.medio)} · publicado ${esc(n.publicado)} · <a href="${esc(n.fuente)}" target="_blank" rel="noopener">Fuente</a></div>
 <div class="note warn" style="margin:8px 0">${esc(n.aviso)}</div>
 <h4 style="margin:12px 0 4px">¿Es verdad y es factible? (contraste con nuestros datos)</h4><ul class="sm" style="margin:0 0 0 18px">${(n.contraste||[]).map(t=>`<li><b>${esc(t.partido)}:</b> ${esc(t.hallazgo)} <span class="tag warn">${esc(t.estado)}</span></li>`).join('')||'<li>Sin contraste todavía.</li>'}</ul>
 <div class="xs mut" style="margin-top:8px">${esc(n.via||'')} Leído ${esc(n.leido)}.</div></div>`}
PAGES.pronosticos={render(){const P=DB.PRON||{},ks=Object.keys(P).sort().reverse();
 if(!ks.length)return`<h1>Pronósticos de Flashscore</h1><div class="card"><div class="empty">Todavía no hay previas ni noticias guardadas.</div></div>`;
 const ALL=prItems(),F=prFiltrar(ALL),cA=prCuenta(ALL),cF=prCuenta(F);
 const mercs=[...new Set(ALL.flatMap(x=>x.mercados))].sort();
 const hayF=['prj','prt','pro','prm','pre','prc','prq'].some(k=>getp('f.'+k,''));
 const cntT=t=>ALL.filter(x=>x.tipo===t).length;
 /* aciertos por origen / mercado (solo lo ya resuelto) */
 const grp=(fn)=>{const g={};ALL.forEach(x=>{if(x.estado!=='cumplió'&&x.estado!=='falló')return;fn(x).forEach(k=>{const o=g[k]=g[k]||{n:0,ok:0};o.n++;if(x.estado==='cumplió')o.ok++})});return g};
 const gO=grp(x=>[x.tipo==='previa'?'previa '+x.origen:'noticia']),gM=grp(x=>x.mercados.map(m=>PR_MERC[m]||m));
 const tb=g=>Object.keys(g).length?`<div class="tbl"><table><thead><tr><th>Grupo</th><th>Se dieron</th><th>%</th></tr></thead><tbody>${Object.keys(g).sort().map(k=>`<tr><td>${esc(k)}</td><td class="num">${g[k].ok} de ${g[k].n}</td><td class="num">${pc(g[k].ok/g[k].n,0)}</td></tr>`).join('')}</tbody></table></div>`:'<div class="xs mut">Todavía no hay pronósticos resueltos.</div>';
 const noticiasF=ks.flatMap(k=>(P[k].noticias||[]).map(n=>({k,n}))).filter(({k,n})=>{const j=getp('f.prj',''),t=getp('f.prt',''),q=(getp('f.prq','')||'').toLowerCase().trim();return(!j||k===j)&&(!t||t==='noticia')&&(!q||(n.titulo+' '+n.autor).toLowerCase().includes(q)||(n.pronosticos||[]).some(p=>(p.partido+' '+p.argumento).toLowerCase().includes(q)))});
 const listas=ks.filter(k=>!getp('f.prj','')||k===getp('f.prj','')).map(k=>({k,L:P[k].lista})).filter(x=>x.L);
 return`<h1>Pronósticos de Flashscore</h1><p class="mut">La apuesta que Flashscore da en la <b>previa</b> de los partidos con Preview y los picks de sus <b>noticias</b>. Se guardan antes del partido y se califican con el marcador real: así se ve si lo que dicen se cumple. Criterio de tipsters y medios <b>sin resultados verificados</b>: se mide, no se asume.</p>
 <div class="card"><div class="hd"><h3 style="margin:0">Filtros</h3><div class="sp"></div>${hayF?`<button class="chip" data-act="prlimpiar">Limpiar filtros</button>`:''}</div>
  <div class="xs mut" style="margin:6px 0 4px">Jornada</div><div class="chips">${chip('f.prj','','Todas')}${ks.map(k=>chip('f.prj',k,esc(k))).join('')}</div>
  <div class="xs mut" style="margin:8px 0 4px">Tipo</div><div class="chips">${chip('f.prt','','Todos',ALL.length)}${chip('f.prt','previa','Previas',cntT('previa'))}${chip('f.prt','noticia','Noticias',cntT('noticia'))}</div>
  <div class="xs mut" style="margin:8px 0 4px">Estado</div><div class="chips">${chip('f.pre','','Todos')}${chip('f.pre','pendiente','Pendientes',ALL.filter(x=>x.estado==='pendiente').length)}${chip('f.pre','resuelto','Resueltos',cA.n)}${chip('f.pre','cumplió','Se dieron ✓',cA.ok)}${chip('f.pre','falló','Fallaron ✗',cA.n-cA.ok)}${chip('f.pre','sin apuesta','Sin apuesta (IA)',ALL.filter(x=>x.estado==='sin apuesta').length)}</div>
  <div class="grid g3" style="margin-top:10px">${sel('f.pro',[['','Todos'],['humana','Previa escrita por una persona'],['IA','Previa generada con IA'],['noticia','Noticia']],'Origen')}${sel('f.prm',[['','Todos']].concat(mercs.map(m=>[m,PR_MERC[m]||m])),'Mercado')}${sel('f.prc',[['','Todas'],['con','Con cuota en la fuente'],['sin','Sin cuota']],'Cuota')}</div>
  ${txt('f.prq','Buscar','equipo, liga, mercado o argumento')}</div>
 <div class="grid g2">
  <div class="card"><div class="hd"><h3 style="margin:0">Balance de lo filtrado</h3></div><div class="num b" style="font-size:26px">${cF.n?cF.ok+' de '+cF.n+' se dieron ('+pc(cF.ok/cF.n,0)+')':'Sin resultados todavía'}</div><div class="xs mut">${F.length} pronósticos en el filtro · ${ALL.length} guardados en total${cA.n?' · acumulado '+cA.ok+' de '+cA.n+' ('+pc(cA.ok/cA.n,0)+')':''}. Las previas generadas con IA no traen apuesta y no cuentan.</div></div>
  <div class="card"><div class="hd"><h3 style="margin:0">Dónde acierta cada fuente</h3></div>${tb(gO)}<div style="margin-top:8px">${tb(gM)}</div></div></div>
 <h2 style="margin:18px 0 6px">Pronósticos (${F.length})</h2>
 ${F.length?`<div class="grid g2">${F.slice().sort((a,b)=>(b.jor+(b.hora||'')).localeCompare(a.jor+(a.hora||''))||a.partido.localeCompare(b.partido)).map(prFila).join('')}</div>`:'<div class="card"><div class="empty">Ningún pronóstico cumple estos filtros.</div></div>'}
 ${noticiasF.length?`<h2 style="margin:20px 0 6px">Noticias de pronósticos y su contraste (${noticiasF.length})</h2>${noticiasF.map(({n})=>prNoticia(n)).join('')}`:''}
 ${listas.length?`<h2 style="margin:20px 0 6px">Qué partidos tienen Preview</h2>${listas.map(({k,L})=>`<details class="card" style="margin-bottom:8px"><summary class="b">${esc(k)} · ${(L.leidas||[]).length||(L.con_preview_pendientes_de_leer||[]).length} con Preview · ${(L.sin_preview_no_se_recolecta||[]).length} sin Preview</summary>
   ${(L.con_preview_pendientes_de_leer||[]).length?`<div class="note warn" style="margin-top:8px"><b>Con Preview, pendientes de leer:</b> ${L.con_preview_pendientes_de_leer.map(p=>esc(p.partido)+' '+esc(p.hora_bogota||'')).join(' · ')}.</div>`:''}
   ${(L.sin_preview_no_se_recolecta||[]).length?`<div class="note" style="margin-top:8px"><b>Sin Preview (no se recolecta apuesta):</b> ${L.sin_preview_no_se_recolecta.map(p=>esc(p.partido)+' ('+esc(p.hora_bogota||'')+')').join(' · ')}.</div>`:''}
   ${L.nota?`<div class="xs mut" style="margin-top:8px">${esc(L.nota)}</div>`:''}</details>`).join('')}`:''}`}};
