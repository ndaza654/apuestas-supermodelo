# Local FC - Visitante SC
Liga de ejemplo · 2026-11-15 15:00

**Tipo de partido:** Favorito leve · medio · caliente · **Favorito:** Local FC · primer gol: local 60 %, visitante 32 %, nadie 7 % · gol del favorito antes del 35′: 37 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?)

## Guiones del partido
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 29 % |
| Sorpresa: gana el no favorito | 18 % |
| Empate | 17 % |
| Favorito gana en partido trabado | 13 % |
| Favorito golpea temprano y gana | 12 % |
| Expulsión antes del 70′ | 11 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro Árbitro X: 5.6 tarjetas/partido contra 4.7 de la liga (ficha) en 11 partidos → tarjetas ×1.06 (encogido por muestra).
- Lluvia fuerte: goles ×1,04 y córners ×1,03 (meses lluviosos dan más goles y córners).
- local ataca por bandas y centros: más córners propios.
- local de posesión: sigue atacando aunque gane (sensibilidad ×0,85); el rival le hace más faltas.
- Estilo de local a media fuerza (ya está en sus promedios y en el precio).
- local sin 1 defensa(s) clave: goles del rival ×1.06.
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- visitante en bloque bajo: el rival saca más córners y remata más, pero menos al arco.
- visitante juega al contragolpe: cuando gana se repliega más (sensibilidad ×1,2).
- Estilo de visitante a media fuerza (ya está en sus promedios y en el precio).
- visitante se encierra al ir ganando (sensibilidad ×1,5).
- visitante sin 1 atacante(s) clave: goles ×0.92.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.62 | 15.6 | 4.8 | 6.5 | 12.4 | 2.4 |
| visitante | 0.95 | 9.7 | 3.5 | 3.7 | 13.9 | 2.6 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.6 (2.6) · 1–5 | 1.6 (1.5) · 0–3 | 1.0 (0.9) · 0–2 | 1.1 (1.2) · 0–3 | 1.4 · 0–3 |
| Córners | 10.3 (9.5) · 6–15 | 6.6 (6.0) · 3–11 | 3.7 (3.8) · 1–7 | 4.6 · 2–8 | 5.7 · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 4.9 (4.5) · 2–8 | 2.3 · 1–4 | 2.6 (2.4) · 1–5 | 1.6 · 0–3 | 3.3 · 1–6 |
| Remates | 25.4 (25.0) · 18–33 | 15.6 (14.9) · 10–22 | 9.8 (10.6) · 5–15 | 11.2 · 7–16 | 14.1 · 9–19 |
| Tiros al arco | 8.4 (8.5) · 5–12 | 4.9 (5.0) · 2–8 | 3.5 · 1–6 | 3.7 · 1–6 | 4.7 · 2–8 |
| Faltas | 26.4 (24.8) · 20–33 | 12.4 · 8–17 | 13.9 (12.9) · 9–19 | 11.8 · 7–16 | 14.6 · 10–20 |
| Fueras de lugar | 3.7 (3.5) · 1–6 | 1.8 · 0–4 | 1.9 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.2 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 39.9 · 29–52 | 19.9 · 12–28 | 20.0 · 12–28 | 17.8 · 11–24 | 22.1 · 15–30 |
| Atajadas del portero | — | 2.6 · 0–5 | 3.2 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 3.5 | 1.30 | 74 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (35 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.95 | 51 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa |
| Resultado y hándicap | Gana Local FC | 1.85 | 53 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Sorpresa: gana el no favorito (0 %) | Justa |
| Córners | Córners Más 8.5 | 1.62 | 66 % | 62 % | Partido abierto (ambos marcan y 3+ goles) (69 %) | Sorpresa: gana el no favorito (62 %) | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Tarjetas | Tarjetas Más 3.5 | 1.50 | 69 % | 60 % | Expulsión antes del 70′ (98 %) | Favorito golpea temprano y gana (60 %) | Alta probabilidad · Contexto a favor (+6 pts) · Valor |
| Faltas | Faltas Más 24.5 | 1.85 | 63 % | 61 % | Expulsión antes del 70′ (69 %) | Partido abierto (ambos marcan y 3+ goles) (61 %) | Contexto a favor (+11 pts) · Valor · ⚠ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |
| Remates | Remates Visitante SC Menos 10.5 | 1.80 | 62 % | 50 % | Empate (71 %) | Partido abierto (ambos marcan y 3+ goles) (50 %) | Contexto a favor (+10 pts) · Valor |
| Tiros al arco | Tiros al arco Menos 8.5 | 1.80 | 54 % | 30 % | Empate (72 %) | Partido abierto (ambos marcan y 3+ goles) (30 %) | Justa |
| Fueras de lugar | Fueras de lugar Más 3.5 | 2.05 | 49 % | 48 % | Favorito golpea temprano y gana (52 %) | Empate (48 %) | Contexto a favor (+5 pts) |
| Jugadores | Portero Visitante atajadas 2+ | 1.45 | 66 % | 66 % | Empate (67 %) | Expulsión antes del 70′ (65 %) | Alta probabilidad |
| Quién saca más | Más corners: Local FC | 1.45 | 72 % | 62 % | Sorpresa: gana el no favorito (80 %) | Favorito golpea temprano y gana (62 %) | Alta probabilidad · Contexto a favor (+7 pts) · Valor |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Goles Menos 3.5 | 1.30 | 74 % | 75 % | 74 % | -0 pts | -4 % | 74 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Más 1.5 | 1.30 | 73 % | 75 % | 74 % | -1 pts | -5 % | 73 % | +0.7 | 1.41 | Favorito gana en partido trabado | Alta probabilidad |
| Más corners: Local FC | 1.45 | 72 % | 65 % | 65 % | +7 pts | +4 % | 62 % | — | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+7 pts) · Valor |
| Volante Visitante entradas 1+ | 1.25 | 70 % | 71 % | 70 % | +0 pts | -12 % | 67 % | — | 1.46 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas Más 3.5 | 1.50 | 69 % | 64 % | 63 % | +6 pts | +4 % | 60 % | +0.6 | 1.49 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+6 pts) · Valor |
| Goles 1.er tiempo Más 0.5 | 1.40 | 68 % | 69 % | 69 % | -1 pts | -5 % | 68 % | +0.6 | 1.52 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Portero Visitante atajadas 2+ | 1.45 | 66 % | 62 % | 67 % | -1 pts | -4 % | 66 % | +0.8 | 1.55 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Más 8.5 | 1.62 | 66 % | 58 % | 61 % | +5 pts | +7 % | 62 % | +0.5 | 1.57 | Sorpresa: gana el no favorito | Alta probabilidad · Contexto a favor (+5 pts) · Valor |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Faltas Más 24.5 | 1.85 | 63 % | 51 % | 51 % | +11 pts | +16 % | 61 % | +0.4 | 1.65 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+11 pts) · Valor · ⚠ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |
| Faltas Visitante SC Más 12.5 | 1.80 | 63 % | 52 % | 52 % | +11 pts | +14 % | 58 % | +0.4 | 1.63 | Favorito golpea temprano y gana | Contexto a favor (+11 pts) · Valor · ⚠ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |
| Remates Visitante SC Menos 10.5 | 1.80 | 62 % | 52 % | 52 % | +10 pts | +11 % | 50 % | +0.2 | 1.67 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+10 pts) · Valor |
| Córners Local FC Más 5.5 | 1.80 | 61 % | 52 % | 52 % | +9 pts | +9 % | 52 % | +0.3 | 1.71 | Favorito golpea temprano y gana | Contexto a favor (+9 pts) · Valor |
| Tarjetas Más 4.5 | 2.05 | 52 % | 45 % | 45 % | +7 pts | +7 % | 42 % | +0.2 | 1.99 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Más corners: Local FC | 1.45 | 72 % | 65 % | 65 % | +7 pts | +4 % | 62 % | — | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+7 pts) · Valor |
| Remates Local FC Más 14.5 | 1.85 | 57 % | 51 % | 50 % | +6 pts | +5 % | 53 % | +0.2 | 1.83 | Expulsión antes del 70′ | Contexto a favor (+6 pts) · Valor · Historial propio en contra (remates mas: 2/7 contra 50 % del precio) |
| Tarjetas Visitante SC Más 2.5 | 2.20 | 47 % | 42 % | 41 % | +6 pts | +4 % | 38 % | +0.1 | 2.20 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) |
| Córners Más 9.5 | 1.95 | 55 % | 48 % | 49 % | +6 pts | +8 % | 52 % | +0.2 | 1.88 | Sorpresa: gana el no favorito | Contexto a favor (+6 pts) · Valor |
| Tarjetas Más 3.5 | 1.50 | 69 % | 64 % | 63 % | +6 pts | +4 % | 60 % | +0.6 | 1.49 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+6 pts) · Valor |
| Córners Más 10.5 | 2.45 | 44 % | 37 % | 38 % | +6 pts | +8 % | 40 % | -0.1 | 2.38 | Sorpresa: gana el no favorito | Contexto a favor (+6 pts) · Valor |
| Ambos 2+ tarjetas: Sí | 2.40 | 49 % | 38 % | 43 % | +6 pts | +17 % | 41 % | — | 2.15 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor |
| Córners Más 8.5 | 1.62 | 66 % | 58 % | 61 % | +5 pts | +7 % | 62 % | +0.5 | 1.57 | Sorpresa: gana el no favorito | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Fueras de lugar Más 3.5 | 2.05 | 49 % | 45 % | 45 % | +5 pts | +1 % | 48 % | +0.1 | 2.11 | Empate | Contexto a favor (+5 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ambos 2+ tarjetas: Sí | 2.40 | 49 % | 38 % | 43 % | +6 pts | +17 % | 41 % | — | 2.15 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor |
| Faltas Más 24.5 | 1.85 | 63 % | 51 % | 51 % | +11 pts | +16 % | 61 % | +0.4 | 1.65 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+11 pts) · Valor · ⚠ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |
| Faltas Visitante SC Más 12.5 | 1.80 | 63 % | 52 % | 52 % | +11 pts | +14 % | 58 % | +0.4 | 1.63 | Favorito golpea temprano y gana | Contexto a favor (+11 pts) · Valor · ⚠ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |
| Remates Visitante SC Menos 10.5 | 1.80 | 62 % | 52 % | 52 % | +10 pts | +11 % | 50 % | +0.2 | 1.67 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+10 pts) · Valor |
| Córners Local FC Más 5.5 | 1.80 | 61 % | 52 % | 52 % | +9 pts | +9 % | 52 % | +0.3 | 1.71 | Favorito golpea temprano y gana | Contexto a favor (+9 pts) · Valor |
| Córners Más 10.5 | 2.45 | 44 % | 37 % | 38 % | +6 pts | +8 % | 40 % | -0.1 | 2.38 | Sorpresa: gana el no favorito | Contexto a favor (+6 pts) · Valor |
| Córners Más 9.5 | 1.95 | 55 % | 48 % | 49 % | +6 pts | +8 % | 52 % | +0.2 | 1.88 | Sorpresa: gana el no favorito | Contexto a favor (+6 pts) · Valor |
| Tarjetas Más 4.5 | 2.05 | 52 % | 45 % | 45 % | +7 pts | +7 % | 42 % | +0.2 | 1.99 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Córners Más 8.5 | 1.62 | 66 % | 58 % | 61 % | +5 pts | +7 % | 62 % | +0.5 | 1.57 | Sorpresa: gana el no favorito | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Remates Local FC Más 14.5 | 1.85 | 57 % | 51 % | 50 % | +6 pts | +5 % | 53 % | +0.2 | 1.83 | Expulsión antes del 70′ | Contexto a favor (+6 pts) · Valor · Historial propio en contra (remates mas: 2/7 contra 50 % del precio) |
| Más corners: Local FC | 1.45 | 72 % | 65 % | 65 % | +7 pts | +4 % | 62 % | — | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+7 pts) · Valor |
| Tarjetas Más 3.5 | 1.50 | 69 % | 64 % | 63 % | +6 pts | +4 % | 60 % | +0.6 | 1.49 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+6 pts) · Valor |

