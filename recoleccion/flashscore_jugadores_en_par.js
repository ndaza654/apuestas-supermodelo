/* Variante PARALELA de flashscore_jugadores_en.js (Flashscore en inglés, www.flashscore.com): lee el historial por jugador de un partido pasado.
   Diferencias: acepta un índice de iframe (idx) para varios trabajadores a la vez en la misma pestaña, y resuelve la URL con un fetch a /match/football/<mid>/
   (redirige a la URL completa) para cargar directamente la pestaña player-stats (1 carga de iframe en vez de 2).
   Uso: window.__PJ={}; window.__LISTA=[mids...]; window.__logP=[]; (0,eval)(...); window.pjPar(3)  → lanza 3 trabajadores; progreso: window.__PJ / window.__logP / window.__LISTA.length */
window.__PJ = window.__PJ || {}; window.__logP = window.__logP || [];
window.pjEnP = async function (mid, idx) {
  idx = idx || 0;
  const sleep = m => new Promise(r => setTimeout(r, m));
  const until = async (fn, ms) => { const t = Date.now(); while (Date.now() - t < ms) { try { if (fn()) return true; } catch (e) {} await sleep(250); } return false; };
  let base = null;
  try { const r = await fetch('/match/football/' + mid + '/', { redirect: 'follow' }); const p = new URL(r.url).pathname; if (/\/match\/football\/.+-.+\/.+-.+\//.test(p)) base = p.replace(/\/summary.*$/, '/') + 'summary/player-stats/'; } catch (e) {}
  if (!base) return mid + ' sin url';
  const fid = 'pjen' + idx; let f = document.getElementById(fid); if (f) f.remove();
  f = document.createElement('iframe'); f.id = fid; f.style.cssText = 'position:fixed;left:0;top:0;width:1300px;height:1000px;opacity:0.01;pointer-events:none;border:0;z-index:-1';
  f.src = 'https://www.flashscore.com' + base + '?mid=' + mid; document.body.appendChild(f);
  await new Promise(r => { f.onload = r; setTimeout(r, 12000); });
  let D; try { D = f.contentDocument; } catch (e) { f.remove(); return mid + ' bloqueado'; }
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

window.pjPar = function (n) {
  window.__done = window.__done || 0;
  async function w(idx) {
    while (window.__LISTA.length) {
      const m = window.__LISTA.shift(); let r;
      try { r = await window.pjEnP(m, idx); } catch (e) { r = m + ' ERR ' + e.message; }
      window.__logP.push(r); window.__done++;
    }
  }
  window.__run = Promise.all(Array.from({ length: n }, (_, i) => w(i)));
  return 'lanzado ' + n;
};
