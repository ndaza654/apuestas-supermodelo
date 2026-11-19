/* ===== BB Boost de Betano: combinaciones con precio REAL del Bet Builder ===== */
const bbSg=v=>v==null?'–':(v>=0?'+':'−')+Math.abs(v*100).toFixed(0)+' %';
const bbName=(slug,j)=>{const p=P.find(x=>x.slug===slug&&x.jor===j);return p?p.n:slug};
function bbCombo(c){const ok=c.cumple,evc=c.ev_con_boost;
 return`<div class="card"><div class="hd"><h3 style="margin:0">${esc(c.tag)}</h3><div class="sp"></div><span class="tag ${ok?'ok':'bad'}">${ok?'cumple las condiciones':'NO cumple'}</span></div>
 ${c.patas.map((t,i)=>`<div class="leg"><div><div class="b sm">${esc(t)}</div><div class="xs mut">en el cupón @${f2((c.cuotas_cupon||[])[i])} · catálogo @${f2((c.cuotas_catalogo||[])[i])} · ${c.solidez_patas&&c.solidez_patas[i]>=0.6?'respaldada por la ficha':'sin respaldo de la ficha'}</div></div></div>`).join('')}
 <div class="row" style="margin-top:10px;gap:14px;flex-wrap:wrap"><div><div class="xs mut">Precio BB real</div><div class="num b" style="font-size:24px;color:var(--blue)">${f2(c.precio_bb)}</div><div class="xs mut">producto de cuotas ${f2(c.producto_cupon)}</div></div>
  <div><div class="xs mut">p prudente</div><div class="num b" style="font-size:24px">${pc(c.p_prudente,1)}</div><div class="xs mut">modelo ${pc(c.p_modelo,1)} · estrés ${pc(c.p_stress,1)}</div></div>
  <div><div class="xs mut">EV con boost 25 %</div><div class="num b" style="font-size:24px;color:${evc>=0?'var(--ok)':'var(--bad)'}">${bbSg(evc)}</div><div class="xs mut">sin boost ${bbSg(c.ev_sin_boost)} · equilibrio ${pc(c.p_equilibrio_boost,1)}</div></div></div>
 <div class="xs mut" style="margin-top:8px">Pago con boost ≈ ×${f2(c.pago_boost)} (si el +25 % se suma a la ganancia neta: confírmalo en el cupón) · solidez ${f2(c.solidez)} de 1</div></div>`}
function bbInicio(j){const B=DB.BB[j],ks=Object.keys(B).filter(k=>B[k]&&B[k].combos);
 return`<div class="card"><div class="hd"><h2>BB Boost de hoy</h2><div class="sp"></div><a class="btn soft sm" href="#/bb">Ver combos</a></div>${ks.map(k=>{const m=B[k],c=m.combos[0];return`<div class="leg"><div><div class="b sm">${esc(bbName(k,j))}</div><div class="xs mut">${esc(m.veredicto)}${c?` · mejor: precio ${f2(c.precio_bb)} · p ${pc(c.p_prudente)}`:''}</div></div></div>`}).join('')}</div>`}
PAGES.bb={render(){const j=ST.jor,B=(DB.BB||{})[j];
 if(!B)return`<h1>BB Boost</h1><div style="margin-bottom:12px">${jorChips('jor')}</div><div class="card"><div class="empty">Esta jornada no tiene combinaciones BB Boost guardadas.</div></div>`;
 const ks=Object.keys(B).filter(k=>B[k]&&B[k].combos);
 return`<h1>BB Boost</h1><p class="mut">Bet Builder del mismo partido con el bono de Betano. Aquí el precio es el REAL que devuelve Betano al armar la combinación, no el producto de las cuotas.</p><div style="margin-bottom:12px">${jorChips('jor')}</div>
 <div class="note"><b>Condiciones:</b> ${(B.condiciones_lista||[]).map(esc).join(' · ')}. Se exige margen: cada pata ≥ 1,51 y total ≥ 5,05.</div>
 ${B.aviso?`<div class="note warn">${esc(B.aviso)} Leído a las ${esc(B.leido_hora||'')} (Bogotá).</div>`:''}
 ${ks.map(k=>{const m=B[k];return`<h2 style="margin:18px 0 6px">${esc(bbName(k,j))} <span class="tag ${/^S/i.test(m.veredicto)?'ok':/NO/.test(m.veredicto)?'bad':'warn'}">${esc(m.veredicto)}</span></h2><p class="sm mut">${esc(m.nota)}</p><div class="grid g2">${m.combos.map(bbCombo).join('')}</div>`}).join('')}
 <p class="xs mut" style="margin-top:14px">3 patas son lotería (en el histórico propio salieron 28 %, igual a lo que decía el precio): stake mínimo. Detalle en <code>entregas/${j}/</code> y <code>jornadas/${j}/bb/</code>.</p>`}};
