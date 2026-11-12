# Goles y resultado · Liechtenstein - Azerbaiyán · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas Betano leídas el Cuotas de Betano leídas 2026-11-12T17:32:31.482Z · 114 mercados. Todas las cifras salen de `fichas/ficha_liechtenstein-azerbaiyan.json` (clave `goles`, `contexto`), `informes/liechtenstein-azerbaiyan_resultado.json` y `betano/liechtenstein-azerbaiyan.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (9 líneas), de Liechtenstein (2), de Azerbaiyán (5), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 8 mercados de hándicap. Ambos marcan 1T/2T y total exacto no aparecen.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 34 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 38 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 53 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 6 líneas; especial: 2 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 2.6 pts (Descanso o final: Liechtenstein). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 0.41 / 2.01 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.36 | 2.44 | 2.42 | 1.5 | 1.0–4.0 |
| local | 0.42 | 0.41 | 0.41 | 0.64 | 0.0–1.0 |
| visitante | 1.95 | 2.03 | 2.0 | 1.34 | 0.0–4.0 |
| 1T | 1.08 | 1.14 | 1.06 | 1.03 | 0.0–2.0 |
| 2T | 1.28 | 1.31 | 1.37 | 1.12 | 0.0–3.0 |

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Liechtenstein: motivación normal, necesita ganar True, rotación False. Azerbaiyán: motivación alta, necesita ganar False, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Liechtenstein n = 7, Azerbaiyán n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Liechtenstein 0.71 (a favor 0.29 · Azerbaiyán concede 1.14); Azerbaiyán 2.07 (a favor 1.57 · Liechtenstein concede 2.57); total 2.79.
- Series (a favor–en contra): Liechtenstein 0-0 0-2 1-4 1-0 0-7 0-1 0-4; Azerbaiyán 1-0 0-0 1-1 2-1 6-1 1-3 0-2; directos (total) 0.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.08 | 2.79 | +2.29 | 6 de 7 | 6 de 7 | 0 de 1 | SÍ | no | 0.908 | 0.908 | -0.020 |
| 0.5 | Menos | 6.7 | 2.79 | -2.29 | 1 de 7 | 1 de 7 | 1 de 1 | no | sí | 0.092 | 0.092 | -0.382 |
| 1.5 | Más | 1.37 | 2.79 | +1.29 | 4 de 7 | 5 de 7 | 0 de 1 | no | sí | 0.686 | 0.698 | -0.061 |
| 1.5 | Menos | 2.85 | 2.79 | -1.29 | 3 de 7 | 2 de 7 | 1 de 1 | no | sí | 0.314 | 0.302 | -0.104 |
| 1.75 | Más | 1.47 | 2.79 | +1.04 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.642 | 0.655 | -0.056 |
| 1.75 | Menos | 2.57 | 2.79 | -1.04 | 3 de 7 | 2 de 7 | 1 de 1 | no | sí | 0.367 | 0.354 | -0.056 |
| 2 | Más | 1.62 | 2.79 | +0.79 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.581 | 0.594 | -0.059 |
| 2 | Menos | 2.22 | 2.79 | -0.79 | 3 de 7 | 2 de 7 | 1 de 1 | no | sí | 0.437 | 0.423 | -0.029 |
| 2.25 | Más | 1.87 | 2.79 | +0.54 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.487 | 0.505 | -0.089 |
| 2.25 | Menos | 1.87 | 2.79 | -0.54 | 3 de 7 | 2 de 7 | 1 de 1 | no | sí | 0.522 | 0.505 | -0.024 |
| 2.5 | Más | 2.07 | 2.79 | +0.29 | 3 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.418 | 0.440 | -0.135 |
| 2.5 | Menos | 1.67 | 2.79 | -0.29 | 4 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.582 | 0.560 | -0.028 |
| 2.75 | Más | 2.45 | 2.79 | +0.04 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.355 | 0.375 | -0.130 |
| 2.75 | Menos | 1.52 | 2.79 | -0.04 | 4 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.652 | 0.632 | -0.009 |
| 3.5 | Más | 3.6 | 2.79 | -0.71 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.207 | 0.223 | -0.256 |
| 3.5 | Menos | 1.24 | 2.79 | +0.71 | 4 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.793 | 0.777 | -0.016 |
| 4.5 | Más | 6.3 | 2.79 | -1.71 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.087 | 0.094 | -0.449 |
| 4.5 | Menos | 1.08 | 2.79 | +1.71 | 5 de 7 | 6 de 7 | 1 de 1 | SÍ | no | 0.913 | 0.906 | -0.014 |

### Goles · Liechtenstein (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 2.65 | 0.71 | +0.21 | 2 de 7 | 5 de 7 | 0 de 1* | no | sí | 0.343 | 0.338 | -0.091 |
| 0.5 | Menos | 1.45 | 0.71 | -0.21 | 5 de 7 | 2 de 7 | 1 de 1* | no | sí | 0.657 | 0.662 | -0.047 |
| 1.5 | Más | 8.25 | 0.71 | -0.79 | 0 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.064 | 0.062 | -0.471 |
| 1.5 | Menos | 1.05 | 0.71 | +0.79 | 7 de 7 | 5 de 7 | 1 de 1* | SÍ | no | 0.936 | 0.938 | -0.017 |

