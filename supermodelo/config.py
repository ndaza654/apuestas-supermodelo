# -*- coding: utf-8 -*-
"""Parámetros del supermodelo SM-1 (10-nov-2026). Todo número que mueve una probabilidad vive aquí, con su fuente.

Base: modelo v2 + calibración del 9-nov + calibración con datos reales del 10-nov (238 858 partidos públicos de
football-data.co.uk vía github.com/xgabora/Club-Football-Match-Data-2000-2025; detalle en docs/CALIBRACION_10NOV.md).
Regla de oro: siguen siendo PUNTOS DE PARTIDA. El registro mide cada familia de mercado y cada tipo de partido; con
30+ casos de un grupo, estos valores se recalibran con los datos propios (balance.py lo sugiere).
"""

# ---------------------------------------------------------------- perfiles de equipo (heredado del kit v1)
DECAY = 0.92          # peso de cada partido anterior (el más reciente pesa 1, el anterior 0.92, ...)
SHRINK_K = 3.0        # encogimiento hacia el promedio del grupo de equipos (kit v1)
W_OPP = 0.40          # media del partido = 0.6 * lo que produce el equipo + 0.4 * lo que concede el rival
MIN_PARTIDOS = 6      # con menos, la confianza baja (no se bloquea: se avisa)

# ---------------------------------------------------------------- el mercado es el punto de partida
# Prueba con 17 partidos reales del 5-nov (pruebas/backtest_5nov.py): la probabilidad sin margen de Betano
# calibró MEJOR que el modelo de promedios v1 y que mezclar 50/50 con él; las líneas "de valor" del modelo de
# promedios perdieron 16–19 %. Por eso el v2 ancla las medias al mercado y se mueve por dos vías:
#   1) el modelo de perfiles solo como alerta (W_MODELO_MEDIA = 0: apagado hasta que el registro diga que ayuda),
#   2) el contexto (ficha): hechos concretos que el mercado puede no haber puesto en el precio.
# Peso del modelo de perfiles al fijar las medias (media geométrica mercado^(1-w) · modelo^w).
W_MODELO_MEDIA = 0.0   # 0 = solo mercado. Subirlo solo si el registro demuestra que el modelo de perfiles ayuda.
# Peso del mercado sin margen al mezclar la probabilidad (corrige la forma de la distribución simulada).
# 10-nov-2026 (supermodelo): con la simulación recalibrada con 62 000 partidos, el simulador SOLO ya iguala al mercado
# en el backtest del 5-nov (Brier 0,2323 contra 0,2322; antes 0,2331); mezclando 50/50 queda igual al mercado también en
# log-loss (0,6566). El 9-nov el modelo fue algo mejor que el mercado (0,1900 contra 0,1937, n=153, ruido). 0,5 es el
# punto medio defendible y reemplaza la columna «Combinada» (50 % modelo + 50 % mercado) de los informes del 9-nov.
W_MERCADO = {
    'goles': 0.50, 'ambos': 0.50, 'resultado': 0.50,
    'corners': 0.50, 'tarjetas': 0.50, 'faltas': 0.50, 'remates': 0.50, 'al_arco': 0.50,
    'fueras': 0.50, 'saques_meta': 0.50, 'saques_banda': 0.50,
    'jugador': 0.70, 'pareja': 0.70, 'especial': 0.50,
}
# El mercado se mezcla con la probabilidad SIN contexto; el movimiento que aporta el contexto se suma completo.
# Jugadores: el reparto por jugador del simulador es aproximado, así que pesa más lo que dice Betano (0,70).
# Peso del mercado al fijar la tasa de goles (lambda): el mercado de goles es el mejor ajustado.
W_MERCADO_GOLES = 0.80

# Cómo se quita el margen: 'potencia' (validado con 160 000 partidos, ver mercado._potencia) o 'proporcional'.
METODO_SIN_MARGEN = 'potencia'

# ---------------------------------------------------------------- simulación
N_SIM = 20000
MIN_1T = 47           # 45 + descuento medio del 1.er tiempo
MIN_2T = 50           # 45 + descuento medio del 2.º tiempo (IZA DP 17512: ~5,2 min de añadido)
SEED = 7

# Forma temporal: el 2.º tiempo produce más (≈56 % de los goles) y los primeros minutos de cada mitad arrancan
# más lentos (arXiv 2508.04008: la producción sube los primeros ~5 min de cada mitad y luego es estable).
PESO_1T = 0.92
PESO_2T = 1.07
RAMPA_MIN = 5
RAMPA_FACTOR = 0.80

