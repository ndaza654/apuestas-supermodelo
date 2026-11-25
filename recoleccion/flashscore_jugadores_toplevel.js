/* Historial por jugador de UN partido pasado leído en la PESTAÑA (nivel superior), no en un iframe. Mismo formato que `flashscore_jugadores_en_par.js` (guarda `pjE_<mid>` en localStorage y en window.__PJ),
 * así que `jugadores_en_decod.py` y `cache_jugadores.py` lo leen igual.
 * Por qué: con el panel del navegador oculto los iframes de Flashscore salen vacíos («filas 0») o tardan minutos (Chrome estrangula los temporizadores de páginas ocultas); la página de nivel superior renderiza en ~10–20 s.
 * Uso (un partido): navigate a https://www.flashscore.com/match/football/<mid>/ ; luego
 *   (0,eval)(await (await fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/flashscore_jugadores_toplevel.js')).text()); await window.pjTop()
 *   → 'mid Local-Visitante N [general:8 shots:11 …]' o 'mid sin tabla de jugadores (filas n)'. Cabe en una llamada de javascript_exec (< 45 s).
 * Con browser_batch se encadenan varios partidos: [navigate, javascript_exec, navigate, javascript_exec…] en una sola llamada.
 * Para bajar todo lo leído (de CUALQUIER pestaña de www.flashscore.com, el localStorage es común): window.pjDescargar('pj_x.json') de flashscore_jugadores_en_par.js, o ver `pjTodo()` aquí. */
window.__PJ = window.__PJ || {};
window.pjTop = async function () {
  const sleep = m => new Promise(r => setTimeout(r, m));
  const until = async (fn, ms) => { const t = Date.now(); while (Date.now() - t < ms) { try { if (fn()) return true; } catch (e) {} await sleep(200); } return false; };
  const D = document; const mid = new URL(location.href).searchParams.get('mid');
  if (!mid) return 'sin mid en la URL';
  if (!/player-stats/.test(location.pathname)) {
    await until(() => [...D.querySelectorAll('a')].some(a => /player-stats/.test(a.getAttribute('href') || '')), 12000);
    const l0 = [...D.querySelectorAll('a')].find(a => /player-stats/.test(a.getAttribute('href') || '')); if (!l0) return mid + ' sin pestaña de jugadores';
    l0.click();
  }
  const ok = await until(() => D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length >= 8, 20000);
  if (!ok) return mid + ' sin tabla de jugadores (filas ' + D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length + ')';
  const logos = [...D.querySelectorAll('.participant__image')].map(i => i.src.split('/').pop());
  const names = [...D.querySelectorAll('.participant__participantName')].map(x => x.textContent.trim());
  const rows = {}; const cols = []; const TH = {};
  for (const nm of ['general', 'shots', 'attack', 'defense', 'goalkeeping']) {
    const l = D.querySelector('a[href*="player-stats/' + nm + '/"]'); if (!l) continue;
    const hb = [...D.querySelectorAll('th')].map(x => x.textContent.trim()).join(',');
    l.click(); await until(() => [...D.querySelectorAll('th')].map(x => x.textContent.trim()).join(',') !== hb && D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]').length >= 1, 6000); await sleep(400);
    const H = [...D.querySelectorAll('th')].map(x => x.textContent.trim()).filter(x => x); cols.push(nm + ':' + H.length); TH[nm] = [...D.querySelectorAll('th')].map(x => x.textContent.trim());
    for (const tr of D.querySelectorAll('tr[data-testid="wcl-tableBodyRow"]')) {
      const fg = tr.querySelector('figure'); if (!fg) continue; const pid = fg.getAttribute('data-analytics-player-id'); if (!pid) continue;
      const imgs = tr.querySelectorAll('.wcl-photoContainer_llQ-a img'); const logo = imgs.length > 1 ? imgs[imgs.length - 1].src.split('/').pop() : null;
      const o = rows[pid] || (rows[pid] = { n: ((tr.querySelector('[class*="playerName"]') || {}).textContent || '').trim(), pos: ((tr.querySelector('[class*="position"]') || {}).textContent || '').trim(), eq: logo === logos[0] ? 'H' : logo === logos[1] ? 'A' : '?', v: {} });
      const tds = [...tr.querySelectorAll('td')].slice(1); H.forEach((h, i) => { if (tds[i]) o.v[h] = tds[i].textContent.trim(); });
      (o.raw || (o.raw = {}))[nm] = [...tr.querySelectorAll('td')].map(x => x.textContent.trim());
    }
  }
  window.__PJ[mid] = { url: location.href, h: names[0], a: names[1], rows, cols, th: TH };
  try { localStorage.setItem('pjE_' + mid, JSON.stringify(window.__PJ[mid])); } catch (e) {}
  return mid + ' ' + names[0] + '-' + names[1] + ' ' + Object.keys(rows).length + ' [' + cols.join(' ') + ']';
};
/* pjTodo(nombre): baja un JSON {pj:{mid:…}} con TODO lo guardado en localStorage (pjE_*) — de cualquier pestaña de www.flashscore.com — y devuelve {n,len,h} (h = hash para verificar_hash.py). */
window.pjTodo = function (nombre) {
  const pj = {}; for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (/^pjE_/.test(k)) { try { pj[k.slice(4)] = JSON.parse(localStorage.getItem(k)); } catch (e) {} } }
  const s = JSON.stringify({ pj, log: [] }); let h = 0; for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0;
  const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([s], { type: 'application/json' })); a.download = nombre; document.body.appendChild(a); a.click(); a.remove();
  return { n: Object.keys(pj).length, len: s.length, h };
};
