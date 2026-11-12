# Goles y resultado · Eslovaquia - Islas Feroé · UEFA Liga de Naciones · 2026-11-13 14:45 (Bogotá)

Agente goles-resultado. Cuotas Betano leídas el Cuotas de Betano leídas 2026-11-12T17:32:25.998Z · 167 mercados. Todas las cifras salen de `fichas/ficha_eslovaquia-islas-feroe.json` (clave `goles`, `contexto`), `informes/eslovaquia-islas-feroe_resultado.json` y `betano/eslovaquia-islas-feroe.json`; nada de memoria. Horas en Bogotá.

## Enfoque de mercados
- Betano ofrece en este partido goles totales (10 líneas), de Eslovaquia (5), de Islas Feroé (2), 1T (6) y 2T (3); además 1X2, doble oportunidad (1X, X2, 12), resultado 1T y 2T, descanso o final (`htft_o`, 3 opciones), descanso/final (`htft`, 9 combinaciones), ambos marcan y 10 mercados de hándicap. Ambos marcan 1T/2T y total exacto no aparecen.
- Pesan: goles totales y por equipo (con regularidad 7+7 en la ficha) y 1X2/ambos/htft (solo modelo + mercado, sin regularidad). 1T/2T de goles: solo modelo + mercado (sin estadística por tiempo no hay ficha).
- Directos: `ficha.h2h` = None (la ficha no trae esa clave); los directos de `goles.series.directos` son n = 1 (informativos, nunca llegan a n ≥ 5).

## Alertas del modelo (leídas antes de usarlo)
- Revisar: la simulación sin contexto se aleja 25 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 34 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 38 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 52 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

- Dónde caen: corners: 4 líneas; especial: 2 líneas. Líneas de familia goles/resultado/ambos con alerta: 0.
- Brecha máxima simulación sin contexto vs mercado en goles/resultado/ambos: 2.5 pts (Descanso o final: Islas Feroé). Las alertas grandes están en otras familias (córners 1T, tarjetas, saques, «más córners»).
- Aun así NO se usa la probabilidad del modelo como argumento a favor de ninguna línea: el modelo no es independiente del mercado (`fuente_objetivos` de los goles = «mercado»; `lambdas_mercado` = 2.10 / 0.65 salen de las cuotas de Betano), y con alertas abiertas en el mismo informe se trata como señal de dato o modelo dudoso. `historial_vs_mercado` = {} (vacío: no hay contraste histórico del modelo).

### Medias de goles (informe)
| Ámbito | Modelo | Sin contexto | Betano | sd | p10–p90 |
|---|---|---|---|---|---|
| total | 2.71 | 2.72 | 2.75 | 1.6 | 1.0–5.0 |
| local | 2.06 | 2.08 | 2.1 | 1.35 | 0.0–4.0 |
| visitante | 0.65 | 0.65 | 0.66 | 0.8 | 0.0–2.0 |
| 1T | 1.24 | 1.26 | 1.19 | 1.1 | 0.0–3.0 |
| 2T | 1.47 | 1.47 | 1.58 | 1.2 | 0.0–3.0 |

## Contexto (solo matiz; tal como está en la ficha)
- Importancia: normal. Eslovaquia: motivación alta, necesita ganar False, rotación False. Islas Feroé: motivación normal, necesita ganar True, rotación False. Bajas: ninguna anotada. Dudas: ninguna.

## Goles: criterios
- Muestra (fuente: Flashscore, últimos 7 oficiales de cada selección, cualquier sede; partido completo 90 min + descuento): Eslovaquia n = 7, Islas Feroé n = 7, directos n = 1.
- Esperado = (a favor propio + concedido por el rival)/2: Eslovaquia 1.57 (a favor 1.86 · Islas Feroé concede 1.29); Islas Feroé 1.36 (a favor 1.0 · Eslovaquia concede 1.71); total 2.93.
- Series (a favor–en contra): Eslovaquia 4-0 1-1 2-1 2-0 3-4 0-6 1-0; Islas Feroé 2-2 1-1 1-1 1-1 1-0 0-1 1-3; directos (total) 2.
- Regla: cumple = ≥ 5 de 7 en ambos equipos. Asiáticas (.25/.75) cuentan solo la victoria completa; el punto medio es media ganancia/pérdida. En la columna L de una línea de equipo va lo que ese equipo marca (L) y en V lo que el rival concede; en el total, L y V son los goles totales de los partidos de cada equipo. Colchón = esperado − línea (Más) / línea − esperado (Menos).
- Columnas p mod / p mkt / EV: probabilidad del modelo, probabilidad de Betano sin margen (método potencia del informe) y EV = p mod·cuota − 1 del informe. **Solo informativas**; el modelo no es argumento (ver alertas). El EV no decide.