# ---------------------------------------------------------------- efectos del marcador (perspectiva del equipo)
# d = goles propios − goles del rival. Valores por defecto a partir de:
#  · StatsBomb "Score Effects": el que va +1 baja su cuota de remates a 46,6 % y el que va −1 la sube a 53,4 %.
#  · arXiv 2508.04008 (5 grandes ligas 2008–2023): los ajustes implican que ir perdiendo sube la producción
#    ~10–40 % y ir ganando la baja ~10–45 % según la ventaja; efectos parecidos en remates y córners.
#  · Balance propio 4–8 nov (72 partidos): el que ganaba al descanso perdió 9,5 pts de cuota de remates y
#    5,9 pts de cuota de córners en el 2.º tiempo; el que perdía los ganó.
# 10-nov: el que va perdiendo al descanso marca 13 % más en el 2.º tiempo que si fuera empatado (76 000 partidos; sim 9 %);
# el que gana, −2 % (sim −5 %). Esto genera más empates y más Ambos Marcan que el Poisson independiente, como en la realidad
# (+1,9 y +2,25 pts; sim +1,7 y +2,3). Córners: el que gana deja de sacarlos (más fuerte que en el v2: real corr −0,12).
EFECTO_MARCADOR = {
    #        d<=-2  d=-1  d=0   d=+1  d=+2  d>=+3
    'sh':   (1.30, 1.17, 1.00, 0.86, 0.74, 0.64),
    'c':    (1.30, 1.18, 1.00, 0.80, 0.68, 0.60),
    'off':  (1.15, 1.08, 1.00, 0.97, 0.92, 0.88),
    'f':    (0.95, 0.97, 1.00, 1.04, 1.02, 0.95),
}
# Calidad del remate según el marcador: el que va ganando remata menos pero mejor (contraataques);
# el que va perdiendo remata más pero peor (StatsBomb: % de gol mayor en +1 que en −1).
CALIDAD_MARCADOR = {  # multiplica la prob. de que un remate vaya al arco y de que el remate al arco sea gol
    'sot': (0.98, 0.99, 1.00, 1.01, 1.02, 1.02),
    'gol': (1.02, 1.02, 1.00, 1.00, 1.00, 1.00),
}
# Superioridad numérica (arXiv 2508.04008: la expulsión es el efecto más grande por partido).
EFECTO_HOMBRES = {  # clave = jugadores propios − jugadores rivales
    -2: {'ataque': 0.40, 'gol': 0.75}, -1: {'ataque': 0.60, 'gol': 0.85}, 0: {'ataque': 1.0, 'gol': 1.0},
     1: {'ataque': 1.30, 'gol': 1.12},  2: {'ataque': 1.60, 'gol': 1.20},
}

# ---------------------------------------------------------------- factores latentes del día
# Dos factores simétricos entre los equipos, exp(±sigma·Z), con Z independientes:
#  · TERRITORIO: quién pisa el campo rival hoy → remates y córners del equipo (no su calidad).
#  · DOMINIO: quién está mejor de lo que decía el precio en la calidad del remate (sot) y en volumen (sh).
# 10-nov (62 164 partidos, condicionando a liga, goles esperados y diferencia de fuerza del precio):
#   corr(dif. goles, dif. remates) 0,14 (sim 0,12) · con dif. al arco 0,50 (sim 0,48) · con dif. córners −0,12 (sim −0,11)
#   corr(córners local, córners visitante) −0,18 (sim −0,18).
# El v2 (72 partidos propios) usaba un solo factor con 'q' 0,15–0,30: daba corr con remates 0,30 y bajaba Ambos Sí y el
# empate 4–5 pts frente a la realidad (el residuo «Ambos Sí bajo el mercado» del 9-nov era ESTE sesgo, no información).
DOMINIO = {'sh': 0.10, 'c': 0.0, 'q': 0.0, 'sot': 0.12}
TERRITORIO = {'sh': 0.14, 'c': 0.25}
# Volumen contra calidad: q ∝ (ritmo·forma·territorio)^(−0,30). Real: corr(goles, remates) total 0,23; sim 0,34 sin esto y
# 0,33 con esto (queda algo alta: para las parejas de patas donde pesa está dependencia.py).
CALIDAD_VOLUMEN = 0.30
# Córners que nacen de un remate (rechazo o atajada al córner): Binomial(remates, 0,09). Da la corr remates–córners real
# (0,28; sim ≈0,23–0,24) sin inflar la dispersión de córners (var/media real 1,11; sim ≈1,15–1,16).
CORNER_POR_REMATE = 0.09

