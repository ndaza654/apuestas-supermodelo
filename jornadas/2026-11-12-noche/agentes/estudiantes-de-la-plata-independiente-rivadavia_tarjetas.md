# Tarjetas · Estudiantes de La Plata – Independiente Rivadavia (Supercopa Argentina, final) · 12-nov 18:00 Bogotá

## Enfoque de mercados
Betano ofrece tarjetas del partido (total 4.5–8.5), por equipo (0.5–4.5), 1T (1.5 y 2.5), «Ambos con 1+ / 2+ tarjetas» y «Más tarjetas que» (lados Estudiantes / empate / Rivadavia). Aquí se analiza equipo y partido; las tarjetas de jugadores las analiza el agente `jugadores`. Esperado de la ficha: Estudiantes 3.64, Rivadavia 2.36, total **6.0** (Estudiantes: 3.43 a favor / 1.86 en contra; Rivadavia: 2.86 / 3.86). Muestra: 7 + 7 + 3 directos (fuente Flashscore).

## Límites (leer primero)
- Betano cuenta en PUNTOS (amarilla 1, roja 2); Flashscore solo trae amarillas. La serie de la ficha queda POR DEBAJO de los puntos reales si hubo rojas. Afecta sobre todo a las líneas «Menos» ajustadas (un partido con roja suma 2 puntos que la serie no ve) y a «Más» de forma conservadora.
- No hay estadísticas del árbitro (solo el nombre). Cualquier mención al árbitro es hipótesis sin respaldo.
- No hay estadística por tiempo: las líneas de 1T no tienen ficha.
- «L» y «V» en las líneas de equipo: L = veces que la línea se cumplió con las tarjetas del local (o, en el total, con el total de sus partidos); V = lo mismo del visitante. En una línea de equipo (p. ej. «Estudiantes Más 0.5») L = tarjetas propias del equipo y V = tarjetas que recibe su rival, según la ficha. Cumple = ≥5 en ambos con n≥5.
- «p modelo» viene de `informes/<partido>_resultado.json` (supermodelo, con contexto «importancia alta» que sube tarjetas ×1.10); «p mercado» es la probabilidad implícita sin margen; EV = p modelo · cuota − 1, informativo, no decide. Sin alineaciones publicadas (17:35 Bogotá): todo es a nivel equipo.
- La dependencia entre equipos (si uno recibe muchas, el otro suele recibir) NO está modelada en la ficha: las cifras de «ambos con N» y «más tarjetas que» se leen por separado por equipo y son una referencia, no una probabilidad conjunta.

## Contexto (matiz, no número)
- Final de la Supercopa Argentina a partido único en cancha neutra (Córdoba); importancia alta para ambos; sin derbi; ambos descansaron 5 días. Una final suele ser más trabada y tensa, lo que tiende a más duelos y tarjetas, pero la ficha no lo cuantifica; el modelo aplicó ×1.10 por importancia (supuesto del modelo, sin verificación propia).
- Estudiantes prepara la final de la Libertadores ante Palmeiras (Flashscore): posible rotación o cuidado con amonestados; sin confirmar. Bajas según la previa: Correa y Castro (Estudiantes), Arce (Rivadavia); Betano aún trae líneas de jugadores de esos tres.
- Si hay empate a los 90 min puede haber prórroga o penales; verificar si el mercado de tarjetas se liquida a 90 min.
- Árbitro: Pérez Y. Sin estadísticas; no se usa.
- Directos (n=3, series [6-2], [4-3], [1-1] amarillas, orientación local–visitante de la ficha, sin verificar): total 9, 7 y 2. Son pocos para criterio, solo referencia.