### Goles · Total
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.05 | 2.93 | +2.43 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.940 | 0.938 | -0.013 |
| 0.5 | Menos | 8.25 | 2.93 | -2.43 | 0 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.060 | 0.062 | -0.502 |
| 1.5 | Más | 1.27 | 2.93 | +1.43 | 6 de 7 | 5 de 7 | 1 de 1 | SÍ | sí | 0.764 | 0.762 | -0.030 |
| 1.5 | Menos | 3.55 | 2.93 | -1.43 | 1 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.236 | 0.237 | -0.161 |
| 2.25 | Más | 1.62 | 2.93 | +0.68 | 4 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.593 | 0.594 | -0.039 |
| 2.25 | Menos | 2.27 | 2.93 | -0.68 | 1 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.414 | 0.413 | -0.060 |
| 2.5 | Más | 1.8 | 2.93 | +0.43 | 4 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.517 | 0.519 | -0.070 |
| 2.5 | Menos | 1.93 | 2.93 | -0.43 | 3 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.483 | 0.481 | -0.068 |
| 2.75 | Más | 2.05 | 2.93 | +0.18 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.457 | 0.461 | -0.063 |
| 2.75 | Menos | 1.75 | 2.93 | -0.18 | 3 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.550 | 0.546 | -0.038 |
| 3 | Más | 2.4 | 2.93 | -0.07 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.384 | 0.390 | -0.080 |
| 3 | Menos | 1.55 | 2.93 | +0.07 | 3 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.631 | 0.624 | -0.022 |
| 3.25 | Más | 2.7 | 2.93 | -0.32 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.331 | 0.339 | -0.106 |
| 3.25 | Menos | 1.45 | 2.93 | +0.32 | 3 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.676 | 0.667 | -0.020 |
| 3.5 | Más | 2.95 | 2.93 | -0.57 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | 0.288 | 0.297 | -0.150 |
| 3.5 | Menos | 1.37 | 2.93 | +0.57 | 4 de 7 | 5 de 7 | 1 de 1 | no | sí | 0.712 | 0.703 | -0.025 |
| 4.5 | Más | 5.2 | 2.93 | -1.57 | 2 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.136 | 0.143 | -0.291 |
| 4.5 | Menos | 1.14 | 2.93 | +1.57 | 5 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.864 | 0.857 | -0.015 |
| 5.5 | Más | 8.5 | 2.93 | -2.57 | 2 de 7 | 0 de 7 | 0 de 1 | no | sí | 0.056 | 0.062 | -0.522 |
| 5.5 | Menos | 1.05 | 2.93 | +2.57 | 5 de 7 | 7 de 7 | 1 de 1 | SÍ | no | 0.944 | 0.938 | -0.009 |

### Goles · Eslovaquia (local)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.11 | 1.57 | +1.07 | 6 de 7 | 6 de 7 | 1 de 1* | SÍ | no | 0.886 | 0.882 | -0.017 |
| 0.5 | Menos | 5.9 | 1.57 | -1.07 | 1 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.114 | 0.118 | -0.327 |
| 1.5 | Más | 1.53 | 1.57 | +0.07 | 4 de 7 | 2 de 7 | 0 de 1* | no | sí | 0.624 | 0.623 | -0.046 |
| 1.5 | Menos | 2.4 | 1.57 | -0.07 | 3 de 7 | 5 de 7 | 1 de 1* | no | sí | 0.377 | 0.377 | -0.096 |
| 2.5 | Más | 2.57 | 1.57 | -0.93 | 2 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.342 | 0.349 | -0.122 |
| 2.5 | Menos | 1.47 | 1.57 | +0.93 | 5 de 7 | 6 de 7 | 1 de 1* | SÍ | sí | 0.658 | 0.651 | -0.032 |
| 3.5 | Más | 4.85 | 1.57 | -1.93 | 1 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.150 | 0.159 | -0.273 |
| 3.5 | Menos | 1.16 | 1.57 | +1.93 | 6 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.850 | 0.841 | -0.014 |
| 4.5 | Más | 8.75 | 1.57 | -2.93 | 0 de 7 | 0 de 7 | 0 de 1* | no | sí | 0.053 | 0.061 | -0.539 |
| 4.5 | Menos | 1.05 | 1.57 | +2.93 | 7 de 7 | 7 de 7 | 1 de 1* | SÍ | no | 0.947 | 0.939 | -0.005 |

