# Estudiantes de La Plata - Independiente Rivadavia · goles y resultado

Argentina Supercopa · 2026-11-12 18:00 · cuotas Betano: Cuotas de Betano leídas 2026-11-12T22:29:11.874Z · 445 mercados

## Enfoque de mercados
Informe: «Parejo · cerrado · caliente»; favorito leve Estudiantes. Pesan: goles del partido (Menos), 1T (Menos) y empate al descanso, doble oportunidad / empate / HT-FT X. Poco favorecidos según el informe: ambos marcan, hándicap y victoria. Es una hipótesis del informe, no cambia probabilidades.

## Qué ofrece Betano (raw/bet_*.txt, líneas `L|goles` y `U|…`)
- Goles: total 0.5, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 3.5, 4.5; 1T 0.5, 0.75, 1, 1.25, 1.5, 2.5; 2T 0.5, 1.5, 2.5; Estudiantes 0.5, 1.5, 2.5; Rivadavia 0.5, 1.5, 2.5.
- Únicos: 1X2 (`MRES`), doble oportunidad (`DBLC`), empate no apuesta (`DNOB`), 1X2 del 1T (`H1RS`) y del 2T (`H2RS`), «descanso o final» (`HOFR`), ambos marcan (`BTSC`), descanso/final 9 combinaciones (`HTFT`), hándicap europeo (`FHMR`, -3 a +2) y asiático (`AHRF`, -1 a +0.25 local). Además existen `4151`/`4152` (Sí/No, códigos sin etiqueta en el repo: no se analizan).
- Corners/tarjetas/remates/jugadores existen pero son de otros agentes.

## Modelo vs mercado (1X2)
Margen de Betano en el 1X2: 5.2%. 

| | Estudiantes de La Plata | Empate | Independiente Rivadavia |
|---|---|---|---|
| Cuota | 2.42 | 2.8 | 3.55 |
| Implícita sin margen (proporcional) | 39% | 34% | 27% |
| `p_resultado` (simulación con contexto) | 40% | 34% | 25% |
| Diferencia (modelo − mercado), pts | +1.1 | +0.4 | -1.6 |

Lambdas de goles: modelo 1.03 / 0.79; el informe declara `fuente_objetivos.g = mercado` para ambos equipos: las tasas de gol del modelo se parten de las propias cuotas de Betano. Por eso las probabilidades de goles/resultado salen casi iguales al mercado (distancia máxima «sin contexto vs mercado» en goles/resultado/ambos: ≤ 2 pts). **Esto NO es una segunda opinión independiente; no se usa como argumento a favor de ninguna línea.** `historial_vs_mercado` viene vacío (sin calibración propia).

**ALERTAS del modelo (10):** «Revisar: la simulación sin contexto se aleja 16 pts del merc…» (rango 16–40 pts). Líneas marcadas por familia: {'tarjetas': 30}. Ninguna línea de goles/resultado/ambos lleva la marca (su distancia sin contexto vs mercado es ≤ 2 pts), pero el informe sí dice que en otras familias la simulación se aleja del mercado: señal de que el modelo o el dato de ese partido pueden estar mal. Por eso las probabilidades de goles/resultado se muestran SIEMPRE con esta advertencia y NO se usan como argumento a favor de ninguna línea.


## Goles (ficha `goles`; goles del partido completo 90′+descuento; n: L 7, V 7, directos 3)

Esperado: local 1.43, visitante 1.36, total 2.79 (a favor/en contra: L 1.29/1.57, V 1.14/1.57). Colchón informativo = esperado − línea (Más) / línea − esperado (Menos). Cumple = ≥5 de 7 en AMBOS. Líneas .25/.75: solo victoria completa. «p» = probabilidad del informe, «p mkt» = implícita sin margen del informe, EV = p·cuota−1.


