# Goles y resultado · Serbia - Alemania · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas Betano leídas el Cuotas de Betano leídas 2026-11-12T17:32:20.227Z · 601 mercados. Todas las cifras salen de `fichas/ficha_serbia-alemania.json` (clave `goles`, `contexto`), `informes/serbia-alemania_resultado.json` y `betano/serbia-alemania.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (11 líneas), de Serbia (3), de Alemania (6), 1T (8) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 12 mercados de hándicap. Ambos marcan 1T/2T y total exacto no aparecen.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 2 líneas; saques_banda: 2 líneas; tarjetas: 2 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 3.0 pts (Descanso o final: Serbia). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 0.85 / 2.65 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 3.46 | 3.5 | 3.51 | 1.82 | 1.0–6.0 |
| local | 0.84 | 0.86 | 0.86 | 0.91 | 0.0–2.0 |
| visitante | 2.62 | 2.65 | 2.64 | 1.51 | 1.0–5.0 |
| 1T | 1.58 | 1.61 | 1.56 | 1.25 | 0.0–3.0 |
| 2T | 1.88 | 1.89 | 1.97 | 1.35 | 0.0–4.0 |

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Serbia: motivación alta, necesita ganar True, rotación False. Alemania: motivación alta, necesita ganar True, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Serbia n = 7, Alemania n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Serbia 1.07 (a favor 1.14 · Alemania concede 1.0); Alemania 1.36 (a favor 1.0 · Serbia concede 1.71); total 2.43.
- Series (a favor–en contra): Serbia 1-2 0-2 1-2 1-2 2-1 0-2 3-1; Alemania 0-0 2-0 0-1 1-1 1-2 1-2 2-1; directos (total) 2.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.5 | Más | 1.14 | 2.43 | +0.93 | 7 de 7 | 5 de 7 | 1 de 1 | SÍ | no | 0.862 | 0.863 | -0.018 |
| 1.5 | Menos | 5.9 | 2.43 | -0.93 | 0 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.138 | 0.137 | -0.184 |
| 2.5 | Más | 1.42 | 2.43 | -0.07 | 5 de 7 | 3 de 7 | 0 de 1 | no | sí | 0.676 | 0.683 | -0.040 |
| 2.5 | Menos | 2.87 | 2.43 | +0.07 | 2 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.324 | 0.317 | -0.071 |
| 2.75 | Más | 1.52 | 2.43 | -0.32 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.637 | 0.643 | -0.032 |
| 2.75 | Menos | 2.62 | 2.43 | +0.32 | 2 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.368 | 0.362 | -0.037 |
| 3 | Más | 1.65 | 2.43 | -0.57 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.586 | 0.593 | -0.032 |
| 3 | Menos | 2.32 | 2.43 | +0.57 | 2 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.422 | 0.415 | -0.021 |
| 3.25 | Más | 1.85 | 2.43 | -0.82 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.513 | 0.523 | -0.051 |
| 3.25 | Menos | 2.0 | 2.43 | +0.82 | 2 de 7 | 4 de 7 | 1 de 1 | no | sí | 0.492 | 0.482 | -0.017 |
| 3.5 | Más | 2.05 | 2.43 | -1.07 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.452 | 0.462 | -0.074 |
| 3.5 | Menos | 1.78 | 2.43 | +1.07 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | sí | 0.548 | 0.538 | -0.024 |
| 3.75 | Más | 2.32 | 2.43 | -1.32 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.401 | 0.413 | -0.070 |
| 3.75 | Menos | 1.65 | 2.43 | +1.32 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | sí | 0.602 | 0.591 | -0.006 |
| 4 | Más | 2.75 | 2.43 | -1.57 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.334 | 0.343 | -0.082 |
| 4 | Menos | 1.47 | 2.43 | +1.57 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | sí | 0.674 | 0.665 | -0.009 |
| 4.5 | Más | 3.25 | 2.43 | -2.07 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.267 | 0.275 | -0.134 |
| 4.5 | Menos | 1.34 | 2.43 | +2.07 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | sí | 0.734 | 0.725 | -0.017 |
| 5.5 | Más | 5.6 | 2.43 | -3.07 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.135 | 0.145 | -0.245 |
| 5.5 | Menos | 1.15 | 2.43 | +3.07 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.865 | 0.855 | -0.005 |
| 6.5 | Más | 9.75 | 2.43 | -4.07 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.059 | 0.067 | -0.428 |
| 6.5 | Menos | 1.06 | 2.43 | +4.07 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.941 | 0.933 | -0.002 |

