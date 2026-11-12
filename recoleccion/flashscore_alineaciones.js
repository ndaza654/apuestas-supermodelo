/* Flashscore → alineaciones probables y bajas de un partido (la previa de la pestaña «Alineaciones»).
 *
 * Se ejecuta en una pestaña de flashscore.co sobre la página del partido  …/<local>/<visitante>/resumen/alineaciones/?mid=<mid>
 * (o sobre un <iframe> del mismo origen ya cargado: leerLineups(iframe.contentDocument)).
 * Salida: { titulo, tipo:'Alineaciones probables'|…, probables:{L:[{n,num,pid,slug,gk}],V:[…]}, bajas:{L:[{n,pid,slug,motivo}],V:[…]} }
 * L = columna izquierda = local de la página. Sin alineaciones publicadas la función devuelve probables vacío (no se inventa nada).
 * Flashscore anuncia las oficiales ~1 h antes del inicio; antes son «probables».
 */
function leerLineups(doc) {
  const out = { titulo: doc.title, probables: { L: [], V: [] }, bajas: { L: [], V: [] }, tipo: null };
  for (const g of doc.querySelectorAll('[data-testid="wcl-lineupsGroup"]')) {
    const t = (g.querySelector('[data-testid="wcl-headerSection-text"]') || {}).textContent || '';
    const sides = [...g.querySelectorAll('.wcl-side_R64pI')];
    const leer = s => !s ? [] : [...s.querySelectorAll('.wcl-participant_YylQz')].map(p => {
      const a = p.querySelector('a[href*="/jugador/"]'), nm = p.querySelector('.wcl-name_ZggyJ'), num = p.querySelector('.wcl-number_lTBFk'),
        rol = p.querySelector('.wcl-roles_GB-m2'), desc = p.querySelector('.wcl-description_SpoaC');
      return { n: nm ? nm.textContent.trim() : null, num: num ? num.textContent.trim() : null, pid: a ? a.getAttribute('href').split('/').pop() : null,
        slug: a ? a.getAttribute('href').split('/')[2] : null, gk: !!(rol && /\(G\)/.test(rol.textContent)), motivo: desc ? desc.textContent.trim() : null };
    });
    const tl = t.toLowerCase();
    if (/probables|confirmadas|oficiales|titulares/.test(tl)) { out.tipo = t.trim(); out.probables.L = leer(sides[0]); out.probables.V = leer(sides[1]); }
    else if (/bajas/.test(tl)) { out.bajas.L = leer(sides[0]); out.bajas.V = leer(sides[1]); }
  }
  return out;
}
if (typeof window !== 'undefined') window.leerLineups = leerLineups;
