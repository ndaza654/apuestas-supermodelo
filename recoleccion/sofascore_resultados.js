// Resultados de partidos terminados desde Sofascore (balance). Pegar en una pestaña de www.sofascore.com (request_access) con
//   window.__ids = {"<clave>": <sofa_id>, ...}   (sofa_id sale de jornadas/<día>/sofascore/<clave>.json)
// Guarda event + statistics + lineups + incidents en window.__RES y baja `sofa_resultados.json` (Blob a.download → Descargas →
// mover a Documents\Claude-Apuestas\recoleccion → device_stage_files). 19 partidos ≈ 1 min. Luego:
//   python3 recoleccion/sofascore_resultados_a_repo.py jornadas/AAAA-MM-DD <crudo.json>
(async () => {
  window.__RES = {}; window.__finRes = false;
  const g = async u => { try { const r = await fetch(u); return r.ok ? await r.json() : { err: r.status } } catch (e) { return { err: String(e) } } };
  const sl = ms => new Promise(r => setTimeout(r, ms));
  for (const [k, id] of Object.entries(window.__ids)) {
    const ev = await g('/api/v1/event/' + id); await sl(150);
    const st = await g('/api/v1/event/' + id + '/statistics'); await sl(150);
    const lu = await g('/api/v1/event/' + id + '/lineups'); await sl(150);
    const inc = await g('/api/v1/event/' + id + '/incidents'); await sl(150);
    window.__RES[k] = {
      ev: ev.event ? { status: ev.event.status, hs: ev.event.homeScore, as: ev.event.awayScore, h: ev.event.homeTeam.name, a: ev.event.awayTeam.name, ts: ev.event.startTimestamp } : ev,
      st: st.statistics || st,
      lu: lu.err ? lu : { h: (lu.home.players || []).map(p => ({ n: p.player.name, s: p.statistics, sub: p.substitute })), a: (lu.away.players || []).map(p => ({ n: p.player.name, s: p.statistics, sub: p.substitute })) },
      inc: inc.incidents ? inc.incidents.map(i => ({ t: i.incidentType, c: i.incidentClass, time: i.time, add: i.addedTime, tm: i.isHome, p: i.player && i.player.name, as: i.assist1 && i.assist1.name })) : inc
    };
  }
  window.__finRes = true;
  const b = new Blob([JSON.stringify(window.__RES)], { type: 'application/json' }), a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = 'sofa_resultados.json'; document.body.appendChild(a); a.click();
})();
