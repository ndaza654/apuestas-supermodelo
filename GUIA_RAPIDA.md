# Supermodelo SM-1.2 — guía rápida para los chats del proyecto (11-nov-2026)

> **Nota del 23-nov-2026:** este documento es de la etapa de diseño del modelo (11-nov). Las reglas vigentes de proceso (muestra de 10, historial de jugadores, árbitro, BB Boost, balances) están en `CLAUDE.md`; donde se contradigan, manda `CLAUDE.md`. Los «hallazgos» de abajo son del 10-nov y se midieron con otra muestra.

Reemplaza a «Modelo v2 (versión final) — guía rápida». Paquete: `supermodelo` (README.md). Un solo paquete: ya no hay v2 ni v3.

## Reglas fijas del usuario (11-nov-2026)
1. **Orden:** primero se leen los mercados y líneas que Betano ofrece en ESE partido (JSON de la página, `docs/LEER_BETANO.md`); luego se analizan.
2. **Jugadores siempre:** con alineación confirmada o, si no la hay, la PROBABLE de cualquier fuente (también la de Betano). Solo se omite el mercado si no hay nada en ningún sitio.
3. **Mercados que siempre se miran cuando existen:** «cualquiera de los jugadores…» (asistencia, anota, anota o asiste, tarjeta) y el resultado al descanso/final (HT/FT y «resultado medio tiempo o tiempo completo»).
4. **Bajas del día:** Betano no retira las líneas del lesionado (Lukaku, 11-nov): se marca `fuera: true` y sus parejas quedan en «no apostar».

## La idea en 6 líneas
1. La base es el precio de Betano sin margen, quitado con el **método de potencia**. Con 160.000 partidos calibra mejor
   que repartir el margen en proporción: el lado favorito queda 1–3 pts más probable.
2. El simulador minuto a minuto está **calibrado con 62.000 partidos reales**. Reproduce la dispersión de córners,
   remates, al arco, faltas y tarjetas, los empates y Ambos Marcan de más que trae el efecto marcador, el reparto por
   tiempos y la dependencia entre patas.
3. La probabilidad de decisión es 50 % simulación + 50 % mercado, más lo que agrega el contexto. Sin contexto fresco el
   modelo casi no se aleja del precio, y está bien: así fue en todas las pruebas.
4. La ventaja posible sale de cuatro cosas:
   - hechos frescos (menos de 24 h: alineación, baja, árbitro, clima);
   - la línea que aguanta los guiones probables;
   - el precio del cupón (cuota mínima);
   - patas que se ayudan.
5. Nada se descarta por regla. Cada línea trae el guion donde gana, el que la mata, su robustez, su cuota mínima y sus
   alertas.
6. Todo va al registro y se cierra solo con las estadísticas reales. El balance semanal responde las 5 preguntas, y el
   CLV dice antes que nadie si se está tomando buen precio.

## Lo que aprendimos el 10-nov con datos (y que cambia cómo leer los informes)
- **El mercado le gana a los promedios de goles en todas las ligas.** Apostar donde un Poisson de promedios "ve valor"
  rinde −14 % a −17 %, peor que apostar a todo al azar (−6,8 %). Por eso el ancla es el precio.
- **Ningún sistema de filtros de tipsters supera el margen.** Se probaron 20 en 160.000+ partidos con cuotas: Ingeniero
  Analista (#400, #453, #14, #5, #26, #45, #420, #429, #16), Jeke («contra el último»), Sharpods («Menos por sesgo del
  público»), «seguir favoritos». Con la **mejor cuota del mercado** varios quedan cerca de 0 %: el precio que se toma
  pesa más que el filtro.
- **Empate y Ambos Sí:** el precio ya los trae bien. El Poisson los subestimaba unos 2 pts y el simulador nuevo lo
  corrige. El «Ambos Sí bajo el mercado» del 9-nov era ese sesgo.
- **Tarjetas del 1.er tiempo:** una de cada tres tarjetas, no 41 %. Tarjetas = amarilla 1, roja 2; la roja directa ahora
  cuenta 2 (antes 1).
- **Combos:** «gana el favorito + córners del favorito Más» se estorban (0,88), y «Más 2.5 + córners Más» también un poco
  (0,98). En cambio «gana el favorito + sus tiros al arco Más» se ayudan (1,27), igual que «gana el favorito + Más 2.5»
  (1,20). El informe ya corrige esto.
- **Volumen de un equipo:** ganar y rematar más va junto, pero poco (0,14). Con tiros al arco sí, fuerte (0,50). El
  «Menos remates del favorito» no muere tanto como creíamos; el «Menos al arco del favorito», sí.
- **En vivo:** un 0-0 al descanso es un partido de menos gol del que decía la cuota. El modo en vivo lo actualiza.

