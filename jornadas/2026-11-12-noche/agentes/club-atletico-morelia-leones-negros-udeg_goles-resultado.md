# Club Atletico Morelia - Leones Negros UdeG · goles y resultado

México Liga de Expansion MX · 2026-11-12 21:00 · cuotas Betano: Cuotas de Betano leídas 2026-11-12T22:30:01.794Z · 37 mercados

## Enfoque de mercados
Informe: «Favorito leve · medio · normal»; favorito Morelia (local). Pesan: goles del partido (Menos), 1T (Menos) y empate al descanso (ida de semifinal). Ambos marcan y resultado/hándicap: neutros (el precio ya recoge el favoritismo). Base de liga: Liga MX 2.83 goles/partido, Más 2.5 55 %, ambos marcan 57 % (liga base del modelo, no de la Expansión). Hipótesis del informe, no cambia probabilidades.

## Qué ofrece Betano (raw/bet_*.txt, líneas `L|goles` y `U|…`)
- Goles: total 0.5, 1.5, 2.25, 2.5, 3.5, 4.5; 1T 0.5, 1, 1.25, 1.5, 2.5; 2T solo 1.5; Morelia solo 1.5; Leones solo 0.5.
- Únicos: 1X2, doble oportunidad, empate no apuesta, 1X2 de 1T y 2T, ambos marcan, descanso/final (9), hándicap europeo (solo -1) y asiático (L -0.75, -0.5 y espejos). No hay «descanso o final» (`HOFR`).
- Más: 1 línea de córners total (10.5) y 1 de córners 1T (4.5) (otro agente). Sin tarjetas, tiros ni jugadores.

## Modelo vs mercado (1X2)
Margen de Betano en el 1X2: 8.9%. 

| | Club Atletico Morelia | Empate | Leones Negros UdeG |
|---|---|---|---|
| Cuota | 1.7 | 3.5 | 4.65 |
| Implícita sin margen (proporcional) | 54% | 26% | 20% |
| `p_resultado` (simulación con contexto) | 57% | 26% | 18% |
| Diferencia (modelo − mercado), pts | +3.1 | -0.7 | -2.2 |

Lambdas de goles: modelo 1.70 / 0.89; el informe declara `fuente_objetivos.g = mercado` para ambos equipos: las tasas de gol del modelo se parten de las propias cuotas de Betano. Por eso las probabilidades de goles/resultado salen casi iguales al mercado (distancia máxima «sin contexto vs mercado» en goles/resultado/ambos: ≤ 2 pts). **Esto NO es una segunda opinión independiente; no se usa como argumento a favor de ninguna línea.** `historial_vs_mercado` viene vacío (sin calibración propia).

**Alertas del modelo:** ninguna en este informe.


## Goles (ficha `goles`; goles del partido completo 90′+descuento; n: L 7, V 7, directos 7)

Esperado: local 1.36, visitante 1.79, total 3.14 (a favor/en contra: L 1.43/1.43, V 2.14/1.29). Colchón informativo = esperado − línea (Más) / línea − esperado (Menos). Cumple = ≥5 de 7 en AMBOS. Líneas .25/.75: solo victoria completa. «p» = probabilidad del informe, «p mkt» = implícita sin margen del informe, EV = p·cuota−1.


### Goles total

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.06 | 3.14 | +2.64 | 7 de 7 | 7 de 7 | 7 de 7 | SÍ | 92% | 92% | -2.3% |
| 0.5 | Menos | 6.7 | 3.14 | -2.64 | 0 de 7 | 0 de 7 | 0 de 7 | no | 8% | 8% | -47.4% |
| 1.5 | Más | 1.31 | 3.14 | +1.64 | 7 de 7 | 6 de 7 | 7 de 7 | SÍ | 71% | 73% | -6.7% |
| 1.5 | Menos | 3.1 | 3.14 | -1.64 | 0 de 7 | 1 de 7 | 0 de 7 | no | 29% | 27% | -10.9% |
| 2.25 | Más | 1.7 | 3.14 | +0.89 | 5 de 7 | 4 de 7 | 2 de 7 | no | 53% | 55% | -9.6% |
| 2.25 | Menos | 2.02 | 3.14 | -0.89 | 0 de 7 | 1 de 7 | 0 de 7 | no | 48% | 46% | -3.3% |
| 2.5 | Más | 1.9 | 3.14 | +0.64 | 5 de 7 | 4 de 7 | 2 de 7 | no | 46% | 48% | -13.1% |
| 2.5 | Menos | 1.78 | 3.14 | -0.64 | 2 de 7 | 3 de 7 | 5 de 7 | no | 54% | 52% | -3.4% |
| 3.5 | Más | 3.1 | 3.14 | -0.36 | 1 de 7 | 2 de 7 | 1 de 7 | no | 24% | 26% | -25.5% |
| 3.5 | Menos | 1.3 | 3.14 | +0.36 | 6 de 7 | 5 de 7 | 6 de 7 | SÍ | 76% | 74% | -1.2% |
| 4.5 | Más | 5.3 | 3.14 | -1.36 | 0 de 7 | 1 de 7 | 1 de 7 | no | 11% | 12% | -42.6% |
| 4.5 | Menos | 1.11 | 3.14 | +1.36 | 7 de 7 | 6 de 7 | 6 de 7 | SÍ | 89% | 88% | -1.0% |

