/* Flashscore → JSON de contexto de un partido (últimos 10 de cada equipo con estadísticas, directos, árbitro, estadio).
 *
 * Se ejecuta DENTRO de una pestaña de flashscore.co (el navegador integrado). Solo lectura: pide al servidor de datos de la propia página
 * (global.flashscore.ninja, el mismo que usa la web) los datos que la página muestra. Con pausa entre llamadas para no saturar.
 *
 *   const lista = listarPartidosFlashscore();                       // [{mid, local, visitante, url}] de la portada abierta
 *   const ctx = await extraerFlashscore('8nErnE8t');                // contexto de un partido (mid = ?mid= de la URL)
 *
 * Salida (ctx):
 *   { mid, local, visitante, arbitro, arbitro_pais, estadio, capacidad, n,
 *     forma: { local: [partido…], visitante: [partido…] },         // más reciente primero
 *     h2h:   [partido…],                                           // estadísticas orientadas al local/visitante ACTUAL: [local_actual, visitante_actual]
 *     avisos: [..] }
 *   partido = { fecha:'AAAA-MM-DD', rival, comp, v:'L'|'V' (sede del equipo), mid, g:[a_favor,en_contra],
 *               stats:{ c, sh, sot, f, off, ti, gk, y, xg, + contexto 25-nov: pos, xgot, xa, big, blk, shi, sho, box, fk, du, cl, it, wd, hg, sv, xgotf, gp, es, eg, tp, r, cr/crw, tk/tkw, pas, lp, pf3 }  cada una [a_favor, en_contra]  (y = amarillas + 2·rojas, puntos de Betano),
 *               stats_1t:{ …mismas claves… } }
 * Solo partidos oficiales terminados (se excluyen amistosos). Si Flashscore no trae estadísticas de un partido, `stats` queda vacío y se avisa.
 */
const FS_FEED = 'https://global.flashscore.ninja/2/x/feed/';
const FS_HDR = { 'x-fsign': 'SW9D1eZo' };
const fsPausa = ms => new Promise(r => setTimeout(r, ms));
const fsRec = s => Object.fromEntries(s.split('¬').filter(x => x.includes('÷')).map(x => { const i = x.indexOf('÷'); return [x.slice(0, i), x.slice(i + 1)]; }));
async function fsGet(ruta) {
  const r = await fetch(FS_FEED + ruta, { headers: FS_HDR });
  if (r.status === 403 || r.status === 429) throw new Error('Flashscore HTTP ' + r.status + ' (bloqueo: parar y reintentar más tarde)');
  if (!r.ok) throw new Error('Flashscore HTTP ' + r.status);
  return r.text();
}
function listarPartidosFlashscore() {
  const vistos = new Set(), out = [];
  for (const a of document.querySelectorAll('a[href*="/partido/futbol/"]')) {
    const h = a.href, m = h.match(/\/partido\/futbol\/([^/]+)-[A-Za-z0-9]{8}\/([^/]+)-[A-Za-z0-9]{8}\/.*[?&]mid=([A-Za-z0-9]+)/);
    if (m && !vistos.has(m[3])) { vistos.add(m[3]); out.push({ mid: m[3], local: m[1], visitante: m[2], url: h }); }
  }
  return out;
}
const FS_STATS = { c: ['Corner kicks', 'Tiros de esquina'], sh: ['Total shots', 'Tiros totales'], sot: ['Shots on target', 'Tiros a puerta', 'Tiros al arco'],
  f: ['Fouls', 'Faltas'], off: ['Offsides', 'Fuera de juego', 'Fueras de juego'], ti: ['Throw ins', 'Saques de banda'], gk: ['Goal kicks', 'Saques de puerta', 'Saques de meta'],
  xg: ['Expected goals (xG)', 'Goles esperados (xG)'] };