## Cómo leer el informe nuevo (SM-1.1)
Sigue la hoja de partido Toulouse–Estrasburgo y agrega lo del modelo:
- **Media esperada en cada bloque** (goles, córners, tarjetas, remates, tiros al arco, faltas, fueras, saques): la media de los
  partidos simulados con el contexto de la ficha, al lado de lo que espera Betano, la media sin ficha y el rango del 80 %. Si la media del modelo
  y la de Betano son iguales, no hay señal en ese mercado; si difieren, hay que poder explicar por qué (un hecho fresco) o revisar el dato.
- **Lectura de cada línea:** «casi sobre la línea: moneda al aire» (el lado probable < 56 %), «el lado X es el probable» o «queda lejos: paga muy
  poco y el otro es lotería» (> 80 %).
- **Proyección del partido:** por equipo, modelo contra Betano (y a favor / en contra si la ficha trae `forma`).
- **Más y Menos lado a lado** con probabilidad, EV, cuota mínima y robustez; «veces que salió Más» si hay `forma`.
- **Veredicto en cajas:** líneas con valor, builder, jugadores y riesgo (cuota ≥ 2.40), lo que no haría.
- **Jugadores:** mejores líneas, líderes esperados y una tarjeta por jugador (esperado hoy, /90 y barras si hay `jugadores_hist`).
- En vivo, `--vivo` trae la **media final esperada** del partido: lo que ya pasó más lo que falta.

## Flujo
1. **Filtro:** elige los partidos. No descarta por mercado.
2. **Lector de contexto** (`prompts/lector_de_contexto.md`): llena la ficha con hechos y fuentes. Incluye las bajas una
   por una (posición, peso, reemplazo, horas desde la noticia), la información tardía, el calendario, las rachas y H2H
   (solo para medir) y el consenso del público.
3. **Cuotas:** se copian las de Betano en la entrada, y los combos con la cuota del **cupón**, no la de la tarjeta.
4. **Modelo:** `python3 -m supermodelo partido.json --registro registro.csv`. Genera el informe .md, el .html y el .json.
5. **Selector:** cruza su lectura con el informe.
   - Una línea va si el guion que la mata no es el que la lectura ve probable y si Betano paga la cuota mínima.
   - Si una línea trae **⚠ alerta**, primero se revisan los datos.
   - Un combo es «valor» solo si su EV ajustado es ≥ +3 % y aguanta el stress (una pata 5 pts peor). Dos boletos que
     dependen de la misma idea del partido cuentan como una apuesta.
6. **Antes del partido:** alineaciones. Si cambia algo, se pone en `info_tardia` y se vuelve a correr el modelo.
7. **En vivo:** solo como continuación del plan, con `--vivo` y el estado del partido. Si la línea no estaba en el plan
   previo, es una entrada por reacción.
8. **Después:** `--cerrar registro.csv "Local - Visitante" real.json cierres.json` califica todo y guarda el partido en
   la base propia de la liga. Cada semana se corren `--balance` e `--informe`, y `--sombra` para las fuentes externas.

## Enfoque de mercados por contexto (regla del usuario, 11-nov-2026)
Antes de analizar líneas, el informe abre con un bloque que dice qué mercados le quedan bien al contexto del partido y cuáles
no (p. ej. «este es mejor para córners que para tarjetas»): favorece / neutro / en contra / sin señal, cada uno con su porqué en
palabras (`enfoque.py`, umbrales `ENFOQUE_*` en config). El análisis a fondo va primero a los mercados «favorece»; las líneas
de esos mercados llevan «★ enfoque a favor» (o «enfoque en contra») en la etiqueta. No cambia ninguna probabilidad ni EV:
es una hipótesis que orienta; si el número dice otra cosa, manda el número. No es la tabla de guiones.
Orden: 1) mercados que ofrece Betano → 2) hechos de la ficha → 3) enfoque → 4) análisis a fondo de los favorecidos → 5) número.

## Guiones (solo para medir la robustez de una línea; cada partido simulado cae en uno)
- Expulsión antes del 70′ (ahora ~11 %: las rojas reales son 0,1 por equipo).
- Sorpresa.
- Partido abierto.
- Favorito golpea temprano.
- Favorito gana trabado.
- Empate.

**Robustez** = probabilidad de la línea en el peor guion con ≥12 % de probabilidad.

## Claves por mercado (hipótesis; el registro las reemplaza con tus datos)
- **Goles y resultado:** son los mercados más eficientes. Solo hay valor con un hecho fresco sobre la fuerza de un equipo
  o sobre quién necesita ganar.
  - Más 2.5 muere en «favorito golpea temprano y administra».
  - El hándicap −1 muere con cualquier victoria por un gol.
  - Los favoritos muy claros pierden menos margen que los no favoritos: cuota ≤1,30 → −0,4 %; no favorito >8 → −29 %.
- **Córners:**
  - Dependen del guion: el que gana deja de sacarlos y el que pierde los fabrica. Los del favorito mueren si marca
    temprano; los del no favorito suben si el favorito se adelanta. Los totales altos mueren en goleadas y partidos cortados.
  - Las colas (Menos 6.5, Más 13.5) son más finas de lo que creía el v2.
  - Los centros entran a 40 % de fuerza.