### Goles local

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.5 | Más | 1.82 | 1.36 | -0.14 | 3 de 7 | 2 de 7 | 3 de 7 | no | 50% | 51% | -9.7% |
| 1.5 | Menos | 1.88 | 1.36 | +0.14 | 4 de 7 | 5 de 7 | 4 de 7 | no | 50% | 49% | -5.3% |

### Goles visitante

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.57 | 1.79 | +1.29 | 7 de 7 | 6 de 7 | 5 de 7 | SÍ | 58% | 60% | -8.6% |
| 0.5 | Menos | 2.25 | 1.79 | -1.29 | 0 de 7 | 1 de 7 | 2 de 7 | no | 42% | 40% | -6.0% |

### Goles 1T / 2T (sin estadística de goles por tiempo: SIN regularidad ni colchón; solo modelo y mercado)

| Ámbito | Línea | Lado | Cuota | p | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.34 | 68% | 70% | -8.6% |
| 1T | 0.5 | Menos | 2.67 | 32% | 30% | -15.1% |
| 1T | 1.0 | Más | 1.72 | 53% | 55% | -8.5% |
| 1T | 1.0 | Menos | 1.95 | 50% | 48% | -2.1% |
| 1T | 1.25 | Más | 2.15 | 40% | 42% | -13.1% |
| 1T | 1.25 | Menos | 1.6 | 61% | 59% | -2.1% |
| 1T | 1.5 | Más | 2.42 | 32% | 34% | -22.2% |
| 1T | 1.5 | Menos | 1.42 | 68% | 66% | -3.7% |
| 1T | 2.5 | Más | 4.7 | 11% | 12% | -50.0% |
| 1T | 2.5 | Menos | 1.1 | 89% | 88% | -1.7% |
| 2T | 1.5 | Más | 2.2 | 39% | 40% | -13.9% |
| 2T | 1.5 | Menos | 1.57 | 61% | 60% | -4.4% |

Verificación propia de los conteos de la ficha en TODAS las líneas de total (incl. asiáticas, solo victoria completa) (mi recuento desde las series vs ficha, L/V): coinciden todas.


## Resultado, doble oportunidad, ambos marcan, hándicap, descanso/final

Regularidad derivada de las series de la ficha (marcadores de los últimos 7/7; no es un campo de la ficha). Evento medido en el partido de cada equipo en su propio papel: L = el equipo local de este partido, V = el visitante (ej. «Gana Club Atletico Morelia»: L ganó X de 7; V perdió X de 7). Directos orientados [local, visitante] según la ficha (n=7).

| Selección | Cuota | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|
| Gana Club Atletico Morelia | 1.7 | 3 de 7 | 2 de 7 | 2 de 7 | no | 57% | 56% | -3.3% |
| Empate | 3.5 | 2 de 7 | 1 de 7 | 0 de 7 | no | 25% | 25% | -11.7% |
| Gana Leones Negros UdeG | 4.65 | 2 de 7 | 4 de 7 | 5 de 7 | no | 18% | 19% | -16.8% |
| Club Atletico Morelia o empate | 1.17 | 5 de 7 | 3 de 7 | 2 de 7 | no | 82% | 81% | -3.9% |
| Leones Negros UdeG o empate | 2.1 | 4 de 7 | 5 de 7 | 5 de 7 | no | 43% | 44% | -9.4% |
| No hay empate | 1.25 | 5 de 7 | 6 de 7 | 7 de 7 | SÍ | 75% | 75% | -6.6% |
| 1.er tiempo: Club Atletico Morelia | 2.18 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 41% | 42% | -10.3% |
| 1.er tiempo: Empate | 2.2 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 43% | 41% | -6.0% |
| 1.er tiempo: Leones Negros UdeG | 4.85 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 16% | 17% | -21.8% |
| 2.º tiempo: Club Atletico Morelia | 2.07 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 44% | 44% | -8.8% |
| 2.º tiempo: Empate | 2.4 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 38% | 37% | -9.8% |
| 2.º tiempo: Leones Negros UdeG | 4.45 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 18% | 19% | -18.2% |
| Ambos marcan: Sí | 1.85 | 7 de 7 | 5 de 7 | 2 de 7 | SÍ | 48% | 50% | -10.8% |
| Ambos marcan: No | 1.83 | 0 de 7 | 2 de 7 | 5 de 7 | no | 52% | 50% | -5.2% |
| Descanso/final: Club Atletico Morelia / Club Atletico Morelia | 2.5 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 35% | 35% | -12.6% |
| Descanso/final: Club Atletico Morelia / Empate | 14.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 5% | 5% | -31.7% |
| Descanso/final: Club Atletico Morelia / Leones Negros UdeG | 50.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 1% | 1% | -41.1% |
| Descanso/final: Empate / Club Atletico Morelia | 4.45 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 19% | 18% | -13.3% |
| Descanso/final: Empate / Empate | 5.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 16% | 16% | -20.1% |
| Descanso/final: Empate / Leones Negros UdeG | 10.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 7% | 7% | -25.4% |
| Descanso/final: Leones Negros UdeG / Club Atletico Morelia | 26.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 2% | 2% | -35.5% |
| Descanso/final: Leones Negros UdeG / Empate | 15.5 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 4% | 4% | -31.7% |
| Descanso/final: Leones Negros UdeG / Leones Negros UdeG | 7.6 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 9% | 10% | -30.3% |
| Hándicap Club Atletico Morelia -1 | 2.9 | 0 de 7 | 0 de 7 | 2 de 7 | no | 30% | 31% | -14.3% |
| Hándicap empate (Club Atletico Morelia -1) | 3.45 | 3 de 7 | 2 de 7 | 0 de 7 | no | 27% | 25% | -5.5% |
| Hándicap Leones Negros UdeG +1 | 2.1 | 4 de 7 | 5 de 7 | 5 de 7 | no | 43% | 44% | -9.5% |
| Hándicap Club Atletico Morelia -0.75 (asiática: devuelve 14%) | 1.85 | 0 de 7 | 0 de 7 | 2 de 7 | no | 51% | 51% | -6.1% |
| Hándicap Leones Negros UdeG +0.75 (asiática: devuelve 14%) | 1.85 | 4 de 7 | 5 de 7 | 5 de 7 | no | 50% | 51% | -6.8% |
| Hándicap Club Atletico Morelia -0.5 | 1.67 | 3 de 7 | 2 de 7 | 2 de 7 | no | 57% | 56% | -5.0% |
| Hándicap Leones Negros UdeG +0.5 | 2.07 | 4 de 7 | 5 de 7 | 5 de 7 | no | 43% | 44% | -10.8% |

