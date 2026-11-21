/* Mercados por partido en Betano (solo lectura). Se corre DENTRO de una pestaña de betano.co.
 *   (0,eval)(await (await fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/mercados_dia.js')).text());
 *   const cal = await leerCalendarioDia(1795237200000);        // ms de 00:00 Bogotá (= 05:00Z) del día → [{id,n,l,lid,r,t,m,u,br,lu}]
 *   const res = await leerMercadosPartidos(cal.slice(0,40));   // arranca en segundo plano; poll: window.__mkEstado()  → {hechos,total,err}
 *   window.__mkFamilias()                                      // → {id: {tot, leidos, j_remates, j_arco, ...}} cuando termine
 * `m` = totalMarketsAvailable que Betano anuncia en el calendario; «leidos» = mercados distintos que la API del partido entrega (la unión de las pestañas bt=2..9,13).
 * Calendario: sort=Leagues&pageSize=1000 devuelve TODOS los partidos del día (el orden por hora se corta en 1000). Hay que recorrer el JSON buscando objetos con totalMarketsAvailable + startTime.
 */
async function leerCalendarioDia(dayMs) {
  const url = `/api/sports/upcoming/calendar/FOOT/?timeZoneId=America/Bogota&day=${dayMs}&sort=Leagues&pageSize=1000`;
  const j = await (await fetch(url)).json();
  const out = [], vistos = new Set();
  (function rec(o) {
    if (!o || typeof o !== 'object') return;
    if (Array.isArray(o)) { o.forEach(rec); return; }
    if (o.totalMarketsAvailable != null && o.startTime != null && o.id != null) {
      if (!vistos.has(o.id)) { vistos.add(o.id);
        out.push({ id: String(o.id), n: o.name, l: o.leagueName, lid: o.leagueId, r: o.regionName, t: o.startTime,
          m: o.totalMarketsAvailable, u: o.url, br: o.betRadarId, lu: !!o.hasLineupsAvailability, live: !!o.willGoLive }); }
      return;
    }
    for (const k in o) rec(o[k]);
  })(j);
  return out;
}

function familiaMercado(n) {
  const mm = /m[aá]s\/menos|menos\/m[aá]s|mas\/menos|menos\/mas|m[aá]s|menos/i;
  const pref = re => { const m = n.match(re); return m && m.index > 0; };
  if (/h2h/i.test(n)) return 'h2h';
  if (/remates totales( - primer tiempo)?\s*$/i.test(n) && pref(/remates totales/i) && !mm.test(n)) return 'j_remates';
  if (/tiros al arco( - primer tiempo)?\s*$/i.test(n) && pref(/tiros al arco/i) && !mm.test(n)) return 'j_arco';
  if (/tackles totales\s*$/i.test(n) && pref(/tackles/i)) return 'j_entradas';
  if (/faltas (cometidas|ganadas|recibidas)\s*$/i.test(n) && pref(/faltas/i) && !mm.test(n)) return 'j_faltas';
  if (/asistencias totales\s*$/i.test(n)) return 'j_asist';
  if (/total de pases\s*$/i.test(n)) return 'j_pases';
  if (/fueras de juego\s*$/i.test(n) && pref(/fueras/i)) return 'j_fuera';
  if (/atajadas/i.test(n)) return 'atajadas';
  if (/anotar|anotador|anota |goleador|marcar|último en marcar|hat-trick|hat trick|palo|cabezazo|asistencia/i.test(n)) return 'goleador';
  if (/esquina/i.test(n)) return 'corners';
  if (/tarjeta/i.test(n)) return 'tarjetas';
  if (/cronometrad|por minuto|minuto|hora del|tiempo del primer|pr[oó]ximo gol|primer gol/i.test(n)) return 'minutos';
  if (/faltas|fuera de juego|fueras|saques? de (banda|meta)|saque/i.test(n)) return 'partido';
  if (/remates|tiros al arco|tiros a puerta/i.test(n)) return 'remates_eq';
  if (/goles|gol |ambos|marcador|puntuaci/i.test(n)) return 'goles';
  if (/resultado|doble oportunidad|h[aá]ndicap|empate|ganador|victoria|clasific|descanso|medio tiempo/i.test(n)) return 'resultado';
  return 'otros';
}

async function leerMercadosPartidos(lista, conc = 4) {
  window.__mk = {}; window.__mkErr = {}; window.__mkHechos = 0; window.__mkTotal = lista.length;
  const BTS = [2, 3, 4, 5, 6, 7, 8, 9, 13];
  let idx = 0;
  async function uno(p) {
    const slug = (p.u || '').split('/')[2], mp = new Map(); let tot = null;
    for (const bt of BTS) {
      try {
        const r = await fetch(`/api/cuotas-de-partido/${slug}/${p.id}/?bt=${bt}&req=s,stnf,c,mb`);
        if (!r.ok) { window.__mkErr[p.id + '_' + bt] = r.status; continue; }
        const e = (await r.json()).data.event; tot = e.totalMarketsAvailable;
        for (const m of (e.markets || [])) mp.set(m.id, m.name);
      } catch (x) { window.__mkErr[p.id + '_' + bt] = 'x'; }
    }
    window.__mk[p.id] = { tot, names: [...mp.values()] }; window.__mkHechos++;
  }
  async function w() { while (idx < lista.length) await uno(lista[idx++]); }
  window.__mkRun = Promise.all(Array.from({ length: conc }, w));
  return 'lanzado';
}
window.__mkEstado = () => ({ hechos: window.__mkHechos, total: window.__mkTotal, err: Object.keys(window.__mkErr || {}).length });
window.__mkFamilias = () => {
  const res = {};
  for (const [id, v] of Object.entries(window.__mk || {})) {
    const c = {}; for (const n of v.names) { const f = familiaMercado(n); c[f] = (c[f] || 0) + 1; }
    res[id] = { tot: v.tot, leidos: v.names.length, ...c };
  }
  return res;
};
