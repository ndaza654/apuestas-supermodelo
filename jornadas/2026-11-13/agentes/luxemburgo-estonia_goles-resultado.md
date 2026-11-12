# Goles y resultado · Luxemburgo - Estonia · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas de Betano leídas 2026-11-12T17:32:24.886Z · 169 mercados (UTC; 17:32 UTC = 12:32 Bogotá). Todas las cifras salen de `fichas/ficha_luxemburgo-estonia.json` (clave `goles`, `contexto`), `informes/luxemburgo-estonia_resultado.json` y `betano/luxemburgo-estonia.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (8 líneas), de Luxemburgo (3), de Estonia (3), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 10 mercados de hándicap.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 36 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 4 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 1.6 pts (Descanso o final: Estonia). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 1.19 / 0.99 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.11 | 2.16 | 2.18 | 1.44 | 0.0–4.0 |
| local | 1.15 | 1.17 | 1.19 | 1.03 | 0.0–3.0 |
| visitante | 0.96 | 0.99 | 0.99 | 0.95 | 0.0–2.0 |
| 1T | 0.93 | 0.96 | 0.94 | 0.97 | 0.0–2.0 |
| 2T | 1.18 | 1.2 | 1.26 | 1.08 | 0.0–3.0 |

Esperado de la ficha (historial) vs media implícita de Betano: total 1.57 vs 2.18; Luxemburgo 0.71 vs 1.19; Estonia 0.86 vs 0.99. Cuando difieren mucho, el colchón (basado en el historial) y las cuotas cuentan historias distintas.

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Luxemburgo: motivación alta, necesita ganar True, rotación False. Estonia: motivación alta, necesita ganar False, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Luxemburgo n = 7, Estonia n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Luxemburgo 0.71 (a favor 1.0 · Estonia concede 0.43); Estonia 0.86 (a favor 0.57 · Luxemburgo concede 1.14); total 1.57.
- Series (a favor–en contra): Luxemburgo 0-2 0-1 0-3 2-1 3-0 2-0 0-1; Estonia 0-0 1-0 0-0 1-1 1-0 1-0 0-2; directos (total) 1.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.11 | 1.57 | +1.07 | 7 de 7 | 5 de 7 | 1 de 1 | SÍ | no | 0.883 | 0.883 | -0.020 |
| 0.5 | Menos | 6.0 | 1.57 | -1.07 | 0 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.117 | 0.117 | -0.297 |
| 1.5 | Más | 1.5 | 1.57 | +0.07 | 5 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.622 | 0.638 | -0.067 |
| 1.5 | Menos | 2.5 | 1.57 | -0.07 | 2 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.378 | 0.362 | -0.055 |
| 1.75 | Más | 1.62 | 1.57 | -0.18 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.575 | 0.593 | -0.069 |
| 1.75 | Menos | 2.25 | 1.57 | +0.18 | 2 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.433 | 0.415 | -0.025 |
| 2 | Más | 1.85 | 1.57 | -0.43 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.504 | 0.519 | -0.067 |
| 2 | Menos | 1.93 | 1.57 | +0.43 | 2 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.511 | 0.496 | -0.013 |
| 2.25 | Más | 2.15 | 1.57 | -0.68 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.423 | 0.436 | -0.091 |
| 2.25 | Menos | 1.67 | 1.57 | +0.68 | 2 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.585 | 0.573 | -0.022 |
| 2.5 | Más | 2.42 | 1.57 | -0.93 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.362 | 0.373 | -0.124 |
| 2.5 | Menos | 1.52 | 1.57 | +0.93 | 4 de 7 | 7 de 7 | 1 de 1 | no | sí | 0.638 | 0.627 | -0.030 |
| 3.5 | Más | 4.4 | 1.57 | -1.93 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.163 | 0.181 | -0.281 |
| 3.5 | Menos | 1.19 | 1.57 | +1.93 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.837 | 0.819 | -0.004 |
| 4.5 | Más | 7.9 | 1.57 | -2.93 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.062 | 0.072 | -0.510 |
| 4.5 | Menos | 1.06 | 1.57 | +2.93 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.938 | 0.928 | -0.006 |

### Goles · Luxemburgo (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.38 | 0.71 | +0.21 | 3 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.695 | 0.698 | -0.041 |
| 0.5 | Menos | 2.92 | 0.71 | -0.21 | 4 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.305 | 0.302 | -0.110 |
| 1.5 | Más | 2.67 | 0.71 | -0.79 | 3 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.325 | 0.334 | -0.133 |
| 1.5 | Menos | 1.44 | 0.71 | +0.79 | 4 de 7 | 6 de 7 | 1 de 1* | no | sí | 0.675 | 0.666 | -0.028 |
| 2.5 | Más | 5.9 | 0.71 | -1.79 | 1 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.107 | 0.118 | -0.370 |
| 2.5 | Menos | 1.11 | 0.71 | +1.79 | 6 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.893 | 0.882 | -0.008 |

