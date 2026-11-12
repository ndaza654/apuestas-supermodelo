# -*- coding: utf-8 -*-
"""Balance semanal (o de cualquier periodo) con las 5 preguntas de Ingeniero Analista (#397), respondidas con los datos
del registro y no con la intuición, más CLV y tamaño de muestra:
  1. ¿Cuál es la operativa más rentable?        (mercado fino × tipo de partido, con ROI, intervalo y CLV)
  2. ¿Qué mercado conviene dejar o revisar?      (peor ROI y peor calibración contra el mercado)
  3. ¿Qué tan consistente es?                    (por semana, racha de pérdidas, % de semanas en rojo, stake)
  4. ¿Cuál es el patrón de las pérdidas?          (guion, n.º de patas, vivo/previo, tramo de cuota, alertas)
  5. Tres mejoras concretas                       (derivadas de los números: pesos del modelo, contexto, precio)
Ninguna respuesta es una regla: con menos de 300 apuestas por grupo, el error típico del ROI es de ±6 pts o más, y el
informe lo dice. Uso: python3 -m supermodelo.balance registro.csv [--desde 2026-11-01] [--hasta 2026-11-08]
"""
import math, sys, datetime as dt
from collections import defaultdict
from . import registro as RG


def _fecha(x):
    t = (x.get('fecha') or x.get('hora_analisis') or '')[:10]
    try:
        return dt.date.fromisoformat(t)
    except ValueError:
        return None


def _roi(X):
    st = [x['stake_f'] or 1.0 for x in X]
    pl = [((x['cuota_f'] - 1) if x['y'] else -1) * s for x, s in zip(X, st)]
    tot = sum(st)
    m = sum(pl) / tot if tot else 0
    u = [((x['cuota_f'] - 1) if x['y'] else -1) for x in X]
    mu = sum(u) / len(u)
    sd = math.sqrt(sum((v - mu) ** 2 for v in u) / max(len(u) - 1, 1))
    return m, 1.96 * sd / math.sqrt(len(u)), sum(pl)


