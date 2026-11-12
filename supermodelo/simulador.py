# -*- coding: utf-8 -*-
"""Simulador minuto a minuto con estado del partido.

La diferencia de fondo con el v1: el v1 trataba cada estadística por separado con su media fija. Aquí el partido
se juega miles de veces y cada minuto depende de cómo va: el que se adelanta remata y saca menos córners, el que
va perdiendo se vuelca, una expulsión cambia todo, un partido cerrado y tarde da más tarjetas. Así salen:
  · la probabilidad de cada línea de cada mercado,
  · la probabilidad CONJUNTA de cualquier combinación (builders) sin suponer independencia,
  · los escenarios (guiones) del partido y qué línea aguanta en cada uno.

Las medias de entrada (objetivos) son incondicionales: el simulador se calibra solo para que, en promedio, las
reproduzca; el estado del partido cambia la FORMA de la distribución y las correlaciones, no la media.
"""
import numpy as np
from . import config as C

LADOS = (0, 1)
CLAVES = ['g', 'sh', 'sot', 'c', 'f', 'y', 'off', 'gk', 'ti', 'tk']
POR_DEFECTO = {'off': 1.8, 'gk': 8.0, 'ti': 20.0, 'tk': 16.0}


def _idx(d):
    return np.clip(d, -2, 3) + 2   # d<=-2 →0, -1→1, 0→2, +1→3, +2→4, >=+3→5


def _efecto(tabla, d, sens):
    t = np.asarray(tabla)[_idx(d)]
    return 1.0 + sens * (t - 1.0)


def _minutos():
    mins = []
    for k in range(C.MIN_1T):
        w = C.PESO_1T * (C.RAMPA_FACTOR if k < C.RAMPA_MIN else 1.0)
        mins.append((1, k + 1, w))
    for k in range(C.MIN_2T):
        w = C.PESO_2T * (C.RAMPA_FACTOR if k < C.RAMPA_MIN else 1.0)
        mins.append((2, 46 + k, w))
    tot = sum(w for _, _, w in mins)
    return [(h, m, w / tot) for h, m, w in mins]