### Goles total

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.18 | 2.79 | +2.29 | 6 de 7 | 7 de 7 | 3 de 3 | SÍ | 83% | 83% | -2.2% |
| 0.5 | Menos | 4.9 | 2.79 | -2.29 | 1 de 7 | 0 de 7 | 0 de 3 | no | 17% | 17% | -16.0% |
| 1.0 | Más | 1.28 | 2.79 | +1.79 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | 76% | 77% | -2.1% |
| 1.0 | Menos | 3.85 | 2.79 | -1.79 | 1 de 7 | 0 de 7 | 0 de 3 | no | 25% | 24% | -4.7% |
| 1.25 | Más | 1.52 | 2.79 | +1.54 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | 63% | 64% | -4.2% |
| 1.25 | Menos | 2.6 | 2.79 | -1.54 | 1 de 7 | 0 de 7 | 0 de 3 | no | 38% | 36% | -2.3% |
| 1.5 | Más | 1.75 | 2.79 | +1.29 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | 53% | 55% | -6.8% |
| 1.5 | Menos | 2.1 | 2.79 | -1.29 | 2 de 7 | 2 de 7 | 0 de 3 | no | 47% | 45% | -1.9% |
| 1.75 | Más | 2.0 | 2.79 | +1.04 | 4 de 7 | 3 de 7 | 2 de 3 | no | 47% | 48% | -6.9% |
| 1.75 | Menos | 1.85 | 2.79 | -1.04 | 2 de 7 | 2 de 7 | 0 de 3 | no | 54% | 52% | -0.1% |
| 2.0 | Más | 2.47 | 2.79 | +0.79 | 4 de 7 | 3 de 7 | 2 de 3 | no | 37% | 39% | -8.2% |
| 2.0 | Menos | 1.57 | 2.79 | -0.79 | 2 de 7 | 2 de 7 | 0 de 3 | no | 64% | 62% | +0.4% |
| 2.25 | Más | 2.87 | 2.79 | +0.54 | 4 de 7 | 3 de 7 | 2 de 3 | no | 31% | 33% | -11.2% |
| 2.25 | Menos | 1.44 | 2.79 | -0.54 | 2 de 7 | 2 de 7 | 0 de 3 | no | 70% | 68% | +0.3% |
| 2.5 | Más | 3.2 | 2.79 | +0.29 | 4 de 7 | 3 de 7 | 2 de 3 | no | 26% | 28% | -16.0% |
| 2.5 | Menos | 1.35 | 2.79 | -0.29 | 3 de 7 | 4 de 7 | 1 de 3 | no | 74% | 72% | -0.4% |
| 3.5 | Más | 6.5 | 2.79 | -0.71 | 3 de 7 | 3 de 7 | 1 de 3 | no | 11% | 12% | -30.9% |
| 3.5 | Menos | 1.12 | 2.79 | +0.71 | 4 de 7 | 4 de 7 | 2 de 3 | no | 89% | 88% | +0.1% |
| 4.5 | Más | 12.5 | 2.79 | -1.71 | 1 de 7 | 1 de 7 | 0 de 3 | no | 4% | 4% | -56.1% |
| 4.5 | Menos | 1.03 | 2.79 | +1.71 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | 96% | 96% | -0.6% |

### Goles local

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.47 | 1.43 | +0.93 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | 65% | 65% | -4.5% |
| 0.5 | Menos | 2.55 | 1.43 | -0.93 | 1 de 7 | 1 de 7 | 0 de 3 | no | 35% | 35% | -10.7% |
| 1.5 | Más | 3.15 | 1.43 | -0.07 | 2 de 7 | 2 de 7 | 2 de 3 | no | 27% | 27% | -14.8% |
| 1.5 | Menos | 1.33 | 1.43 | +0.07 | 5 de 7 | 5 de 7 | 1 de 3 | SÍ | 73% | 73% | -3.0% |
| 2.5 | Más | 7.2 | 1.43 | -1.07 | 1 de 7 | 1 de 7 | 0 de 3 | no | 8% | 8% | -44.6% |
| 2.5 | Menos | 1.07 | 1.43 | +1.07 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | 92% | 92% | -1.2% |

