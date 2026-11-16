/* node pruebas/backtest/tasas.js [salida.json]  ->  registro/tasas_historicas.json
   Tasa histórica de acierto por línea, para que recoleccion/analisis_jornada.py la use como factor de p.
   Cohorte = partidos donde el MENOR de los dos conteos (X de 10) es >= k, repartidos por tramo de colchón. Dos periodos: todo y desde 2019/20.
   Mismo motor que el informe del backtest (motor.js), verificado contra un cálculo independiente en Python. */
const fs = require('fs'), path = require('path');
const M = require('./motor.js');
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'datos.json'), 'utf8'));
const E = M.crear(D);
const NOM = { goles: 'goles', corners: 'corners', remates: 'remates', arco: 'al_arco', faltas: 'faltas', tarj: 'tarjetas' };
const RANGO = {   // [mínima, máxima] de las medias líneas a calcular, por mercado y ámbito
  goles: { total: [0.5, 6.5], equipo: [0.5, 4.5] }, corners: { total: [4.5, 16.5], equipo: [1.5, 9.5] }, remates: { total: [12.5, 36.5], equipo: [4.5, 20.5] },
  arco: { total: [3.5, 14.5], equipo: [1.5, 8.5] }, faltas: { total: [14.5, 34.5], equipo: [6.5, 20.5] }, tarj: { total: [0.5, 9.5], equipo: [0.5, 6.5] } };
const BANDAS = [-1e9, 0.5, 1, 1.5, 2, 3, 1e9];            // 6 tramos de colchón
const REC = 2019;
const F0 = { ligas: D.ligas.map(() => true), tDesde: 0, tHasta: 9999, equipo: -1, K: 0, quien: 'todas', nmin: 7, colMin: null, colMax: null, favMin: null, favMax: null, cuoMin: null, cuoMax: null };
const celdas = () => Array.from({ length: 11 }, () => new Array(6).fill(0));
const out = { meta: { fuente: D.fuente, partidos: E.n, ligas: D.ligas, N: 10, nmin: 7, desde_rec: REC, bandas_colchon: BANDAS.slice(1, -1), nota: 'cohorte = min(X local, X visitante) >= k de 10, por tramo de colchón; n = partidos, h = aciertos' }, t: {} };
let nk = 0;
for (const mk in NOM) for (const amb of ['total', 'local', 'visitante']) {
  const [a, b] = RANGO[mk][amb === 'total' ? 'total' : 'equipo'];
  for (let l = a; l <= b + 1e-9; l += 1) for (const lado of ['mas', 'menos']) {
    const r = E.analizar({ mk, amb, linea: l, lado, N: 10 }, F0);
    if (r.bn < 500) continue;
    const c = { todo: { n: celdas(), h: celdas() }, rec: { n: celdas(), h: celdas() } };
    for (const i of r.base) {
      const k = Math.min(r.xL[i], r.xV[i]), col = r.col[i]; let bi = 0; while (col >= BANDAS[bi + 1]) bi++;
      for (const per of (E.temp[i] >= REC ? ['todo', 'rec'] : ['todo'])) for (let kk = 0; kk <= k; kk++) { c[per].n[kk][bi]++; c[per].h[kk][bi] += r.hit[i]; }
    }
    out.t[`${NOM[mk]}|${amb}|${lado}|${l.toFixed(1)}`] = { todo: [c.todo.n, c.todo.h], rec: [c.rec.n, c.rec.h] }; nk++;
  }
}
const dst = process.argv[2] || path.join(__dirname, '..', '..', 'registro', 'tasas_historicas.json');
fs.writeFileSync(dst, JSON.stringify(out));
console.log(nk, 'líneas ->', dst, (fs.statSync(dst).size / 1e3).toFixed(0), 'KB');