## Líneas de tarjetas (todas las que ofrece Betano; ninguna excluida por colchón)
| Ámbito | Lado | Línea | Cuota | Esperado | Colchón | L | V | Directos | Cumple | p modelo | p mercado | EV (p·cuota−1) | Marca |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Total | Más | 4.5 | 1.33 | 6.00 | +1.50 | 4 de 7 | 5 de 7 | 2 de 3 | no | 0.64 | 0.73 | -0.15 |  |
| Total | Menos | 4.5 | 3.15 | 6.00 | -1.50 | 3 de 7 | 2 de 7 | 1 de 3 | no | 0.36 | 0.27 | +0.13 |  |
| Total | Más | 5.5 | 1.62 | 6.00 | +0.50 | 3 de 7 | 4 de 7 | 2 de 3 | no | 0.49 | 0.59 | -0.20 |  |
| Total | Menos | 5.5 | 2.22 | 6.00 | -0.50 | 4 de 7 | 3 de 7 | 1 de 3 | no | 0.51 | 0.41 | +0.12 |  |
| Total | Más | 6.5 | 2.05 | 6.00 | -0.50 | 3 de 7 | 3 de 7 | 2 de 3 | no | 0.36 | 0.45 | -0.27 |  |
| Total | Menos | 6.5 | 1.72 | 6.00 | +0.50 | 4 de 7 | 4 de 7 | 1 de 3 | no | 0.64 | 0.55 | +0.11 |  |
| Total | Más | 7.5 | 2.75 | 6.00 | -1.50 | 2 de 7 | 2 de 7 | 1 de 3 | no | 0.25 | 0.32 | -0.32 |  |
| Total | Menos | 7.5 | 1.42 | 6.00 | +1.50 | 5 de 7 | 5 de 7 | 2 de 3 | SÍ | 0.75 | 0.68 | +0.07 |  |
| Total | Más | 8.5 | 3.80 | 6.00 | -2.50 | 1 de 7 | 2 de 7 | 0 de 3 | no | 0.16 | 0.22 | -0.40 |  |
| Total | Menos | 8.5 | 1.24 | 6.00 | +2.50 | 6 de 7 | 5 de 7 | 3 de 3 | SÍ | 0.84 | 0.78 | +0.04 |  |
| Local | Más | 0.5 | 1.42 | 3.64 | +3.14 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | 0.79 | 0.67 | +0.13 |  |
| Local | Menos | 0.5 | 2.72 | 3.64 | -3.14 | 1 de 7 | 1 de 7 | 0 de 3 | no | 0.21 | 0.33 | -0.44 |  |
| Local | Más | 1.5 | 2.87 | 3.64 | +2.14 | 5 de 7 | 5 de 7 | 2 de 3 | SÍ | 0.50 | 0.31 | +0.44 |  |
| Local | Menos | 1.5 | 1.39 | 3.64 | -2.14 | 2 de 7 | 2 de 7 | 1 de 3 | no | 0.50 | 0.69 | -0.31 |  |
| Local | Más | 2.5 | 1.60 | 3.64 | +1.14 | 3 de 7 | 4 de 7 | 2 de 3 | no | 0.50 | 0.59 | -0.20 |  |
| Local | Menos | 2.5 | 2.25 | 3.64 | -1.14 | 4 de 7 | 3 de 7 | 1 de 3 | no | 0.50 | 0.41 | +0.12 |  |
| Local | Más | 3.5 | 2.45 | 3.64 | +0.14 | 3 de 7 | 3 de 7 | 2 de 3 | no | 0.29 | 0.37 | -0.29 |  |
| Local | Menos | 3.5 | 1.52 | 3.64 | -0.14 | 4 de 7 | 4 de 7 | 1 de 3 | no | 0.71 | 0.63 | +0.08 |  |
| Local | Más | 4.5 | 4.10 | 3.64 | -0.86 | 3 de 7 | 3 de 7 | 1 de 3 | no | 0.14 | 0.20 | -0.42 |  |
| Local | Menos | 4.5 | 1.21 | 3.64 | +0.86 | 4 de 7 | 4 de 7 | 2 de 3 | no | 0.86 | 0.80 | +0.04 |  |
| Visitante | Más | 0.5 | 1.38 | 2.36 | +1.86 | 5 de 7 | 7 de 7 | 3 de 3 | SÍ | 0.83 | 0.70 | +0.14 |  |
| Visitante | Menos | 0.5 | 2.92 | 2.36 | -1.86 | 2 de 7 | 0 de 7 | 0 de 3 | no | 0.17 | 0.30 | -0.49 |  |
| Visitante | Más | 1.5 | 2.65 | 2.36 | +0.86 | 3 de 7 | 6 de 7 | 2 de 3 | no | 0.56 | 0.34 | +0.49 |  |
| Visitante | Menos | 1.5 | 1.44 | 2.36 | -0.86 | 4 de 7 | 1 de 7 | 1 de 3 | no | 0.44 | 0.66 | -0.37 |  |
| Visitante | Más | 2.5 | 1.50 | 2.36 | -0.14 | 3 de 7 | 4 de 7 | 1 de 3 | no | 0.58 | 0.64 | -0.14 |  |
| Visitante | Menos | 2.5 | 2.50 | 2.36 | +0.14 | 4 de 7 | 3 de 7 | 2 de 3 | no | 0.42 | 0.36 | +0.06 |  |
| Visitante | Más | 3.5 | 2.20 | 2.36 | -1.14 | 1 de 7 | 2 de 7 | 0 de 3 | no | 0.35 | 0.42 | -0.23 |  |
| Visitante | Menos | 3.5 | 1.62 | 2.36 | +1.14 | 6 de 7 | 5 de 7 | 3 de 3 | SÍ | 0.65 | 0.58 | +0.05 |  |
| Visitante | Más | 4.5 | 3.55 | 2.36 | -2.14 | 1 de 7 | 1 de 7 | 0 de 3 | no | 0.19 | 0.24 | -0.34 |  |
| Visitante | Menos | 4.5 | 1.27 | 2.36 | +2.14 | 6 de 7 | 6 de 7 | 3 de 3 | SÍ | 0.81 | 0.76 | +0.03 |  |
| 1T | Más | 1.5 | 1.50 | — | — | — | — | — | n/a (1T: sin estadística por tiempo) | 0.56 | 0.64 | -0.16 |  |
| 1T | Menos | 1.5 | 2.47 | — | — | — | — | — | n/a (1T: sin estadística por tiempo) | 0.44 | 0.36 | +0.08 |  |
| 1T | Más | 2.5 | 2.27 | — | — | — | — | — | n/a (1T: sin estadística por tiempo) | 0.33 | 0.40 | -0.26 |  |
| 1T | Menos | 2.5 | 1.60 | — | — | — | — | — | n/a (1T: sin estadística por tiempo) | 0.67 | 0.60 | +0.08 |  |

