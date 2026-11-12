# Combinadas · Moldavia - Kazajistán · 2026-11-13 12:00 (Bogotá) · jornada 2026-11-13

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


### Moldavia - Kazajistán  (2026-11-13 12:00 Bogotá)
Favorito según modelo/mercado: Moldavia (p_resultado {'local': 0.365, 'empate': 0.29, 'visitante': 0.345}). Alertas del modelo en este informe: 2 (líneas con alerta: Córners 1.er tiempo Más 1.5, Córners 1.er tiempo Menos 1.5, Córners 1.er tiempo Más 2.5, Córners 1.er tiempo Menos 2.5).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Más 6.5 @1.24 (L 7 de 7, V 7 de 7, D 2 de 3); Córners Más 7.5 @1.45 (L 6 de 7, V 7 de 7, D 2 de 3); Córners Más 8.5 @1.82 (L 6 de 7, V 7 de 7, D 2 de 3); Córners Más 9.5 @2.35 (L 5 de 7, V 6 de 7, D 2 de 3); Goles Más 1.5 @1.47 (L 7 de 7, V 6 de 7, D 3 de 3); Goles Kazajistán Más 0.5 @1.45 (L 7 de 7, V 7 de 7, D 3 de 3*).

**MOL-1: Córners Más 6.5 + Goles Kazajistán Más 0.5**

- Pata Córners Más 6.5 · cuota @1.24 · L 7 de 7 / V 7 de 7 / directos 2 de 3 · p modelo 0.785 (sim 0.778, mercado sin margen 0.781) · alerta de la línea: no
- Pata Goles Kazajistán Más 0.5 · cuota @1.45 · L 7 de 7 / V 7 de 7 / directos 3 de 3* · p modelo 0.663 (sim 0.666, mercado sin margen 0.6616) · alerta de la línea: no
- Cuota producto (techo) **1.80**; p **0.523**, p_sim 0.521, cuota justa **1.91**, cuota mínima **1.97**, p_stress 0.484 (pata más frágil por stress: Goles Kazajistán Más 0.5), margen acumulado 0.071, correlación 1.01, guion común «Partido abierto (ambos marcan y 3+ goles)», robustez 0.445, avisos ninguno.
- EV si el cupón pagara el producto: -0.059 (con p_stress: -0.130). Con la cuota real del cupón: pendiente.
- Dependencia declarada: Sin dependencia fuerte (corr. 1.01). Guion «Partido abierto» como mejor escenario. Las dos patas tienen 7 de 7 en ambos equipos (córners 7/7 y 7/7; gol de Kazajistán 7/7 y 7/7), la regularidad más limpia de la jornada, pero con directos de solo 2 de 3 en córners.
- Pata más frágil (regularidad / stress): Goles Kazajistán Más 0.5 @1.45 (si Kazajistán no marca, cae todo; es el visitante).

Segunda combinada: ninguna defendible. Las otras patas que cumplen (córners Más 7.5/8.5/9.5 y Goles Más 1.5) son del mismo guion «partido abierto» y de la misma línea escalonada que MOL-1; las mejores (Córners Más 7.5 + Goles Kazajistán Más 0.5, p 0.446; Córners Más 6.5 + Goles Más 1.5, p 0.468) bajan la probabilidad y repiten idea.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

| Línea | Cuota | p modelo | Prob. devolución | L | V |
|---|---|---|---|---|---|
| Hándicap Kazajistán +1 | 1.5 | 0.638 | — | 5 de 7 | 6 de 7 |
| Hándicap Kazajistán +0.5 | 1.5 | 0.636 | — | 5 de 7 | 6 de 7 |

Series de diferencia de goles (a favor − en contra, últimos 7): local [-4.0, 1.0, 0.0, -2.0, -3.0, -2.0, 0.0]; visitante [0.0, -1.0, -1.0, 0.0, 1.0, 2.0, 0.0]. Solo informativo; no se combinó.

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