class Partido:
    """objetivos: [dict_local, dict_visitante] con medias por partido de g, sh, sot, c, f, y (+ off, gk, ti, tk).
    ajustes: contexto.Ajustes (sensibilidad, global de eliminatoria, necesita ganar, factor de rojas)."""

    def __init__(self, objetivos, ajustes=None, n=C.N_SIM, seed=C.SEED, estado=None):
        """estado (opcional, para EN VIVO): el partido ya va en un minuto con un marcador y unas estadísticas.
        Convención de tarjetas: 'amarillas' = amarillas mostradas (incluida la 2.ª amarilla de una expulsión), 'rojas' = todas
        las rojas, 'rojas_directas' = las rojas directas (Betano: amarilla 1, roja 2 → doble amarilla 3, roja directa 2).
        {'mitad': 2, 'minuto': 60, 'goles': [1, 0], 'rojas': [0, 1], 'rojas_directas': [0, 1], 'amarillas': [2, 1], 'corners': [4, 3],
         'remates': [9, 5], 'al_arco': [3, 1], 'faltas': [7, 9], 'goles_1t': [1, 0], 'corners_1t': [3, 2],
         'amarillas_1t': [1, 0], 'remates_1t': [5, 3], 'al_arco_1t': [2, 1], 'faltas_1t': [4, 5]}
        La calibración se hace con el partido completo (las medias previas); luego se juegan solo los minutos que
        faltan, desde ese estado. El ritmo y la producción de cada equipo se actualizan con lo observado (gamma-Poisson:
        lo visto pesa más cuanto más minutos van; el previo nunca desaparece)."""
        from .contexto import Ajustes
        self.obj = [dict(POR_DEFECTO, **o) for o in objetivos]
        self.aj = ajustes or Ajustes()
        self.n = n
        self.rng = np.random.default_rng(seed)
        self.mins = _minutos()
        self.k = [{s: 1.0 for s in ['sh', 'c', 'f', 'off', 'gk', 'ti', 'tk', 'psot', 'q', 'py']} for _ in LADOS]
        self._calibrar()
        self.estado = estado
        self.res = self._jugar(self.n, estado)

    # ------------------------------------------------------------ calibración de medias
    def _calibrar(self, iters=4, n=6000):
        for _ in range(iters):
            r = self._jugar(n)
            for l in LADOS:
                o = self.obj[l]
                for s in ['sh', 'c', 'f', 'off', 'gk', 'ti', 'tk']:
                    m = r[l][s].mean()
                    if m > 0:
                        self.k[l][s] *= o[s] / m
                ms, mt = r[l]['sh'].mean(), r[l]['sot'].mean()
                if mt > 0:
                    self.k[l]['psot'] *= (o['sot'] / o['sh']) / (mt / ms)
                mg = r[l]['g'].mean()
                if mg > 0:
                    self.k[l]['q'] *= (o['g'] / o['sot']) / (mg / mt)
                my, mf = r[l]['tarjetas'].mean(), r[l]['f'].mean()   # puntos de Betano: amarilla 1, roja 2
                if my > 0:
                    self.k[l]['py'] *= (o['y'] / o['f']) / (my / mf)

    # ------------------------------------------------------------ un lote de partidos
    def _factores(self, n, estado):
        """Factores latentes de cada partido simulado. Sin estado: los previos. Con estado (en vivo): la parte
        observada del partido actualiza ritmo, dureza y la producción de cada equipo (gamma-Poisson conjugada)."""
        rng = self.rng
        g = lambda forma, obs=0.0, esp=0.0: rng.gamma(forma + obs, 1.0 / (forma + esp), n)
        if not estado:
            ritmo, dureza = g(C.FORMA_RITMO), g(C.FORMA_DUREZA)
            ind = [{s: g(C.FORMA_EQUIPO[s]) for s in C.FORMA_EQUIPO} for _ in LADOS]
            return ritmo, dureza, ind
        fr = self._fraccion_jugada(estado)
        ob = lambda clave, l: float((estado.get(clave) or [0, 0])[l])
        tiene = lambda clave: estado.get(clave) is not None
        # ritmo: remates y córners de los dos equipos
        o_r = e_r = 0.0
        for clave, s in (('remates', 'sh'), ('corners', 'c')):
            if tiene(clave):
                o_r += ob(clave, 0) + ob(clave, 1); e_r += (self.obj[0][s] + self.obj[1][s]) * fr
        ritmo = g(C.FORMA_RITMO, o_r, e_r)
        o_d = e_d = 0.0
        if tiene('faltas'):
            o_d = ob('faltas', 0) + ob('faltas', 1); e_d = (self.obj[0]['f'] + self.obj[1]['f']) * fr
        dureza = g(C.FORMA_DUREZA, o_d, e_d)
        # Goles: lo que va del partido dice algo de la intensidad de gol de cada equipo HOY (un 0-0 al descanso es un partido
        # de menos gol de lo que decía la cuota). Validado con partidos reales desde el descanso (docs/CALIBRACION_10NOV.md).
        self._fg = [g(C.VIVO_FORMA_GOLES, ob('goles', l), self.obj[l]['g'] * fr) for l in LADOS] if C.VIVO_FORMA_GOLES else [1.0, 1.0]
        r_hat = (C.FORMA_RITMO + o_r) / (C.FORMA_RITMO + e_r)
        d_hat = (C.FORMA_DUREZA + o_d) / (C.FORMA_DUREZA + e_d)
        ind = []
        for l in LADOS:
            f_l = {}
            for s in C.FORMA_EQUIPO:
                clave = {'sh': 'remates', 'c': 'corners', 'f': 'faltas'}.get(s)
                if clave and tiene(clave):
                    base = r_hat if s != 'f' else d_hat
                    f_l[s] = g(C.FORMA_EQUIPO[s], ob(clave, l), self.obj[l][s] * fr * base)
                else:
                    f_l[s] = g(C.FORMA_EQUIPO[s])
            ind.append(f_l)
        return ritmo, dureza, ind

    def _fraccion_jugada(self, estado):
        ya = self._ya_jugado(estado)
        return sum(w for (h, m, w), j in zip(self.mins, ya) if j)

    def _ya_jugado(self, estado):
        if not estado:
            return [False] * len(self.mins)
        mitad, minuto = int(estado.get('mitad', 2 if estado.get('minuto', 0) > 45 else 1)), int(estado.get('minuto', 0))
        return [(h < mitad) or (h == mitad and m <= minuto) for (h, m, w) in self.mins]

    def _jugar(self, n, estado=None):
        rng, aj = self.rng, self.aj
        self._fg = [1.0, 1.0]
        ritmo, dureza, ind = self._factores(n, estado)
        fg = self._fg
        # Dos factores latentes simétricos entre los equipos (exp(±sigma·Z)):
        #  · territorio: quién pisa el campo rival hoy → remates y córners (no la calidad);
        #  · dominio: quién está mejor de lo que el precio decía en la calidad del remate y la definición.
        terr = rng.standard_normal(n)
        dom = rng.standard_normal(n)
        z = lambda: np.zeros(n, dtype=np.int32)
        R = [{s: z() for s in ['g', 'g1', 'sh', 'sot', 'c', 'c1', 'f', 'y', 'r', 'rd', 'r1', 'rd1', 'off', 'gk', 'ti', 'tk',
                               'y1', 'sh1', 'sot1', 'f1', 'off1', 'gk1', 'ti1']} for _ in LADOS]
        primer_eq = np.full(n, -1, dtype=np.int8); primer_min = np.full(n, 99, dtype=np.int16)
        roja_min = np.full(n, 99, dtype=np.int16)
        ya = self._ya_jugado(estado)
        if estado:
            mapa = {'goles': 'g', 'rojas': 'r', 'amarillas': 'y', 'corners': 'c', 'remates': 'sh', 'al_arco': 'sot',
                    'faltas': 'f', 'goles_1t': 'g1', 'corners_1t': 'c1', 'amarillas_1t': 'y1', 'remates_1t': 'sh1',
                    'al_arco_1t': 'sot1', 'faltas_1t': 'f1', 'rojas_directas': 'rd', 'rojas_1t': 'r1', 'rojas_directas_1t': 'rd1',
                    'fueras': 'off', 'saques_meta': 'gk', 'saques_banda': 'ti', 'fueras_1t': 'off1', 'saques_meta_1t': 'gk1',
                    'saques_banda_1t': 'ti1'}
            if estado.get('rojas') is not None and estado.get('rojas_directas') is None:
                estado = dict(estado, rojas_directas=estado['rojas'])   # sin dato: se suponen directas (2 puntos cada una)
            for clave, s in mapa.items():
                v = estado.get(clave)
                if v is not None:
                    for l in LADOS:
                        R[l][s][:] = int(v[l])
            mitad_e = int(estado.get('mitad', 2 if estado.get('minuto', 0) > 45 else 1))
            if mitad_e == 2:
                # En el 2.º tiempo lo del 1T ya es fijo. Si no viene (p. ej. córners del 1T), se reparte en proporción a los
                # minutos jugados; los goles del 1T, si no vienen, se suponen iguales al marcador actual (dar 'goles_1t').
                jug = 47 + max(0, int(estado.get('minuto', 46)) - 45)
                for clave, s1, s in (('goles_1t', 'g1', 'g'), ('corners_1t', 'c1', 'c'), ('amarillas_1t', 'y1', 'y'),
                                     ('remates_1t', 'sh1', 'sh'), ('al_arco_1t', 'sot1', 'sot'), ('faltas_1t', 'f1', 'f'),
                                     ('fueras_1t', 'off1', 'off'), ('saques_meta_1t', 'gk1', 'gk'), ('saques_banda_1t', 'ti1', 'ti')):
                    if estado.get(clave) is None:
                        for l in LADOS:
                            R[l][s1][:] = R[l][s][0] if s == 'g' else int(round(R[l][s][0] * 47 / jug))
            else:
                for s1, s in (('g1', 'g'), ('c1', 'c'), ('y1', 'y'), ('sh1', 'sh'), ('sot1', 'sot'), ('f1', 'f'), ('r1', 'r'), ('rd1', 'rd'),
                              ('off1', 'off'), ('gk1', 'gk'), ('ti1', 'ti')):
                    for l in LADOS:
                        R[l][s1][:] = R[l][s][0]   # en el 1T, lo que va es todo del 1T
            g0 = estado.get('goles') or [0, 0]
            if g0[0] or g0[1]:
                pe = estado.get('primer_gol')   # 'local' | 'visitante'; si no viene, el que más goles lleva
                primer_eq[:] = (0 if pe == 'local' else 1) if pe else (0 if g0[0] >= g0[1] else 1)
                primer_min[:] = int(estado.get('minuto_primer_gol', estado.get('minuto', 0)))
            r0 = estado.get('rojas') or [0, 0]
            if r0[0] or r0[1]:
                roja_min[:] = int(estado.get('minuto_roja', estado.get('minuto', 0)))
        base_roja = C.ROJA_DIRECTA_90 * aj.roja / len(self.mins)
        for (mitad, minuto, w), jugado in zip(self.mins, ya):
            if jugado:
                continue
            gol_ahora = [None, None]
            rampa_t = max(0.2, 1.0 + C.TARJETA_RAMPA * (minuto - 48.0) / 48.0)
            for l in LADOS:
                o, k, ri = self.obj[l], self.k[l], 1 - l
                d = R[l]['g'] - R[ri]['g'] + aj.offset_global[l]
                if aj.necesita_ganar[l] and minuto > 60:
                    d = np.where(d == 0, -1, d)
                hombres = np.clip(R[ri]['r'] - R[l]['r'], -2, 2)
                man_at = np.choose(hombres + 2, [C.EFECTO_HOMBRES[h]['ataque'] for h in (-2, -1, 0, 1, 2)])
                man_gol = np.choose(hombres + 2, [C.EFECTO_HOMBRES[h]['gol'] for h in (-2, -1, 0, 1, 2)])
                s = aj.sens[l]
                sg = 1.0 if l == 0 else -1.0
                t_sh, t_c = (np.exp(sg * C.TERRITORIO[x] * terr) for x in ('sh', 'c'))
                d_sh, d_c, d_q = (np.exp(sg * C.DOMINIO[x] * dom) for x in ('sh', 'c', 'q'))
                d_sot = np.exp(sg * C.DOMINIO.get('sot', 0.0) * dom)
                # remates → al arco → goles
                lam_sh = o['sh'] * k['sh'] * w * ritmo * ind[l]['sh'] * _efecto(C.EFECTO_MARCADOR['sh'], d, s) * man_at * d_sh * t_sh
                sh = rng.poisson(lam_sh)
                psot = np.clip(o['sot'] / o['sh'] * k['psot'] * _efecto(C.CALIDAD_MARCADOR['sot'], d, 1.0) * d_sot, 0, 0.95)
                sot = rng.binomial(sh, psot)
                # Volumen contra calidad: el partido o el equipo que remata más de lo previsto (ritmo, forma del día,
                # territorio) remata peor. Sin esto los goles iban demasiado atados al volumen de remates (corr 0,34 contra
                # 0,23 real en 62 000 partidos) y los combos «Más goles + Más córners/remates» salían inflados.
                vol = (ritmo * ind[l]['sh'] * t_sh) ** (-C.CALIDAD_VOLUMEN) if C.CALIDAD_VOLUMEN else 1.0
                q = np.clip(o['g'] / o['sot'] * k['q'] * _efecto(C.CALIDAD_MARCADOR['gol'], d, 1.0) * man_gol * d_q * vol * fg[l], 0, 0.9)
                gl = rng.binomial(sot, q)
                # córners, fueras de lugar, saques
                # Una parte de los córners sale de remates (rechazados o atajados al córner): Binomial(remates, pi).
                # Es lo que da la correlación remates–córners real (0,28 en 62 000 partidos) sin inflar la dispersión.
                pi_c = min(C.CORNER_POR_REMATE, 0.8 * o['c'] / max(o['sh'], 1e-6))
                c = rng.poisson(o['c'] * k['c'] * w * ritmo * ind[l]['c'] * _efecto(C.EFECTO_MARCADOR['c'], d, s) * man_at * d_c * t_c) \
                    + (rng.binomial(sh, pi_c) if pi_c > 0 else 0)
                off = rng.poisson(o['off'] * k['off'] * w * ritmo * ind[l]['off'] * _efecto(C.EFECTO_MARCADOR['off'], d, s) * np.sqrt(man_at))
                d_r = -d  # estado del rival
                ataque_rival = _efecto(C.EFECTO_MARCADOR['sh'], d_r, aj.sens[ri]) / np.maximum(man_at, 0.3)
                gk = rng.poisson(o['gk'] * k['gk'] * w * ritmo * ind[l]['gk'] * ataque_rival ** 0.6)
                ti = rng.poisson(o['ti'] * k['ti'] * w * ritmo * ind[l]['ti'])
                tk = rng.poisson(o['tk'] * k['tk'] * w * ritmo * ataque_rival)
                # faltas y tarjetas
                f = rng.poisson(o['f'] * k['f'] * w * dureza * ind[l]['f'] * _efecto(C.EFECTO_MARCADOR['f'], d, 1.0))
                cerrado_tarde = np.where((np.abs(d) <= 1) & (minuto >= 70), C.TARJETA_CERRADO_TARDE, 1.0)
                goleada = np.where(np.abs(d) >= 3, C.TARJETA_GOLEADA, 1.0)
                comp = np.clip(np.exp(C.COMPENSACION_AMARILLAS * (R[ri]['y'] - R[l]['y'])), *C.COMPENSACION_TOPE)
                # Amarillas: (1) por falta, Binomial(faltas, p); (2) sin falta (protestas, pérdida de tiempo, simulación),
                # que según StatsBomb pasan de casi 0 al inicio a ~la mitad al final. La parte (2) baja la correlación
                # faltas–tarjetas a la real (0,29) y retrasa las tarjetas (la amarilla media llega al 59 % del partido).
                ctx_y = ind[l]['y'] * cerrado_tarde * goleada * comp
                so = C.TARJETA_SIN_FALTA
                py = np.clip((1 - so) * o['y'] / o['f'] * k['py'] * ctx_y * rampa_t * dureza ** C.TARJETA_EXP_DUREZA, 0, 0.8)
                yy = rng.binomial(f, py)
                if so > 0:
                    yy = yy + rng.poisson(so * o['y'] * k['py'] * w * ctx_y * (minuto / 48.0) ** C.TARJETA_SIN_FALTA_RAMPA)
                seg = rng.binomial(yy, np.clip(C.PROB_SEGUNDA_AMARILLA * R[l]['y'], 0, 0.5))
                directa = (rng.random(n) < base_roja * cerrado_tarde * dureza * rampa_t).astype(np.int32)
                rojas = seg + directa
                nueva_roja = (rojas > 0) & (roja_min == 99)
                roja_min[nueva_roja] = minuto
                for key, val in (('sh', sh), ('sot', sot), ('g', gl), ('c', c), ('off', off), ('gk', gk), ('ti', ti),
                                 ('tk', tk), ('f', f), ('y', yy), ('r', rojas), ('rd', directa)):
                    R[l][key] += val
                if mitad == 1:
                    for key, val in (('g1', gl), ('c1', c), ('y1', yy), ('sh1', sh), ('sot1', sot), ('f1', f), ('r1', rojas), ('rd1', directa),
                                     ('off1', off), ('gk1', gk), ('ti1', ti)):
                        R[l][key] += val
                gol_ahora[l] = gl
            for l in LADOS:
                nuevo = (gol_ahora[l] > 0) & (primer_eq == -1)
                primer_eq[nuevo] = l
                primer_min[nuevo] = minuto
            empate = (gol_ahora[0] > 0) & (gol_ahora[1] > 0) & (primer_min == minuto)
            primer_eq[empate] = rng.integers(0, 2, empate.sum())
        for l in LADOS:
            R[l]['sv'] = R[1 - l]['sot'] - R[1 - l]['g']   # atajadas del portero de l
            # Puntos de tarjetas como los cuenta Betano: amarilla 1, roja 2. Doble amarilla = 1 + roja 2 = 3 (la 2.ª
            # amarilla ya está en 'y' y la roja suma 1 más); roja directa = 2 (suma 1 en 'r' y 1 en 'rd').
            R[l]['tarjetas'] = R[l]['y'] + R[l]['r'] + R[l]['rd']
            R[l]['tarj1'] = R[l]['y1'] + R[l]['r1'] + R[l]['rd1']
        return dict(lados=R, primer_eq=primer_eq, primer_min=primer_min, roja_min=roja_min) | {0: R[0], 1: R[1]}

    # ------------------------------------------------------------ utilidades
    def resumen(self):
        out = {}
        for l in LADOS:
            out[l] = {s: float(self.res[l][s].mean()) for s in ['g', 'sh', 'sot', 'c', 'f', 'y', 'r', 'off', 'gk', 'ti', 'sv', 'tk']}
        return out