# ---------------------------------------------------------------- en vivo
# Forma del previo gamma de la intensidad de gol de cada equipo que se actualiza con los goles que van (solo en vivo).
# Más bajo = lo que va del partido pesa más. 0 = no actualizar. Probado con 400 partidos reales desde el descanso: 6 da
# el mejor Brier conjunto (Más 2.5, Ambos, 1, X); con 0-0 al HT predice 1,32 goles en el 2T (real 1,22; sin actualizar 1,47).
VIVO_FORMA_GOLES = 6.0

# ---------------------------------------------------------------- tarjetas (puntos de Betano: amarilla 1, roja 2)
# Partido cerrado y tarde = más tarjetas; goleada = menos. Real (62 000): por |dif. final| 0/1/2/3+ = 1,03/1,05/0,95/0,82
# de la media (sim 1,04/1,04/0,97/0,84).
TARJETA_CERRADO_TARDE = 1.30   # |d|<=1 y minuto >= 70
TARJETA_GOLEADA = 0.65         # |d|>=3
# Compensación del árbitro (IZA DP 17512): da más amarillas al equipo que lleva menos. Con 0,25 las amarillas de cada
# equipo quedan infra-dispersas como en la realidad (var/media 0,85; sim 0,83).
COMPENSACION_AMARILLAS = 0.25  # factor exp(0,25 · (amarillas rival − amarillas propias)), acotado
COMPENSACION_TOPE = (0.70, 1.40)
# Rojas: real 0,099 por equipo y partido (incluye doble amarilla); sim 0,097.
ROJA_DIRECTA_90 = 0.040        # rojas directas por equipo y partido (base, antes de contexto)
PROB_SEGUNDA_AMARILLA = 0.035  # por cada amonestado propio, prob. de que la nueva amarilla sea la 2.ª
# Amarillas sin falta (protestas, pérdida de tiempo, simulación): StatsBomb, «casi ninguna al inicio, cerca de la mitad
# al final»; la amarilla media llega al 59 % del partido. Con 30 % sin falta, la corr faltas–tarjetas queda en 0,25
# (real 0,29; el v2 daba 0,58) y el 1.er tiempo se lleva el 34 % de las tarjetas (el v2 daba 41–43 %: por eso «Más 1.5
# tarjetas 1T» salía 5–10 pts sobre el precio el 9-nov).
TARJETA_SIN_FALTA = 0.30
TARJETA_SIN_FALTA_RAMPA = 1.0  # ritmo de las amarillas sin falta ∝ (minuto/48)^1
TARJETA_RAMPA = 0.08           # propensión a amonestar por falta: 1 + 0,08·(min−48)/48
TARJETA_EXP_DUREZA = 0.0       # (sin usar) tarjetas por falta ∝ dureza^EXP

# ---------------------------------------------------------------- sobredispersión (variación entre partidos)
# Factores gamma por simulación (forma alta = poca variación): "ritmo" compartido (remates, córners, saques), "dureza"
# compartida (faltas) y uno propio de cada equipo y estadística. Objetivo: la dispersión REAL condicionada a lo que sabe
# la casa (OLS por liga-temporada con efecto de cada equipo + precio): var/media córners equipo 1,34 / total 1,11;
# remates 1,41 / 1,18; al arco 1,06 / 1,05; faltas 0,97 / 1,06; tarjetas total 1,23; goles total 0,95.
# Sim con estos valores: córners 1,40 / 1,16; remates 1,23 total; al arco 1,08; faltas 1,02 / 1,02; tarjetas 1,24; goles 1,01.
# El v2 (FORMA_RITMO 40, DUREZA 14) daba faltas 3,2 y córners total 1,47: colas muy anchas.
FORMA_RITMO = 150.0
FORMA_DUREZA = 1000.0
FORMA_EQUIPO = {'sh': 200.0, 'c': 60.0, 'f': 2000.0, 'y': 60.0, 'off': 10.0, 'gk': 14.0, 'ti': 25.0}