### Goles · Estonia (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.5 | 0.86 | +0.36 | 5 de 7 | 4 de 7 | 1 de 1* | no | sí | 0.630 | 0.636 | -0.056 |
| 0.5 | Menos | 2.47 | 0.86 | -0.36 | 2 de 7 | 3 de 7 | 0 de 1* | no | sí | 0.370 | 0.364 | -0.085 |
| 1.5 | Más | 3.3 | 0.86 | -0.64 | 2 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.248 | 0.258 | -0.183 |
| 1.5 | Menos | 1.3 | 0.86 | +0.64 | 5 de 7 | 7 de 7 | 1 de 1* | SÍ | sí | 0.752 | 0.742 | -0.022 |
| 2.5 | Más | 7.7 | 0.86 | -1.64 | 1 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.068 | 0.072 | -0.478 |
| 2.5 | Menos | 1.06 | 0.86 | +1.64 | 6 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.932 | 0.928 | -0.012 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.57 | 0.597 | 0.605 | -0.063 |
| 1T | 0.5 | Menos | 2.3 | 0.403 | 0.395 | -0.072 |
| 1T | 0.75 | Más | 1.83 | 0.515 | 0.523 | -0.058 |
| 1T | 0.75 | Menos | 1.95 | 0.496 | 0.488 | -0.033 |
| 1T | 1 | Más | 2.42 | 0.385 | 0.393 | -0.069 |
| 1T | 1 | Menos | 1.55 | 0.636 | 0.629 | -0.014 |
| 1T | 1.25 | Más | 3.0 | 0.295 | 0.302 | -0.114 |
| 1T | 1.25 | Menos | 1.37 | 0.716 | 0.709 | -0.019 |
| 1T | 1.5 | Más | 3.5 | 0.236 | 0.243 | -0.174 |
| 1T | 1.5 | Menos | 1.28 | 0.764 | 0.757 | -0.022 |
| 1T | 2.5 | Más | 8.0 | 0.068 | 0.071 | -0.454 |
| 1T | 2.5 | Menos | 1.06 | 0.932 | 0.929 | -0.012 |
| 2T | 0.5 | Más | 1.35 | 0.705 | 0.716 | -0.048 |
| 2T | 0.5 | Menos | 3.1 | 0.295 | 0.284 | -0.086 |
| 2T | 1.5 | Más | 2.55 | 0.341 | 0.359 | -0.132 |
| 2T | 1.5 | Menos | 1.5 | 0.659 | 0.641 | -0.011 |
| 2T | 2.5 | Más | 5.7 | 0.123 | 0.132 | -0.300 |
| 2T | 2.5 | Menos | 1.13 | 0.877 | 0.868 | -0.009 |

