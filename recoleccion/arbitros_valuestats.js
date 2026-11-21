/* Árbitros en ValueStats (solo lectura). Se corre en una pestaña de valuestats.com (hay que dar request_access una vez).
 *   window.__R = [[clave, 'Madley A.', 'Eng'], ...]   // de flashscore/<clave>.json: arbitro y arbitro_pais (código de 3 letras de Flashscore)
 *   (0,eval)(await (await fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/arbitros_valuestats.js')).text());  → lanza 2 trabajadores
 *   progreso: Object.keys(window.__ref).length ; resultado: window.__ref[clave] = {arbitro, pais, vs, vs_nombre, pj_vs, otros, temporada, faq, leido} o {error}
 * Búsqueda /en/referees?name=<apellido>; se elige por país + inicial + apellido (el de más partidos). `temporada` = tabla «Statistics by Season»; `faq` = muestra de los últimos 20 (amarillas, rojas, penales, % de superar 3,5/4,5/5,5). */
(function () {
  const CP = { Ger: 'Germany', Eng: 'England', Arg: 'Argentina', Fra: 'France', Sco: 'Scotland', Rou: 'Romania', Bra: 'Brazil', Uru: 'Uruguay', Ita: 'Italy', Esp: 'Spain', Gre: 'Greece', Col: 'Colombia', Por: 'Portugal', Ned: 'Netherlands', Bel: 'Belgium', Tur: 'Turkey', Mex: 'Mexico', Usa: 'United States', Chi: 'Chile', Cze: 'Czech Republic', Pol: 'Poland', Aut: 'Austria', Sui: 'Switzerland', Cro: 'Croatia', Hun: 'Hungary', Den: 'Denmark', Swe: 'Sweden', Nor: 'Norway' };
  const PAISES = Object.values(CP).sort((a, b) => b.length - a.length);
  const norm = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  window.__ref = window.__ref || {};
  async function uno([slug, nom, pa]) {
    const parts = nom.split(' '), ap = []; for (const p of parts) { if (/^[A-Z]\.?$/.test(p)) break; ap.push(p); }
    const apellido = ap.join(' '), ini = (nom.slice(apellido.length).trim()[0] || '').toLowerCase();
    let h = await (await fetch('/en/referees?name=' + encodeURIComponent(ap.find(w => w.length > 3) || ap[0]))).text(); let d = new DOMParser().parseFromString(h, 'text/html');
    if (!d.querySelector('a[href*="/en/referee/"]') && ap[0].length > 4) { h = await (await fetch('/en/referees?name=' + encodeURIComponent(norm(ap[0]).slice(0, 4)))).text(); d = new DOMParser().parseFromString(h, 'text/html'); }   // ñ, tildes: Baliño, Echavarría
    const cand = [], seen = new Set();
    for (const a of d.querySelectorAll('a[href*="/en/referee/"]')) {
      const hr = a.getAttribute('href'); if (seen.has(hr)) continue;
      const tx = (a.closest('tr,li,div') || a).textContent.replace(/\s+/g, ' ').trim(); if (/Calculated from|View profile/.test(tx)) continue; seen.add(hr);
      const m = tx.match(/^(.*?) (\d+) PJ/); const pj = m ? +m[2] : 0; let rest = m ? m[1] : tx, pais = null;
      for (const p of PAISES) if (rest.endsWith(' ' + p)) { pais = p; rest = rest.slice(0, -p.length - 1); break; }
      cand.push({ hr, tx, pj, pais, nm: rest });
    }
    let c = cand.filter(x => x.pais === CP[pa] && ap.some(w => norm(x.nm).includes(norm(w).slice(0, 5))));
    const ci = c.filter(x => ini && (norm(x.nm).replace(/[^a-z ]/g, '').split(' ')[0] || '')[0] === ini);   // inicial del primer nombre if (ci.length) c = ci;
    c.sort((x, y) => y.pj - x.pj);
    if (!c.length) { window.__ref[slug] = { arbitro: nom, error: 'sin candidato', cand: cand.slice(0, 4).map(x => x.tx) }; return; }
    const hr = c[0].hr; const pg = await (await fetch(hr)).text(); const dd = new DOMParser().parseFromString(pg, 'text/html'); dd.querySelectorAll('script,style,noscript').forEach(x => x.remove());
    const t = dd.body.textContent.replace(/[ \t\r]+/g, ' ').replace(/\n\s*\n+/g, '\n'); const i1 = t.indexOf('Statistics by Season'), i2 = t.indexOf('Frequently');
    window.__ref[slug] = { arbitro: nom, pais: pa, vs: hr, vs_nombre: c[0].nm, pj_vs: c[0].pj, otros: c.slice(1, 3).map(x => x.tx), temporada: i1 >= 0 ? t.slice(i1, i1 + 3500) : null, faq: i2 >= 0 ? t.slice(i2, i2 + 1900) : null, leido: new Date().toISOString() };
  }
  let k = 0;
  async function w() { while (k < window.__R.length) { const r = window.__R[k++]; try { await uno(r); } catch (e) { window.__ref[r[0]] = { arbitro: r[1], error: String(e) }; } await new Promise(x => setTimeout(x, 250)); } }
  window.__refRun = Promise.all([w(), w()]);
})();
