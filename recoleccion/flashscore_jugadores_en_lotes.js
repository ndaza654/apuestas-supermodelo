/* Lotes con respaldo para el historial por jugador (Flashscore inglés). Requiere flashscore_jugadores_en_par.js ya cargado en la pestaña de www.flashscore.com.
 *   window.__COLA = [mids…]  (jornadas/AAAA-MM-DD/flashscore/jugadores_cola.json)
 *   __lote(80)                   → lee los próximos 80 mids que no estén hechos ni fallidos (5 trabajadores); lo leído queda en localStorage (pjE_<mid>)
 *   __descargarLote('pj_x.json') → baja un JSON con lo leído, lo marca como hecho (pjDone) y libera localStorage (5 MB ≈ 150 partidos)
 * La pestaña se cae sola cada ~100 páginas («page load failed»): se navega de nuevo, se vuelve a cargar esto y se sigue; nada se pierde porque pjE_/pjDone/pjFail viven en localStorage.
 * Fallos («sin tabla de jugadores»: copas/ligas sin estadísticas en Flashscore) → pjFail: no se reintentan. */
window.__doneSet = new Set(JSON.parse(localStorage.getItem('pjDone') || '[]'));
window.__failSet = new Set(JSON.parse(localStorage.getItem('pjFail') || '[]'));
window.__anotarFallos = function () { for (const l of (window.__logP || [])) { if (!/ \d+ \[/.test(l)) window.__failSet.add(l.split(' ')[0]); } localStorage.setItem('pjFail', JSON.stringify([...window.__failSet])); return [...window.__failSet]; };
window.__descargarLote = function (nombre) {
  const r = window.pjDescargar(nombre);
  const ids = Object.keys(window.__PJ).concat(Object.keys(localStorage).filter(k => k.startsWith('pjE_')).map(k => k.slice(4)));
  ids.forEach(i => window.__doneSet.add(i)); localStorage.setItem('pjDone', JSON.stringify([...window.__doneSet]));
  Object.keys(localStorage).filter(k => k.startsWith('pjE_')).forEach(k => localStorage.removeItem(k)); window.__PJ = {};
  return r;
};
window.__lote = function (n) {
  window.__anotarFallos();
  window.__LISTA = window.__COLA.filter(m => !window.__doneSet.has(m) && !window.__failSet.has(m) && !localStorage.getItem('pjE_' + m)).slice(0, n);
  window.__logP = []; window.__done = 0; window.__t0 = Date.now();
  document.querySelectorAll('iframe').forEach(f => f.remove());
  return window.pjPar(5);
};
