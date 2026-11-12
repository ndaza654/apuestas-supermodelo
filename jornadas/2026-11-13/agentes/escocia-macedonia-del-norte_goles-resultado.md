# Goles y resultado · Escocia - Macedonia del Norte · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas Betano leídas el Cuotas de Betano leídas 2026-11-12T17:32:28.294Z · 270 mercados. Todas las cifras salen de `fichas/ficha_escocia-macedonia-del-norte.json` (clave `goles`, `contexto`), `informes/escocia-macedonia-del-norte_resultado.json` y `betano/escocia-macedonia-del-norte.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (10 líneas), de Escocia (6), de Macedonia del Norte (2), 1T (8) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 10 mercados de hándicap. Ambos marcan 1T/2T y total exacto no aparecen.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 34 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 37 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 41 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 48 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 4 líneas; especial: 2 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 3.1 pts (Descanso o final: Empate). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 2.47 / 0.47 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.93 | 2.94 | 2.95 | 1.63 | 1.0–5.0 |
| local | 2.48 | 2.48 | 2.48 | 1.45 | 1.0–4.0 |
| visitante | 0.45 | 0.46 | 0.47 | 0.67 | 0.0–1.0 |
| 1T | 1.36 | 1.38 | 1.31 | 1.14 | 0.0–3.0 |
| 2T | 1.57 | 1.56 | 1.64 | 1.22 | 0.0–3.0 |

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: normal. Escocia: motivación alta, necesita ganar True, rotación False. Macedonia del Norte: motivación baja, necesita ganar False, rotación False. Bajas: ninguna anotada. Dudas: ['Historial: sin casar con Betano → Gannon-Doak B.', 'Alineación probable: sin casar con Betano → Gannon-Doak B.', 'Luis Binks: Flashscore lo lista en el XI probable y también como baja; se toma como baja'].

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Escocia n = 7, Macedonia del Norte n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Escocia 1.86 (a favor 0.57 · Macedonia del Norte concede 3.14); Macedonia del Norte 0.79 (a favor 0.29 · Escocia concede 1.29); total 2.64.
- Series (a favor–en contra): Escocia 1-2 2-0 0-3 0-0 0-3 0-1 1-0; Macedonia del Norte 0-3 0-2 0-2 0-3 0-4 1-7 1-1; directos (total) 2.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.04 | 2.64 | +2.14 | 6 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.958 | 0.948 | -0.004 |
| 0.5 | Menos | 9.0 | 2.64 | -2.14 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.042 | 0.052 | -0.621 |
| 1.5 | Más | 1.23 | 2.64 | +1.14 | 4 de 7 | 7 de 7 | 1 de 1 | no | sí | 0.798 | 0.790 | -0.018 |
| 1.5 | Menos | 3.95 | 2.64 | -1.14 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.202 | 0.210 | -0.202 |
| 2.25 | Más | 1.52 | 2.64 | +0.39 | 3 de 7 | 4 de 7 | 0 de 1 | no | sí | 0.640 | 0.636 | -0.027 |
| 2.25 | Menos | 2.5 | 2.64 | -0.39 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.366 | 0.371 | -0.084 |
| 2.5 | Más | 1.67 | 2.64 | +0.14 | 3 de 7 | 4 de 7 | 0 de 1 | no | sí | 0.566 | 0.566 | -0.055 |
| 2.5 | Menos | 2.12 | 2.64 | -0.14 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.434 | 0.434 | -0.080 |
| 2.75 | Más | 1.85 | 2.64 | -0.11 | 0 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.511 | 0.512 | -0.054 |
| 2.75 | Menos | 1.91 | 2.64 | +0.11 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.496 | 0.495 | -0.052 |
| 3 | Más | 2.12 | 2.64 | -0.36 | 0 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.442 | 0.447 | -0.062 |
| 3 | Menos | 1.7 | 2.64 | +0.36 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.572 | 0.567 | -0.028 |
| 3.25 | Más | 2.4 | 2.64 | -0.61 | 0 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.380 | 0.386 | -0.089 |
| 3.25 | Menos | 1.55 | 2.64 | +0.61 | 4 de 7 | 3 de 7 | 1 de 1 | no | sí | 0.628 | 0.621 | -0.027 |
| 3.5 | Más | 2.62 | 2.64 | -0.86 | 0 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.331 | 0.340 | -0.133 |
| 3.5 | Menos | 1.45 | 2.64 | +0.86 | 7 de 7 | 5 de 7 | 1 de 1 | SÍ | sí | 0.669 | 0.660 | -0.030 |
| 4.5 | Más | 4.5 | 2.64 | -1.86 | 0 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.162 | 0.175 | -0.273 |
| 4.5 | Menos | 1.18 | 2.64 | +1.86 | 7 de 7 | 6 de 7 | 1 de 1 | SÍ | no | 0.839 | 0.825 | -0.011 |
| 5.5 | Más | 7.6 | 2.64 | -2.86 | 0 de 7 | 1 de 7 | 0 de 1 | no | sí | 0.073 | 0.081 | -0.446 |
| 5.5 | Menos | 1.07 | 2.64 | +2.86 | 7 de 7 | 6 de 7 | 1 de 1 | SÍ | no | 0.927 | 0.919 | -0.008 |