## «Ambos con N tarjetas»
(cada equipo recibió ≥N en cuántos de sus últimos 7; los directos no entran)
| Mercado | Cuota | Esperado L / V | L (≥N) | V (≥N) | Cumple | p modelo | p mercado | EV modelo |
|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí | 1.07 ⚠ cuota<1.20 | 3.64 / 2.36 | 6 de 7 | 7 de 7 | SÍ | 0.90 | 0.92 | -0.04 |
| Ambos 1+ tarjetas: No | 7.50 | 3.64 / 2.36 | 6 de 7 | 7 de 7 | no (la serie apunta al Sí) | 0.10 | 0.08 | -0.24 |
| Ambos 2+ tarjetas: Sí | 1.37 | 3.64 / 2.36 | 5 de 7 | 6 de 7 | SÍ | 0.64 | 0.70 | -0.12 |
| Ambos 2+ tarjetas: No | 2.95 | 3.64 / 2.36 | 5 de 7 | 6 de 7 | no (la serie apunta al Sí) | 0.36 | 0.30 | +0.05 |

Producto simple de frecuencias (independencia, solo referencia): Ambos 1+ Sí ≈ 0.86, Ambos 2+ Sí ≈ 0.61. Dependencia entre equipos no modelada.

## «Más tarjetas que»
| Mercado | Cuota | Esperado L − V | Serie propia: L más / empate / menos | Serie propia: V más / empate / menos | Directos (más L / emp / más V)* | Cumple | p modelo | p mercado | EV modelo |
|---|---|---|---|---|---|---|---|---|---|
| Más tarjetas: Estudiantes | 2.50 | +1.28 | 4 / 1 / 2 de 7 | 2 / 1 / 4 de 7 | 2 / 1 / 0 de 3 | no | 0.33 | 0.37 | -0.18 |
| Más tarjetas: empate | 4.70 | +1.28 | 4 / 1 / 2 de 7 | 2 / 1 / 4 de 7 | 2 / 1 / 0 de 3 | n/a | 0.22 | 0.18 | +0.01 |
| Más tarjetas: Rivadavia | 2.07 | +1.28 | 4 / 1 / 2 de 7 | 2 / 1 / 4 de 7 | 2 / 1 / 0 de 3 | no | 0.46 | 0.45 | -0.06 |

