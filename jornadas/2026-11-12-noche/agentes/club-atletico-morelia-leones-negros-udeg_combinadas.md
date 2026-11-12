# Combinadas · Atlético Morelia – Leones Negros UdeG (Liga de Expansión MX, semifinal, ida, 21:00 Bogotá)

Fuentes: agentes corners / tarjetas / goles-resultado de este partido (no hay agente `partido` ni jugadores: Betano no ofrece); `informes/..._resultado.json` (sin alertas); combinadas calculadas con `python3 -m supermodelo --combos`.

## Enfoque de mercados
Solo goles y resultado. Córners: **ninguna línea cumple** (Más 10.5: 4 y 2; Menos 10.5: 3 y 5), no hay tarjetas ni tiros ni jugadores. Por eso todas las patas son de goles/resultado.

## Advertencias arriba (leer primero)
1. **Todo es goles/resultado: el modelo copia el mercado** (g = mercado, ≤2 pts; informe sin alertas). Las probabilidades conjuntas son el mercado más la dependencia medida; no hay segunda opinión.
2. Mercados poco distintos entre sí (Goles total, Goles de un equipo, No hay empate): las patas se solapan; evité escalones del mismo mercado (Menos 3.5 con Más 1.5 es una banda del total: descartada).
3. La muestra mezcla fase regular y cuartos de liguilla; liga base del modelo es Liga MX, no Expansión.
4. Liquidación a 90 min no verificada (ida de semifinal).
5. Cuota total = producto de las individuales (techo, no el cupón). La «cuota mínima» es del modelo. No verificado que el builder de Betano combine «No hay empate» con goles.

## Combinadas

### 1. Goles Menos 3.5 + No hay empate (M2) — la de mayor probabilidad
| Pata | Cuota | X de 7 (Morelia / Leones) | Directos |
|---|---|---|---|
| Goles total Menos 3.5 | 1.30 | 6 / 5 | 6 de 7 |
| No hay empate | 1.25 | 5 / 6 | 7 de 7 |

- Cuota total (producto): **1.62**. p ajustada **56 %** (p_sim 56 %), justa 1.78, mínima 1.84. EV si paga el producto: **−9.1 %**.
- Correlación 0.99; esperada ~0 (ligeramente negativa: los empates con goles quedan fuera de las dos). Stress **52 %**; pata más frágil **No hay empate** (75 %). Margen acumulado 11 %. Guion común: favorito gana en partido trabado; robustez 0 %.
- Menos 3.5 tiene colchón +0.36 sobre el esperado 3.14 (casi nada) y el esperado de la ficha supera al de Betano.

### 2. Goles Más 1.5 + Leones marcan (M6) — OJO: patas casi redundantes
| Pata | Cuota | X de 7 (Morelia / Leones) | Directos |
|---|---|---|---|
| Goles total Más 1.5 | 1.31 | 7 / 6 | 7 de 7 |
| Goles Leones Más 0.5 | 1.57 | 7 / 6 | 5 de 7 |

- Cuota total (producto): **2.06**. p ajustada **52 %** (p_sim 52 %), justa 1.94, mínima 2.00. EV si paga el producto: **+6.2 %**.
- Correlación 1.24 (positiva fuerte). Si Leones marca, hay ≥2 goles en ~89 % de los casos: es casi «Leones marca» con una pata de relleno. Por eso el EV aparente con producto es un artefacto de multiplicar cuotas de patas dependientes; si el cupón aplica la dependencia pagará menos que 2.06. No lo trates como dos patas independientes.
- Stress **47 %**; pata más frágil **Goles Leones Más 0.5** (58 %). Margen 10 %. Guion común: partido abierto; robustez 0 %.

### 3. Goles Más 1.5 + No hay empate (M4) — comparte pata con la 1
| Pata | Cuota | X de 7 | Directos |
|---|---|---|---|
| Goles total Más 1.5 | 1.31 | 7 / 6 | 7 de 7 |
| No hay empate | 1.25 | 5 / 6 | 7 de 7 |

- Producto **1.64**. p ajustada **54 %** (p_sim 54 %), justa 1.86, mínima 1.91. EV si paga el producto: **−11.6 %**. Correlación 1.01. Stress **50 %**; pata más frágil **Goles Más 1.5** (71 %). Margen 11 %.
- Compartiendo «No hay empate» con la 1, las dos juntas se mueven con la misma pata.

## Descartadas
- Menos 3.5 + Leones marcan (M1): correlación 0.83 (se estorban), p 37 %; Menos 3.5 + Ambos marcan Sí (M3): 28 %, corr 0.77; tres patas (Menos 3.5 + No empate + Leones marcan): 25 %; Menos 3.5 + Más 1.5: banda del mismo mercado.
- Ambos marcan Sí @1.85 cumple (7 y 5 de 7) pero directos 2 de 7 y su p es del mercado (48 %).
- Los dos builders del informe (Gana Morelia + Hándicap −0.5; + Goles 1T Menos 2.5) llevan patas que no cumplen (Gana Morelia 3 y 2 de 7) y son la misma apuesta (hándicap −0.5 = gana).

## Hándicap
Ninguna línea de hándicap cumple (Leones +0.5/+0.75/+1: 4 y 5 de 7; Morelia −0.5/−0.75/−1: 0 a 3 de 7). Sin ficha de goles por tiempo.

## No pude evaluar
Cuota del cupón; si el builder admite estas patas; liquidación a 90; córners (no cumple), tarjetas, tiros, jugadores (Betano no los ofrece); 1T/2T.
