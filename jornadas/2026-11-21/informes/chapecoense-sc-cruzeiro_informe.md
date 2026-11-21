# Chapecoense SC - Cruzeiro
Brasil Brasileirao - Serie A · 2026-11-21 19:00

**Tipo de partido:** Favorito claro · abierto · normal · **Favorito:** Cruzeiro · primer gol: local 26 %, visitante 70 %, nadie 4 % · gol del favorito antes del 35′: 49 %

**Base de la liga:** Brasil Serie A · 2.43 goles/partido, Más 2.5 45 %, ambos marcan 50 % (841 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Hándicap y victoria de Cruzeiro, Goles de Cruzeiro (Más), Remates / tiros al arco de Cruzeiro, Tarjetas (Menos), Faltas (Menos).

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Hándicap y victoria de Cruzeiro | ✅ favorece | favorito claro: manda en el marcador y en el territorio |
| Goles de Cruzeiro (Más) | ✅ favorece | favorito claro contra rival que sufre |
| Remates / tiros al arco de Cruzeiro | ✅ favorece | el que domina remata más |
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
| Favorito golpea temprano y gana | 18 % |
| Favorito gana en partido trabado | 12 % |
| Empate | 11 % |
| Sorpresa: gana el no favorito | 11 % |
| Expulsión antes del 70′ | 10 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 0.97 | 12.1 | 3.7 | 5.4 | 11.8 | 2.5 |
| visitante | 2.27 | 17.7 | 6.7 | 5.4 | 11.8 | 2.0 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.2 (3.2) · 1–6 | 1.0 (1.0) · 0–2 | 2.3 (2.3) · 1–4 | 1.5 (1.4) · 0–3 | 1.8 (1.9) · 0–3 |
| Córners | 10.9 (10.8) · 7–15 | 5.5 · 2–9 | 5.4 · 2–9 | 4.9 (5.2) · 2–8 | 6.0 (5.7) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 4.5 (4.5) · 2–8 | 2.5 (2.5) · 1–5 | 2.0 (2.0) · 0–4 | 1.6 (1.6) · 0–3 | 2.9 · 1–6 |
| Remates | 29.9 (29.8) · 22–38 | 12.2 (12.1) · 7–18 | 17.7 (17.7) · 11–25 | 13.5 · 9–19 | 16.4 · 11–22 |
| Tiros al arco | 10.4 (10.4) · 6–15 | 3.7 (3.7) · 1–6 | 6.7 (6.7) · 3–11 | 4.7 · 2–8 | 5.7 · 3–9 |
| Faltas | 23.7 · 17–30 | 11.9 · 8–17 | 11.8 · 7–16 | 10.6 · 7–15 | 13.1 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 15.9 · 10–23 | 7.9 · 4–13 | 8.0 · 4–13 | 7.0 · 3–11 | 8.9 · 5–13 |
| Saques de banda | 40.1 · 29–52 | 19.9 · 12–28 | 20.2 · 13–28 | 17.9 · 12–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 4.5 · 2–8 | 2.7 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.26 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (59 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.67 | 57 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa |
| Resultado y hándicap | Hándicap Chapecoense SC +3 | 1.27 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (45 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 7.0 | 1.30 | 82 % | 74 % | Sorpresa: gana el no favorito (76 %) | Partido abierto (ambos marcan y 3+ goles) (74 %) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Tarjetas | Tarjetas Menos 5.5 | 1.39 | 70 % | 74 % | Favorito golpea temprano y gana (79 %) | Expulsión antes del 70′ (32 %) | Alta probabilidad · ★ enfoque a favor |
| Remates | Remates Más 25.5 | 1.25 | 76 % | 72 % | Partido abierto (ambos marcan y 3+ goles) (85 %) | Empate (68 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco Cruzeiro Menos 8.5 | 1.26 | 76 % | 68 % | Empate (91 %) | Partido abierto (ambos marcan y 3+ goles) (68 %) | Alta probabilidad |
| Quién saca más | Más corners: Chapecoense SC | 3.25 | 36 % | 37 % | Favorito golpea temprano y gana (42 %) | Sorpresa: gana el no favorito (28 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Más 3.0 | 1.27 | 83 % | 82 % | 83 % | +0 pts | +5 % | 71 % | +0.8 | 1.25 | Empate | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners 1.er tiempo Menos 7.0 | 1.30 | 82 % | 80 % | 82 % | +0 pts | +7 % | 74 % | +0.9 | 1.25 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Más 8.0 | 1.28 | 80 % | 79 % | 80 % | +0 pts | +3 % | 71 % | +0.8 | 1.29 | Expulsión antes del 70′ | Alta probabilidad · asiática: devuelve 9 % |
| Goles Menos 4.5 | 1.26 | 78 % | 77 % | 78 % | +0 pts | -2 % | 78 % | +0.7 | 1.33 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Hándicap Chapecoense SC +3 | 1.27 | 77 % | 77 % | 77 % | +0 pts | -2 % | 77 % | — | 1.34 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Goles 1.er tiempo Más 0.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -1 % | 76 % | +0.8 | 1.35 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Remates Más 25.5 | 1.25 | 76 % | 78 % | 76 % | +0 pts | -4 % | 72 % | +0.7 | 1.35 | Empate | Alta probabilidad |
| Tiros al arco Cruzeiro Menos 8.5 | 1.26 | 76 % | 77 % | 76 % | +0 pts | -4 % | 68 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 13.0 | 1.34 | 76 % | 76 % | 76 % | +0 pts | +2 % | 67 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Córners 1.er tiempo Menos 6.5 | 1.30 | 76 % | 74 % | 76 % | +0 pts | -2 % | 75 % | +0.7 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 8.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -4 % | 73 % | +0.7 | 1.38 | Expulsión antes del 70′ | Alta probabilidad |
| Tiros al arco Menos 12.5 | 1.29 | 75 % | 75 % | 75 % | +0 pts | -4 % | 61 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Chapecoense SC Menos 1.5 | 1.30 | 75 % | 74 % | 75 % | +0 pts | -3 % | 75 % | +0.6 | 1.38 | Sorpresa: gana el no favorito | Alta probabilidad |
| Remates Menos 33.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -5 % | 65 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Chapecoense SC Menos 14.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -5 % | 68 % | +0.5 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Cruzeiro Menos 20.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -5 % | 69 % | +0.5 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Chapecoense SC Más 9.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 72 % | +0.6 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates Cruzeiro Más 14.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 71 % | +0.6 | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners 1.er tiempo Más 3.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 74 % | +0.6 | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Goles 2.º tiempo Menos 2.5 | 1.36 | 73 % | 71 % | 73 % | +0 pts | -1 % | 73 % | +0.6 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Descanso o final: Cruzeiro | 1.33 | 72 % | 70 % | 72 % | +0 pts | -4 % | 72 % | — | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Goles 1.er tiempo Más 0.75 | 1.39 | 72 % | 70 % | 72 % | +0 pts | -1 % | 72 % | +0.6 | 1.44 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| Córners Menos 12.5 | 1.34 | 71 % | 72 % | 71 % | +0 pts | -5 % | 68 % | +0.5 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles Más 2.25 | 1.39 | 71 % | 70 % | 71 % | +0 pts | -2 % | 71 % | +0.6 | 1.46 | Empate | Alta probabilidad · asiática: devuelve 10 % · ★ enfoque a favor |
| Remates Más 26.5 | 1.35 | 70 % | 71 % | 70 % | +0 pts | -5 % | 66 % | +0.6 | 1.46 | Empate | Alta probabilidad |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Chapecoense SC Más 7.5 | 6.90 | 18 % | 14 % | 18 % | +0 pts | +21 % | 20 % | -0.7 | 6.44 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Chapecoense SC Más 6.5 | 4.50 | 26 % | 21 % | 26 % | +0 pts | +18 % | 29 % | -0.4 | 4.14 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: Chapecoense SC | 3.25 | 36 % | 26 % | 36 % | +0 pts | +16 % | 37 % | — | 2.98 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Menos 4.0 | 3.55 | 32 % | 31 % | 32 % | +0 pts | +15 % | 27 % | -0.4 | 3.30 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 5.0 | 2.22 | 52 % | 49 % | 52 % | +0 pts | +14 % | 43 % | +0.0 | 2.02 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % |
| Córners Chapecoense SC Más 5.5 | 2.92 | 38 % | 32 % | 38 % | +0 pts | +12 % | 41 % | -0.0 | 2.76 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 6.0 | 1.62 | 69 % | 66 % | 69 % | +0 pts | +12 % | 59 % | +0.5 | 1.49 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 14 % |
| Córners 1.er tiempo Más 4.0 | 1.62 | 66 % | 67 % | 66 % | +0 pts | +7 % | 55 % | +0.4 | 1.56 | Empate | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 7.0 | 1.30 | 82 % | 80 % | 82 % | +0 pts | +7 % | 74 % | +0.9 | 1.25 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Chapecoense SC Más 4.5 | 1.98 | 53 % | 47 % | 53 % | +0 pts | +6 % | 56 % | +0.3 | 1.95 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Más 10.0 | 1.82 | 58 % | 58 % | 58 % | +0 pts | +5 % | 49 % | +0.2 | 1.80 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 3.0 | 1.27 | 83 % | 82 % | 83 % | +0 pts | +5 % | 71 % | +0.8 | 1.25 | Empate | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners Más 9.0 | 1.50 | 70 % | 69 % | 70 % | +0 pts | +5 % | 60 % | +0.5 | 1.47 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 11.0 | 1.93 | 54 % | 54 % | 54 % | +0 pts | +5 % | 46 % | +0.0 | 1.91 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners Más 11.0 | 2.32 | 45 % | 45 % | 45 % | +0 pts | +5 % | 38 % | -0.0 | 2.32 | Expulsión antes del 70′ | Valor · asiática: devuelve 11 % |
| Córners Menos 12.0 | 1.57 | 66 % | 66 % | 66 % | +0 pts | +4 % | 57 % | +0.3 | 1.56 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners Chapecoense SC Más 7.5 0.9 % de la banca; Córners Chapecoense SC Más 6.5 1.3 % de la banca; Más corners: Chapecoense SC 1.8 % de la banca; Córners 1.er tiempo Menos 4.0 1.4 % de la banca; Córners 1.er tiempo Menos 5.0 3.0 % de la banca; Córners Chapecoense SC Más 5.5 1.5 % de la banca; Córners 1.er tiempo Menos 6.0 4.8 % de la banca; Córners 1.er tiempo Más 4.0 2.8 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #429 (sin racha) | empate ≥3,90, visitante ≤2,00 | Ambos marcan: Sí | 4451 partidos: Ambos Sí 52.8 % contra 54.0 % que ya da el precio (-1.1 pts ± 1.5) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Cruzeiro o empate + Hándicap Cruzeiro +1 + Goles 2.º tiempo Menos 2.5 | 62 % | 65 % | 58 % | 1.62 | 1.67 | 1.14 | 7 % | Empate | 53 % |
| Cruzeiro o empate + Goles 1.er tiempo Más 0.5 + Descanso o final: Cruzeiro | 58 % | 61 % | 54 % | 1.73 | 1.79 | 1.2 | 11 % | Favorito golpea temprano y gana | 77 % |
| Hándicap Cruzeiro +1 + Goles 1.er tiempo Más 0.5 + Descanso o final: Cruzeiro | 58 % | 61 % | 54 % | 1.74 | 1.79 | 1.2 | 11 % | Favorito golpea temprano y gana | 77 % |
| Tarjetas Más 1.5 + Ambos 1+ tarjetas: Sí + Remates Más 25.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.08 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 54 % |
| Goles 2.º tiempo Menos 2.5 + Tarjetas Más 1.5 + Tiros al arco Menos 14.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.05 | 7 % | Empate | 44 % |
| Córners Chapecoense SC Más 3.5 + Tiros al arco Cruzeiro Más 3.5 | 61 % | 65 % | 57 % | 1.63 | 1.68 | 1.0 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 68 % |
| Córners Chapecoense SC Más 3.5 + Tiros al arco Chapecoense SC Menos 6.5 | 62 % | 66 % | 57 % | 1.62 | 1.66 | 0.99 | 8 % | Favorito golpea temprano y gana | 61 % |
| Ambos 1+ tarjetas: Sí + Remates Más 25.5 | 62 % | 62 % | 58 % | 1.62 | 1.67 | 0.99 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 54 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.