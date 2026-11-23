# St. Louis City SC - Los Angeles FC
EE. UU. MLS · 2026-11-23 20:00

**Tipo de partido:** Parejo · abierto · normal · **Favorito:** St. Louis City SC · primer gol: local 48 %, visitante 47 %, nadie 5 % · gol del favorito antes del 35′: 32 %

**Base de la liga:** Estados Unidos MLS · 2.97 goles/partido, Más 2.5 59 %, ambos marcan 60 % (1159 partidos ago-2022/nov-2026)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), 1.er tiempo (Menos) y empate al descanso, Ambos marcan, Empate / doble oportunidad / HT-FT X. Poco favorecidos: Hándicap y victoria.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; parejo: más duelos y más faltas |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Sorpresa: gana el no favorito | 31 % |
| Partido abierto (ambos marcan y 3+ goles) | 28 % |
| Empate | 16 % |
| Expulsión antes del 70′ | 10 % |
| Favorito gana en partido trabado | 8 % |
| Favorito golpea temprano y gana | 7 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.53 | 14.4 | 4.9 | 5.3 | 11.8 | 2.5 |
| visitante | 1.50 | 14.4 | 4.9 | 5.3 | 11.8 | 2.5 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.0) · 1–5 | 1.5 (1.6) · 0–3 | 1.5 (1.5) · 0–3 | 1.3 (1.3) · 0–3 | 1.7 (1.8) · 0–3 |
| Córners | 10.5 (10.5) · 6–15 | 5.2 · 2–9 | 5.2 · 2–9 | 4.7 (5.1) · 2–8 | 5.8 (5.6) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 5.0 (4.9) · 2–8 | 2.5 (2.5) · 1–4 | 2.5 (2.5) · 1–5 | 1.6 (1.7) · 0–3 | 3.3 · 1–6 |
| Remates | 28.7 (28.7) · 21–37 | 14.4 (14.4) · 9–21 | 14.3 (14.4) · 9–21 | 12.9 · 8–18 | 15.9 · 11–22 |
| Tiros al arco | 9.8 (9.8) · 6–14 | 4.9 (4.9) · 2–8 | 4.9 (4.9) · 2–8 | 4.4 · 2–7 | 5.4 · 2–9 |
| Faltas | 23.6 · 17–30 | 11.8 · 7–16 | 11.8 · 7–16 | 10.5 · 6–15 | 13.0 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.1 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 40.1 · 29–52 | 19.9 · 12–28 | 20.1 · 12–28 | 17.9 · 12–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 3.4 · 1–6 | 3.4 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Menos 2.5 | 1.31 | 75 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (56 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.52 | 63 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | No hay empate | 1.29 | 73 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 7.0 | 1.26 | 84 % | 75 % | Favorito gana en partido trabado (80 %) | Partido abierto (ambos marcan y 3+ goles) (75 %) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Tarjetas | Tarjetas Más 3.5 | 1.39 | 69 % | 65 % | Expulsión antes del 70′ (96 %) | Favorito golpea temprano y gana (60 %) | Alta probabilidad |
| Remates | Remates Más 24.5 | 1.25 | 76 % | 66 % | Partido abierto (ambos marcan y 3+ goles) (86 %) | Empate (66 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco Los Angeles FC Menos 6.5 | 1.25 | 77 % | 65 % | Favorito gana en partido trabado (94 %) | Sorpresa: gana el no favorito (65 %) | Alta probabilidad |
| Jugadores | Timo Baumgartl anota o asiste | 11.00 | 12 % | 7 % | Partido abierto (ambos marcan y 3+ goles) (20 %) | Empate (7 %) | Valor frágil (depende de un guion) |
| Quién saca más | Más corners: St. Louis City SC | 2.22 | 43 % | 40 % | Sorpresa: gana el no favorito (49 %) | Favorito golpea temprano y gana (30 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 7.0 | 1.26 | 84 % | 81 % | 84 % | +0 pts | +6 % | 75 % | +1.0 | 1.22 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners 1.er tiempo Más 3.0 | 1.30 | 81 % | 81 % | 81 % | +0 pts | +5 % | 68 % | +0.8 | 1.27 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 16 % |
| Córners Menos 13.0 | 1.29 | 79 % | 78 % | 79 % | +0 pts | +2 % | 71 % | +0.7 | 1.31 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners 1.er tiempo Menos 6.5 | 1.26 | 78 % | 77 % | 78 % | +0 pts | -1 % | 76 % | +0.8 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 8.0 | 1.33 | 77 % | 77 % | 77 % | +0 pts | +3 % | 70 % | +0.7 | 1.33 | Expulsión antes del 70′ | Alta probabilidad · asiática: devuelve 10 % |
| Tiros al arco Los Angeles FC Menos 6.5 | 1.25 | 77 % | 78 % | 77 % | +0 pts | -3 % | 65 % | +0.7 | 1.33 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco St. Louis City SC Menos 6.5 | 1.25 | 77 % | 78 % | 77 % | +0 pts | -4 % | 61 % | +0.7 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates Más 24.5 | 1.25 | 76 % | 78 % | 76 % | +0 pts | -5 % | 66 % | +0.7 | 1.35 | Empate | Alta probabilidad |
| Remates Menos 32.5 | 1.26 | 76 % | 77 % | 76 % | +0 pts | -5 % | 66 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.31 | 75 % | 74 % | 75 % | +0 pts | -1 % | 76 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Más 7.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -4 % | 57 % | +0.7 | 1.37 | Empate | Alta probabilidad |
| Córners Menos 12.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -4 % | 72 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates St. Louis City SC Más 11.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 68 % | +0.6 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates Los Angeles FC Más 11.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 66 % | +0.6 | 1.40 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| No hay empate | 1.29 | 73 % | 73 % | 73 % | +0 pts | -5 % | 73 % | — | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Goles 1.er tiempo Más 0.5 | 1.35 | 73 % | 72 % | 73 % | +0 pts | -2 % | 73 % | +0.7 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Menos 6.0 | 1.55 | 72 % | 69 % | 72 % | +0 pts | +12 % | 62 % | +0.6 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Tiros al arco Menos 11.5 | 1.34 | 72 % | 72 % | 72 % | +0 pts | -4 % | 57 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Hándicap St. Louis City SC +0.75 | 1.37 | 72 % | 71 % | 72 % | +0 pts | -2 % | 72 % | — | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 10 % · ★ enfoque a favor |
| Córners St. Louis City SC Más 3.5 | 1.30 | 72 % | 72 % | 72 % | +0 pts | -7 % | 71 % | +0.6 | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Remates Los Angeles FC Menos 16.5 | 1.32 | 72 % | 73 % | 72 % | +0 pts | -5 % | 66 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates St. Louis City SC Menos 16.5 | 1.32 | 72 % | 73 % | 72 % | +0 pts | -6 % | 65 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Más 3.5 | 1.30 | 71 % | 74 % | 71 % | +0 pts | -7 % | 70 % | +0.6 | 1.44 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 8.5 | 1.33 | 71 % | 73 % | 71 % | +0 pts | -5 % | 71 % | +0.6 | 1.45 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Armindo Sieb tiros al arco 1+ | 1.25 | 71 % | 71 % | 71 % | +0 pts | -11 % | 66 % | — | 1.45 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Virgilio Olaya anota o asiste | 13.50 | 10 % | 6 % | 10 % | +0 pts | +33 % | 6 % | — | 12.74 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Timo Baumgartl anota o asiste | 11.00 | 12 % | 8 % | 12 % | +0 pts | +31 % | 7 % | — | 10.07 | Empate | Valor frágil (depende de un guion) |
| Yevhen Cheberko anota o asiste | 10.00 | 12 % | 9 % | 12 % | +0 pts | +22 % | 7 % | — | 9.78 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Eddie Segura anota o asiste | 10.00 | 12 % | 9 % | 12 % | +0 pts | +22 % | 7 % | — | 9.80 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Nkosi Tafari anota o asiste | 10.00 | 12 % | 9 % | 12 % | +0 pts | +20 % | 6 % | — | 10.00 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Dante Polvara anota o asiste | 6.50 | 18 % | 13 % | 18 % | +0 pts | +16 % | 10 % | — | 6.30 | Empate | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 4.0 | 3.30 | 35 % | 33 % | 35 % | +0 pts | +15 % | 28 % | -0.3 | 3.04 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 5.0 | 2.10 | 55 % | 52 % | 55 % | +0 pts | +15 % | 45 % | +0.1 | 1.89 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % |
| Igor Jesus Lima anota o asiste | 6.80 | 17 % | 13 % | 17 % | +0 pts | +14 % | 10 % | — | 6.74 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Ryan Porteous anota o asiste | 6.00 | 19 % | 14 % | 19 % | +0 pts | +12 % | 10 % | — | 5.98 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 6.0 | 1.55 | 72 % | 69 % | 72 % | +0 pts | +12 % | 62 % | +0.6 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners Menos 10.0 | 2.35 | 46 % | 45 % | 46 % | +0 pts | +7 % | 38 % | -0.1 | 2.29 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Menos 7.0 | 1.26 | 84 % | 81 % | 84 % | +0 pts | +6 % | 75 % | +1.0 | 1.22 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners Menos 11.0 | 1.82 | 58 % | 58 % | 58 % | +0 pts | +6 % | 50 % | +0.2 | 1.78 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 4.0 | 1.67 | 63 % | 65 % | 63 % | +0 pts | +6 % | 50 % | +0.3 | 1.63 | Favorito gana en partido trabado | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 3.0 | 1.30 | 81 % | 81 % | 81 % | +0 pts | +5 % | 68 % | +0.8 | 1.27 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 16 % |
| Córners Menos 12.0 | 1.50 | 70 % | 69 % | 70 % | +0 pts | +5 % | 61 % | +0.5 | 1.48 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Virgilio Olaya anota o asiste 0.7 % de la banca; Timo Baumgartl anota o asiste 0.8 % de la banca; Yevhen Cheberko anota o asiste 0.6 % de la banca; Eddie Segura anota o asiste 0.6 % de la banca; Nkosi Tafari anota o asiste 0.6 % de la banca; Dante Polvara anota o asiste 0.7 % de la banca; Córners 1.er tiempo Menos 4.0 1.7 % de la banca; Córners 1.er tiempo Menos 5.0 3.4 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #16 | liga con Ambos Sí ≥55 %, Más 2.5 ≤1,80 y Ambos Sí ≤1,75 | Ambos marcan: Sí | 27602 partidos: Ambos Sí 56.0 % contra 56.5 % que ya da el precio (-0.5 pts ± 0.6) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Tiros al arco Los Angeles FC Menos 8.5 + Tarjetas Más 3.5 | 62 % | 63 % | 58 % | 1.60 | 1.65 | 1.13 | 8 % | Expulsión antes del 70′ | 56 % |
| Ambos 1+ tarjetas: Sí + Tiros al arco St. Louis City SC Menos 8.5 + Tarjetas Más 3.5 | 62 % | 62 % | 58 % | 1.61 | 1.66 | 1.13 | 8 % | Expulsión antes del 70′ | 56 % |
| Goles Los Angeles FC Menos 3.5 + Tiros al arco Los Angeles FC Menos 8.5 + St. Louis City SC o empate | 62 % | 62 % | 57 % | 1.62 | 1.67 | 1.09 | 6 % | Favorito gana en partido trabado | 0 % |
| Córners Menos 16.5 + Tiros al arco Más 5.5 + Ambos marcan: Sí | 60 % | 58 % | 55 % | 1.66 | 1.71 | 1.08 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 53 % |
| Tiros al arco Más 5.5 + Ambos marcan: Sí | 61 % | 61 % | 56 % | 1.63 | 1.68 | 1.05 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 56 % |
| Goles Los Angeles FC Menos 3.5 + Córners Menos 16.5 + St. Louis City SC o empate | 61 % | 61 % | 56 % | 1.64 | 1.69 | 1.05 | 6 % | Favorito gana en partido trabado | 0 % |
| Goles Menos 6.5 + Tarjetas St. Louis City SC Menos 2.5 | 54 % | 54 % | 49 % | 1.87 | 1.92 | 1.0 | 6 % | Favorito golpea temprano y gana | 54 % |
| Goles Menos 6.5 + Tarjetas Los Angeles FC Menos 2.5 | 53 % | 54 % | 48 % | 1.88 | 1.94 | 1.0 | 6 % | Favorito golpea temprano y gana | 54 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.