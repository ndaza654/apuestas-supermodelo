# Combinadas · Serbia - Alemania · 2026-11-13 14:45 (Bogotá) · jornada 2026-11-13

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


### Serbia - Alemania  (2026-11-13 14:45 Bogotá)
Favorito según modelo/mercado: Alemania (p_resultado {'local': 0.082, 'empate': 0.132, 'visitante': 0.786}). Alertas del modelo en este informe: 3 (líneas con alerta: Córners 1.er tiempo Más 0.5, Córners 1.er tiempo Menos 0.5, Tarjetas Serbia Más 0.5, Tarjetas Serbia Menos 0.5, Saques de banda 1.er tiempo Más 18.5, Saques de banda 1.er tiempo Menos 18.5).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Más 7.5 @1.34 (L 6 de 7, V 5 de 7, D 1 de 1); Córners Más 8.5 @1.6 (L 5 de 7, V 5 de 7, D 1 de 1); Córners Más 9.5 @2.02 (L 5 de 7, V 5 de 7, D 1 de 1); Córners Serbia Más 1.5 @1.2 (L 6 de 7, V 6 de 7, D 0 de 1); Faltas Serbia Menos 11.5 @2.05 (L 5 de 7, V 5 de 7, D 1 de 1); Remates Serbia Más 6.5 @1.4 (L 6 de 7, V 5 de 7, D 0 de 1); Tiros al arco Serbia Más 1.5 @1.3 (L 5 de 7, V 5 de 7, D 0 de 1); Tiros al arco Menos 11.5 @1.53 (L 5 de 7, V 6 de 7, D 1 de 1); Tiros al arco Alemania Menos 8.5 @1.6 (L 6 de 7, V 7 de 7, D 1 de 1); Goles Menos 3.5 @1.78 (L 6 de 7, V 7 de 7, D 1 de 1); Goles Menos 3.75 @1.65 (L 6 de 7, V 7 de 7, D 1 de 1); Goles Menos 4 @1.47 (L 6 de 7, V 7 de 7, D 1 de 1); Goles Menos 4.5 @1.34 (L 7 de 7, V 7 de 7, D 1 de 1); Goles Serbia Más 0.5 @1.65 (L 5 de 7, V 5 de 7, D 0 de 1*); Goles Serbia Menos 1.5 @1.23 (L 5 de 7, V 5 de 7, D 1 de 1*); Goles Alemania Menos 2.5 @1.85 (L 7 de 7, V 7 de 7, D 1 de 1*); Goles Alemania Menos 3.5 @1.32 (L 7 de 7, V 7 de 7, D 1 de 1*); Tarjetas Serbia Más 0.5 @1.75 (L 6 de 7, V 6 de 6, D 1 de 1); Tarjetas Alemania Más 0.5 @1.25 (L 5 de 7, V 5 de 6, D 0 de 1); Tarjetas Alemania Menos 2.5 @1.2 (L 6 de 7, V 5 de 6, D 1 de 1); Ambos 1+ tarjetas: Sí @1.38 (L 6 de 7/5 de 6, V concede 5 de 7/6 de 6, D 0 de 1).

**SAL-1: Córners Serbia Más 1.5 + Tarjetas Alemania Más 0.5**

- Pata Córners Serbia Más 1.5 · cuota @1.2 · L 6 de 7 / V 6 de 7 / directos 0 de 1 · p modelo 0.803 (sim 0.797, mercado sin margen 0.8108) · alerta de la línea: no
- Pata Tarjetas Alemania Más 0.5 · cuota @1.25 · L 5 de 7 / V 5 de 6 / directos 0 de 1 · p modelo 0.798 (sim 0.799, mercado sin margen 0.7752) · alerta de la línea: no
- Cuota producto (techo) **1.50**; p **0.642**, p_sim 0.637, cuota justa **1.56**, cuota mínima **1.61**, p_stress 0.601 (pata más frágil por stress: Tarjetas Alemania Más 0.5), margen acumulado 0.057, correlación 1.0, guion común «Expulsión antes del 70′», robustez 0.617, avisos ninguno.
- EV si el cupón pagara el producto: -0.038 (con p_stress: -0.098). Con la cuota real del cupón: pendiente.
- Dependencia declarada: Poco vinculadas (corr. 1.0). Guion común del simulador: «Expulsión antes del 70′». Ojo: la familia «Tarjetas Serbia» lleva alerta del modelo (31 pts) y «Tarjetas Alemania Más 0.5» es su línea vecina sin alerta: la p de tarjetas es de mezcla, no verificada contra el mercado.
- Pata más frágil (regularidad / stress): Tarjetas Alemania Más 0.5 @1.25 (L 5 de 7, V 5 de 6) y Córners Serbia Más 1.5 @1.20 en el piso de cuota.

