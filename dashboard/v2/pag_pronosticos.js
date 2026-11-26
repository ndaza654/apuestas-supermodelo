/* ===== Pronósticos de Flashscore: apuesta de la PREVIA (partidos con Preview) y picks de las NOTICIAS ===== */
const prTag=r=>r==='cumplió'?'<span class="tag ok">SE DIO ✓</span>':r==='falló'?'<span class="tag bad">FALLÓ ✗</span>':'<span class="tag warn">pendiente</span>';
const prLado=p=>p.mercado==='resultado'?({'1':'Gana el local','2':'Gana el visitante','X':'Empate','1X':'Local o empate','X2':'Visitante o empate','12':'Cualquiera gana'}[p.lado]||p.lado):p.mercado==='goles'?`Goles ${p.ambito||'total'} ${p.lado} ${f1(p.linea)}`:p.mercado==='ambos'?`Ambos marcan: ${p.lado}`:esc(p.texto||p.mercado);
function prCuenta(L){const r=L.filter(x=>x.resultado==='cumplió'||x.resultado==='falló');return{n:r.length,ok:r.filter(x=>x.resultado==='cumplió').length,tot:L.length}}
function prPrevia(x){const a=x.apuesta||{};return`<div class="card"><div class="hd"><h3 style="margin:0">${esc(x.partido)}</h3><div class="sp"></div>${prTag(a.resultado)}</div>
 <div class="xs mut">${esc(x.liga)} · ${esc(x.fecha)} ${esc(x.hora_bogota)} (Bogotá)</div>
 <div class="b" style="margin:8px 0 4px">Apuesta de la previa: ${esc(a.texto||prLado(a))}</div>
 <div class="xs mut">${a.cuota?'Cuota '+f2(a.cuota)+(a.casa?' · '+esc(a.casa):''):'La previa no trae cuota.'}${a.real?' · real: '+esc(a.real):''}</div>
 <ul class="sm" style="margin:8px 0 4px 18px">${(x.argumentos||[]).map(t=>`<li>${esc(t)}</li>`).join('')}</ul>
 ${(x.bajas||[]).length?`<div class="xs mut">Bajas y dudas: ${x.bajas.map(esc).join(' · ')}</div>`:''}
 <div class="xs mut" style="margin-top:6px"><a href="${esc(x.fuente)}" target="_blank" rel="noopener">Fuente</a> · leído ${esc(x.leido)}</div></div>`}
function prNoticia(n){const L=n.pronosticos||[],c=prCuenta(L);
 return`<div class="card"><div class="hd"><h3 style="margin:0">${esc(n.titulo)}</h3><div class="sp"></div><span class="tag ${c.n?(c.ok*2>=c.n?'ok':'bad'):'warn'}">${c.n?c.ok+' de '+c.n+' se dieron':'sin resultados todavía'}</span></div>
 <div class="xs mut">${esc(n.autor)} · ${esc(n.medio)} · publicado ${esc(n.publicado)} · <a href="${esc(n.fuente)}" target="_blank" rel="noopener">Fuente</a></div>
 <div class="note warn" style="margin:8px 0">${esc(n.aviso)}</div>
 <div class="tbl"><table><thead><tr><th>Partido</th><th>Hora (Bogotá)</th><th>Pick</th><th>Cuota</th><th>p del precio</th><th>Estado</th></tr></thead><tbody>${L.map(p=>`<tr><td>${esc(p.partido)}</td><td>${esc(p.fecha)} ${esc(p.hora_bogota)}</td><td>${prLado(p)}</td><td class="num">${f2(p.cuota)} <span class="xs mut">(${esc(p.cuota_fraccional)} ${esc(p.casa)})</span></td><td class="num">${pc(p.p_implicita,0)}</td><td>${prTag(p.resultado)}${p.real?` <span class="xs mut">${esc(p.real)}</span>`:''}</td></tr>`).join('')}</tbody></table></div>
 <details style="margin-top:8px"><summary class="sm b">Argumentos del autor</summary><ul class="sm" style="margin:6px 0 0 18px">${L.map(p=>`<li><b>${esc(p.partido)}:</b> ${esc(p.argumento)}</li>`).join('')}</ul></details>
 <h4 style="margin:12px 0 4px">¿Es verdad y es factible? (contraste con nuestros datos)</h4><ul class="sm" style="margin:0 0 0 18px">${(n.contraste||[]).map(t=>`<li><b>${esc(t.partido)}:</b> ${esc(t.hallazgo)} <span class="tag warn">${esc(t.estado)}</span></li>`).join('')}</ul>
 <div class="xs mut" style="margin-top:8px">${esc(n.via)} Leído ${esc(n.leido)}.</div></div>`}
PAGES.pronosticos={render(){const P=DB.PRON||{},ks=Object.keys(P).sort().reverse();
 if(!ks.length)return`<h1>Pronósticos de Flashscore</h1><div class="card"><div class="empty">Todavía no hay previas ni noticias guardadas.</div></div>`;
 const all=ks.flatMap(k=>[...(P[k].previas||[]).map(x=>x.apuesta||{}),...(P[k].noticias||[]).flatMap(n=>n.pronosticos||[])]),c=prCuenta(all);
 return`<h1>Pronósticos de Flashscore</h1><p class="mut">La apuesta que Flashscore da en la <b>previa</b> de los partidos con Preview y los picks de sus <b>noticias</b>. Se guardan antes del partido y se califican con el marcador real: así se ve si lo que dicen se cumple. Son criterios de tipsters <b>sin resultados verificados</b>; no son una recomendación nuestra.</p>
 <div class="card"><div class="hd"><h3 style="margin:0">Balance acumulado</h3></div><div class="num b" style="font-size:26px">${c.n?c.ok+' de '+c.n+' se dieron ('+pc(c.ok/c.n,0)+')':'Sin resultados todavía'}</div><div class="xs mut">${c.tot} pronósticos guardados · muestra chica: solo pistas.</div></div>
 ${ks.map(k=>{const e=P[k],L=e.lista;return`<h2 style="margin:20px 0 6px">${esc(k)}</h2>
  ${(e.previas||[]).length?`<h3 style="margin:10px 0 6px">Apuestas de la previa</h3><div class="grid g2">${e.previas.map(prPrevia).join('')}</div>`:''}
  ${L&&(L.con_preview_pendientes_de_leer||[]).length?`<div class="note warn" style="margin-top:10px"><b>Con Preview, pendientes de leer (${L.con_preview_pendientes_de_leer.length}):</b> ${L.con_preview_pendientes_de_leer.map(p=>esc(p.partido)+' '+esc(p.hora_bogota)).join(' · ')}. Se leen con el computador conectado.</div>`:''}
  ${L&&(L.sin_preview_no_se_recolecta||[]).length?`<div class="note" style="margin-top:8px"><b>Sin Preview (no se recolecta apuesta):</b> ${L.sin_preview_no_se_recolecta.map(p=>esc(p.partido)).join(' · ')}.</div>`:''}
  ${(e.noticias||[]).length?`<h3 style="margin:14px 0 6px">Noticias de pronósticos</h3>${e.noticias.map(prNoticia).join('')}`:''}`}).join('')}`}};