Empate no apuesta (Betano `DNOB`; el informe no lo trae como línea; probabilidad derivada por mí de p_resultado excluyendo el empate y de la implícita del 1X2): Club Atletico Morelia 1.27, Leones Negros UdeG 3.3. Modelo: Club Atletico Morelia 76.5% / Leones Negros UdeG 23.5%; mercado (1X2 sin margen): 73.2% / 26.8%. EV con p del modelo: Club Atletico Morelia -2.8%, Leones Negros UdeG -22.6% (el empate devuelve la apuesta; el EV así calculado supone devolución de 1; es una aproximación). Regularidad = la de «Gana …» más arriba (victoria completa).


### Directos y muestra
7 directos con goles en 5 años (ficha; los 3 más recientes con estadísticas completas). Orientación [Morelia, Leones] según la ficha. Los últimos 7 de ambos mezclan fase regular y cuartos de liguilla (ritmo y motivación distintos).


## Mejores líneas por probabilidad del informe que además cumplen ≥5 de 7 en ambos (cuota ≥ 1.20)

No es una recomendación: ordenado por p del informe (que sigue al mercado), no por EV.

| # | Línea | Cuota | Esperado | Colchón | L | V | D | p | EV |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Goles Menos 3.5 | 1.3 | 3.14 | 0.36 | 6 de 7 | 5 de 7 | 6 de 7 | 76% | -1.2% |
| 2 | No hay empate | 1.25 | — | — | 5 de 7 | 6 de 7 | 7 de 7 | 75% | -6.6% |
| 3 | Goles Más 1.5 | 1.31 | 3.14 | 1.64 | 7 de 7 | 6 de 7 | 7 de 7 | 71% | -6.7% |
| 4 | Goles visitante Más 0.5 | 1.57 | 1.79 | 1.29 | 7 de 7 | 6 de 7 | 5 de 7 | 58% | -8.6% |
| 5 | Ambos marcan: Sí | 1.85 | — | — | 7 de 7 | 5 de 7 | 2 de 7 | 48% | -10.8% |

Líneas que cumplen pero con cuota < 1.20 (2): Goles Más 0.5 @1.06, Goles Menos 4.5 @1.11

## Límites
- Muestra mezcla fase regular y liguilla; la liga base del modelo es Liga MX (no Expansión), y las medias de remates/córners/faltas son prior de liga, no del partido.
- Sin alineaciones ni estadísticas de árbitro. Casi sin mercados fuera de goles/resultado.
- n = 7+7; 7 directos en 5 años (plantillas muy distintas, valor orientativo).
- Informe sin alertas (0), pero goles/resultado salen de lambdas de Betano: coinciden con el mercado por construcción, no son segunda opinión.
- Sin goles por tiempo: 1T/2T, descanso/final y 1X2 de tiempos solo tienen modelo y mercado. Ida de semifinal: la regla de liquidación del mercado (90′) no está en el repo, aunque en la ida no hay prórroga.