Kelly ¼ (dato informativo, no una orden de stake): Ambos 2+ tarjetas: Sí 2.9 % de la banca; Faltas Más 24.5 4.7 % de la banca; Faltas Visitante SC Más 12.5 4.3 % de la banca; Remates Visitante SC Menos 10.5 3.5 % de la banca; Córners Local FC Más 5.5 2.9 % de la banca; Córners Más 10.5 1.3 % de la banca; Córners Más 9.5 2.0 % de la banca; Tarjetas Más 4.5 1.7 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Remates Visitante SC Menos 10.5 + Más corners: Local FC | 49 % | 49 % | 45 % | 2.04 | 2.10 | 1.11 | 11 % | Sorpresa: gana el no favorito | 39 % |
| Más corners: Local FC + Goles Menos 3.5 | 54 % | 53 % | 50 % | 1.87 | 1.92 | 1.01 | 8 % | Empate | 24 % |
| Goles Menos 3.5 + Volante Visitante entradas 1+ | 52 % | 51 % | 49 % | 1.91 | 1.97 | 1.0 | 14 % | Empate | 24 % |
| Faltas Más 24.5 + Tarjetas Más 3.5 | 47 % | 47 % | 43 % | 2.13 | 2.19 | 1.09 | 10 % | Expulsión antes del 70′ | 41 % |
| ↳ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |  |  |  |  |  |  |  |  |  |
| Faltas Visitante SC Más 12.5 + Tarjetas Más 3.5 | 46 % | 46 % | 43 % | 2.16 | 2.22 | 1.06 | 10 % | Expulsión antes del 70′ | 38 % |
| ↳ Revisar: el contexto mueve 11 pts sin un hecho fresco que toque este mercado (¿la ficha repite lo que ya está en el precio?) |  |  |  |  |  |  |  |  |  |
| Remates Local FC Más 14.5 + Portero Visitante atajadas 2+ | 43 % | 51 % | 39 % | 2.33 | 2.40 | 1.14 | 16 % | Partido abierto (ambos marcan y 3+ goles) | 40 % |
| ↳ Historial propio en contra (remates mas: 2/7 contra 50 % del precio) |  |  |  |  |  |  |  |  |  |
| Remates Local FC Más 14.5 + Delantero Local remates 2+ | 39 % | 39 % | 36 % | 2.54 | 2.62 | 1.2 | 16 % | Partido abierto (ambos marcan y 3+ goles) | 36 % |
| ↳ Historial propio en contra (remates mas: 2/7 contra 50 % del precio) |  |  |  |  |  |  |  |  |  |
| Goles 1.er tiempo Más 0.5 + Volante Visitante entradas 1+ | 47 % | 46 % | 44 % | 2.11 | 2.17 | 0.99 | 14 % | Favorito golpea temprano y gana | 16 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.