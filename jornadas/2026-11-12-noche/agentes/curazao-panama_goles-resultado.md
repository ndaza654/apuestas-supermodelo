# Curazao - Panamá · goles y resultado

CONCACAF Nations League Play-offs · 2026-11-12 19:30 · cuotas Betano: Cuotas de Betano leídas 2026-11-12T22:29:12.295Z · 197 mercados

## Enfoque de mercados
Informe: «Favorito leve · medio · normal»; favorito Panamá (visitante). Pesan: goles del partido (Menos), 1T (Menos) y empate al descanso (ida: nadie quiere abrirse). Ambos marcan, resultado/hándicap, córners y tarjetas: neutros (el precio ya recoge el favoritismo). Hipótesis del informe, no cambia probabilidades.

## Qué ofrece Betano (raw/bet_*.txt, líneas `L|goles` y `U|…`)
- Goles: total 0.5, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.5, 4.5, 5.5; 1T 0.5, 0.75, 1, 1.25, 1.5, 2.5; 2T 0.5, 1.5, 2.5; Curazao 0.5, 1.5, 2.5; Panamá 0.5, 1.5, 2.5, 3.5.
- Únicos: 1X2, doble oportunidad, empate no apuesta, 1X2 de 1T y 2T, «descanso o final», ambos marcan, descanso/final (9), hándicap europeo (-2 a +3) y asiático (L -0.25 a +1.25). `4151`/`4152` sin etiqueta (no se analizan).
- Líneas de 1T/2T y córners/tarjetas por tiempo existen; sin tiros/faltas; jugadores solo «anota».

## Modelo vs mercado (1X2)
Margen de Betano en el 1X2: 4.9%. 

| | Curazao | Empate | Panamá |
|---|---|---|---|
| Cuota | 3.95 | 3.25 | 2.05 |
| Implícita sin margen (proporcional) | 24% | 29% | 47% |
| `p_resultado` (simulación con contexto) | 24% | 29% | 48% |
| Diferencia (modelo − mercado), pts | -0.6 | -0.6 | +1.3 |

Lambdas de goles: modelo 0.98 / 1.45; el informe declara `fuente_objetivos.g = mercado` para ambos equipos: las tasas de gol del modelo se parten de las propias cuotas de Betano. Por eso las probabilidades de goles/resultado salen casi iguales al mercado (distancia máxima «sin contexto vs mercado» en goles/resultado/ambos: ≤ 2 pts). **Esto NO es una segunda opinión independiente; no se usa como argumento a favor de ninguna línea.** `historial_vs_mercado` viene vacío (sin calibración propia).

**ALERTAS del modelo (5):** «Revisar: la simulación sin contexto se aleja 18 pts del merc…» (rango 18–31 pts). Líneas marcadas por familia: {'tarjetas': 14, 'corners': 2}. Ninguna línea de goles/resultado/ambos lleva la marca (su distancia sin contexto vs mercado es ≤ 2 pts), pero el informe sí dice que en otras familias la simulación se aleja del mercado: señal de que el modelo o el dato de ese partido pueden estar mal. Por eso las probabilidades de goles/resultado se muestran SIEMPRE con esta advertencia y NO se usan como argumento a favor de ninguna línea.


## Goles (ficha `goles`; goles del partido completo 90′+descuento; n: L 7, V 7, directos 1)

Esperado: local 1.57, visitante 1.64, total 3.21 (a favor/en contra: L 1.86/2.0, V 1.29/1.29). Colchón informativo = esperado − línea (Más) / línea − esperado (Menos). Cumple = ≥5 de 7 en AMBOS. Líneas .25/.75: solo victoria completa. «p» = probabilidad del informe, «p mkt» = implícita sin margen del informe, EV = p·cuota−1.