Comprobación: Betano trae 23 líneas de goles; la ficha trae 23 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 2.4 / 3.15 / 3.2; margen 4.7%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Luxemburgo | 2.4 | 0.403 | 0.401 | 0.398 | +0.2 |
| Empate | 3.15 | 0.303 | 0.302 | 0.303 | +0.1 |
| Estonia | 3.2 | 0.293 | 0.297 | 0.299 | -0.4 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Luxemburgo: ganó 3 de 7, no perdió 3 de 7, marcó 3 de 7, dejó la portería a cero 2 de 7, ambos marcaron 1 de 7.
- Estonia: ganó 3 de 7, no perdió 6 de 7, marcó 4 de 7, dejó la portería a cero 5 de 7, ambos marcaron 1 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Luxemburgo | 2.4 | 0.406 | 0.398 | 0.401 | +0.5 | -0.026 |
| Empate | 3.15 | 0.298 | 0.307 | 0.302 | -0.4 | -0.060 |
| Gana Estonia | 3.2 | 0.296 | 0.295 | 0.297 | -0.1 | -0.054 |
| Luxemburgo o empate | 1.38 | 0.704 | 0.705 | 0.703 | +0.1 | -0.028 |
| Estonia o empate | 1.6 | 0.594 | 0.602 | 0.599 | -0.5 | -0.050 |
| No hay empate | 1.35 | 0.702 | 0.693 | 0.698 | +0.3 | -0.053 |
| 1.er tiempo: Luxemburgo | 3.1 | 0.280 | 0.285 | 0.285 | -0.5 | -0.132 |
| 1.er tiempo: Empate | 1.9 | 0.497 | 0.490 | 0.491 | +0.7 | -0.055 |
| 1.er tiempo: Estonia | 3.85 | 0.223 | 0.225 | 0.224 | -0.2 | -0.143 |
| 2.º tiempo: Luxemburgo | 2.75 | 0.328 | 0.326 | 0.329 | -0.2 | -0.099 |
| 2.º tiempo: Empate | 2.25 | 0.417 | 0.418 | 0.410 | +0.7 | -0.061 |
| 2.º tiempo: Estonia | 3.4 | 0.255 | 0.256 | 0.261 | -0.6 | -0.133 |
| Descanso o final: Luxemburgo | 1.93 | 0.478 | 0.473 | 0.484 | -0.6 | -0.078 |
| Descanso o final: Empate | 1.57 | 0.596 | 0.593 | 0.595 | +0.1 | -0.064 |
| Descanso o final: Estonia | 2.37 | 0.377 | 0.379 | 0.394 | -1.7 | -0.107 |
| Ambos marcan: Sí | 2.05 | 0.440 | 0.452 | 0.448 | -0.7 | -0.097 |
| Ambos marcan: No | 1.7 | 0.560 | 0.548 | 0.552 | +0.7 | -0.049 |
| Descanso/final: Luxemburgo / Luxemburgo | 3.95 | 0.217 | 0.218 | 0.220 | -0.3 | -0.143 |
| Descanso/final: Luxemburgo / Empate | 15.0 | 0.050 | 0.051 | 0.050 | -0.1 | -0.253 |
| Descanso/final: Luxemburgo / Estonia | 45.0 | 0.013 | 0.016 | 0.015 | -0.2 | -0.401 |
| Descanso/final: Empate / Luxemburgo | 5.2 | 0.169 | 0.161 | 0.162 | +0.6 | -0.123 |
| Descanso/final: Empate / Empate | 4.2 | 0.204 | 0.208 | 0.205 | -0.2 | -0.145 |
| Descanso/final: Empate / Estonia | 6.6 | 0.126 | 0.122 | 0.125 | +0.1 | -0.169 |
| Descanso/final: Estonia / Luxemburgo | 37.0 | 0.020 | 0.019 | 0.019 | +0.1 | -0.259 |
| Descanso/final: Estonia / Empate | 15.5 | 0.046 | 0.050 | 0.049 | -0.2 | -0.284 |
| Descanso/final: Estonia / Estonia | 5.4 | 0.156 | 0.156 | 0.156 | +0.0 | -0.160 |
| Hándicap Luxemburgo -3 | 29.0 | 0.012 | 0.013 | 0.015 | -0.3 | -0.657 |
| Hándicap empate (Luxemburgo -3) | 12.5 | 0.037 | 0.039 | 0.043 | -0.7 | -0.541 |
| Hándicap Estonia +3 | 1.05 | 0.952 | 0.949 | 0.941 | +1.0 | -0.001 |
| Hándicap Luxemburgo -2 | 13.0 | 0.047 | 0.050 | 0.056 | -0.9 | -0.388 |
| Hándicap empate (Luxemburgo -2) | 6.9 | 0.110 | 0.113 | 0.114 | -0.4 | -0.243 |
| Hándicap Estonia +2 | 1.18 | 0.843 | 0.837 | 0.830 | +1.3 | -0.005 |
| Hándicap Luxemburgo -1 | 5.2 | 0.156 | 0.162 | 0.168 | -1.2 | -0.188 |
| Hándicap empate (Luxemburgo -1) | 3.9 | 0.248 | 0.235 | 0.230 | +1.9 | -0.031 |
| Hándicap Estonia +1 | 1.6 | 0.596 | 0.603 | 0.602 | -0.6 | -0.047 |
| Hándicap Luxemburgo +1 | 1.38 | 0.704 | 0.705 | 0.703 | +0.1 | -0.028 |
| Hándicap empate (Luxemburgo +1) | 4.55 | 0.197 | 0.192 | 0.191 | +0.6 | -0.103 |
| Hándicap Estonia -1 | 7.8 | 0.098 | 0.103 | 0.106 | -0.7 | -0.232 |
| Hándicap Luxemburgo +2 | 1.1 | 0.901 | 0.897 | 0.894 | +0.7 | -0.008 |
| Hándicap empate (Luxemburgo +2) | 8.75 | 0.073 | 0.076 | 0.078 | -0.5 | -0.362 |
| Hándicap Estonia -2 | 21.0 | 0.025 | 0.027 | 0.028 | -0.2 | -0.464 |
| Hándicap Luxemburgo -0.75 | 2.8 | 0.325 | 0.322 | 0.325 | -0.0 | -0.090 |
| Hándicap Estonia +0.75 | 1.42 | 0.683 | 0.685 | 0.682 | +0.0 | -0.031 |
| Hándicap Luxemburgo -0.5 | 2.32 | 0.406 | 0.398 | 0.400 | +0.5 | -0.059 |
| Hándicap Estonia +0.5 | 1.6 | 0.594 | 0.602 | 0.600 | -0.5 | -0.049 |
| Hándicap Luxemburgo -0.25 | 2.0 | 0.480 | 0.475 | 0.476 | +0.4 | -0.040 |
| Hándicap Estonia +0.25 | 1.8 | 0.528 | 0.534 | 0.533 | -0.5 | -0.049 |
| Hándicap Luxemburgo +0 | 1.67 | 0.584 | 0.581 | 0.580 | +0.3 | -0.025 |
| Hándicap Estonia -0 | 2.18 | 0.434 | 0.437 | 0.438 | -0.4 | -0.055 |
| Hándicap Luxemburgo +0.25 | 1.47 | 0.658 | 0.657 | 0.657 | +0.1 | -0.033 |
| Hándicap Estonia -0.25 | 2.6 | 0.352 | 0.353 | 0.353 | -0.1 | -0.085 |

Diferencia máxima modelo − mercado en estas selecciones: 1.9 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
