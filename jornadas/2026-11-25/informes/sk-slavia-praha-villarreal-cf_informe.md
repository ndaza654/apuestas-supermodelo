# SK Slavia Praha - Villarreal CF
Champions League Champions League · 2026-11-25 12:45

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** Villarreal CF · primer gol: local 42 %, visitante 54 %, nadie 4 % · gol del favorito antes del 35′: 37 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Resultado / hándicap | ➖ neutro | Villarreal CF favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 34 % |
| Sorpresa: gana el no favorito | 26 % |
| Empate | 13 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 9 % |
| Favorito gana en partido trabado | 8 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.48 | 14.3 | 4.6 | 5.0 | 13.3 | 2.3 |
| visitante | 1.80 | 15.3 | 5.1 | 5.0 | 11.7 | 2.1 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.2 (3.3) · 1–6 | 1.4 (1.5) · 0–3 | 1.8 (1.8) · 0–3 | 1.4 (1.4) · 0–3 | 1.8 (1.8) · 0–4 |
| Córners | 10.1 (10.0) · 6–15 | 5.0 (5.0) · 2–8 | 5.0 (5.0) · 2–9 | 4.5 (4.8) · 2–7 | 5.6 (5.3) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 4.5 (4.4) · 2–8 | 2.3 (2.3) · 1–4 | 2.1 (2.1) · 0–4 | 1.5 (1.5) · 0–3 | 3.0 · 1–6 |
| Remates | 29.7 (29.6) · 22–38 | 14.3 (14.3) · 9–20 | 15.4 (15.3) · 9–22 | 13.3 · 9–18 | 16.4 · 11–22 |
| Tiros al arco | 9.7 (9.8) · 6–14 | 4.5 (4.6) · 2–8 | 5.2 (5.1) · 2–9 | 4.4 (4.5) · 2–7 | 5.3 · 2–8 |
| Faltas | 25.0 (25.0) · 19–32 | 13.4 (13.3) · 9–18 | 11.7 (11.7) · 7–16 | 11.2 · 7–16 | 13.8 · 9–19 |
| Fueras de lugar | 3.4 (3.5) · 1–6 | 2.2 (2.2) · 0–4 | 1.2 (1.2) · 0–3 | 1.5 (1.8) · 0–3 | 1.9 · 0–4 |
| Saques de meta | 16.5 (16.6) · 10–23 | 8.5 (8.6) · 4–14 | 8.0 (8.1) · 4–13 | 7.3 (7.7) · 4–11 | 9.2 · 5–14 |
| Saques de banda | 32.2 (32.2) · 23–42 | 15.7 (15.6) · 9–23 | 16.6 (16.6) · 10–24 | 14.4 (17.0) · 9–20 | 17.8 · 11–25 |
| Atajadas del portero | — | 3.4 · 1–6 | 3.1 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.28 | 77 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (62 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.45 | 66 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · ★ enfoque a favor |
| Resultado y hándicap | Hándicap SK Slavia Praha +2 | 1.28 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (25 %) | Alta probabilidad |
| Córners | Córners 2.º tiempo Más 3.5 | 1.26 | 78 % | 78 % | Partido abierto (ambos marcan y 3+ goles) (79 %) | Expulsión antes del 70′ (73 %) | Alta probabilidad |
| Tarjetas | Tarjetas Más 2.5 | 1.25 | 78 % | 76 % | Expulsión antes del 70′ (98 %) | Favorito golpea temprano y gana (70 %) | Alta probabilidad |
| Faltas | Faltas Más 24.5 | 1.80 | 52 % | 51 % | Expulsión antes del 70′ (56 %) | Favorito golpea temprano y gana (49 %) | Cara |
| Remates | Remates Menos 33.5 | 1.25 | 76 % | 66 % | Empate (87 %) | Partido abierto (ambos marcan y 3+ goles) (66 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco Villarreal CF Menos 6.5 | 1.30 | 74 % | 59 % | Empate (88 %) | Partido abierto (ambos marcan y 3+ goles) (59 %) | Alta probabilidad |
| Fueras de lugar | Fueras de lugar Menos 4.5 | 1.30 | 74 % | 74 % | Empate (76 %) | Favorito golpea temprano y gana (72 %) | Alta probabilidad |
| Saques de meta | Saques de meta Menos 19.5 | 1.25 | 76 % | 76 % | Favorito golpea temprano y gana (77 %) | Expulsión antes del 70′ (70 %) | Alta probabilidad · cuota por debajo de la justa |
| Saques de banda | Saques de banda 1.er tiempo Menos 16.5 | 1.93 | 59 % | 58 % | Favorito golpea temprano y gana (61 %) | Partido abierto (ambos marcan y 3+ goles) (58 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jugadores | Jakub Markovic atajadas 5+ | 4.20 | 23 % | 22 % | Favorito gana en partido trabado (25 %) | Favorito golpea temprano y gana (21 %) | Justa |
| Parejas de jugadores | Michal Sadilek o Tajon Buchanan (da una asistencia) | 3.30 | 29 % | 15 % | Partido abierto (ambos marcan y 3+ goles) (37 %) | Favorito gana en partido trabado (15 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 2.5 | 1.25 | 78 % | 78 % | 78 % | +0 pts | -2 % | 76 % | +0.8 | 1.32 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 2.º tiempo Más 3.5 | 1.26 | 78 % | 77 % | 78 % | +0 pts | -2 % | 78 % | +0.8 | 1.32 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.37 | 78 % | 78 % | 78 % | +0 pts | +6 % | 64 % | +0.7 | 1.33 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Goles Menos 4.5 | 1.28 | 77 % | 76 % | 77 % | +0 pts | -1 % | 77 % | +0.7 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Hándicap SK Slavia Praha +2 | 1.28 | 77 % | 76 % | 77 % | +0 pts | -2 % | 77 % | — | 1.34 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.27 | 76 % | 77 % | 76 % | +0 pts | -3 % | 76 % | +0.8 | 1.35 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Menos 6.0 | 1.44 | 76 % | 74 % | 76 % | +0 pts | +10 % | 66 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Remates Menos 33.5 | 1.25 | 76 % | 78 % | 76 % | +0 pts | -5 % | 66 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Saques de meta Menos 19.5 | 1.25 | 76 % | 78 % | 76 % | +0 pts | -6 % | 76 % | +0.6 | 1.36 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates Más 25.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -4 % | 63 % | +0.7 | 1.36 | Empate | Alta probabilidad |
| Córners SK Slavia Praha Menos 6.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -4 % | 72 % | +0.6 | 1.37 | Favorito golpea temprano y gana | Alta probabilidad |
| No hay empate | 1.25 | 75 % | 76 % | 75 % | +0 pts | -6 % | 75 % | — | 1.37 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Córners Menos 12.0 | 1.36 | 75 % | 75 % | 75 % | +0 pts | +2 % | 66 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Tarjetas 1.er tiempo Más 0.5 | 1.30 | 75 % | 74 % | 75 % | +0 pts | -3 % | 73 % | +0.8 | 1.38 | Favorito gana en partido trabado | Alta probabilidad |
| Tiros al arco Más 7.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -4 % | 53 % | +0.7 | 1.38 | Empate | Alta probabilidad |
| Córners Villarreal CF Menos 6.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -5 % | 70 % | +0.6 | 1.38 | Sorpresa: gana el no favorito | Alta probabilidad |
| Saques de meta SK Slavia Praha Menos 10.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 69 % | +0.5 | 1.38 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Villarreal CF Más 3.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -4 % | 58 % | +0.7 | 1.39 | Empate | Alta probabilidad |
| Fueras de lugar Menos 4.5 | 1.30 | 74 % | 74 % | 74 % | +0 pts | -4 % | 74 % | +0.5 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad |
| Remates SK Slavia Praha Más 11.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 67 % | +0.6 | 1.39 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Villarreal CF Menos 6.5 | 1.30 | 74 % | 74 % | 74 % | +0 pts | -4 % | 59 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Villarreal CF Menos 2.5 | 1.32 | 73 % | 73 % | 73 % | +0 pts | -3 % | 74 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates Villarreal CF Más 12.5 | 1.28 | 73 % | 76 % | 73 % | +0 pts | -6 % | 65 % | +0.6 | 1.41 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Saques de meta Más 13.5 | 1.27 | 73 % | 76 % | 73 % | +0 pts | -7 % | 71 % | +0.6 | 1.41 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 8.0 | 1.44 | 73 % | 72 % | 73 % | +0 pts | +5 % | 63 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.92 | 39 % | 38 % | 39 % | +0 pts | +15 % | 32 % | -0.2 | 2.67 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Saques de banda 1.er tiempo Menos 16.5 | 1.93 | 59 % | 48 % | 59 % | +0 pts | +14 % | 58 % | +0.5 | 1.75 | Partido abierto (ambos marcan y 3+ goles) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Menos 5.0 | 1.91 | 60 % | 57 % | 60 % | +0 pts | +14 % | 50 % | +0.2 | 1.73 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.44 | 76 % | 74 % | 76 % | +0 pts | +10 % | 66 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 4.0 | 1.83 | 59 % | 60 % | 59 % | +0 pts | +7 % | 45 % | +0.2 | 1.77 | Empate | Valor · asiática: devuelve 19 % |
| Córners Más 10.0 | 2.25 | 47 % | 47 % | 47 % | +0 pts | +7 % | 40 % | +0.0 | 2.21 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 3.0 | 1.37 | 78 % | 78 % | 78 % | +0 pts | +6 % | 64 % | +0.7 | 1.33 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners Más 9.0 | 1.75 | 60 % | 60 % | 60 % | +0 pts | +6 % | 52 % | +0.3 | 1.71 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.44 | 73 % | 72 % | 73 % | +0 pts | +5 % | 63 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 10.0 | 2.02 | 52 % | 52 % | 52 % | +0 pts | +5 % | 44 % | -0.0 | 2.00 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Menos 7.0 | 1.20 | 87 % | 84 % | 87 % | +0 pts | +4 % | 78 % | +1.1 | 1.19 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 8 % |
| Córners 1.er tiempo Más 2.0 | 1.14 | 91 % | 89 % | 91 % | +0 pts | +3 % | 80 % | +1.1 | 1.14 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Más 7.0 | 1.24 | 83 % | 82 % | 83 % | +0 pts | +3 % | 75 % | +0.9 | 1.24 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 9 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.0 % de la banca; Saques de banda 1.er tiempo Menos 16.5 3.9 % de la banca; Córners 1.er tiempo Menos 5.0 3.9 % de la banca; Córners 1.er tiempo Menos 6.0 5.4 % de la banca; Córners 1.er tiempo Más 4.0 2.1 % de la banca; Córners Más 10.0 1.3 % de la banca; Córners 1.er tiempo Más 3.0 4.3 % de la banca; Córners Más 9.0 1.9 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Hándicap Villarreal CF +0.5 + Córners 2.º tiempo Más 2.5 + Villarreal CF o empate | 62 % | 64 % | 57 % | 1.62 | 1.66 | 1.4 | 8 % | Favorito gana en partido trabado | 0 % |
| Hándicap Villarreal CF +0.5 + Goles Villarreal CF Menos 3.5 + Villarreal CF o empate | 59 % | 62 % | 55 % | 1.69 | 1.74 | 1.35 | 8 % | Empate | 0 % |
| Ambos 1+ tarjetas: Sí + Tarjetas Más 1.5 + Goles 2.º tiempo Menos 2.5 | 59 % | 61 % | 55 % | 1.69 | 1.74 | 1.1 | 8 % | Empate | 44 % |
| Tarjetas Más 1.5 + Tiros al arco SK Slavia Praha Menos 7.5 + Goles 2.º tiempo Menos 2.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.03 | 7 % | Empate | 45 % |
| Ambos 1+ tarjetas: Sí + Córners Más 5.5 + Tarjetas Villarreal CF Menos 3.5 | 62 % | 63 % | 58 % | 1.62 | 1.67 | 0.97 | 7 % | Favorito gana en partido trabado | 63 % |
| Saques de banda 1.er tiempo Menos 16.5 + Goles Menos 6.5 | 57 % | 67 % | 52 % | 1.77 | 1.82 | 1.0 | 8 % | Favorito golpea temprano y gana | 54 % |
| ↳ Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |  |  |  |  |  |  |  |  |  |
| Saques de banda 1.er tiempo Menos 16.5 + Córners 1.er tiempo Menos 8.5 | 57 % | 67 % | 52 % | 1.77 | 1.82 | 1.0 | 8 % | Empate | 55 % |
| ↳ Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.