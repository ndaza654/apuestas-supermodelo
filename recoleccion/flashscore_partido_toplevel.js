/* Previa, alineaciones (probables/oficiales), bajas y tabla de UN partido futuro leídos en la PESTAÑA (navegación de nivel superior), no en iframes.
 * Por qué: con el panel del navegador oculto los iframes de Flashscore no renderizan (salen vacíos o con «filas 0»); la página de nivel superior sí (probado el 24-nov-2026: ~25 s por partido).
 * Uso por partido (3 pasos, uno por llamada porque navegar borra window):
 *   1) navigate a https://www.flashscore.com/match/football/<mid>/       (redirige a la URL completa)
 *   2) (0,eval)(await (await fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/flashscore_partido_toplevel.js')).text()); window.leerPartido().then(r => window.__ultimo = r);
 *   3) esperar ~25 s y leer window.__ultimo  → [mid, largo_previa, n_jugadores, largo_lineups, largo_tabla]; el resultado completo queda en window.__P[mid] y en localStorage('recp_<mid>').
 * Salida: {mid, url, hora, resumen (texto de la pestaña Resumen: «FLASHSCORE PREVIEW»), lu_texto, lu_anclas [{n,h,c,g}], formaciones ['fp-home… | ;Oblak;…','fp-away… | …'], st_texto (tabla), clic_lu, clic_st}.
 * La formación fp-home es el local y fp-away el visitante; el primero de cada una es el arquero. «Predicted lineups» o «Confirmed lineups» sale en lu_texto.
 * Cuidado: guardar/descargar lo leído ANTES de navegar a otra cosa o de recargar la pestaña (se pierde window). localStorage sobrevive. */
window.leerPartido = async function () {
  const sleep = m => new Promise(r => setTimeout(r, m));
  const until = async (fn, ms) => { const t = Date.now(); while (Date.now() - t < ms) { try { if (fn()) return true; } catch (e) {} await sleep(300); } return false; };
  const detail = () => (document.querySelector('#detail') || document.body).innerText;
  const mid = new URL(location.href).searchParams.get('mid');
  const out = { mid, url: location.pathname, hora: new Date().toISOString() };
  await until(() => /FLASHSCORE PREVIEW|MATCH INFORMATION|PREDICTED|SUMMARY/i.test(detail()), 12000);
  out.resumen = detail();
  const clic = h => { const a = [...document.querySelectorAll('a')].find(x => (x.getAttribute('href') || '').includes(h)); if (a) { a.click(); return true; } return false; };
  out.clic_lu = clic('summary/lineups/');
  await until(() => document.querySelectorAll('a[href*="/player/"]').length > 5 || /no lineups|not available/i.test(document.body.innerText), 12000);
  await sleep(1500);
  await until(() => [...document.querySelectorAll('[data-testid="wcl-headerSection-text"]')].some(x => /will not play/i.test(x.textContent)), 6000);
  out.lu_texto = detail();
  out.lu_anclas = [...document.querySelectorAll('a[href*="/player/"]')].map(a => ({ n: a.textContent.trim().slice(0, 40), h: a.getAttribute('href'), c: (a.closest('[class*="fp-"],[class*="lineup"],[class*="formation"]') || {}).className || '' }));
  out.formaciones = [...document.querySelectorAll('[class*="fp-formation_"]')].map(f => f.className.slice(0, 80) + ' | ' + [...f.querySelectorAll('a[href*="/player/"]')].map(a => a.textContent.trim()).join(';'));
  out.clic_st = clic('/standings/');
  await until(() => /PTS/.test(document.body.innerText), 15000);
  out.st_texto = detail();
  try { localStorage.setItem('recp_' + mid, JSON.stringify(out)); } catch (e) {}
  window.__P = window.__P || {}; window.__P[mid] = out;
  return [mid, out.resumen.length, out.lu_anclas.length, out.lu_texto.length, out.st_texto.length];
};
