# Goles y resultado · Países Bajos - Grecia · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas Betano leídas el Cuotas de Betano leídas 2026-11-12T17:32:21.538Z · 592 mercados. Todas las cifras salen de `fichas/ficha_paises-bajos-grecia.json` (clave `goles`, `contexto`), `informes/paises-bajos-grecia_resultado.json` y `betano/paises-bajos-grecia.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (12 líneas), de Países Bajos (5), de Grecia (3), 1T (8) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 12 mercados de hándicap. Ambos marcan 1T/2T y total exacto no aparecen.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 3 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 30 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: saques_banda: 2 líneas; tarjetas: 2 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 3.0 pts (Descanso o final: Grecia). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 2.07 / 0.99 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 3.02 | 3.09 | 3.07 | 1.73 | 1.0–5.0 |
| local | 2.02 | 2.09 | 2.06 | 1.36 | 0.0–4.0 |
| visitante | 1.0 | 1.0 | 1.01 | 0.98 | 0.0–2.0 |
| 1T | 1.36 | 1.41 | 1.32 | 1.16 | 0.0–3.0 |
| 2T | 1.66 | 1.69 | 1.76 | 1.29 | 0.0–3.0 |

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: alta. Países Bajos: motivación alta, necesita ganar False, rotación False. Grecia: motivación alta, necesita ganar False, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Países Bajos n = 7, Grecia n = 7, directos n = 3.
- Esperado = (a favor propio + concedido por el rival)/2: Países Bajos 1.71 (a favor 2.29 · Grecia concede 1.14); Grecia 1.29 (a favor 1.29 · Países Bajos concede 1.29); total 3.0.
- Series (a favor–en contra): Países Bajos 2-1 2-2 2-1 1-1 1-2 3-1 5-1; Grecia 0-0 2-2 1-0 2-1 0-0 3-2 1-3; directos (total) 4 1 3.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.04 | 3.0 | +2.50 | 7 de 7 | 5 de 7 | 3 de 3 | SÍ | no | 0.950 | 0.952 | -0.012 |
| 0.5 | Menos | 11.25 | 3.0 | -2.50 | 0 de 7 | 2 de 7 | 0 de 3 | no | sí | 0.050 | 0.048 | -0.435 |
| 1.5 | Más | 1.21 | 3.0 | +1.50 | 7 de 7 | 4 de 7 | 2 de 3 | no | sí | 0.806 | 0.809 | -0.025 |
| 1.5 | Menos | 4.45 | 3.0 | -1.50 | 0 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.194 | 0.191 | -0.136 |
| 2.25 | Más | 1.47 | 3.0 | +0.75 | 6 de 7 | 4 de 7 | 2 de 3 | no | sí | 0.658 | 0.665 | -0.033 |
| 2.25 | Menos | 2.77 | 3.0 | -0.75 | 0 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.347 | 0.340 | -0.039 |
| 2.5 | Más | 1.62 | 3.0 | +0.50 | 6 de 7 | 4 de 7 | 2 de 3 | no | sí | 0.583 | 0.594 | -0.056 |
| 2.5 | Menos | 2.3 | 3.0 | -0.50 | 1 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.417 | 0.406 | -0.041 |
| 2.75 | Más | 1.8 | 3.0 | +0.25 | 3 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.529 | 0.539 | -0.048 |
| 2.75 | Menos | 2.07 | 3.0 | -0.25 | 1 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.475 | 0.465 | -0.016 |
| 3 | Más | 2.02 | 3.0 | +0.00 | 3 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.465 | 0.479 | -0.060 |
| 3 | Menos | 1.83 | 3.0 | +0.00 | 1 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.544 | 0.531 | -0.004 |
| 3.25 | Más | 2.3 | 3.0 | -0.25 | 3 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.401 | 0.415 | -0.079 |
| 3.25 | Menos | 1.65 | 3.0 | +0.25 | 1 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.604 | 0.589 | -0.003 |
| 3.5 | Más | 2.52 | 3.0 | -0.50 | 3 de 7 | 3 de 7 | 1 de 3 | no | sí | 0.351 | 0.368 | -0.115 |
| 3.5 | Menos | 1.53 | 3.0 | +0.50 | 4 de 7 | 4 de 7 | 2 de 3 | no | sí | 0.649 | 0.632 | -0.008 |
| 3.75 | Más | 3.0 | 3.0 | -0.75 | 1 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.296 | 0.313 | -0.111 |
| 3.75 | Menos | 1.42 | 3.0 | +0.75 | 4 de 7 | 4 de 7 | 2 de 3 | no | sí | 0.707 | 0.690 | +0.004 |
| 4.5 | Más | 4.35 | 3.0 | -1.50 | 1 de 7 | 1 de 7 | 0 de 3 | no | sí | 0.184 | 0.197 | -0.200 |
| 4.5 | Menos | 1.22 | 3.0 | +1.50 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | sí | 0.816 | 0.803 | -0.004 |
| 5.5 | Más | 7.8 | 3.0 | -2.50 | 1 de 7 | 0 de 7 | 0 de 3 | no | sí | 0.080 | 0.087 | -0.378 |
| 5.5 | Menos | 1.08 | 3.0 | +2.50 | 6 de 7 | 7 de 7 | 3 de 3 | SÍ | no | 0.920 | 0.913 | -0.006 |
| 6.5 | Más | 12.5 | 3.0 | -3.50 | 0 de 7 | 0 de 7 | 0 de 3 | no | sí | 0.033 | 0.038 | -0.588 |
| 6.5 | Menos | 1.03 | 3.0 | +3.50 | 7 de 7 | 7 de 7 | 3 de 3 | SÍ | no | 0.967 | 0.962 | -0.004 |