### Goles · Escocia (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.07 | 1.86 | +1.36 | 3 de 7 | 7 de 7 | 1 de 1* | no | no | 0.934 | 0.918 | -0.001 |
| 0.5 | Menos | 7.3 | 1.86 | -1.36 | 4 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.066 | 0.082 | -0.516 |
| 1.5 | Más | 1.36 | 1.86 | +0.36 | 1 de 7 | 6 de 7 | 1 de 1* | no | sí | 0.725 | 0.708 | -0.014 |
| 1.5 | Menos | 3.0 | 1.86 | -0.36 | 6 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.275 | 0.292 | -0.175 |
| 2.5 | Más | 2.05 | 1.86 | -0.64 | 0 de 7 | 4 de 7 | 0 de 1* | no | sí | 0.450 | 0.452 | -0.078 |
| 2.5 | Menos | 1.72 | 1.86 | +0.64 | 7 de 7 | 3 de 7 | 1 de 1* | no | sí | 0.550 | 0.548 | -0.053 |
| 3.5 | Más | 3.55 | 1.86 | -1.64 | 0 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.225 | 0.237 | -0.202 |
| 3.5 | Menos | 1.27 | 1.86 | +1.64 | 7 de 7 | 5 de 7 | 1 de 1* | SÍ | sí | 0.775 | 0.762 | -0.015 |
| 4.5 | Más | 6.4 | 1.86 | -2.64 | 0 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.092 | 0.101 | -0.410 |
| 4.5 | Menos | 1.09 | 1.86 | +2.64 | 7 de 7 | 6 de 7 | 1 de 1* | SÍ | no | 0.908 | 0.899 | -0.010 |
| 5.5 | Más | 10.25 | 1.86 | -3.64 | 0 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.035 | 0.040 | -0.643 |
| 5.5 | Menos | 1.03 | 1.86 | +3.64 | 7 de 7 | 6 de 7 | 1 de 1* | SÍ | no | 0.965 | 0.960 | -0.006 |

### Goles · Macedonia del Norte (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 2.4 | 0.79 | +0.29 | 4 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.367 | 0.377 | -0.120 |
| 0.5 | Menos | 1.53 | 0.79 | -0.29 | 3 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.633 | 0.623 | -0.031 |
| 1.5 | Más | 7.5 | 0.79 | -0.71 | 3 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.075 | 0.081 | -0.439 |
| 1.5 | Menos | 1.07 | 0.79 | +0.71 | 4 de 7 | 7 de 7 | 1 de 1* | no | no | 0.925 | 0.919 | -0.010 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.32 | 0.739 | 0.731 | -0.024 |
| 1T | 0.5 | Menos | 3.2 | 0.261 | 0.269 | -0.165 |
| 1T | 0.75 | Más | 1.44 | 0.684 | 0.675 | -0.016 |
| 1T | 0.75 | Menos | 2.75 | 0.327 | 0.336 | -0.101 |
| 1T | 1 | Más | 1.65 | 0.598 | 0.589 | -0.014 |
| 1T | 1 | Menos | 2.22 | 0.423 | 0.431 | -0.062 |
| 1T | 1.25 | Más | 2.05 | 0.469 | 0.462 | -0.038 |
| 1T | 1.25 | Menos | 1.75 | 0.541 | 0.548 | -0.052 |
| 1T | 1.5 | Más | 2.4 | 0.383 | 0.377 | -0.082 |
| 1T | 1.5 | Menos | 1.53 | 0.617 | 0.623 | -0.056 |
| 1T | 1.75 | Más | 3.0 | 0.303 | 0.300 | -0.091 |
| 1T | 1.75 | Menos | 1.37 | 0.705 | 0.708 | -0.035 |
| 1T | 2.5 | Más | 5.2 | 0.143 | 0.143 | -0.256 |
| 1T | 2.5 | Menos | 1.14 | 0.857 | 0.857 | -0.023 |
| 1T | 3.5 | Más | 9.75 | 0.043 | 0.041 | -0.585 |
| 1T | 3.5 | Menos | 1.03 | 0.958 | 0.959 | -0.014 |
| 2T | 0.5 | Más | 1.21 | 0.808 | 0.807 | -0.022 |
| 2T | 0.5 | Menos | 4.3 | 0.192 | 0.193 | -0.175 |
| 2T | 1.5 | Más | 1.93 | 0.479 | 0.488 | -0.076 |
| 2T | 1.5 | Menos | 1.85 | 0.521 | 0.511 | -0.035 |
| 2T | 2.5 | Más | 3.75 | 0.215 | 0.228 | -0.193 |
| 2T | 2.5 | Menos | 1.26 | 0.785 | 0.772 | -0.011 |

