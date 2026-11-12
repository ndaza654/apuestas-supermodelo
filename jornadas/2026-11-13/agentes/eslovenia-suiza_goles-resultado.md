# Goles y resultado · Eslovenia - Suiza · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas Betano leídas el Cuotas de Betano leídas 2026-11-12T17:32:27.194Z · 240 mercados. Todas las cifras salen de `fichas/ficha_eslovenia-suiza.json` (clave `goles`, `contexto`), `informes/eslovenia-suiza_resultado.json` y `betano/eslovenia-suiza.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (11 líneas), de Eslovenia (3), de Suiza (4), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 11 mercados de hándicap. Ambos marcan 1T/2T y total exacto no aparecen.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 3 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 25 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 43 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 8 líneas; especial: 2 líneas; tarjetas: 16 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 2.3 pts (Descanso o final: Eslovenia). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 0.78 / 1.62 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.32 | 2.42 | 2.41 | 1.5 | 1.0–4.0 |
| local | 0.75 | 0.79 | 0.79 | 0.86 | 0.0–2.0 |
| visitante | 1.57 | 1.63 | 1.62 | 1.19 | 0.0–3.0 |
| 1T | 1.04 | 1.09 | 1.03 | 1.01 | 0.0–2.0 |
| 2T | 1.29 | 1.33 | 1.38 | 1.13 | 0.0–3.0 |

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Eslovenia: motivación alta, necesita ganar True, rotación False. Suiza: motivación alta, necesita ganar False, rotación False. Bajas: ninguna anotada. Dudas: ['Historial: sin casar con Betano → Gnezda Cerin A.', 'Alineación probable: sin casar con Betano → Gnezda Cerin A.'].

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Eslovenia n = 7, Suiza n = 7, directos n = 3.
- Esperado = (a favor propio + concedido por el rival)/2: Eslovenia 0.71 (a favor 0.86 · Suiza concede 0.57); Suiza 1.5 (a favor 2.14 · Eslovenia concede 0.86); total 2.21.
- Series (a favor–en contra): Eslovenia 2-1 1-2 2-0 0-0 1-1 0-2 0-0; Suiza 3-0 2-1 3-0 3-0 1-3 1-0 2-0; directos (total) 3 0 3.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.09 | 2.21 | +1.71 | 5 de 7 | 7 de 7 | 2 de 3 | SÍ | no | 0.904 | 0.905 | -0.014 |
| 0.5 | Menos | 7.6 | 2.21 | -1.71 | 2 de 7 | 0 de 7 | 1 de 3 | no | sí | 0.096 | 0.095 | -0.273 |
| 1.5 | Más | 1.4 | 2.21 | +0.71 | 5 de 7 | 6 de 7 | 2 de 3 | SÍ | sí | 0.677 | 0.693 | -0.052 |
| 1.5 | Menos | 2.95 | 2.21 | -0.71 | 2 de 7 | 1 de 7 | 1 de 3 | no | sí | 0.323 | 0.307 | -0.049 |
| 1.75 | Más | 1.5 | 2.21 | +0.46 | 2 de 7 | 5 de 7 | 2 de 3 | no | sí | 0.634 | 0.650 | -0.050 |
| 1.75 | Menos | 2.65 | 2.21 | -0.46 | 2 de 7 | 1 de 7 | 1 de 3 | no | sí | 0.372 | 0.355 | -0.013 |
| 2 | Más | 1.67 | 2.21 | +0.21 | 2 de 7 | 5 de 7 | 2 de 3 | no | sí | 0.569 | 0.585 | -0.049 |
| 2 | Menos | 2.27 | 2.21 | -0.21 | 2 de 7 | 1 de 7 | 1 de 3 | no | sí | 0.441 | 0.425 | +0.002 |
| 2.25 | Más | 1.93 | 2.21 | -0.04 | 2 de 7 | 5 de 7 | 2 de 3 | no | sí | 0.480 | 0.500 | -0.073 |
| 2.25 | Menos | 1.91 | 2.21 | +0.04 | 2 de 7 | 1 de 7 | 1 de 3 | no | sí | 0.525 | 0.505 | +0.003 |
| 2.5 | Más | 2.18 | 2.21 | -0.29 | 2 de 7 | 5 de 7 | 2 de 3 | no | sí | 0.412 | 0.434 | -0.102 |
| 2.5 | Menos | 1.7 | 2.21 | +0.29 | 5 de 7 | 2 de 7 | 1 de 3 | no | sí | 0.588 | 0.566 | -0.001 |
| 2.75 | Más | 2.57 | 2.21 | -0.54 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.346 | 0.367 | -0.109 |
| 2.75 | Menos | 1.53 | 2.21 | +0.54 | 5 de 7 | 2 de 7 | 1 de 3 | no | sí | 0.658 | 0.637 | +0.007 |
| 3 | Más | 3.25 | 2.21 | -0.79 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.265 | 0.287 | -0.138 |
| 3 | Menos | 1.36 | 2.21 | +0.79 | 5 de 7 | 2 de 7 | 1 de 3 | no | sí | 0.744 | 0.722 | +0.012 |
| 3.5 | Más | 3.9 | 2.21 | -1.29 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.201 | 0.224 | -0.216 |
| 3.5 | Menos | 1.26 | 2.21 | +1.29 | 7 de 7 | 6 de 7 | 3 de 3 | SÍ | sí | 0.799 | 0.776 | +0.007 |
| 4.5 | Más | 7.5 | 2.21 | -2.29 | 0 de 7 | 0 de 7 | 0 de 3 | no | sí | 0.082 | 0.096 | -0.385 |
| 4.5 | Menos | 1.09 | 2.21 | +2.29 | 7 de 7 | 7 de 7 | 3 de 3 | SÍ | no | 0.918 | 0.904 | +0.001 |
| 5.5 | Más | 13.0 | 2.21 | -3.29 | 0 de 7 | 0 de 7 | 0 de 3 | no | sí | 0.030 | 0.037 | -0.615 |
| 5.5 | Menos | 1.03 | 2.21 | +3.29 | 7 de 7 | 7 de 7 | 3 de 3 | SÍ | no | 0.970 | 0.963 | -0.001 |

