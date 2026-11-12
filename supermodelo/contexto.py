# -*- coding: utf-8 -*-
"""Ficha de contexto: los hechos del partido que los números de temporada no ven.

La ficha la llena una persona o el chat de análisis (LLM) con HECHOS, nunca con probabilidades:
quién es favorito, si es derbi, el árbitro, el clima, bajas, rotación, motivación, eliminatoria, estilos.
El código la traduce en multiplicadores sobre las medias de cada equipo y en el comportamiento del simulador
(por ejemplo, el equipo que necesita remontar una eliminatoria juega desde el minuto 1 como si fuera perdiendo).

Los multiplicadores son puntos de partida con su fuente; el registro los recalibra con tus datos.

Ejemplo de ficha (JSON):
{
  "derbi": false, "importancia": "normal",            # normal | alta | final
  "arbitro": {"tarjetas_por_partido": 5.3, "partidos": 12, "media_liga": 4.6},
  "clima": {"lluvia": "fuerte", "viento_fuerte": false, "temperatura": 9},
  "eliminatoria": {"global_local": 0, "global_visitante": 2},   # marcador global antes del partido
  "local":     {"estilo": ["posesion", "centros"], "marcador": "normal", "bajas_ataque": 1,
                "bajas_defensa": 0, "rotacion": false, "motivacion": "normal", "necesita_ganar": false},
  "visitante": {"estilo": ["bloque_bajo", "contragolpe"], "marcador": "se_encierra", ...}
}
"""
from dataclasses import dataclass, field
from . import config as C

ESTADISTICAS = ['g', 'sh', 'sot', 'c', 'f', 'y', 'off', 'gk', 'ti']


@dataclass
class Ajustes:
    mult: dict = field(default_factory=lambda: {s: {k: 1.0 for k in ESTADISTICAS} for s in (0, 1)})
    sens: list = field(default_factory=lambda: [1.0, 1.0])     # sensibilidad al marcador
    offset_global: list = field(default_factory=lambda: [0, 0])  # diferencia del global (eliminatorias)
    necesita_ganar: list = field(default_factory=lambda: [False, False])
    roja: float = 1.0
    frescos: list = field(default_factory=list)
    notas: list = field(default_factory=list)

    def x(self, lado, stats, f, nota=None):
        for s in stats:
            self.mult[lado][s] *= f
        if nota:
            self.notas.append(nota)