### Goles · Azerbaiyán (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.13 | 2.07 | +1.57 | 5 de 7 | 5 de 7 | 0 de 1* | SÍ | no | 0.862 | 0.865 | -0.026 |
| 0.5 | Menos | 5.4 | 2.07 | -1.57 | 2 de 7 | 2 de 7 | 1 de 1* | no | sí | 0.138 | 0.135 | -0.254 |
| 1.5 | Más | 1.6 | 2.07 | +0.57 | 4 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.583 | 0.594 | -0.067 |
| 1.5 | Menos | 2.25 | 2.07 | -0.57 | 3 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.417 | 0.406 | -0.062 |
| 2.5 | Más | 2.75 | 2.07 | -0.43 | 3 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.298 | 0.324 | -0.180 |
| 2.5 | Menos | 1.42 | 2.07 | +0.43 | 4 de 7 | 6 de 7 | 1 de 1* | no | sí | 0.702 | 0.676 | -0.004 |
| 3.5 | Más | 5.2 | 2.07 | -1.43 | 3 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.127 | 0.143 | -0.342 |
| 3.5 | Menos | 1.14 | 2.07 | +1.43 | 4 de 7 | 6 de 7 | 1 de 1* | no | no | 0.873 | 0.857 | -0.004 |
| 4.5 | Más | 9.0 | 2.07 | -2.43 | 1 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.043 | 0.052 | -0.613 |
| 4.5 | Menos | 1.04 | 2.07 | +2.43 | 6 de 7 | 6 de 7 | 1 de 1* | SÍ | no | 0.957 | 0.948 | -0.005 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.45 | 0.650 | 0.655 | -0.058 |
| 1T | 0.5 | Menos | 2.55 | 0.350 | 0.345 | -0.107 |
| 1T | 0.75 | Más | 1.65 | 0.576 | 0.579 | -0.050 |
| 1T | 0.75 | Menos | 2.15 | 0.438 | 0.434 | -0.059 |
| 1T | 1 | Más | 2.05 | 0.461 | 0.465 | -0.055 |
| 1T | 1 | Menos | 1.72 | 0.565 | 0.561 | -0.029 |
| 1T | 1.25 | Más | 2.57 | 0.353 | 0.357 | -0.093 |
| 1T | 1.25 | Menos | 1.47 | 0.660 | 0.656 | -0.030 |
| 1T | 1.5 | Más | 3.0 | 0.281 | 0.284 | -0.156 |
| 1T | 1.5 | Menos | 1.34 | 0.719 | 0.716 | -0.037 |
| 1T | 2.5 | Más | 6.6 | 0.086 | 0.092 | -0.431 |
| 1T | 2.5 | Menos | 1.08 | 0.914 | 0.907 | -0.013 |
| 2T | 0.5 | Más | 1.29 | 0.735 | 0.746 | -0.052 |
| 2T | 0.5 | Menos | 3.3 | 0.265 | 0.254 | -0.126 |
| 2T | 1.5 | Más | 2.27 | 0.376 | 0.398 | -0.146 |
| 2T | 1.5 | Menos | 1.57 | 0.624 | 0.602 | -0.020 |
| 2T | 2.5 | Más | 4.65 | 0.143 | 0.156 | -0.335 |
| 2T | 2.5 | Menos | 1.15 | 0.857 | 0.844 | -0.014 |