### Goles total

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.09 | 3.21 | +2.71 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | 90% | 90% | -1.6% |
| 0.5 | Menos | 7.6 | 3.21 | -2.71 | 1 de 7 | 0 de 7 | 0 de 1 | no | 10% | 10% | -26.4% |
| 1.5 | Más | 1.39 | 3.21 | +1.71 | 5 de 7 | 5 de 7 | 1 de 1 | SÍ | 69% | 70% | -4.4% |
| 1.5 | Menos | 3.05 | 3.21 | -1.71 | 2 de 7 | 2 de 7 | 0 de 1 | no | 31% | 30% | -4.7% |
| 1.75 | Más | 1.47 | 3.21 | +1.46 | 3 de 7 | 4 de 7 | 1 de 1 | no | 65% | 66% | -4.8% |
| 1.75 | Menos | 2.75 | 3.21 | -1.46 | 2 de 7 | 2 de 7 | 0 de 1 | no | 36% | 34% | -1.6% |
| 2.0 | Más | 1.62 | 3.21 | +1.21 | 3 de 7 | 4 de 7 | 1 de 1 | no | 59% | 60% | -4.9% |
| 2.0 | Menos | 2.35 | 3.21 | -1.21 | 2 de 7 | 2 de 7 | 0 de 1 | no | 42% | 41% | -0.4% |
| 2.25 | Más | 1.9 | 3.21 | +0.96 | 3 de 7 | 4 de 7 | 1 de 1 | no | 49% | 51% | -6.3% |
| 2.25 | Menos | 1.95 | 3.21 | -0.96 | 2 de 7 | 2 de 7 | 0 de 1 | no | 51% | 50% | -0.2% |
| 2.5 | Más | 2.15 | 3.21 | +0.71 | 3 de 7 | 4 de 7 | 1 de 1 | no | 42% | 44% | -9.0% |
| 2.5 | Menos | 1.72 | 3.21 | -0.71 | 4 de 7 | 3 de 7 | 0 de 1 | no | 58% | 56% | -0.8% |
| 2.75 | Más | 2.5 | 3.21 | +0.46 | 3 de 7 | 1 de 7 | 0 de 1 | no | 36% | 38% | -9.4% |
| 2.75 | Menos | 1.57 | 3.21 | -0.46 | 4 de 7 | 3 de 7 | 0 de 1 | no | 64% | 62% | +0.7% |
| 3.0 | Más | 3.15 | 3.21 | +0.21 | 3 de 7 | 1 de 7 | 0 de 1 | no | 28% | 30% | -11.4% |
| 3.0 | Menos | 1.39 | 3.21 | -0.21 | 4 de 7 | 3 de 7 | 0 de 1 | no | 73% | 71% | +1.0% |
| 3.5 | Más | 3.75 | 3.21 | -0.29 | 3 de 7 | 1 de 7 | 0 de 1 | no | 22% | 24% | -19.0% |
| 3.5 | Menos | 1.28 | 3.21 | +0.29 | 4 de 7 | 6 de 7 | 1 de 1 | no | 78% | 76% | +0.4% |
| 4.5 | Más | 7.1 | 3.21 | -1.29 | 3 de 7 | 1 de 7 | 0 de 1 | no | 9% | 10% | -36.7% |
| 4.5 | Menos | 1.1 | 3.21 | +1.29 | 4 de 7 | 6 de 7 | 1 de 1 | no | 91% | 90% | +0.2% |
| 5.5 | Más | 12.5 | 3.21 | -2.29 | 3 de 7 | 0 de 7 | 0 de 1 | no | 3% | 4% | -59.3% |
| 5.5 | Menos | 1.03 | 3.21 | +2.29 | 4 de 7 | 7 de 7 | 1 de 1 | no | 97% | 96% | -0.4% |

### Goles local

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.5 | 1.57 | +1.07 | 5 de 7 | 6 de 7 | 1 de 1 | SÍ | 62% | 64% | -6.4% |
| 0.5 | Menos | 2.47 | 1.57 | -1.07 | 2 de 7 | 1 de 7 | 0 de 1 | no | 38% | 36% | -7.2% |
| 1.5 | Más | 3.35 | 1.57 | +0.07 | 2 de 7 | 3 de 7 | 0 de 1 | no | 25% | 26% | -16.8% |
| 1.5 | Menos | 1.3 | 1.57 | -0.07 | 5 de 7 | 4 de 7 | 1 de 1 | no | 75% | 74% | -2.3% |
| 2.5 | Más | 7.9 | 1.57 | -0.93 | 2 de 7 | 0 de 7 | 0 de 1 | no | 7% | 7% | -47.8% |
| 2.5 | Menos | 1.06 | 1.57 | +0.93 | 5 de 7 | 7 de 7 | 1 de 1 | SÍ | 93% | 93% | -1.0% |

### Goles visitante

