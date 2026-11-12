# Combinadas · Bulgaria - Islandia · 2026-11-13 14:45 (Bogotá) · jornada 2026-11-13

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


### Bulgaria - Islandia  (2026-11-13 14:45 Bogotá)
Favorito según modelo/mercado: Islandia (p_resultado {'local': 0.211, 'empate': 0.272, 'visitante': 0.517}). Alertas del modelo en este informe: 2 (líneas con alerta: Córners 1.er tiempo Más 1.5, Córners 1.er tiempo Menos 1.5, Córners 1.er tiempo Más 2.5, Córners 1.er tiempo Menos 2.5).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Más 6.5 @1.22 (L 6 de 7, V 6 de 7, D 1 de 1); Córners Más 7.5 @1.42 (L 6 de 7, V 6 de 7, D 1 de 1); Córners Más 8.5 @1.75 (L 6 de 7, V 6 de 7, D 1 de 1); Goles Más 1.5 @1.36 (L 5 de 7, V 6 de 7, D 1 de 1); Goles Menos 3.5 @1.27 (L 6 de 7, V 6 de 7, D 1 de 1); Goles Islandia Menos 2.5 @1.22 (L 6 de 7, V 5 de 7, D 0 de 1*); Tarjetas Islandia Menos 2.5 @1.85 (L 7 de 7, V 6 de 7, D 1 de 1).

**BUL-1: Córners Más 6.5 + Goles Menos 3.5**

- Pata Córners Más 6.5 · cuota @1.22 · L 6 de 7 / V 6 de 7 / directos 1 de 1 · p modelo 0.808 (sim 0.797, mercado sin margen 0.795) · alerta de la línea: no
- Pata Goles Menos 3.5 · cuota @1.27 · L 6 de 7 / V 6 de 7 / directos 1 de 1 · p modelo 0.773 (sim 0.773, mercado sin margen 0.7625) · alerta de la línea: no
- Cuota producto (techo) **1.55**; p **0.657**, p_sim 0.613, cuota justa **1.52**, cuota mínima **1.57**, p_stress 0.614 (pata más frágil por stress: Goles Menos 3.5), margen acumulado 0.061, correlación 1.05, guion común «Empate», robustez 0.324, avisos ninguno.
- EV si el cupón pagara el producto: +0.017 (con p_stress: -0.048). Con la cuota real del cupón: pendiente.
- Nota del modelo: goles Menos + córners totales Más: dependencia real 1.02 contra 0.97 del simulador (×1.056)
- Dependencia declarada: Débil (el modelo aplica ×1.056 por dependencia real córners Más/goles Menos). Alternativa excluyente con casi la misma probabilidad y sin ajuste de dependencia: Córners Más 6.5 + Goles Islandia Menos 2.5 (p 0.651; p_sim 0.644).
- Pata más frágil (regularidad / stress): Goles Menos 3.5 (L 6 de 7, V 6 de 7, directo 1 de 1); el modelo la marca como pata más frágil.

Segunda combinada: ninguna defendible. Fuera de córners solo queda Tarjetas Islandia Menos 2.5 @1.85 (p modelo 0.488 sola) y todas las parejas sin córners tienen p ≤ 0.38. Parejas con Córners Más 7.5/8.5 repiten la misma línea de córners que BUL-1.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

Ninguna línea de hándicap con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos (series de diferencia de goles: local [2.0, -3.0, 0.0, -1.0, 1.0, 8.0, 1.0]; visitante [0.0, 3.0, 3.0, 0.0, -2.0, 2.0, 0.0]).

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
