/* ===== Inicio y Partidos ===== */
let _sc={k:'',v:null};
function stratRows(jor,S){S=S||ST.strat;const k=jor+JSON.stringify(S);if(_sc.k===k)return _sc.v;let r=ALL.filter(x=>enJor(x,jor)&&pasa(x,S));if(S.uno)r=unoPor(r);r.sort((a,b)=>sentido(b)-sentido(a)||b.c-a.c);_sc={k,v:r};return r}
const estTag=p=>p.est==='final'?`<span class="tag">final</span>`:p.est==='vivo'?`<span class="tag bad">sin cerrar${p.min?' '+esc(p.min):''}</span>`:`<span class="tag blue">${p.hh}</span>`;
const cover=p=>{const d=p.dat||{};return`<span class="dots" data-tip="${esc(`Betano ${d.B?'✓':'✗'} · Flashscore ${d.F?'✓':'✗'} · alineación ${d.A?'✓':'✗'} · historial de jugadores ${d.J?'✓':'✗'} · árbitro ${d.R?'✓':'✗'}`)}">${'BFAJR'.split('').map(k=>`<i class="${d[k]?'y':''}"></i>`).join('')}</span>`};
function matchRow(p,n){return`<a class="match" href="#/partido/${p.i}"><div class="c"><div class="b num">${p.hh}</div><div class="xs mut">${jorLab(p.jor).split(' ')[0]}</div></div>
 <div style="min-width:0"><div class="t">${esc(p.loc)} <span class="mut" style="font-weight:400">vs</span> ${esc(p.vis)}</div><div class="xs mut" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${esc(p.liga)} · ${cover(p)}</div></div>
 <div class="r">${p.g?`<div class="sc num">${p.g[0]}–${p.g[1]}</div>`:''}${n!=null&&n>0?`<span class="tag blue">${n} pasan</span>`:p.g?'':'<span class="tag">0 pasan</span>'}</div></a>`}
function comboKeys(j,cb){return cb.patas.map(l=>[j,l.partido,l.mercado.replace('jugador:',''),l.jugador?(l.ambito==='local'?'L':'V'):l.ambito,l.jugador||'',l.lado,parseFloat(l.linea)].join('|'))}
function comboCard(j,cb){const keys=comboKeys(j,cb),inf=cupInfo(keys);return`<div class="card"><div class="hd"><h3 style="margin:0">Combinada ${cb.n}</h3><span class="tag">${cb.mismo_partido?'mismo partido':'varios partidos'}</span>${inf.st!=='Pendiente'?`<span class="tag ${inf.st==='Ganada'?'ok':'bad'}">${inf.st}</span>`:''}<div class="sp"></div><b class="num" style="font-size:20px;color:var(--blue)">${cb.mismo_partido?'~':''}${f2(cb.cuota_producto)}</b></div>
 <div class="sm mut" style="margin-bottom:6px">${esc(cb.nota)}</div>${inf.legs.map(x=>`<div class="leg" data-act="line" data-key="${esc(x.key)}" style="cursor:pointer"><div><div class="b sm">${esc(tx(x))}</div><div class="xs mut">${esc(P[x.p].n)} · ${regCell(x)}</div></div><span class="num b">${f2(x.c)}</span>${rsTag(x)}</div>`).join('')}
 <div class="row" style="margin-top:10px"><span class="sm mut num">p ${cb.mismo_partido?'~':''}${pc(cb.p_producto)}</span><div class="sp"></div><button class="btn soft sm" data-act="loadcup" data-keys="${esc(JSON.stringify(keys))}">Cargar en el cupón</button></div></div>`}
