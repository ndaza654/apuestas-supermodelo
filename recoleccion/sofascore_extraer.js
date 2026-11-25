/* Sofascore → estadísticas de equipo, historial por jugador y árbitro, en el MISMO formato que flashscore/<clave>.json y jugadores/<clave>.json.
 * Se corre en una pestaña de https://www.sofascore.com (el navegador integrado pide request_access en cada uso). Rutas del MISMO sitio (/api/v1/...):
 * api.sofascore.com da 403. ≈0,1 s por llamada; ≈60–90 llamadas por partido (10 partidos × 2 equipos × estadísticas + once + incidentes, y 6 directos).
 *   window.__M = [[clave, 'Royale Union SG', 'Lech Poznan', '2026-11-26'], ...]      // clave de la jornada, nombres (Flashscore/Betano), fecha AAAA-MM-DD (Bogotá)
 *   (0,eval)(await (await fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/sofascore_extraer.js')).text());
 *   await sfCorrer(window.__M)           // ≈15–30 s por partido; resultado en window.__sf[clave]; progreso en window.__sfLog
 *   sfExportar()                         // JSON (string) para bajar con Blob + a.download → recoleccion/sofascore_decod.py
 * Si hay 403/429: se detiene (sfParar=true) y avisa; no insistir. Solo partidos oficiales terminados (se excluyen amistosos).
 * Estadísticas por partido (orientadas [equipo de referencia, rival]): c,sh,sot,f,off,ti,gk,xg,y + pos,xgot,big,blk,shi,sho,box,fk,cl,it,wd,sv,gp,es,eg,tp,tk/tkw,cr/crw,pas,lp/lpw,du,dsp,rec,r.
 * Fila de jugador (la más reciente primero): [mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas, entradas_ganadas, atajadas, entradas_total,
 *   faltas_recibidas, centros, xA, rating].   Faltas recibidas SÍ existen aquí (Flashscore no las trae). */
