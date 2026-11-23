# Diseño: BB diarias a fondo, regularidad ajustada por rival y recolección más rápida
Lunes 23-nov-2026, 11:35 Bogotá. Es una **propuesta**: nada de esto cambia las reglas de CLAUDE.md hasta que el usuario la apruebe. Cifras de `registro/` y de `jornadas/2026-11-22|23`. Límites al final.

## 1. ¿1–3 BB al día analizadas a fondo? Mi opinión
**Sí, pero como cambio de método, no como promesa de ganar más.**
- Lo que dicen los datos hasta hoy: BB Boost 15 de 64 (23 %) frente a un punto de equilibrio de ≈16 %, pero los aciertos se concentran en pocos partidos (4 de 12 partidos con algún combo ganador). El 21–22-nov, las BB de **un solo partido armadas a fondo** dieron 2 de 4 y las combinadas **entre partidos** 0 de 7. Son muestras diminutas: no prueban nada todavía (con p ≈ 25 % y 30 combos, el error estándar es ≈ 8 puntos; para distinguir 16 % de 23 % hacen falta ~100 combos).
- Lo que sí gana la profundidad: leer el **precio real en el cupón** (no el producto de cuotas), comprobar el **% del boost** (el 21-nov cobró +50 %, no +25 %), usar **onces oficiales** ~1 h antes, y elegir patas que **no se parezcan** (Betano comprime el precio cuando se parecen). Getafe fue así: 2 de 4 patas respaldadas y la que falló (tiros al arco) «cumplía» pero sin mirar contra qué rivales (ver §2).
- Reglas que propongo si se aprueba: máximo 3 BB por día, todas de **un solo partido** con datos completos; mínimo 3 patas con cuota > 1,50 y total > 5,05; precio real y % de boost leídos en el cupón; stake mínimo fijo (lotería); **cada combo se registra en `bb/bb_boost_resumen.json` en el momento de enviarlo**; la evaluación se hace al llegar a 30 y a 100 combos, contando **partidos**, no variantes.

## 2. Regularidad ajustada por rival y contexto (el caso Getafe)
**Problema, con sus datos:** los últimos 10 de Getafe en tiros al arco a favor fueron 1, 4, 5, 8, 1, 8, 4, 3, 1, 7. Los 1 son contra Villarreal, Athletic y Barcelona; los 8, 8 y 7 contra Lebrijana (Copa), Lugano y Málaga. Un «X de 10» que mezcla esos rivales dice poco sobre cómo le irá a Atlético (3.º en la tabla, 28 pts; Getafe 15.º, 12 pts). Lo mismo con el contexto genérico («necesita ganar» en la jornada 13 de 38).

**Diseño (tres capas, de lo más seguro a lo más opinable):**
1. **Rating de cada rival por mercado, calculado con datos, no con etiquetas.** Para cada equipo de la liga: lo que hace y lo que concede por partido (tiros al arco, remates, córners, faltas, tarjetas) en sus últimos 10, contra la media de la liga. Se arma con los feeds de Flashscore (`df_st`, ~0,1 s cada uno): para 20 equipos, ~200 llamadas ≈ 30 s. Se guarda en `datos_ligas/<liga>.json` y se actualiza solo con los partidos nuevos.
2. **Esperado ajustado.** Para cada partido pasado del equipo: observado ÷ (lo que ese rival suele conceder ÷ media de la liga). Con eso, el esperado de hoy = ataque del equipo × lo que concede el rival de hoy ÷ media. La ficha muestra tres cosas juntas: «X de 10» crudo, «X de 10 ajustado» (cuántas veces superó la línea **después** de ajustar por rival y sede) y «contra rivales parecidos al de hoy: k de n» (n pequeño, 3–5; **solo informativo**, nunca el criterio).
3. **Contexto específico por mercado, solo con hechos leídos.** Cada mercado tiene su lista de qué leer: tiros al arco/remates (qué concede el rival, bajas defensivas y de portero, guion esperado según 1X2 y total de Betano: el favorito suele tirar más y el débil depende de ir perdiendo), córners (igual + estilo), faltas/tarjetas (árbitro, rivalidad, presión de tabla), goles (bajas, rotación, tabla). «Necesita ganar» solo aparece si la tabla y las fechas que faltan lo respaldan (jornada 13 de 38 no cuenta). Sin lectura: «sin leer», nunca texto genérico.

