/* node pruebas/backtest/hallazgos.js  -> imprime las tablas de las que salen los hallazgos (y hallazgos.json) */
const fs = require('fs'), path = require('path');
const M = require('./motor.js');
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'datos.json'), 'utf8'));
const E = M.crear(D);
const F0 = () => ({ ligas: D.ligas.map(() => true), tDesde: 0, tHasta: 9999, equipo: -1, K: 7, quien: 'ambos', nmin: 7, colMin: null, colMax: null, favMin: null, favMax: null, cuoMin: null, cuoMax: null });
const pc = (h, n) => n ? (100 * h / n).toFixed(1) : '  - ';
const out = { maestro: [] };
console.log('partidos', E.n, 'temporadas', E.tMin, E.tMax);
console.log('\n== MAESTRO (7 de 10 en ambos; n filtro >= 300) ==\nmercado amb linea lado | n_f %f | n_b %b | dif | frec%');
for (const mk in M.MERCADOS) for (const amb of ['total', 'local', 'visitante']) {
  const ls = amb === 'total' ? M.MERCADOS[mk].total : M.MERCADOS[mk].equipo;
  for (const linea of ls) for (const lado of ['mas', 'menos']) {
    const r = E.analizar({ mk, amb, linea, lado, N: 10 }, F0());
    const row = { mk, amb, linea, lado, sn: r.sn, sh: r.sh, bn: r.bn, bh: r.bh };
    out.maestro.push(row);
    if (r.sn >= 300) console.log(mk, amb, linea, lado, '|', r.sn, pc(r.sh, r.sn), '|', r.bn, pc(r.bh, r.bn), '|', (100 * (r.sh / r.sn - r.bh / r.bn)).toFixed(1), '|', pc(r.sn, r.bn));
  }
}
const CLAVE = [['corners', 'total', 8.5, 'mas'], ['corners', 'total', 9.5, 'mas'], ['corners', 'total', 10.5, 'menos'], ['goles', 'total', 1.5, 'mas'], ['goles', 'total', 2.5, 'mas'], ['goles', 'total', 3.5, 'menos'],
  ['remates', 'total', 22.5, 'mas'], ['arco', 'total', 7.5, 'mas'], ['faltas', 'total', 24.5, 'mas'], ['tarj', 'total', 3.5, 'mas'], ['tarj', 'total', 5.5, 'menos'], ['corners', 'local', 4.5, 'mas'], ['btts', 'total', 0.5, 'mas']];
console.log('\n== K (ambos >= K de 10): n %  ==');
for (const [mk, amb, linea, lado] of CLAVE) {
  let s = [mk, amb, linea, lado].join(' ') + ' | base ';
  for (const K of [0, 5, 6, 7, 8, 9, 10]) { const f = F0(); f.K = K; const r = E.analizar({ mk, amb, linea, lado, N: 10 }, f); if (K === 0) s += pc(r.bh, r.bn); s += ` | K${K}: ${pc(r.sh, r.sn)} (${r.sn})`; }
  console.log(s);
}
console.log('\n== Periodos (cumple vs base) ==');
for (const [mk, amb, linea, lado] of CLAVE) {
  let s = [mk, amb, linea, lado].join(' ');
  for (const [d, h] of [[2000, 2011], [2012, 2018], [2019, 2022], [2023, 2026]]) { const f = F0(); f.tDesde = d; f.tHasta = h; const r = E.analizar({ mk, amb, linea, lado, N: 10 }, f); s += ` | ${d}-${h}: ${pc(r.sh, r.sn)} (${r.sn}) vs ${pc(r.bh, r.bn)}`; }
  console.log(s);
}
console.log('\n== Mismo colchon: cumple vs no cumple (tercios del colchon en la base) ==');
for (const [mk, amb, linea, lado] of CLAVE) {
  const r = E.analizar({ mk, amb, linea, lado, N: 10 }, F0());
  const cs = Array.from(r.base, i => r.col[i]).sort((a, b) => a - b), q = p => cs[Math.floor(p * (cs.length - 1))];
  const cortes = [q(.5), q(.7), q(.85), q(.95)];
  let s = [mk, amb, linea, lado].join(' ');
  for (let b = 0; b <= cortes.length; b++) {
    const lo = b ? cortes[b - 1] : -1e9, hi = b < cortes.length ? cortes[b] : 1e9; let cn = 0, ch = 0, nn = 0, nh = 0;
    for (const i of r.base) { const c = r.col[i]; if (c < lo || c >= hi) continue; if (r.sel[i]) { cn++; ch += r.hit[i]; } else { nn++; nh += r.hit[i]; } }
    s += ` | col ${b ? lo.toFixed(1) : '-inf'}..${b < cortes.length ? hi.toFixed(1) : 'inf'}: SI ${pc(ch, cn)} (${cn}) NO ${pc(nh, nn)} (${nn})`;
  }
  console.log(s);
}
console.log('\n== Goles 2.5 contra el mercado (p sin margen) ==');
for (const lado of ['mas', 'menos']) for (const K of [0, 6, 7, 8, 9]) {
  const f = F0(); f.K = K; const r = E.analizar({ mk: 'goles', amb: 'total', linea: 2.5, lado, N: 10 }, f);
  let sn = 0, sh = 0, pm = 0; for (const i of r.base) if (r.sel[i] && E.O.o25[i] && E.O.u25[i]) { sn++; sh += r.hit[i]; const o = lado === 'mas' ? E.O.o25[i] : E.O.u25[i], u = lado === 'mas' ? E.O.u25[i] : E.O.o25[i]; pm += (1 / o) / (1 / o + 1 / u); }
  console.log('goles 2.5', lado, 'K' + K, 'n', sn, 'real', pc(sh, sn), 'mercado', pc(pm, sn));
}
console.log('\n== Por liga (cumple vs base) ==');
for (const [mk, amb, linea, lado] of CLAVE) {
  const r = E.analizar({ mk, amb, linea, lado, N: 10 }, F0()); const g = E.agrupar(r, i => E.lg[i]);
  console.log([mk, amb, linea, lado].join(' '), [...g.values()].sort((a, b) => a.k - b.k).map(x => `${D.ligas[x.k].slice(0, 6)}: ${pc(x.sh, x.sn)} (${x.sn}) vs ${pc(x.bh, x.bn)}`).join(' | '));
}
fs.writeFileSync(path.join(__dirname, 'hallazgos.json'), JSON.stringify(out));
