# Combinadas · Escocia - Macedonia del Norte · 2026-11-13 14:45 (Bogotá) · jornada 2026-11-13

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


### Escocia - Macedonia del Norte  (2026-11-13 14:45 Bogotá)
Favorito según modelo/mercado: Escocia (p_resultado {'local': 0.853, 'empate': 0.111, 'visitante': 0.035}). Alertas del modelo en este informe: 5 (líneas con alerta: Córners 1.er tiempo Más 0.5, Córners 1.er tiempo Menos 0.5, Córners Escocia Más 6.5, Córners Macedonia del Norte Más 2.5, Más corners: Escocia, Más corners: Macedonia del Norte).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Menos 11.5 @1.28 (L 6 de 7, V 5 de 7, D 1 de 1); Fueras de lugar Escocia Menos 1.5 @1.9 (L 6 de 7, V 6 de 7, D 1 de 1); Fueras de lugar Menos 2.5 @2.07 (L 5 de 7, V 6 de 7, D 1 de 1); Fueras de lugar Macedonia del Norte Menos 1.5 @1.45 (L 5 de 7, V 6 de 7, D 1 de 1); Remates Escocia Menos 20.5 @1.82 (L 6 de 7, V 5 de 7, D 0 de 1); Remates Escocia Menos 21.5 @1.57 (L 6 de 7, V 5 de 7, D 0 de 1); Remates Menos 25.5 @2.5 (L 5 de 7, V 5 de 7, D 0 de 1); Remates Menos 27.5 @1.83 (L 5 de 7, V 5 de 7, D 0 de 1); Remates Menos 29.5 @1.45 (L 5 de 7, V 5 de 7, D 0 de 1); Goles Menos 3.5 @1.45 (L 7 de 7, V 5 de 7, D 1 de 1); Goles Escocia Menos 3.5 @1.27 (L 7 de 7, V 5 de 7, D 1 de 1*); Tarjetas Menos 4.5 @1.88 (L 5 de 7, V 5 de 7, D 0 de 1); Ambos 1+ tarjetas: Sí @1.23 (L 7 de 7/7 de 7, V concede 6 de 7/3 de 7, D 1 de 1).

**ESC-1: Goles Escocia Menos 3.5 + Ambos 1+ tarjetas: Sí**

- Pata Goles Escocia Menos 3.5 · cuota @1.27 · L 7 de 7 / V 5 de 7 / directos 1 de 1* · p modelo 0.775 (sim 0.782, mercado sin margen 0.7625) · alerta de la línea: no
- Pata Ambos 1+ tarjetas: Sí · cuota @1.23 · L 7 de 7/7 de 7 / V concede 6 de 7/3 de 7 / directos 1 de 1 · p modelo 0.784 (sim 0.790, mercado sin margen 0.788) · alerta de la línea: no
- Cuota producto (techo) **1.56**; p **0.626**, p_sim 0.636, cuota justa **1.6**, cuota mínima **1.64**, p_stress 0.586 (pata más frágil por stress: Goles Escocia Menos 3.5), margen acumulado 0.061, correlación 1.03, guion común «Empate», robustez 0.53, avisos ninguno.
- EV si el cupón pagara el producto: -0.022 (con p_stress: -0.085). Con la cuota real del cupón: pendiente.
- Dependencia declarada: Independientes (corr. 1.03). Goles Escocia Menos 3.5 solo falla si Escocia mete 4+ (Escocia es muy favorita: 85 % de victoria según el modelo, 79 % según las cuotas del ranking; eso sube el riesgo de goleada). «Ambos 1+ tarjetas» depende de que Macedonia reciba al menos una: la serie de Macedonia concedida es 3 de 7 (el cumple se apoya en los 7 de 7 de ambos «a favor»).
- Pata más frágil (regularidad / stress): Goles Escocia Menos 3.5 (V 5 de 7) y «Ambos 1+» (conceden 3 de 7 en la columna de Macedonia).

**ESC-2: Córners Menos 11.5 + Remates Menos 29.5**

- Pata Córners Menos 11.5 · cuota @1.28 · L 6 de 7 / V 5 de 7 / directos 1 de 1 · p modelo 0.754 (sim 0.744, mercado sin margen 0.7568) · alerta de la línea: no
- Pata Remates Menos 29.5 · cuota @1.45 · L 5 de 7 / V 5 de 7 / directos 0 de 1 · p modelo 0.643 (sim 0.628, mercado sin margen 0.6598) · alerta de la línea: no
- Cuota producto (techo) **1.86**; p **0.509**, p_sim 0.491, cuota justa **1.96**, cuota mínima **2.02**, p_stress 0.470 (pata más frágil por stress: Remates Menos 29.5), margen acumulado 0.073, correlación 1.05, guion común «Favorito golpea temprano y gana», robustez 0.424, avisos ninguno.
- EV si el cupón pagara el producto: -0.054 (con p_stress: -0.128). Con la cuota real del cupón: pendiente.
- Dependencia declarada: MISMO guion «poco volumen/partido controlado» (corr. 1.05): remates y córners bajan juntos. Declarado; p conjunta ligeramente por encima del producto. Alternativa con otra pata de la misma lista: Fueras de lugar Macedonia Menos 1.5 en lugar de Remates (p 0.494).
- Pata más frágil (regularidad / stress): Remates Menos 29.5 (5 de 7 en ambos, directo 0 de 1).

Nota: el agente de jugadores no marcó ninguna línea de jugador como «cumple» en este partido. Alertas del modelo de 31–48 pts caen en córners por equipo y «más córners»; el total Córners Menos 11.5 no tiene alerta propia pero es de esa familia.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

Ninguna línea de hándicap con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos (series de diferencia de goles: local [-1.0, 2.0, -3.0, 0.0, -3.0, -1.0, 1.0]; visitante [-3.0, -2.0, -2.0, -3.0, -4.0, -6.0, 0.0]).

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