Comprobación: Betano trae 25 líneas de goles; la ficha trae 25 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 11.75 / 4.75 / 1.29; margen 7.1%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Liechtenstein | 11.75 | 0.060 | 0.066 | 0.079 | -0.6 |
| Empate | 4.75 | 0.180 | 0.179 | 0.197 | +0.1 |
| Azerbaiyán | 1.29 | 0.760 | 0.755 | 0.724 | +0.5 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Liechtenstein: ganó 1 de 7, no perdió 2 de 7, marcó 2 de 7, dejó la portería a cero 2 de 7, ambos marcaron 1 de 7.
- Azerbaiyán: ganó 3 de 7, no perdió 5 de 7, marcó 5 de 7, dejó la portería a cero 2 de 7, ambos marcaron 4 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Liechtenstein | 11.75 | 0.067 | 0.059 | 0.066 | +0.1 | -0.212 |
| Empate | 4.75 | 0.181 | 0.178 | 0.179 | +0.2 | -0.140 |
| Gana Azerbaiyán | 1.29 | 0.752 | 0.763 | 0.755 | -0.3 | -0.030 |
| Liechtenstein o empate | 3.65 | 0.248 | 0.237 | 0.245 | +0.3 | -0.095 |
| Azerbaiyán o empate | 1.05 | 0.933 | 0.942 | 0.934 | -0.1 | -0.020 |
| No hay empate | 1.16 | 0.819 | 0.822 | 0.821 | -0.2 | -0.050 |
| 1.er tiempo: Liechtenstein | 10.0 | 0.068 | 0.066 | 0.074 | -0.6 | -0.324 |
| 1.er tiempo: Empate | 2.22 | 0.413 | 0.389 | 0.406 | +0.8 | -0.083 |
| 1.er tiempo: Azerbaiyán | 1.78 | 0.519 | 0.544 | 0.521 | -0.1 | -0.076 |
| 2.º tiempo: Liechtenstein | 10.0 | 0.083 | 0.076 | 0.075 | +0.9 | -0.167 |
| 2.º tiempo: Empate | 2.72 | 0.336 | 0.336 | 0.324 | +1.2 | -0.086 |
| 2.º tiempo: Azerbaiyán | 1.57 | 0.581 | 0.588 | 0.602 | -2.1 | -0.088 |
| Descanso o final: Liechtenstein | 6.7 | 0.120 | 0.114 | 0.140 | -1.9 | -0.194 |
| Descanso o final: Empate | 1.98 | 0.470 | 0.447 | 0.472 | -0.2 | -0.069 |
| Descanso o final: Azerbaiyán | 1.23 | 0.771 | 0.781 | 0.760 | +1.1 | -0.052 |
| Ambos marcan: Sí | 2.92 | 0.295 | 0.298 | 0.292 | +0.4 | -0.138 |
| Ambos marcan: No | 1.35 | 0.705 | 0.702 | 0.708 | -0.4 | -0.049 |
| Descanso/final: Liechtenstein / Liechtenstein | 19.5 | 0.030 | 0.027 | 0.032 | -0.2 | -0.414 |
| Descanso/final: Liechtenstein / Empate | 25.0 | 0.021 | 0.022 | 0.024 | -0.3 | -0.487 |
| Descanso/final: Liechtenstein / Azerbaiyán | 30.0 | 0.017 | 0.018 | 0.019 | -0.2 | -0.479 |
| Descanso/final: Empate / Liechtenstein | 20.0 | 0.034 | 0.028 | 0.031 | +0.3 | -0.327 |
| Descanso/final: Empate / Empate | 5.7 | 0.134 | 0.131 | 0.132 | +0.2 | -0.238 |
| Descanso/final: Empate / Azerbaiyán | 3.4 | 0.245 | 0.230 | 0.241 | +0.4 | -0.168 |
| Descanso/final: Azerbaiyán / Liechtenstein | 150.0 | 0.005 | 0.003 | 0.003 | +0.2 | -0.250 |
| Descanso/final: Azerbaiyán / Empate | 25.0 | 0.027 | 0.026 | 0.024 | +0.3 | -0.327 |
| Descanso/final: Azerbaiyán / Azerbaiyán | 1.83 | 0.490 | 0.516 | 0.495 | -0.5 | -0.103 |
| Hándicap Liechtenstein +1 | 3.65 | 0.247 | 0.236 | 0.243 | +0.4 | -0.097 |
| Hándicap empate (Liechtenstein +1) | 3.4 | 0.279 | 0.267 | 0.263 | +1.6 | -0.053 |
| Hándicap Azerbaiyán -1 | 1.91 | 0.474 | 0.498 | 0.493 | -1.9 | -0.094 |
| Hándicap Liechtenstein +2 | 1.85 | 0.528 | 0.505 | 0.511 | +1.7 | -0.023 |
| Hándicap empate (Liechtenstein +2) | 3.8 | 0.242 | 0.239 | 0.233 | +0.8 | -0.081 |
| Hándicap Azerbaiyán -2 | 3.5 | 0.230 | 0.256 | 0.255 | -2.5 | -0.195 |
| Hándicap Liechtenstein +3 | 1.3 | 0.770 | 0.744 | 0.744 | +2.6 | +0.001 |
| Hándicap empate (Liechtenstein +3) | 5.5 | 0.137 | 0.151 | 0.146 | -0.9 | -0.246 |
| Hándicap Azerbaiyán -3 | 7.1 | 0.093 | 0.105 | 0.110 | -1.6 | -0.338 |
| Hándicap Liechtenstein +1.25 | 2.12 | 0.453 | 0.433 | 0.439 | +1.4 | -0.039 |
| Hándicap Azerbaiyán -1.25 | 1.67 | 0.557 | 0.577 | 0.570 | -1.4 | -0.070 |
| Hándicap Liechtenstein +1.5 | 1.85 | 0.526 | 0.503 | 0.507 | +1.9 | -0.026 |
| Hándicap Azerbaiyán -1.5 | 1.9 | 0.474 | 0.497 | 0.493 | -1.9 | -0.100 |
| Hándicap Liechtenstein +1.75 | 1.65 | 0.599 | 0.575 | 0.577 | +2.2 | -0.012 |
| Hándicap Azerbaiyán -1.75 | 2.15 | 0.410 | 0.434 | 0.432 | -2.2 | -0.119 |

Diferencia máxima modelo − mercado en estas selecciones: 2.6 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
