# Combinadas · Países Bajos - Grecia · 2026-11-13 14:45 (Bogotá) · jornada 2026-11-13

Elaborado el 12-nov-2026 (horas en Bogotá). Fuentes: `agentes/<clave>_{corners,partido,jugadores,goles-resultado,tarjetas}.md` (patas «cumple» + cuota ≥ 1.20), `entradas/<clave>.json` y `supermodelo.combos.evaluar()` (p, p_sim, cuota justa/mínima, stress, margen, correlación, guion, robustez, avisos). Los números del modelo se recalcularon con `python3` (mismo motor que `--combos`; ver «Método»).

## Enfoque de mercados
Las combinadas son del MISMO partido y solo con patas que (a) el agente de su mercado marcó «cumple» (≥5 de 7 en ambos equipos; jugadores ≥5 de ≤7 con titular probable), (b) tienen cuota ≥ 1.20 en Betano (leída el 12-nov ~12:32 Bogotá) y (c) están en el modelo con la misma cuota (verificado: todas coinciden). No hay dos patas del mismo mercado/ámbito en la misma dirección (líneas anidadas), ni una pata que implique otra (p. ej. «Ambos 1+ tarjetas Sí» + «Tarjetas Alemania Más 0.5» se descartó por anidada).

## Límites que condicionan TODO lo de abajo (leer primero)
- **Precio real**: no tengo el precio del cupón de Betano. «Cuota producto» es el producto de las cuotas individuales y es un TECHO; el cupón de Betano puede pagar menos que el producto (o no ofrecer la combinación): no lo he podido ver. El EV se muestra solo como «si el cupón pagara el producto» (p·producto−1); con el precio real del cupón se recalcula. El usuario puede dar el precio del cupón.
- **Alertas del modelo**: caen en córners 1T, córners por equipo / «más córners», tarjetas (algunas líneas de equipo) y saques de banda 1T. Las patas de goles/resultado no tienen alerta, pero el modelo toma sus goles esperados de las cuotas de Betano (`fuente_objetivos` = «mercado»), así que su probabilidad de goles NO es una confirmación independiente del mercado. La p conjunta mezcla simulación y mercado (`p`/«ajust.»); `p_sim` es la conjunta pura de la simulación.
- **Regularidad ≠ probabilidad**: «X de 7» con rivales de nivel muy distinto; p del modelo y regularidad son dos lecturas distintas, y ninguna está calibrada contra resultados verificados.
- **Dependencia entre combinadas**: dentro de un mismo partido las combinadas listadas comparten pata o guion (se dice en cada una). Entre partidos, las de «córners Más + goles Más/Menos» en 6 partidos dependen de la misma idea (muchos córners): contarlas como una apuesta repetida (ver «Cartera»).
- **Hándicap**: ninguna línea de hándicap tiene «cumple» de un agente (la ficha de goles no trae regularidad de diferencia de goles ni de ganó/no perdió). Por eso no entra a las combinadas. Abajo hay una tabla DERIVADA por mí de `goles.series` (diferencia de goles; solo victoria completa cuenta; no es criterio oficial de la ficha).
- No se evaluó: pago real de líneas asiáticas dentro de una combinada (solo se usaron líneas .5 en las combinadas; ninguna lleva devolución), jugadores sin alineación confirmada (las alineaciones son «probables», Flashscore ~13:00 Bogotá del 12-nov), 1T/2T (sin estadística por tiempo), cuota de cupón real.


### Países Bajos - Grecia  (2026-11-13 14:45 Bogotá)
Favorito según modelo/mercado: Países Bajos (p_resultado {'local': 0.618, 'empate': 0.222, 'visitante': 0.16}). Alertas del modelo en este informe: 2 (líneas con alerta: Tarjetas Grecia Más 0.5, Tarjetas Grecia Menos 0.5, Saques de banda 1.er tiempo Más 16.5, Saques de banda 1.er tiempo Menos 16.5).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Más 6.5 @1.2 (L 7 de 7, V 6 de 7, D 3 de 3); Córners Más 7.5 @1.38 (L 5 de 7, V 6 de 7, D 3 de 3); Córners Grecia Más 2.5 @1.45 (L 6 de 7, V 5 de 7, D 2 de 3); Córners Grecia Más 3.5 @2.07 (L 5 de 7, V 5 de 7, D 1 de 3); Fueras de lugar Países Bajos Más 1.5 @1.7 (L 5 de 7, V 5 de 7, D 1 de 3); Saques de banda Más 32.5 @1.91 (L 5 de 7, V 5 de 7, D 1 de 1); Saques de banda Grecia Más 14.5 @1.75 (L 5 de 7, V 5 de 7, D 1 de 1); Tiros al arco Países Bajos Menos 7.5 @1.42 (L 5 de 7, V 6 de 7, D 3 de 3); Tiros al arco Grecia Más 1.5 @1.24 (L 7 de 7, V 6 de 7, D 2 de 3); Tiros al arco Grecia Más 2.5 @1.72 (L 6 de 7, V 5 de 7, D 1 de 3); Goles Menos 4.5 @1.22 (L 6 de 7, V 6 de 7, D 3 de 3); Goles Países Bajos Menos 2.5 @1.45 (L 5 de 7, V 6 de 7, D 2 de 3*); Goles Grecia Más 0.5 @1.5 (L 7 de 7, V 5 de 7, D 1 de 3*); Tarjetas Menos 5.5 @1.45 (L 6 de 6, V 5 de 7, D 1 de 3); Tarjetas Menos 6.5 @1.24 (L 6 de 6, V 6 de 7, D 3 de 3); Tarjetas Países Bajos Menos 2.5 @1.37 (L 5 de 6, V 5 de 7, D 3 de 3); Tarjetas Grecia Más 0.5 @1.5 (L 6 de 6, V 7 de 7, D 3 de 3); Tarjetas Grecia Menos 3.5 @1.39 (L 5 de 6, V 5 de 7, D 1 de 3); Denzel Dumfries remates 1+ @1.27 (L 5 de 7, V , D ); Konstantinos Karetsas remates 1+ @1.2 (L 5 de 7, V , D ); Konstantinos Mavropanos remates 1+ @1.4 (L 5 de 5, V , D ).

