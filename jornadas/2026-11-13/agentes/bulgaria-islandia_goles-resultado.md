# Goles y resultado · Bulgaria - Islandia · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas de Betano leídas 2026-11-12T17:32:23.792Z · 212 mercados (UTC; 17:32 UTC = 12:32 Bogotá). Todas las cifras salen de `fichas/ficha_bulgaria-islandia.json` (clave `goles`, `contexto`), `informes/bulgaria-islandia_resultado.json` y `betano/bulgaria-islandia.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (10 líneas), de Bulgaria (3), de Islandia (4), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 10 mercados de hándicap.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 33 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 35 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 4 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 2.1 pts (Descanso o final: Bulgaria). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 0.92 / 1.56 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.44 | 2.49 | 2.48 | 1.54 | 1.0–4.0 |
| local | 0.91 | 0.94 | 0.92 | 0.92 | 0.0–2.0 |
| visitante | 1.53 | 1.55 | 1.56 | 1.18 | 0.0–3.0 |
| 1T | 1.08 | 1.12 | 1.12 | 1.04 | 0.0–2.0 |
| 2T | 1.35 | 1.37 | 1.37 | 1.16 | 0.0–3.0 |

Esperado de la ficha (historial) vs media implícita de Betano: total 2.86 vs 2.48; Bulgaria 1.5 vs 0.92; Islandia 1.36 vs 1.56. Cuando difieren mucho, el colchón (basado en el historial) y las cuotas cuentan historias distintas.

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Bulgaria: motivación alta, necesita ganar True, rotación False. Islandia: motivación alta, necesita ganar False, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Bulgaria n = 7, Islandia n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Bulgaria 1.5 (a favor 2.29 · Islandia concede 0.71); Islandia 1.36 (a favor 1.57 · Bulgaria concede 1.14); total 2.86.
- Series (a favor–en contra): Bulgaria 2-0 0-3 0-0 1-2 1-0 10-2 2-1; Islandia 0-0 3-0 3-0 1-1 0-2 2-0 2-2; directos (total) 3.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.07 | 2.86 | +2.36 | 6 de 7 | 6 de 7 | 1 de 1 | SÍ | no | 0.914 | 0.918 | -0.022 |
| 0.5 | Menos | 7.2 | 2.86 | -2.36 | 1 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.086 | 0.082 | -0.380 |
| 1.5 | Más | 1.36 | 2.86 | +1.36 | 5 de 7 | 6 de 7 | 1 de 1 | SÍ | sí | 0.703 | 0.708 | -0.043 |
| 1.5 | Menos | 3.0 | 2.86 | -1.36 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.297 | 0.292 | -0.110 |
| 1.75 | Más | 1.45 | 2.86 | +1.11 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.662 | 0.668 | -0.040 |
| 1.75 | Menos | 2.7 | 2.86 | -1.11 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.346 | 0.340 | -0.066 |
| 2 | Más | 1.57 | 2.86 | +0.86 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.608 | 0.616 | -0.045 |
| 2 | Menos | 2.35 | 2.86 | -0.86 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.408 | 0.400 | -0.041 |
| 2.25 | Más | 1.83 | 2.86 | +0.61 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.512 | 0.521 | -0.064 |
| 2.25 | Menos | 1.95 | 2.86 | -0.61 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.496 | 0.486 | -0.033 |
| 2.5 | Más | 2.05 | 2.86 | +0.36 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.440 | 0.452 | -0.098 |
| 2.5 | Menos | 1.72 | 2.86 | -0.36 | 3 de 7 | 4 de 7 | 0 de 1 | no | sí | 0.560 | 0.548 | -0.037 |
| 2.75 | Más | 2.4 | 2.86 | +0.11 | 1 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.376 | 0.386 | -0.097 |
| 2.75 | Menos | 1.55 | 2.86 | -0.11 | 3 de 7 | 4 de 7 | 0 de 1 | no | sí | 0.630 | 0.621 | -0.023 |
| 3.5 | Más | 3.55 | 2.86 | -0.64 | 1 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.227 | 0.237 | -0.194 |
| 3.5 | Menos | 1.27 | 2.86 | +0.64 | 6 de 7 | 6 de 7 | 1 de 1 | SÍ | sí | 0.773 | 0.762 | -0.018 |
| 4.5 | Más | 6.4 | 2.86 | -1.64 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.098 | 0.108 | -0.371 |
| 4.5 | Menos | 1.1 | 2.86 | +1.64 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.902 | 0.892 | -0.008 |
| 5.5 | Más | 10.0 | 2.86 | -2.64 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.035 | 0.040 | -0.648 |
| 5.5 | Menos | 1.03 | 2.86 | +2.64 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.965 | 0.960 | -0.006 |

