# FC Botosani - FC Voluntari
Rumanía Liga1 · 2026-11-20 10:30

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** FC Botosani · primer gol: local 63 %, visitante 32 %, nadie 5 % · gol del favorito antes del 35′: 42 %

**Base de la liga:** Rumanía Liga I · 2.50 goles/partido, Más 2.5 46 %, ambos marcan 52 % (697 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más).

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Resultado / hándicap | ➖ neutro | FC Botosani favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 33 % |
| Sorpresa: gana el no favorito | 16 % |
| Empate | 14 % |
| Favorito golpea temprano y gana | 14 % |
| Favorito gana en partido trabado | 12 % |
| Expulsión antes del 70′ | 11 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.91 | 16.1 | 5.1 | 4.7 | 11.8 | 2.1 |
| visitante | 1.07 | 11.7 | 3.6 | 4.7 | 11.8 | 2.9 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.0) · 1–5 | 1.9 (1.9) · 0–4 | 1.1 (1.1) · 0–2 | 1.3 (1.3) · 0–3 | 1.6 (1.7) · 0–3 |
| Córners | 9.4 (9.3) · 5–14 | 4.7 · 2–8 | 4.7 · 2–8 | 4.2 (4.6) · 2–7 | 5.1 (4.9) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.0 (5.0) · 2–8 | 2.1 (2.1) · 0–4 | 2.9 (2.9) · 1–5 | 1.7 (1.8) · 0–4 | 3.3 · 1–6 |
| Remates | 27.8 (27.6) · 20–35 | 16.1 (16.1) · 10–23 | 11.7 (11.7) · 7–17 | 12.5 · 8–18 | 15.2 · 10–21 |
| Tiros al arco | 8.7 (8.8) · 5–13 | 5.1 (5.1) · 2–8 | 3.6 (3.6) · 1–6 | 3.9 · 1–7 | 4.8 · 2–8 |
| Faltas | 23.7 · 18–30 | 11.9 · 8–16 | 11.8 · 8–16 | 10.6 · 7–15 | 13.1 · 9–18 |
| Fueras de lugar | 2.8 (2.8) · 1–5 | 1.5 (1.5) · 0–3 | 1.3 (1.4) · 0–3 | 1.2 · 0–3 | 1.6 · 0–3 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.1 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 40.1 · 29–52 | 20.0 · 13–28 | 20.0 · 12–28 | 17.9 · 12–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 2.5 · 1–5 | 3.2 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Menos 2.5 | 1.29 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (57 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.65 | 58 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa |
| Resultado y hándicap | No hay empate | 1.25 | 76 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.37 | 80 % | 70 % | Empate (74 %) | Partido abierto (ambos marcan y 3+ goles) (70 %) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas | Tarjetas Más 3.5 | 1.37 | 71 % | 60 % | Expulsión antes del 70′ (95 %) | Favorito golpea temprano y gana (60 %) | Alta probabilidad |
| Remates | Remates Más 23.5 | 1.25 | 77 % | 66 % | Partido abierto (ambos marcan y 3+ goles) (86 %) | Empate (66 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco FC Botosani Menos 6.5 | 1.30 | 74 % | 61 % | Empate (91 %) | Partido abierto (ambos marcan y 3+ goles) (61 %) | Alta probabilidad |
| Fueras de lugar | Fueras de lugar Más 1.5 | 1.27 | 75 % | 75 % | Favorito golpea temprano y gana (76 %) | Favorito gana en partido trabado (74 %) | Alta probabilidad |
| Jugadores | Lucas de Vega anota o asiste | 2.60 | 36 % | 17 % | Partido abierto (ambos marcan y 3+ goles) (51 %) | Sorpresa: gana el no favorito (17 %) | Cara |
| Quién saca más | Más corners: FC Voluntari | 3.65 | 33 % | 26 % | Favorito golpea temprano y gana (38 %) | Sorpresa: gana el no favorito (26 %) | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Menos 12.0 | 1.25 | 81 % | 80 % | 81 % | +0 pts | +1 % | 73 % | +0.8 | 1.27 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners 1.er tiempo Menos 6.0 | 1.37 | 80 % | 77 % | 80 % | +0 pts | +9 % | 70 % | +0.8 | 1.29 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Más 7.0 | 1.34 | 78 % | 77 % | 78 % | +0 pts | +4 % | 68 % | +0.7 | 1.33 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Remates Más 23.5 | 1.25 | 77 % | 78 % | 77 % | +0 pts | -4 % | 66 % | +0.7 | 1.34 | Empate | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -1 % | 76 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 11.5 | 1.25 | 76 % | 78 % | 76 % | +0 pts | -4 % | 74 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Más 6.5 | 1.26 | 76 % | 77 % | 76 % | +0 pts | -4 % | 57 % | +0.7 | 1.35 | Empate | Alta probabilidad |
| No hay empate | 1.25 | 76 % | 76 % | 76 % | +0 pts | -5 % | 76 % | — | 1.35 | Empate | Alta probabilidad |
| Fueras de lugar FC Botosani Más 0.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -4 % | 74 % | +0.7 | 1.37 | Favorito golpea temprano y gana | Alta probabilidad |
| Fueras de lugar Más 1.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -4 % | 75 % | +0.7 | 1.37 | Favorito gana en partido trabado | Alta probabilidad |
| Córners FC Voluntari Más 2.5 | 1.35 | 75 % | 69 % | 75 % | +0 pts | +1 % | 71 % | +0.8 | 1.38 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.44 | 74 % | 75 % | 74 % | +0 pts | +7 % | 60 % | +0.6 | 1.39 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Tiros al arco FC Botosani Menos 6.5 | 1.30 | 74 % | 74 % | 74 % | +0 pts | -4 % | 61 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco FC Botosani Más 3.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -5 % | 53 % | +0.7 | 1.39 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco Menos 10.5 | 1.31 | 73 % | 74 % | 73 % | +0 pts | -4 % | 56 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates FC Botosani Menos 18.5 | 1.28 | 73 % | 76 % | 73 % | +0 pts | -6 % | 67 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 2.º tiempo Más 3.5 | 1.34 | 73 % | 72 % | 73 % | +0 pts | -2 % | 71 % | +0.7 | 1.41 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.36 | 72 % | 71 % | 72 % | +0 pts | -2 % | 72 % | +0.7 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners Menos 11.0 | 1.42 | 72 % | 72 % | 72 % | +0 pts | +3 % | 63 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Fueras de lugar FC Voluntari Más 0.5 | 1.31 | 72 % | 74 % | 72 % | +0 pts | -5 % | 72 % | +0.7 | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Menos 5.5 | 1.37 | 72 % | 70 % | 72 % | +0 pts | -1 % | 70 % | +0.6 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Menos 3.75 | 1.38 | 71 % | 71 % | 71 % | +0 pts | -2 % | 71 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Goles FC Voluntari Menos 1.5 | 1.36 | 71 % | 71 % | 71 % | +0 pts | -3 % | 71 % | +0.5 | 1.45 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Más 7.5 | 1.34 | 71 % | 72 % | 71 % | +0 pts | -5 % | 69 % | +0.6 | 1.45 | Expulsión antes del 70′ | Alta probabilidad |
| Tarjetas Más 3.5 | 1.37 | 71 % | 70 % | 71 % | +0 pts | -3 % | 60 % | +0.6 | 1.46 | Favorito golpea temprano y gana | Alta probabilidad |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners FC Voluntari Más 6.5 | 7.30 | 17 % | 13 % | 17 % | +0 pts | +26 % | 14 % | -0.7 | 6.57 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners FC Voluntari Más 5.5 | 4.60 | 27 % | 20 % | 27 % | +0 pts | +23 % | 21 % | -0.3 | 4.06 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: FC Voluntari | 3.65 | 33 % | 22 % | 33 % | +0 pts | +20 % | 26 % | — | 3.23 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Menos 4.0 | 2.67 | 44 % | 41 % | 44 % | +0 pts | +17 % | 35 % | -0.1 | 2.39 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 20 % |
| David Kiki anota o asiste | 7.40 | 16 % | 12 % | 16 % | +0 pts | +15 % | 0 % | — | 7.39 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 5.0 | 1.78 | 64 % | 61 % | 64 % | +0 pts | +15 % | 55 % | +0.3 | 1.60 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners FC Voluntari Más 4.5 | 2.80 | 41 % | 33 % | 41 % | +0 pts | +14 % | 35 % | +0.1 | 2.59 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 3.0 | 4.60 | 24 % | 23 % | 24 % | +0 pts | +11 % | 19 % | -0.6 | 4.50 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 6.0 | 1.37 | 80 % | 77 % | 80 % | +0 pts | +9 % | 70 % | +0.8 | 1.29 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 3.0 | 1.44 | 74 % | 75 % | 74 % | +0 pts | +7 % | 60 % | +0.6 | 1.39 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners Menos 10.0 | 1.75 | 61 % | 60 % | 61 % | +0 pts | +6 % | 51 % | +0.2 | 1.70 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners FC Voluntari Más 3.5 | 1.85 | 57 % | 51 % | 57 % | +0 pts | +6 % | 52 % | +0.5 | 1.81 | Expulsión antes del 70′ | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Más 8.0 | 1.62 | 65 % | 65 % | 65 % | +0 pts | +6 % | 55 % | +0.4 | 1.58 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Menos 9.0 | 2.22 | 48 % | 47 % | 48 % | +0 pts | +6 % | 40 % | -0.1 | 2.19 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 4.0 | 1.95 | 54 % | 57 % | 54 % | +0 pts | +5 % | 42 % | +0.1 | 1.93 | Favorito gana en partido trabado | Valor · asiática: devuelve 20 % |
| Córners Más 9.0 | 2.02 | 52 % | 52 % | 52 % | +0 pts | +5 % | 44 % | +0.1 | 2.01 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 7.0 | 1.34 | 78 % | 77 % | 78 % | +0 pts | +4 % | 68 % | +0.7 | 1.33 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 2.0 | 1.17 | 89 % | 88 % | 89 % | +0 pts | +4 % | 76 % | +1.1 | 1.16 | Empate | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners 1.er tiempo Menos 7.0 | 1.17 | 89 % | 86 % | 89 % | +0 pts | +4 % | 81 % | +1.3 | 1.16 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 7 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners FC Voluntari Más 6.5 1.0 % de la banca; Córners FC Voluntari Más 5.5 1.6 % de la banca; Más corners: FC Voluntari 1.9 % de la banca; Córners 1.er tiempo Menos 4.0 2.6 % de la banca; David Kiki anota o asiste 0.6 % de la banca; Córners 1.er tiempo Menos 5.0 4.7 % de la banca; Córners FC Voluntari Más 4.5 1.9 % de la banca; Córners 1.er tiempo Menos 3.0 0.8 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Tiros al arco FC Botosani Menos 8.5 + Tarjetas Más 3.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.14 | 8 % | Expulsión antes del 70′ | 52 % |
| Ambos 1+ tarjetas: Sí + Tiros al arco FC Voluntari Menos 6.5 + Tarjetas Más 3.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.13 | 8 % | Expulsión antes del 70′ | 56 % |
| Hándicap FC Botosani +2 + Goles 2.º tiempo Menos 2.5 + FC Botosani o empate | 62 % | 64 % | 58 % | 1.62 | 1.67 | 1.06 | 7 % | Empate | 0 % |
| Goles 2.º tiempo Menos 2.5 + Tiros al arco FC Botosani Menos 8.5 + Fueras de lugar FC Voluntari Menos 2.5 | 61 % | 61 % | 57 % | 1.64 | 1.69 | 1.04 | 7 % | Empate | 42 % |
| Córners 1.er tiempo Menos 5.5 + Fueras de lugar Más 0.5 + Tiros al arco FC Voluntari Menos 6.5 | 62 % | 63 % | 58 % | 1.61 | 1.65 | 1.0 | 7 % | Favorito gana en partido trabado | 57 % |
| Hándicap FC Botosani +2 + Córners 1.er tiempo Menos 5.5 + FC Botosani o empate | 58 % | 61 % | 54 % | 1.72 | 1.77 | 1.06 | 8 % | Empate | 0 % |
| Córners FC Voluntari Más 3.5 + Goles FC Botosani Menos 4.5 | 55 % | 62 % | 50 % | 1.81 | 1.87 | 1.0 | 8 % | Favorito golpea temprano y gana | 52 % |
| ↳ Línea contra el guion (Más de un equipo que perdió: 2/11) |  |  |  |  |  |  |  |  |  |
| Córners FC Voluntari Más 3.5 + Goles 1.er tiempo Menos 3.5 | 55 % | 61 % | 50 % | 1.82 | 1.88 | 1.0 | 8 % | Favorito golpea temprano y gana | 50 % |
| ↳ Línea contra el guion (Más de un equipo que perdió: 2/11) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.