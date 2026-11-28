# FC Cincinnati - Nashville SC
EE. UU. MLS · 2026-11-28 18:30

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** Nashville SC · primer gol: local 42 %, visitante 55 %, nadie 4 % · gol del favorito antes del 35′: 37 %

**Base de la liga:** Estados Unidos MLS · 2.97 goles/partido, Más 2.5 59 %, ambos marcan 60 % (1159 partidos ago-2022/nov-2026)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Resultado / hándicap | ➖ neutro | Nashville SC favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; los dos se juegan algo importante |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 36 % |
| Sorpresa: gana el no favorito | 25 % |
| Empate | 12 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 9 % |
| Favorito gana en partido trabado | 8 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.45 | 13.7 | 4.7 | 5.0 | 12.1 | 2.3 |
| visitante | 1.84 | 14.7 | 5.2 | 5.0 | 12.1 | 2.3 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.3 (3.4) · 1–6 | 1.4 (1.5) · 0–3 | 1.8 (1.9) · 0–4 | 1.4 (1.4) · 0–3 | 1.8 (1.9) · 0–4 |
| Córners | 10.0 (9.9) · 6–14 | 5.0 · 2–8 | 5.0 · 2–8 | 4.4 (4.8) · 2–7 | 5.6 (5.2) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 4.6 (4.3) · 2–8 | 2.3 (2.2) · 1–4 | 2.3 (2.2) · 1–4 | 1.6 (1.5) · 0–3 | 3.0 · 1–6 |
| Remates | 28.4 (28.2) · 21–36 | 13.7 (13.7) · 8–20 | 14.7 (14.7) · 9–21 | 12.6 · 8–18 | 15.8 · 10–21 |
| Tiros al arco | 9.8 (9.8) · 6–14 | 4.7 (4.7) · 2–8 | 5.2 (5.2) · 2–8 | 4.4 · 2–7 | 5.5 · 3–9 |
| Faltas | 24.3 · 18–31 | 12.2 · 8–17 | 12.1 · 8–17 | 10.9 · 7–15 | 13.4 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 39.9 · 29–52 | 20.0 · 12–28 | 19.9 · 12–28 | 17.9 · 11–25 | 22.0 · 15–30 |
| Atajadas del portero | — | 3.3 · 1–6 | 3.2 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.31 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (60 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.42 | 66 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Resultado y hándicap | Hándicap FC Cincinnati +2 | 1.29 | 76 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (25 %) | Alta probabilidad |
| Córners | Córners 2.º tiempo Más 3.5 | 1.27 | 78 % | 79 % | Partido abierto (ambos marcan y 3+ goles) (80 %) | Expulsión antes del 70′ (75 %) | Alta probabilidad |
| Tarjetas | Tarjetas FC Cincinnati Más 1.5 | 1.52 | 66 % | 64 % | Expulsión antes del 70′ (86 %) | Favorito golpea temprano y gana (59 %) | Alta probabilidad |
| Remates | Remates Más 24.5 | 1.29 | 75 % | 66 % | Partido abierto (ambos marcan y 3+ goles) (84 %) | Favorito gana en partido trabado (65 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco Nashville SC Más 3.5 | 1.28 | 75 % | 59 % | Partido abierto (ambos marcan y 3+ goles) (91 %) | Sorpresa: gana el no favorito (59 %) | Alta probabilidad |
| Jugadores | Andy Najar anota o asiste | 2.50 | 38 % | 21 % | Partido abierto (ambos marcan y 3+ goles) (53 %) | Empate (21 %) | Cara |
| Quién saca más | Más corners: FC Cincinnati | 2.45 | 41 % | 35 % | Favorito golpea temprano y gana (54 %) | Sorpresa: gana el no favorito (35 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 2.º tiempo Más 3.5 | 1.27 | 78 % | 76 % | 77 % | +1 pts | -0 % | 79 % | +0.8 | 1.31 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.37 | 77 % | 78 % | 77 % | -0 pts | +6 % | 62 % | +0.7 | 1.33 | Empate | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.45 | 76 % | 73 % | 76 % | +0 pts | +11 % | 66 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Goles Menos 4.5 | 1.31 | 76 % | 74 % | 75 % | +2 pts | -0 % | 76 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Más 7.5 | 1.27 | 76 % | 76 % | 76 % | +0 pts | -3 % | 57 % | +0.7 | 1.35 | Empate | Alta probabilidad |
| Hándicap FC Cincinnati +2 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -2 % | 76 % | — | 1.36 | Favorito golpea temprano y gana | Alta probabilidad |
| No hay empate | 1.26 | 76 % | 75 % | 75 % | +0 pts | -5 % | 76 % | — | 1.36 | Empate | Alta probabilidad |
| Córners Menos 12.0 | 1.36 | 75 % | 75 % | 75 % | -0 pts | +2 % | 66 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Goles 1.er tiempo Más 0.5 | 1.29 | 75 % | 75 % | 77 % | -2 pts | -3 % | 75 % | +0.8 | 1.37 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Remates Más 24.5 | 1.29 | 75 % | 75 % | 74 % | +1 pts | -4 % | 66 % | +0.7 | 1.38 | Favorito gana en partido trabado | Alta probabilidad |
| Tiros al arco Nashville SC Más 3.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -5 % | 59 % | +0.7 | 1.38 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco Nashville SC Menos 6.5 | 1.31 | 73 % | 74 % | 74 % | -0 pts | -4 % | 60 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 8.0 | 1.45 | 73 % | 72 % | 72 % | +1 pts | +6 % | 65 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Remates Menos 31.5 | 1.30 | 72 % | 74 % | 73 % | -0 pts | -6 % | 63 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Hándicap Nashville SC +0.5 | 1.37 | 72 % | 71 % | 71 % | +1 pts | -1 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Nashville SC o empate | 1.36 | 72 % | 71 % | 71 % | +1 pts | -2 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Nashville SC +1 | 1.36 | 72 % | 71 % | 71 % | +1 pts | -2 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles Nashville SC Menos 2.5 | 1.36 | 72 % | 71 % | 71 % | +1 pts | -2 % | 72 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Menos 11.5 | 1.34 | 72 % | 72 % | 72 % | +0 pts | -4 % | 58 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Nashville SC Más 3.5 | 1.26 | 71 % | 74 % | 72 % | -0 pts | -10 % | 71 % | +0.6 | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Goles Menos 4.0 | 1.42 | 71 % | 69 % | 69 % | +2 pts | +1 % | 71 % | +0.4 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 18 % |
| Goles 2.º tiempo Menos 2.5 | 1.40 | 71 % | 69 % | 70 % | +1 pts | -1 % | 71 % | +0.5 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Kévin Denkey remates 2+ | 1.25 | 71 % | 71 % | 71 % | +0 pts | -11 % | 69 % | — | 1.45 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Más 0.75 | 1.38 | 70 % | 71 % | 72 % | -2 pts | -3 % | 70 % | +0.6 | 1.46 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| Córners 2.º tiempo Menos 6.5 | 1.31 | 70 % | 74 % | 71 % | -1 pts | -8 % | 68 % | +0.4 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeison Palacios anota o asiste | 11.00 | 11 % | 8 % | 12 % | -1 pts | +24 % | 5 % | — | 10.76 | Empate | Valor frágil (depende de un guion) |
| Miles Robinson anota o asiste | 9.75 | 12 % | 9 % | 13 % | -0 pts | +20 % | 8 % | — | 9.70 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 4.0 | 2.95 | 40 % | 37 % | 40 % | +0 pts | +18 % | 32 % | -0.2 | 2.64 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.93 | 60 % | 57 % | 60 % | +0 pts | +16 % | 49 % | +0.3 | 1.72 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 3.0 | 5.20 | 21 % | 21 % | 21 % | +0 pts | +12 % | 18 % | -0.7 | 5.14 | Expulsión antes del 70′ | Valor frágil (depende de un guion) · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.45 | 76 % | 73 % | 76 % | +0 pts | +11 % | 66 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Más 10.0 | 2.25 | 47 % | 47 % | 47 % | +1 pts | +7 % | 40 % | -0.0 | 2.20 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |
| Córners Más 9.0 | 1.75 | 61 % | 60 % | 60 % | +1 pts | +6 % | 53 % | +0.3 | 1.70 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.45 | 73 % | 72 % | 72 % | +1 pts | +6 % | 65 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 3.0 | 1.37 | 77 % | 78 % | 77 % | -0 pts | +6 % | 62 % | +0.7 | 1.33 | Empate | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 7.0 | 1.21 | 87 % | 84 % | 87 % | +0 pts | +5 % | 79 % | +1.2 | 1.18 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 8 % |
| Córners 1.er tiempo Más 4.0 | 1.80 | 58 % | 61 % | 58 % | -0 pts | +5 % | 43 % | +0.2 | 1.78 | Empate | Valor · asiática: devuelve 19 % |
| Córners Menos 11.0 | 1.60 | 65 % | 65 % | 65 % | -1 pts | +3 % | 55 % | +0.3 | 1.60 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |

Kelly ¼ (dato informativo, no una orden de stake): Jeison Palacios anota o asiste 0.6 % de la banca; Miles Robinson anota o asiste 0.6 % de la banca; Córners 1.er tiempo Menos 4.0 2.3 % de la banca; Córners 1.er tiempo Menos 5.0 4.2 % de la banca; Córners 1.er tiempo Menos 3.0 0.7 % de la banca; Córners 1.er tiempo Menos 6.0 6.0 % de la banca; Córners Más 10.0 1.3 % de la banca; Córners Más 9.0 2.1 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #16 | liga con Ambos Sí ≥55 %, Más 2.5 ≤1,80 y Ambos Sí ≤1,75 | Ambos marcan: Sí | 27602 partidos: Ambos Sí 56.0 % contra 56.5 % que ya da el precio (-0.5 pts ± 0.6) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí | 60 % | 62 % | 55 % | 1.66 | 1.71 | 1.16 | 8 % | Expulsión antes del 70′ | 55 % |
| Ambos 1+ tarjetas: Sí + Tarjetas FC Cincinnati Más 1.5 | 61 % | 63 % | 57 % | 1.64 | 1.68 | 1.12 | 8 % | Expulsión antes del 70′ | 58 % |
| Goles 2.º tiempo Menos 2.5 + Hándicap FC Cincinnati +3 + Tiros al arco Nashville SC Menos 8.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.06 | 7 % | Empate | 44 % |
| Goles Nashville SC Menos 4.5 + Córners 1.er tiempo Menos 5.5 + Tiros al arco Nashville SC Menos 8.5 | 62 % | 63 % | 57 % | 1.62 | 1.67 | 1.02 | 7 % | Empate | 55 % |
| Tarjetas Nashville SC Más 1.5 + Goles Nashville SC Menos 4.5 + Hándicap FC Cincinnati +3 | 60 % | 62 % | 56 % | 1.66 | 1.71 | 1.04 | 8 % | Expulsión antes del 70′ | 58 % |
| Goles FC Cincinnati Menos 3.5 + Tiros al arco FC Cincinnati Más 1.5 + Córners FC Cincinnati Más 3.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.01 | 9 % | Partido abierto (ambos marcan y 3+ goles) | 53 % |
| Tarjetas FC Cincinnati Más 1.5 + Tiros al arco Más 5.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.0 | 6 % | Expulsión antes del 70′ | 58 % |
| Tarjetas Nashville SC Más 1.5 + Tiros al arco Más 5.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.0 | 6 % | Expulsión antes del 70′ | 57 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.