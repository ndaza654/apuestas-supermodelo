// Se pega en la consola de una pestaña de betano.co (cualquier página). Pide a Betano el precio REAL del Bet Builder de cada combo
// (POST /api/betslip/v3/mc-leg, sin sesión de apuesta: no coloca nada). Entrada: EVENT = id del evento, COMBOS = [[idSel, idSel, idSel], ...]
// (los ids salen de bb/cand_<clave>.json → `ids`). Devuelve [precio | null ...] en el mismo orden (null = Betano no deja combinarlo).
// Usar lotes de ~60 combos por llamada (el navegador corta a los 45 s).
(async (EVENT, COMBOS) => {
  const una = async ids => {
    try {
      const r = await fetch('/api/betslip/v3/mc-leg', { method: 'POST', headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ selectionIds: ids, legId: 'MC-' + EVENT, betslip: { hash: '', slipData: '', legs: [], bets: [], betslipTabId: 1, betslipTrackId: 'bb' }, eventId: String(EVENT), triggerPoint: { origin: 10, parentOrigin: 5 } }) });
      const j = await r.json(); const d = j.data;
      if (!d || (d.errors && d.errors.length) || !d.bets || !d.bets[0]) return null;
      return d.bets[0].odds;
    } catch (e) { return null; }
  };
  const out = new Array(COMBOS.length).fill(null);
  for (let i = 0; i < COMBOS.length; i += 6) {
    const lote = COMBOS.slice(i, i + 6);
    const r = await Promise.all(lote.map(una));
    r.forEach((v, k) => out[i + k] = v);
  }
  return out;
})
