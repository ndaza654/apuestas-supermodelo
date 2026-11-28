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
| Partido abierto (ambos marcan y 3+ goles) | 35 % |
| Sorpresa: gana el no favorito | 26 % |
| Empate | 12 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 8 % |
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
| Goles | 3.3 (3.4) · 1–6 | 1.5 (1.5) · 0–3 | 1.8 (1.9) · 0–4 | 1.5 (1.4) · 0–3 | 1.9 (1.9) · 0–4 |
| Córners | 10.0 (10.0) · 6–14 | 5.0 · 2–9 | 5.0 · 2–8 | 4.4 (4.8) · 2–7 | 5.6 (5.3) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 4.6 (4.2) · 2–8 | 2.3 (2.2) · 1–4 | 2.3 (2.2) · 1–4 | 1.5 (1.5) · 0–3 | 3.0 · 1–6 |
| Remates | 28.5 (28.3) · 21–36 | 13.8 (13.7) · 8–20 | 14.7 (14.7) · 9–21 | 12.7 · 8–18 | 15.8 · 11–22 |
| Tiros al arco | 9.9 (9.8) · 6–14 | 4.7 (4.7) · 2–8 | 5.2 (5.2) · 2–8 | 4.4 · 2–7 | 5.5 · 3–9 |
| Faltas | 24.3 · 18–31 | 12.2 · 8–17 | 12.1 · 8–17 | 10.9 · 7–15 | 13.4 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.1 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 8.9 · 5–13 |
| Saques de banda | 39.9 · 29–52 | 20.0 · 12–28 | 19.9 · 12–28 | 17.8 · 11–25 | 22.0 · 15–30 |
| Atajadas del portero | — | 3.3 · 1–6 | 3.2 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.30 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (60 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.42 | 67 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · ★ enfoque a favor |
| Resultado y hándicap | No hay empate | 1.26 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad |
| Córners | Córners 2.º tiempo Más 3.5 | 1.26 | 79 % | 78 % | Partido abierto (ambos marcan y 3+ goles) (81 %) | Expulsión antes del 70′ (73 %) | Alta probabilidad |
| Tarjetas | Tarjetas Nashville SC Más 1.5 | 1.52 | 67 % | 64 % | Expulsión antes del 70′ (86 %) | Favorito golpea temprano y gana (58 %) | Alta probabilidad |
| Remates | Remates Más 26.5 | 1.55 | 62 % | 53 % | Partido abierto (ambos marcan y 3+ goles) (72 %) | Favorito gana en partido trabado (48 %) | Justa |
| Tiros al arco | Tiros al arco Nashville SC Menos 6.5 | 1.31 | 73 % | 59 % | Empate (87 %) | Partido abierto (ambos marcan y 3+ goles) (59 %) | Alta probabilidad |
| Jugadores | Andy Najar anota o asiste | 2.50 | 38 % | 22 % | Partido abierto (ambos marcan y 3+ goles) (54 %) | Sorpresa: gana el no favorito (22 %) | Cara |
| Quién saca más | Más corners: FC Cincinnati | 2.47 | 41 % | 34 % | Favorito golpea temprano y gana (54 %) | Sorpresa: gana el no favorito (34 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 2.º tiempo Más 3.5 | 1.26 | 79 % | 77 % | 78 % | +1 pts | -1 % | 78 % | +0.8 | 1.31 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.37 | 77 % | 78 % | 77 % | -1 pts | +5 % | 60 % | +0.7 | 1.34 | Empate | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.44 | 77 % | 74 % | 77 % | +0 pts | +11 % | 67 % | +0.7 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| No hay empate | 1.26 | 77 % | 75 % | 75 % | +2 pts | -3 % | 77 % | — | 1.34 | Empate | Alta probabilidad |
| Hándicap FC Cincinnati +2 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -2 % | 76 % | — | 1.35 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Menos 4.5 | 1.30 | 76 % | 75 % | 75 % | +0 pts | -2 % | 76 % | +0.7 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.28 | 76 % | 76 % | 76 % | -1 pts | -3 % | 76 % | +0.8 | 1.36 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners Menos 12.0 | 1.36 | 75 % | 75 % | 76 % | -0 pts | +2 % | 66 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Tiros al arco Nashville SC Menos 6.5 | 1.31 | 73 % | 74 % | 74 % | -0 pts | -4 % | 59 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 8.0 | 1.44 | 73 % | 72 % | 72 % | +0 pts | +5 % | 64 % | +0.6 | 1.42 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Goles Nashville SC Menos 2.5 | 1.35 | 72 % | 71 % | 72 % | +0 pts | -3 % | 72 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Nashville SC Más 3.5 | 1.25 | 71 % | 75 % | 72 % | -1 pts | -11 % | 71 % | +0.6 | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Más 0.75 | 1.37 | 71 % | 71 % | 72 % | -1 pts | -3 % | 71 % | +0.6 | 1.45 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| Kévin Denkey remates 2+ | 1.25 | 71 % | 71 % | 71 % | +0 pts | -11 % | 68 % | — | 1.45 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Nashville SC o empate | 1.37 | 71 % | 71 % | 71 % | -1 pts | -3 % | 71 % | — | 1.46 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Nashville SC +1 | 1.37 | 71 % | 71 % | 71 % | -1 pts | -3 % | 70 % | — | 1.46 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Nashville SC +0.5 | 1.38 | 71 % | 71 % | 71 % | -1 pts | -3 % | 70 % | — | 1.46 | Sorpresa: gana el no favorito | Alta probabilidad |
| Elias Saad remates 2+ | 1.26 | 70 % | 71 % | 70 % | +0 pts | -12 % | 68 % | — | 1.47 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Goles Menos 4.0 | 1.42 | 70 % | 69 % | 70 % | +0 pts | -0 % | 70 % | +0.4 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 18 % |
| Goles 2.º tiempo Menos 2.5 | 1.40 | 70 % | 69 % | 71 % | -0 pts | -2 % | 70 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 11.5 | 1.36 | 70 % | 71 % | 70 % | -1 pts | -5 % | 67 % | +0.4 | 1.48 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 2.º tiempo Menos 6.5 | 1.32 | 70 % | 73 % | 71 % | -1 pts | -8 % | 67 % | +0.4 | 1.48 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Kenji Mboma Dem remates 2+ | 1.26 | 70 % | 71 % | 69 % | +0 pts | -12 % | 66 % | — | 1.48 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Menos 5.5 | 1.44 | 69 % | 67 % | 69 % | +0 pts | -0 % | 68 % | +0.5 | 1.49 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco FC Cincinnati Más 3.5 | 1.40 | 68 % | 69 % | 67 % | +0 pts | -5 % | 56 % | +0.5 | 1.52 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 4.5 | 2.20 | 47 % | 42 % | 42 % | +5 pts | +2 % | 42 % | +0.0 | 2.24 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Ambos 2+ tarjetas: Sí | 2.10 | 49 % | 44 % | 44 % | +4 pts | +2 % | 46 % | — | 2.14 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeison Palacios anota o asiste | 11.00 | 12 % | 8 % | 12 % | -0 pts | +28 % | 6 % | — | 10.41 | Empate | Valor frágil (depende de un guion) |
| Miles Robinson anota o asiste | 9.75 | 13 % | 9 % | 13 % | +0 pts | +26 % | 7 % | — | 9.18 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Obinna Nwobodo anota o asiste | 7.20 | 17 % | 12 % | 16 % | +0 pts | +19 % | 11 % | — | 6.86 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 4.0 | 2.92 | 40 % | 38 % | 40 % | +1 pts | +18 % | 33 % | -0.2 | 2.61 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 5.0 | 1.91 | 60 % | 57 % | 60 % | +0 pts | +16 % | 51 % | +0.3 | 1.71 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % |
| Kyle Smith anota o asiste | 6.60 | 17 % | 13 % | 18 % | -0 pts | +15 % | 11 % | — | 6.48 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 3.0 | 5.10 | 22 % | 21 % | 21 % | +1 pts | +12 % | 18 % | -0.7 | 5.02 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.44 | 77 % | 74 % | 77 % | +0 pts | +11 % | 67 % | +0.7 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Más 10.0 | 2.25 | 48 % | 47 % | 46 % | +1 pts | +7 % | 42 % | +0.0 | 2.20 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 9.0 | 1.75 | 60 % | 60 % | 60 % | +1 pts | +6 % | 53 % | +0.3 | 1.71 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Menos 7.0 | 1.21 | 87 % | 84 % | 87 % | +0 pts | +5 % | 80 % | +1.2 | 1.18 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 8 % |
| Córners 1.er tiempo Más 4.0 | 1.83 | 58 % | 60 % | 58 % | -1 pts | +5 % | 44 % | +0.2 | 1.80 | Empate | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 3.0 | 1.37 | 77 % | 78 % | 77 % | -1 pts | +5 % | 60 % | +0.7 | 1.34 | Empate | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners Más 8.0 | 1.44 | 73 % | 72 % | 72 % | +0 pts | +5 % | 64 % | +0.6 | 1.42 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 10.0 | 2.02 | 52 % | 52 % | 53 % | -1 pts | +5 % | 43 % | -0.0 | 2.01 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Menos 11.0 | 1.60 | 65 % | 65 % | 65 % | -1 pts | +3 % | 55 % | +0.3 | 1.60 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |

Kelly ¼ (dato informativo, no una orden de stake): Jeison Palacios anota o asiste 0.7 % de la banca; Miles Robinson anota o asiste 0.7 % de la banca; Obinna Nwobodo anota o asiste 0.8 % de la banca; Córners 1.er tiempo Menos 4.0 2.3 % de la banca; Córners 1.er tiempo Menos 5.0 4.3 % de la banca; Kyle Smith anota o asiste 0.7 % de la banca; Córners 1.er tiempo Menos 3.0 0.7 % de la banca; Córners 1.er tiempo Menos 6.0 6.0 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #16 | liga con Ambos Sí ≥55 %, Más 2.5 ≤1,80 y Ambos Sí ≤1,75 | Ambos marcan: Sí | 27602 partidos: Ambos Sí 56.0 % contra 56.5 % que ya da el precio (-0.5 pts ± 0.6) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Tarjetas Nashville SC Más 1.5 | 62 % | 63 % | 57 % | 1.62 | 1.67 | 1.11 | 8 % | Expulsión antes del 70′ | 59 % |
| Ambos 1+ tarjetas: Sí + Tarjetas FC Cincinnati Más 1.5 | 61 % | 63 % | 57 % | 1.63 | 1.68 | 1.11 | 8 % | Expulsión antes del 70′ | 59 % |
| Goles Nashville SC Menos 4.5 + Hándicap FC Cincinnati +3 + Ambos marcan: Sí | 62 % | 63 % | 57 % | 1.61 | 1.66 | 1.06 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 62 % |
| Tarjetas Nashville SC Más 1.5 + Goles Nashville SC Menos 4.5 + Hándicap FC Cincinnati +3 | 61 % | 62 % | 56 % | 1.64 | 1.69 | 1.04 | 8 % | Expulsión antes del 70′ | 58 % |
| Goles Menos 6.5 + Córners Más 5.5 + Nashville SC o empate | 62 % | 62 % | 58 % | 1.61 | 1.66 | 1.0 | 6 % | Empate | 0 % |
| Tarjetas FC Cincinnati Más 1.5 + Córners Más 5.5 | 62 % | 62 % | 57 % | 1.62 | 1.67 | 1.0 | 6 % | Expulsión antes del 70′ | 60 % |
| Goles FC Cincinnati Menos 3.5 + Nashville SC o empate + Córners FC Cincinnati Más 2.5 | 58 % | 59 % | 54 % | 1.73 | 1.78 | 1.06 | 11 % | Favorito golpea temprano y gana | 0 % |
| Goles FC Cincinnati Menos 3.5 + Ambos marcan: Sí | 62 % | 63 % | 58 % | 1.60 | 1.65 | 0.98 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 49 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.