### Goles · Países Bajos (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.12 | 1.71 | +1.21 | 7 de 7 | 4 de 7 | 3 de 3* | no | no | 0.874 | 0.874 | -0.021 |
| 0.5 | Menos | 5.7 | 1.71 | -1.21 | 0 de 7 | 3 de 7 | 0 de 3* | no | sí | 0.126 | 0.126 | -0.280 |
| 1.5 | Más | 1.55 | 1.71 | +0.21 | 5 de 7 | 3 de 7 | 2 de 3* | no | sí | 0.602 | 0.614 | -0.068 |
| 1.5 | Menos | 2.35 | 1.71 | -0.21 | 2 de 7 | 4 de 7 | 1 de 3* | no | sí | 0.398 | 0.386 | -0.064 |
| 2.5 | Más | 2.65 | 1.71 | -0.79 | 2 de 7 | 1 de 7 | 1 de 3* | no | sí | 0.322 | 0.338 | -0.146 |
| 2.5 | Menos | 1.45 | 1.71 | +0.79 | 5 de 7 | 6 de 7 | 2 de 3* | SÍ | sí | 0.678 | 0.662 | -0.017 |
| 3.5 | Más | 5.0 | 1.71 | -1.79 | 1 de 7 | 0 de 7 | 0 de 3* | no | sí | 0.138 | 0.151 | -0.309 |
| 3.5 | Menos | 1.15 | 1.71 | +1.79 | 6 de 7 | 7 de 7 | 3 de 3* | SÍ | no | 0.862 | 0.849 | -0.009 |
| 4.5 | Más | 8.75 | 1.71 | -2.79 | 1 de 7 | 0 de 7 | 0 de 3* | no | sí | 0.051 | 0.061 | -0.555 |
| 4.5 | Menos | 1.05 | 1.71 | +2.79 | 6 de 7 | 7 de 7 | 3 de 3* | SÍ | no | 0.949 | 0.939 | -0.003 |

### Goles · Grecia (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.5 | 1.29 | +0.79 | 7 de 7 | 5 de 7 | 1 de 3* | SÍ | sí | 0.636 | 0.638 | -0.045 |
| 0.5 | Menos | 2.5 | 1.29 | -0.79 | 0 de 7 | 2 de 7 | 2 de 3* | no | sí | 0.364 | 0.362 | -0.091 |
| 1.5 | Más | 3.25 | 1.29 | -0.21 | 2 de 7 | 3 de 7 | 1 de 3* | no | sí | 0.263 | 0.263 | -0.146 |
| 1.5 | Menos | 1.31 | 1.29 | +0.21 | 5 de 7 | 4 de 7 | 2 de 3* | no | sí | 0.737 | 0.737 | -0.034 |
| 2.5 | Más | 7.6 | 1.29 | -1.21 | 0 de 7 | 1 de 7 | 0 de 3* | no | sí | 0.078 | 0.081 | -0.404 |
| 2.5 | Menos | 1.07 | 1.29 | +1.21 | 7 de 7 | 6 de 7 | 3 de 3* | SÍ | no | 0.922 | 0.919 | -0.014 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.33 | 0.734 | 0.727 | -0.024 |
| 1T | 0.5 | Menos | 3.2 | 0.266 | 0.273 | -0.147 |
| 1T | 0.75 | Más | 1.45 | 0.678 | 0.672 | -0.017 |
| 1T | 0.75 | Menos | 2.77 | 0.331 | 0.337 | -0.083 |
| 1T | 1 | Más | 1.65 | 0.594 | 0.591 | -0.020 |
| 1T | 1 | Menos | 2.25 | 0.424 | 0.426 | -0.046 |
| 1T | 1.25 | Más | 2.05 | 0.466 | 0.467 | -0.045 |
| 1T | 1.25 | Menos | 1.78 | 0.543 | 0.542 | -0.033 |
| 1T | 1.5 | Más | 2.42 | 0.378 | 0.381 | -0.084 |
| 1T | 1.5 | Menos | 1.55 | 0.622 | 0.619 | -0.037 |
| 1T | 1.75 | Más | 3.05 | 0.298 | 0.300 | -0.090 |
| 1T | 1.75 | Menos | 1.38 | 0.708 | 0.706 | -0.023 |
| 1T | 2.5 | Más | 5.3 | 0.144 | 0.148 | -0.238 |
| 1T | 2.5 | Menos | 1.15 | 0.856 | 0.852 | -0.015 |
| 1T | 3.5 | Más | 10.5 | 0.044 | 0.049 | -0.535 |
| 1T | 3.5 | Menos | 1.04 | 0.956 | 0.951 | -0.006 |
| 2T | 0.5 | Más | 1.18 | 0.816 | 0.828 | -0.037 |
| 2T | 0.5 | Menos | 4.7 | 0.184 | 0.172 | -0.135 |
| 2T | 1.5 | Más | 1.8 | 0.509 | 0.526 | -0.084 |
| 2T | 1.5 | Menos | 1.98 | 0.491 | 0.474 | -0.028 |
| 2T | 2.5 | Más | 3.4 | 0.241 | 0.258 | -0.179 |
| 2T | 2.5 | Menos | 1.31 | 0.759 | 0.742 | -0.006 |