### Goles · Bulgaria (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.57 | 1.5 | +1.00 | 5 de 7 | 3 de 7 | 0 de 1* | no | sí | 0.601 | 0.605 | -0.057 |
| 0.5 | Menos | 2.3 | 1.5 | -1.00 | 2 de 7 | 4 de 7 | 1 de 1* | no | sí | 0.399 | 0.395 | -0.082 |
| 1.5 | Más | 3.6 | 1.5 | +0.00 | 3 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.226 | 0.232 | -0.188 |
| 1.5 | Menos | 1.26 | 1.5 | +0.00 | 4 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.774 | 0.768 | -0.024 |
| 2.5 | Más | 8.25 | 1.5 | -1.00 | 1 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.057 | 0.062 | -0.534 |
| 2.5 | Menos | 1.05 | 1.5 | +1.00 | 6 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.944 | 0.938 | -0.009 |

### Goles · Islandia (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.22 | 1.36 | +0.86 | 4 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.797 | 0.795 | -0.028 |
| 0.5 | Menos | 3.95 | 1.36 | -0.86 | 3 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.203 | 0.205 | -0.197 |
| 1.5 | Más | 2.0 | 1.36 | -0.14 | 3 de 7 | 4 de 7 | 1 de 1* | no | sí | 0.460 | 0.463 | -0.081 |
| 1.5 | Menos | 1.75 | 1.36 | +0.14 | 4 de 7 | 3 de 7 | 0 de 1* | no | sí | 0.540 | 0.537 | -0.054 |
| 2.5 | Más | 4.0 | 1.36 | -1.14 | 1 de 7 | 2 de 7 | 1 de 1* | no | sí | 0.193 | 0.204 | -0.228 |
| 2.5 | Menos | 1.22 | 1.36 | +1.14 | 6 de 7 | 5 de 7 | 0 de 1* | SÍ | sí | 0.807 | 0.796 | -0.016 |
| 3.5 | Más | 7.9 | 1.36 | -2.14 | 0 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.063 | 0.072 | -0.506 |
| 3.5 | Menos | 1.06 | 1.36 | +2.14 | 7 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.937 | 0.928 | -0.006 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.42 | 0.659 | 0.673 | -0.065 |
| 1T | 0.5 | Menos | 2.7 | 0.341 | 0.327 | -0.079 |
| 1T | 0.75 | Más | 1.6 | 0.590 | 0.603 | -0.056 |
| 1T | 0.75 | Menos | 2.3 | 0.421 | 0.408 | -0.032 |
| 1T | 1 | Más | 1.95 | 0.482 | 0.494 | -0.060 |
| 1T | 1 | Menos | 1.83 | 0.539 | 0.528 | -0.013 |
| 1T | 1.25 | Más | 2.45 | 0.370 | 0.380 | -0.094 |
| 1T | 1.25 | Menos | 1.53 | 0.641 | 0.631 | -0.019 |
| 1T | 1.5 | Más | 2.85 | 0.298 | 0.309 | -0.151 |
| 1T | 1.5 | Menos | 1.39 | 0.702 | 0.691 | -0.024 |
| 1T | 2.5 | Más | 6.4 | 0.095 | 0.101 | -0.392 |
| 1T | 2.5 | Menos | 1.09 | 0.905 | 0.899 | -0.014 |
| 2T | 0.5 | Más | 1.3 | 0.745 | 0.747 | -0.031 |
| 2T | 0.5 | Menos | 3.45 | 0.255 | 0.253 | -0.121 |
| 2T | 1.5 | Más | 2.32 | 0.394 | 0.400 | -0.085 |
| 2T | 1.5 | Menos | 1.6 | 0.606 | 0.600 | -0.031 |
| 2T | 2.5 | Más | 5.0 | 0.152 | 0.157 | -0.238 |
| 2T | 2.5 | Menos | 1.16 | 0.848 | 0.843 | -0.017 |