| Línea | Lado | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.25 | 1.64 | +1.14 | 5 de 7 | 4 de 7 | 1 de 1 | no | 77% | 78% | -3.8% |
| 0.5 | Menos | 3.7 | 1.64 | -1.14 | 2 de 7 | 3 de 7 | 0 de 1 | no | 23% | 22% | -14.8% |
| 1.5 | Más | 2.12 | 1.64 | +0.14 | 3 de 7 | 3 de 7 | 1 de 1 | no | 42% | 43% | -11.2% |
| 1.5 | Menos | 1.67 | 1.64 | -0.14 | 4 de 7 | 4 de 7 | 0 de 1 | no | 58% | 57% | -3.0% |
| 2.5 | Más | 4.4 | 1.64 | -0.86 | 2 de 7 | 2 de 7 | 0 de 1 | no | 17% | 18% | -27.2% |
| 2.5 | Menos | 1.19 | 1.64 | +0.86 | 5 de 7 | 5 de 7 | 1 de 1 | SÍ | 83% | 82% | -0.7% |
| 3.5 | Más | 8.75 | 1.64 | -1.86 | 1 de 7 | 0 de 7 | 0 de 1 | no | 5% | 6% | -57.4% |
| 3.5 | Menos | 1.05 | 1.64 | +1.86 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | 95% | 94% | -0.1% |

### Goles 1T / 2T (sin estadística de goles por tiempo: SIN regularidad ni colchón; solo modelo y mercado)

| Ámbito | Línea | Lado | Cuota | p | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.45 | 66% | 66% | -4.2% |
| 1T | 0.5 | Menos | 2.7 | 34% | 34% | -8.5% |
| 1T | 0.75 | Más | 1.62 | 59% | 60% | -4.3% |
| 1T | 0.75 | Menos | 2.3 | 42% | 41% | -3.6% |
| 1T | 1.0 | Más | 1.98 | 48% | 49% | -5.5% |
| 1T | 1.0 | Menos | 1.83 | 54% | 53% | -0.8% |
| 1T | 1.25 | Más | 2.47 | 37% | 38% | -9.7% |
| 1T | 1.25 | Menos | 1.55 | 64% | 63% | -0.2% |
| 1T | 1.5 | Más | 2.9 | 29% | 31% | -15.8% |
| 1T | 1.5 | Menos | 1.4 | 71% | 69% | -0.7% |
| 1T | 2.5 | Más | 6.7 | 10% | 11% | -36.4% |
| 1T | 2.5 | Menos | 1.1 | 90% | 89% | -0.4% |
| 2T | 0.5 | Más | 1.32 | 72% | 74% | -4.4% |
| 2T | 0.5 | Menos | 3.35 | 28% | 26% | -7.7% |
| 2T | 1.5 | Más | 2.37 | 37% | 39% | -11.3% |
| 2T | 1.5 | Menos | 1.57 | 63% | 61% | -1.8% |
| 2T | 2.5 | Más | 5.1 | 14% | 16% | -27.1% |
| 2T | 2.5 | Menos | 1.16 | 86% | 84% | -0.6% |

Verificación propia de los conteos de la ficha en TODAS las líneas de total (incl. asiáticas, solo victoria completa) (mi recuento desde las series vs ficha, L/V): coinciden todas.


## Resultado, doble oportunidad, ambos marcan, hándicap, descanso/final

Regularidad derivada de las series de la ficha (marcadores de los últimos 7/7; no es un campo de la ficha). Evento medido en el partido de cada equipo en su propio papel: L = el equipo local de este partido, V = el visitante (ej. «Gana Curazao»: L ganó X de 7; V perdió X de 7). Directos orientados [local, visitante] según la ficha (n=1). «Descanso o final» (`HOFR`) se muestra con el nombre que le da el informe; la regla exacta del mercado no está documentada en el repo.

