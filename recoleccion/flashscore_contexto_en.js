/* Contexto de un partido FUTURO en Flashscore en inglés (www.flashscore.com): alineaciones (probables/oficiales), bajas, previa y tabla. Solo lectura.
 *   window.__CTX = {}; window.__LISTAC = [mid, ...]; (0,eval)(await (await fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/flashscore_contexto_en.js')).text());  window.ctxPar(2)
 *   progreso: Object.keys(window.__CTX).length ; resultado: window.__CTX[mid] = {url, lu:{grupos:[{h, L:[{n,pid,num,nota}], V:[…]}], texto}, st:{texto}} o {error}
 * `texto` = innerText de #detail (la previa de Flashscore y la explicación suelen estar ahí). Se interpreta en Python (recoleccion/contexto_en_decod.py), no aquí.
 * Un iframe por trabajador (id ctx<idx>); ~5–8 s por página. */
window.__CTX = window.__CTX || {}; window.__logC = window.__logC || [];
window.ctxEnP = async function (mid, idx) {
  idx = idx || 0;
  const sleep = m => new Promise(r => setTimeout(r, m));
  const until = async (fn, ms) => { const t = Date.now(); while (Date.now() - t < ms) { try { if (fn()) return true; } catch (e) {} await sleep(250); } return false; };
  let base = null;
  try { const r = await fetch('/match/football/' + mid + '/', { redirect: 'follow' }); const p = new URL(r.url).pathname; if (/\/match\/football\/.+-.+\/.+-.+\//.test(p)) base = p.replace(/\/(summary|standings|odds|h2h).*$/, '/'); } catch (e) {}
  if (!base) { window.__CTX[mid] = { error: 'sin url' }; return mid + ' sin url'; }
  const cargar = async url => {
    const fid = 'ctx' + idx; let f = document.getElementById(fid); if (f) f.remove();
    f = document.createElement('iframe'); f.id = fid; f.style.cssText = 'position:fixed;left:0;top:0;width:1300px;height:1000px;opacity:0.01;pointer-events:none;border:0;z-index:-1'; f.src = url; document.body.appendChild(f);
    await new Promise(r => { f.onload = r; setTimeout(r, 12000); });
    return f;
  };
  const out = { url: base };
  // alineaciones
  let f = await cargar('https://www.flashscore.com' + base + 'summary/lineups/?mid=' + mid);
  try {
    const D = f.contentDocument;
    await until(() => D.querySelectorAll('[data-testid="wcl-lineupsGroup"]').length > 0 || /No lineups|not available|no information/i.test((D.querySelector('#detail') || D.body).innerText), 9000);
    const grupos = [];
    for (const g of D.querySelectorAll('[data-testid="wcl-lineupsGroup"]')) {
      const h = ((g.querySelector('[data-testid="wcl-headerSection-text"]') || {}).textContent || '').trim();
      const sides = [...g.querySelectorAll('[class*="wcl-side_"]')];
      const leer = s => !s ? [] : [...s.querySelectorAll('[class*="wcl-participant_"]')].map(p => {
        const a = p.querySelector('a[href*="/player/"]'), nm = p.querySelector('[class*="wcl-name_"]'), num = p.querySelector('[class*="wcl-number_"]'), ds = p.querySelector('[class*="wcl-description_"]'), rol = p.querySelector('[class*="wcl-roles_"]');
        return { n: nm ? nm.textContent.trim() : null, pid: a ? a.getAttribute('href').split('/').filter(Boolean).pop() : null, num: num ? num.textContent.trim() : null, nota: ds ? ds.textContent.trim() : null, rol: rol ? rol.textContent.trim() : null };
      });
      grupos.push({ h, L: leer(sides[0]), V: leer(sides[1]) });
    }
    out.lu = { grupos, texto: ((D.querySelector('#detail') || D.body).innerText || '').slice(0, 6000), titulo: D.title };
  } catch (e) { out.lu = { error: String(e) }; }
  // tabla
  const hrefSt = (() => { try { const a = [...f.contentDocument.querySelectorAll('a')].find(x => /\/standings\//.test(x.getAttribute('href') || '')); return a ? a.getAttribute('href') : null; } catch (e) { return null; } })();
  f.remove();
  if (hrefSt) {
    f = await cargar('https://www.flashscore.com' + hrefSt.split('?')[0] + '?mid=' + mid);
    try { const D = f.contentDocument; await until(() => ((D.querySelector('#detail') || D.body).innerText || '').length > 400, 9000); out.st = { href: hrefSt, texto: ((D.querySelector('#detail') || D.body).innerText || '').slice(0, 6000) }; } catch (e) { out.st = { error: String(e) }; }
    f.remove();
  } else out.st = { error: 'sin enlace de tabla' };
  window.__CTX[mid] = out;
  return mid + ' lu=' + ((out.lu && out.lu.grupos) ? out.lu.grupos.length : 'x') + ' st=' + (out.st && out.st.texto ? out.st.texto.length : 'x');
};
window.ctxPar = function (n) {
  async function w(idx) { while (window.__LISTAC.length) { const m = window.__LISTAC.shift(); let r; try { r = await window.ctxEnP(m, idx); } catch (e) { r = m + ' ERR ' + e.message; } window.__logC.push(r); } }
  window.__runC = Promise.all(Array.from({ length: n }, (_, i) => w(i)));
  return 'lanzado ' + n;
};