PAGES.inicio={render(){const j=ST.jor,ps=P.filter(p=>p.jor===j),rows=stratRows(j),est=DB.EST[j],byP={};rows.forEach(x=>byP[x.p]=(byP[x.p]||0)+1);
 const pend=ps.filter(p=>p.est==='pend').length,fin=ps.filter(p=>p.est==='final').length,a=agg(rows),jm=ps.filter(p=>G.some(g=>g.p===p.i&&!['anota','tarjeta'].includes(g.m))),jh=jm.filter(p=>DB.HIS[p.i]);
 const leidas=[...new Set(DB.L.filter(r=>P[r[0]].jor===j).map(r=>r[17]))].sort(),avis=[];
 jm.filter(p=>!p.xi).forEach(p=>avis.push(`<b>${esc(p.n)}</b>: Betano ofrece mercados de jugador pero no hay alineación. No apuestes jugadores ahí todavía.`));
 jm.filter(p=>!DB.HIS[p.i]).forEach(p=>avis.push(`<b>${esc(p.n)}</b>: falta el historial de jugadores.`));
 ps.forEach(p=>(p.an&&p.an.bajas||[]).slice(0,2).forEach(b=>avis.push(`<b>${esc(p.n)}</b>: ${esc(typeof b==='string'?b:JSON.stringify(b))}`)));
 return`<h1>${jorLong(j)}</h1><p class="mut">${ps.length} partidos · ${pend} por jugar · ${fin} terminados${leidas.length?` · cuotas de Betano leídas el ${esc(bog(leidas[0]))}`:''}</p>
 <div style="margin-bottom:14px">${jorChips('jor')}</div>
 <div class="kpis"><div class="kpi"><div class="v num">${rows.length}</div><div class="l">líneas pasan tu estrategia</div><div class="s"><a href="#/estrategia">Ajustar el filtro</a></div></div>
  <div class="kpi"><div class="v num">${est?est.combinadas.length:0}</div><div class="l">combinadas que te envié</div><div class="s">cuota 3 o más</div></div>
  <div class="kpi"><div class="v num">${jh.length}/${jm.length}</div><div class="l">partidos con historial de jugadores</div><div class="s">de los que tienen mercado de estadística</div></div>
  ${a.n?`<div class="kpi"><div class="v num">${pc(a.hit)}</div><div class="l">acierto de tu filtro (${a.w} de ${a.n})</div><div class="s">la cuota decía ${pc(a.imp)} · ROI ${sg(a.roi)}</div></div>`:`<div class="kpi"><div class="v num">${ST.cup.length}</div><div class="l">patas en tu cupón</div><div class="s"><a href="#/cupon">Abrir cupón</a></div></div>`}</div>
 <div class="split"><div>
  <div class="card flush"><div class="hd" style="padding:14px 14px 0"><h2>Lo que más sentido tiene ${fin&&!pend?'(ya jugado)':'hoy'}</h2><div class="sp"></div><a class="btn soft sm" href="#/estrategia">Ver las ${rows.length}</a></div>${listLi(rows.slice(0,8),{empty:'Ninguna línea pasa tu filtro en esta jornada. Aflójalo en «Mi estrategia».'})}</div>
  ${est&&est.combinadas.length?`<h2 style="margin:18px 0 10px">Combinadas que te envié</h2><div class="grid g2">${est.combinadas.map(c=>comboCard(j,c)).join('')}</div>`:''}
 </div><div>
  ${(()=>{const t=hStats(HBOL());return`<div class="card"><div class="hd"><h2>Histórico desde el 4-nov</h2><div class="sp"></div><a class="btn soft sm" href="#/historico">Abrir</a></div><div class="row"><span class="num b" style="font-size:22px;color:${hCol(t.net)}">${hCop(t.net)}</span><span class="sm mut">en ${t.nr} boletos con dinero · ${t.gan} ganados</span></div><p class="xs mut" style="margin:6px 0 0">Boletos, selecciones, picks, partidos, banca y lecciones de todos los días.</p></div>`})()}
  ${avis.length?`<div class="card"><h2>Ojo con esto</h2>${avis.slice(0,6).map(t=>`<div class="note warn">${t}</div>`).join('')}</div>`:''}
  <div class="card flush"><div class="hd" style="padding:14px 14px 0"><h2>Partidos</h2><div class="sp"></div><a class="btn soft sm" href="#/partidos">Todos</a></div>${ps.map(p=>matchRow(p,byP[p.i]||0)).join('')}</div>
 </div></div>`}};
PAGES.partidos={render(){const j=ST.jor,q=(getp('f.pq','')||'').toLowerCase(),sj=getp('f.psj',''),rows=stratRows(j),byP={};rows.forEach(x=>byP[x.p]=(byP[x.p]||0)+1);
 let ps=P.filter(p=>p.jor===j&&(!q||(p.n+' '+p.liga).toLowerCase().includes(q)));if(sj==='jug')ps=ps.filter(p=>DB.HIS[p.i]);if(sj==='pasan')ps=ps.filter(p=>byP[p.i]);if(sj==='pend')ps=ps.filter(p=>p.est==='pend');
 const hrs=[...new Set(ps.map(p=>p.hh))];
 return`<h1>Partidos</h1><p class="mut">Toca un partido para ver sus gráficos por mercado, sus líneas y sus jugadores.</p><div style="margin-bottom:12px">${jorChips('jor')}</div>
 <div class="card"><div class="filters">${txt('f.pq','Buscar','equipo o liga')}<div class="chips">${chip('f.psj','','Todos')}${chip('f.psj','pasan','Con líneas que pasan')}${chip('f.psj','jug','Con historial de jugadores')}${chip('f.psj','pend','Por jugar')}</div></div></div>
 ${hrs.map(h=>`<div class="card flush">${ps.filter(p=>p.hh===h).map(p=>matchRow(p,byP[p.i]||0)).join('')}</div>`).join('')||'<div class="card"><div class="empty">Ningún partido con ese filtro.</div></div>'}
 <p class="xs mut">Los cinco puntos: Betano, Flashscore, alineación, historial de jugadores, árbitro (verde = está en el repo).</p>`}};
