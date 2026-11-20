/* Historial por jugador (Flashscore en INGLÉS, www.flashscore.com): estadísticas de jugadores de partidos pasados, todas las columnas.
   Sirve cuando la pestaña está en www.flashscore.com (la versión en español está en flashscore_jugadores_iframe.js).
   Uso (pestaña en www.flashscore.com, solo lectura):
     window.__PJ = {}; window.__LISTA = [{mid, fecha, key}]   // key = '<partido>:<L|V>' del equipo del día
     await window.pjEn(mid)  -> window.__PJ[mid] = {url, h, a, lh, la, rows:{pid:{n,pos,eq:'H'|'A',v:{col:valor}}}, cols}
   La URL se arma desde /match/football/<mid>/ (redirige a la completa) y se abre `summary/player-stats/` en un iframe del mismo origen.
   Pestañas leídas: general (rating, minutos, goles, autogoles, asistencias, amarillas, rojas), shots (remates, a puerta, xG...),
   attack (faltas recibidas «Fouls suffered», fueras de juego, regates), defense (duelos, entradas ganadas «Tackles won», faltas cometidas...),
   goalkeeping (atajadas). Un partido a la vez (en paralelo los iframes no pintan la tabla). */
window.__PJ = window.__PJ || {};
window.pjEn = async function (mid) {
  const sleep = m => new Promise(r => setTimeout(r, m));
  const until = async (fn, ms) => { const t = Date.now(); while (Date.now() - t < ms) { try { if (fn()) return true; } catch (e) {} await sleep(250); } return false; };
  let f = document.getElementById('pjen'); if (f) f.remove();
  f = document.createElement('iframe'); f.id = 'pjen'; f.style.cssText = 'position:fixed;left:0;top:0;width:1300px;height:1000px;opacity:0.01;pointer-events:none;border:0;z-index:-1';
  f.src = 'https://www.flashscore.com/match/football/' + mid + '/'; document.body.appendChild(f);
  await new Promise(r => { f.onload = r; setTimeout(r, 12000); });
  let D; try { D = f.contentDocument; } catch (e) { return mid + ' bloqueado'; }
  await until(() => [...D.querySelectorAll('a')].some(a => /summary\/player-stats\//.test(a.getAttribute('href') || '')), 10000);
  const a0 = [...D.querySelectorAll('a')].find(a => /summary\/player-stats\//.test(a.getAttribute('href') || ''));
  if (!a0) { f.remove(); return mid + ' sin pestaña de jugadores'; }
  const base = a0.getAttribute('href').split('player-stats')[0] + 'player-stats/';
  f.src = 'https://www.flashscore.com' + base + '?mid=' + mid;
  await new Promise(r => { f.onload = r; setTimeout(r, 12000); });
  D = f.contentDocument;
  const ok = await until(() => D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length >= 8, 20000);
  if (!ok) { const n = D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length; f.remove(); return mid + ' sin tabla de jugadores (filas ' + n + ')'; }
  const logos = [...D.querySelectorAll('.participant__image')].map(i => i.src.split('/').pop());
  const names = [...D.querySelectorAll('.participant__participantName')].map(x => x.textContent.trim());
  const rows = {}; const cols = [];
  for (const nm of ['general', 'shots', 'attack', 'defense', 'goalkeeping']) {
    const l = D.querySelector('a[href*="player-stats/' + nm + '/"]'); if (!l) continue;
    const hb = [...D.querySelectorAll('th')].map(x => x.textContent.trim()).join(',');
    l.click(); await until(() => [...D.querySelectorAll('th')].map(x => x.textContent.trim()).join(',') !== hb && D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length >= 1, 7000); await sleep(500);
    const H = [...D.querySelectorAll('th')].map(x => x.textContent.trim()).filter(x => x); cols.push(nm + ':' + H.length);
    for (const tr of D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]')) {
      const fg = tr.querySelector('figure'); if (!fg) continue; const pid = fg.getAttribute('data-analytics-player-id'); if (!pid) continue;
      const imgs = tr.querySelectorAll('.wcl-photoContainer_llQ-a img'); const logo = imgs.length > 1 ? imgs[imgs.length - 1].src.split('/').pop() : null;
      const o = rows[pid] || (rows[pid] = { n: ((tr.querySelector('[class*="playerName"]') || {}).textContent || '').trim(), pos: ((tr.querySelector('[class*="position"]') || {}).textContent || '').trim(), eq: logo === logos[0] ? 'H' : logo === logos[1] ? 'A' : '?', v: {} });
      const tds = [...tr.querySelectorAll('td')].slice(1); H.forEach((h, i) => { if (tds[i]) o.v[h] = tds[i].textContent.trim(); });
    }
  }
  f.remove();
  window.__PJ[mid] = { url: f.src, h: names[0], a: names[1], rows, cols };
  return mid + ' ' + names[0] + '-' + names[1] + ' ' + Object.keys(rows).length + ' [' + cols.join(' ') + ']';
};