### Goles · Islas Feroé (visitante)
| Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | cuota ≥ 1.20 | p mod | p mkt | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | Más | 1.93 | 1.36 | +0.86 | 4 de 7 | 6 de 7 | 1 de 1* | no | sí | 0.482 | 0.481 | -0.069 |
| 0.5 | Menos | 1.8 | 1.36 | -0.86 | 3 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.518 | 0.519 | -0.068 |
| 1.5 | Más | 5.3 | 1.36 | -0.14 | 2 de 7 | 1 de 7 | 0 de 1* | no | sí | 0.143 | 0.142 | -0.239 |
| 1.5 | Menos | 1.14 | 1.36 | +0.14 | 5 de 7 | 6 de 7 | 1 de 1* | SÍ | no | 0.857 | 0.858 | -0.024 |

\* Directos de líneas por equipo: la ficha no indica si la serie de directos está orientada local/visitante; léase con cautela (n ≤ 3, informativo; el directo nunca decide el «cumple»).

### Goles · 1T y 2T (solo modelo + mercado; sin estadística de goles por tiempo no hay ficha ni regularidad)
| Ámbito | Línea | Lado | Cuota | p mod | p mkt | EV |
|---|---|---|---|---|---|---|
| 1T | 0.5 | Más | 1.39 | 0.701 | 0.692 | -0.025 |
| 1T | 0.5 | Menos | 2.87 | 0.299 | 0.308 | -0.143 |
| 1T | 0.75 | Más | 1.53 | 0.640 | 0.631 | -0.021 |
| 1T | 0.75 | Menos | 2.45 | 0.371 | 0.380 | -0.091 |
| 1T | 1 | Más | 1.82 | 0.540 | 0.530 | -0.018 |
| 1T | 1 | Menos | 1.95 | 0.483 | 0.493 | -0.059 |
| 1T | 1.25 | Más | 2.27 | 0.423 | 0.415 | -0.039 |
| 1T | 1.25 | Menos | 1.62 | 0.587 | 0.596 | -0.049 |
| 1T | 1.5 | Más | 2.67 | 0.344 | 0.334 | -0.083 |
| 1T | 1.5 | Menos | 1.44 | 0.656 | 0.666 | -0.055 |
| 1T | 2.5 | Más | 5.9 | 0.122 | 0.118 | -0.282 |
| 1T | 2.5 | Menos | 1.11 | 0.878 | 0.882 | -0.025 |
| 2T | 0.5 | Más | 1.23 | 0.788 | 0.793 | -0.031 |
| 2T | 0.5 | Menos | 4.1 | 0.212 | 0.207 | -0.130 |
| 2T | 1.5 | Más | 2.0 | 0.451 | 0.468 | -0.098 |
| 2T | 1.5 | Menos | 1.78 | 0.549 | 0.532 | -0.023 |
| 2T | 2.5 | Más | 4.0 | 0.194 | 0.209 | -0.224 |
| 2T | 2.5 | Menos | 1.23 | 0.806 | 0.791 | -0.009 |

Comprobación: Betano trae 26 líneas de goles; la ficha trae 26 (todas incluidas arriba, sin excluir ninguna por colchón).
Verificación: recalculé X de n de cada línea desde `goles.series` (con la regla asiática de victoria completa) y coincide con la ficha en todas las líneas total/local/visitante.

## Resultado, doble oportunidad, descanso/final y ambos marcan (SOLO modelo + mercado; la ficha no trae regularidad para esto, nada aquí es «cumple»)
1X2 (cuotas Betano 1.38 / 4.7 / 9.0; margen 4.9%):
| | Cuota | p modelo (`p_resultado`) | p Betano sin margen (potencia) | p Betano proporcional | modelo − mercado (pts) |
|---|---|---|---|---|---|
| Eslovaquia | 1.38 | 0.719 | 0.710 | 0.691 | +0.9 |
| Empate | 4.7 | 0.190 | 0.193 | 0.203 | -0.3 |
| Islas Feroé | 9.0 | 0.091 | 0.097 | 0.106 | -0.6 |