# ---------------------------------------------------------------- contexto
# El estilo habitual de un equipo (bloque bajo, centros, posesión...) ya está en sus promedios y en el precio de
# Betano: se aplica a media fuerza. Solo va a fuerza completa si la ficha marca que es un cambio reciente
# (entrenador nuevo, sistema nuevo) con "estilo_nuevo": true.
# Más general: cada hecho de contexto se aplica en la parte que se supone que Betano todavía no puso en el precio.
# Un hecho "fresco" (alineación confirmada, lesión de última hora, cambio de árbitro, clima del día) va completo:
# en la ficha, "frescos": ["bajas", "clima", ...]. Recalibrar con registro.informe(): grupo "por hecho de contexto".
FUERZA_CONTEXTO = {'estilo': 0.5, 'arbitro': 0.6, 'derbi': 0.6, 'importancia': 0.5, 'clima': 0.7,
                   'bajas': 0.6, 'rotacion': 0.7, 'motivacion': 0.5, 'corners_perfil': 0.4}
# Perfil de córners (idea tomada de un tipster, medida con 70 partidos propios): los centros por partido explican
# los córners del equipo (r = 0,70; elasticidad log-log 0,70, pero mezclada con la fuerza del equipo, por eso
# se usa la mitad). Los centros altos de UN equipo ya están en su media y en el precio: entran a 40 % de fuerza
# y solo cuando se alejan de la media de la liga. El % de acciones ofensivas en campo rival (territorio) no se
# pudo medir con datos propios; entra más flojo todavía y queda en el registro como hecho para medirlo.
ELASTICIDAD_CENTROS = 0.35
ELASTICIDAD_TERRITORIO = 0.25
CENTROS_MEDIA_LIGA = 17.7   # centros por equipo y partido en los 70 partidos del balance (cambiar por la liga)
# Tope del efecto combinado por estadística (muchos hechos a la vez se solapan: el bloque bajo del rival y los
# centros propios explican en parte lo mismo). 1,10 = como mucho ±10 % sobre la media que da el mercado.
TOPE_CONTEXTO = 1.10
# Un hecho conocido hace menos de HORAS_FRESCO horas cuenta como fresco (Ingeniero Analista #296: la noticia de
# más de 24 h ya está en la línea; la ventana útil es justo después de las alineaciones).
HORAS_FRESCO = 24
# Calidad del reemplazo de una baja (1 = igual de bueno). Puntos de partida sin medir; el registro los recalibra.
CALIDAD_REEMPLAZO = {'titular': 0.7, 'suplente': 0.55, 'suplente_flojo': 0.5, 'juvenil': 0.4}
TOPE_CONTEXTO_FRESCO = 1.25

# ---------------------------------------------------------------- escenarios
FAMILIAS_DEL_MARCADOR = ('goles', 'ambos', 'resultado')
UMBRAL_ESCENARIO_RELEVANTE = 0.12   # para medir la robustez de una línea solo cuentan guiones con >= 12 %
# Etiquetas (informativas, no reglas)
P_ALTA = 0.65            # probabilidad alta
ROBUSTEZ_ALTA = 0.50     # aguanta en todos los guiones relevantes
MOV_CONTEXTO = 0.04      # el contexto movió la probabilidad al menos 4 puntos
GOL_TEMPRANO_MIN = 35

# ---------------------------------------------------------------- alertas (Ingeniero Analista: abstenerse cuando el
# modelo discrepa mucho del mercado sin una razón; sus 7 'valores' acertaron 2 contra 5,2 esperados)
ALERTA_DISCREPANCIA = 0.15   # la simulación sin contexto se aleja ≥15 pts del precio sin hecho fresco → revisar datos
ALERTA_CONTEXTO = 0.10       # el contexto mueve ≥10 pts sin hecho fresco → revisar la ficha

# ---------------------------------------------------------------- enfoque de mercados por contexto (enfoque.py)
# Umbrales de la lectura cualitativa «qué mercados le quedan bien a este partido». Puntos de partida sin medir; el
# registro dirá si los mercados marcados «a favor» salen mejor que los demás.
ENFOQUE_FAV_CLARO = 0.60      # prob. de ganar del favorito (simulación) para llamarlo favorito claro
ENFOQUE_FAV_LEVE = 0.45
ENFOQUE_GOLES_ALTO = 2.9
ENFOQUE_GOLES_BAJO = 2.3
ENFOQUE_EQUIPO_FLOJO = 0.80   # goles esperados de un equipo por debajo de esto: Ambos marcan en contra
ENFOQUE_EQUIPO_ANOTA = 1.10
ENFOQUE_CORNERS_DIF = 1.0     # córners totales esperados vs liga / precio
ENFOQUE_CORNERS_EQUIPO = 1.2  # diferencia de córners esperados entre los dos equipos
ENFOQUE_ARBITRO_ALTO = 1.15
ENFOQUE_ARBITRO_BAJO = 0.85
