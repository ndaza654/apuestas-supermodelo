# Goles y resultado · Andorra - Gibraltar · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas de Betano leídas 2026-11-12T17:32:30.373Z · 168 mercados (UTC; 17:32 UTC = 12:32 Bogotá). Todas las cifras salen de `fichas/ficha_andorra-gibraltar.json` (clave `goles`, `contexto`), `informes/andorra-gibraltar_resultado.json` y `betano/andorra-gibraltar.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (9 líneas), de Andorra (4), de Gibraltar (2), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 10 mercados de hándicap.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 25 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 32 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 36 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 52 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 4 líneas; especial: 2 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 2.1 pts (Descanso o final: Gibraltar). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 1.28 / 0.57 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 1.81 | 1.88 | 1.86 | 1.32 | 0.0–4.0 |
| local | 1.25 | 1.3 | 1.28 | 1.06 | 0.0–3.0 |
| visitante | 0.56 | 0.58 | 0.57 | 0.74 | 0.0–2.0 |
| 1T | 0.8 | 0.85 | 0.84 | 0.9 | 0.0–2.0 |
| 2T | 1.01 | 1.04 | 1.02 | 0.99 | 0.0–2.0 |

Esperado de la ficha (historial) vs media implícita de Betano: total 2.21 vs 1.86; Andorra 1.29 vs 1.28; Gibraltar 0.93 vs 0.57. Cuando difieren mucho, el colchón (basado en el historial) y las cuotas cuentan historias distintas.

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Andorra: motivación alta, necesita ganar True, rotación False. Gibraltar: motivación alta, necesita ganar True, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Andorra n = 7, Gibraltar n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Andorra 1.29 (a favor 0.57 · Gibraltar concede 2.0); Gibraltar 0.93 (a favor 0.29 · Andorra concede 1.57); total 2.21.
- Series (a favor–en contra): Andorra 0-1 0-0 1-2 0-1 1-3 2-2 0-2; Gibraltar 1-1 0-0 0-1 0-1 0-6 1-2 0-3; directos (total) 0.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.16 | 2.21 | +1.71 | 6 de 7 | 6 de 7 | 0 de 1 | SÍ | no | 0.845 | 0.841 | -0.020 |
| 0.5 | Menos | 4.85 | 2.21 | -1.71 | 1 de 7 | 1 de 7 | 1 de 1 | no | sí | 0.155 | 0.159 | -0.246 |
| 1.25 | Más | 1.5 | 2.21 | +0.96 | 4 de 7 | 4 de 7 | 0 de 1 | no | sí | 0.631 | 0.646 | -0.054 |
| 1.25 | Menos | 2.57 | 2.21 | -0.96 | 1 de 7 | 1 de 7 | 1 de 1 | no | sí | 0.378 | 0.362 | -0.029 |
| 1.5 | Más | 1.7 | 2.21 | +0.71 | 4 de 7 | 4 de 7 | 0 de 1 | no | sí | 0.527 | 0.554 | -0.104 |
| 1.5 | Menos | 2.07 | 2.21 | -0.71 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.473 | 0.446 | -0.021 |
| 1.75 | Más | 1.93 | 2.21 | +0.46 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.466 | 0.490 | -0.102 |
| 1.75 | Menos | 1.83 | 2.21 | -0.46 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.543 | 0.519 | -0.007 |
| 2 | Más | 2.35 | 2.21 | +0.21 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.380 | 0.400 | -0.106 |
| 2 | Menos | 1.57 | 2.21 | -0.21 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.636 | 0.617 | -0.002 |
| 2.25 | Más | 2.75 | 2.21 | -0.04 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.318 | 0.334 | -0.126 |
| 2.25 | Menos | 1.44 | 2.21 | +0.04 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.690 | 0.674 | -0.007 |
| 2.5 | Más | 3.05 | 2.21 | -0.29 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.272 | 0.286 | -0.172 |
| 2.5 | Menos | 1.35 | 2.21 | +0.29 | 4 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.728 | 0.714 | -0.017 |
| 3.5 | Más | 5.9 | 2.21 | -1.29 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.104 | 0.118 | -0.386 |
| 3.5 | Menos | 1.11 | 2.21 | +1.29 | 5 de 7 | 6 de 7 | 1 de 1 | SÍ | no | 0.896 | 0.882 | -0.005 |
| 4.5 | Más | 10.0 | 2.21 | -2.29 | 0 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.033 | 0.040 | -0.666 |
| 4.5 | Menos | 1.03 | 2.21 | +2.29 | 7 de 7 | 6 de 7 | 1 de 1 | SÍ | no | 0.967 | 0.960 | -0.004 |