// Desde el 25-nov-2026: datos de contexto por mercado (ver estrategias/datos_por_mercado.md). Números simples (se toma el primer número).
const FS_EXTRA = { pos: ['Ball possession', 'Posesión de balón'], xgot: ['xG on target (xGOT)'], xa: ['Expected assists (xA)'], big: ['Big chances', 'Ocasiones claras'],
  blk: ['Blocked shots', 'Tiros bloqueados'], shi: ['Shots inside the box', 'Tiros dentro del área'], sho: ['Shots outside the box', 'Tiros fuera del área'],
  box: ['Touches in opposition box', 'Toques en el área rival'], fk: ['Free kicks', 'Tiros libres'], du: ['Duels won', 'Duelos ganados'],
  cl: ['Clearances', 'Despejes'], it: ['Interceptions', 'Intercepciones'], wd: ['Hit the woodwork', 'Palos'], hg: ['Headed goals', 'Goles de cabeza'],
  sv: ['Goalkeeper saves', 'Paradas del portero', 'Atajadas'], xgotf: ['xGOT faced'], gp: ['Goals prevented'], es: ['Errors leading to shot'], eg: ['Errors leading to goal'],
  tp: ['Accurate through passes'], r: ['Red cards', 'Tarjetas rojas'] };
// Con formato «40% (6/15)»: se guardan intentos (clave) y acertados (clave + 'w'); para pases, sólo intentos.
const FS_RATIO = { cr: ['Crosses', 'Centros'], tk: ['Tackles', 'Entradas'], pas: ['Passes', 'Pases'], lp: ['Long passes', 'Pases largos'], pf3: ['Passes in final third', 'Pases en el último tercio'] };
const fsNum = s => { const m = String(s == null ? '' : s).match(/-?\d+(\.\d+)?/); return m ? parseFloat(m[0]) : null; };
const fsRatio = s => { const m = String(s == null ? '' : s).match(/\((\d+)\/(\d+)\)/); return m ? [parseInt(m[1], 10), parseInt(m[2], 10)] : null; };   // [acertados, intentos]
function fsParseStats(texto) {                               // { 'Match': {nombre:[h,a]}, '1st Half': {...}, ... }
  const per = {}; let p = null;
  for (const r of texto.split('~').map(fsRec)) { if (r.SE) { p = r.SE.toLowerCase(); per[p] = {}; } else if (r.SG && p) per[p][r.SG] = [r.SH, r.SI]; }
  return per;
}
function fsTomar(periodo) {                                  // → { c:[h,a], … , y:[h,a] }
  const o = {}; if (!periodo) return o;
  for (const [k, nombres] of Object.entries(FS_STATS)) {
    const n = nombres.find(x => periodo[x]); if (!n) continue;
    const h = fsNum(periodo[n][0]), a = fsNum(periodo[n][1]); if (h != null && a != null) o[k] = [h, a];
  }
  for (const [k, nombres] of Object.entries(FS_EXTRA)) {
    const n = nombres.find(x => periodo[x]); if (!n) continue;
    const h = fsNum(periodo[n][0]), a = fsNum(periodo[n][1]); if (h != null && a != null) o[k] = [h, a];
  }
  for (const [k, nombres] of Object.entries(FS_RATIO)) {
    const n = nombres.find(x => periodo[x]); if (!n) continue;
    const h = fsRatio(periodo[n][0]), a = fsRatio(periodo[n][1]); if (!h || !a) continue;
    o[k] = [h[1], a[1]]; if (k !== 'pas' && k !== 'lp' && k !== 'pf3') o[k + 'w'] = [h[0], a[0]];
  }
  const am = periodo['Yellow cards'] || periodo['Tarjetas amarillas'], ro = periodo['Red cards'] || periodo['Tarjetas rojas'];
  if (am) { const h = fsNum(am[0]), a = fsNum(am[1]); if (h != null && a != null) o.y = [h + 2 * (ro ? fsNum(ro[0]) || 0 : 0), a + 2 * (ro ? fsNum(ro[1]) || 0 : 0)]; }
  return o;
}
const fsLimpio = s => (s || '').replace(/^\*/, '').trim();
const fsFecha = ts => new Date(Number(ts) * 1000).toISOString().slice(0, 10);
const fsOficial = r => !/friend|amistos/i.test(r.KF || '') && /^\d+:\d+$/.test(r.KL || '') && Number(r.KC) * 1000 < Date.now();

