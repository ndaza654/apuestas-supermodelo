# Prueba de tu estrategia (cuota ~1,50 + regularidad + colchón) contra los resultados reales
**Entrega:** dom 15-nov-2026, ~01:20 Bogotá. **Datos:** `registro/lineas.csv`, 3.868 líneas de equipo con resultado de tres jornadas (12-nov noche, 13 y 14-nov); cuotas de Betano de cada jornada (hora en el CSV). Muestra de 7 partidos (no de 10): 5 de 7 ≈ 7 de 10 y 6 de 7 ≈ 8 de 10.

**Límites:** solo 3 jornadas y líneas de equipo (jugadores no evaluados); las líneas de un mismo partido se parecen entre sí, así que los datos efectivos son ~27 partidos, no 83 líneas; no tengo tus boletos del 13 y 14-nov, así que no puedo comprobar lo de «falló por una sola pata».

## Resultados (cuotas 1,40–1,65)
| Grupo | Líneas | Acierta | Lo que decía la cuota | ROI plano |
|---|---|---|---|---|
| Todas las de cuota ~1,50 | 583 | 62,6 % | 65,8 % | −5,0 % |
| Regularidad ≥5 de 7 en ambos (≈7 de 10) | 83 | 69,9 % | 66,3 % | +5,3 % |
| Regularidad ≥6 de 7 (≈8 de 10) | 25 | 80,0 % | 66,8 % | +20 % (muestra muy chica) |
| No cumple regularidad | 308 | 61,4 % | 65,6 % | −6,4 % |
| Colchón negativo | 79 | 51,9 % | 65,0 % | −19,9 % |
| Colchón ≥10 % de la línea | 233 | ~65 % | ~66 % | +0,3 % |
| Cumple Y colchón ≥10 % | 78 | 70,5 % | 66,4 % | +6,0 % |
| No cumple pero colchón ≥10 % | 155 | 64,5 % | 66,2 % | −2,5 % |
| No cumple y colchón <10 % | 153 | 58,2 % | 65,0 % | −10,3 % |

Por mercado (cuota 1,40–1,65): goles −8 %, córners −2 %, tarjetas +0,5 %, remates −3 %, tiros al arco −7 %. Por jornada, «cumple 5 de 7»: −19 % (12-nov), −20 % (13-nov), +19 % (14-nov); IC95 por partido de −16 % a +22 %.

## Lectura
1. Lo más claro: no apostar con colchón negativo (pierde 20 %).
2. Cumplir regularidad ayuda, pero no está probado: toda la ventaja viene del 14-nov.
3. Más colchón no mejora: 5–10 % acierta 68 %, 10–20 % 65 %, >20 % 68 %.
4. «No cumple pero con colchón» queda en tablas (−2,5 %); es mejor que no tener ninguno (−10 %), no una ventaja.
5. La cuota ~1,50 por sí sola no es filtro: pierde lo que cobra la casa de margen.
6. Combinadas: con patas de ~70 %, de 5 patas pierdes 83 % de las veces y en ~43 % de las perdidas falla una sola pata; con 8 patas, ~21 %. Fallar por una pata es lo normal, no mejora.