**Para que no se degrade:** el ajuste se calcula por partido con datos de ese partido; no hay guiones reutilizables. Y **ninguna capa entra al análisis sin pasar el backtest**: en los 50.408 partidos de `pruebas/backtest/` (que traen tiros al arco, córners, faltas y tarjetas) se mide si el X de 10 **ajustado** acierta más que el crudo **a igual cuota/colchón**. Si no gana, se queda como información y no cambia ninguna p. Esto responde a lo que ya vimos: ni el filtro ni el contexto superaron al precio fuera de muestra.

**Riesgos que declaro:** al partir 10 partidos por nivel de rival, n es muy chico (por eso el ajuste es continuo y el «parecidos» es informativo); los ratings de rivales de ligas menores o copas tendrán muestra corta; el ajuste no ve bajas ni alineaciones pasadas.

**Orden de construcción propuesto:** (a) ratings por liga + «X de 10 ajustado» en la ficha y el dashboard; (b) backtest del ajuste contra el crudo; (c) listas de «qué leer» por mercado en `contexto_mercado.py`; (d) solo si (b) da ventaja, usarlo en las sugerencias.

## 3. Recolección más rápida (con lo que realmente pasó)
**Dónde se va el tiempo (12 partidos del 23-nov = 1 h 15 min, hoy ya mejor que lo de antes):** lo lento es la **tabla de jugadores**, que solo existe como página renderizada (iframe por partido pasado). Todo lo demás (resultados, goles, árbitro anunciado, estadísticas de equipo) sale de feeds en ~0,1 s.
**Fallos que ya conocemos y su arreglo:** «filas 0» por esperar 20 s (ahora 60 s); la pestaña se degrada tras ~80–100 cargas (pestaña nueva por lote); más de 3 iframes en paralelo se atascan; ligas menores sin tabla (8 de 23 el 22-nov: se declaran); onces sin publicar hasta ~1 h antes; paso de datos por archivo con hash (lento pero confiable); `javascript_tool` corta a 45 s.

**Mejoras propuestas, de mayor a menor ahorro:**
1. **Probar si la tabla de jugadores se puede pedir directo (sin iframe).** Prueba de ~15 min: abrir una tabla con `read_network_requests` y ver si hay un feed. Si lo hay, la parte lenta pasa de minutos a segundos y casi desaparece el problema de pestañas. **No está probado: no lo prometo.**
2. **Caché de partidos pasados.** Una tabla de un partido terminado no cambia. Guardar `cache/jugadores/<mid>.json` (una página trae los dos equipos) y no volver a pedirla. Con datos reales: de las 112 páginas del 23-nov, 26 (23 %) ya se habían bajado el 22-nov, y 5 se repetían dentro del mismo día (un partido entre dos equipos del día). En la misma liga semana tras semana el ahorro sube; en ligas nuevas es poco.
3. **Dos tiempos.** Noche anterior o madrugada: Betano, feeds, árbitros, tablas y jugadores históricos. ~1 h antes de cada partido: solo onces y cuotas (lectura corta, y de paso da el CLV). Se puede dejar como tarea programada que necesite el PC.
4. **Por niveles** (ya lo haces tú): solo goleador = solo feeds (rápido); estadística de jugador = historial completo. Dentro del historial, saltar la pestaña «Paradas» salvo que haya línea de atajadas.
5. **Un solo envío por lote** (un archivo por nivel con un hash), no uno por partido.
6. **Propuesta pre-armada de niveles**: leo los mercados y te mando ya la tabla «partido → nivel sugerido» para que solo corrijas, en vez de preguntar partido por partido.
**Meta realista sin la mejora 1:** 12 partidos en ~45–60 min; con la mejora 1 y la caché, menos de 20 min (estimación, a confirmar con la prueba).

## Límites
- La opinión sobre las BB se apoya en 4+7 combos y 64 variantes agrupadas: es una lectura, no una medición.
- El ejemplo de Getafe lo describe con los números de la ficha; la clasificación de rivales fuertes/débiles saldrá del rating propuesto (hoy no está calculado) y no de mi impresión.
- No se probó ningún feed nuevo de Flashscore para jugadores; el tiempo de la mejora 1 y la meta son estimaciones.