(function () {
  const W = window;
  W.__sf = W.__sf || {}; W.__sfLog = W.__sfLog || []; W.__sfCache = W.__sfCache || {}; W.sfParar = false;
  let ultima = 0;
  const pausa = ms => new Promise(r => setTimeout(r, ms));
  async function sfGet(ruta, intentos = 2) {
    for (let i = 0; i <= intentos; i++) {
      const espera = Math.max(0, 120 - (Date.now() - ultima)); ultima = Date.now() + espera; if (espera) await pausa(espera);
      if (W.sfParar) throw new Error('detenido');
      const r = await fetch('/api/v1' + ruta);
      if (r.status === 403 || r.status === 429) { W.sfParar = true; throw new Error('Sofascore HTTP ' + r.status + ' (bloqueo: parar)'); }
      if (r.status === 404) return null;
      if (r.ok) return r.json();
      await pausa(400 * (i + 1));
    }
    return null;
  }
  const quita = s => String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const STOP = new Set(['fc', 'cf', 'sc', 'ac', 'as', 'club', 'de', 'la', 'el', 'the', 'ca', 'cd', 'sd', 'ud', 'fk', 'sk', 'afc', 'rc', 'real', 'royale', 'atletico', 'athletic']);
  const toks = s => quita(s).replace(/[^a-z0-9 ]+/g, ' ').split(/\s+/).filter(t => t && !STOP.has(t));
  function sim(a, b) {                                   // 0..1: fracción de las palabras significativas (la más corta) contenidas en la otra (con prefijo de 4)
    const A = toks(a), B = toks(b); if (!A.length || !B.length) return 0;
    const [c, l] = A.length <= B.length ? [A, B] : [B, A];
    return c.filter(t => l.some(u => u === t || (t.length >= 4 && u.length >= 4 && (u.startsWith(t.slice(0, 4)) || t.startsWith(u.slice(0, 4)))))).length / c.length;
  }
  const dia = ts => new Date(ts * 1000 - 5 * 3600 * 1000).toISOString().slice(0, 10);   // fecha Bogotá
  const num = x => (x == null || x === '' || isNaN(+x)) ? null : +x;
  const ratio = t => { const m = String(t || '').match(/(\d+)\/(\d+)/); return m ? [+m[1], +m[2]] : null; };

  const MAP = { cornerKicks: 'c', totalShotsOnGoal: 'sh', shotsOnGoal: 'sot', fouls: 'f', offsides: 'off', throwIns: 'ti', goalKicks: 'gk', expectedGoals: 'xg', ballPossession: 'pos',
    expectedGoalsOnTarget: 'xgot', bigChanceCreated: 'big', blockedScoringAttempt: 'blk', totalShotsInsideBox: 'shi', totalShotsOutsideBox: 'sho', touchesInOppBox: 'box',
    freeKicks: 'fk', totalClearance: 'cl', interceptionWon: 'it', hitWoodwork: 'wd', goalkeeperSaves: 'sv', goalsPrevented: 'gp', errorsLeadToShot: 'es', errorsLeadToGoal: 'eg',
    accurateThroughBall: 'tp', totalTackle: 'tk', wonTacklePercent: 'tkw', accurateCross: 'crw', passes: 'pas', accurateLongBalls: 'lpw', dispossessed: 'dsp', ballRecovery: 'rec' };
  function periodo(p) {                                  // un periodo de /statistics → {clave:[local, visitante]}
    const o = {}, duelos = [0, 0]; let hayDuelos = false;
    for (const g of p.groups || []) for (const it of g.statisticsItems || []) {
      const h = num(it.homeValue), a = num(it.awayValue); if (h == null || a == null) continue;
      if (MAP[it.key] && !(it.key in o && MAP[it.key] in o)) o[MAP[it.key]] = [h, a];
      if (it.key === 'accurateCross') { const rh = ratio(it.home), ra = ratio(it.away); if (rh && ra) o.cr = [rh[1], ra[1]]; }
      if (it.key === 'accurateLongBalls') { const rh = ratio(it.home), ra = ratio(it.away); if (rh && ra) o.lp = [rh[1], ra[1]]; }
      if (it.key === 'groundDuelsPercentage' || it.key === 'aerialDuelsPercentage') { duelos[0] += h; duelos[1] += a; hayDuelos = true; }
      if (it.key === 'yellowCards') o._y = [h, a];
      if (it.key === 'redCards') o.r = [h, a];
    }
    if (hayDuelos) o.du = duelos;
    if (o._y) { const r = o.r || [0, 0]; o.y = [o._y[0] + 2 * r[0], o._y[1] + 2 * r[1]]; delete o._y; }
    return o;
  }
  const orienta = (o, esLocal) => { const r = {}; for (const k in o) r[k] = esLocal ? [o[k][0], o[k][1]] : [o[k][1], o[k][0]]; return r; };
  async function estadisticas(id) {                       // → {all, h1}  sin orientar (local, visitante del partido)
    const j = await sfGet('/event/' + id + '/statistics'); if (!j) return null;
    const por = {}; for (const p of j.statistics || []) por[p.period] = periodo(p);
    return { all: por.ALL || {}, h1: por['1ST'] || {} };
  }
  async function jugadoresPartido(ev, esLocal) {          // filas de jugadores del equipo de referencia en ese partido
    const [lu, inc] = await Promise.all([sfGet('/event/' + ev.id + '/lineups'), sfGet('/event/' + ev.id + '/incidents')]);
    if (!lu) return [];
    const am = {}, ro = {};
    for (const x of (inc && inc.incidents) || []) if (x.incidentType === 'card' && x.player) { const k = x.player.id; if (x.incidentClass === 'yellow') am[k] = (am[k] || 0) + 1; else if (x.incidentClass === 'red') ro[k] = (ro[k] || 0) + 1; else if (x.incidentClass === 'yellowRed') { am[k] = (am[k] || 0) + 1; ro[k] = (ro[k] || 0) + 1; } }
    const lado = esLocal ? lu.home : lu.away, out = [];
    for (const p of (lado && lado.players) || []) {
      const s = p.statistics || {}, mn = num(s.minutesPlayed); if (!mn) continue;
      const id = p.player.id;
      out.push({ pid: String(id), nombre: p.player.name, pos: p.position || (p.player.position) || '', fila: [String(ev.id), dia(ev.startTimestamp), mn, s.totalShots || 0, s.onTargetScoringAttempt || 0, s.goals || 0, s.goalAssist || 0,
        am[id] || 0, ro[id] || 0, s.fouls || 0, s.wonTackle || 0, s.saves || 0, s.totalTackle || 0, s.wasFouled || 0, s.totalCross || 0, +(s.expectedAssists || 0).toFixed(2), s.rating ? +(+s.rating).toFixed(2) : null] });
    }
    return out;
  }
  const oficial = e => e.status && e.status.type === 'finished' && !/friend|amistos/i.test(((e.tournament && e.tournament.name) || '') + ' ' + ((e.tournament && e.tournament.uniqueTournament && e.tournament.uniqueTournament.name) || ''));
  async function ultimos(teamId, n) {
    let ev = [];
    for (let pg = 0; pg < 3 && ev.length < n; pg++) {
      const j = await sfGet('/team/' + teamId + '/events/last/' + pg); if (!j) break;
      ev = ev.concat((j.events || []).filter(oficial)); if (!j.hasNextPage) break;
    }
    return ev.sort((a, b) => b.startTimestamp - a.startTimestamp).slice(0, n);
  }
  async function entrada(ev, teamId, nombreRival) {       // un partido pasado de un equipo → entrada de forma + filas de jugadores
    const esLocal = ev.homeTeam.id === teamId;
    const C = W.__sfCache[ev.id] || (W.__sfCache[ev.id] = {});
    if (!C.st) C.st = await estadisticas(ev.id) || { all: {}, h1: {} };
    const g = esLocal ? [ev.homeScore.current, ev.awayScore.current] : [ev.awayScore.current, ev.homeScore.current];
    return { e: { fecha: dia(ev.startTimestamp), rival: esLocal ? ev.awayTeam.name : ev.homeTeam.name, comp: (ev.tournament.uniqueTournament || ev.tournament).name, v: esLocal ? 'L' : 'V', mid: String(ev.id), g,
      stats: orienta(C.st.all, esLocal), stats_1t: orienta(C.st.h1, esLocal) }, esLocal };
  }
  async function buscarEvento(local, visita, fecha) {     // por equipo: búsqueda → próximos partidos → el que enfrenta al rival ese día (±1)
    const intentos = [[local, visita], [visita, local]];
    for (const [a, b] of intentos) {
      const q = (toks(a).join(' ') || a);
      const r = await sfGet('/search/all?q=' + encodeURIComponent(q) + '&page=0'); if (!r) continue;
      const equipos = (r.results || []).filter(x => x.type === 'team' && x.entity.sport && x.entity.sport.name === 'Football').map(x => x.entity).filter(t => sim(t.name, a) >= 0.5).slice(0, 4);
      for (const t of equipos) for (const dir of ['next', 'last']) {
        const j = await sfGet('/team/' + t.id + '/events/' + dir + '/0'); if (!j) continue;
        const f0 = Date.parse(fecha + 'T12:00:00-05:00') / 1000;
        const ev = (j.events || []).find(e => Math.abs(e.startTimestamp - f0) < 40 * 3600 && ((sim(e.homeTeam.name, local) >= 0.5 && sim(e.awayTeam.name, visita) >= 0.5) || (sim(e.homeTeam.name, visita) >= 0.5 && sim(e.awayTeam.name, local) >= 0.5)));
        if (ev) return ev;
      }
    }
    return null;
  }
  async function unPartido([clave, local, visita, fecha]) {
    const t0 = Date.now(), avisos = [];
    const ev = await buscarEvento(local, visita, fecha);
    if (!ev) { W.__sf[clave] = { clave, error: 'sin evento en Sofascore', local, visitante: visita, fecha }; return; }
    const det = await sfGet('/event/' + ev.id); const E = (det && det.event) || ev;
    const out = { clave, sofa_id: ev.id, mid: String(ev.id), local: ev.homeTeam.name, visitante: ev.awayTeam.name, fecha, n: 10, forma: { local: [], visitante: [] }, h2h: [], avisos, jugadores: { local: {}, visitante: {} },
      arbitro: null, arbitro_pais: null, arbitro_sofa: null, estadio: (E.venue && E.venue.name) || null, capacidad: (E.venue && E.venue.stadium && E.venue.stadium.capacity) || null, fuente: 'Sofascore /api/v1', leido: new Date().toISOString() };
    if (E.referee) { out.arbitro = E.referee.name; out.arbitro_pais = (E.referee.country && E.referee.country.name) || null; out.arbitro_sofa = { id: E.referee.id, partidos: E.referee.games, amarillas: E.referee.yellowCards, rojas: E.referee.redCards, doble_amarilla: E.referee.yellowRedCards }; }
    else avisos.push('árbitro no anunciado en Sofascore');
    const lu0 = await sfGet('/event/' + ev.id + '/lineups');      // once probable/oficial + ausentes (solo si Sofascore ya lo tiene)
    if (lu0 && lu0.home && (lu0.home.players || []).length) {
      const cut = l => ({ formacion: l.formation || null, xi: (l.players || []).filter(x => !x.substitute).map(x => [x.player.name, String(x.player.id), x.position || '']),
        banca: (l.players || []).filter(x => x.substitute).map(x => [x.player.name, String(x.player.id), x.position || '']),
        ausentes: (l.missingPlayers || []).map(m => [m.player.name, String(m.player.id), m.type, m.reason == null ? '' : String(m.reason)]) });
      out.alineacion = { confirmada: !!lu0.confirmed, local: cut(lu0.home), visitante: cut(lu0.away), leida: new Date().toISOString() };
    } else avisos.push('Sofascore aún no publica once ni ausentes');
    for (const [lado, team] of [['local', ev.homeTeam], ['visitante', ev.awayTeam]]) {
      const pasados = await ultimos(team.id, 10);
      if (pasados.length < 10) avisos.push(`${lado}: solo ${pasados.length} partidos oficiales terminados`);
      for (const pe of pasados) {
        const { e, esLocal } = await entrada(pe, team.id);
        out.forma[lado].push(e);
        if (!Object.keys(e.stats).length) avisos.push(`${lado}: sin estadísticas ${e.fecha} vs ${e.rival}`);
        const js = await jugadoresPartido(pe, esLocal);
        for (const j of js) { const R = out.jugadores[lado]; (R[j.nombre] = R[j.nombre] || { lado: lado === 'local' ? 'L' : 'V', pos: j.pos, pid: j.pid, p: [] }).p.push(j.fila); }
      }
    }
    const h = await sfGet('/event/' + ev.id + '/h2h/events');
    for (const pe of ((h && h.events) || []).filter(oficial).sort((a, b) => b.startTimestamp - a.startTimestamp).slice(0, 6)) {
      const C = W.__sfCache[pe.id] || (W.__sfCache[pe.id] = {}); if (!C.st) C.st = await estadisticas(pe.id) || { all: {}, h1: {} };
      const eLocal = pe.homeTeam.id === ev.homeTeam.id;       // orientado a [local_actual, visitante_actual]
      out.h2h.push({ fecha: dia(pe.startTimestamp), comp: (pe.tournament.uniqueTournament || pe.tournament).name, mid: String(pe.id),
        g: eLocal ? [pe.homeScore.current, pe.awayScore.current] : [pe.awayScore.current, pe.homeScore.current], stats: orienta(C.st.all, eLocal), stats_1t: orienta(C.st.h1, eLocal) });
    }
    for (const lado of ['local', 'visitante']) for (const n in out.jugadores[lado]) out.jugadores[lado][n].p.sort((a, b) => b[1] < a[1] ? -1 : 1);
    out.seg = Math.round((Date.now() - t0) / 100) / 10;
    W.__sf[clave] = out; W.__sfLog.push(`${clave}: ok ${out.seg}s · forma ${out.forma.local.length}/${out.forma.visitante.length} · h2h ${out.h2h.length} · jugadores ${Object.keys(out.jugadores.local).length}/${Object.keys(out.jugadores.visitante).length}`);
  }
  W.sfCorrer = async function (M, trabajadores = 2) {
    const cola = M.filter(m => !(W.__sf[m[0]] && !W.__sf[m[0]].error)).slice();
    await Promise.all(Array.from({ length: trabajadores }, async () => {
      while (cola.length && !W.sfParar) { const m = cola.shift(); try { await unPartido(m); } catch (e) { W.__sf[m[0]] = { clave: m[0], error: String(e.message || e) }; W.__sfLog.push(m[0] + ': ' + (e.message || e)); } }
    }));
    return W.__sfLog.slice(-M.length);
  };
  W.sfExportar = () => JSON.stringify({ generado: new Date().toISOString(), fuente: 'Sofascore /api/v1 (www.sofascore.com)', Q: W.__sf });
  W.sfBuscarEvento = buscarEvento; W.sfUnPartido = unPartido;
})();