### Goles · Andorra (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.33 | 1.29 | +0.79 | 3 de 7 | 6 de 7 | 0 de 1* | no | sí | 0.725 | 0.725 | -0.035 |
| 0.5 | Menos | 3.15 | 1.29 | -0.79 | 4 de 7 | 1 de 7 | 1 de 1* | no | sí | 0.275 | 0.275 | -0.135 |
| 1.5 | Más | 2.45 | 1.29 | -0.21 | 1 de 7 | 3 de 7 | 0 de 1* | no | sí | 0.352 | 0.366 | -0.138 |
| 1.5 | Menos | 1.5 | 1.29 | +0.21 | 6 de 7 | 4 de 7 | 1 de 1* | no | sí | 0.648 | 0.634 | -0.028 |
| 2.5 | Más | 5.3 | 1.29 | -1.21 | 0 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.121 | 0.136 | -0.359 |
| 2.5 | Menos | 1.13 | 1.29 | +1.21 | 7 de 7 | 5 de 7 | 1 de 1* | SÍ | no | 0.879 | 0.864 | -0.007 |
| 3.5 | Más | 10.0 | 1.29 | -2.21 | 0 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.030 | 0.040 | -0.695 |
| 3.5 | Menos | 1.03 | 1.29 | +2.21 | 7 de 7 | 6 de 7 | 1 de 1* | SÍ | no | 0.970 | 0.960 | -0.001 |

### Goles · Gibraltar (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 2.1 | 0.93 | +0.43 | 6 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.428 | 0.436 | -0.101 |
| 0.5 | Menos | 1.67 | 0.93 | -0.43 | 1 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.572 | 0.564 | -0.045 |
| 1.5 | Más | 6.1 | 0.93 | -0.57 | 4 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.103 | 0.110 | -0.369 |
| 1.5 | Menos | 1.1 | 0.93 | +0.57 | 3 de 7 | 7 de 7 | 1 de 1* | no | no | 0.897 | 0.890 | -0.014 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.67 | 0.548 | 0.566 | -0.085 |
| 1T | 0.5 | Menos | 2.12 | 0.452 | 0.434 | -0.041 |
| 1T | 0.75 | Más | 1.98 | 0.460 | 0.480 | -0.089 |
| 1T | 0.75 | Menos | 1.8 | 0.551 | 0.531 | -0.009 |
| 1T | 1 | Más | 2.8 | 0.316 | 0.334 | -0.115 |
| 1T | 1 | Menos | 1.42 | 0.706 | 0.688 | +0.002 |
| 1T | 1.25 | Más | 3.45 | 0.241 | 0.259 | -0.169 |
| 1T | 1.25 | Menos | 1.3 | 0.770 | 0.751 | +0.001 |
| 1T | 1.5 | Más | 3.95 | 0.188 | 0.205 | -0.259 |
| 1T | 1.5 | Menos | 1.22 | 0.812 | 0.795 | -0.009 |
| 1T | 2.5 | Más | 9.0 | 0.046 | 0.052 | -0.582 |
| 1T | 2.5 | Menos | 1.04 | 0.954 | 0.948 | -0.008 |
| 2T | 0.5 | Más | 1.5 | 0.637 | 0.641 | -0.044 |
| 2T | 0.5 | Menos | 2.55 | 0.363 | 0.359 | -0.075 |
| 2T | 1.5 | Más | 3.25 | 0.261 | 0.271 | -0.152 |
| 2T | 1.5 | Menos | 1.33 | 0.739 | 0.729 | -0.017 |
| 2T | 2.5 | Más | 7.7 | 0.080 | 0.088 | -0.385 |
| 2T | 2.5 | Menos | 1.08 | 0.920 | 0.912 | -0.006 |

