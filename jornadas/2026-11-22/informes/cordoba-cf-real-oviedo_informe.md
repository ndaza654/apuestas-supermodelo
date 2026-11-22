# Cordoba CF - Real Oviedo
España Segunda División · 2026-11-22 08:00

**Tipo de partido:** Favorito leve · abierto · caliente · **Favorito:** Cordoba CF · primer gol: local 56 %, visitante 39 %, nadie 5 % · gol del favorito antes del 35′: 37 %

**Base de la liga:** España Segunda · 2.36 goles/partido, Más 2.5 43 %, ambos marcan 49 % · córners 9.3 · tarjetas (amarilla 1, roja 2) 5.4 (1881 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan, Córners totales (Más).

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Córners totales (Más) | ✅ favorece | se espera claramente por encima de lo normal de la liga / del precio |
| Resultado / hándicap | ➖ neutro | Cordoba CF favorito leve: el precio ya lo recoge |
| Tarjetas y faltas | ➖ neutro | árbitro cerca de la media y sin otros factores de fricción |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 31 % |
| Sorpresa: gana el no favorito | 22 % |
| Expulsión antes del 70′ | 17 % |
| Empate | 13 % |
| Favorito golpea temprano y gana | 9 % |
| Favorito gana en partido trabado | 8 % |

## Lo que cambió el contexto
- Árbitro Palencia D.: 6.15 tarjetas/partido contra 5.4 de la liga (prior de la liga (España Segunda)) en 56 partidos → tarjetas ×1.06 (encogido por muestra).
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.79 | 13.5 | 4.5 | 5.4 | 13.2 | 3.2 |
| visitante | 1.29 | 10.5 | 3.4 | 5.4 | 13.0 | 4.0 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.1 (3.1) · 1–5 | 1.8 (1.8) · 0–3 | 1.3 (1.3) · 0–3 | 1.4 (1.3) · 0–3 | 1.7 (1.8) · 0–3 |
| Córners | 10.8 (10.8) · 6–15 | 5.4 · 2–9 | 5.4 · 2–9 | 4.9 (5.2) · 2–8 | 5.9 (5.7) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 7.3 (6.8) · 3–11 | 3.2 (3.0) · 1–6 | 4.0 (3.8) · 2–7 | 2.4 (2.4) · 0–5 | 4.9 · 2–8 |
| Remates | 24.0 · 17–31 | 13.4 · 8–19 | 10.5 · 6–16 | 10.8 · 6–15 | 13.2 · 8–18 |
| Tiros al arco | 8.0 · 4–12 | 4.5 · 2–8 | 3.5 · 1–6 | 3.6 · 1–6 | 4.4 · 2–7 |
| Faltas | 26.3 · 20–33 | 13.2 · 9–18 | 13.1 · 8–18 | 11.8 · 7–16 | 14.5 · 10–20 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 15.8 · 10–23 | 7.9 · 4–13 | 7.9 · 4–13 | 7.0 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 40.0 · 29–52 | 20.1 · 13–28 | 19.9 · 12–28 | 17.8 · 11–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 2.2 · 0–4 | 2.7 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Menos 2.5 | 1.32 | 75 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (55 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.53 | 63 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | No hay empate | 1.26 | 75 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad · cuota por debajo de la justa |
| Córners | Córners 1.er tiempo Menos 7.0 | 1.31 | 82 % | 74 % | Expulsión antes del 70′ (76 %) | Partido abierto (ambos marcan y 3+ goles) (74 %) | Alta probabilidad · Valor · asiática: devuelve 10 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas | Ambos 2+ tarjetas: Sí | 1.33 | 78 % | 75 % | Expulsión antes del 70′ (89 %) | Favorito golpea temprano y gana (68 %) | Alta probabilidad · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Quién saca más | Más tarjetas: Real Oviedo | 1.75 | 55 % | 54 % | Expulsión antes del 70′ (59 %) | Favorito gana en partido trabado (53 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Más 3.0 | 1.26 | 83 % | 83 % | 83 % | +0 pts | +4 % | 70 % | +0.8 | 1.24 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 15 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 7.0 | 1.31 | 82 % | 79 % | 82 % | -0 pts | +7 % | 74 % | +0.9 | 1.26 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Más 8.0 | 1.28 | 79 % | 79 % | 80 % | -0 pts | +2 % | 69 % | +0.8 | 1.30 | Expulsión antes del 70′ | Alta probabilidad · asiática: devuelve 9 % · ★ enfoque a favor |
| Ambos 2+ tarjetas: Sí | 1.33 | 78 % | 73 % | 74 % | +4 pts | +3 % | 75 % | — | 1.33 | Favorito golpea temprano y gana | Alta probabilidad · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Menos 13.0 | 1.34 | 76 % | 76 % | 76 % | +0 pts | +2 % | 67 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Córners 1.er tiempo Menos 6.5 | 1.31 | 75 % | 74 % | 76 % | -0 pts | -1 % | 74 % | +0.7 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| No hay empate | 1.26 | 75 % | 75 % | 75 % | +0 pts | -5 % | 75 % | — | 1.37 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Goles 2.º tiempo Menos 2.5 | 1.32 | 75 % | 73 % | 74 % | +0 pts | -2 % | 75 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Hándicap Real Oviedo +2 | 1.31 | 75 % | 74 % | 74 % | +0 pts | -2 % | 74 % | — | 1.38 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Más 8.5 | 1.28 | 74 % | 76 % | 74 % | +0 pts | -5 % | 71 % | +0.7 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Más 3.5 | 1.26 | 74 % | 77 % | 74 % | +0 pts | -7 % | 72 % | +0.6 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Hándicap Cordoba CF +1 | 1.32 | 74 % | 74 % | 74 % | -0 pts | -3 % | 74 % | — | 1.40 | Sorpresa: gana el no favorito | Alta probabilidad |
| Cordoba CF o empate | 1.32 | 74 % | 73 % | 74 % | -0 pts | -3 % | 74 % | — | 1.40 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.33 | 73 % | 73 % | 74 % | -1 pts | -2 % | 73 % | +0.8 | 1.40 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Goles Real Oviedo Más 0.5 | 1.32 | 73 % | 73 % | 73 % | -0 pts | -3 % | 73 % | +0.7 | 1.40 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Goles Cordoba CF Menos 2.5 | 1.31 | 73 % | 74 % | 74 % | -0 pts | -4 % | 73 % | +0.6 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Hándicap Real Oviedo +1.25 | 1.38 | 71 % | 71 % | 71 % | +0 pts | -2 % | 71 % | — | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 12 % |
| Córners Menos 12.5 | 1.34 | 71 % | 72 % | 71 % | -0 pts | -5 % | 68 % | +0.5 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Hándicap Cordoba CF +0.25 | 1.40 | 70 % | 70 % | 70 % | +0 pts | -2 % | 70 % | — | 1.47 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 13 % |
| Córners Más 9.0 | 1.50 | 69 % | 69 % | 69 % | +0 pts | +4 % | 59 % | +0.5 | 1.48 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Más 5.5 | 1.50 | 69 % | 64 % | 64 % | +5 pts | +3 % | 63 % | +0.6 | 1.50 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 6.0 | 1.62 | 69 % | 66 % | 69 % | -0 pts | +12 % | 60 % | +0.5 | 1.50 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 14 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Goles 1.er tiempo Menos 1.75 | 1.39 | 69 % | 70 % | 69 % | -0 pts | -4 % | 69 % | +0.3 | 1.50 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % |
| Goles Menos 3.75 | 1.42 | 68 % | 69 % | 69 % | -0 pts | -3 % | 68 % | +0.4 | 1.51 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Goles 1.er tiempo Más 0.75 | 1.45 | 68 % | 67 % | 68 % | -0 pts | -1 % | 68 % | +0.5 | 1.51 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 6.5 | 1.87 | 56 % | 50 % | 50 % | +6 pts | +5 % | 49 % | +0.2 | 1.85 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Más 7.5 | 2.45 | 43 % | 37 % | 37 % | +6 pts | +6 % | 36 % | -0.1 | 2.42 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Cordoba CF Más 2.5 | 1.65 | 63 % | 57 % | 57 % | +5 pts | +3 % | 58 % | +0.4 | 1.65 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Más 5.5 | 1.50 | 69 % | 64 % | 64 % | +5 pts | +3 % | 63 % | +0.6 | 1.50 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Real Oviedo Más 3.5 | 1.82 | 56 % | 52 % | 52 % | +5 pts | +3 % | 51 % | +0.3 | 1.84 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Tarjetas 1.er tiempo Más 2.5 | 2.12 | 45 % | 43 % | 41 % | +4 pts | -5 % | 38 % | -0.1 | 2.33 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Real Oviedo Más 7.5 | 7.70 | 16 % | 12 % | 17 % | -1 pts | +22 % | 12 % | -0.8 | 7.23 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ★ enfoque a favor · Línea contra el guion (Más de un equipo que perdió: 2/11) · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Real Oviedo Más 6.5 | 5.00 | 24 % | 19 % | 25 % | -1 pts | +22 % | 20 % | -0.4 | 4.47 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ★ enfoque a favor · Línea contra el guion (Más de un equipo que perdió: 2/11) · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Más corners: Real Oviedo | 3.65 | 33 % | 22 % | 34 % | -1 pts | +19 % | 27 % | — | 3.27 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 4.0 | 3.65 | 32 % | 30 % | 32 % | -0 pts | +16 % | 27 % | -0.4 | 3.35 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) · asiática: devuelve 17 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Real Oviedo Más 5.5 | 3.20 | 36 % | 29 % | 37 % | -1 pts | +15 % | 32 % | -0.0 | 2.95 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · ★ enfoque a favor · Línea contra el guion (Más de un equipo que perdió: 2/11) · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 5.0 | 2.25 | 51 % | 49 % | 52 % | -1 pts | +15 % | 43 % | +0.1 | 2.04 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 6.0 | 1.62 | 69 % | 66 % | 69 % | -0 pts | +12 % | 60 % | +0.5 | 1.50 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 14 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 7.0 | 1.31 | 82 % | 79 % | 82 % | -0 pts | +7 % | 74 % | +0.9 | 1.26 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Real Oviedo Más 4.5 | 2.12 | 50 % | 44 % | 52 % | -1 pts | +7 % | 46 % | +0.3 | 2.07 | Expulsión antes del 70′ | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · ★ enfoque a favor · Línea contra el guion (Más de un equipo que perdió: 2/11) · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Más 4.0 | 1.60 | 66 % | 68 % | 66 % | +0 pts | +6 % | 54 % | +0.4 | 1.55 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 17 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Más 7.5 | 2.45 | 43 % | 37 % | 37 % | +6 pts | +6 % | 36 % | -0.1 | 2.42 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Más 6.5 | 1.87 | 56 % | 50 % | 50 % | +6 pts | +5 % | 49 % | +0.2 | 1.85 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Menos 11.0 | 1.93 | 54 % | 54 % | 54 % | -0 pts | +5 % | 46 % | +0.1 | 1.91 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Más 11.0 | 2.32 | 45 % | 45 % | 45 % | +0 pts | +5 % | 36 % | -0.1 | 2.32 | Expulsión antes del 70′ | Valor · asiática: devuelve 11 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Más 10.0 | 1.82 | 58 % | 58 % | 57 % | +0 pts | +5 % | 47 % | +0.2 | 1.80 | Expulsión antes del 70′ | Valor · asiática: devuelve 11 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Más 3.0 | 1.26 | 83 % | 83 % | 83 % | +0 pts | +4 % | 70 % | +0.8 | 1.24 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 15 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Más 9.0 | 1.50 | 69 % | 69 % | 69 % | +0 pts | +4 % | 59 % | +0.5 | 1.48 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % · ★ enfoque a favor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners Menos 12.0 | 1.57 | 66 % | 66 % | 66 % | -0 pts | +4 % | 57 % | +0.3 | 1.56 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Tarjetas Más 5.5 | 1.50 | 69 % | 64 % | 64 % | +5 pts | +3 % | 63 % | +0.6 | 1.50 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+5 pts) · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Ambos 2+ tarjetas: Sí | 1.33 | 78 % | 73 % | 74 % | +4 pts | +3 % | 75 % | — | 1.33 | Favorito golpea temprano y gana | Alta probabilidad · Valor · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |
| Córners 1.er tiempo Menos 8.0 | 1.15 | 90 % | 87 % | 90 % | -0 pts | +3 % | 84 % | +1.4 | 1.15 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 6 % · Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |

Kelly ¼ (dato informativo, no una orden de stake): Córners Real Oviedo Más 7.5 0.8 % de la banca; Córners Real Oviedo Más 6.5 1.4 % de la banca; Más corners: Real Oviedo 1.8 % de la banca; Córners 1.er tiempo Menos 4.0 1.5 % de la banca; Córners Real Oviedo Más 5.5 1.7 % de la banca; Córners 1.er tiempo Menos 5.0 2.9 % de la banca; Córners 1.er tiempo Menos 6.0 4.7 % de la banca; Córners 1.er tiempo Menos 7.0 5.9 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 2+ tarjetas: Sí + Tarjetas Cordoba CF Más 2.5 | 59 % | 60 % | 54 % | 1.70 | 1.75 | 1.21 | 9 % | Expulsión antes del 70′ | 55 % |
| ↳ Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |  |  |  |  |  |  |  |  |  |
| Cordoba CF o empate + Descanso o final: Cordoba CF | 55 % | 55 % | 50 % | 1.83 | 1.88 | 1.29 | 9 % | Favorito golpea temprano y gana | 0 % |
| Goles Real Oviedo Menos 3.5 + Cordoba CF o empate + Descanso o final: Cordoba CF | 54 % | 54 % | 50 % | 1.84 | 1.90 | 1.34 | 10 % | Favorito golpea temprano y gana | 0 % |
| Ambos 2+ tarjetas: Sí + Tarjetas Cordoba CF Más 2.5 + Goles Menos 6.5 | 57 % | 58 % | 52 % | 1.75 | 1.81 | 1.22 | 10 % | Expulsión antes del 70′ | 51 % |
| ↳ Liga con historial propio atípico (ESPAÑA: 9/12 contra 53 % del precio) |  |  |  |  |  |  |  |  |  |
| Córners Menos 16.5 + Ambos marcan: Sí | 61 % | 59 % | 56 % | 1.65 | 1.70 | 1.03 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 56 % |
| Hándicap Real Oviedo +3 + Ambos marcan: Sí | 59 % | 59 % | 54 % | 1.71 | 1.76 | 1.05 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 55 % |
| Córners Real Oviedo Más 3.5 + Hándicap Real Oviedo +3 + Goles Cordoba CF Menos 3.5 | 56 % | 62 % | 52 % | 1.78 | 1.84 | 1.05 | 10 % | Empate | 52 % |
| Córners Real Oviedo Más 3.5 + Goles Cordoba CF Menos 3.5 | 59 % | 65 % | 55 % | 1.69 | 1.74 | 0.99 | 8 % | Empate | 54 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.