Comprobación: Betano trae 29 líneas de goles; la ficha trae 29 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 1.21 / 6.3 / 16.0; margen 4.8%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Escocia | 1.21 | 0.853 | 0.814 | 0.789 | +3.9 |
| Empate | 6.3 | 0.111 | 0.137 | 0.152 | -2.6 |
| Macedonia del Norte | 16.0 | 0.035 | 0.050 | 0.060 | -1.5 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Escocia: ganó 2 de 7, no perdió 3 de 7, marcó 3 de 7, dejó la portería a cero 3 de 7, ambos marcaron 1 de 7.
- Macedonia del Norte: ganó 0 de 7, no perdió 1 de 7, marcó 2 de 7, dejó la portería a cero 0 de 7, ambos marcaron 2 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Escocia | 1.21 | 0.843 | 0.824 | 0.814 | +2.9 | +0.020 |
| Empate | 6.3 | 0.117 | 0.131 | 0.137 | -2.0 | -0.264 |
| Gana Macedonia del Norte | 16.0 | 0.040 | 0.045 | 0.050 | -0.9 | -0.356 |
| Escocia o empate | 1.04 | 0.960 | 0.955 | 0.950 | +0.9 | -0.002 |
| Macedonia del Norte o empate | 4.8 | 0.157 | 0.176 | 0.186 | -2.9 | -0.246 |
| No hay empate | 1.12 | 0.883 | 0.869 | 0.864 | +2.0 | -0.011 |
| 1.er tiempo: Escocia | 1.57 | 0.618 | 0.618 | 0.598 | +2.0 | -0.030 |
| 1.er tiempo: Empate | 2.6 | 0.326 | 0.321 | 0.336 | -1.0 | -0.152 |
| 1.er tiempo: Macedonia del Norte | 10.75 | 0.056 | 0.061 | 0.067 | -1.0 | -0.397 |
| 2.º tiempo: Escocia | 1.45 | 0.662 | 0.650 | 0.658 | +0.4 | -0.040 |
| 2.º tiempo: Empate | 3.2 | 0.272 | 0.278 | 0.270 | +0.1 | -0.131 |
| 2.º tiempo: Macedonia del Norte | 10.5 | 0.066 | 0.072 | 0.071 | -0.5 | -0.305 |
| Descanso o final: Escocia | 1.16 | 0.851 | 0.834 | 0.806 | +4.5 | -0.013 |
| Descanso o final: Empate | 2.27 | 0.381 | 0.381 | 0.412 | -3.1 | -0.136 |
| Descanso o final: Macedonia del Norte | 7.7 | 0.092 | 0.100 | 0.121 | -3.0 | -0.294 |
| Ambos marcan: Sí | 2.55 | 0.341 | 0.347 | 0.345 | -0.3 | -0.130 |
| Ambos marcan: No | 1.45 | 0.659 | 0.653 | 0.655 | +0.3 | -0.045 |
| Descanso/final: Escocia / Escocia | 1.62 | 0.594 | 0.591 | 0.574 | +2.0 | -0.038 |
| Descanso/final: Escocia / Empate | 27.0 | 0.021 | 0.024 | 0.022 | -0.1 | -0.419 |
| Descanso/final: Escocia / Macedonia del Norte | 175.0 | 0.005 | 0.003 | 0.003 | +0.2 | -0.125 |
| Descanso/final: Empate / Escocia | 3.7 | 0.230 | 0.213 | 0.221 | +0.9 | -0.149 |
| Descanso/final: Empate / Empate | 7.9 | 0.078 | 0.087 | 0.092 | -1.4 | -0.383 |
| Descanso/final: Empate / Macedonia del Norte | 27.0 | 0.018 | 0.021 | 0.022 | -0.4 | -0.514 |
| Descanso/final: Macedonia del Norte / Escocia | 28.0 | 0.020 | 0.021 | 0.021 | -0.1 | -0.435 |
| Descanso/final: Macedonia del Norte / Empate | 29.0 | 0.017 | 0.019 | 0.021 | -0.4 | -0.520 |
| Descanso/final: Macedonia del Norte / Macedonia del Norte | 26.0 | 0.019 | 0.021 | 0.023 | -0.5 | -0.509 |
| Hándicap Escocia -5 | 19.0 | 0.024 | 0.026 | 0.029 | -0.4 | -0.536 |
| Hándicap empate (Escocia -5) | 12.0 | 0.044 | 0.047 | 0.050 | -0.6 | -0.476 |
| Hándicap Macedonia del Norte +5 | 1.07 | 0.932 | 0.927 | 0.922 | +1.0 | -0.003 |
| Hándicap Escocia -4 | 9.75 | 0.067 | 0.072 | 0.077 | -0.9 | -0.345 |
| Hándicap empate (Escocia -4) | 7.6 | 0.103 | 0.098 | 0.102 | +0.2 | -0.216 |
| Hándicap Macedonia del Norte +4 | 1.19 | 0.830 | 0.829 | 0.822 | +0.8 | -0.013 |
| Hándicap Escocia -3 | 4.9 | 0.171 | 0.171 | 0.179 | -0.8 | -0.162 |
| Hándicap empate (Escocia -3) | 5.0 | 0.178 | 0.184 | 0.175 | +0.2 | -0.111 |
| Hándicap Macedonia del Norte +3 | 1.5 | 0.651 | 0.645 | 0.645 | +0.6 | -0.023 |
| Hándicap Escocia -2 | 2.62 | 0.350 | 0.356 | 0.358 | -0.8 | -0.082 |
| Hándicap empate (Escocia -2) | 3.9 | 0.252 | 0.242 | 0.234 | +1.8 | -0.018 |
| Hándicap Macedonia del Norte +2 | 2.32 | 0.398 | 0.401 | 0.408 | -1.0 | -0.077 |
| Hándicap Escocia -1 | 1.62 | 0.603 | 0.600 | 0.594 | +0.9 | -0.022 |
| Hándicap empate (Escocia -1) | 4.05 | 0.241 | 0.225 | 0.221 | +1.9 | -0.025 |
| Hándicap Macedonia del Norte +1 | 4.8 | 0.156 | 0.175 | 0.184 | -2.8 | -0.251 |
| Hándicap Escocia -2.5 | 2.55 | 0.351 | 0.357 | 0.359 | -0.8 | -0.105 |
| Hándicap Macedonia del Norte +2.5 | 1.5 | 0.649 | 0.643 | 0.641 | +0.8 | -0.026 |
| Hándicap Escocia -2.25 | 2.3 | 0.404 | 0.408 | 0.406 | -0.2 | -0.071 |
| Hándicap Macedonia del Norte +2.25 | 1.6 | 0.604 | 0.600 | 0.601 | +0.3 | -0.034 |
| Hándicap Escocia -1.75 | 1.78 | 0.545 | 0.544 | 0.538 | +0.8 | -0.029 |
| Hándicap Macedonia del Norte +1.75 | 2.02 | 0.462 | 0.463 | 0.469 | -0.8 | -0.067 |
| Hándicap Escocia -1.5 | 1.62 | 0.602 | 0.598 | 0.591 | +1.1 | -0.025 |
| Hándicap Macedonia del Norte +1.5 | 2.27 | 0.398 | 0.402 | 0.409 | -1.1 | -0.096 |

Diferencia máxima modelo − mercado en estas selecciones: 4.5 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