def traducir(ficha):
    """Convierte la ficha en Ajustes. Lado 0 = local, 1 = visitante."""
    A = Ajustes()
    if not ficha:
        return A
    nom = {0: 'local', 1: 'visitante'}
    frescos = set(ficha.get('frescos') or [])
    # Información tardía (Sharpods, Ingeniero Analista #296): lo que se supo en las últimas horas no está en la cuota.
    # Cada entrada {"tipo": "bajas", "hecho": "...", "horas": 2} marca su tipo como fresco si tiene < HORAS_FRESCO horas.
    for it in ficha.get('info_tardia') or []:
        if it.get('tipo') and (it.get('horas') is None or float(it['horas']) < C.HORAS_FRESCO):
            frescos.add(it['tipo'])
    for b in ficha.get('bajas') or []:
        if b.get('horas_desde_noticia') is not None and float(b['horas_desde_noticia']) < C.HORAS_FRESCO and b.get('confirmada', True):
            frescos.add('bajas')
    A.frescos = sorted(frescos)

    def F(tipo, f):
        """Parte del efecto que todavía NO está en el precio de Betano. Un hecho marcado como fresco
        (conocido hace pocas horas: alineación, lesión de última hora, cambio de árbitro) va completo."""
        fz = 1.0 if tipo in frescos else C.FUERZA_CONTEXTO.get(tipo, 0.5)
        return 1 + fz * (f - 1)

    # ---- partido
    if ficha.get('derbi'):
        # Harvard Sports Analysis (Premier): derbis 25,95 faltas vs 22,38 (+16 %).
        for l in (0, 1):
            A.x(l, ['f'], F('derbi', 1.15)); A.x(l, ['y'], F('derbi', 1.20))
        A.roja *= F('derbi', 1.5)
        A.notas.append('Derbi: faltas ×1,15 y tarjetas ×1,20 (derbis de Premier: +3,6 faltas por partido).')
    imp = ficha.get('importancia', 'normal')
    if imp in ('alta', 'final'):
        for l in (0, 1):
            A.x(l, ['y'], F('importancia', 1.10)); A.x(l, ['f'], F('importancia', 1.05)); A.x(l, ['g'], F('importancia', 0.95))
        A.notas.append(f'Importancia {imp}: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).')

    arb = dict(ficha.get('arbitro') or {})
    # Unidades: puntos de Betano (amarilla 1, roja 2). Si la fuente da amarillas y rojas por partido por separado
    # (StatsHub, Flashscore), se convierten. La media de la liga, si la ficha no la trae, sale del prior verificado
    # (datos/prior_liga.csv): lección del 9-nov, no usar al árbitro sin media de liga.
    # Convención: amarillas por partido SIN contar la 2.ª amarilla que termina en roja (así las dan StatsHub/Flashscore en
    # la mayoría de las ligas) y rojas = todas las rojas → puntos = amarillas + 2·rojas. Si la fuente da rojas directas por
    # separado ('rojas_directas_por_partido') y sus amarillas SÍ incluyen la 2.ª: puntos = amarillas + rojas + directas.
    if not arb.get('tarjetas_por_partido') and arb.get('amarillas_por_partido') is not None:
        am, ro = float(arb['amarillas_por_partido']), float(arb.get('rojas_por_partido') or 0)
        rd = arb.get('rojas_directas_por_partido')
        arb['tarjetas_por_partido'] = round(am + ro + float(rd) if rd is not None else am + 2 * ro, 2)
    fuente_media = 'ficha'
    if arb.get('tarjetas_por_partido') and not arb.get('media_liga'):
        from . import ligas
        p = ligas.prior(ficha.get('_liga'))
        if p and p.get('tarjetas_betano_x_partido'):
            arb['media_liga'] = round(float(p['tarjetas_betano_x_partido']), 2)
            fuente_media = f"prior de la liga ({p.get('nombre', '')})"
    if arb.get('tarjetas_por_partido') and arb.get('media_liga'):
        n = arb.get('partidos', 0) or 0
        w = 0.7 * min(1.0, n / 15.0)
        fac = F('arbitro', 1 + w * (arb['tarjetas_por_partido'] / arb['media_liga'] - 1))
        for l in (0, 1):
            A.x(l, ['y'], fac)
        A.roja *= fac
        A.notas.append(f'Árbitro {arb.get("nombre", "")}: {arb["tarjetas_por_partido"]} tarjetas/partido contra '
                       f'{arb["media_liga"]} de la liga ({fuente_media}) en {n} partidos → tarjetas ×{fac:.2f} (encogido por muestra).')
    elif arb.get('tarjetas_por_partido'):
        A.notas.append('Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.')
    else:
        A.notas.append('Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).')
    if arb.get('tarjetas_por_partido') and not arb.get('partidos'):
        A.notas.append('Árbitro sin número de partidos dirigidos: su efecto queda en 0 (poner "partidos" en la ficha).')

    clima = ficha.get('clima') or {}
    if clima.get('lluvia') == 'fuerte':
        for l in (0, 1):
            A.x(l, ['g'], F('clima', 1.04)); A.x(l, ['c'], F('clima', 1.03))
        A.notas.append('Lluvia fuerte: goles ×1,04 y córners ×1,03 (meses lluviosos dan más goles y córners).')
    if clima.get('viento_fuerte'):
        for l in (0, 1):
            A.x(l, ['g'], F('clima', 0.95)); A.x(l, ['sot'], F('clima', 0.96))
        A.notas.append('Viento fuerte: goles ×0,95.')
    t = clima.get('temperatura')
    if t is not None and t < 5:
        for l in (0, 1):
            A.x(l, ['g'], F('clima', 0.96)); A.x(l, ['c'], F('clima', 0.97))
        A.notas.append('Frío (<5 °C): goles ×0,96 y córners ×0,97.')

    el = ficha.get('eliminatoria')
    if el:
        dif = (el.get('global_local') or 0) - (el.get('global_visitante') or 0)
        A.offset_global = [max(-2, min(2, dif)), max(-2, min(2, -dif))]
        if dif:
            atrasado = 0 if dif < 0 else 1
            A.notas.append(f'Eliminatoria: el {nom[atrasado]} empieza abajo en el global ({abs(dif)}); el simulador '
                           'lo hace jugar desde el minuto 1 como si fuera perdiendo.')

    # ---- equipos
    for l in (0, 1):
        e = ficha.get(nom[l]) or {}
        o = 1 - l
        est = set(e.get('estilo') or [])
        fz = 1.0 if (e.get('estilo_nuevo') or 'estilo' in frescos) else C.FUERZA_CONTEXTO['estilo']
        k = lambda f: 1 + fz * (f - 1)
        if 'bloque_bajo' in est:
            A.x(l, ['sh', 'c'], k(0.90)); A.x(o, ['c'], k(1.08)); A.x(o, ['sh'], k(1.05)); A.x(l, ['f'], k(1.05)); A.x(o, ['sot'], k(0.95))
            A.notas.append(f'{nom[l]} en bloque bajo: el rival saca más córners y remata más, pero menos al arco.')
        if 'presion_alta' in est:
            A.x(l, ['f'], k(1.08)); A.x(o, ['gk'], k(1.05))
            A.notas.append(f'{nom[l]} presiona alto: más faltas propias.')
        if 'centros' in est:
            A.x(l, ['c'], k(1.10))
            A.notas.append(f'{nom[l]} ataca por bandas y centros: más córners propios.')
        if 'balon_parado' in est:
            A.x(l, ['c'], k(1.04)); A.x(l, ['g'], k(1.03))
        if 'contragolpe' in est:
            A.sens[l] *= 1.2; A.x(l, ['off'], k(1.15))
            A.notas.append(f'{nom[l]} juega al contragolpe: cuando gana se repliega más (sensibilidad ×1,2).')
        if 'posesion' in est:
            A.sens[l] *= 0.85; A.x(o, ['f'], k(1.05))
            A.notas.append(f'{nom[l]} de posesión: sigue atacando aunque gane (sensibilidad ×0,85); el rival le hace más faltas.')
        if fz < 1 and est:
            A.notas.append(f'Estilo de {nom[l]} a media fuerza (ya está en sus promedios y en el precio).')
        pc = e.get('perfil_corners') or {}
        cen, cmed = pc.get('centros_pj'), pc.get('centros_media_liga') or C.CENTROS_MEDIA_LIGA
        if cen and cmed:
            fc = (cen / cmed) ** C.ELASTICIDAD_CENTROS
            A.x(l, ['c'], F('corners_perfil', fc))
            A.notas.append(f'{nom[l]} tira {cen} centros por partido contra {cmed} de media: córners propios ×{F("corners_perfil", fc):.2f} '
                           '(en tus datos, más centros → más córners; el efecto entra a 40 % porque ya está en el precio).')
        terr = pc.get('territorio_pct')
        if terr:
            ft = (terr / 50.0) ** C.ELASTICIDAD_TERRITORIO
            A.x(l, ['c'], F('corners_perfil', ft))
            A.notas.append(f'{nom[l]} hace {terr} % de sus acciones ofensivas en campo rival (territorio, no posesión): '
                           f'córners propios ×{F("corners_perfil", ft):.2f}. Hipótesis sin medir todavía.')
        marc = e.get('marcador')
        if marc == 'se_encierra':
            A.sens[l] *= 1.5; A.notas.append(f'{nom[l]} se encierra al ir ganando (sensibilidad ×1,5).')
        elif marc == 'sigue_atacando':
            A.sens[l] *= 0.5; A.notas.append(f'{nom[l]} sigue atacando aunque gane (sensibilidad ×0,5).')
        # Bajas con detalle (posición, peso y reemplazo). Si vienen, reemplazan a bajas_ataque/bajas_defensa de ese lado.
        det = [b for b in (ficha.get('bajas') or []) if b.get('lado') == nom[l] and b.get('confirmada', True)]
        explicitas = frescos   # incluye lo marcado por info_tardia
        for fresca in (True, False):
            grupo = [b for b in det if ((b.get('horas_desde_noticia') is not None and float(b['horas_desde_noticia']) < C.HORAS_FRESCO)
                                          or 'bajas' in explicitas) == fresca]
            if grupo:
                fg = fs = fr = 1.0
                txt = []
                fz = 1.0 if fresca else C.FUERZA_CONTEXTO['bajas']
                Fb = lambda f: 1 + fz * (f - 1)
                for b in grupo:
                    pos = (b.get('posicion') or '').lower()
                    rep = C.CALIDAD_REEMPLAZO.get(b.get('reemplazo') or 'titular', 0.7)
                    peso = b.get('peso')
                    if pos.startswith('del') or pos.startswith('ext'):
                        pe = float(peso) if peso is not None else 0.25        # parte de los goles del equipo
                        fg *= 1 - pe * (1 - rep); fs *= 1 - 0.6 * pe * (1 - rep)
                    elif pos.startswith('med'):
                        pe = float(peso) if peso is not None else 0.12
                        fg *= 1 - pe * (1 - rep); fs *= 1 - pe * (1 - rep)
                    elif pos.startswith('por'):
                        fr *= 1 + 0.10 * (1 - rep) / 0.3
                    elif pos.startswith('def') or pos.startswith('lat') or pos.startswith('cen'):
                        fr *= 1 + 0.06 * (1 - rep) / 0.3
                    txt.append(f"{b.get('jugador', '?')} ({pos or 'sin posición'}, reemplazo {b.get('reemplazo') or 'titular'})")
                fg, fs, fr = max(0.75, fg), max(0.80, fs), min(1.25, fr)
                A.x(l, ['g'], Fb(fg)); A.x(l, ['sh', 'sot'], Fb(fs)); A.x(o, ['g', 'sot'], Fb(fr))
                A.notas.append(f"{nom[l]} con bajas: {', '.join(txt)} → goles propios ×{Fb(fg):.2f}, goles del rival ×{Fb(fr):.2f}"
                               + (' (noticia de menos de 24 h: va completa)' if fresca else ' (conocida hace más de 24 h: ya está en parte en la cuota)'))
        ba = 0 if det else int(e.get('bajas_ataque') or 0)
        if ba:
            A.x(l, ['g'], F('bajas', 1 - 0.08 * ba)); A.x(l, ['sh', 'sot'], F('bajas', 1 - 0.05 * ba))
            A.notas.append(f'{nom[l]} sin {ba} atacante(s) clave: goles ×{1 - 0.08 * ba:.2f}.')
        bd = 0 if det else int(e.get('bajas_defensa') or 0)
        if bd:
            A.x(o, ['g'], F('bajas', 1 + 0.06 * bd)); A.x(o, ['sot'], F('bajas', 1 + 0.04 * bd))
            A.notas.append(f'{nom[l]} sin {bd} defensa(s) clave: goles del rival ×{1 + 0.06 * bd:.2f}.')
        if e.get('rotacion'):
            A.x(l, ['g', 'sh', 'sot', 'c'], F('rotacion', 0.93)); A.x(l, ['f'], F('rotacion', 0.95))
            A.notas.append(f'{nom[l]} rota titulares: producción ×0,93.')
        mot = e.get('motivacion', 'normal')
        if mot == 'baja':
            A.x(l, ['g', 'sh', 'c'], F('motivacion', 0.93)); A.x(l, ['f'], F('motivacion', 0.92)); A.x(l, ['y'], F('motivacion', 0.85))
            A.notas.append(f'{nom[l]} sin nada en juego: menos intensidad (tarjetas ×0,85).')
        elif mot == 'alta':
            A.x(l, ['sh', 'c'], F('motivacion', 1.04)); A.x(l, ['f'], F('motivacion', 1.04))
        if e.get('necesita_ganar'):
            A.necesita_ganar[l] = True
            A.notas.append(f'{nom[l]} necesita ganar: con empate después del 60′ se vuelca como si perdiera.')
        if e.get('sensibilidad') is not None:   # valor medido en su historial (perfiles.sensibilidad_marcador)
            A.sens[l] *= float(e['sensibilidad'])
    cal = []
    for l in (0, 1):
        e = ficha.get(nom[l]) or {}
        if e.get('dias_descanso') is not None and e['dias_descanso'] <= 3:
            cal.append(f"{nom[l]} con {e['dias_descanso']} días de descanso")
        if e.get('viaje_largo'):
            cal.append(f'{nom[l]} viene de un viaje largo')
        if e.get('fecha_fifa'):
            cal.append(f'{nom[l]} con convocados de la fecha FIFA')
    if ficha.get('fecha_fifa'):
        cal.append('partido junto a una fecha FIFA')
    if cal:
        A.notas.append('Calendario: ' + '; '.join(cal) + '. Sin efecto en los números (no hay evidencia firme); '
                       'queda en el registro para medirlo.')
    if A.notas:
        txt = ', '.join(sorted(frescos)) if frescos else 'ninguno'
        A.notas.append('Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio '
                       f'(config.FUERZA_CONTEXTO). Hechos frescos que van completos: {txt}.')
    return A