def balance(ruta, desde=None, hasta=None, min_n=5):
    T = RG._leer(ruta)
    if desde:
        T = [x for x in T if (_fecha(x) or dt.date.min) >= desde]
    if hasta:
        T = [x for x in T if (_fecha(x) or dt.date.max) <= hasta]
    ap = [x for x in T if x.get('apostada') == 'Sí' and x['cuota_f']]
    L = [f"# Balance {'desde ' + str(desde) if desde else ''}{' hasta ' + str(hasta) if hasta else ''}".strip(),
         f"Líneas cerradas: {len(T)} · apostadas: {len(ap)}"]
    if not ap:
        L.append('\nNo hay apuestas cerradas en el periodo: el balance usa solo la calibración de las líneas analizadas.')
    else:
        m, ic, pl = _roi(ap)
        clv = [x['cuota_f'] / x['cierre'] - 1 for x in ap if x['cierre']]
        L.append(f"Resultado: {pl:+.2f} u · ROI {m:+.1%} ± {ic:.1%} (95 %) · acierto {sum(x['y'] for x in ap) / len(ap):.0%} contra "
                 f"{sum(1 / x['cuota_f'] for x in ap) / len(ap):.0%} que pedían las cuotas"
                 + (f" · CLV medio {sum(clv) / len(clv):+.1%} en {len(clv)}" if clv else ' · sin cuotas de cierre (anótalas: es la señal más rápida)'))
    # 1 y 2: por grupo
    def grupos(clave):
        g = defaultdict(list)
        for x in ap:
            g[clave(x)].append(x)
        filas = []
        for k, X in g.items():
            if len(X) < min_n:
                continue
            m, ic, pl = _roi(X)
            clv = [x['cuota_f'] / x['cierre'] - 1 for x in X if x['cierre']]
            filas.append((k, len(X), m, ic, pl, sum(clv) / len(clv) if clv else None))
        return sorted(filas, key=lambda f: -f[2])
    sub = lambda x: x.get('submercado') or x.get('familia')
    G = grupos(lambda x: f"{sub(x)} · {(x.get('tipo') or '').split(' · ')[0]}")
    Gf = grupos(lambda x: x.get('familia'))
    def tabla(t, filas):
        L.append(f'\n## {t}')
        if not filas:
            L.append(f'(ningún grupo con {min_n}+ apuestas)')
            return
        L.append('| Grupo | n | ROI | ± 95 % | Resultado (u) | CLV |')
        L.append('|---|---|---|---|---|---|')
        for k, n, m, ic, pl, c in filas:
            L.append(f"| {k} | {n} | {m:+.1%} | {ic:.1%} | {pl:+.2f} | {'—' if c is None else f'{c:+.1%}'} |")
    tabla('1. Operativa más rentable (mercado fino × fuerza del favorito)', G[:6])
    peores = sorted(Gf, key=lambda f: f[2])[:4]
    tabla('2. Mercados a revisar (peor ROI por familia)', peores)
    # calibración contra el mercado por familia (todas las líneas, apostadas o no)
    cal = defaultdict(list)
    for x in T:
        if x['pm'] is not None and x['p1'] is not None and x.get('familia') != 'combo':
            cal[x['familia']].append(x)
    filas = []
    for k, X in cal.items():
        if len(X) < 20:
            continue
        bm = sum((x['pm'] - x['y']) ** 2 for x in X) / len(X)
        b1 = sum((x['p1'] - x['y']) ** 2 for x in X) / len(X)
        filas.append((k, len(X), bm, b1))
    if filas:
        L.append('\n| Familia | líneas | Brier mercado | Brier modelo | Lectura |')
        L.append('|---|---|---|---|---|')
        for k, n, bm, b1 in sorted(filas, key=lambda f: f[3] - f[2]):
            lect = 'el modelo calibra mejor' if b1 < bm - 0.003 else ('el mercado calibra mejor' if b1 > bm + 0.003 else 'igual')
            L.append(f'| {k} | {n} | {bm:.4f} | {b1:.4f} | {lect} |')
    # 3. consistencia
    L.append('\n## 3. Consistencia')
    if ap:
        sem = defaultdict(list)
        for x in ap:
            f = _fecha(x)
            if f:
                sem[f.isocalendar()[:2]].append(x)
        rojo = 0
        for k in sorted(sem):
            m, ic, pl = _roi(sem[k])
            rojo += pl < 0
            L.append(f"- Semana {k[1]} de {k[0]}: {len(sem[k])} apuestas, {pl:+.2f} u (ROI {m:+.1%})")
        orden = sorted(ap, key=lambda x: (x.get('hora_analisis') or x.get('fecha') or ''))
        racha = mx = 0
        for x in orden:
            racha = racha + 1 if not x['y'] else 0
            mx = max(mx, racha)
        st = [x['stake_f'] for x in ap if x['stake_f']]
        L.append(f"- Semanas en rojo: {rojo} de {len(sem)} · racha de pérdidas más larga: {mx}"
                 + (f" · stake medio {sum(st) / len(st):.2f} (máx. {max(st):.2f})" if st else ''))
        L.append(f"- Con {len(ap)} apuestas el ROI tiene un error típico de ±{100 / math.sqrt(len(ap)):.0f} pts aprox.: "
                 + ('todavía es ruido.' if len(ap) < 300 else 'la muestra ya dice algo.'))
    # 4. patrón de pérdidas
    L.append('\n## 4. Patrón de las pérdidas')
    perd = [x for x in ap if not x['y']]
    if perd:
        def reparto(nombre, clave):
            g = defaultdict(lambda: [0, 0])
            for x in ap:
                k = clave(x)
                g[k][0] += 1; g[k][1] += (not x['y'])
            partes = [f"{k}: {v[1]}/{v[0]} perdidas" for k, v in sorted(g.items(), key=lambda z: -z[1][0]) if v[0] >= 2]
            if partes:
                L.append(f"- {nombre}: " + ' · '.join(partes))
        reparto('Por guion principal del partido', lambda x: x.get('guion_principal') or '—')
        reparto('Simple, combo o vivo', lambda x: x.get('tipo_apuesta') or ('combo' if x.get('familia') == 'combo' else 'simple'))
        reparto('Por tramo de cuota', lambda x: '<1,50' if x['cuota_f'] < 1.5 else ('1,50–2,20' if x['cuota_f'] < 2.2 else ('2,20–4' if x['cuota_f'] < 4 else '4+')))
        reparto('Con o sin alerta del modelo', lambda x: 'con alerta' if x.get('alerta') else 'sin alerta')
        reparto('Etiqueta del modelo', lambda x: (x.get('etiqueta') or '').split(' · ')[0] or '—')
        ev_perd = [float(x['ev']) for x in perd if x.get('ev') not in (None, '')]
        if ev_perd:
            L.append(f"- EV medio que el modelo daba a las perdidas: {sum(ev_perd) / len(ev_perd):+.1%}")
    else:
        L.append('- Sin pérdidas cerradas en el periodo.')
    # 5. mejoras
    L.append('\n## 5. Tres mejoras sugeridas por los números')
    mej = []
    for k, n, bm, b1 in sorted(filas, key=lambda f: f[3] - f[2]):
        if n >= 30 and b1 < bm - 0.004:
            from . import config as C
            wv = C.W_MERCADO.get(k, 0.5)
            mej.append(f"En {k} el modelo calibra mejor que el mercado ({b1:.4f} contra {bm:.4f}, {n} líneas): probar a bajar W_MERCADO['{k}'] de {wv:.2f} a {max(0.0, wv - 0.1):.2f}.")
        elif n >= 30 and b1 > bm + 0.004:
            mej.append(f"En {k} el mercado calibra mejor ({bm:.4f} contra {b1:.4f}, {n} líneas): subir W_MERCADO['{k}'] o revisar qué contexto se le está metiendo.")
    for k, n, m, ic, pl, c in Gf:
        if c is not None and c < -0.02 and n >= 10:
            mej.append(f"En {k} se toma peor precio que el cierre (CLV {c:+.1%}): apostar más cerca del partido o comparar cuota antes.")
    comb = [x for x in ap if x.get('familia') == 'combo']
    if len(comb) >= 5:
        esp = sum(x['p1'] or 0 for x in comb)
        real = sum(x['y'] for x in comb)
        if real < esp - 1:
            mej.append(f"Los combos ganaron {real} de {len(comb)} contra {esp:.1f} esperados: revisar patas que se estorban (correlación < 1) y la pata más frágil antes de jugar.")
    if not mej:
        mej.append('Sin señales claras todavía: seguir registrando todas las líneas (apostadas o no) y la cuota de cierre.')
    for x in mej[:3]:
        L.append(f'- {x}')
    return '\n'.join(L)


if __name__ == '__main__':
    a = sys.argv[1:]
    d = dt.date.fromisoformat(a[a.index('--desde') + 1]) if '--desde' in a else None
    h = dt.date.fromisoformat(a[a.index('--hasta') + 1]) if '--hasta' in a else None
    print(balance(a[0], d, h))