### Goles · Serbia (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.65 | 1.07 | +0.57 | 5 de 7 | 5 de 7 | 0 de 1* | SÍ | sí | 0.569 | 0.573 | -0.062 |
| 0.5 | Menos | 2.15 | 1.07 | -0.57 | 2 de 7 | 2 de 7 | 1 de 1* | no | sí | 0.431 | 0.427 | -0.073 |
| 1.5 | Más | 3.85 | 1.07 | -0.43 | 2 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.208 | 0.212 | -0.198 |
| 1.5 | Menos | 1.23 | 1.07 | +0.43 | 5 de 7 | 5 de 7 | 1 de 1* | SÍ | sí | 0.792 | 0.788 | -0.026 |
| 2.5 | Más | 8.75 | 1.07 | -1.43 | 1 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.056 | 0.061 | -0.509 |
| 2.5 | Menos | 1.05 | 1.07 | +1.43 | 6 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.944 | 0.939 | -0.009 |

### Goles · Alemania (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.05 | 1.36 | +0.86 | 7 de 7 | 5 de 7 | 1 de 1* | SÍ | no | 0.942 | 0.938 | -0.011 |
| 0.5 | Menos | 8.25 | 1.36 | -0.86 | 0 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.058 | 0.062 | -0.522 |
| 1.5 | Más | 1.3 | 1.36 | -0.14 | 5 de 7 | 2 de 7 | 1 de 1* | no | sí | 0.751 | 0.744 | -0.024 |
| 1.5 | Menos | 3.35 | 1.36 | +0.14 | 2 de 7 | 5 de 7 | 0 de 1* | no | sí | 0.249 | 0.256 | -0.165 |
| 2.5 | Más | 1.9 | 1.36 | -1.14 | 0 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.490 | 0.493 | -0.069 |
| 2.5 | Menos | 1.85 | 1.36 | +1.14 | 7 de 7 | 7 de 7 | 1 de 1* | SÍ | sí | 0.510 | 0.507 | -0.057 |
| 3.5 | Más | 3.2 | 1.36 | -2.14 | 0 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.257 | 0.269 | -0.177 |
| 3.5 | Menos | 1.32 | 1.36 | +2.14 | 7 de 7 | 7 de 7 | 1 de 1* | SÍ | sí | 0.743 | 0.731 | -0.020 |
| 4.5 | Más | 5.7 | 1.36 | -3.14 | 0 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.115 | 0.126 | -0.347 |
| 4.5 | Menos | 1.12 | 1.36 | +3.14 | 7 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.885 | 0.874 | -0.008 |
| 5.5 | Más | 9.25 | 1.36 | -4.14 | 0 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.043 | 0.051 | -0.604 |
| 5.5 | Menos | 1.04 | 1.36 | +4.14 | 7 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.957 | 0.949 | -0.005 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.24 | 0.790 | 0.787 | -0.020 |
| 1T | 0.5 | Menos | 4.0 | 0.210 | 0.213 | -0.161 |
| 1T | 1 | Más | 1.42 | 0.693 | 0.691 | -0.016 |
| 1T | 1 | Menos | 2.9 | 0.323 | 0.325 | -0.064 |
| 1T | 1.25 | Más | 1.75 | 0.555 | 0.552 | -0.029 |
| 1T | 1.25 | Menos | 2.1 | 0.453 | 0.455 | -0.050 |
| 1T | 1.5 | Más | 2.02 | 0.465 | 0.466 | -0.061 |
| 1T | 1.5 | Menos | 1.78 | 0.535 | 0.534 | -0.047 |
| 1T | 1.75 | Más | 2.42 | 0.388 | 0.389 | -0.060 |
| 1T | 1.75 | Menos | 1.57 | 0.618 | 0.618 | -0.029 |
| 1T | 2 | Más | 3.25 | 0.285 | 0.286 | -0.073 |
| 1T | 2 | Menos | 1.35 | 0.727 | 0.727 | -0.018 |
| 1T | 2.5 | Más | 4.1 | 0.206 | 0.207 | -0.156 |
| 1T | 2.5 | Menos | 1.23 | 0.794 | 0.793 | -0.023 |
| 1T | 3.5 | Más | 8.5 | 0.071 | 0.070 | -0.400 |
| 1T | 3.5 | Menos | 1.06 | 0.929 | 0.930 | -0.015 |
| 2T | 0.5 | Más | 1.14 | 0.858 | 0.860 | -0.021 |
| 2T | 0.5 | Menos | 5.5 | 0.142 | 0.140 | -0.221 |
| 2T | 1.5 | Más | 1.62 | 0.575 | 0.589 | -0.068 |
| 2T | 1.5 | Menos | 2.25 | 0.425 | 0.411 | -0.045 |
| 2T | 2.5 | Más | 2.87 | 0.296 | 0.311 | -0.151 |
| 2T | 2.5 | Menos | 1.4 | 0.704 | 0.689 | -0.014 |

