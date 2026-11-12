# Combinadas · Eslovaquia - Islas Feroé · 2026-11-13 14:45 (Bogotá) · jornada 2026-11-13

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


### Eslovaquia - Islas Feroé  (2026-11-13 14:45 Bogotá)
Favorito según modelo/mercado: Eslovaquia (p_resultado {'local': 0.719, 'empate': 0.19, 'visitante': 0.091}). Alertas del modelo en este informe: 4 (líneas con alerta: Córners 1.er tiempo Más 1.5, Córners 1.er tiempo Menos 1.5, Córners Eslovaquia Más 6.5, Córners Islas Feroé Más 2.5, Más corners: Eslovaquia, Más corners: Islas Feroé).

Patas candidatas (cumple + cuota ≥ 1.20): Córners Más 7.5 @1.3 (L 6 de 7, V 5 de 7, D 1 de 1); Córners Más 8.5 @1.55 (L 6 de 7, V 5 de 7, D 1 de 1); Goles Más 1.5 @1.27 (L 6 de 7, V 5 de 7, D 1 de 1); Goles Eslovaquia Menos 2.5 @1.47 (L 5 de 7, V 6 de 7, D 1 de 1*); Más tarjetas: Islas Feroé @1.57 (L 5 de 7, V 6 de 7, D 1 de 1).

**SVK-1: Córners Más 7.5 + Goles Más 1.5**

- Pata Córners Más 7.5 · cuota @1.3 · L 6 de 7 / V 5 de 7 / directos 1 de 1 · p modelo 0.733 (sim 0.730, mercado sin margen 0.7423) · alerta de la línea: no
- Pata Goles Más 1.5 · cuota @1.27 · L 6 de 7 / V 5 de 7 / directos 1 de 1 · p modelo 0.764 (sim 0.764, mercado sin margen 0.7625) · alerta de la línea: no
- Cuota producto (techo) **1.65**; p **0.532**, p_sim 0.559, cuota justa **1.88**, cuota mínima **1.94**, p_stress 0.496 (pata más frágil por stress: Córners Más 7.5), margen acumulado 0.066, correlación 0.95, guion común «Partido abierto (ambos marcan y 3+ goles)», robustez 0.357, avisos ninguno.
- EV si el cupón pagara el producto: -0.122 (con p_stress: -0.182). Con la cuota real del cupón: pendiente.
- Nota del modelo: goles Más + córners totales Más: dependencia real 0.98 contra 1.03 del simulador (×0.947)
- Dependencia declarada: MISMO guion «partido abierto» (goles Más + córners Más); el simulador da correlación 0.95 (por debajo de 1: se estorban un poco, p ajustada menor que la sim). Segunda combinada defendible: ninguna sin repetir córners o goles; las que quedan tienen p<0.45.
- Pata más frágil (regularidad / stress): Córners Más 7.5 (V 5 de 7) es la pata más frágil según stress.

Probadas y no elegidas: Córners Más 7.5 + Goles Eslovaquia Menos 2.5 · p 0.483 (comparte córners con SVK-1); Goles Más 1.5 + Más tarjetas Islas Feroé @1.57 · p 0.461 (comparte goles). Las líneas de córners por equipo de este partido (Eslovaquia Más 6.5, Feroe Más 2.5) llevan alertas de 25–52 pts en el modelo.

## Hándicap (derivado; NO entra a combinadas)
Regularidad = en cuántos de los últimos 7 partidos de cada equipo la diferencia de goles habría dado victoria COMPLETA de la línea (las asiáticas .25/.75 cuentan solo la victoria completa; la devolución es media pérdida/ganancia). Es una lectura mía sobre `goles.series`, no un «cumple» de la ficha, y n=7 con rivales de distinto nivel. Solo líneas con cuota ≥ 1.20 y ≥5 de 7 en ambos equipos. p = probabilidad del modelo (que parte de las cuotas de Betano: no independiente).

| Línea | Cuota | p modelo | Prob. devolución | L | V |
|---|---|---|---|---|---|
| Hándicap Islas Feroé +3 | 1.28 | 0.769 | — | 7 de 7 | 6 de 7 |
| Hándicap Islas Feroé +2 | 1.78 | 0.546 | — | 6 de 7 | 5 de 7 |
| Hándicap Islas Feroé +1.75 | 1.57 | 0.618 | 0.1142 | 6 de 7 | 5 de 7 |
| Hándicap Islas Feroé +1.5 | 1.75 | 0.547 | — | 6 de 7 | 5 de 7 |

Series de diferencia de goles (a favor − en contra, últimos 7): local [4.0, 0.0, 1.0, 2.0, -1.0, -6.0, 1.0]; visitante [0.0, 0.0, 0.0, 0.0, 1.0, -1.0, -2.0]. Solo informativo; no se combinó.

## Cartera (dependencia entre boletos)
Las combinadas de la jornada dependen de dos ideas repetidas entre partidos: «muchos córners» (Córners Más 6.5/7.5 en NLG-1, SLO-1, BUL-1, LUX-1, MOL-1, SVK-1: seis boletos) y «pocos goles» (Goles Menos en NLG-1, SLO-1, BUL-1, ESC-1, SAL-2, LUX-1). Si el modelo de córners de selecciones sobrestima el volumen de córners, esos seis pierden juntos: cuéntalos como una apuesta repetida, no como seis independientes.

## Método
- Patas leídas de las tablas de los agentes (cumple = SÍ y cuota ≥ 1.20). Verificado que cada pata existe en el modelo y que su cuota coincide con la de Betano del informe (sin diferencias).
- Probabilidades: `supermodelo.analizar(entrada, devolver_sim=True)` + `supermodelo.combos.evaluar(A, S, patas)` (el mismo cálculo de `python3 -m supermodelo --combos`; se llamó a la función desde un script para probar parejas/tríos y ordenar por p; no se escribió ningún `combos.json` en el repo).
- Parejas probadas: todas las de patas candidatas de mercados distintos (y tríos sin alertas); se eligieron por p conjunta descartando patas con alerta, anidadas o de la misma línea.
- Cuota producto = techo; no hay cuota de cupón y no se inventó ningún precio.
