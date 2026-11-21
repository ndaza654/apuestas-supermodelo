# SV Elversberg - SC Friburgo
Alemania Bundesliga · 2026-11-21 09:30

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** SC Friburgo · primer gol: local 39 %, visitante 57 %, nadie 4 % · gol del favorito antes del 35′: 39 %

**Base de la liga:** Alemania Bundesliga · 3.19 goles/partido, Más 2.5 62 %, ambos marcan 60 % · córners 9.8 · tarjetas (amarilla 1, roja 2) 4.3 (1233 partidos ago-2022/nov-2026)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Resultado / hándicap | ➖ neutro | SC Friburgo favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro que saca más tarjetas que la liga |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 34 % |
| Sorpresa: gana el no favorito | 23 % |
| Empate | 13 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 10 % |
| Favorito gana en partido trabado | 9 % |

## Lo que cambió el contexto
- Árbitro Hempel R.: 5.5 tarjetas/partido contra 4.32 de la liga (prior de la liga (Alemania Bundesliga)) en 51 partidos → tarjetas ×1.11 (encogido por muestra).
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.34 | 13.2 | 4.1 | 4.4 | 12.6 | 2.3 |
| visitante | 1.84 | 15.6 | 4.9 | 5.0 | 11.1 | 2.3 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.2 (3.2) · 1–6 | 1.4 (1.4) · 0–3 | 1.9 (1.9) · 0–4 | 1.4 (1.4) · 0–3 | 1.8 (1.9) · 0–4 |
| Córners | 9.4 (9.4) · 5–14 | 4.4 (4.4) · 2–8 | 5.0 (5.0) · 2–9 | 4.2 (4.5) · 2–7 | 5.2 (5.0) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 4.5 (4.1) · 2–8 | 2.3 (2.1) · 1–4 | 2.3 (2.1) · 1–4 | 1.5 (1.4) · 0–3 | 3.0 · 1–6 |
| Remates | 28.8 (28.6) · 21–37 | 13.1 (13.2) · 8–19 | 15.7 (15.6) · 10–22 | 12.9 · 8–18 | 15.9 · 11–21 |
| Tiros al arco | 9.1 (9.0) · 5–13 | 4.1 (4.1) · 1–7 | 4.9 (4.9) · 2–8 | 4.1 (4.2) · 2–7 | 5.0 · 2–8 |
| Faltas | 23.8 (23.7) · 18–30 | 12.7 (12.6) · 8–17 | 11.1 (11.1) · 7–16 | 10.7 · 7–15 | 13.2 · 9–18 |
| Fueras de lugar | 3.5 (3.6) · 1–6 | 2.3 (2.3) · 0–5 | 1.2 (1.3) · 0–3 | 1.6 (1.9) · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.1 · 3–11 | 9.0 · 5–14 |
| Saques de banda | 40.0 · 29–52 | 20.0 · 12–28 | 20.0 · 12–28 | 17.9 · 12–25 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.1 · 1–6 | 2.8 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.25 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (60 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.47 | 64 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Cara · ★ enfoque a favor |
| Resultado y hándicap | No hay empate | 1.27 | 76 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.36 | 80 % | 70 % | Empate (74 %) | Partido abierto (ambos marcan y 3+ goles) (70 %) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas | Ambos 1+ tarjetas: Sí | 1.25 | 82 % | 80 % | Expulsión antes del 70′ (91 %) | Favorito golpea temprano y gana (78 %) | Alta probabilidad |
| Faltas | Faltas SC Friburgo Más 10.5 | 1.70 | 55 % | 53 % | Expulsión antes del 70′ (58 %) | Sorpresa: gana el no favorito (53 %) | Cara |
| Remates | Remates SV Elversberg Menos 15.5 | 1.27 | 75 % | 69 % | Favorito gana en partido trabado (87 %) | Partido abierto (ambos marcan y 3+ goles) (69 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco SV Elversberg Más 2.5 | 1.25 | 77 % | 69 % | Sorpresa: gana el no favorito (93 %) | Favorito gana en partido trabado (48 %) | Alta probabilidad |
| Fueras de lugar | Fueras de lugar Menos 4.5 | 1.33 | 73 % | 72 % | Expulsión antes del 70′ (76 %) | Partido abierto (ambos marcan y 3+ goles) (72 %) | Alta probabilidad |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí | 1.25 | 82 % | 78 % | 78 % | +4 pts | +3 % | 80 % | — | 1.25 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 12.0 | 1.26 | 81 % | 80 % | 81 % | -0 pts | +1 % | 72 % | +0.8 | 1.28 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners 1.er tiempo Menos 6.0 | 1.36 | 80 % | 77 % | 80 % | -0 pts | +9 % | 70 % | +0.8 | 1.29 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas Más 2.5 | 1.31 | 80 % | 74 % | 74 % | +5 pts | +4 % | 77 % | +0.8 | 1.30 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Córners Más 7.0 | 1.33 | 78 % | 77 % | 78 % | +0 pts | +4 % | 70 % | +0.8 | 1.32 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles Menos 4.5 | 1.25 | 78 % | 78 % | 78 % | -0 pts | -3 % | 78 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco SC Friburgo Menos 6.5 | 1.25 | 77 % | 78 % | 77 % | +0 pts | -4 % | 63 % | +0.7 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco SV Elversberg Más 2.5 | 1.25 | 77 % | 78 % | 76 % | +0 pts | -4 % | 69 % | +0.7 | 1.34 | Favorito gana en partido trabado | Alta probabilidad |
| Remates Menos 32.5 | 1.25 | 76 % | 78 % | 76 % | +1 pts | -5 % | 67 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco SV Elversberg Menos 5.5 | 1.26 | 76 % | 77 % | 76 % | -0 pts | -4 % | 60 % | +0.6 | 1.35 | Sorpresa: gana el no favorito | Alta probabilidad |
| Remates Más 24.5 | 1.26 | 76 % | 77 % | 76 % | -0 pts | -4 % | 66 % | +0.7 | 1.35 | Favorito gana en partido trabado | Alta probabilidad |
| Córners Menos 11.5 | 1.26 | 76 % | 77 % | 76 % | -0 pts | -5 % | 73 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas 1.er tiempo Más 0.5 | 1.34 | 76 % | 72 % | 73 % | +3 pts | +1 % | 73 % | +0.8 | 1.36 | Favorito golpea temprano y gana | Alta probabilidad |
| No hay empate | 1.27 | 76 % | 75 % | 75 % | +1 pts | -4 % | 76 % | — | 1.36 | Empate | Alta probabilidad |
| Córners SC Friburgo Menos 6.5 | 1.27 | 75 % | 76 % | 75 % | -0 pts | -5 % | 69 % | +0.6 | 1.37 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.32 | 75 % | 73 % | 75 % | +0 pts | -1 % | 75 % | +0.8 | 1.37 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Remates SC Friburgo Más 12.5 | 1.26 | 75 % | 77 % | 75 % | -0 pts | -6 % | 68 % | +0.7 | 1.38 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates SV Elversberg Menos 15.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -5 % | 69 % | +0.5 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles SV Elversberg Más 0.5 | 1.29 | 75 % | 75 % | 75 % | -1 pts | -4 % | 75 % | +0.8 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Más 3.0 | 1.45 | 74 % | 75 % | 74 % | +0 pts | +7 % | 60 % | +0.6 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 2.º tiempo Más 3.5 | 1.33 | 74 % | 73 % | 74 % | +0 pts | -2 % | 74 % | +0.7 | 1.39 | Expulsión antes del 70′ | Alta probabilidad |
| SC Friburgo o empate | 1.32 | 74 % | 74 % | 74 % | -0 pts | -3 % | 74 % | — | 1.40 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap SC Friburgo +1 | 1.32 | 74 % | 74 % | 74 % | -0 pts | -3 % | 74 % | — | 1.40 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap SV Elversberg +2 | 1.31 | 74 % | 74 % | 75 % | -1 pts | -4 % | 74 % | — | 1.40 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.35 | 73 % | 72 % | 73 % | -0 pts | -2 % | 73 % | +0.6 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 | 1.67 | 64 % | 56 % | 56 % | +7 pts | +6 % | 60 % | +0.4 | 1.62 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Tarjetas Más 4.5 | 2.32 | 46 % | 39 % | 39 % | +7 pts | +8 % | 41 % | +0.0 | 2.25 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Tarjetas Más 5.5 | 3.40 | 32 % | 25 % | 25 % | +7 pts | +8 % | 27 % | -0.4 | 3.37 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor frágil (depende de un guion) |
| Ambos 2+ tarjetas: Sí | 2.20 | 49 % | 42 % | 42 % | +7 pts | +7 % | 46 % | — | 2.14 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Tarjetas SV Elversberg Más 2.5 | 2.65 | 40 % | 34 % | 33 % | +6 pts | +6 % | 36 % | -0.1 | 2.64 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor |
| Tarjetas SC Friburgo Más 2.5 | 2.65 | 39 % | 34 % | 32 % | +6 pts | +3 % | 34 % | -0.2 | 2.72 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) |
| Tarjetas SC Friburgo Más 1.5 | 1.57 | 67 % | 61 % | 61 % | +6 pts | +5 % | 64 % | +0.5 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+6 pts) · Valor |
| Tarjetas Más 2.5 | 1.31 | 80 % | 74 % | 74 % | +5 pts | +4 % | 77 % | +0.8 | 1.30 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Tarjetas SV Elversberg Más 1.5 | 1.57 | 66 % | 61 % | 61 % | +5 pts | +4 % | 64 % | +0.5 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Tarjetas Más 6.5 | 5.10 | 20 % | 15 % | 15 % | +5 pts | +1 % | 16 % | -0.8 | 5.62 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Tarjetas 1.er tiempo Más 1.5 | 2.15 | 46 % | 43 % | 41 % | +5 pts | -1 % | 40 % | +0.0 | 2.27 | Empate | Contexto a favor (+5 pts) |
| Tarjetas SV Elversberg Más 3.5 | 5.00 | 19 % | 15 % | 15 % | +5 pts | -3 % | 16 % | -0.8 | 5.72 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Tarjetas SC Friburgo Más 3.5 | 5.00 | 19 % | 15 % | 15 % | +4 pts | -5 % | 16 % | -0.8 | 5.89 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · cuota por debajo de la justa |
| Tarjetas Más 7.5 | 7.40 | 12 % | 8 % | 8 % | +4 pts | -12 % | 9 % | -1.2 | 10.14 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.62 | 44 % | 42 % | 45 % | -0 pts | +16 % | 36 % | -0.1 | 2.36 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.75 | 65 % | 62 % | 65 % | -0 pts | +13 % | 54 % | +0.4 | 1.60 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 3.0 | 4.55 | 24 % | 24 % | 24 % | -0 pts | +10 % | 19 % | -0.6 | 4.50 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 6.0 | 1.36 | 80 % | 77 % | 80 % | -0 pts | +9 % | 70 % | +0.8 | 1.29 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas Más 5.5 | 3.40 | 32 % | 25 % | 25 % | +7 pts | +8 % | 27 % | -0.4 | 3.37 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor frágil (depende de un guion) |
| Tarjetas Más 4.5 | 2.32 | 46 % | 39 % | 39 % | +7 pts | +8 % | 41 % | +0.0 | 2.25 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Córners 1.er tiempo Más 3.0 | 1.45 | 74 % | 75 % | 74 % | +0 pts | +7 % | 60 % | +0.6 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Ambos 2+ tarjetas: Sí | 2.20 | 49 % | 42 % | 42 % | +7 pts | +7 % | 46 % | — | 2.14 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Córners Más 9.0 | 2.02 | 53 % | 52 % | 52 % | +1 pts | +7 % | 45 % | +0.1 | 1.96 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 4.0 | 2.00 | 53 % | 55 % | 53 % | +0 pts | +7 % | 41 % | +0.1 | 1.95 | Empate | Valor · asiática: devuelve 19 % |
| Córners Más 8.0 | 1.60 | 67 % | 66 % | 66 % | +1 pts | +7 % | 58 % | +0.4 | 1.55 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Tarjetas Más 3.5 | 1.67 | 64 % | 56 % | 56 % | +7 pts | +6 % | 60 % | +0.4 | 1.62 | Favorito golpea temprano y gana | Contexto a favor (+7 pts) · Valor |
| Córners Más 10.0 | 2.67 | 40 % | 39 % | 39 % | +1 pts | +6 % | 33 % | -0.2 | 2.66 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Tarjetas SV Elversberg Más 2.5 | 2.65 | 40 % | 34 % | 33 % | +6 pts | +6 % | 36 % | -0.1 | 2.64 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor |
| Córners 1.er tiempo Más 2.0 | 1.18 | 89 % | 88 % | 89 % | +0 pts | +5 % | 77 % | +1.1 | 1.16 | Empate | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Tarjetas SC Friburgo Más 1.5 | 1.57 | 67 % | 61 % | 61 % | +6 pts | +5 % | 64 % | +0.5 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+6 pts) · Valor |
| Córners Menos 10.0 | 1.75 | 60 % | 60 % | 60 % | -1 pts | +4 % | 50 % | +0.2 | 1.73 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Tarjetas SV Elversberg Más 1.5 | 1.57 | 66 % | 61 % | 61 % | +5 pts | +4 % | 64 % | +0.5 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Córners Más 7.0 | 1.33 | 78 % | 77 % | 78 % | +0 pts | +4 % | 70 % | +0.8 | 1.32 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Tarjetas Más 2.5 | 1.31 | 80 % | 74 % | 74 % | +5 pts | +4 % | 77 % | +0.8 | 1.30 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor |
| Córners 1.er tiempo Menos 7.0 | 1.16 | 89 % | 86 % | 89 % | -0 pts | +3 % | 82 % | +1.3 | 1.16 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 7 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.5 % de la banca; Córners 1.er tiempo Menos 5.0 4.4 % de la banca; Córners 1.er tiempo Menos 3.0 0.7 % de la banca; Córners 1.er tiempo Menos 6.0 6.0 % de la banca; Tarjetas Más 5.5 0.8 % de la banca; Tarjetas Más 4.5 1.5 % de la banca; Córners 1.er tiempo Más 3.0 4.1 % de la banca; Ambos 2+ tarjetas: Sí 1.5 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #45 (sin H2H) | Bundesliga, empate 3,60–4,33, ambos ≥2,00 | Empate | 534 partidos: acierto 27.3 % contra 25.3 % del precio; ROI +1.5 % ± 14.1 (con la mejor cuota +5.9 %) |
| Ingeniero Analista #16 | liga con Ambos Sí ≥55 %, Más 2.5 ≤1,80 y Ambos Sí ≤1,75 | Ambos marcan: Sí | 27602 partidos: Ambos Sí 56.0 % contra 56.5 % que ya da el precio (-0.5 pts ± 0.6) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí | 61 % | 62 % | 56 % | 1.63 | 1.68 | 1.17 | 9 % | Expulsión antes del 70′ | 57 % |
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí + Goles SV Elversberg Menos 3.5 | 59 % | 59 % | 54 % | 1.70 | 1.75 | 1.18 | 10 % | Expulsión antes del 70′ | 50 % |
| Tarjetas 1.er tiempo Más 0.5 + Fueras de lugar SC Friburgo Menos 2.5 + Córners SC Friburgo Más 1.5 | 62 % | 62 % | 58 % | 1.60 | 1.65 | 1.0 | 7 % | Expulsión antes del 70′ | 60 % |
| Goles 1.er tiempo Más 0.5 + Fueras de lugar SC Friburgo Menos 2.5 + Tiros al arco Más 5.5 | 60 % | 60 % | 56 % | 1.67 | 1.72 | 1.04 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 35 % |
| Tarjetas 1.er tiempo Más 0.5 + Córners 2.º tiempo Más 1.5 + Goles SC Friburgo Más 0.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.0 | 7 % | Expulsión antes del 70′ | 44 % |
| Tarjetas SV Elversberg Más 1.5 + Córners 1.er tiempo Menos 8.5 + Goles SV Elversberg Menos 3.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.01 | 7 % | Expulsión antes del 70′ | 53 % |
| Tarjetas SC Friburgo Más 1.5 + Tiros al arco SV Elversberg Menos 7.5 | 62 % | 61 % | 57 % | 1.61 | 1.66 | 1.0 | 6 % | Expulsión antes del 70′ | 55 % |
| Tarjetas SV Elversberg Más 1.5 + Tiros al arco SV Elversberg Menos 7.5 | 62 % | 62 % | 57 % | 1.62 | 1.67 | 1.0 | 6 % | Expulsión antes del 70′ | 54 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.