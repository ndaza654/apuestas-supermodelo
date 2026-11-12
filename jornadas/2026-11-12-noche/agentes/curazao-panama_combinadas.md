# Combinadas · Curazao – Panamá (CONCACAF Nations League, cuartos, ida, 19:30 Bogotá)

Fuentes: agentes corners / tarjetas / goles-resultado de este partido (no hay agente `partido`: Betano no ofrece tiros ni faltas); `informes/..._resultado.json`; combinadas calculadas con `python3 -m supermodelo --combos`. Jugadores no aplica (sin alineaciones; Betano solo «anota»).

## Enfoque de mercados
Pocos mercados cumplen: córners total (solo Menos 10.5), goles totales/equipo y resultado/hándicap. Tarjetas: ninguna línea utilizable (las que cumplen son «Más 0.5» de equipo y «Ambos 1+», excluidas por cuotas incoherentes sin verificar). Por tanto no hay combinada con tarjetas.

## Advertencias arriba (leer primero)
1. **Alertas del modelo (5, de 18 a 31 pts):** 14 líneas de tarjetas y 2 de córners. Las patas que uso (Córners Menos 10.5, goles, hándicap, No hay empate) NO llevan marca; las tarjetas no se usan. La conjunta sigue siendo del simulador.
2. **Goles/resultado: el modelo copia el mercado** (g = mercado, ≤2 pts): para Goles Más 1.5, Curazao marca, No hay empate y Hándicap Curazao +2 no hay segunda opinión.
3. **El esperado de la ficha (goles 3.21) supera lo que cobra Betano (≈ 2.45):** 6-1 y 1-7 de Curazao inflan el promedio. «Goles Más 1.5» cumple 5 y 5 de 7 pero su p viene del mercado (69 %).
4. Muestra mezclada (Mundial, Nations League, Kirin Cup), 1 solo directo (2023); «Córners Menos 10.5» es la única línea de córners que cumple (6 de 7 y 6 de 7), con esperado 8.07.
5. Liquidación (90 min) no verificada en el repo; en una ida de cuartos no suele haber prórroga, pero la regla del mercado no está escrita.
6. Cuota total = producto de las individuales (techo, no el cupón). La «cuota mínima» es del modelo, no exigencia de Betano; no verificado que el builder combine estos mercados.

## Combinadas

### 1. Córners Menos 10.5 + Curazao no pierde por 2 o más (C8) — la de mayor probabilidad
| Pata | Cuota | X de 7 (Curazao / Panamá) | Directos |
|---|---|---|---|
| Córners total Menos 10.5 | 1.30 | 6 / 6 | 1 de 1 |
| Hándicap Curazao +2 | 1.26 | 5 / 6 | 1 de 1 |

- Cuota total (producto): **1.64**. p ajustada **56 %** (p_sim 55 %), justa 1.79, mínima 1.84. EV si paga el producto: **−8.4 %**.
- Correlación 1.00; esperada ~0 (córners y margen de goles no están vinculados). Stress **52 %**; pata más frágil **Córners Menos 10.5** (72 %). Margen acumulado 6 %. Guion común: empate; robustez 23 %.
- Hándicap +2 se apoya en la diferencia de goles de la ficha (Curazao no pierde por 2+ en 5 de 7; Panamá no gana por 2+ en 6 de 7), pero Curazao perdió 1-7 en la muestra: la regularidad esconde la cola.

### 2. Córners Menos 10.5 + Goles Más 1.5 (C1)
| Pata | Cuota | X de 7 (Curazao / Panamá) | Directos |
|---|---|---|---|
| Córners total Menos 10.5 | 1.30 | 6 / 6 | 1 de 1 |
| Goles total Más 1.5 | 1.39 | 5 / 5 | 1 de 1 |

- Cuota total (producto): **1.81**. p ajustada **52 %** (p_sim 49 %), justa 1.93, mínima 1.99. EV si paga el producto: **−6.4 %**.
- Correlación 1.05. Esperada: conceptualmente opuestas (pocos córners / goles), pero líneas laxas (Más 1.5 es solo ≥2 goles), casi independientes. Stress **48 %**; pata más frágil **Goles Más 1.5** (69 %). Margen 6 %. Guion común: partido abierto; robustez 28 %.
- Comparte la pata Córners Menos 10.5 con la 1: misma apuesta repetida en esa pata.

### 3. Córners Menos 10.5 + Curazao marca + Curazao +2 (C3) — 3 patas
| Pata | Cuota | X de 7 (Curazao / Panamá) | Directos |
|---|---|---|---|
| Córners total Menos 10.5 | 1.30 | 6 / 6 | 1 de 1 |
| Goles Curazao Más 0.5 | 1.50 | 5 / 6 | 1 de 1 |
| Hándicap Curazao +2 | 1.26 | 5 / 6 | 1 de 1 |

- Cuota total (producto): **2.46**. p ajustada **39 %** (p_sim 39 %), justa 2.55, mínima 2.62. EV si paga el producto: **−3.4 %**.
- Correlación 1.12 (positiva: que Curazao marque ayuda a no perder por 2). Stress **36 %**; pata más frágil **Goles Curazao Más 0.5** (62 %, 5 de 7 en Curazao). Margen 10 %. Guion común: sorpresa (gana el no favorito); robustez 0 %.
- Dos patas de Curazao (marca + no pierde por 2) son parcialmente la misma historia.

## Descartadas
- C4 (+ No hay empate): p 51 %, EV −12 %; C5 (córners + no empate + goles): 37 %; C6 (Goles Más 1.5 + Curazao +2): correlación 0.88 (se estorban), EV −17.7 %; C2 (córners + goles Más 1.5 + Curazao +2): 35 %, correlación 0.91, EV −19.8 %; C7: EV −13.8 %.
- Hándicap Panamá +2 @1.07, Goles Panamá/Curazao Menos 2.5/3.5 (cuotas < 1.20): sin sentido en combinada.
- «No hay empate» @1.33 cumple (5/7, 7/7, D 1/1), pero cualquier combinada con él cae por debajo del mínimo.

## Hándicap
Cumplen Curazao +2 @1.26 y Panamá +2 @1.07 (y Curazao +3 @1.08, cuotas bajas). Las líneas asiáticas no cumplen (2 a 5 de 7). Sin ficha de goles por tiempo.

## No pude evaluar
Cuota del cupón; si Betano permite el builder con córners + hándicap; liquidación a 90; tarjetas (sin patas utilizables); jugadores; 1T/2T (sin estadística por tiempo).
