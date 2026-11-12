# Goles y resultado · Moldavia - Kazajistán · UEFA Liga de Naciones · 2026-11-13 12:00 (Bogotá)

Agente goles-resultado. Cuotas de Betano leídas 2026-11-12T17:32:22.660Z · 169 mercados (UTC; 17:32 UTC = 12:32 Bogotá). Todas las cifras salen de `fichas/ficha_moldavia-kazajistan.json` (clave `goles`, `contexto`), `informes/moldavia-kazajistan_resultado.json` y `betano/moldavia-kazajistan.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (8 líneas), de Moldavia (3), de Kazajistán (3), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 10 mercados de hándicap.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 3 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 38 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 4 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 1.6 pts (Descanso o final: Kazajistán). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 1.12 / 1.07 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.15 | 2.2 | 2.2 | 1.45 | 0.0–4.0 |
| local | 1.09 | 1.13 | 1.13 | 1.0 | 0.0–2.0 |
| visitante | 1.05 | 1.07 | 1.08 | 0.99 | 0.0–2.0 |
| 1T | 0.92 | 0.98 | 1.02 | 0.97 | 0.0–2.0 |
| 2T | 1.22 | 1.22 | 1.19 | 1.1 | 0.0–3.0 |

Esperado de la ficha (historial) vs media implícita de Betano: total 2.64 vs 2.2; Moldavia 0.93 vs 1.13; Kazajistán 1.71 vs 1.08. Cuando difieren mucho, el colchón (basado en el historial) y las cuotas cuentan historias distintas.

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Moldavia: motivación alta, necesita ganar True, rotación False. Kazajistán: motivación alta, necesita ganar True, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Moldavia n = 7, Kazajistán n = 7, directos n = 3.
- Esperado = (a favor propio + concedido por el rival)/2: Moldavia 0.93 (a favor 0.71 · Kazajistán concede 1.14); Kazajistán 1.71 (a favor 1.29 · Moldavia concede 2.14); total 2.64.
- Series (a favor–en contra): Moldavia 0-4 2-1 1-1 0-2 1-4 0-2 1-1; Kazajistán 2-2 1-2 1-2 1-1 1-0 2-0 1-1; directos (total) 3 2 3.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.11 | 2.64 | +2.14 | 7 de 7 | 7 de 7 | 3 de 3 | SÍ | no | 0.890 | 0.883 | -0.011 |
| 0.5 | Menos | 6.0 | 2.64 | -2.14 | 0 de 7 | 0 de 7 | 0 de 3 | no | sí | 0.110 | 0.117 | -0.343 |
| 1.5 | Más | 1.47 | 2.64 | +1.14 | 7 de 7 | 6 de 7 | 3 de 3 | SÍ | sí | 0.625 | 0.649 | -0.081 |
| 1.5 | Menos | 2.55 | 2.64 | -1.14 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.375 | 0.350 | -0.044 |
| 1.75 | Más | 1.62 | 2.64 | +0.89 | 3 de 7 | 3 de 7 | 2 de 3 | no | sí | 0.573 | 0.593 | -0.072 |
| 1.75 | Menos | 2.25 | 2.64 | -0.89 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.436 | 0.415 | -0.020 |
| 2 | Más | 1.83 | 2.64 | +0.64 | 3 de 7 | 3 de 7 | 2 de 3 | no | sí | 0.505 | 0.523 | -0.076 |
| 2 | Menos | 1.93 | 2.64 | -0.64 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.512 | 0.494 | -0.011 |
| 2.25 | Más | 2.12 | 2.64 | +0.39 | 3 de 7 | 3 de 7 | 2 de 3 | no | sí | 0.426 | 0.444 | -0.097 |
| 2.25 | Menos | 1.7 | 2.64 | -0.39 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.582 | 0.564 | -0.011 |
| 2.5 | Más | 2.4 | 2.64 | +0.14 | 3 de 7 | 3 de 7 | 2 de 3 | no | sí | 0.363 | 0.377 | -0.129 |
| 2.5 | Menos | 1.53 | 2.64 | -0.14 | 4 de 7 | 4 de 7 | 1 de 3 | no | sí | 0.637 | 0.623 | -0.025 |
| 3.5 | Más | 4.35 | 2.64 | -0.86 | 2 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.166 | 0.182 | -0.280 |
| 3.5 | Menos | 1.19 | 2.64 | +0.86 | 5 de 7 | 6 de 7 | 3 de 3 | SÍ | no | 0.834 | 0.818 | -0.007 |
| 4.5 | Más | 7.8 | 2.64 | -1.86 | 1 de 7 | 0 de 7 | 0 de 3 | no | sí | 0.069 | 0.072 | -0.466 |
| 4.5 | Menos | 1.06 | 2.64 | +1.86 | 6 de 7 | 7 de 7 | 3 de 3 | SÍ | no | 0.931 | 0.928 | -0.013 |

### Goles · Moldavia (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.4 | 0.93 | +0.43 | 4 de 7 | 5 de 7 | 3 de 3* | no | sí | 0.675 | 0.685 | -0.055 |
| 0.5 | Menos | 2.8 | 0.93 | -0.43 | 3 de 7 | 2 de 7 | 0 de 3* | no | sí | 0.325 | 0.315 | -0.090 |
| 1.5 | Más | 2.85 | 0.93 | -0.57 | 1 de 7 | 3 de 7 | 1 de 3* | no | sí | 0.297 | 0.309 | -0.152 |
| 1.5 | Menos | 1.39 | 0.93 | +0.57 | 6 de 7 | 4 de 7 | 2 de 3* | no | sí | 0.703 | 0.691 | -0.023 |
| 2.5 | Más | 6.6 | 0.93 | -1.57 | 0 de 7 | 0 de 7 | 0 de 3* | no | sí | 0.090 | 0.100 | -0.407 |
| 2.5 | Menos | 1.09 | 0.93 | +1.57 | 7 de 7 | 7 de 7 | 3 de 3* | SÍ | no | 0.910 | 0.900 | -0.008 |

### Goles · Kazajistán (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.45 | 1.71 | +1.21 | 7 de 7 | 7 de 7 | 3 de 3* | SÍ | sí | 0.663 | 0.662 | -0.038 |
| 0.5 | Menos | 2.65 | 1.71 | -1.21 | 0 de 7 | 0 de 7 | 0 de 3* | no | sí | 0.337 | 0.338 | -0.107 |
| 1.5 | Más | 3.0 | 1.71 | +0.21 | 4 de 7 | 2 de 7 | 1 de 3* | no | sí | 0.285 | 0.292 | -0.146 |
| 1.5 | Menos | 1.36 | 1.71 | -0.21 | 3 de 7 | 5 de 7 | 2 de 3* | no | sí | 0.715 | 0.708 | -0.027 |
| 2.5 | Más | 6.9 | 1.71 | -0.79 | 2 de 7 | 0 de 7 | 0 de 3* | no | sí | 0.086 | 0.091 | -0.409 |
| 2.5 | Menos | 1.08 | 1.71 | +0.79 | 5 de 7 | 7 de 7 | 3 de 3* | SÍ | no | 0.914 | 0.909 | -0.013 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.5 | 0.605 | 0.634 | -0.093 |
| 1T | 0.5 | Menos | 2.45 | 0.395 | 0.366 | -0.031 |
| 1T | 0.75 | Más | 1.72 | 0.528 | 0.556 | -0.092 |
| 1T | 0.75 | Menos | 2.07 | 0.483 | 0.455 | +0.001 |
| 1T | 1 | Más | 2.18 | 0.410 | 0.439 | -0.106 |
| 1T | 1 | Menos | 1.67 | 0.611 | 0.582 | +0.020 |
| 1T | 1.25 | Más | 2.72 | 0.310 | 0.338 | -0.156 |
| 1T | 1.25 | Menos | 1.44 | 0.701 | 0.673 | +0.009 |
| 1T | 1.5 | Más | 3.15 | 0.246 | 0.275 | -0.226 |
| 1T | 1.5 | Menos | 1.33 | 0.754 | 0.725 | +0.003 |
| 1T | 2.5 | Más | 7.3 | 0.069 | 0.082 | -0.499 |
| 1T | 2.5 | Menos | 1.07 | 0.931 | 0.918 | -0.003 |
| 2T | 0.5 | Más | 1.39 | 0.704 | 0.695 | -0.021 |
| 2T | 0.5 | Menos | 2.92 | 0.296 | 0.305 | -0.136 |
| 2T | 1.5 | Más | 2.72 | 0.335 | 0.334 | -0.088 |
| 2T | 1.5 | Menos | 1.45 | 0.665 | 0.666 | -0.036 |
| 2T | 2.5 | Más | 6.2 | 0.122 | 0.116 | -0.242 |
| 2T | 2.5 | Menos | 1.11 | 0.878 | 0.884 | -0.026 |

Comprobación: Betano trae 23 líneas de goles; la ficha trae 23 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 2.67 / 3.05 / 2.87; margen 5.1%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Moldavia | 2.67 | 0.365 | 0.358 | 0.356 | +0.7 |
| Empate | 3.05 | 0.290 | 0.311 | 0.312 | -2.1 |
| Kazajistán | 2.87 | 0.345 | 0.331 | 0.332 | +1.4 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Moldavia: ganó 1 de 7, no perdió 3 de 7, marcó 4 de 7, dejó la portería a cero 0 de 7, ambos marcaron 4 de 7.
- Kazajistán: ganó 2 de 7, no perdió 5 de 7, marcó 7 de 7, dejó la portería a cero 2 de 7, ambos marcaron 5 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Moldavia | 2.67 | 0.363 | 0.360 | 0.357 | +0.5 | -0.031 |
| Empate | 3.05 | 0.289 | 0.312 | 0.311 | -2.2 | -0.117 |
| Gana Kazajistán | 2.87 | 0.347 | 0.329 | 0.332 | +1.6 | -0.003 |
| Moldavia o empate | 1.45 | 0.652 | 0.671 | 0.668 | -1.6 | -0.054 |
| Kazajistán o empate | 1.5 | 0.637 | 0.640 | 0.642 | -0.5 | -0.044 |
| No hay empate | 1.37 | 0.711 | 0.688 | 0.689 | +2.2 | -0.027 |
| 1.er tiempo: Moldavia | 3.25 | 0.252 | 0.270 | 0.269 | -1.7 | -0.180 |
| 1.er tiempo: Empate | 1.95 | 0.499 | 0.478 | 0.475 | +2.3 | -0.028 |
| 1.er tiempo: Kazajistán | 3.4 | 0.249 | 0.253 | 0.256 | -0.7 | -0.153 |
| 2.º tiempo: Moldavia | 3.05 | 0.301 | 0.297 | 0.295 | +0.7 | -0.081 |
| 2.º tiempo: Empate | 2.18 | 0.414 | 0.425 | 0.426 | -1.2 | -0.098 |
| 2.º tiempo: Kazajistán | 3.2 | 0.285 | 0.278 | 0.280 | +0.5 | -0.088 |
| Descanso o final: Moldavia | 2.07 | 0.440 | 0.441 | 0.452 | -1.2 | -0.090 |
| Descanso o final: Empate | 1.6 | 0.595 | 0.585 | 0.584 | +1.1 | -0.048 |
| Descanso o final: Kazajistán | 2.18 | 0.427 | 0.412 | 0.429 | -0.1 | -0.068 |
| Ambos marcan: Sí | 2.0 | 0.444 | 0.463 | 0.458 | -1.3 | -0.111 |
| Ambos marcan: No | 1.72 | 0.556 | 0.537 | 0.542 | +1.3 | -0.044 |
| Descanso/final: Moldavia / Moldavia | 4.25 | 0.190 | 0.202 | 0.203 | -1.4 | -0.194 |
| Descanso/final: Moldavia / Empate | 15.0 | 0.044 | 0.052 | 0.051 | -0.6 | -0.333 |
| Descanso/final: Moldavia / Kazajistán | 45.0 | 0.018 | 0.015 | 0.015 | +0.3 | -0.179 |
| Descanso/final: Empate / Moldavia | 6.1 | 0.156 | 0.140 | 0.137 | +1.9 | -0.049 |
| Descanso/final: Empate / Empate | 4.15 | 0.197 | 0.207 | 0.209 | -1.2 | -0.184 |
| Descanso/final: Empate / Kazajistán | 6.4 | 0.146 | 0.130 | 0.130 | +1.6 | -0.065 |
| Descanso/final: Kazajistán / Moldavia | 40.0 | 0.017 | 0.018 | 0.017 | +0.0 | -0.312 |
| Descanso/final: Kazajistán / Empate | 14.5 | 0.049 | 0.052 | 0.053 | -0.4 | -0.289 |
| Descanso/final: Kazajistán / Kazajistán | 4.6 | 0.183 | 0.183 | 0.186 | -0.3 | -0.158 |
| Hándicap Moldavia -3 | 32.0 | 0.007 | 0.009 | 0.010 | -0.3 | -0.784 |
| Hándicap empate (Moldavia -3) | 14.0 | 0.026 | 0.029 | 0.029 | -0.3 | -0.635 |
| Hándicap Kazajistán +3 | 1.03 | 0.967 | 0.962 | 0.961 | +0.6 | -0.004 |
| Hándicap Moldavia -2 | 16.0 | 0.034 | 0.040 | 0.042 | -0.8 | -0.452 |
| Hándicap empate (Moldavia -2) | 7.6 | 0.094 | 0.101 | 0.098 | -0.4 | -0.287 |
| Hándicap Kazajistán +2 | 1.14 | 0.872 | 0.859 | 0.861 | +1.1 | -0.006 |
| Hándicap Moldavia -1 | 6.2 | 0.128 | 0.140 | 0.139 | -1.1 | -0.209 |
| Hándicap empate (Moldavia -1) | 4.1 | 0.234 | 0.218 | 0.217 | +1.7 | -0.039 |
| Hándicap Kazajistán +1 | 1.5 | 0.638 | 0.641 | 0.644 | -0.6 | -0.043 |
| Hándicap Moldavia +1 | 1.45 | 0.652 | 0.671 | 0.669 | -1.6 | -0.054 |
| Hándicap empate (Moldavia +1) | 4.3 | 0.227 | 0.207 | 0.206 | +2.1 | -0.026 |
| Hándicap Kazajistán -1 | 6.8 | 0.121 | 0.121 | 0.125 | -0.5 | -0.178 |
| Hándicap Moldavia +2 | 1.12 | 0.880 | 0.880 | 0.877 | +0.3 | -0.014 |
| Hándicap empate (Moldavia +2) | 8.25 | 0.089 | 0.086 | 0.087 | +0.2 | -0.265 |
| Hándicap Kazajistán -2 | 17.5 | 0.031 | 0.035 | 0.036 | -0.6 | -0.463 |
| Hándicap Moldavia -0.5 | 2.55 | 0.363 | 0.360 | 0.359 | +0.5 | -0.073 |
| Hándicap Kazajistán +0.5 | 1.5 | 0.636 | 0.640 | 0.641 | -0.5 | -0.045 |
| Hándicap Moldavia -0.25 | 2.2 | 0.428 | 0.430 | 0.427 | +0.1 | -0.058 |
| Hándicap Kazajistán +0.25 | 1.65 | 0.581 | 0.580 | 0.582 | -0.2 | -0.042 |
| Hándicap Moldavia +0 | 1.82 | 0.522 | 0.531 | 0.528 | -0.6 | -0.050 |
| Hándicap Kazajistán -0 | 1.95 | 0.496 | 0.489 | 0.491 | +0.5 | -0.033 |
| Hándicap Moldavia +0.25 | 1.57 | 0.601 | 0.615 | 0.613 | -1.3 | -0.057 |
| Hándicap Kazajistán -0.25 | 2.35 | 0.408 | 0.394 | 0.396 | +1.2 | -0.040 |
| Hándicap Moldavia +0.5 | 1.44 | 0.652 | 0.671 | 0.669 | -1.6 | -0.060 |
| Hándicap Kazajistán -0.5 | 2.72 | 0.347 | 0.329 | 0.331 | +1.6 | -0.055 |

Diferencia máxima modelo − mercado en estas selecciones: 2.3 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