| Selección | Cuota | L | V | Directos | Cumple | p | p mkt | EV |
|---|---|---|---|---|---|---|---|---|
| Gana Curazao | 3.95 | 3 de 7 | 4 de 7 | 0 de 1 | no | 24% | 24% | -6.6% |
| Empate | 3.25 | 2 de 7 | 0 de 7 | 0 de 1 | no | 29% | 29% | -5.0% |
| Gana Panamá | 2.05 | 2 de 7 | 3 de 7 | 1 de 1 | no | 47% | 47% | -3.4% |
| Curazao o empate | 1.8 | 5 de 7 | 4 de 7 | 0 de 1 | no | 53% | 53% | -4.9% |
| Panamá o empate | 1.27 | 4 de 7 | 3 de 7 | 1 de 1 | no | 76% | 76% | -3.0% |
| No hay empate | 1.33 | 5 de 7 | 7 de 7 | 1 de 1 | SÍ | 71% | 71% | -5.9% |
| 1.er tiempo: Curazao | 4.4 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 20% | 20% | -12.4% |
| 1.er tiempo: Empate | 2.07 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 45% | 45% | -7.4% |
| 1.er tiempo: Panamá | 2.62 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 35% | 35% | -7.4% |
| 2.º tiempo: Curazao | 3.9 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 23% | 22% | -11.9% |
| 2.º tiempo: Empate | 2.32 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 41% | 40% | -5.9% |
| 2.º tiempo: Panamá | 2.42 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 37% | 38% | -10.9% |
| Descanso o final: Curazao | 2.72 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 33% | 34% | -11.0% |
| Descanso o final: Empate | 1.65 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 56% | 57% | -7.8% |
| Descanso o final: Panamá | 1.7 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 55% | 55% | -7.0% |
| Ambos marcan: Sí | 1.85 | 4 de 7 | 3 de 7 | 1 de 1 | no | 49% | 50% | -9.4% |
| Ambos marcan: No | 1.88 | 3 de 7 | 4 de 7 | 0 de 1 | no | 51% | 50% | -4.1% |
| Descanso/final: Curazao / Curazao | 6.5 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 13% | 13% | -18.3% |
| Descanso/final: Curazao / Empate | 15.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 5% | 5% | -24.7% |
| Descanso/final: Curazao / Panamá | 32.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 2% | 2% | -24.1% |
| Descanso/final: Empate / Curazao | 8.5 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 10% | 9% | -19.1% |
| Descanso/final: Empate / Empate | 4.55 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 19% | 19% | -14.9% |
| Descanso/final: Empate / Panamá | 5.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 17% | 17% | -17.1% |
| Descanso/final: Panamá / Curazao | 45.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 2% | 2% | -31.3% |
| Descanso/final: Panamá / Empate | 14.0 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 6% | 5% | -21.1% |
| Descanso/final: Panamá / Panamá | 3.2 | — | — | — | sin estadística por tiempo (solo modelo y mercado) | 28% | 28% | -10.2% |
| Hándicap Curazao -2 | 24.0 | 1 de 7 | 0 de 7 | 0 de 1 | no | 2% | 2% | -56.5% |
| Hándicap empate (Curazao -2) | 10.0 | 0 de 7 | 1 de 7 | 0 de 1 | no | 6% | 6% | -41.9% |
| Hándicap Panamá +2 | 1.07 | 6 de 7 | 6 de 7 | 1 de 1 | SÍ | 92% | 92% | -1.2% |
| Hándicap Curazao -1 | 9.75 | 1 de 7 | 1 de 7 | 0 de 1 | no | 8% | 8% | -26.6% |
| Hándicap empate (Curazao -1) | 5.2 | 2 de 7 | 3 de 7 | 0 de 1 | no | 16% | 16% | -16.8% |
| Hándicap Panamá +1 | 1.27 | 4 de 7 | 3 de 7 | 1 de 1 | no | 76% | 76% | -2.9% |
| Hándicap Curazao +1 | 1.8 | 5 de 7 | 4 de 7 | 0 de 1 | no | 53% | 53% | -4.8% |
| Hándicap empate (Curazao +1) | 3.65 | 0 de 7 | 2 de 7 | 1 de 1 | no | 25% | 25% | -7.7% |
| Hándicap Panamá -1 | 3.95 | 2 de 7 | 1 de 7 | 0 de 1 | no | 22% | 23% | -13.7% |
| Hándicap Curazao +2 | 1.26 | 5 de 7 | 6 de 7 | 1 de 1 | SÍ | 78% | 77% | -1.6% |
| Hándicap empate (Curazao +2) | 5.8 | 1 de 7 | 0 de 7 | 0 de 1 | no | 14% | 14% | -17.4% |
| Hándicap Panamá -2 | 9.0 | 1 de 7 | 1 de 7 | 0 de 1 | no | 8% | 9% | -30.9% |
| Hándicap Curazao +3 | 1.08 | 6 de 7 | 6 de 7 | 1 de 1 | SÍ | 92% | 91% | -0.4% |
| Hándicap empate (Curazao +3) | 10.0 | 0 de 7 | 1 de 7 | 0 de 1 | no | 6% | 6% | -43.5% |
| Hándicap Panamá -3 | 19.5 | 1 de 7 | 0 de 7 | 0 de 1 | no | 2% | 3% | -57.8% |
| Hándicap Curazao -0.25 (asiática: devuelve 14%) | 3.3 | 3 de 7 | 4 de 7 | 0 de 1 | no | 28% | 28% | -7.6% |
| Hándicap Panamá +0.25 (asiática: devuelve 14%) | 1.35 | 2 de 7 | 3 de 7 | 1 de 1 | no | 73% | 73% | -1.9% |
| Hándicap Curazao +0 (asiática: devuelve 29%) | 2.8 | 3 de 7 | 4 de 7 | 0 de 1 | no | 34% | 34% | -4.5% |
| Hándicap Panamá -0 (asiática: devuelve 29%) | 1.47 | 2 de 7 | 3 de 7 | 1 de 1 | no | 67% | 67% | -1.5% |
| Hándicap Curazao +0.25 (asiática: devuelve 14%) | 2.12 | 3 de 7 | 4 de 7 | 0 de 1 | no | 45% | 45% | -4.2% |
| Hándicap Panamá -0.25 (asiática: devuelve 14%) | 1.75 | 2 de 7 | 3 de 7 | 1 de 1 | no | 55% | 55% | -3.0% |
| Hándicap Curazao +0.5 | 1.83 | 5 de 7 | 4 de 7 | 0 de 1 | no | 53% | 53% | -3.5% |
| Hándicap Panamá -0.5 | 2.02 | 2 de 7 | 3 de 7 | 1 de 1 | no | 47% | 47% | -4.6% |
| Hándicap Curazao +0.75 (asiática: devuelve 13%) | 1.62 | 5 de 7 | 4 de 7 | 0 de 1 | no | 61% | 60% | -1.9% |
| Hándicap Panamá -0.75 (asiática: devuelve 13%) | 2.37 | 2 de 7 | 1 de 7 | 0 de 1 | no | 40% | 40% | -5.3% |