*Orientación de los directos supuesta (local primero), no verificada. «Más / menos» de la serie propia compara tarjetas a favor y en contra de cada equipo contra SUS rivales (no entre sí). Lectura: los datos esperan más tarjetas para Estudiantes (3.64 vs 2.36), pero el mercado tiene a Rivadavia más barato (2.07 vs 2.50) y el modelo lo sigue (46 % vs 33 %). Ninguna opción cumple 5 de 7 en ambos lados.

## Alertas de coherencia (revisar antes de usar)
- Las líneas de equipo «Más 0.5» (Estudiantes 1.42, Rivadavia 1.38) implican ≈ 70 % cada una (p mercado 0.67 y 0.70), mientras «Ambos 1+ tarjetas: Sí» paga 1.07 (≈ 92 %), imposible si cada equipo fuera 70 % (la conjunta no puede superar a cada marginal). Alguna de las dos cuotas o su etiqueta no corresponde a lo que se lee: confirmar en Betano antes de apostar. La serie (6 de 7 y 7 de 7) respalda más la cuota baja del «Ambos».
- El modelo marcó «Revisar» en casi todas las tarjetas (su simulación se aleja 17–40 pts del mercado). El EV de «Rivadavia Más 1.5» (+0.56) y «Estudiantes Más 1.5» (+0.44) nace de esa brecha, no de la serie: Estudiantes cumple 5 de 7 y 5 de 7, Rivadavia 3 de 7 y 6 de 7 (no cumple).

## Líneas que cumplen (≥5 de 7 en ambos, n≥5)
Visitante Más 0.5 @1.38 (L 5/7, V 7/7) · Local Más 0.5 @1.42 (6/7, 6/7) · Total Menos 8.5 @1.24 (6/7, 5/7) · Total Menos 7.5 @1.42 (5/7, 5/7) · Visitante Menos 4.5 @1.27 (6/7, 6/7) · Visitante Menos 3.5 @1.62 (6/7, 5/7) · Local Más 1.5 @2.87 (5/7, 5/7) · Ambos 1+ Sí @1.07 (6/7, 7/7; cuota<1.20) · Ambos 2+ Sí @1.37 (5/7, 6/7).
Las «Menos» son las más expuestas a rojas no contadas (serie por debajo de los puntos): Total Menos 7.5 tiene colchón +1.5 y Menos 8.5 +2.5 en amarillas.

## Las que NO cumplen (resumen)
- Total: Más 4.5 (4/7 y 5/7), Más 5.5, Más 6.5, Más 7.5, Más 8.5, Menos 4.5, 5.5 y 6.5 (3–4 de 7 en al menos un equipo). El centro del esperado (6.0) cae justo entre 5.5 y 6.5: colchón ±0.5, sin regularidad.
- Equipo: Estudiantes Más 2.5/3.5/4.5, Menos 0.5/1.5/2.5/3.5/4.5; Rivadavia Más 1.5 (3/7), Más 2.5/3.5/4.5, Menos 0.5/1.5/2.5.
- 1T (Más/Menos 1.5 y 2.5): sin estadística por tiempo; no hay ficha.
- Ambos con N «No», y «Más tarjetas que» (los tres lados): no cumplen o contradicen la serie.
