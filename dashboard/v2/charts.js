/* ===== gráficos (SVG a mano; sin librerías) ===== */
const ab=s=>{s=String(s||'').replace(/^(CD|CF|SD|UD|AD|CE|FC|Club|Real|Atl[eé]tico)\s+/i,'');return s.slice(0,3).toUpperCase()};
const fdia=d=>{if(!d)return'';const m=d.match(/(\d{4})-(\d{2})-(\d{2})/);return m?`${+m[3]}-${['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'][+m[2]-1]}${m[1]!=='2026'?' '+m[1].slice(2):''}`:d};
/* Barras por partido (el más reciente a la derecha). items: [{v, m:[fecha,rival,sede,gf,gc], min?}] ya en orden reciente→antiguo */
function matchBars(items,o){o=o||{};const it=items.slice(0,10).reverse(),n=it.length;if(!n)return'<div class="empty sm">Sin datos de este mercado en la muestra.</div>';
 const W=400,H=o.h||180,top=30,bot=34,left=6,bw=(W-left*2)/Math.max(n,7),ph=H-top-bot,line=o.line,mx=Math.max(...it.map(x=>x.v||0),line!=null?line*1.15:0,1);
 const y=v=>top+ph-ph*(v/mx),isHit=v=>o.ge?v>=line:(o.side==='Menos'?v<line:v>line);let s=`<svg class="ch" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(o.title||'valores por partido')}">`;
 s+=`<line x1="${left}" x2="${W-left}" y1="${top+ph}" y2="${top+ph}" stroke="#E4E6EB"/>`;
 it.forEach((x,k)=>{const cx=left+bw*k+bw/2,w=Math.min(bw-6,30),hh=line==null?null:isHit(x.v),col=line==null?'#1877F2':hh?'#1877F2':'#C9D2E0',m=x.m||[],yy=y(x.v),bh=Math.max(top+ph-yy,2);
  const res=m[3]!=null?`${m[3]}-${m[4]}`:'',gp=m[3]!=null?(m[3]>m[4]?'ganó':m[3]<m[4]?'perdió':'empató'):'';
  const tip=`<b>${esc(fdia(m[0]))}${m[1]?' vs '+esc(m[1]):''}</b>${m[2]?' ('+(m[2]==='L'?'de local':m[2]==='V'?'de visitante':esc(m[2]))+')':''}${res?'<br>'+gp+' '+res:''}<br>${esc(o.unit||'valor')}: <b>${x.v}</b>${x.min!=null?' · '+x.min+' min':''}${line!=null?'<br>'+(hh?'✓ cumple':'✗ no cumple')+' '+esc(o.lineLab||''):''}`;
  s+=`<g class="bar" data-tip="${esc(tip)}"><rect x="${cx-bw/2}" y="0" width="${bw}" height="${H}" fill="transparent"/><rect class="m" x="${cx-w/2}" y="${yy}" width="${w}" height="${bh}" rx="4" fill="${col}"/>`
   +`<text class="val" x="${cx}" y="${yy-4}" text-anchor="middle">${x.v}</text><text x="${cx}" y="${H-19}" text-anchor="middle">${esc(o.lab?o.lab(x):ab(m[1])||'·')}</text>`
   +`<text x="${cx}" y="${H-6}" text-anchor="middle" style="font-size:10px">${esc((m[2]||'')+(res?' '+res:''))}</text></g>`});
 if(line!=null){const ly=y(o.ge?line-.5:line);s+=`<line x1="${left}" x2="${W-left}" y1="${ly}" y2="${ly}" stroke="#1C1E21" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="${left}" x2="${left+18}" y1="8" y2="8" stroke="#1C1E21" stroke-width="1.5" stroke-dasharray="5 4"/><text x="${left+23}" y="12" class="val">${esc(o.lineLab||line)}</text>`}
 return s+'</svg>'}
function pips(arr,f){const w=arr.slice(0,10);let s='<span class="pips">';for(let k=w.length-1;k>=0;k--)s+=`<i class="${f(w[k])?'h':''}"></i>`;return s+'</span>'}
/* barras horizontales de acierto: rows [{l, hit, imp, n}] */
function hitBars(rows){if(!rows.length)return'<div class="empty sm">Sin líneas resueltas con este filtro.</div>';let s='<div>';
 rows.forEach(r=>{const dim=r.n<20?'opacity:.55':'';s+=`<div style="display:grid;grid-template-columns:minmax(90px,150px) minmax(0,1fr) 108px;gap:8px;align-items:center;padding:5px 0;${dim}" data-tip="${esc(`<b>${r.l}</b><br>${r.w} de ${r.n} líneas se dieron (${pc(r.hit)})<br>La cuota decía ${pc(r.imp)}<br>ROI plano ${sg(r.roi)}${r.n<20?'<br>Muestra muy chica: no concluir':''}`)}">
  <div class="sm" style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(r.l)}</div>
  <div style="position:relative;height:18px;background:#EEF0F3;border-radius:4px"><div style="width:${r.n?r.hit*100:0}%;height:100%;background:#1877F2;border-radius:4px"></div>${r.imp!=null?`<div style="position:absolute;top:-3px;bottom:-3px;left:${r.imp*100}%;width:2px;background:#1C1E21"></div>`:''}</div>
  <div class="sm num r"><b>${pc(r.hit)}</b> <span class="mut">n ${r.n}</span></div></div>`});
 return s+'</div><div class="legend" style="margin-top:6px"><span><i style="background:#1877F2"></i>se dio</span>'+(rows.some(r=>r.imp!=null)?'<span><i style="background:#1C1E21;width:2px;height:12px"></i>lo que decía la cuota</span>':'')+'<span>más claro = menos de 20 líneas</span></div>'}
