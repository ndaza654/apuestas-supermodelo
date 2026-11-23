/* Ratings por rival (propuesta aprobada 23-nov-2026). Se corre en una pestaña de flashscore (usa los mismos feeds que flashscore_extraer.js: cárgalo antes).
 * ratingsRivales(mids, {pausa, conc}) — mids = ids de partidos YA JUGADOS de los equipos de interés (los de la ficha).
 * Para cada uno pide df_hh (los últimos de los dos equipos) y df_st de cada partido (estadísticas, ~0,1 s). Devuelve
 * { equipos: { <nombre>: [ [fecha, v(L/V), comp, gf, gc, mid, {c:[fav,cont], sh:…, sot:…, f:…, off:…, y:…}] ] }, errores:[…] }
 * Resultado en window.__rat y localStorage 'rat_<día>' (corre en segundo plano: el javascript_tool corta a ~45 s). */
async function ratingsRivales(mids, opts = {}) {
  const pausa = opts.pausa == null ? 40 : opts.pausa, N = opts.n || 10, out = { equipos: {}, errores: [], t0: Date.now() }, cache = {};
  const per = async id => cache[id] || (cache[id] = (async () => { const t = await fsGet('df_st_1_' + id); await fsPausa(pausa); const p = fsParseStats(t); return fsTomar(p['match']); })());
  async function equipo(sec) {
    const nombre = sec.titulo.replace(/^Last matches:\s*/i, '').trim();
    if (out.equipos[nombre]) return;
    out.equipos[nombre] = [];
    const filas = sec.filas.filter(fsOficial).sort((a, b) => Number(b.KC) - Number(a.KC)).slice(0, N);
    const res = await Promise.all(filas.map(async r => { try { return [r, await per(r.KP)]; } catch (e) { out.errores.push(r.KP + ': ' + e.message); return [r, null]; } }));
    for (const [r, m] of res) {
      const esL = fsLimpio(r.KJ).toLowerCase() === nombre.toLowerCase(), [gh, ga] = r.KL.split(':').map(Number);
      const st = m ? Object.fromEntries(Object.entries(m).map(([k, v]) => [k, esL ? [v[0], v[1]] : [v[1], v[0]]])) : null;
      out.equipos[nombre].push([fsFecha(r.KC), esL ? 'L' : 'V', r.KF, esL ? gh : ga, esL ? ga : gh, r.KP, st, fsLimpio(esL ? r.KK : r.KJ)]);
    }
  }
  for (const mid of mids) {
    try {
      const hh = (await fsGet('df_hh_1_' + mid)).split('~').map(fsRec).filter(r => Object.keys(r).length); await fsPausa(pausa);
      const secs = []; let cur = null, g = 0;
      for (const r of hh) { if (r.KA) { g++; if (g > 1) break; continue; } if (r.KB) { cur = { titulo: r.KB, filas: [] }; secs.push(cur); } else if (cur && r.KP) cur.filas.push(r); }
      for (const s of secs.filter(s => /^Last matches:/i.test(s.titulo)).slice(0, 2)) await equipo(s);
    } catch (e) { out.errores.push(mid + ': ' + e.message); }
    window.__rat_prog = Object.keys(out.equipos).length + ' equipos, ' + Object.keys(cache).length + ' partidos';
  }
  out.seg = (Date.now() - out.t0) / 1000; window.__rat = out; return out;
}
if (typeof window !== 'undefined') window.ratingsRivales = ratingsRivales;