### Goles visitante

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.7 | 1.36 | +0.86 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | 54% | 55% | -8.6% |
| 0.5 | Menos | 2.07 | 1.36 | -0.86 | 2 de 7 | 2 de 7 | 0 de 3 | no | 46% | 45% | -4.3% |
| 1.5 | Más | 4.25 | 1.36 | -0.14 | 4 de 7 | 2 de 7 | 1 de 3 | no | 17% | 19% | -25.8% |
| 1.5 | Menos | 1.2 | 1.36 | +0.14 | 3 de 7 | 5 de 7 | 2 de 3 | no | 83% | 81% | -1.0% |
| 2.5 | Más | 9.75 | 1.36 | -1.14 | 2 de 7 | 1 de 7 | 0 de 3 | no | 4% | 4% | -65.5% |
| 2.5 | Menos | 1.03 | 1.36 | +1.14 | 5 de 7 | 6 de 7 | 3 de 3 | SÍ | 96% | 96% | -0.6% |

### Goles 1T / 2T (sin estadística de goles por tiempo: SIN regularidad ni colchón; solo modelo y mercado)

| Ámbito | Línea | Lado | Cuota | p | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.67 | 56% | 57% | -7.0% |
| 1T | 0.5 | Menos | 2.18 | 44% | 43% | -3.4% |
| 1T | 0.75 | Más | 1.98 | 47% | 48% | -7.5% |
| 1T | 0.75 | Menos | 1.83 | 54% | 53% | -0.8% |
| 1T | 1.0 | Más | 2.72 | 33% | 35% | -10.4% |
| 1T | 1.0 | Menos | 1.47 | 69% | 67% | +1.1% |
| 1T | 1.25 | Más | 3.35 | 25% | 27% | -16.0% |
| 1T | 1.25 | Menos | 1.33 | 76% | 74% | +0.8% |
| 1T | 1.5 | Más | 3.85 | 20% | 22% | -23.9% |
| 1T | 1.5 | Menos | 1.25 | 80% | 78% | +0.3% |
| 1T | 2.5 | Más | 9.25 | 5% | 6% | -51.9% |
| 1T | 2.5 | Menos | 1.05 | 95% | 94% | -0.5% |
| 2T | 0.5 | Más | 1.55 | 62% | 62% | -4.2% |
| 2T | 0.5 | Menos | 2.42 | 38% | 38% | -7.6% |
| 2T | 1.5 | Más | 3.4 | 25% | 25% | -14.8% |
| 2T | 1.5 | Menos | 1.3 | 75% | 75% | -2.6% |
| 2T | 2.5 | Más | 8.25 | 7% | 8% | -38.4% |
| 2T | 2.5 | Menos | 1.07 | 93% | 92% | -1.0% |

Verificación propia de los conteos de la ficha en TODAS las líneas de total (incl. asiáticas, solo victoria completa) (mi recuento desde las series vs ficha, L/V): coinciden todas.


## Resultado, doble oportunidad, ambos marcan, hándicap, descanso/final

Regularidad derivada de las series de la ficha (marcadores de los últimos 7/7; no es un campo de la ficha). Evento medido en el partido de cada equipo en su propio papel: L = el equipo local de este partido, V = el visitante (ej. «Gana Estudiantes de La Plata»: L ganó X de 7; V perdió X de 7). Directos orientados [local, visitante] según la ficha (n=3). «Descanso o final» (`HOFR`) se muestra con el nombre que le da el informe; la regla exacta del mercado no está documentada en el repo.

