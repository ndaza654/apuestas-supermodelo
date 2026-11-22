/* Betano → texto compacto (el que lee recoleccion/betano.py).
 *
 * Se ejecuta DENTRO de una pestaña de betano.co (el navegador integrado, con su sesión).
 *   const txt = await extraerBetano('italia-francia', '94654134');   // devuelve el texto compacto
 *   const lista = listarPartidos();                                  // [{slug,id,url}] de la página abierta
 *
 * Formato (una línea por bloque):
 *   E|local - visitante|inicio_utc|id|region|liga|n=<mercados>|leido=<ISO>
 *   L|<mercado>|<ambito>|<linea>:<mas>/<menos> ...        mercado ∈ goles corners tarjetas al_arco remates faltas fueras saques_meta saques_banda
 *                                                          ámbito ∈ total local visitante 1T 2T
 *   U|<TIPO>|nombre=cuota;...                              mercados únicos (resultado, doble oportunidad, ambos, htft, hándicap…)
 *   P|<jugador>|L|V|an=..|aoa=..|tj=..|as=1:c,2:c|sh=..|sot=..|tk=..|fc=..|sv=..
 *   R|<stat>|A o B=cuota;...                               parejas «cualquiera de los jugadores…»
 * Solo lee (fetch GET de la API pública de la propia página); no apuesta ni cambia nada.
 */
function listarPartidos() {
  const vistos = new Set(), out = [];
  for (const a of document.querySelectorAll('a[href*="/cuotas-de-partido/"]')) {
    const m = (a.getAttribute('href') || '').match(/cuotas-de-partido\/([^/]+)\/(\d+)/);
    if (m && !vistos.has(m[2])) { vistos.add(m[2]); out.push({ slug: m[1], id: m[2], url: `/cuotas-de-partido/${m[1]}/${m[2]}/` }); }
  }
  return out;
}

