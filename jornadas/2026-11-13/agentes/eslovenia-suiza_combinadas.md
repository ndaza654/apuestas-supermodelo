# Combinadas · Eslovenia - Suiza · 2026-11-13 14:45 (Bogotá) · jornada 2026-11-13

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


### Eslovenia - Suiza  (2026-11-13 14:45 Bogotá)
Favorito según modelo/mercado: Suiza (p_resultado {'local': 0.168, 'empate': 0.254, 'visitante': 0.578}). Alertas del modelo en este informe: 9 (líneas con alerta: Tarjetas Más 3.5, Tarjetas Menos 3.5, Córners 1.er tiempo Más 0.5, Córners 1.er tiempo Menos 0.5, Córners 1.er tiempo Más 1.5, Córners 1.er tiempo Menos 1.5, Tarjetas 1.er tiempo Más 1.5, Tarjetas 1.er tiempo Menos 1.5, Córners Eslovenia Más 3.5, Córners Eslovenia Más 4.5, Córners Suiza Más 4.5, Córners Suiza Más 5.5, Tarjetas Eslovenia Más 0.5, Tarjetas Eslovenia Menos 0.5, Tarjetas Eslovenia Más 2.5, Tarjetas Eslovenia Menos 2.5, Tarjetas Suiza Más 0.5, Tarjetas Suiza Menos 0.5, Tarjetas Suiza Más 1.5, Tarjetas Suiza Menos 1.5, Más corners: Eslovenia, Más corners: Suiza, Ambos 1+ tarjetas: S).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Más 6.5 @1.26 (L 6 de 7, V 5 de 7, D 3 de 3); Córners Menos 10.5 @1.29 (L 5 de 7, V 6 de 7, D 3 de 3); Córners Suiza Más 3.5 @1.26 (L 5 de 7, V 5 de 7, D 3 de 3); Goles Más 1.5 @1.4 (L 5 de 7, V 6 de 7, D 2 de 3); Goles Menos 3.5 @1.26 (L 7 de 7, V 6 de 7, D 3 de 3); Tarjetas Eslovenia Más 0.5 @1.67 (L 7 de 7, V 7 de 7, D 3 de 3); Más tarjetas: Eslovenia @1.82 (L 5 de 7, V 5 de 7, D 3 de 3); Dan Ndoye anota o asiste @1.98 (L 5 de 7, V , D ).

**SLO-1: Córners Más 6.5 + Goles Menos 3.5**

- Pata Córners Más 6.5 · cuota @1.26 · L 6 de 7 / V 5 de 7 / directos 3 de 3 · p modelo 0.774 (sim 0.764, mercado sin margen 0.7682) · alerta de la línea: no
- Pata Goles Menos 3.5 · cuota @1.26 · L 7 de 7 / V 6 de 7 / directos 3 de 3 · p modelo 0.799 (sim 0.798, mercado sin margen 0.7758) · alerta de la línea: no
- Cuota producto (techo) **1.59**; p **0.650**, p_sim 0.607, cuota justa **1.54**, cuota mínima **1.59**, p_stress 0.608 (pata más frágil por stress: Córners Más 6.5), margen acumulado 0.054, correlación 1.05, guion común «Empate», robustez 0.335, avisos ninguno.
- EV si el cupón pagara el producto: +0.031 (con p_stress: -0.035). Con la cuota real del cupón: pendiente.
- Nota del modelo: goles Menos + córners totales Más: dependencia real 1.02 contra 0.97 del simulador (×1.056)
- Dependencia declarada: Débil: goles Menos y córners Más (el modelo ajusta ×1.056 por dependencia). Guion común «Empate/partido trabado». Alerta: las líneas de córners por equipo de este partido (Eslovenia Más 3.5/4.5, Suiza Más 4.5/5.5) llevan alertas de 15–25 pts; el total Más 6.5 no, pero es de la misma familia.
- Pata más frágil (regularidad / stress): Córners Más 6.5 (L 6 de 7, V 5 de 7); directo 3 de 3.

**SLO-2: Córners Menos 10.5 + Goles Más 1.5**

- Pata Córners Menos 10.5 · cuota @1.29 · L 5 de 7 / V 6 de 7 / directos 3 de 3 · p modelo 0.724 (sim 0.715, mercado sin margen 0.748) · alerta de la línea: no
- Pata Goles Más 1.5 · cuota @1.4 · L 5 de 7 / V 6 de 7 / directos 2 de 3 · p modelo 0.677 (sim 0.679, mercado sin margen 0.6928) · alerta de la línea: no
- Cuota producto (techo) **1.81**; p **0.512**, p_sim 0.479, cuota justa **1.95**, cuota mínima **2.01**, p_stress 0.474 (pata más frágil por stress: Goles Más 1.5), margen acumulado 0.064, correlación 1.04, guion común «Partido abierto (ambos marcan y 3+ goles)», robustez 0.337, avisos ninguno.
- EV si el cupón pagara el producto: -0.076 (con p_stress: -0.144). Con la cuota real del cupón: pendiente.
- Nota del modelo: goles Más + córners totales Menos: dependencia real 1.02 contra 0.97 del simulador (×1.056)
- Dependencia declarada: Pareja de guiones opuestos (poco córner + al menos 2 goles) sin dependencia fuerte (corr. 1.04). NO es independiente de SLO-1: Córners Más 6.5 y Menos 10.5 forman una banda de córners (7–10): si los córners se salen de la banda por arriba o por abajo, solo una de las dos falla; no apostar ambas pensando en cobertura.
- Pata más frágil (regularidad / stress): Goles Más 1.5 @1.40 (L 5 de 7, V 6 de 7, directo 2 de 3) y Córners Menos 10.5 (L 5 de 7).

Otras combinaciones probadas (no elegidas): banda Córners Más 6.5 + Córners Menos 10.5 · p 0.492 (p_sim 0.479, corr. 0.88, p_stress 0.458; cuota producto 1.63; ambas patas de córners, misma estadística); Goles Menos 3.5 + Tarjetas Eslovenia Más 0.5 · p 0.563 pero la pata de tarjetas lleva alerta de 24 pts (p no fiable); con Dan Ndoye «anota o asiste» @1.98 (5 de 7; titular probable Flashscore ~13:00, no confirmado) la mejor es Goles Más 1.5 + Ndoye · p 0.384, p_stress 0.341, producto 2.77: probabilidad baja y pata de jugador sin alineación confirmada.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

Ninguna línea de hándicap con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos (series de diferencia de goles: local [1.0, -1.0, 2.0, 0.0, 0.0, -2.0, 0.0]; visitante [3.0, 1.0, 3.0, 3.0, -2.0, 1.0, 2.0]).

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