| Selección | Cuota | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|
| Gana Estudiantes de La Plata | 2.42 | 1 de 7 | 2 de 7 | 1 de 3 | no | 41% | 40% | -1.9% |
| Empate | 2.8 | 4 de 7 | 3 de 7 | 2 de 3 | no | 34% | 34% | -4.5% |
| Gana Independiente Rivadavia | 3.55 | 2 de 7 | 2 de 7 | 0 de 3 | no | 25% | 26% | -9.9% |
| Estudiantes de La Plata o empate | 1.31 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | 75% | 74% | -2.2% |
| Independiente Rivadavia o empate | 1.57 | 6 de 7 | 5 de 7 | 2 de 3 | SÍ | 59% | 60% | -6.6% |
| No hay empate | 1.42 | 3 de 7 | 4 de 7 | 1 de 3 | no | 66% | 66% | -6.4% |
| 1.er tiempo: Estudiantes de La Plata | 3.2 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 28% | 28% | -9.0% |
| 1.er tiempo: Empate | 1.83 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 52% | 52% | -4.0% |
| 1.er tiempo: Independiente Rivadavia | 4.4 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 19% | 20% | -16.0% |
| 2.º tiempo: Estudiantes de La Plata | 3.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 31% | 30% | -7.2% |
| 2.º tiempo: Empate | 1.95 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 48% | 48% | -6.9% |
| 2.º tiempo: Independiente Rivadavia | 3.95 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 21% | 22% | -15.9% |
| Descanso o final: Estudiantes de La Plata | 1.98 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 47% | 47% | -6.6% |
| Descanso o final: Empate | 1.52 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 62% | 61% | -6.0% |
| Descanso o final: Independiente Rivadavia | 2.65 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 33% | 35% | -13.4% |
| Ambos marcan: Sí | 2.4 | 5 de 7 | 4 de 7 | 3 de 3 | no | 36% | 38% | -13.5% |
| Ambos marcan: No | 1.53 | 2 de 7 | 3 de 7 | 0 de 3 | no | 64% | 62% | -2.2% |
| Descanso/final: Estudiantes de La Plata / Estudiantes de La Plata | 3.9 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 23% | 22% | -12.1% |
| Descanso/final: Estudiantes de La Plata / Empate | 15.5 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 5% | 5% | -27.6% |
| Descanso/final: Estudiantes de La Plata / Independiente Rivadavia | 60.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 1% | 1% | -33.2% |
| Descanso/final: Empate / Estudiantes de La Plata | 5.4 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 16% | 15% | -11.9% |
| Descanso/final: Empate / Empate | 3.4 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 25% | 26% | -13.3% |
| Descanso/final: Empate / Independiente Rivadavia | 7.4 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 11% | 11% | -20.0% |
| Descanso/final: Independiente Rivadavia / Estudiantes de La Plata | 50.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 1% | 1% | -33.2% |
| Descanso/final: Independiente Rivadavia / Empate | 17.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 4% | 4% | -25.1% |
| Descanso/final: Independiente Rivadavia / Independiente Rivadavia | 5.8 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 13% | 14% | -22.7% |
| Hándicap Estudiantes de La Plata -3 | 30.0 | 0 de 7 | 1 de 7 | 0 de 3 | no | 1% | 1% | -72.5% |
| Hándicap empate (Estudiantes de La Plata -3) | 12.5 | 0 de 7 | 0 de 7 | 0 de 3 | no | 3% | 3% | -62.5% |
| Hándicap Independiente Rivadavia +3 | 1.03 | 7 de 7 | 6 de 7 | 3 de 3 | SÍ | 96% | 96% | -1.0% |
| Hándicap Estudiantes de La Plata -2 | 15.0 | 0 de 7 | 1 de 7 | 0 de 3 | no | 4% | 4% | -38.4% |
| Hándicap empate (Estudiantes de La Plata -2) | 7.0 | 0 de 7 | 0 de 7 | 0 de 3 | no | 11% | 11% | -24.9% |
| Hándicap Independiente Rivadavia +2 | 1.15 | 7 de 7 | 6 de 7 | 3 de 3 | SÍ | 85% | 85% | -2.1% |
| Hándicap Estudiantes de La Plata -1 | 5.8 | 0 de 7 | 1 de 7 | 0 de 3 | no | 15% | 15% | -14.5% |
| Hándicap empate (Estudiantes de La Plata -1) | 3.7 | 1 de 7 | 1 de 7 | 1 de 3 | no | 25% | 24% | -6.0% |
| Hándicap Independiente Rivadavia +1 | 1.57 | 6 de 7 | 5 de 7 | 2 de 3 | SÍ | 60% | 61% | -6.0% |
| Hándicap Estudiantes de La Plata +1 | 1.31 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | 75% | 74% | -1.9% |
| Hándicap empate (Estudiantes de La Plata +1) | 4.6 | 1 de 7 | 1 de 7 | 0 de 3 | no | 18% | 18% | -16.8% |
| Hándicap Independiente Rivadavia -1 | 10.0 | 1 de 7 | 1 de 7 | 0 de 3 | no | 7% | 8% | -29.6% |
| Hándicap Estudiantes de La Plata +2 | 1.07 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | 93% | 92% | -0.7% |
| Hándicap empate (Estudiantes de La Plata +2) | 9.5 | 1 de 7 | 1 de 7 | 0 de 3 | no | 6% | 6% | -45.4% |
| Hándicap Independiente Rivadavia -2 | 26.0 | 0 de 7 | 0 de 7 | 0 de 3 | no | 1% | 2% | -62.4% |
| Hándicap Estudiantes de La Plata -0.75 (asiática: devuelve 13%) | 3.05 | 0 de 7 | 1 de 7 | 0 de 3 | no | 32% | 31% | -3.8% |
| Hándicap Independiente Rivadavia +0.75 (asiática: devuelve 13%) | 1.4 | 6 de 7 | 5 de 7 | 2 de 3 | SÍ | 69% | 70% | -3.4% |
| Hándicap Estudiantes de La Plata -0.5 | 2.42 | 1 de 7 | 2 de 7 | 1 de 3 | no | 40% | 39% | -2.4% |
| Hándicap Independiente Rivadavia +0.5 | 1.6 | 6 de 7 | 5 de 7 | 2 de 3 | SÍ | 60% | 61% | -4.5% |
| Hándicap Estudiantes de La Plata -0.25 (asiática: devuelve 17%) | 2.02 | 1 de 7 | 2 de 7 | 1 de 3 | no | 49% | 48% | -1.3% |
| Hándicap Independiente Rivadavia +0.25 (asiática: devuelve 17%) | 1.83 | 2 de 7 | 2 de 7 | 0 de 3 | no | 52% | 53% | -5.1% |
| Hándicap Estudiantes de La Plata +0 (asiática: devuelve 34%) | 1.62 | 1 de 7 | 2 de 7 | 1 de 3 | no | 62% | 61% | -0.2% |
| Hándicap Independiente Rivadavia -0 (asiática: devuelve 34%) | 2.37 | 2 de 7 | 2 de 7 | 0 de 3 | no | 40% | 41% | -5.8% |
| Hándicap Estudiantes de La Plata +0.25 (asiática: devuelve 17%) | 1.42 | 1 de 7 | 2 de 7 | 1 de 3 | no | 70% | 69% | -0.9% |
| Hándicap Independiente Rivadavia -0.25 (asiática: devuelve 17%) | 2.95 | 2 de 7 | 2 de 7 | 0 de 3 | no | 31% | 32% | -8.7% |