Comprobación: Betano trae 31 líneas de goles; la ficha trae 31 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 9.25 / 5.8 / 1.3; margen 5.0%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Serbia | 9.25 | 0.082 | 0.092 | 0.103 | -1.0 |
| Empate | 5.8 | 0.132 | 0.152 | 0.164 | -2.0 |
| Alemania | 1.3 | 0.786 | 0.755 | 0.733 | +3.1 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Serbia: ganó 2 de 7, no perdió 2 de 7, marcó 5 de 7, dejó la portería a cero 0 de 7, ambos marcaron 5 de 7.
- Alemania: ganó 2 de 7, no perdió 4 de 7, marcó 5 de 7, dejó la portería a cero 2 de 7, ambos marcaron 4 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Serbia | 9.25 | 0.089 | 0.085 | 0.092 | -0.3 | -0.173 |
| Empate | 5.8 | 0.135 | 0.149 | 0.152 | -1.7 | -0.215 |
| Gana Alemania | 1.3 | 0.775 | 0.766 | 0.755 | +2.0 | +0.008 |
| Serbia o empate | 3.65 | 0.225 | 0.234 | 0.245 | -2.0 | -0.180 |
| Alemania o empate | 1.08 | 0.911 | 0.915 | 0.907 | +0.3 | -0.017 |
| No hay empate | 1.14 | 0.865 | 0.851 | 0.848 | +1.7 | -0.014 |
| 1.er tiempo: Serbia | 7.1 | 0.104 | 0.106 | 0.117 | -1.3 | -0.264 |
| 1.er tiempo: Empate | 2.8 | 0.319 | 0.316 | 0.324 | -0.5 | -0.107 |
| 1.er tiempo: Alemania | 1.7 | 0.577 | 0.578 | 0.559 | +1.8 | -0.019 |
| 2.º tiempo: Serbia | 6.7 | 0.120 | 0.121 | 0.119 | +0.1 | -0.197 |
| 2.º tiempo: Empate | 3.35 | 0.264 | 0.269 | 0.259 | +0.5 | -0.115 |
| 2.º tiempo: Alemania | 1.53 | 0.616 | 0.610 | 0.622 | -0.6 | -0.058 |
| Descanso o final: Serbia | 4.75 | 0.169 | 0.167 | 0.197 | -2.8 | -0.197 |
| Descanso o final: Empate | 2.22 | 0.393 | 0.397 | 0.421 | -2.8 | -0.127 |
| Descanso o final: Alemania | 1.21 | 0.804 | 0.798 | 0.772 | +3.1 | -0.027 |
| Ambos marcan: Sí | 1.75 | 0.534 | 0.544 | 0.539 | -0.6 | -0.066 |
| Ambos marcan: No | 2.02 | 0.466 | 0.456 | 0.461 | +0.6 | -0.058 |
| Descanso/final: Serbia / Serbia | 15.0 | 0.041 | 0.042 | 0.047 | -0.6 | -0.385 |
| Descanso/final: Serbia / Empate | 20.0 | 0.028 | 0.030 | 0.034 | -0.5 | -0.433 |
| Descanso/final: Serbia / Alemania | 19.0 | 0.034 | 0.034 | 0.036 | -0.2 | -0.358 |
| Descanso/final: Empate / Serbia | 18.5 | 0.038 | 0.034 | 0.037 | +0.1 | -0.297 |
| Descanso/final: Empate / Empate | 8.75 | 0.076 | 0.083 | 0.086 | -0.9 | -0.333 |
| Descanso/final: Empate / Alemania | 4.15 | 0.204 | 0.198 | 0.200 | +0.4 | -0.154 |
| Descanso/final: Alemania / Serbia | 70.0 | 0.010 | 0.008 | 0.008 | +0.2 | -0.309 |
| Descanso/final: Alemania / Empate | 20.0 | 0.031 | 0.036 | 0.034 | -0.3 | -0.381 |
| Descanso/final: Alemania / Alemania | 1.78 | 0.538 | 0.535 | 0.520 | +1.7 | -0.043 |
| Hándicap Serbia -1 | 20.0 | 0.022 | 0.023 | 0.026 | -0.4 | -0.559 |
| Hándicap empate (Serbia -1) | 9.5 | 0.066 | 0.061 | 0.064 | +0.2 | -0.373 |
| Hándicap Alemania +1 | 1.08 | 0.912 | 0.916 | 0.910 | +0.2 | -0.015 |
| Hándicap Serbia +1 | 3.65 | 0.226 | 0.236 | 0.247 | -2.1 | -0.175 |
| Hándicap empate (Serbia +1) | 4.15 | 0.235 | 0.222 | 0.215 | +2.0 | -0.024 |
| Hándicap Alemania -1 | 1.78 | 0.539 | 0.542 | 0.537 | +0.2 | -0.041 |
| Hándicap Serbia +2 | 2.05 | 0.460 | 0.457 | 0.461 | -0.1 | -0.057 |
| Hándicap empate (Serbia +2) | 4.2 | 0.226 | 0.222 | 0.212 | +1.4 | -0.049 |
| Hándicap Alemania -2 | 2.82 | 0.314 | 0.322 | 0.327 | -1.3 | -0.116 |
| Hándicap Serbia +3 | 1.44 | 0.686 | 0.677 | 0.672 | +1.4 | -0.013 |
| Hándicap empate (Serbia +3) | 5.4 | 0.159 | 0.163 | 0.159 | -0.0 | -0.142 |
| Hándicap Alemania -3 | 5.1 | 0.155 | 0.159 | 0.169 | -1.4 | -0.207 |
| Hándicap Serbia +4 | 1.17 | 0.847 | 0.843 | 0.835 | +1.2 | -0.010 |
| Hándicap empate (Serbia +4) | 7.9 | 0.088 | 0.088 | 0.093 | -0.4 | -0.300 |
| Hándicap Alemania -4 | 9.75 | 0.065 | 0.069 | 0.073 | -0.8 | -0.366 |
| Hándicap Serbia +1.25 | 2.4 | 0.391 | 0.391 | 0.396 | -0.6 | -0.062 |
| Hándicap Alemania -1.25 | 1.6 | 0.614 | 0.614 | 0.608 | +0.6 | -0.017 |
| Hándicap Serbia +1.5 | 2.07 | 0.460 | 0.456 | 0.460 | -0.0 | -0.049 |
| Hándicap Alemania -1.5 | 1.78 | 0.540 | 0.544 | 0.540 | +0.0 | -0.038 |
| Hándicap Serbia +1.75 | 1.87 | 0.520 | 0.516 | 0.517 | +0.3 | -0.027 |
| Hándicap Alemania -1.75 | 1.98 | 0.484 | 0.489 | 0.487 | -0.3 | -0.041 |
| Hándicap Serbia +2.25 | 1.53 | 0.648 | 0.640 | 0.637 | +1.0 | -0.009 |
| Hándicap Alemania -2.25 | 2.57 | 0.357 | 0.365 | 0.368 | -1.0 | -0.081 |
| Hándicap Serbia +2.5 | 1.45 | 0.686 | 0.678 | 0.673 | +1.3 | -0.005 |
| Hándicap Alemania -2.5 | 2.85 | 0.314 | 0.322 | 0.327 | -1.3 | -0.106 |

Diferencia máxima modelo − mercado en estas selecciones: 3.1 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