Comprobación: Betano trae 26 líneas de goles; la ficha trae 26 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 4.3 / 3.6 / 1.87; margen 4.5%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Bulgaria | 4.3 | 0.211 | 0.218 | 0.223 | -0.7 |
| Empate | 3.6 | 0.272 | 0.262 | 0.266 | +1.0 |
| Islandia | 1.87 | 0.517 | 0.520 | 0.512 | -0.3 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Bulgaria: ganó 4 de 7, no perdió 5 de 7, marcó 5 de 7, dejó la portería a cero 3 de 7, ambos marcaron 3 de 7.
- Islandia: ganó 3 de 7, no perdió 6 de 7, marcó 5 de 7, dejó la portería a cero 4 de 7, ambos marcaron 2 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Bulgaria | 4.3 | 0.212 | 0.216 | 0.218 | -0.5 | -0.086 |
| Empate | 3.6 | 0.271 | 0.263 | 0.262 | +0.9 | -0.024 |
| Gana Islandia | 1.87 | 0.516 | 0.520 | 0.520 | -0.3 | -0.034 |
| Bulgaria o empate | 2.0 | 0.483 | 0.480 | 0.480 | +0.3 | -0.033 |
| Islandia o empate | 1.25 | 0.788 | 0.783 | 0.782 | +0.5 | -0.015 |
| No hay empate | 1.29 | 0.729 | 0.737 | 0.738 | -0.9 | -0.060 |
| 1.er tiempo: Bulgaria | 4.45 | 0.176 | 0.185 | 0.191 | -1.5 | -0.216 |
| 1.er tiempo: Empate | 2.12 | 0.448 | 0.436 | 0.434 | +1.3 | -0.051 |
| 1.er tiempo: Islandia | 2.42 | 0.376 | 0.378 | 0.375 | +0.1 | -0.089 |
| 2.º tiempo: Bulgaria | 4.3 | 0.204 | 0.206 | 0.203 | +0.1 | -0.124 |
| 2.º tiempo: Empate | 2.42 | 0.386 | 0.385 | 0.380 | +0.6 | -0.065 |
| 2.º tiempo: Islandia | 2.22 | 0.410 | 0.409 | 0.418 | -0.8 | -0.090 |
| Descanso o final: Bulgaria | 2.87 | 0.302 | 0.305 | 0.326 | -2.3 | -0.133 |
| Descanso o final: Empate | 1.72 | 0.549 | 0.539 | 0.543 | +0.6 | -0.055 |
| Descanso o final: Islandia | 1.6 | 0.580 | 0.586 | 0.584 | -0.4 | -0.072 |
| Ambos marcan: Sí | 1.91 | 0.484 | 0.492 | 0.483 | +0.1 | -0.075 |
| Ambos marcan: No | 1.8 | 0.516 | 0.508 | 0.517 | -0.1 | -0.071 |
| Descanso/final: Bulgaria / Bulgaria | 7.0 | 0.103 | 0.114 | 0.116 | -1.3 | -0.280 |
| Descanso/final: Bulgaria / Empate | 15.5 | 0.048 | 0.046 | 0.048 | +0.0 | -0.253 |
| Descanso/final: Bulgaria / Islandia | 28.0 | 0.024 | 0.025 | 0.025 | -0.1 | -0.325 |
| Descanso/final: Empate / Bulgaria | 9.0 | 0.094 | 0.088 | 0.088 | +0.7 | -0.151 |
| Descanso/final: Empate / Empate | 5.0 | 0.177 | 0.168 | 0.168 | +0.9 | -0.117 |
| Descanso/final: Empate / Islandia | 4.7 | 0.177 | 0.181 | 0.180 | -0.3 | -0.166 |
| Descanso/final: Islandia / Bulgaria | 55.0 | 0.014 | 0.013 | 0.012 | +0.2 | -0.233 |
| Descanso/final: Islandia / Empate | 16.0 | 0.046 | 0.049 | 0.046 | +0.0 | -0.258 |
| Descanso/final: Islandia / Islandia | 2.82 | 0.316 | 0.316 | 0.317 | -0.1 | -0.109 |
| Hándicap Bulgaria -2 | 26.0 | 0.012 | 0.016 | 0.018 | -0.6 | -0.684 |
| Hándicap empate (Bulgaria -2) | 11.0 | 0.049 | 0.052 | 0.052 | -0.3 | -0.461 |
| Hándicap Islandia +2 | 1.06 | 0.939 | 0.932 | 0.930 | +0.8 | -0.005 |
| Hándicap Bulgaria -1 | 10.75 | 0.063 | 0.070 | 0.072 | -1.0 | -0.326 |
| Hándicap empate (Bulgaria -1) | 5.7 | 0.150 | 0.147 | 0.146 | +0.4 | -0.144 |
| Hándicap Islandia +1 | 1.25 | 0.787 | 0.783 | 0.781 | +0.6 | -0.016 |
| Hándicap Bulgaria +1 | 2.0 | 0.482 | 0.478 | 0.477 | +0.5 | -0.035 |
| Hándicap empate (Bulgaria +1) | 3.65 | 0.253 | 0.258 | 0.251 | +0.2 | -0.075 |
| Hándicap Islandia -1 | 3.4 | 0.264 | 0.264 | 0.271 | -0.7 | -0.101 |
| Hándicap Bulgaria +2 | 1.33 | 0.737 | 0.738 | 0.732 | +0.5 | -0.020 |
| Hándicap empate (Bulgaria +2) | 5.4 | 0.160 | 0.159 | 0.158 | +0.2 | -0.138 |
| Hándicap Islandia -2 | 7.5 | 0.103 | 0.103 | 0.110 | -0.7 | -0.226 |
| Hándicap Bulgaria +3 | 1.1 | 0.899 | 0.898 | 0.894 | +0.5 | -0.011 |
| Hándicap empate (Bulgaria +3) | 9.5 | 0.070 | 0.070 | 0.071 | -0.0 | -0.331 |
| Hándicap Islandia -3 | 17.0 | 0.031 | 0.032 | 0.036 | -0.5 | -0.476 |
| Hándicap Bulgaria +0.25 | 2.3 | 0.407 | 0.406 | 0.406 | +0.1 | -0.064 |
| Hándicap Islandia -0.25 | 1.6 | 0.601 | 0.602 | 0.602 | -0.1 | -0.038 |
| Hándicap Bulgaria +0.5 | 1.95 | 0.484 | 0.480 | 0.481 | +0.3 | -0.056 |
| Hándicap Islandia -0.5 | 1.82 | 0.516 | 0.520 | 0.519 | -0.3 | -0.061 |
| Hándicap Bulgaria +0.75 | 1.72 | 0.558 | 0.555 | 0.555 | +0.3 | -0.040 |
| Hándicap Islandia -0.75 | 2.07 | 0.450 | 0.453 | 0.454 | -0.3 | -0.068 |
| Hándicap Bulgaria +1.25 | 1.4 | 0.700 | 0.700 | 0.694 | +0.6 | -0.020 |
| Hándicap Islandia -1.25 | 2.92 | 0.307 | 0.307 | 0.313 | -0.6 | -0.103 |

Diferencia máxima modelo − mercado en estas selecciones: 2.3 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