Empate no apuesta (Betano `DNOB`; el informe no lo trae como línea; probabilidad derivada por mí de p_resultado excluyendo el empate y de la implícita del 1X2): Estudiantes de La Plata 1.6, Independiente Rivadavia 2.27. Modelo: Estudiantes de La Plata 61.6% / Independiente Rivadavia 38.4%; mercado (1X2 sin margen): 59.5% / 40.5%. EV con p del modelo (EV = p_victoria·cuota + p_empate·1 − 1): Estudiantes de La Plata -1.1%, Independiente Rivadavia -8.5%. Regularidad = la de «Gana …» más arriba (victoria completa).


### Verificación de la liquidación (final única, Córdoba, cancha neutra)
**NO VERIFICADO.** Grep acotado sobre `raw/bet_*.txt` (los tres partidos) buscando «prórroga», «tiempo reglamentario», «90 minutos», «penales/penaltis»: **0 coincidencias**. Esos archivos solo traen los códigos de mercado (`MRES`, `DBLC`, `HTFT`…) y cuotas, sin texto de reglas. Tampoco hay ficha ni nota con la regla (la nota solo dice «los mercados de Betano suelen liquidarse a 90 min (verificar)»). Por tanto no se puede afirmar desde el repo si el 1X2, doble oportunidad, hándicap, descanso/final y ambos marcan se liquidan a 90′ (+descuento) o incluyen prórroga/penales. Las series de la ficha (goles de la muestra) son de 90′ + descuento. Si Betano liquidara con prórroga, el «Empate» y «X/X» cambiarían de significado; hay que leer la regla en la página del mercado antes de tocar 1X2/doble/hándicap/htft. Las líneas de goles totales suelen ser a 90′ por convención, pero tampoco está confirmado aquí.