Regularidad de «ganó / no perdió / marcó»: la ficha **no la trae**. Como dato descriptivo derivado por mí de `goles.series` (no es criterio de la ficha, no marca «cumple»; sin ajustar por nivel de rivales):
- Eslovaquia: ganó 4 de 7, no perdió 5 de 7, marcó 6 de 7, dejó la portería a cero 3 de 7, ambos marcaron 3 de 7.
- Islas Feroé: ganó 1 de 7, no perdió 5 de 7, marcó 6 de 7, dejó la portería a cero 1 de 7, ambos marcaron 5 de 7.

Todas las selecciones del informe (familias resultado y ambos): cuota, p modelo, p mercado sin margen (potencia, como en el informe), p modelo sin contexto, diferencia modelo − mercado y EV del informe. EV no decide; p modelo no es argumento.

| Selección | Cuota | p mod | p sin contexto | p mkt | mod − mkt (pts) | EV |
|---|---|---|---|---|---|---|
| Gana Eslovaquia | 1.38 | 0.713 | 0.716 | 0.710 | +0.3 | -0.016 |
| Empate | 4.7 | 0.192 | 0.192 | 0.193 | -0.2 | -0.100 |
| Gana Islas Feroé | 9.0 | 0.096 | 0.092 | 0.097 | -0.1 | -0.139 |
| Eslovaquia o empate | 1.09 | 0.904 | 0.908 | 0.903 | +0.1 | -0.014 |
| Islas Feroé o empate | 3.2 | 0.287 | 0.284 | 0.290 | -0.3 | -0.081 |
| No hay empate | 1.19 | 0.808 | 0.808 | 0.807 | +0.2 | -0.038 |
| 1.er tiempo: Eslovaquia | 1.87 | 0.513 | 0.514 | 0.497 | +1.6 | -0.041 |
| 1.er tiempo: Empate | 2.3 | 0.386 | 0.382 | 0.394 | -0.9 | -0.113 |
| 1.er tiempo: Islas Feroé | 7.3 | 0.102 | 0.104 | 0.109 | -0.7 | -0.259 |
| 2.º tiempo: Eslovaquia | 1.65 | 0.557 | 0.562 | 0.574 | -1.7 | -0.082 |
| 2.º tiempo: Empate | 2.85 | 0.322 | 0.325 | 0.313 | +0.9 | -0.082 |
| 2.º tiempo: Islas Feroé | 7.1 | 0.121 | 0.113 | 0.114 | +0.7 | -0.140 |
| Descanso o final: Eslovaquia | 1.28 | 0.746 | 0.748 | 0.730 | +1.6 | -0.045 |
| Descanso o final: Empate | 1.93 | 0.465 | 0.461 | 0.484 | -2.0 | -0.103 |
| Descanso o final: Islas Feroé | 4.85 | 0.172 | 0.168 | 0.193 | -2.1 | -0.168 |
| Ambos marcan: Sí | 2.12 | 0.431 | 0.430 | 0.430 | +0.1 | -0.086 |
| Ambos marcan: No | 1.65 | 0.569 | 0.570 | 0.570 | -0.1 | -0.061 |
| Descanso/final: Eslovaquia / Eslovaquia | 2.0 | 0.471 | 0.473 | 0.459 | +1.2 | -0.058 |
| Descanso/final: Eslovaquia / Empate | 21.0 | 0.035 | 0.035 | 0.033 | +0.3 | -0.254 |
| Descanso/final: Eslovaquia / Islas Feroé | 90.0 | 0.007 | 0.006 | 0.006 | +0.1 | -0.370 |
| Descanso/final: Empate / Eslovaquia | 3.75 | 0.217 | 0.218 | 0.226 | -1.0 | -0.188 |
| Descanso/final: Empate / Empate | 6.3 | 0.124 | 0.124 | 0.126 | -0.3 | -0.220 |
| Descanso/final: Empate / Islas Feroé | 16.5 | 0.046 | 0.040 | 0.043 | +0.3 | -0.248 |
| Descanso/final: Islas Feroé / Eslovaquia | 24.0 | 0.027 | 0.027 | 0.028 | -0.1 | -0.354 |
| Descanso/final: Islas Feroé / Empate | 21.0 | 0.031 | 0.032 | 0.033 | -0.1 | -0.341 |
| Descanso/final: Islas Feroé / Islas Feroé | 15.5 | 0.042 | 0.045 | 0.046 | -0.4 | -0.344 |
| Hándicap Eslovaquia -4 | 16.5 | 0.032 | 0.034 | 0.038 | -0.6 | -0.471 |
| Hándicap empate (Eslovaquia -4) | 10.25 | 0.064 | 0.062 | 0.067 | -0.3 | -0.347 |
| Hándicap Islas Feroé +4 | 1.1 | 0.904 | 0.903 | 0.895 | +0.9 | -0.005 |
| Hándicap Eslovaquia -3 | 7.8 | 0.095 | 0.096 | 0.103 | -0.8 | -0.260 |
| Hándicap empate (Eslovaquia -3) | 6.1 | 0.136 | 0.137 | 0.136 | +0.1 | -0.169 |
| Hándicap Islas Feroé +3 | 1.28 | 0.769 | 0.767 | 0.761 | +0.8 | -0.016 |
| Hándicap Eslovaquia -2 | 3.8 | 0.232 | 0.233 | 0.241 | -0.9 | -0.118 |
| Hándicap empate (Eslovaquia -2) | 4.15 | 0.222 | 0.226 | 0.219 | +0.3 | -0.080 |
| Hándicap Islas Feroé +2 | 1.78 | 0.546 | 0.541 | 0.540 | +0.6 | -0.028 |
| Hándicap Eslovaquia -1 | 2.07 | 0.453 | 0.459 | 0.459 | -0.5 | -0.061 |
| Hándicap empate (Eslovaquia -1) | 3.6 | 0.261 | 0.259 | 0.254 | +0.7 | -0.062 |
| Hándicap Islas Feroé +1 | 3.2 | 0.286 | 0.283 | 0.288 | -0.2 | -0.085 |
| Hándicap Eslovaquia +1 | 1.09 | 0.904 | 0.908 | 0.903 | +0.1 | -0.015 |
| Hándicap empate (Eslovaquia +1) | 9.0 | 0.075 | 0.071 | 0.074 | +0.1 | -0.327 |
| Hándicap Islas Feroé -1 | 24.0 | 0.021 | 0.021 | 0.023 | -0.2 | -0.494 |
| Hándicap Eslovaquia -1.75 | 2.35 | 0.389 | 0.393 | 0.395 | -0.6 | -0.085 |
| Hándicap Islas Feroé +1.75 | 1.57 | 0.618 | 0.614 | 0.612 | +0.6 | -0.030 |
| Hándicap Eslovaquia -1.5 | 2.05 | 0.453 | 0.458 | 0.457 | -0.4 | -0.072 |
| Hándicap Islas Feroé +1.5 | 1.75 | 0.547 | 0.542 | 0.543 | +0.4 | -0.042 |
| Hándicap Eslovaquia -1.25 | 1.8 | 0.526 | 0.531 | 0.530 | -0.4 | -0.053 |
| Hándicap Islas Feroé +1.25 | 1.98 | 0.482 | 0.477 | 0.478 | +0.4 | -0.046 |
| Hándicap Eslovaquia -0.75 | 1.44 | 0.674 | 0.678 | 0.673 | +0.1 | -0.029 |
| Hándicap Islas Feroé +0.75 | 2.75 | 0.334 | 0.330 | 0.334 | -0.1 | -0.083 |

Diferencia máxima modelo − mercado en estas selecciones: 2.1 pts. Ninguna selección de resultado/ambos lleva `alerta` en el informe, pero el informe sí tiene las alertas listadas arriba; además el modelo está anclado a las cuotas, así que coincidir con el mercado no es confirmación independiente.

## Límites
- Muestra de 7 por equipo (rivales de distinto nivel, sin ajuste); 4 de 7 se muestra y no cumple. La regularidad no es una probabilidad calibrada.
- Goles por tiempo: no hay estadística; 1T/2T solo modelo + mercado.
- Directos: n ≤ 3, orientación local/visitante no verificada en líneas por equipo.
- 1X2, doble oportunidad, htft, ambos marcan, hándicap: solo modelo + mercado.
- Cuotas leídas el 12-nov ~12:32 Bogotá: relee antes de apostar. El usuario decide.