async function extraerBetano(slug, id) {
  // `bt` es el número de la pestaña de mercados de la página del partido; la pestaña «Todo» cambia de número según el partido
  // (14-nov: en Mirassol–Atlético-MG y Chapecoense–Vasco «Todo» es bt=13 y bt=12 es «Minutos»: 28 mercados de 806). Se parte de bt=12
  // y, si trae menos de la mitad de los mercados declarados (totalMarketsAvailable), se prueban otras pestañas y se queda la más completa.
  const leer = async bt => {
    const r = await fetch(`/api/cuotas-de-partido/${slug}/${id}/?bt=${bt}&req=s,stnf,c,mb`);
    if (!r.ok) throw new Error('Betano HTTP ' + r.status + ' (bt=' + bt + ')');
    return (await r.json()).data.event;
  };
  const nUnicos = e => new Set((e.markets || []).map(m => m.id)).size;
  // 22-nov: desde el 20-nov la pestaña «Todo» (bt=12/13) devuelve como máximo ~160–276 mercados y deja fuera los de jugador (remates, tackles, faltas,
  // asistencias, tarjeta, anota o asiste, atajadas) y parte de los de equipo; esos viven en las pestañas «Jugadores», «Estadísticas», «Hándicap»… (bt distinto según el partido).
  // Por eso se lee la UNIÓN de todas las pestañas (bt 0–15), sin repetir mercados por id (en Liverpool–United: 680 mercados frente a 28 de bt=12).
  let ev = await leer(12);
  // Un mismo mercado puede venir vacío en una pestaña y completo en otra: se queda con la copia que trae más selecciones / filas de tabla.
  const riqueza = m => (m.selections || []).length + (((m.tableLayout || {}).rows || []).reduce((a, rw) => a + (rw.groupSelections || []).reduce((b, g) => b + (g.selections || []).length, 0), 0));
  const unidos = new Map(); const meter = m => { const x = unidos.get(m.id); if (!x || riqueza(m) > riqueza(x)) unidos.set(m.id, m); };
  for (const m of (ev.markets || [])) meter(m);
  for (const bt of [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 0, 1]) {
    try { const e2 = await leer(bt); for (const m of (e2.markets || [])) meter(m); } catch (e) { /* una pestaña que no existe en ese partido no es error */ }
  }
  ev.markets = [...unidos.values()];
  const [P0, P1] = ev.participants, loc = P0.name, vis = P1.name;
  const norm = s => (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const nl = norm(loc), nv = norm(vis);
  const lado = (teamId, nombre) => String(teamId) === String(P0.id) ? 'L' : String(teamId) === String(P1.id) ? 'V'
    : (nombre && norm(nombre).includes(nl)) ? 'L' : (nombre && norm(nombre).includes(nv)) ? 'V' : null;
  const equipo = s => s === loc ? 'L' : s === vis ? 'V' : s;            // «Italia» → L, «Francia» → V
  const reemplazar = s => s.split(loc).join('L').split(vis).join('V');
  const dedup = new Map(); for (const m of ev.markets) if (!dedup.has(m.id)) dedup.set(m.id, m);
  const ms = [...dedup.values()];
  const num = x => (x == null ? '-' : String(Math.round(x * 1000) / 1000));

  // ---------- líneas Más/Menos ----------
  const EXCLUIR = /cronometrad|tackle|penal|roja|palo|^total de goles|extra|resultado|doble|ambos|medio tiempo| y mas|primer saque|primero|ultimo/;
  function clasificar(nombre) {
    const n = norm(nombre);
    if (EXCLUIR.test(n)) return null;
    const stat = /esquina/.test(n) ? 'corners' : /tarjeta/.test(n) ? 'tarjetas' : /tiros al arco/.test(n) ? 'al_arco'
      : /remates/.test(n) ? 'remates' : /faltas/.test(n) ? 'faltas' : /fueras/.test(n) ? 'fueras'
      : /saques? de meta/.test(n) ? 'saques_meta' : /saques? de banda/.test(n) ? 'saques_banda' : /goles/.test(n) ? 'goles' : null;
    if (!stat) return null;
    if (/asiatic/.test(n) && stat !== 'goles') return null;     // asiáticos: solo los de goles (cuartos de línea)
    const periodo = /primer tiempo/.test(n) ? '1T' : /segundo tiempo/.test(n) ? '2T' : null;
    const ini = n.startsWith(nl) ? 'local' : n.startsWith(nv) ? 'visitante' : null;
    const fin = n.endsWith(nl) || n.endsWith(nv);
    // «Goles en Primer Tiempo Italia» y «Primer Tiempo Japón Tiros de esquina» (equipo + tiempo): no son el total del tiempo.
    // 14-nov: FXH2/FYH2 («Primer Tiempo <equipo> Tiros de esquina») se colaban en corners|1T y ensuciaban las líneas 0.5 y 1.5.
    if ((fin || n.includes(nl) || n.includes(nv)) && periodo) return null;
    if (ini && periodo) return null;   // «Serbia … Primer/Segundo Tiempo»: no es la línea del equipo a partido completo (13-nov: Serbia tarjetas 1T 0.5 se colaba como 0.5 de partido)
    return { mercado: stat, ambito: ini || periodo || 'total' };
  }
  const lineas = new Map();                                             // clave mercado|ambito → Map(linea → {mas,menos})
  // 18-nov: en los partidos de Brasil (y otros) Betano ya no manda las líneas Más/Menos en `m.selections` sino en la tabla
  // (`m.tableLayout.rows[].groupSelections[].selections`, layoutType 6). Se lee de donde estén.
  const selsDe = m => (m.selections && m.selections.length) ? m.selections
    : ((m.tableLayout && m.tableLayout.rows) || []).flatMap(rw => (rw.groupSelections || []).flatMap(g => g.selections || []));
  for (const m of ms) {
    const c = clasificar(m.name); if (!c) continue;
    for (const s of selsDe(m)) {
      const mm = norm(s.name).match(/^(mas|menos)( de)? ([\d.]+)$/); if (!mm) continue;
      const clave = c.mercado + '|' + c.ambito, h = parseFloat(mm[3]);
      if (!lineas.has(clave)) lineas.set(clave, new Map());
      const f = lineas.get(clave); if (!f.has(h)) f.set(h, {});
      const lado = mm[1] === 'mas' ? 'mas' : 'menos';
      if (f.get(h)[lado] == null) f.get(h)[lado] = s.price;
    }
  }
  const L = [];
  for (const [clave, f] of lineas) {
    const [mer, amb] = clave.split('|');
    // se descartan las líneas con un lado < 1.03 (sin información: la casa ya da el resultado por hecho)
    const items = [...f.entries()].filter(([, v]) => !((v.mas != null && v.mas < 1.03) || (v.menos != null && v.menos < 1.03)))
      .sort((a, b) => a[0] - b[0]).map(([h, v]) => `${h}:${num(v.mas)}/${num(v.menos)}`);
    L.push(`L|${mer}|${amb}|${items.join(' ')}`);
  }

  // ---------- mercados únicos ----------
  const U = [], porTipo = t => ms.find(m => m.type === t);
  const lista = (m, f) => (m.selections || []).map(s => `${f(s)}=${num(s.price)}`).join(';');
  for (const t of ['MRES']) { const m = porTipo(t); if (m) U.push(`U|MRES|${lista(m, s => s.name)}`); }
  for (const t of ['DBLC', 'DNOB', 'H1RS', 'H2RS', 'HOFR', 'TWMC', 'NTYC', 'BTSC', '4151', '4152']) {
    const m = porTipo(t); if (m) U.push(`U|${t}|${lista(m, s => reemplazar(s.name).replace('Empate', 'Empate'))}`);
  }
  { // medio tiempo / tiempo completo: se ordena 1/1 1/X 1/2 X/1 X/X X/2 2/1 2/X 2/2
    const m = porTipo('HTFT');
    if (m) {
      const cod = x => x === loc ? '1' : x === vis ? '2' : 'X';
      const o = {}; for (const s of m.selections) { const [a, b] = s.name.split(' / '); o[cod(a) + '/' + cod(b)] = s.price; }
      const orden = ['1/1', '1/X', '1/2', 'X/1', 'X/X', 'X/2', '2/1', '2/X', '2/2'];
      if (orden.every(k => o[k] != null)) U.push('U|HTFT|' + orden.map(k => `${k}=${num(o[k])}`).join(';'));
    }
  }
  { // hándicap resultado del partido (tabla)
    const m = porTipo('FHMR');
    if (m && m.tableLayout) {
      const filas = m.tableLayout.rows.map(rw => (rw.groupSelections[0].selections || []).map(s => `${s.handicap}=${num(s.price)}`).join('/'));
      U.push('U|FHMR|' + filas.join(';'));
    }
  }
  { // hándicap asiático
    const m = porTipo('AHRF');
    if (m) U.push('U|AHRF|' + (m.selections || []).map(s => {
      const lado = String(s.teamId) === String(P0.id) ? 'L' : 'V';
      const t = s.name.replace(loc, '').replace(vis, '').trim();
      return `${lado} ${t}@${s.handicap}=${num(s.price)}`;
    }).join(';'));
  }

  // ---------- jugadores ----------
  const jug = new Map();                                                // nombre → {lado, campos}
  const J = (nombre, ld) => { if (!jug.has(nombre)) jug.set(nombre, { lado: ld, c: {} }); const j = jug.get(nombre); if (!j.lado && ld) j.lado = ld; return j; };
  const limpiar = (s, team) => { const e = ` (${team})`; return team && s.endsWith(e) ? s.slice(0, -e.length) : s.replace(/ \(.*$/, ''); };
  const nomSel = s => { const t = [loc, vis].find(x => s.name.endsWith(` (${x})`)); return { nombre: limpiar(s.name, t), ld: lado(s.teamId, t) }; };
  const ESC = { PALS: ['sh', 'Remates totales'], PLTA: ['tk', 'Tackles totales'], 1000679: ['fc', 'Faltas cometidas'], PALA: ['as', 'Asistencias totales'], 1000115: ['sv', 'Atajadas de Portero'], PLST: ['sot', 'Tiros al Arco'] };   // 22-nov: PLST también llega por jugador (pestaña «Jugadores»)
  for (const m of ms) {
    const e = ESC[m.type];
    if (e && m.playerId) {
      const nombre = m.name.replace(new RegExp(' ' + e[1] + '$', 'i'), '');
      const esc = selsDe(m).map(s => { const k = parseInt(s.name); return isNaN(k) ? null : `${k}:${num(s.price)}`; }).filter(Boolean);
      if (esc.length) J(nombre, lado(m.teamId, null)).c[e[0]] = esc.join(',');
    } else if (m.type === 'PLST' && m.tableLayout) {                    // tiros al arco por jugador (tabla)
      for (const rw of m.tableLayout.rows) {
        const ld = rw.groupId === String(P0.id) ? 'L' : rw.groupId === String(P1.id) ? 'V' : null;
        const esc = ((rw.groupSelections[0] || {}).selections || []).map(s => { const k = parseInt(s.name); return isNaN(k) ? null : `${k}:${num(s.price)}`; }).filter(Boolean);
        if (esc.length) J(rw.title, ld).c.sot = esc.join(',');
      }
    } else if (m.type === 'PSCR' && m.tableLayout) {                    // anota en cualquier momento (1.ª columna)
      for (const rw of m.tableLayout.rows) {
        const s = ((rw.groupSelections[0] || {}).selections || [])[0]; if (!s) continue;
        const ld = rw.groupId === String(P0.id) ? 'L' : rw.groupId === String(P1.id) ? 'V' : null;
        if (/^Sin Goles/i.test(rw.title)) continue;
        J(rw.title, ld).c.an = num(s.price);
      }
    } else if (m.type === '1000661' || m.type === 'PTRC') {
      for (const s of selsDe(m)) { const { nombre, ld } = nomSel(s); J(nombre, ld).c[m.type === 'PTRC' ? 'tj' : 'aoa'] = num(s.price); }
    }
  }
  const P = [];
  for (const [nombre, j] of jug) {
    if (!j.lado) continue;
    const campos = ['an', 'aoa', 'tj', 'as', 'sh', 'sot', 'tk', 'fc', 'sv'].filter(k => j.c[k] != null).map(k => `${k}=${j.c[k]}`);
    if (campos.length) P.push(`P|${nombre}|${j.lado}|${campos.join('|')}`);
  }

  // ---------- parejas ----------
  const PAR = { 1001133: 'anota', 1001134: 'asiste', 1001136: 'tarjeta', 1001137: 'anota_o_asiste' }, R = [];
  for (const m of ms) if (PAR[m.type]) R.push(`R|${PAR[m.type]}|${(m.selections || []).map(s => `${s.name}=${num(s.price)}`).join(';')}`);

  const ini = new Date(Number(ev.startTime) || ev.startTime).toISOString();
  const E = `E|${loc} - ${vis}|${ini}|${id}|${ev.regionName}|${ev.leagueName}|n=${ms.length}|leido=${new Date().toISOString()}`;
  return [E, ...L, ...U, ...P, ...R].join('\n');
}
if (typeof window !== 'undefined') { window.extraerBetano = extraerBetano; window.listarPartidos = listarPartidos; }