async function extraerFlashscore(mid, opciones = {}) {
  const N = opciones.n || 10, NH2H = opciones.nH2H || 6, h2hAnos = opciones.h2hAnos == null ? 5 : opciones.h2hAnos, pausa = opciones.pausa == null ? 120 : opciones.pausa, avisos = [];
  const hh = (await fsGet('df_hh_1_' + mid)).split('~').map(fsRec).filter(r => Object.keys(r).length);
  // primer grupo («Overall»): últimos del local, últimos del visitante, directos
  const secs = []; let cur = null, grupos = 0;
  for (const r of hh) {
    if (r.KA) { grupos++; if (grupos > 1) break; continue; }
    if (r.KB) { cur = { titulo: r.KB, filas: [] }; secs.push(cur); } else if (cur && r.KP) cur.filas.push(r);
  }
  const sLocal = secs.find(s => /^Last matches:/i.test(s.titulo)), sVis = secs.filter(s => /^Last matches:/i.test(s.titulo))[1], sH2H = secs.find(s => /head-to-head/i.test(s.titulo));
  if (!sLocal || !sVis) throw new Error('Flashscore: sin «últimos partidos» para ' + mid);
  const local = sLocal.titulo.replace(/^Last matches:\s*/i, '').trim(), visitante = sVis.titulo.replace(/^Last matches:\s*/i, '').trim();
  let arbitro = null, arbitro_pais = null, estadio = null, capacidad = null;
  try {
    const sui = {}; let tipo = null;                      // pares MIT÷<tipo>¬MIV÷<valor>
    for (const campo of (await fsGet('df_sui_1_' + mid)).split('~')[0].split('¬')) {
      if (campo.startsWith('MIT÷')) tipo = campo.slice(4); else if (campo.startsWith('MIV÷') && tipo) { sui[tipo] = campo.slice(4); tipo = null; }
    }
    arbitro = sui.REF || null; arbitro_pais = sui.RCC || null; estadio = sui.VEN || null; capacidad = sui.CAP || null;
  } catch (e) { avisos.push('árbitro/estadio: ' + e.message); }
  await fsPausa(pausa);

  async function stats(r, equipoActualEsLocal) {
    // devuelve { stats, stats_1t } orientadas a [equipo_de_referencia, rival]
    const t = await fsGet('df_st_1_' + r.KP); await fsPausa(pausa);
    const per = fsParseStats(t);
    return { m: fsTomar(per['match']), p1: fsTomar(per['1st half'] || per['1.º tiempo'] || per['1er tiempo']) };
  }
  async function forma(sec, equipo) {
    const out = [];
    const filas = sec.filas.filter(fsOficial).sort((a, b) => Number(b.KC) - Number(a.KC)).slice(0, N);
    for (const r of filas) {
      const esLocal = fsLimpio(r.KJ) === equipo || fsLimpio(r.KJ).toLowerCase() === equipo.toLowerCase();
      const [gh, ga] = r.KL.split(':').map(Number);
      const { m, p1 } = await stats(r);
      const ori = o => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, esLocal ? [v[0], v[1]] : [v[1], v[0]]]));
      const e = { fecha: fsFecha(r.KC), rival: fsLimpio(esLocal ? r.KK : r.KJ), comp: r.KF, v: esLocal ? 'L' : 'V', mid: r.KP, g: esLocal ? [gh, ga] : [ga, gh], stats: ori(m), stats_1t: ori(p1) };
      if (!Object.keys(m).length) avisos.push(`sin estadísticas: ${equipo} ${e.fecha} vs ${e.rival} (${r.KF})`);
      out.push(e);
    }
    return out;
  }
  const fl = await forma(sLocal, local), fv = await forma(sVis, visitante);
  const directos = [];
  if (sH2H) {
    const corte = h2hAnos ? Date.now() / 1000 - h2hAnos * 365.25 * 86400 : 0;     // los directos más viejos no se cuentan
    const filas = sH2H.filas.filter(fsOficial).filter(r => Number(r.KC) >= corte).sort((a, b) => Number(b.KC) - Number(a.KC)).slice(0, NH2H);
    for (const r of filas) {
      const hLocal = fsLimpio(r.KJ).toLowerCase() === local.toLowerCase();       // ¿el local de aquel partido es el local de hoy?
      const [gh, ga] = r.KL.split(':').map(Number);
      const { m, p1 } = await stats(r);
      const ori = o => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, hLocal ? [v[0], v[1]] : [v[1], v[0]]]));
      directos.push({ fecha: fsFecha(r.KC), comp: r.KF, mid: r.KP, g: hLocal ? [gh, ga] : [ga, gh], stats: ori(m), stats_1t: ori(p1) });
    }
  }
  return { mid, local, visitante, arbitro, arbitro_pais, estadio, capacidad, n: N, forma: { local: fl, visitante: fv }, h2h: directos, avisos };
}
if (typeof window !== 'undefined') { window.extraerFlashscore = extraerFlashscore; window.listarPartidosFlashscore = listarPartidosFlashscore; }