Comprobación: Betano trae 24 líneas de goles; la ficha trae 24 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 1.78 / 3.1 / 5.4; margen 7.0%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Andorra | 1.78 | 0.553 | 0.539 | 0.525 | +1.4 |
| Empate | 3.1 | 0.286 | 0.297 | 0.302 | -1.1 |
| Gibraltar | 5.4 | 0.161 | 0.164 | 0.173 | -0.3 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Andorra: ganó 0 de 7, no perdió 2 de 7, marcó 3 de 7, dejó la portería a cero 1 de 7, ambos marcaron 3 de 7.
- Gibraltar: ganó 0 de 7, no perdió 2 de 7, marcó 2 de 7, dejó la portería a cero 1 de 7, ambos marcaron 2 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Andorra | 1.78 | 0.549 | 0.543 | 0.539 | +1.1 | -0.022 |
| Empate | 3.1 | 0.285 | 0.298 | 0.297 | -1.2 | -0.117 |
| Gana Gibraltar | 5.4 | 0.166 | 0.159 | 0.164 | +0.2 | -0.105 |
| Andorra o empate | 1.17 | 0.834 | 0.841 | 0.836 | -0.2 | -0.024 |
| Gibraltar o empate | 2.07 | 0.451 | 0.457 | 0.461 | -1.1 | -0.067 |
| No hay empate | 1.34 | 0.715 | 0.702 | 0.703 | +1.2 | -0.042 |
| 1.er tiempo: Andorra | 2.47 | 0.357 | 0.366 | 0.363 | -0.7 | -0.119 |
| 1.er tiempo: Empate | 1.85 | 0.517 | 0.502 | 0.502 | +1.5 | -0.044 |
| 1.er tiempo: Gibraltar | 6.0 | 0.127 | 0.131 | 0.135 | -0.8 | -0.240 |
| 2.º tiempo: Andorra | 2.27 | 0.398 | 0.407 | 0.404 | -0.6 | -0.097 |
| 2.º tiempo: Empate | 2.07 | 0.452 | 0.444 | 0.447 | +0.5 | -0.064 |
| 2.º tiempo: Gibraltar | 5.6 | 0.150 | 0.149 | 0.149 | +0.1 | -0.161 |
| Descanso o final: Andorra | 1.6 | 0.593 | 0.589 | 0.584 | +0.9 | -0.052 |
| Descanso o final: Empate | 1.6 | 0.588 | 0.582 | 0.584 | +0.4 | -0.059 |
| Descanso o final: Gibraltar | 3.75 | 0.229 | 0.228 | 0.249 | -2.1 | -0.143 |
| Ambos marcan: Sí | 2.72 | 0.308 | 0.327 | 0.319 | -1.1 | -0.162 |
| Ambos marcan: No | 1.4 | 0.692 | 0.673 | 0.681 | +1.1 | -0.031 |
| Descanso/final: Andorra / Andorra | 2.8 | 0.313 | 0.320 | 0.318 | -0.5 | -0.122 |
| Descanso/final: Andorra / Empate | 19.0 | 0.036 | 0.039 | 0.038 | -0.1 | -0.312 |
| Descanso/final: Andorra / Gibraltar | 100.0 | 0.006 | 0.006 | 0.006 | +0.0 | -0.381 |
| Descanso/final: Empate / Andorra | 4.15 | 0.221 | 0.207 | 0.205 | +1.6 | -0.083 |
| Descanso/final: Empate / Empate | 3.8 | 0.219 | 0.224 | 0.226 | -0.7 | -0.168 |
| Descanso/final: Empate / Gibraltar | 10.5 | 0.078 | 0.072 | 0.073 | +0.5 | -0.182 |
| Descanso/final: Gibraltar / Andorra | 45.0 | 0.015 | 0.015 | 0.014 | +0.0 | -0.349 |
| Descanso/final: Gibraltar / Empate | 20.0 | 0.031 | 0.036 | 0.036 | -0.5 | -0.384 |
| Descanso/final: Gibraltar / Gibraltar | 9.25 | 0.081 | 0.080 | 0.084 | -0.3 | -0.250 |
| Hándicap Andorra -3 | 21.0 | 0.020 | 0.025 | 0.026 | -0.6 | -0.577 |
| Hándicap empate (Andorra -3) | 10.0 | 0.056 | 0.063 | 0.063 | -0.7 | -0.443 |
| Hándicap Gibraltar +3 | 1.08 | 0.924 | 0.913 | 0.912 | +1.3 | -0.002 |
| Hándicap Andorra -2 | 8.75 | 0.078 | 0.089 | 0.093 | -1.5 | -0.318 |
| Hándicap empate (Andorra -2) | 5.2 | 0.159 | 0.165 | 0.164 | -0.4 | -0.171 |
| Hándicap Gibraltar +2 | 1.31 | 0.763 | 0.745 | 0.744 | +1.9 | -0.001 |
| Hándicap Andorra -1 | 3.6 | 0.237 | 0.254 | 0.255 | -1.8 | -0.148 |
| Hándicap empate (Andorra -1) | 3.25 | 0.313 | 0.289 | 0.284 | +2.9 | +0.018 |
| Hándicap Gibraltar +1 | 2.07 | 0.450 | 0.457 | 0.460 | -1.0 | -0.068 |
| Hándicap Andorra +1 | 1.17 | 0.835 | 0.842 | 0.837 | -0.2 | -0.023 |
| Hándicap empate (Andorra +1) | 6.3 | 0.133 | 0.123 | 0.125 | +0.8 | -0.162 |
| Hándicap Gibraltar -1 | 18.0 | 0.032 | 0.035 | 0.038 | -0.6 | -0.422 |
| Hándicap Andorra +2 | 1.03 | 0.968 | 0.965 | 0.962 | +0.6 | -0.003 |
| Hándicap empate (Andorra +2) | 13.5 | 0.027 | 0.029 | 0.032 | -0.5 | -0.637 |
| Hándicap Gibraltar -2 | 45.0 | 0.005 | 0.006 | 0.006 | -0.1 | -0.759 |
| Hándicap Andorra -1.25 | 3.0 | 0.288 | 0.301 | 0.301 | -1.3 | -0.136 |
| Hándicap Gibraltar +1.25 | 1.37 | 0.722 | 0.708 | 0.709 | +1.3 | -0.011 |
| Hándicap Andorra -0.75 | 2.05 | 0.467 | 0.466 | 0.462 | +0.6 | -0.043 |
| Hándicap Gibraltar +0.75 | 1.75 | 0.542 | 0.542 | 0.547 | -0.5 | -0.051 |
| Hándicap Andorra -0.5 | 1.75 | 0.552 | 0.545 | 0.543 | +0.9 | -0.035 |
| Hándicap Gibraltar +0.5 | 2.05 | 0.448 | 0.455 | 0.457 | -0.9 | -0.081 |
| Hándicap Andorra -0.25 | 1.52 | 0.643 | 0.641 | 0.636 | +0.7 | -0.022 |
| Hándicap Gibraltar +0.25 | 2.5 | 0.365 | 0.368 | 0.372 | -0.7 | -0.087 |

Diferencia máxima modelo − mercado en estas selecciones: 2.9 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