Empate no apuesta (Betano `DNOB`; el informe no lo trae como línea; probabilidad derivada por mí de p_resultado excluyendo el empate y de la implícita del 1X2): Curazao 2.67, Panamá 1.44. Modelo: Curazao 33.0% / Panamá 67.0%; mercado (1X2 sin margen): 34.2% / 65.8%. EV con p del modelo (EV = p_victoria·cuota + p_empate·1 − 1): Curazao -8.6%, Panamá -2.5%. Regularidad = la de «Gana …» más arriba (victoria completa).


### Directos y muestra
Un solo directo en la ficha (13-oct-2023, Nations League, Curazao 1-2 Panamá según la serie): n=1, no sirve como criterio. Los últimos 7 de Curazao incluyen 3 del Mundial (jun-2026) y 4 de Nations League; los de Panamá, 5 del Mundial/eliminatoria y 2 de la Kirin Cup (amistosa que Flashscore marca como oficial).

### Esperado de la ficha vs lo que cobra Betano
El esperado de la ficha para el total (3.21 goles) está muy por encima de lo que Betano espera (~2.45 según `medias.betano` del informe; línea central 2.5 @2.15 Más / 1.72 Menos). La muestra de Curazao trae un 6-1 y un 1-7 (rivales de nivel muy distinto) que inflan el promedio; el colchón de las líneas «Más» sale por eso muy holgado y de las «Menos» negativo. Es informativo, no mide la probabilidad real.


## Mejores líneas por probabilidad del informe que además cumplen ≥5 de 7 en ambos (cuota ≥ 1.20)

No es una recomendación: ordenado por p del informe (que sigue al mercado), no por EV.

| # | Línea | Cuota | Esperado | Colchón | L | V | D | p | EV |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Hándicap Curazao +2 | 1.26 | — | — | 5 de 7 | 6 de 7 | 1 de 1 | 78% | -1.6% |
| 2 | No hay empate | 1.33 | — | — | 5 de 7 | 7 de 7 | 1 de 1 | 71% | -5.9% |
| 3 | Goles Más 1.5 | 1.39 | 3.21 | 1.71 | 5 de 7 | 5 de 7 | 1 de 1 | 69% | -4.4% |
| 4 | Goles local Más 0.5 | 1.5 | 1.57 | 1.07 | 5 de 7 | 6 de 7 | 1 de 1 | 62% | -6.4% |

Líneas que cumplen pero con cuota < 1.20 (4): Goles visitante Menos 3.5 @1.05, Goles local Menos 2.5 @1.06, Goles Más 0.5 @1.09, Goles visitante Menos 2.5 @1.19

## Límites
- Muestra mezclada (Mundial / Nations League / Kirin Cup) y rivales de nivel muy desigual: 6-1 y 1-7 de Curazao dominan el promedio. Un directo (n=1).
- Sin alineaciones, sin árbitro (Penso M. sin estadística), 39 días sin partido oficial para ambos (descanso).
- Alertas del informe (5, de 18 a 31 pts) caen en tarjetas y 2 líneas de córners; goles/resultado no llevan marca, pero sus probabilidades salen de lambdas de Betano, o sea iguales al mercado por construcción: no son señal propia.
- Sin goles por tiempo: 1T/2T, descanso/final y 1X2 por tiempos solo tienen modelo y mercado. Betano no indica si la ida de cuartos se liquida solo a 90′ (la regla del mercado no está en el repo; no se verificó).
- n = 7+7: 5 de 7 es umbral de muestra pequeña.