## Mejores líneas por probabilidad del informe que además cumplen ≥5 de 7 en ambos (cuota ≥ 1.20)

No es una recomendación: ordenado por p del informe (que sigue al mercado), no por EV.

| # | Línea | Cuota | Esperado | Colchón | L | V | D | p | EV |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Goles Más 1.0 | 1.28 | 2.79 | 1.79 | 5 de 7 | 5 de 7 | 3 de 3 | 76% | -2.1% |
| 2 | Hándicap Estudiantes de La Plata +1 | 1.31 | — | — | 5 de 7 | 5 de 7 | 3 de 3 | 75% | -1.9% |
| 3 | Estudiantes de La Plata o empate | 1.31 | — | — | 5 de 7 | 5 de 7 | 3 de 3 | 75% | -2.2% |
| 4 | Goles local Menos 1.5 | 1.33 | 1.43 | 0.07 | 5 de 7 | 5 de 7 | 1 de 3 | 73% | -3.0% |
| 5 | Hándicap Independiente Rivadavia +0.75 | 1.4 | — | — | 6 de 7 | 5 de 7 | 2 de 3 | 69% | -3.4% |
| 6 | Goles local Más 0.5 | 1.47 | 1.43 | 0.93 | 6 de 7 | 6 de 7 | 3 de 3 | 65% | -4.5% |
| 7 | Goles Más 1.25 | 1.52 | 2.79 | 1.54 | 5 de 7 | 5 de 7 | 3 de 3 | 63% | -4.2% |
| 8 | Hándicap Independiente Rivadavia +1 | 1.57 | — | — | 6 de 7 | 5 de 7 | 2 de 3 | 60% | -6.0% |

Líneas que cumplen pero con cuota < 1.20 (4): Goles Menos 4.5 @1.03, Goles visitante Menos 2.5 @1.03, Goles local Menos 2.5 @1.07, Goles Más 0.5 @1.18

## Límites
- Liquidación (90′ vs prórroga/penales) NO verificada en el repo (ver arriba).
- Sin alineaciones ni estadísticas de árbitro. Bajas de la previa de Flashscore: Correa y Castro (Estudiantes), Arce (Rivadavia), sin hora de la noticia. Estudiantes prepara la final de Libertadores vs Palmeiras (posible rotación, sin confirmar; la nota marca `rotacion: false`).
- Final a partido único en cancha neutra: «local/visitante» es solo el orden de Betano/Flashscore; la muestra mezcla sedes (la regla pide cualquier sede).
- n = 7+7 y 3 directos: 5 de 7 es un umbral de muestra pequeña. Sin goles por tiempo: 1T/2T, descanso/final y 1X2 de tiempos solo tienen modelo y mercado.
- Alertas del informe (10, de 16 a 40 pts) están en tarjetas; las probabilidades de goles/resultado salen de lambdas tomadas de Betano, por lo que coinciden con el mercado por construcción.
- El colchón es informativo y ninguna línea se excluye por él.