**NLG-1: Córners Más 6.5 + Goles Menos 4.5**

- Pata Córners Más 6.5 · cuota @1.2 · L 7 de 7 / V 6 de 7 / directos 3 de 3 · p modelo 0.816 (sim 0.810, mercado sin margen 0.8117) · alerta de la línea: no
- Pata Goles Menos 4.5 · cuota @1.22 · L 6 de 7 / V 6 de 7 / directos 3 de 3 · p modelo 0.816 (sim 0.814, mercado sin margen 0.8028) · alerta de la línea: no
- Cuota producto (techo) **1.46**; p **0.662**, p_sim 0.656, cuota justa **1.51**, cuota mínima **1.55**, p_stress 0.622 (pata más frágil por stress: Córners Más 6.5), margen acumulado 0.046, correlación 0.99, guion común «Empate», robustez 0.518, avisos ninguno.
- EV si el cupón pagara el producto: -0.030 (con p_stress: -0.090). Con la cuota real del cupón: pendiente.
- Dependencia declarada: Sin guion común fuerte: córners Más 6.5 se cumple casi siempre y Goles Menos 4.5 solo falla en goleada o partido muy abierto. Correlación del simulador 0.99 (≈ independientes). Ambas patas son «líneas bajas»: la probabilidad es alta y la cuota (producto) cercana al mínimo posible.
- Pata más frágil (regularidad / stress): Córners Más 6.5 @1.20 está en el piso de cuota (≥1.20); cualquier descuento del cupón la deja bajo 1.20.

**NLG-2: Tiros al arco Grecia Más 1.5 + Tarjetas Menos 6.5**

- Pata Tiros al arco Grecia Más 1.5 · cuota @1.24 · L 7 de 7 / V 6 de 7 / directos 2 de 3 · p modelo 0.783 (sim 0.776, mercado sin margen 0.7822) · alerta de la línea: no
- Pata Tarjetas Menos 6.5 · cuota @1.24 · L 6 de 6 / V 6 de 7 / directos 3 de 3 · p modelo 0.755 (sim 0.770, mercado sin margen 0.7822) · alerta de la línea: no
- Cuota producto (techo) **1.54**; p **0.593**, p_sim 0.599, cuota justa **1.69**, cuota mínima **1.74**, p_stress 0.553 (pata más frágil por stress: Tarjetas Menos 6.5), margen acumulado 0.059, correlación 1.0, guion común «Sorpresa: gana el no favorito», robustez 0.419, avisos ninguno.
- EV si el cupón pagara el producto: -0.089 (con p_stress: -0.149). Con la cuota real del cupón: pendiente.
- Dependencia declarada: Independientes en la práctica (corr. 1.0). Si hay expulsión temprana el partido se rompe y Tarjetas Menos 6.5 se pone en riesgo (la serie de Flashscore cuenta solo amarillas: las series quedan por debajo de los puntos de Betano si hubo rojas; el local tiene n=6).
- Pata más frágil (regularidad / stress): Tarjetas Menos 6.5: la serie de tarjetas es una cota baja (rojas = 2 puntos no contadas) y Países Bajos tiene n=6.

Probadas y no elegidas: Goles Menos 4.5 + Tarjetas Grecia Más 0.5 · p 0.657 pero la pata de tarjetas lleva alerta (30 pts); Tiros al arco Grecia Más 1.5 + Karetsas remates 1+ @1.20 · p 0.607 (jugador, alineación probable no confirmada, y mismo guion de volumen de Grecia); Dumfries remates 1+ @1.27 y Mavropanos remates 1+ @1.40 (5 de 5) también cumplen pero bajan la probabilidad conjunta. Saques de banda y fueras de juego cumplen en este partido pero con cuota ~1.7–1.9 y p ≈ 0.5 cada una.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

| Línea | Cuota | p modelo | Prob. devolución | L | V |
|---|---|---|---|---|---|
| Hándicap Grecia +3 | 1.2 | 0.824 | — | 7 de 7 | 6 de 7 |
| Hándicap Grecia +2 | 1.53 | 0.639 | — | 6 de 7 | 5 de 7 |
| Hándicap Grecia +1.75 | 1.42 | 0.703 | 0.0958 | 6 de 7 | 5 de 7 |
| Hándicap Grecia +1.5 | 1.55 | 0.639 | — | 6 de 7 | 5 de 7 |

Series de diferencia de goles (a favor − en contra, últimos 7): local [1.0, 0.0, 1.0, 0.0, -1.0, 2.0, 4.0]; visitante [0.0, 0.0, 1.0, 1.0, 0.0, 1.0, -2.0]. Solo informativo; no se combinó.

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
