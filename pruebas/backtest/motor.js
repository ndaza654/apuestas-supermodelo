/* Motor del backtest de la regla «X de N» (misma lectura que recoleccion/ficha.py).
   Para cada partido usa SOLO los partidos anteriores de cada equipo (sin mirar el futuro):
   - regularidad: veces que la línea se cumplió en los últimos N partidos de cada equipo
     (total: total del partido; local: lo que hace el local / lo que concede el visitante; visitante: al revés);
   - esperado por equipo = (lo que hace + lo que concede el rival)/2; total = suma;
   - colchón = esperado − línea (Más) o línea − esperado (Menos).
   Sirve igual en node (hallazgos.js) y dentro del informe HTML. */
(function (root) {
  'use strict';
  var P = 10, VIEJO = 400; // historial máximo y días a partir de los cuales un partido ya no cuenta como «último»

  var MERCADOS = {
    goles:   { nombre: 'Goles', H: 'gH', A: 'gA', total: [0.5, 1.5, 2.5, 3.5, 4.5, 5.5], equipo: [0.5, 1.5, 2.5, 3.5] },
    btts:    { nombre: 'Ambos marcan', total: [0.5], equipo: [] },
    corners: { nombre: 'Córners', H: 'cH', A: 'cA', total: [6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5], equipo: [2.5, 3.5, 4.5, 5.5, 6.5, 7.5] },
    remates: { nombre: 'Remates', H: 'rH', A: 'rA', total: [18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5], equipo: [7.5, 9.5, 11.5, 13.5, 15.5, 17.5] },
    arco:    { nombre: 'Tiros al arco', H: 'tH', A: 'tA', total: [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5], equipo: [2.5, 3.5, 4.5, 5.5, 6.5] },
    faltas:  { nombre: 'Faltas', H: 'fH', A: 'fA', total: [18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5], equipo: [8.5, 10.5, 12.5, 14.5, 16.5] },
    tarj:    { nombre: 'Tarjetas (puntos)', total: [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5], equipo: [0.5, 1.5, 2.5, 3.5, 4.5] },
    amar:    { nombre: 'Amarillas', H: 'yH', A: 'yA', total: [1.5, 2.5, 3.5, 4.5, 5.5, 6.5], equipo: [0.5, 1.5, 2.5, 3.5] }
  };
  var AMBITOS = { total: 'Total del partido', local: 'Local', visitante: 'Visitante' };

  function wilson(h, n) {
    if (!n) return [NaN, NaN];
    var z = 1.96, p = h / n, d = 1 + z * z / n, c = p + z * z / (2 * n), e = z * Math.sqrt(p * (1 - p) / n + z * z / (4 * n * n));
    return [(c - e) / d, (c + e) / d];
  }

  function crear(D) {
    var n = D.n, i, k;
    function dec(s) { var a = new Int16Array(n); for (var i = 0; i < n; i++) { var c = s.charCodeAt(i); a[i] = c === 33 ? -1 : c - 35; } return a; }
    var S = {}; for (k in D.stats) S[k] = dec(D.stats[k]);
    var O = {}; for (k in D.odds) O[k] = Int32Array.from(D.odds[k]);
    var fecha = new Int32Array(n), acc = 0; for (i = 0; i < n; i++) { acc += D.dfecha[i]; fecha[i] = acc; }
    var lg = new Uint8Array(n); for (i = 0; i < n; i++) lg[i] = D.lg.charCodeAt(i) - 48;
    var h = Int16Array.from(D.h), a = Int16Array.from(D.a);
    var iBRA = D.ligas.length - 1; // Brasil juega por año calendario
    var temp = new Int16Array(n);
    for (i = 0; i < n; i++) { var dt = new Date(fecha[i] * 864e5), y = dt.getUTCFullYear(); temp[i] = (lg[i] === iBRA || dt.getUTCMonth() >= 6) ? y : y - 1; }
    var fav = new Int32Array(n); for (i = 0; i < n; i++) fav[i] = (O.oh[i] && O.oa[i]) ? Math.min(O.oh[i], O.oa[i]) : 0;

    // últimos P partidos anteriores de cada equipo (más reciente primero)
    var prevH = new Int32Array(n * P).fill(-1), prevA = new Int32Array(n * P).fill(-1), ult = [];
    function llenar(dst, i, T) {
      var arr = ult[T] || (ult[T] = []), c = 0;
      for (var j = arr.length - 1; j >= 0 && c < P; j--) { if (fecha[i] - fecha[arr[j]] > VIEJO) break; dst[i * P + c++] = arr[j]; }
    }
    for (i = 0; i < n; i++) { llenar(prevH, i, h[i]); llenar(prevA, i, a[i]); ult[h[i]].push(i); ult[a[i]].push(i); }

    // valores por mercado (local, visitante); -1 = sin dato
    var V = {};
    function valores(mk) {
      if (V[mk]) return V[mk];
      var vh = new Int16Array(n), va = new Int16Array(n), i;
      if (mk === 'tarj') {
        for (i = 0; i < n; i++) {
          var ok = S.yH[i] >= 0 && S.yA[i] >= 0 && S.xH[i] >= 0 && S.xA[i] >= 0;
          vh[i] = ok ? S.yH[i] + 2 * S.xH[i] : -1; va[i] = ok ? S.yA[i] + 2 * S.xA[i] : -1;
        }
      } else if (mk === 'btts') {
        for (i = 0; i < n; i++) { vh[i] = (S.gH[i] > 0 && S.gA[i] > 0) ? 1 : 0; va[i] = 0; }
      } else { vh = S[MERCADOS[mk].H]; va = S[MERCADOS[mk].A]; }
      return (V[mk] = [vh, va]);
    }

    var cachePrep = {};
    function preparar(mk, amb, N) {
      var key = mk + '|' + amb + '|' + N; if (cachePrep[key]) return cachePrep[key];
      var vv = valores(mk), VH = vv[0], VA = vv[1], ind = mk === 'btts';
      var VL = new Int16Array(n * P).fill(-1), VV = new Int16Array(n * P).fill(-1);
      var nl = new Uint8Array(n), nv = new Uint8Array(n), exp = new Float32Array(n).fill(NaN), real = new Int16Array(n).fill(-1);
      for (var i = 0; i < n; i++) {
        var cl = 0, cv = 0, Fl = 0, Cl = 0, Fv = 0, Cv = 0, k, j, f, c;
        for (k = 0; k < N; k++) {
          j = prevH[i * P + k]; if (j < 0) break; if (VH[j] < 0 || VA[j] < 0) continue;
          if (h[j] === h[i]) { f = VH[j]; c = VA[j]; } else { f = VA[j]; c = VH[j]; }
          VL[i * P + cl++] = ind ? VH[j] : amb === 'total' ? f + c : amb === 'local' ? f : c; Fl += ind ? VH[j] : f; Cl += c;
        }
        for (k = 0; k < N; k++) {
          j = prevA[i * P + k]; if (j < 0) break; if (VH[j] < 0 || VA[j] < 0) continue;
          if (h[j] === a[i]) { f = VH[j]; c = VA[j]; } else { f = VA[j]; c = VH[j]; }
          VV[i * P + cv++] = ind ? VH[j] : amb === 'total' ? f + c : amb === 'local' ? c : f; Fv += ind ? VH[j] : f; Cv += c;
        }
        nl[i] = cl; nv[i] = cv;
        if (cl && cv) {
          if (ind) exp[i] = (Fl / cl + Fv / cv) / 2;
          else { var el = (Fl / cl + Cv / cv) / 2, ev = (Fv / cv + Cl / cl) / 2; exp[i] = amb === 'total' ? el + ev : amb === 'local' ? el : ev; }
        }
        if (VH[i] >= 0 && VA[i] >= 0) real[i] = ind ? VH[i] : amb === 'total' ? VH[i] + VA[i] : amb === 'local' ? VH[i] : VA[i];
      }
      return (cachePrep[key] = { VL: VL, VV: VV, nl: nl, nv: nv, exp: exp, real: real });
    }

    function tieneCuota(q) { return q.mk === 'goles' && q.amb === 'total' && q.linea === 2.5; }

    /* q: {mk, amb, linea, lado:'mas'|'menos', N}
       f: {ligas:[bool], tDesde, tHasta, equipo:-1|id, K, quien:'ambos'|'local'|'visitante'|'cualquiera'|'todas', nmin,
           colMin, colMax, favMin, favMax, cuoMin, cuoMax}  (null = sin límite)
       base = partidos con historial suficiente que pasan liga/temporada/equipo/cuotas; sel = base + regularidad + colchón. */
    function analizar(q, f) {
      var p = preparar(q.mk, q.amb, q.N), mas = q.lado === 'mas', L = q.linea, conCuota = tieneCuota(q);
      var xL = new Uint8Array(n), xV = new Uint8Array(n), sel = new Uint8Array(n), hit = new Uint8Array(n), col = new Float32Array(n);
      var base = [], r = { bn: 0, bh: 0, sn: 0, sh: 0, pmB: 0, pmBn: 0, pmBh: 0, pmS: 0, pmSn: 0, pmSh: 0 };
      var cuo = conCuota ? (mas ? O.o25 : O.u25) : null, otra = conCuota ? (mas ? O.u25 : O.o25) : null;
      var usaFav = f.favMin != null || f.favMax != null, usaCuo = conCuota && (f.cuoMin != null || f.cuoMax != null);
      for (var i = 0; i < n; i++) {
        if (p.real[i] < 0 || p.nl[i] < f.nmin || p.nv[i] < f.nmin) continue;
        if (!f.ligas[lg[i]] || temp[i] < f.tDesde || temp[i] > f.tHasta) continue;
        if (f.equipo >= 0 && h[i] !== f.equipo && a[i] !== f.equipo) continue;
        if (usaFav) { var fv = fav[i] / 100; if (!fv || (f.favMin != null && fv < f.favMin) || (f.favMax != null && fv > f.favMax)) continue; }
        if (usaCuo) { var cq = cuo[i] / 100; if (!cq || (f.cuoMin != null && cq < f.cuoMin) || (f.cuoMax != null && cq > f.cuoMax)) continue; }
        var a1 = 0, a2 = 0, k, o = i * P;
        for (k = 0; k < p.nl[i]; k++) if (p.VL[o + k] > L) a1++;
        for (k = 0; k < p.nv[i]; k++) if (p.VV[o + k] > L) a2++;
        if (!mas) { a1 = p.nl[i] - a1; a2 = p.nv[i] - a2; }
        xL[i] = a1; xV[i] = a2;
        var c = mas ? p.exp[i] - L : L - p.exp[i]; col[i] = c;
        var ok = mas ? p.real[i] > L : p.real[i] < L; hit[i] = ok ? 1 : 0;
        var pm = (conCuota && cuo[i] && otra[i]) ? (1 / cuo[i]) / (1 / cuo[i] + 1 / otra[i]) : NaN;
        base.push(i); r.bn++; if (ok) r.bh++; if (pm === pm) { r.pmB += pm; r.pmBn++; if (ok) r.pmBh++; }
        var reg = f.quien === 'todas' ? true : f.quien === 'ambos' ? (a1 >= f.K && a2 >= f.K) : f.quien === 'local' ? a1 >= f.K
          : f.quien === 'visitante' ? a2 >= f.K : (a1 >= f.K || a2 >= f.K);
        if (reg && (f.colMin == null || c >= f.colMin) && (f.colMax == null || c <= f.colMax)) {
          sel[i] = 1; r.sn++; if (ok) r.sh++; if (pm === pm) { r.pmS += pm; r.pmSn++; if (ok) r.pmSh++; }
        }
      }
      r.base = base; r.sel = sel; r.hit = hit; r.xL = xL; r.xV = xV; r.col = col; r.prep = p; r.conCuota = conCuota;
      return r;
    }

    /* agrupa los partidos de la base: clave(i) -> {bn,bh,sn,sh} */
    function agrupar(r, clave) {
      var m = new Map();
      for (var t = 0; t < r.base.length; t++) {
        var i = r.base[t], k = clave(i); if (k == null) continue;
        var g = m.get(k); if (!g) { g = { k: k, bn: 0, bh: 0, sn: 0, sh: 0 }; m.set(k, g); }
        g.bn++; g.bh += r.hit[i]; if (r.sel[i]) { g.sn++; g.sh += r.hit[i]; }
      }
      return m;
    }

    return {
      D: D, n: n, P: P, fecha: fecha, lg: lg, h: h, a: a, temp: temp, fav: fav, O: O, S: S,
      preparar: preparar, analizar: analizar, agrupar: agrupar, tieneCuota: tieneCuota,
      tMin: Math.min.apply(null, [temp[0]]), tMax: (function () { var m = 0; for (var i = 0; i < n; i++) if (temp[i] > m) m = temp[i]; return m; })()
    };
  }

  var api = { crear: crear, MERCADOS: MERCADOS, AMBITOS: AMBITOS, wilson: wilson };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Motor = api;
})(typeof window !== 'undefined' ? window : this);