Comprobación: Betano trae 31 líneas de goles; la ficha trae 31 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 1.57 / 4.25 / 5.5; margen 5.4%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Países Bajos | 1.57 | 0.618 | 0.620 | 0.604 | -0.2 |
| Empate | 4.25 | 0.222 | 0.216 | 0.223 | +0.6 |
| Grecia | 5.5 | 0.160 | 0.164 | 0.172 | -0.4 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Países Bajos: ganó 4 de 7, no perdió 6 de 7, marcó 7 de 7, dejó la portería a cero 0 de 7, ambos marcaron 7 de 7.
- Grecia: ganó 3 de 7, no perdió 6 de 7, marcó 5 de 7, dejó la portería a cero 3 de 7, ambos marcaron 4 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Países Bajos | 1.57 | 0.611 | 0.627 | 0.620 | -0.9 | -0.041 |
| Empate | 4.25 | 0.221 | 0.217 | 0.216 | +0.5 | -0.060 |
| Gana Grecia | 5.5 | 0.168 | 0.156 | 0.164 | +0.4 | -0.074 |
| Países Bajos o empate | 1.17 | 0.832 | 0.844 | 0.836 | -0.4 | -0.027 |
| Grecia o empate | 2.42 | 0.389 | 0.373 | 0.380 | +0.9 | -0.058 |
| No hay empate | 1.22 | 0.779 | 0.783 | 0.784 | -0.5 | -0.050 |
| 1.er tiempo: Países Bajos | 2.1 | 0.447 | 0.460 | 0.445 | +0.2 | -0.061 |
| 1.er tiempo: Empate | 2.37 | 0.386 | 0.383 | 0.390 | -0.4 | -0.086 |
| 1.er tiempo: Grecia | 5.2 | 0.168 | 0.157 | 0.165 | +0.2 | -0.129 |
| 2.º tiempo: Países Bajos | 1.85 | 0.492 | 0.501 | 0.506 | -1.4 | -0.089 |
| 2.º tiempo: Empate | 2.85 | 0.323 | 0.322 | 0.314 | +1.0 | -0.079 |
| 2.º tiempo: Grecia | 4.7 | 0.184 | 0.177 | 0.180 | +0.4 | -0.134 |
| Descanso o final: Países Bajos | 1.4 | 0.669 | 0.683 | 0.668 | +0.2 | -0.063 |
| Descanso o final: Empate | 1.87 | 0.491 | 0.485 | 0.500 | -0.9 | -0.082 |
| Descanso o final: Grecia | 3.3 | 0.269 | 0.253 | 0.283 | -1.5 | -0.114 |
| Ambos marcan: Sí | 1.67 | 0.562 | 0.570 | 0.564 | -0.1 | -0.061 |
| Ambos marcan: No | 2.1 | 0.438 | 0.430 | 0.436 | +0.1 | -0.081 |
| Descanso/final: Países Bajos / Países Bajos | 2.37 | 0.381 | 0.397 | 0.383 | -0.2 | -0.097 |
| Descanso/final: Países Bajos / Empate | 15.5 | 0.051 | 0.049 | 0.048 | +0.4 | -0.206 |
| Descanso/final: Países Bajos / Grecia | 50.0 | 0.014 | 0.013 | 0.013 | +0.1 | -0.295 |
| Descanso/final: Empate / Países Bajos | 4.3 | 0.192 | 0.195 | 0.198 | -0.6 | -0.173 |
| Descanso/final: Empate / Empate | 6.5 | 0.125 | 0.125 | 0.125 | +0.0 | -0.187 |
| Descanso/final: Empate / Grecia | 11.25 | 0.069 | 0.064 | 0.068 | +0.1 | -0.230 |
| Descanso/final: Grecia / Países Bajos | 21.0 | 0.035 | 0.033 | 0.034 | +0.1 | -0.272 |
| Descanso/final: Grecia / Empate | 16.5 | 0.045 | 0.043 | 0.044 | +0.1 | -0.253 |
| Descanso/final: Grecia / Grecia | 9.0 | 0.088 | 0.081 | 0.087 | +0.1 | -0.212 |
| Hándicap Países Bajos -4 | 18.0 | 0.025 | 0.026 | 0.029 | -0.4 | -0.556 |
| Hándicap empate (Países Bajos -4) | 11.25 | 0.046 | 0.048 | 0.051 | -0.5 | -0.483 |
| Hándicap Grecia +4 | 1.07 | 0.929 | 0.927 | 0.920 | +0.9 | -0.006 |
| Hándicap Países Bajos -3 | 9.5 | 0.070 | 0.072 | 0.077 | -0.8 | -0.340 |
| Hándicap empate (Países Bajos -3) | 7.0 | 0.107 | 0.111 | 0.110 | -0.3 | -0.253 |
| Hándicap Grecia +3 | 1.2 | 0.824 | 0.817 | 0.813 | +1.1 | -0.011 |
| Hándicap Países Bajos -2 | 4.65 | 0.176 | 0.182 | 0.186 | -1.0 | -0.183 |
| Hándicap empate (Países Bajos -2) | 4.65 | 0.185 | 0.193 | 0.186 | -0.1 | -0.140 |
| Hándicap Grecia +2 | 1.53 | 0.639 | 0.625 | 0.628 | +1.1 | -0.022 |
| Hándicap Países Bajos -1 | 2.5 | 0.361 | 0.375 | 0.373 | -1.2 | -0.098 |
| Hándicap empate (Países Bajos -1) | 3.75 | 0.246 | 0.249 | 0.241 | +0.6 | -0.075 |
| Hándicap Grecia +1 | 2.42 | 0.393 | 0.376 | 0.386 | +0.6 | -0.050 |
| Hándicap Países Bajos +1 | 1.17 | 0.831 | 0.843 | 0.834 | -0.3 | -0.028 |
| Hándicap empate (Países Bajos +1) | 6.7 | 0.115 | 0.108 | 0.111 | +0.4 | -0.228 |
| Hándicap Grecia -1 | 12.5 | 0.054 | 0.049 | 0.054 | -0.0 | -0.327 |
| Hándicap Países Bajos -1.75 | 3.0 | 0.301 | 0.312 | 0.313 | -1.3 | -0.098 |
| Hándicap Grecia +1.75 | 1.42 | 0.703 | 0.691 | 0.690 | +1.3 | -0.002 |
| Hándicap Países Bajos -1.5 | 2.52 | 0.361 | 0.376 | 0.373 | -1.2 | -0.090 |
| Hándicap Grecia +1.5 | 1.55 | 0.639 | 0.624 | 0.627 | +1.2 | -0.010 |
| Hándicap Países Bajos -1.25 | 2.22 | 0.419 | 0.434 | 0.432 | -1.3 | -0.069 |
| Hándicap Grecia +1.25 | 1.7 | 0.586 | 0.571 | 0.573 | +1.3 | -0.004 |
| Hándicap Países Bajos -0.75 | 1.72 | 0.557 | 0.573 | 0.565 | -0.8 | -0.042 |
| Hándicap Grecia +0.75 | 2.18 | 0.448 | 0.432 | 0.440 | +0.8 | -0.022 |
| Hándicap Países Bajos -0.5 | 1.57 | 0.610 | 0.626 | 0.618 | -0.9 | -0.043 |
| Hándicap Grecia +0.5 | 2.47 | 0.390 | 0.374 | 0.382 | +0.9 | -0.036 |
| Hándicap Países Bajos -0.25 | 1.42 | 0.686 | 0.701 | 0.691 | -0.5 | -0.026 |
| Hándicap Grecia +0.25 | 3.0 | 0.318 | 0.303 | 0.314 | +0.5 | -0.045 |

Diferencia máxima modelo − mercado en estas selecciones: 1.5 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
