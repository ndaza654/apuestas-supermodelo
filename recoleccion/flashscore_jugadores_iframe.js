/* Historial por jugador de MUCHOS partidos pasados (Flashscore, pestaña «Estadísticas de jugadores»), en una sola pestaña de flashscore.co.
   Regla del repo (CLAUDE.md): obligatorio para los partidos cuya Betano ofrece mercados de jugador de estadística.
   Pasos (navegador del PC, pestaña en flashscore.co, solo lectura):
     1) Para cada partido del día con mercado de jugador, tomar de su ficha (flashscore/<clave>.json → forma.local/visitante) los `mid` de los últimos 10 partidos de cada equipo.
     2) __urls[mid] = {u:'/partido/futbol/<slug local>-<id>/<slug visitante>-<id>/?mid=<mid>', f:fecha, h:local, a:visitante, lh:logo local, la:logo visitante}
        (salen de df_hh_1_<mid del partido de hoy>: campos UE/UQ/UG/UO, EC/ED = logos). No inventar ids: una URL con ids falsos da 404.
     3) __spec[mid] = [[<partido>:<L|V>, <L|V del equipo en ese partido>], ...]  (qué equipos del día jugaron ese partido y de local o visitante)
     4) correr __worker() (UNO a la vez: en paralelo los iframes no pintan la tabla) y esperar a que __queue quede vacía (~14 s por partido)
     5) por cada <partido>:<L|V>: __exportar(key) → texto compacto → raw/pj_<partido>__<L|V>.txt (con hash) → recoleccion/jugadores_decod.py
   Cada partido se abre en un iframe del mismo origen; espera a que la tabla tenga ≥ 8 filas (con esperas fijas fallaban partidos al azar),
   recorre General, Remates, Defensa y Paradas y guarda TODAS las columnas, más el id del jugador y el logo del equipo (así se sabe de qué equipo es cada uno). */
window.__PJ = window.__PJ || {}; window.__log = window.__log || [];
window.scrapeIframe = async function (mid, idx) {
  const sleep = m => new Promise(r => setTimeout(r, m));
  const until = async (fn, ms) => { const t = Date.now(); while (Date.now() - t < ms) { try { if (fn()) return true; } catch (e) {} await sleep(250); } return false; };
  const u = window.__urls[mid]; if (!u) return mid + ' sin url';
  const url = u.u.replace('/?mid=', '/resumen/estadisticas-jugadores/general/?mid=');
  const id = 'pjf' + idx; let f = document.getElementById(id); if (f) f.remove();
  f = document.createElement('iframe'); f.id = id; f.style.cssText = 'position:fixed;left:0;top:0;width:1300px;height:1000px;opacity:0.01;pointer-events:none;border:0;z-index:-1'; f.src = url; document.body.appendChild(f);
  await new Promise(r => { f.onload = r; setTimeout(r, 15000); });
  let D; try { D = f.contentDocument; if (!D || !D.body) return mid + ' sin acceso iframe'; } catch (e) { return mid + ' iframe bloqueado ' + e.message; }
  const ok = await until(() => D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length >= 8, 20000);
  if (!ok) { f.remove(); return mid + ' ' + u.f + ' sin tabla de jugadores (filas ' + D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length + ')'; }
  const P = {}; const isV = s => /^(-|\d[\d.,\/ ()%]*)$/.test(s); const cols = [];
  for (const nm of ['general', 'remates', 'defensa', 'paradas']) {
    const l = D.querySelector('a[href*="estadisticas-jugadores/' + nm + '/"]'); if (!l) continue;
    const hb = [...D.querySelectorAll('th')].map(x => x.textContent).join(',');
    if (nm !== 'general') { l.click(); await until(() => [...D.querySelectorAll('th')].map(x => x.textContent).join(',') !== hb && D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length >= 4, 6000); await sleep(400); } else { await sleep(300); }
    if (nm === 'general') {
      for (const tr of D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]')) {
        const n = (tr.querySelector('.fp-playerName_f0veK') || {}).textContent; const fg = tr.querySelector('figure'); const imgs = tr.querySelectorAll('.wcl-photoContainer_llQ-a img');
        if (n) { const o = P[n.trim()] || (P[n.trim()] = {}); o.pid = fg ? fg.getAttribute('data-analytics-player-id') : null; o.logo = imgs.length > 1 ? imgs[imgs.length - 1].src.split('/').pop() : null; }
      }
    }
    const t = (D.querySelector('#detail') || D.body).innerText; const i = t.indexOf('TODOS'); if (i < 0) continue;
    const T = t.slice(i + 5).split('\n').map(s => s.trim()).filter(s => s); const j = T.findIndex(isV); if (j < 3) continue; const H = T.slice(0, j - 2), k = H.length; cols.push(nm + ':' + k);
    for (let x = j - 2; x + 2 + k <= T.length; x += 2 + k) { const name = T[x], pos = T[x + 1], vals = T.slice(x + 2, x + 2 + k); if (isV(name) || isV(pos) || !vals.every(isV)) break; const o = P[name] || (P[name] = {}); o.pos = pos; H.forEach((h, q) => { o[h] = vals[q]; }); }
  }
  f.remove();
  window.__PJ[mid] = { t: D.title, f: u.f, h: u.h, a: u.a, lh: u.lh, la: u.la, P, cols };
  return mid + ' ' + u.f + ' ' + u.h + '-' + u.a + ' ' + Object.keys(P).length + ' [' + cols.join(' ') + ']';
};
window.__worker = async function () { while (window.__queue.length) { const m = window.__queue.shift(); let r; try { r = await window.scrapeIframe(m, 0); } catch (e) { r = m + ' ERR ' + e.message; } window.__log.push(r); window.__done = (window.__done || 0) + 1; } };
window.__exportar = function (key) {
  const n0 = s => { if (s == null || s === '-' || s === '') return 0; const m = String(s).match(/^(\d+(?:\.\d+)?)/); return m ? m[1] : 0; };
  const pair = s => { if (s == null || s === '-' || s === '') return '0/0'; const m = String(s).match(/^(\d+)\/(\d+)/); if (m) return m[1] + '/' + m[2]; const q = String(s).match(/^\d+/); return q ? q[0] + '/' + q[0] : '0/0'; };
  const L = ['T|' + key]; const roster = {}; const rows = [];
  for (const [mid, pj] of Object.entries(window.__PJ)) {
    for (const [, v] of (window.__spec[mid] || []).filter(x => x[0] === key)) {
      const logo = v === 'L' ? pj.lh : pj.la;
      for (const [name, o] of Object.entries(pj.P)) {
        if (o.logo !== logo) continue; const min = n0(o['Minutos jugados']); if (!Number(min)) continue;
        roster[o.pid] = roster[o.pid] || [name, o.pos];
        rows.push([o.pid, mid, pj.f, min, n0(o['Goles']), n0(o['Asistencias']), n0(o['Remates totales']), n0(o['Remates a puerta']), pair(o['Entradas ganadas']), n0(o['Faltas cometidas']), n0(o['Paradas del arquero']), n0(o['Tarjetas amarillas']), n0(o['Tarjetas rojas']), o['Rating'] && o['Rating'] !== '-' ? o['Rating'] : '', n0(o['Goles esperados (xG)'])].join('|'));
      }
    }
  }
  for (const [pid, [nm, pos]] of Object.entries(roster)) L.push('R|' + pid + '|' + nm + '|' + pos);
  for (const r of rows) L.push('J|' + r);
  return L.join('\n');
};