- **Tarjetas y faltas:**
  - Árbitro (con la media de la liga del prior), derbi, importancia y partido cerrado al final.
  - Una de cada tres tarjetas cae en el 1.er tiempo.
  - Las amarillas de un equipo se compensan con las del otro.
- **Remates y al arco:** el que gana remata un poco menos, y ganar se nota mucho más en los tiros al arco que en los
  remates.
- **Fueras, saques de meta y de banda:** entender de dónde salen (contragolpe contra línea alta; remates desviados del
  rival; juego por bandas) y mirar la columna de colchón.
- **Builders:** Betano también descuenta la correlación; el builder solo vale si el cupón llega a la cuota mínima del informe.
- **Jugador:**
  - Lo que más pesa es la titularidad y los minutos.
  - «Popular» queda en el registro para medir si las estrellas se pagan de menos.
- **En vivo:** el estado actual más lo observado (remates, córners, faltas, goles) actualizan el ritmo.

## Formatos que conviene saber
- **Hándicap:** `h` es siempre el del LOCAL. Con 3 opciones (local/empate/visitante) es el europeo; con 2 y `h` entero o
  de cuarto es asiático (con devolución).
- **Líneas enteras y de cuarto:** 2.0, 2.25 y 2.75 se evalúan con devolución y medias (la etiqueta dice «asiática:
  devuelve X %»).
- **Doble oportunidad:** se deriva del 1X2; una opción suelta usa un margen típico de un lado.
- **Tarjetas en vivo y al cerrar:** amarillas incluida la 2.ª de una expulsión, rojas todas y rojas directas aparte.
  Al cerrar, mejor dar `tarjetas_betano` ya en puntos.

## Fuentes externas
StatArea, Forebet, la app de Sharpods y los picks de TikTok o Telegram van en **sombra**
(`sombra.csv` → `--sombra`). No se usan para decidir hasta tener ≥300 picks por mercado y ventaja con 95 % de
confianza. Lo que ya se sabe: los porcentajes 1X2 de StatArea están bien calibrados, pero su Más 1.5 y su Ambos están
peor que la base, y su tip X acertó 7 de 40.

## Archivos de datos
| Archivo | Contenido |
|---|---|
| `datos/prior_liga.csv` | Base de 38 ligas |
| `datos/sistemas_historial.json` | Auditoría de sistemas |
| `datos/dependencia_pares.json` | Dependencia real entre patas |
| `datos/partidos.csv` | Base propia, se llena al cerrar partidos |
| `docs/MAPA_DE_ORIGEN.md` | De dónde salió cada pieza |
| `docs/CALIBRACION_10NOV.md` | Todas las cifras |

## Lo que sigue vigente del balance 4–8 nov (151 líneas sugeridas; muestras chicas, son alertas y no reglas)
- En conjunto, 72 de 151 (48 %) contra ~50 % del precio: el modelo viejo no le ganó a Betano. Su «valor» no predijo nada
  (VALOR 5/11; «justa» 10/14).
- Los fallos fueron lecturas equivocadas, no mala suerte: de 37 fallos con medida, 12 perdieron por 3 o más y 7 por 1 o menos.
- Por mercado, contra el precio:
  - En contra: remates −12 pts (Más 2/9), goles Menos −20 pts (2/6), córners Más 6/15. Italia 4/14.
  - A favor: fueras Menos 4/5, faltas Menos 4/6, tiros al arco, tarjetas.
- Por familia:
  - Goles Más totales 11/11 y goles del no favorito Más 0.5 1/3.
  - Córners totales Más 9/29.
  - Tarjetas Menos 5/5 y Más 3/6.
  - Al arco de equipo Más 7/8 y remates de equipo Más 3/9.
  - Jugador: anota o asiste 6/6, al arco 5/7 (fallaron los mediocampistas), anota solo 1/4, entradas 0/3.
- Un boleto de 3 patas de ~50 % gana ~12 %. 15 boletos se perdieron por una sola pata. Acierto por selección 59 %, por
  boleto 27 %. En vivo 3 de 13 boletos (−95.370).
- Ingeniero Analista: «no pagues la fama», y los centros sí explican los córners en tus datos (r = 0,70 en 70 partidos).

## Del 9-nov (6 partidos)
- 11 goles reales contra 17,2 esperados: en un día así, todo lo que favorece goles queda peor, también el método de potencia.
- Las 4 «líneas con valor» (no favoritos a 3,65–5,20) perdieron. Coincide con la auditoría: los no favoritos largos
  pierden más margen (−29 % por encima de 8).
- Combos de misión 0/3: dependían de la misma idea («muchos goles y córners»). Ahora `cartera` lo avisa y la
  corrección de dependencia baja «Más 2.5 + córners Más».