**SAL-2: Tiros al arco Serbia Más 1.5 + Goles Alemania Menos 3.5**

- Pata Tiros al arco Serbia Más 1.5 · cuota @1.3 · L 5 de 7 / V 5 de 7 / directos 0 de 1 · p modelo 0.735 (sim 0.727, mercado sin margen 0.744) · alerta de la línea: no
- Pata Goles Alemania Menos 3.5 · cuota @1.32 · L 7 de 7 / V 7 de 7 / directos 1 de 1* · p modelo 0.743 (sim 0.747, mercado sin margen 0.731) · alerta de la línea: no
- Cuota producto (techo) **1.72**; p **0.548**, p_sim 0.546, cuota justa **1.82**, cuota mínima **1.88**, p_stress 0.511 (pata más frágil por stress: Tiros al arco Serbia Más 1.5), margen acumulado 0.067, correlación 1.01, guion común «Sorpresa: gana el no favorito», robustez 0.358, avisos ninguno.
- EV si el cupón pagara el producto: -0.059 (con p_stress: -0.123). Con la cuota real del cupón: pendiente.
- Dependencia declarada: Ligero guion común «Serbia con algo de volumen/resistencia» (SOT Serbia ≥2 y Alemania ≤3 goles) y comparte guion con SAL-1 (Serbia con balón: córners Serbia). Si el partido sale como goleada alemana ambas flaquean: SAL-1 y SAL-2 NO son apuestas independientes entre sí (cuentan como una apuesta repetida en el guion «Serbia compite»).
- Pata más frágil (regularidad / stress): Tiros al arco Serbia Más 1.5 @1.30 (L 5 de 7, V 5 de 7, directo 0 de 1).

Descartadas por anidación: «Ambos 1+ tarjetas Sí» + «Tarjetas Alemania Más 0.5» (p 0.719 es un espejismo: la primera implica la segunda). Descartadas por alerta: cualquier combinada con «Tarjetas Serbia Más 0.5» (alerta 31 pts). Tiros al arco Serbia + Remates Serbia (p 0.593, corr. 1.15) = mismo guion y casi la misma pata. Goles Menos 4 (línea entera, devolución en 4 goles) no se usó: el pago real de una pata con devolución dentro de una combinada se reduce a cuota 1.00 para esa pata.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

| Línea | Cuota | p modelo | Prob. devolución | L | V |
|---|---|---|---|---|---|
| Hándicap Serbia +2 | 2.05 | 0.46 | — | 5 de 7 | 6 de 7 |
| Hándicap Serbia +3 | 1.44 | 0.686 | — | 7 de 7 | 7 de 7 |
| Hándicap Serbia +1.5 | 2.07 | 0.46 | — | 5 de 7 | 6 de 7 |
| Hándicap Serbia +1.75 | 1.87 | 0.52 | 0.1177 | 5 de 7 | 6 de 7 |
| Hándicap Serbia +2.25 | 1.53 | 0.648 | 0.1177 | 5 de 7 | 6 de 7 |
| Hándicap Serbia +2.5 | 1.45 | 0.686 | — | 7 de 7 | 7 de 7 |

Series de diferencia de goles (a favor − en contra, últimos 7): local [-1.0, -2.0, -1.0, -1.0, 1.0, -2.0, 2.0]; visitante [0.0, 2.0, -1.0, 0.0, -1.0, -1.0, 1.0]. Solo informativo; no se combinó.

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