### Goles · Eslovenia (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.72 | 0.71 | +0.21 | 4 de 7 | 2 de 7 | 1 de 3* | no | sí | 0.531 | 0.548 | -0.087 |
| 0.5 | Menos | 2.05 | 0.71 | -0.21 | 3 de 7 | 5 de 7 | 2 de 3* | no | sí | 0.469 | 0.452 | -0.038 |
| 1.5 | Más | 4.35 | 0.71 | -0.79 | 2 de 7 | 1 de 7 | 0 de 3* | no | sí | 0.172 | 0.182 | -0.249 |
| 1.5 | Menos | 1.19 | 0.71 | +0.79 | 5 de 7 | 6 de 7 | 3 de 3* | SÍ | no | 0.828 | 0.818 | -0.015 |
| 2.5 | Más | 9.75 | 0.71 | -1.79 | 0 de 7 | 1 de 7 | 0 de 3* | no | sí | 0.037 | 0.041 | -0.641 |
| 2.5 | Menos | 1.03 | 0.71 | +1.79 | 7 de 7 | 6 de 7 | 3 de 3* | SÍ | no | 0.963 | 0.959 | -0.008 |

### Goles · Suiza (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.2 | 1.5 | +1.00 | 4 de 7 | 7 de 7 | 2 de 3* | no | sí | 0.806 | 0.810 | -0.033 |
| 0.5 | Menos | 4.2 | 1.5 | -1.00 | 3 de 7 | 0 de 7 | 1 de 3* | no | sí | 0.194 | 0.190 | -0.184 |
| 1.5 | Más | 1.93 | 1.5 | +0.00 | 2 de 7 | 5 de 7 | 2 de 3* | no | sí | 0.471 | 0.484 | -0.090 |
| 1.5 | Menos | 1.82 | 1.5 | +0.00 | 5 de 7 | 2 de 7 | 1 de 3* | no | sí | 0.528 | 0.516 | -0.038 |
| 2.5 | Más | 3.8 | 1.5 | -1.00 | 0 de 7 | 3 de 7 | 1 de 3* | no | sí | 0.203 | 0.218 | -0.229 |
| 2.5 | Menos | 1.24 | 1.5 | +1.00 | 7 de 7 | 4 de 7 | 2 de 3* | no | sí | 0.797 | 0.782 | -0.011 |
| 3.5 | Más | 7.5 | 1.5 | -2.00 | 0 de 7 | 0 de 7 | 0 de 3* | no | sí | 0.068 | 0.081 | -0.490 |
| 3.5 | Menos | 1.07 | 1.5 | +2.00 | 7 de 7 | 7 de 7 | 3 de 3* | SÍ | no | 0.932 | 0.919 | -0.003 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.5 | 0.635 | 0.639 | -0.047 |
| 1T | 0.5 | Menos | 2.52 | 0.365 | 0.361 | -0.081 |
| 1T | 0.75 | Más | 1.72 | 0.557 | 0.561 | -0.042 |
| 1T | 0.75 | Menos | 2.12 | 0.453 | 0.449 | -0.041 |
| 1T | 1 | Más | 2.18 | 0.437 | 0.443 | -0.048 |
| 1T | 1 | Menos | 1.7 | 0.581 | 0.574 | -0.013 |
| 1T | 1.25 | Más | 2.72 | 0.337 | 0.345 | -0.084 |
| 1T | 1.25 | Menos | 1.47 | 0.672 | 0.664 | -0.012 |
| 1T | 1.5 | Más | 3.2 | 0.269 | 0.276 | -0.141 |
| 1T | 1.5 | Menos | 1.34 | 0.732 | 0.724 | -0.020 |
| 1T | 2.5 | Más | 7.6 | 0.082 | 0.088 | -0.376 |
| 1T | 2.5 | Menos | 1.08 | 0.918 | 0.912 | -0.009 |
| 2T | 0.5 | Más | 1.3 | 0.732 | 0.747 | -0.049 |
| 2T | 0.5 | Menos | 3.45 | 0.268 | 0.253 | -0.074 |
| 2T | 1.5 | Más | 2.3 | 0.378 | 0.402 | -0.132 |
| 2T | 1.5 | Menos | 1.6 | 0.622 | 0.598 | -0.004 |
| 2T | 2.5 | Más | 4.9 | 0.145 | 0.164 | -0.291 |
| 2T | 2.5 | Menos | 1.17 | 0.855 | 0.836 | +0.001 |

