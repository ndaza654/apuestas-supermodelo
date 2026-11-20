/* Alineaciones probables/oficiales y bajas (Flashscore en INGLÉS, www.flashscore.com) leídas del DOM de la pestaña «Lineups» en un iframe del mismo origen.
   Uso (pestaña en www.flashscore.com, solo lectura; requiere window.espera de flashscore_jugadores_en.js o equivalente basado en MutationObserver):
     const r = await window.leerLU(mid, 'a');   // r = {mid, url, tipo:'Predicted lineups'|'Confirmed lineups', probables:{L:[{n,slug,pid}],V:[…]}, bajas:{L:[{n,pid,motivo}],V:[…]}}
   L = local (formación `fp-home`), V = visitante (`fp-away`); el primero de cada formación es el arquero. Sin pestaña → {sin_pestana:true}.
   La sección «Will not play» carga tarde: se espera hasta 30 s; si no aparece se da por «sin bajas publicadas».
   Después: python3 recoleccion/alineaciones_en_decod.py jornadas/AAAA-MM-DD <entrada.json> → alineaciones/<clave>.json (formato compacto de alineaciones/LEEME.md). */
window.espera = window.espera || ((D, cond, ms) => new Promise(res => { try { if (cond()) return res(true); } catch (e) {} let fin = false; const fn = ok => { if (fin) return; fin = true; try { mo.disconnect(); } catch (e) {} res(ok); }; const mo = new MutationObserver(() => { try { if (cond()) fn(true); } catch (e) {} }); try { mo.observe(D.documentElement, { subtree: true, childList: true, characterData: true, attributes: true }); } catch (e) { return res(false); } setTimeout(() => fn(false), ms); }));
window.leerLU = async function (mid, w) {
  const f = document.createElement('iframe'); f.id = 'lu' + w; f.style.cssText = 'position:fixed;left:0;top:0;width:1300px;height:1000px;opacity:0.01;border:0;z-index:-1'; document.body.appendChild(f);
  const carga = u => new Promise(r => { f.onload = () => r(true); setTimeout(() => r(false), 60000); f.src = u; });
  await carga('https://www.flashscore.com/match/football/' + mid + '/'); let D = f.contentDocument;
  await window.espera(D, () => [...D.querySelectorAll('a')].some(a => /summary\/lineups\//.test(a.getAttribute('href') || '')), 40000);
  const a0 = [...D.querySelectorAll('a')].find(a => /summary\/lineups\//.test(a.getAttribute('href') || '')); if (!a0) { f.remove(); return { mid, sin_pestana: true }; }
  await carga('https://www.flashscore.com' + a0.getAttribute('href').split('lineups')[0] + 'lineups/?mid=' + mid); D = f.contentDocument;
  await window.espera(D, () => D.querySelectorAll('[class*="fp-formation_"]').length >= 2 && D.querySelectorAll('a[href*="/player/"]').length > 20, 50000);
  await window.espera(D, () => [...D.querySelectorAll('[data-testid="wcl-headerSection-text"]')].some(x => /will not play/i.test(x.textContent)), 30000);
  const out = { mid, url: f.src, tipo: null, probables: { L: [], V: [] }, bajas: { L: [], V: [] } };
  const hd = [...D.querySelectorAll('[data-testid="wcl-headerSection-text"]')].map(x => x.textContent.trim()); out.cabeceras = hd; out.tipo = hd.find(x => /lineups/i.test(x)) || null;
  const lee = e => { const seen = new Set(), L = []; for (const a of e.querySelectorAll('a[href*="/player/"]')) { const p = a.getAttribute('href').split('/').filter(Boolean); const pid = p[2], slug = p[1]; if (seen.has(pid)) continue; const t = a.textContent.trim(); if (!t) continue; seen.add(pid); L.push({ n: t, slug, pid }); } return L; };
  const fm = [...D.querySelectorAll('[class*="fp-formation_"]')]; const home = fm.find(e => /fp-home/.test(e.className)), away = fm.find(e => /fp-away/.test(e.className));
  if (home) out.probables.L = lee(home); if (away) out.probables.V = lee(away);
  const h = [...D.querySelectorAll('[data-testid="wcl-headerSection-text"]')].find(x => /will not play/i.test(x.textContent));
  if (h) {
    let c = h; while (c && c.querySelectorAll('a[href*="/player/"]').length < 1 && c.parentElement) c = c.parentElement;
    const r0 = c.getBoundingClientRect(); const lines = c.innerText.split('\n').map(s => s.trim()).filter(Boolean); const seen = new Set();
    for (const a of c.querySelectorAll('a[href*="/player/"]')) {
      const p = a.getAttribute('href').split('/').filter(Boolean); if (seen.has(p[2])) continue; const t = a.textContent.trim(); if (!t) continue; seen.add(p[2]);
      const i = lines.indexOf(t); const side = a.getBoundingClientRect().left < r0.left + r0.width / 2 ? 'L' : 'V'; out.bajas[side].push({ n: t, pid: p[2], motivo: i >= 0 ? lines[i + 1] : '' });
    }
  }
  f.remove(); return out;
};
