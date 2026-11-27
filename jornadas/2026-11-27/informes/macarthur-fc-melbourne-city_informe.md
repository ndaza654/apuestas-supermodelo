# Macarthur FC - Melbourne City
Australia A-League · 2026-11-27 03:40

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** Melbourne City · primer gol: local 40 %, visitante 55 %, nadie 5 % · gol del favorito antes del 35′: 36 %

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Resultado / hándicap | ➖ neutro | Melbourne City favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 32 % |
| Sorpresa: gana el no favorito | 25 % |
| Empate | 16 % |
| Favorito golpea temprano y gana | 10 % |
| Expulsión antes del 70′ | 9 % |
| Favorito gana en partido trabado | 9 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.30 | 13.1 | 4.4 | 5.1 | 11.8 | 1.9 |
| visitante | 1.69 | 15.1 | 5.0 | 5.1 | 11.8 | 1.9 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.0) · 1–5 | 1.3 (1.3) · 0–3 | 1.7 (1.7) · 0–3 | 1.4 (1.3) · 0–3 | 1.6 (1.7) · 0–3 |
| Córners | 10.1 (10.1) · 6–15 | 5.0 · 2–8 | 5.1 · 2–9 | 4.5 (4.9) · 2–7 | 5.6 (5.3) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 3.9 (3.8) · 1–7 | 2.0 (1.9) · 0–4 | 1.9 (1.9) · 0–4 | 1.3 (1.4) · 0–3 | 2.6 · 1–5 |
| Remates | 28.3 (28.2) · 21–36 | 13.1 (13.1) · 8–19 | 15.2 (15.1) · 9–22 | 12.7 · 8–18 | 15.6 · 10–21 |
| Tiros al arco | 9.4 (9.4) · 5–14 | 4.4 (4.4) · 2–7 | 5.0 (5.0) · 2–8 | 4.2 · 2–7 | 5.1 · 2–8 |
| Faltas | 23.6 · 17–30 | 11.8 · 8–16 | 11.7 · 7–16 | 10.6 · 7–15 | 13.0 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 39.9 · 29–52 | 20.0 · 12–28 | 19.9 · 12–28 | 17.8 · 12–24 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.3 · 1–6 | 3.1 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Melbourne City Menos 2.5 | 1.27 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (49 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.57 | 61 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | Hándicap Macarthur FC +2 | 1.27 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (27 %) | Alta probabilidad |
| Córners | Córners 2.º tiempo Más 3.5 | 1.25 | 79 % | 79 % | Partido abierto (ambos marcan y 3+ goles) (81 %) | Expulsión antes del 70′ (74 %) | Alta probabilidad |
| Tarjetas | Ambos 1+ tarjetas: Sí | 1.31 | 75 % | 74 % | Expulsión antes del 70′ (87 %) | Favorito golpea temprano y gana (68 %) | Alta probabilidad |
| Remates | Remates Macarthur FC Menos 15.5 | 1.28 | 74 % | 69 % | Favorito gana en partido trabado (83 %) | Partido abierto (ambos marcan y 3+ goles) (69 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco Menos 11.5 | 1.26 | 77 % | 63 % | Empate (92 %) | Partido abierto (ambos marcan y 3+ goles) (63 %) | Alta probabilidad |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 2.º tiempo Más 3.5 | 1.25 | 79 % | 78 % | 79 % | +0 pts | -2 % | 79 % | +0.8 | 1.31 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.34 | 79 % | 79 % | 79 % | +0 pts | +5 % | 64 % | +0.7 | 1.31 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Hándicap Macarthur FC +2 | 1.27 | 77 % | 76 % | 77 % | +0 pts | -3 % | 77 % | — | 1.34 | Favorito golpea temprano y gana | Alta probabilidad |
| Tiros al arco Menos 11.5 | 1.26 | 77 % | 77 % | 77 % | +0 pts | -4 % | 63 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Melbourne City Menos 6.5 | 1.26 | 76 % | 77 % | 76 % | +0 pts | -4 % | 63 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Melbourne City Menos 2.5 | 1.27 | 76 % | 76 % | 76 % | +0 pts | -3 % | 76 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -2 % | 76 % | +0.7 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Ambos 1+ tarjetas: Sí | 1.31 | 75 % | 74 % | 75 % | +0 pts | -1 % | 74 % | — | 1.37 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 1.er tiempo Menos 6.0 | 1.47 | 75 % | 72 % | 75 % | +0 pts | +10 % | 66 % | +0.7 | 1.37 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Remates Macarthur FC Menos 15.5 | 1.28 | 74 % | 76 % | 74 % | +0 pts | -5 % | 69 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 8.0 | 1.40 | 74 % | 74 % | 74 % | +0 pts | +4 % | 66 % | +0.6 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 11 % |
| No hay empate | 1.28 | 74 % | 74 % | 74 % | +0 pts | -5 % | 74 % | — | 1.39 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Remates Más 24.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -5 % | 64 % | +0.6 | 1.39 | Empate | Alta probabilidad |
| Córners Menos 12.0 | 1.39 | 74 % | 74 % | 74 % | +0 pts | +3 % | 66 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Goles Macarthur FC Más 0.5 | 1.31 | 74 % | 74 % | 74 % | +0 pts | -3 % | 74 % | +0.7 | 1.40 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Remates Macarthur FC Más 10.5 | 1.28 | 73 % | 76 % | 73 % | +0 pts | -7 % | 67 % | +0.6 | 1.41 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Más 0.5 | 1.35 | 73 % | 72 % | 73 % | +0 pts | -2 % | 73 % | +0.7 | 1.41 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Remates Menos 31.5 | 1.30 | 73 % | 74 % | 73 % | +0 pts | -5 % | 64 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Melbourne City Menos 17.5 | 1.30 | 72 % | 74 % | 72 % | +0 pts | -6 % | 67 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Hándicap Melbourne City +1 | 1.35 | 72 % | 72 % | 72 % | +0 pts | -3 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco Macarthur FC Menos 5.5 | 1.33 | 72 % | 73 % | 72 % | +0 pts | -4 % | 55 % | +0.5 | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Melbourne City Más 3.5 | 1.27 | 72 % | 74 % | 72 % | +0 pts | -8 % | 71 % | +0.6 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Melbourne City o empate | 1.35 | 72 % | 71 % | 72 % | +0 pts | -3 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Melbourne City +0.5 | 1.37 | 72 % | 72 % | 72 % | +0 pts | -1 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco Melbourne City Más 3.5 | 1.32 | 72 % | 73 % | 72 % | +0 pts | -5 % | 55 % | +0.6 | 1.43 | Empate | Alta probabilidad |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 3.10 | 38 % | 35 % | 38 % | +0 pts | +18 % | 31 % | -0.2 | 2.78 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 5.0 | 2.00 | 58 % | 55 % | 58 % | +0 pts | +16 % | 49 % | +0.2 | 1.78 | Sorpresa: gana el no favorito | Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 6.0 | 1.47 | 75 % | 72 % | 75 % | +0 pts | +10 % | 66 % | +0.7 | 1.37 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners Menos 10.0 | 2.10 | 51 % | 50 % | 51 % | +0 pts | +6 % | 43 % | -0.0 | 2.06 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Menos 7.0 | 1.23 | 86 % | 83 % | 86 % | +0 pts | +6 % | 78 % | +1.1 | 1.20 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 8 % |
| Córners 1.er tiempo Más 3.0 | 1.34 | 79 % | 79 % | 79 % | +0 pts | +5 % | 64 % | +0.7 | 1.31 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Más 4.0 | 1.75 | 60 % | 63 % | 60 % | +0 pts | +5 % | 47 % | +0.2 | 1.72 | Favorito gana en partido trabado | Valor · asiática: devuelve 18 % |
| Córners Más 10.0 | 2.15 | 49 % | 49 % | 49 % | +0 pts | +5 % | 42 % | +0.0 | 2.14 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Menos 11.0 | 1.65 | 63 % | 63 % | 63 % | +0 pts | +4 % | 55 % | +0.3 | 1.63 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 10 % |
| Córners Más 8.0 | 1.40 | 74 % | 74 % | 74 % | +0 pts | +4 % | 66 % | +0.6 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Más 9.0 | 1.67 | 62 % | 62 % | 62 % | +0 pts | +4 % | 54 % | +0.3 | 1.66 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.1 % de la banca; Córners 1.er tiempo Menos 5.0 4.0 % de la banca; Córners 1.er tiempo Menos 6.0 5.5 % de la banca; Córners Menos 10.0 1.4 % de la banca; Córners 1.er tiempo Menos 7.0 6.3 % de la banca; Córners 1.er tiempo Más 3.0 3.8 % de la banca; Córners 1.er tiempo Más 4.0 1.7 % de la banca; Córners Más 10.0 1.0 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 6.5 + Ambos 1+ tarjetas: Sí + Tarjetas Melbourne City Más 0.5 | 60 % | 63 % | 56 % | 1.66 | 1.71 | 1.16 | 8 % | Expulsión antes del 70′ | 58 % |
| Hándicap Melbourne City +2 + Tarjetas Macarthur FC Más 0.5 + Melbourne City o empate | 62 % | 64 % | 58 % | 1.62 | 1.66 | 1.11 | 8 % | Empate | 0 % |
| Tarjetas Más 1.5 + Hándicap Melbourne City +2 + Melbourne City o empate | 62 % | 64 % | 58 % | 1.62 | 1.66 | 1.11 | 8 % | Empate | 0 % |
| Córners 1.er tiempo Menos 6.5 + Tarjetas Más 1.5 + Ambos 1+ tarjetas: Sí | 60 % | 63 % | 56 % | 1.67 | 1.72 | 1.14 | 8 % | Expulsión antes del 70′ | 58 % |
| Tarjetas Melbourne City Más 0.5 + Goles 2.º tiempo Menos 2.5 + Tiros al arco Melbourne City Menos 8.5 | 62 % | 62 % | 58 % | 1.62 | 1.66 | 1.03 | 7 % | Empate | 43 % |
| Tarjetas Macarthur FC Más 0.5 + Goles 2.º tiempo Menos 2.5 + Tiros al arco Macarthur FC Menos 7.5 | 62 % | 63 % | 58 % | 1.62 | 1.67 | 1.03 | 7 % | Empate | 44 % |
| Goles Macarthur FC Menos 3.5 + Tarjetas 1.er tiempo Menos 1.5 | 60 % | 61 % | 55 % | 1.68 | 1.73 | 1.0 | 6 % | Empate | 58 % |
| Goles 1.er tiempo Menos 3.5 + Tarjetas 1.er tiempo Menos 1.5 | 59 % | 60 % | 55 % | 1.69 | 1.74 | 1.0 | 6 % | Empate | 60 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.