/* calibración: bins [{x(p dicha), y(real), n}] */
function calibChart(bins){const W=400,H=230,l=34,b=28,t=10,r=10,pw=W-l-r,ph=H-t-b,X=v=>l+pw*v,Y=v=>t+ph-ph*v;let s=`<svg class="ch" viewBox="0 0 ${W} ${H}" role="img" aria-label="calibración">`;
 [0,.25,.5,.75,1].forEach(v=>{s+=`<line x1="${l}" x2="${W-r}" y1="${Y(v)}" y2="${Y(v)}" stroke="#EEF0F3"/><text x="${l-5}" y="${Y(v)+4}" text-anchor="end">${v*100}</text><text x="${X(v)}" y="${H-10}" text-anchor="middle">${v*100}</text>`});
 s+=`<line x1="${X(0)}" y1="${Y(0)}" x2="${X(1)}" y2="${Y(1)}" stroke="#8A8D91" stroke-dasharray="4 4"/>`;
 const pts=bins.filter(q=>q.n);if(pts.length>1)s+=`<polyline fill="none" stroke="#1877F2" stroke-width="2" points="${pts.map(q=>X(q.x)+','+Y(q.y)).join(' ')}"/>`;
 pts.forEach(q=>{s+=`<g class="bar" data-tip="${esc(`Se dijo ${pc(q.x)} · se dio ${pc(q.y)}<br>${q.n} líneas`)}"><circle cx="${X(q.x)}" cy="${Y(q.y)}" r="12" fill="transparent"/><circle cx="${X(q.x)}" cy="${Y(q.y)}" r="${Math.max(4,Math.min(9,Math.sqrt(q.n)/1.6))}" fill="#1877F2" stroke="#fff" stroke-width="2"/></g>`});
 return s+`<text x="${l+6}" y="${t+10}">↑ % que se dio · → % que se dijo</text></svg>`}
/* mapa de calor: rows × cols → {hit,n} */
function heat(rl,cl,cell){let s=`<div class="heat" style="grid-template-columns:minmax(70px,auto) repeat(${cl.length},minmax(0,1fr))"><div class="hh"></div>`+cl.map(c=>`<div class="hh">${esc(c)}</div>`).join('');
 rl.forEach((r,i)=>{s+=`<div class="hh" style="justify-content:start;text-align:left">${esc(r)}</div>`;cl.forEach((c,k)=>{const q=cell(i,k);if(!q||!q.n){s+='<div style="background:#F5F6F8;color:#B0B3B8">–</div>';return}
  const d=q.hit-q.imp,a=Math.min(1,Math.abs(d)/.2),bg=q.n<8?'#F5F6F8':d>=0?`rgba(24,119,242,${.12+.55*a})`:`rgba(217,48,37,${.10+.45*a})`;
  s+=`<div style="background:${bg}" data-tip="${esc(`<b>${r} × ${c}</b><br>${q.w} de ${q.n} se dieron (${pc(q.hit)})<br>la cuota decía ${pc(q.imp)}<br>ROI ${sg(q.roi)}`)}"><b>${pc(q.hit)}</b><div class="xs mut">n ${q.n}</div></div>`})});
 return s+'</div><div class="legend" style="margin-top:8px"><span><i style="background:rgba(24,119,242,.6)"></i>acertó más de lo que decía la cuota</span><span><i style="background:rgba(217,48,37,.5)"></i>menos</span><span>gris = menos de 8 líneas</span></div>'}
/* línea acumulada: pts [{y, tip}] */
function lineAcc(pts){if(pts.length<2)return'<div class="empty sm">Aún no hay suficientes boletos cerrados para una curva.</div>';const W=400,H=150,l=8,r=8,t=14,b=14,mn=Math.min(0,...pts.map(p=>p.y)),mx=Math.max(0,...pts.map(p=>p.y)),sp=(mx-mn)||1,X=k=>l+(W-l-r)*k/(pts.length-1),Y=v=>t+(H-t-b)*(1-(v-mn)/sp);
 let s=`<svg class="ch" viewBox="0 0 ${W} ${H}"><line x1="${l}" x2="${W-r}" y1="${Y(0)}" y2="${Y(0)}" stroke="#CED0D4"/><polyline fill="none" stroke="#1877F2" stroke-width="2" points="${pts.map((p,k)=>X(k)+','+Y(p.y)).join(' ')}"/>`;
 pts.forEach((p,k)=>{s+=`<g class="bar" data-tip="${esc(p.tip)}"><circle cx="${X(k)}" cy="${Y(p.y)}" r="11" fill="transparent"/><circle cx="${X(k)}" cy="${Y(p.y)}" r="4" fill="#1877F2" stroke="#fff" stroke-width="2"/></g>`});
 const last=pts[pts.length-1];return s+`<text class="val" x="${W-r}" y="${Math.max(12,Y(last.y)-8)}" text-anchor="end">${last.y<0?'−':''}${cop(Math.abs(last.y))}</text></svg>`}
