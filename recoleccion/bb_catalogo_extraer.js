// Se pega en la consola de betano.co. Baja el catálogo del Bet Builder (todos los mercados con cuotas frescas) de varios partidos.
// PARTIDOS = [[clave, slug, idEvento], ...]  →  guarda window.__cat (objeto) y devuelve {clave: nº de mercados}. Luego exportar con Blob (ver README).
(async (PARTIDOS) => {
  const compact = t => { const d = JSON.parse(t).data.event; return { id: d.id, name: d.name, start: d.startTime, leida: new Date().toISOString(), allowed: d.matchComboAllowedMarketTypes,
    m: d.markets.map(m => ({ i: m.id, n: m.name, t: m.typeId, h: m.handicap, s: m.selections.map(s => [s.id, s.name, s.price, s.handicap, s.fullName || '']), sc: (m.scorerSelections || []).length })) }; };
  window.__cat = {}; const n = {};
  for (const [k, slug, id] of PARTIDOS) {
    const r = await fetch(`/api/cuotas-de-partido/${slug}/betbuilder/${id}/?bt=10&req=s,stnf,c,mb`, { headers: { accept: 'application/json' } });
    window.__cat[k] = compact(await r.text()); n[k] = window.__cat[k].m.length;
  }
  return n;
})
