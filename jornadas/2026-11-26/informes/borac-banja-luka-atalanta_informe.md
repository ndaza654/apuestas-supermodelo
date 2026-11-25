# Borac Banja Luka - Atalanta
UEFA Conference League Conference League · 2026-11-26 15:00

**Tipo de partido:** Favorito claro · abierto · normal · **Favorito:** Atalanta · primer gol: local 26 %, visitante 71 %, nadie 4 % · gol del favorito antes del 35′: 50 %

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Hándicap y victoria de Atalanta, Goles de Atalanta (Más), Remates / tiros al arco de Atalanta, Tarjetas (Menos), Faltas (Menos).

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Hándicap y victoria de Atalanta | ✅ favorece | favorito claro: manda en el marcador y en el territorio |
| Goles de Atalanta (Más) | ✅ favorece | favorito claro contra rival que sufre |
| Remates / tiros al arco de Atalanta | ✅ favorece | el que domina remata más |
| Tarjetas (Menos) | ✅ favorece | árbitro sin dato; favorito claro: poca fricción y, si hay goleada, menos tarjetas |
| Faltas (Menos) | ✅ favorece | árbitro sin dato; favorito claro: poca fricción y, si hay goleada, menos tarjetas |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Córners totales | ➖ neutro | si el favorito marca pronto, sus córners se apagan; si el rival forzara, suben |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 38 % |
| Favorito golpea temprano y gana | 20 % |
| Favorito gana en partido trabado | 12 % |
| Empate | 12 % |
| Sorpresa: gana el no favorito | 10 % |
| Expulsión antes del 70′ | 8 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 0.96 | 11.8 | 4.0 | 4.0 | 11.7 | 1.9 |
| visitante | 2.30 | 18.4 | 6.3 | 5.3 | 12.6 | 1.4 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.2 (3.2) · 1–6 | 0.9 (1.0) · 0–2 | 2.3 (2.3) · 1–4 | 1.5 (1.4) · 0–3 | 1.7 (1.9) · 0–4 |
| Córners | 9.3 (9.2) · 5–14 | 4.1 (4.0) · 1–7 | 5.2 (5.3) · 2–9 | 4.2 (4.4) · 2–7 | 5.1 (4.8) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 3.3 (3.3) · 1–6 | 1.9 (1.9) · 0–4 | 1.4 (1.4) · 0–3 | 1.2 (1.1) · 0–3 | 2.2 · 0–4 |
| Remates | 30.3 (30.1) · 22–38 | 12.0 (11.8) · 7–17 | 18.4 (18.4) · 12–26 | 13.8 · 9–19 | 16.5 · 11–22 |
| Tiros al arco | 10.3 (10.2) · 6–15 | 4.0 (4.0) · 1–7 | 6.3 (6.3) · 3–10 | 4.7 (4.7) · 2–8 | 5.6 · 3–9 |
| Faltas | 24.2 (24.2) · 18–31 | 11.6 (11.7) · 7–16 | 12.6 (12.6) · 8–17 | 10.8 · 7–15 | 13.4 · 9–18 |
| Fueras de lugar | 3.0 (2.9) · 1–5 | 1.0 (1.0) · 0–2 | 2.0 (2.0) · 0–4 | 1.3 (1.5) · 0–3 | 1.6 · 0–3 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.1 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 39.9 · 29–52 | 19.9 · 12–28 | 20.0 · 12–28 | 17.9 · 12–25 | 22.0 · 15–30 |
| Atajadas del portero | — | 4.0 · 1–7 | 3.0 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.27 | 77 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (58 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.70 | 56 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa |
| Resultado y hándicap | Hándicap Borac Banja Luka +3 | 1.28 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (47 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.33 | 81 % | 71 % | Empate (74 %) | Partido abierto (ambos marcan y 3+ goles) (71 %) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas | Tarjetas Menos 4.5 | 1.29 | 75 % | 79 % | Favorito golpea temprano y gana (83 %) | Expulsión antes del 70′ (32 %) | Alta probabilidad · ★ enfoque a favor |
| Faltas | Faltas Más 23.5 | 1.75 | 54 % | 53 % | Expulsión antes del 70′ (57 %) | Favorito golpea temprano y gana (53 %) | Cara |
| Remates | Remates Borac Banja Luka Más 10.5 | 1.53 | 62 % | 59 % | Partido abierto (ambos marcan y 3+ goles) (69 %) | Favorito gana en partido trabado (51 %) | Cara |
| Tiros al arco | Tiros al arco Borac Banja Luka Más 2.5 | 1.28 | 74 % | 58 % | Sorpresa: gana el no favorito (93 %) | Favorito gana en partido trabado (56 %) | Alta probabilidad |
| Fueras de lugar | Fueras de lugar Borac Banja Luka Más 0.5 | 1.55 | 62 % | 62 % | Favorito golpea temprano y gana (65 %) | Sorpresa: gana el no favorito (57 %) | Justa |
| Jugadores | Mladen Jurkas atajadas 3+ | 1.70 | 58 % | 57 % | Favorito gana en partido trabado (61 %) | Expulsión antes del 70′ (56 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 6.0 | 1.33 | 81 % | 79 % | 81 % | +0 pts | +7 % | 71 % | +0.8 | 1.28 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Goles Menos 4.5 | 1.27 | 77 % | 77 % | 77 % | +0 pts | -2 % | 77 % | +0.7 | 1.33 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.28 | 77 % | 76 % | 77 % | +0 pts | -1 % | 77 % | +0.8 | 1.34 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners Más 7.0 | 1.37 | 77 % | 76 % | 77 % | +0 pts | +5 % | 65 % | +0.7 | 1.34 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Hándicap Borac Banja Luka +3 | 1.28 | 77 % | 76 % | 77 % | +0 pts | -2 % | 77 % | — | 1.35 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Tarjetas Atalanta Más 0.5 | 1.28 | 76 % | 76 % | 76 % | +0 pts | -2 % | 71 % | +0.8 | 1.35 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Borac Banja Luka Menos 1.5 | 1.29 | 75 % | 75 % | 75 % | +0 pts | -3 % | 76 % | +0.6 | 1.36 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tarjetas Menos 4.5 | 1.29 | 75 % | 75 % | 75 % | +0 pts | -4 % | 79 % | +0.6 | 1.38 | Expulsión antes del 70′ | Alta probabilidad · ★ enfoque a favor |
| Tiros al arco Borac Banja Luka Más 2.5 | 1.28 | 74 % | 76 % | 74 % | +0 pts | -5 % | 58 % | +0.7 | 1.39 | Favorito gana en partido trabado | Alta probabilidad |
| Córners Atalanta Más 3.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 68 % | +0.7 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Córners Borac Banja Luka Más 2.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -4 % | 76 % | +0.7 | 1.39 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Menos 5.5 | 1.33 | 73 % | 73 % | 73 % | +0 pts | -2 % | 72 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 11.0 | 1.40 | 73 % | 73 % | 73 % | +0 pts | +3 % | 64 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Descanso o final: Atalanta | 1.32 | 73 % | 71 % | 73 % | +0 pts | -3 % | 73 % | — | 1.41 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Goles 2.º tiempo Menos 2.5 | 1.35 | 73 % | 72 % | 73 % | +0 pts | -1 % | 73 % | +0.6 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.50 | 73 % | 73 % | 73 % | +0 pts | +10 % | 60 % | +0.6 | 1.41 | Empate | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Ambos 2+ tarjetas: No | 1.33 | 72 % | 73 % | 72 % | +0 pts | -4 % | 74 % | — | 1.42 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Más 0.75 | 1.37 | 72 % | 71 % | 72 % | +0 pts | -1 % | 72 % | +0.6 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| Córners 2.º tiempo Más 3.5 | 1.35 | 72 % | 71 % | 72 % | +0 pts | -2 % | 68 % | +0.7 | 1.42 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Atalanta Menos 6.5 | 1.32 | 72 % | 73 % | 72 % | +0 pts | -5 % | 71 % | +0.5 | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tarjetas Borac Banja Luka Menos 2.5 | 1.37 | 71 % | 70 % | 71 % | +0 pts | -3 % | 74 % | +0.4 | 1.45 | Expulsión antes del 70′ | Alta probabilidad · ★ enfoque a favor |
| Goles Más 2.25 | 1.39 | 70 % | 71 % | 70 % | +0 pts | -2 % | 70 % | +0.6 | 1.46 | Empate | Alta probabilidad · asiática: devuelve 10 % · ★ enfoque a favor |
| Tiros al arco Atalanta Menos 7.5 | 1.36 | 70 % | 71 % | 70 % | +0 pts | -4 % | 61 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 7.5 | 1.37 | 70 % | 70 % | 70 % | +0 pts | -4 % | 66 % | +0.6 | 1.47 | Favorito golpea temprano y gana | Alta probabilidad |
| Gana Atalanta | 1.45 | 68 % | 67 % | 68 % | +0 pts | -1 % | 68 % | — | 1.51 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mladen Jurkas atajadas 6+ | 9.00 | 14 % | 10 % | 14 % | +0 pts | +25 % | 13 % | -0.7 | 8.38 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Mladen Jurkas atajadas 5+ | 4.85 | 24 % | 18 % | 24 % | +0 pts | +16 % | 23 % | -0.2 | 4.57 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 4.0 | 2.50 | 45 % | 44 % | 45 % | +0 pts | +14 % | 36 % | -0.1 | 2.30 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.72 | 66 % | 64 % | 66 % | +0 pts | +13 % | 54 % | +0.4 | 1.57 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 3.0 | 4.40 | 25 % | 25 % | 25 % | +0 pts | +10 % | 19 % | -0.6 | 4.34 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 3.0 | 1.50 | 73 % | 73 % | 73 % | +0 pts | +10 % | 60 % | +0.6 | 1.41 | Empate | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 4.0 | 2.05 | 52 % | 54 % | 52 % | +0 pts | +8 % | 42 % | +0.1 | 1.98 | Empate | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 6.0 | 1.33 | 81 % | 79 % | 81 % | +0 pts | +7 % | 71 % | +0.8 | 1.28 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Más 9.0 | 2.10 | 51 % | 50 % | 51 % | +0 pts | +6 % | 40 % | +0.1 | 2.05 | Favorito golpea temprano y gana | Valor · asiática: devuelve 13 % |
| Córners Más 8.0 | 1.65 | 64 % | 64 % | 64 % | +0 pts | +6 % | 53 % | +0.4 | 1.60 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |
| Mladen Jurkas atajadas 4+ | 2.72 | 39 % | 33 % | 39 % | +0 pts | +6 % | 38 % | +0.2 | 2.71 | Sorpresa: gana el no favorito | Valor |
| Córners 1.er tiempo Más 2.0 | 1.19 | 88 % | 87 % | 88 % | +0 pts | +5 % | 77 % | +1.1 | 1.16 | Empate | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners Más 7.0 | 1.37 | 77 % | 76 % | 77 % | +0 pts | +5 % | 65 % | +0.7 | 1.34 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 9.0 | 2.15 | 49 % | 49 % | 49 % | +0 pts | +4 % | 40 % | -0.1 | 2.15 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 13 % |
| Córners Menos 10.0 | 1.67 | 62 % | 62 % | 62 % | +0 pts | +4 % | 52 % | +0.2 | 1.66 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |

Kelly ¼ (dato informativo, no una orden de stake): Mladen Jurkas atajadas 6+ 0.8 % de la banca; Mladen Jurkas atajadas 5+ 1.0 % de la banca; Córners 1.er tiempo Menos 4.0 2.2 % de la banca; Córners 1.er tiempo Menos 5.0 4.5 % de la banca; Córners 1.er tiempo Menos 3.0 0.8 % de la banca; Córners 1.er tiempo Más 3.0 4.8 % de la banca; Córners 1.er tiempo Más 4.0 1.8 % de la banca; Córners 1.er tiempo Menos 6.0 5.5 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #429 (sin racha) | empate ≥3,90, visitante ≤2,00 | Ambos marcan: Sí | 4451 partidos: Ambos Sí 52.8 % contra 54.0 % que ya da el precio (-1.1 pts ± 1.5) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles Atalanta Menos 4.5 + Tarjetas Atalanta Más 0.5 + Ambos 1+ tarjetas: Sí | 62 % | 64 % | 58 % | 1.61 | 1.66 | 1.32 | 9 % | Expulsión antes del 70′ | 55 % |
| Goles Borac Banja Luka Menos 2.5 + Tarjetas Atalanta Más 0.5 + Ambos 1+ tarjetas: Sí | 62 % | 64 % | 57 % | 1.62 | 1.67 | 1.3 | 9 % | Expulsión antes del 70′ | 60 % |
| Atalanta o empate + Hándicap Atalanta +1 + Goles 2.º tiempo Menos 2.5 | 62 % | 65 % | 58 % | 1.60 | 1.65 | 1.12 | 7 % | Empate | 52 % |
| Atalanta o empate + Goles 2.º tiempo Menos 2.5 + Córners Atalanta Menos 9.5 | 60 % | 62 % | 56 % | 1.65 | 1.70 | 1.0 | 6 % | Empate | 50 % |
| Goles Menos 6.5 + Fueras de lugar 1.er tiempo Menos 1.5 | 57 % | 59 % | 52 % | 1.76 | 1.81 | 1.0 | 6 % | Empate | 54 % |
| Córners 2.º tiempo Más 1.5 + Fueras de lugar 1.er tiempo Menos 1.5 | 57 % | 59 % | 52 % | 1.76 | 1.82 | 1.0 | 7 % | Empate | 56 % |
| Córners 2.º tiempo Más 1.5 + Mladen Jurkas atajadas 3+ | 56 % | 68 % | 51 % | 1.80 | 1.85 | 1.0 | 12 % | Favorito gana en partido trabado | 54 % |
| Goles Menos 6.5 + Mladen Jurkas atajadas 3+ | 55 % | 68 % | 51 % | 1.81 | 1.86 | 1.0 | 12 % | Favorito gana en partido trabado | 53 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.