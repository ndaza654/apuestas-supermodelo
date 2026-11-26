// Foto en vivo de los partidos de Europa/Conference League desde una pestaña de sofascore.com.
// Uso: pegar en la pestaña de Sofascore (mismo origen: /api/v1/...). Devuelve JSON compacto (string).
(async () => {
  const j = async (u) => { const r = await fetch(u); if (!r.ok) return null; return r.json().catch(() => null); };
  const live = await j('/api/v1/sport/football/events/live');
  const now = Math.floor(Date.now() / 1000);
  const evs = ((live && live.events) || []).filter(e => /UEFA (Europa|Conference) League/i.test((e.tournament && e.tournament.name) || ''));
  const K = { cornerKicks: 'co', totalShotsOnGoal: 'sh', shotsOnGoal: 'sot', yellowCards: 'yc', redCards: 'rc', fouls: 'fo', offsides: 'off', ballPossession: 'pos', bigChanceCreated: 'bc', expectedGoals: 'xg' };
  const out = [];
  for (const e of evs) {
    const s = await j('/api/v1/event/' + e.id + '/statistics');
    const per = {};
    for (const p of ((s && s.statistics) || [])) {
      const o = {};
      for (const g of p.groups) for (const i of g.statisticsItems) if (K[i.key]) o[K[i.key]] = [Number(i.homeValue), Number(i.awayValue)];
      per[p.period] = o;
    }
    const t = e.time || {};
    const cur = (e.status && e.status.description) || '';
    let min = null;
    if (t.currentPeriodStartTimestamp) {
      const el = Math.floor((now - t.currentPeriodStartTimestamp) / 60);
      min = /2nd/i.test(cur) ? 45 + el : /1st/i.test(cur) ? el : null;
    }
    out.push({ id: e.id, h: e.homeTeam.name, a: e.awayTeam.name, g: [(e.homeScore || {}).current ?? 0, (e.awayScore || {}).current ?? 0], st: cur, min, per });
    await new Promise(r => setTimeout(r, 150));
  }
  return JSON.stringify({ t: now, n: out.length, ev: out });
})()
