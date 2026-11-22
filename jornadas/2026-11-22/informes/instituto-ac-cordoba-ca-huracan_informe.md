# Instituto AC Cordoba - CA Huracan
Argentina Liga Profesional · 2026-11-22 20:00

**Tipo de partido:** Favorito leve · cerrado · caliente · **Favorito:** Instituto AC Cordoba · primer gol: local 53 %, visitante 34 %, nadie 14 % · gol del favorito antes del 35′: 30 %

**Base de la liga:** Argentina Liga Profesional · 2.11 goles/partido, Más 2.5 35 %, ambos marcan 43 % (1268 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Resultado / hándicap | ➖ neutro | Instituto AC Cordoba favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Empate | 24 % |
| Sorpresa: gana el no favorito | 20 % |
| Partido abierto (ambos marcan y 3+ goles) | 17 % |
| Favorito gana en partido trabado | 14 % |
| Expulsión antes del 70′ | 13 % |
| Favorito golpea temprano y gana | 12 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.23 | 15.2 | 4.9 | 4.5 | 11.8 | 2.8 |
| visitante | 0.80 | 11.0 | 3.8 | 4.5 | 11.8 | 3.4 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.0 (2.0) · 0–4 | 1.2 (1.2) · 0–3 | 0.8 (0.8) · 0–2 | 0.9 (0.9) · 0–2 | 1.1 (1.2) · 0–3 |
| Córners | 9.0 (9.0) · 5–13 | 4.5 · 2–8 | 4.5 · 2–8 | 4.0 (4.4) · 2–7 | 4.9 (4.7) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 6.1 (6.1) · 3–10 | 2.8 (2.8) · 1–5 | 3.3 (3.4) · 1–6 | 2.0 (2.1) · 0–4 | 4.1 · 1–7 |
| Remates | 26.2 (26.1) · 19–34 | 15.2 (15.2) · 9–22 | 11.0 (11.0) · 6–16 | 11.8 · 7–17 | 14.4 · 9–20 |
| Tiros al arco | 8.6 (8.7) · 5–13 | 4.8 (4.9) · 2–8 | 3.8 (3.8) · 1–7 | 3.9 · 1–6 | 4.7 · 2–8 |
| Faltas | 23.6 · 17–30 | 11.8 · 8–16 | 11.7 · 7–16 | 10.5 · 6–15 | 13.1 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 15.9 · 10–23 | 8.0 · 4–13 | 7.9 · 4–13 | 7.1 · 3–11 | 8.9 · 5–13.1 |
| Saques de banda | 40.2 · 29–52 | 20.1 · 13–28 | 20.1 · 12–28 | 17.9 · 12–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 3.0 · 1–6 | 3.6 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Menos 1.5 | 1.25 | 77 % | (lo define el marcador) | Favorito gana en partido trabado (98 %) | Partido abierto (ambos marcan y 3+ goles) (43 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: No | 1.62 | 59 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Justa |
| Resultado y hándicap | Instituto AC Cordoba o empate | 1.27 | 77 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.31 | 83 % | 72 % | Empate (76 %) | Partido abierto (ambos marcan y 3+ goles) (72 %) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas | Ambos 2+ tarjetas: Sí | 1.44 | 68 % | 62 % | Expulsión antes del 70′ (84 %) | Favorito golpea temprano y gana (62 %) | Alta probabilidad |
| Remates | Remates Más 22.5 | 1.29 | 74 % | 68 % | Partido abierto (ambos marcan y 3+ goles) (87 %) | Empate (68 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco Más 6.5 | 1.27 | 75 % | 63 % | Partido abierto (ambos marcan y 3+ goles) (95 %) | Empate (63 %) | Alta probabilidad |
| Quién saca más | Más corners: CA Huracan | 3.40 | 34 % | 29 % | Favorito golpea temprano y gana (41 %) | Sorpresa: gana el no favorito (29 %) | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 6.0 | 1.31 | 83 % | 80 % | 83 % | +0 pts | +8 % | 72 % | +1.0 | 1.24 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Goles 1.er tiempo Menos 1.5 | 1.25 | 77 % | 78 % | 77 % | +0 pts | -3 % | 77 % | +0.6 | 1.33 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Instituto AC Cordoba o empate | 1.27 | 77 % | 77 % | 77 % | +0 pts | -2 % | 77 % | — | 1.34 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Instituto AC Cordoba +1 | 1.27 | 77 % | 77 % | 77 % | +0 pts | -2 % | 77 % | — | 1.34 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Menos 11.0 | 1.35 | 76 % | 76 % | 76 % | +0 pts | +3 % | 66 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners 1.er tiempo Menos 5.5 | 1.31 | 76 % | 74 % | 76 % | +0 pts | -1 % | 73 % | +0.7 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Más 6.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -5 % | 63 % | +0.7 | 1.37 | Empate | Alta probabilidad |
| Tiros al arco Menos 10.5 | 1.29 | 75 % | 75 % | 75 % | +0 pts | -4 % | 53 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates CA Huracan Más 8.5 | 1.26 | 74 % | 77 % | 74 % | +0 pts | -6 % | 66 % | +0.6 | 1.38 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates Menos 29.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 60 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Más 22.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -4 % | 68 % | +0.6 | 1.39 | Empate | Alta probabilidad |
| Córners Más 7.0 | 1.42 | 74 % | 74 % | 74 % | +0 pts | +5 % | 62 % | +0.6 | 1.40 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Goles Menos 2.75 | 1.34 | 73 % | 73 % | 73 % | +0 pts | -2 % | 74 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % · ★ enfoque a favor |
| Córners CA Huracan Más 2.5 | 1.37 | 73 % | 68 % | 73 % | +0 pts | +0 % | 69 % | +0.8 | 1.41 | Expulsión antes del 70′ | Alta probabilidad |
| Remates Instituto AC Cordoba Menos 17.5 | 1.29 | 73 % | 75 % | 73 % | +0 pts | -6 % | 65 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Menos 1.25 | 1.33 | 73 % | 74 % | 73 % | +0 pts | -3 % | 73 % | +0.4 | 1.41 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 18 % · ★ enfoque a favor |
| Goles Instituto AC Cordoba Más 0.5 | 1.35 | 71 % | 71 % | 71 % | +0 pts | -4 % | 71 % | +0.7 | 1.44 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco CA Huracan Más 2.5 | 1.33 | 71 % | 73 % | 71 % | +0 pts | -5 % | 55 % | +0.6 | 1.44 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Remates Instituto AC Cordoba Más 12.5 | 1.32 | 71 % | 73 % | 71 % | +0 pts | -6 % | 66 % | +0.6 | 1.45 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Córners Menos 10.5 | 1.35 | 71 % | 71 % | 71 % | +0 pts | -5 % | 68 % | +0.5 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 2.º tiempo Más 3.5 | 1.39 | 71 % | 69 % | 71 % | +0 pts | -2 % | 66 % | +0.6 | 1.46 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.52 | 71 % | 72 % | 71 % | +0 pts | +7 % | 56 % | +0.5 | 1.46 | Empate | Alta probabilidad · Valor · asiática: devuelve 19 % |
| Goles Más 1.25 | 1.40 | 70 % | 70 % | 70 % | +0 pts | -2 % | 70 % | +0.5 | 1.48 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 13 % |
| Tarjetas Más 4.5 | 1.38 | 70 % | 70 % | 70 % | +0 pts | -4 % | 60 % | +0.6 | 1.48 | Favorito golpea temprano y gana | Alta probabilidad |
| Tiros al arco Instituto AC Cordoba Más 3.5 | 1.34 | 70 % | 72 % | 70 % | +0 pts | -7 % | 55 % | +0.5 | 1.48 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.45 | 48 % | 45 % | 48 % | +0 pts | +18 % | 39 % | -0.0 | 2.17 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 3.0 | 4.25 | 27 % | 26 % | 27 % | +0 pts | +16 % | 22 % | -0.5 | 3.94 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 19 % |
| Más corners: CA Huracan | 3.40 | 34 % | 24 % | 34 % | +0 pts | +16 % | 29 % | — | 3.13 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners CA Huracan Más 5.5 | 4.60 | 25 % | 20 % | 25 % | +0 pts | +15 % | 22 % | -0.4 | 4.36 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 5.0 | 1.67 | 68 % | 65 % | 68 % | +0 pts | +14 % | 57 % | +0.5 | 1.51 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners CA Huracan Más 4.5 | 2.87 | 38 % | 33 % | 38 % | +0 pts | +10 % | 34 % | -0.0 | 2.75 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 6.0 | 1.31 | 83 % | 80 % | 83 % | +0 pts | +8 % | 72 % | +1.0 | 1.24 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 3.0 | 1.52 | 71 % | 72 % | 71 % | +0 pts | +7 % | 56 % | +0.5 | 1.46 | Empate | Alta probabilidad · Valor · asiática: devuelve 19 % |
| Córners Menos 8.0 | 2.75 | 39 % | 39 % | 39 % | +0 pts | +7 % | 31 % | -0.3 | 2.72 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Menos 9.0 | 2.02 | 53 % | 52 % | 53 % | +0 pts | +6 % | 44 % | +0.0 | 1.98 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.75 | 60 % | 61 % | 60 % | +0 pts | +6 % | 50 % | +0.3 | 1.71 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 4.0 | 2.12 | 50 % | 52 % | 50 % | +0 pts | +5 % | 39 % | +0.0 | 2.10 | Empate | Valor · asiática: devuelve 19 % |
| Córners Más 9.0 | 2.25 | 47 % | 47 % | 47 % | +0 pts | +5 % | 38 % | -0.0 | 2.24 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.60 | 66 % | 65 % | 66 % | +0 pts | +5 % | 55 % | +0.3 | 1.57 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners CA Huracan Más 3.5 | 1.90 | 55 % | 49 % | 55 % | +0 pts | +5 % | 51 % | +0.4 | 1.88 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Más 2.0 | 1.20 | 87 % | 87 % | 87 % | +0 pts | +5 % | 74 % | +1.0 | 1.18 | Empate | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners Más 7.0 | 1.42 | 74 % | 74 % | 74 % | +0 pts | +5 % | 62 % | +0.6 | 1.40 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Menos 7.0 | 1.14 | 91 % | 88 % | 91 % | +0 pts | +3 % | 84 % | +1.4 | 1.14 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 6 % |
| Córners Menos 11.0 | 1.35 | 76 % | 76 % | 76 % | +0 pts | +3 % | 66 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 3.1 % de la banca; Córners 1.er tiempo Menos 3.0 1.3 % de la banca; Más corners: CA Huracan 1.6 % de la banca; Córners CA Huracan Más 5.5 1.0 % de la banca; Córners 1.er tiempo Menos 5.0 5.2 % de la banca; Córners CA Huracan Más 4.5 1.4 % de la banca; Córners 1.er tiempo Menos 6.0 6.8 % de la banca; Córners 1.er tiempo Más 3.0 3.5 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5 | empate 2,90–3,20 (señal de pocos goles) | Goles Menos 2.5 | 18423 partidos: acierto 59.9 % contra 59.5 % del precio; ROI -3.9 % ± 1.1 (con la mejor cuota -0.3 %) |
| Ingeniero Analista #26 | parejo (ambos ≥2,00) y Más 1.5 >1,40 | Goles Menos 2.5 | 58298 partidos: acierto 53.4 % contra 53.3 % del precio; ROI -5.2 % ± 0.7 (con la mejor cuota -1.3 %) |
| Ingeniero Analista #420 | empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas | Empate | 48947 partidos: acierto 29.9 % contra 29.2 % del precio; ROI -5.0 % ± 1.3 (con la mejor cuota -0.1 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles CA Huracan Menos 2.5 + Instituto AC Cordoba o empate + Tarjetas Menos 8.5 | 62 % | 62 % | 58 % | 1.62 | 1.66 | 1.04 | 6 % | Favorito golpea temprano y gana | 0 % |
| Goles CA Huracan Menos 2.5 + Instituto AC Cordoba o empate + Remates Más 21.5 | 61 % | 60 % | 57 % | 1.65 | 1.70 | 1.03 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 0 % |
| Córners Menos 14.5 + Tarjetas Menos 8.5 + Remates Más 21.5 | 62 % | 61 % | 58 % | 1.61 | 1.66 | 1.0 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 37 % |
| Córners Menos 14.5 + Tarjetas CA Huracan Menos 3.5 | 55 % | 56 % | 51 % | 1.80 | 1.86 | 1.0 | 7 % | Favorito golpea temprano y gana | 26 % |
| Córners 2.º tiempo Más 1.5 + Tarjetas CA Huracan Menos 3.5 | 55 % | 56 % | 51 % | 1.81 | 1.86 | 1.0 | 7 % | Favorito golpea temprano y gana | 25 % |
| Córners CA Huracan Más 3.5 + Tiros al arco Instituto AC Cordoba Menos 8.5 | 52 % | 57 % | 47 % | 1.93 | 1.99 | 1.01 | 8 % | Favorito golpea temprano y gana | 48 % |
| ↳ Línea contra el guion (Más de un equipo que perdió: 2/11) |  |  |  |  |  |  |  |  |  |
| Córners CA Huracan Más 3.5 + Tiros al arco Más 4.5 | 51 % | 57 % | 47 % | 1.95 | 2.01 | 1.01 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 47 % |
| ↳ Línea contra el guion (Más de un equipo que perdió: 2/11) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.