Comprobación: Betano trae 27 líneas de goles; la ficha trae 27 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 5.4 / 3.6 / 1.7; margen 5.1%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Eslovenia | 5.4 | 0.168 | 0.169 | 0.176 | -0.1 |
| Empate | 3.6 | 0.254 | 0.259 | 0.264 | -0.5 |
| Suiza | 1.7 | 0.578 | 0.572 | 0.560 | +0.6 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Eslovenia: ganó 2 de 7, no perdió 5 de 7, marcó 4 de 7, dejó la portería a cero 3 de 7, ambos marcaron 3 de 7.
- Suiza: ganó 6 de 7, no perdió 6 de 7, marcó 7 de 7, dejó la portería a cero 5 de 7, ambos marcaron 2 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Eslovenia | 5.4 | 0.172 | 0.164 | 0.169 | +0.3 | -0.068 |
| Empate | 3.6 | 0.255 | 0.258 | 0.259 | -0.4 | -0.081 |
| Gana Suiza | 1.7 | 0.572 | 0.578 | 0.572 | +0.1 | -0.027 |
| Eslovenia o empate | 2.2 | 0.428 | 0.422 | 0.428 | -0.1 | -0.059 |
| Suiza o empate | 1.17 | 0.828 | 0.836 | 0.831 | -0.3 | -0.032 |
| No hay empate | 1.28 | 0.745 | 0.742 | 0.741 | +0.4 | -0.047 |
| 1.er tiempo: Eslovenia | 5.6 | 0.141 | 0.148 | 0.152 | -1.1 | -0.212 |
| 1.er tiempo: Empate | 2.05 | 0.457 | 0.447 | 0.456 | +0.1 | -0.063 |
| 1.er tiempo: Suiza | 2.35 | 0.402 | 0.405 | 0.393 | +1.0 | -0.054 |
| 2.º tiempo: Eslovenia | 5.0 | 0.173 | 0.169 | 0.169 | +0.4 | -0.137 |
| 2.º tiempo: Empate | 2.45 | 0.384 | 0.379 | 0.371 | +1.2 | -0.060 |
| 2.º tiempo: Suiza | 2.02 | 0.444 | 0.452 | 0.460 | -1.6 | -0.104 |
| Descanso o final: Eslovenia | 3.45 | 0.249 | 0.248 | 0.271 | -2.2 | -0.142 |
| Descanso o final: Empate | 1.67 | 0.546 | 0.543 | 0.560 | -1.3 | -0.088 |
| Descanso o final: Suiza | 1.5 | 0.625 | 0.632 | 0.623 | +0.2 | -0.062 |
| Ambos marcan: Sí | 2.07 | 0.428 | 0.452 | 0.446 | -1.8 | -0.114 |
| Ambos marcan: No | 1.7 | 0.572 | 0.548 | 0.554 | +1.7 | -0.028 |
| Descanso/final: Eslovenia / Eslovenia | 9.5 | 0.081 | 0.080 | 0.082 | -0.1 | -0.233 |
| Descanso/final: Eslovenia / Empate | 17.0 | 0.036 | 0.042 | 0.043 | -0.7 | -0.381 |
| Descanso/final: Eslovenia / Suiza | 28.0 | 0.023 | 0.025 | 0.025 | -0.2 | -0.368 |
| Descanso/final: Empate / Eslovenia | 10.25 | 0.081 | 0.072 | 0.075 | +0.5 | -0.172 |
| Descanso/final: Empate / Empate | 4.85 | 0.175 | 0.171 | 0.173 | +0.2 | -0.152 |
| Descanso/final: Empate / Suiza | 4.1 | 0.202 | 0.204 | 0.209 | -0.7 | -0.172 |
| Descanso/final: Suiza / Eslovenia | 65.0 | 0.010 | 0.011 | 0.010 | +0.0 | -0.345 |
| Descanso/final: Suiza / Empate | 16.5 | 0.045 | 0.045 | 0.044 | +0.0 | -0.263 |
| Descanso/final: Suiza / Suiza | 2.65 | 0.348 | 0.349 | 0.339 | +0.9 | -0.078 |
| Hándicap Eslovenia -2 | 32.0 | 0.009 | 0.010 | 0.011 | -0.2 | -0.726 |
| Hándicap empate (Eslovenia -2) | 12.0 | 0.035 | 0.036 | 0.039 | -0.4 | -0.578 |
| Hándicap Suiza +2 | 1.04 | 0.956 | 0.954 | 0.950 | +0.6 | -0.005 |
| Hándicap Eslovenia -1 | 14.5 | 0.042 | 0.044 | 0.046 | -0.4 | -0.396 |
| Hándicap empate (Eslovenia -1) | 6.3 | 0.129 | 0.118 | 0.120 | +0.9 | -0.187 |
| Hándicap Suiza +1 | 1.17 | 0.829 | 0.838 | 0.834 | -0.5 | -0.030 |
| Hándicap Eslovenia +1 | 2.2 | 0.427 | 0.422 | 0.427 | +0.0 | -0.060 |
| Hándicap empate (Eslovenia +1) | 3.4 | 0.271 | 0.274 | 0.267 | +0.4 | -0.080 |
| Hándicap Suiza -1 | 3.0 | 0.302 | 0.304 | 0.306 | -0.4 | -0.094 |
| Hándicap Eslovenia +2 | 1.39 | 0.699 | 0.696 | 0.696 | +0.3 | -0.029 |
| Hándicap empate (Eslovenia +2) | 4.85 | 0.181 | 0.179 | 0.175 | +0.6 | -0.123 |
| Hándicap Suiza -2 | 6.4 | 0.120 | 0.124 | 0.129 | -0.9 | -0.229 |
| Hándicap Eslovenia +3 | 1.13 | 0.878 | 0.874 | 0.868 | +1.0 | -0.008 |
| Hándicap empate (Eslovenia +3) | 8.25 | 0.084 | 0.084 | 0.087 | -0.3 | -0.308 |
| Hándicap Suiza -3 | 14.5 | 0.038 | 0.042 | 0.045 | -0.7 | -0.448 |
| Hándicap Eslovenia +0.25 | 2.75 | 0.344 | 0.338 | 0.342 | +0.3 | -0.053 |
| Hándicap Suiza -0.25 | 1.47 | 0.661 | 0.668 | 0.664 | -0.3 | -0.028 |
| Hándicap Eslovenia +0.5 | 2.22 | 0.429 | 0.423 | 0.430 | -0.1 | -0.049 |
| Hándicap Suiza -0.5 | 1.7 | 0.571 | 0.577 | 0.570 | +0.1 | -0.029 |
| Hándicap Eslovenia +0.75 | 1.95 | 0.497 | 0.492 | 0.496 | +0.1 | -0.031 |
| Hándicap Suiza -0.75 | 1.9 | 0.509 | 0.513 | 0.510 | -0.1 | -0.034 |
| Hándicap Eslovenia +1.25 | 1.5 | 0.654 | 0.651 | 0.651 | +0.2 | -0.019 |
| Hándicap Suiza -1.25 | 2.67 | 0.352 | 0.355 | 0.354 | -0.2 | -0.060 |
| Hándicap Eslovenia +1.5 | 1.4 | 0.700 | 0.697 | 0.697 | +0.2 | -0.021 |
| Hándicap Suiza -1.5 | 3.05 | 0.300 | 0.303 | 0.303 | -0.2 | -0.084 |

Diferencia máxima modelo − mercado en estas selecciones: 2.2 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
