# Argentinos Juniors - CA Independiente
Argentina Liga Profesional · 2026-11-21 15:00

**Tipo de partido:** Favorito leve · cerrado · caliente · **Favorito:** Argentinos Juniors · primer gol: local 55 %, visitante 33 %, nadie 12 % · gol del favorito antes del 35′: 32 %

**Base de la liga:** Argentina Liga Profesional · 2.11 goles/partido, Más 2.5 35 %, ambos marcan 43 % (1268 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Resultado / hándicap | ➖ neutro | Argentinos Juniors favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Empate | 23 % |
| Sorpresa: gana el no favorito | 19 % |
| Partido abierto (ambos marcan y 3+ goles) | 18 % |
| Favorito gana en partido trabado | 14 % |
| Favorito golpea temprano y gana | 13 % |
| Expulsión antes del 70′ | 13 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.33 | 16.1 | 5.0 | 4.8 | 11.8 | 2.8 |
| visitante | 0.80 | 11.7 | 3.8 | 4.8 | 11.8 | 3.1 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.1 (2.1) · 0–4 | 1.3 (1.3) · 0–3 | 0.8 (0.8) · 0–2 | 0.9 (1.0) · 0–2 | 1.2 (1.2) · 0–3 |
| Córners | 9.5 (9.6) · 5–14 | 4.7 · 2–8 | 4.8 · 2–8 | 4.3 (4.7) · 2–7 | 5.2 (5.0) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.9 (5.8) · 3–10 | 2.8 (2.8) · 1–5 | 3.1 (3.1) · 1–5 | 1.9 (2.0) · 0–4 | 3.9 · 1–7 |
| Remates | 27.9 (27.7) · 21–36 | 16.1 (16.1) · 10–23 | 11.8 (11.7) · 7–17 | 12.5 · 8–17 | 15.4 · 10–21 |
| Tiros al arco | 8.9 (8.9) · 5–13 | 5.0 (5.0) · 2–8 | 3.9 (3.8) · 1–7 | 4.0 · 2–7 | 4.9 · 2–8 |
| Faltas | 23.7 · 17–30 | 11.9 · 8–16 | 11.8 · 7–16 | 10.6 · 6–15 | 13.1 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 15.9 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.9 · 5–13 |
| Saques de banda | 39.9 · 29–52 | 20.0 · 12–28 | 19.9 · 12–28 | 17.8 · 11–25 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.0 · 1–6 | 3.8 · 1–7 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Menos 1.5 | 1.30 | 75 % | (lo define el marcador) | Favorito gana en partido trabado (99 %) | Partido abierto (ambos marcan y 3+ goles) (43 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: No | 1.65 | 57 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Cara |
| Resultado y hándicap | Hándicap CA Independiente +2 | 1.25 | 78 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (35 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.39 | 79 % | 70 % | Expulsión antes del 70′ (73 %) | Partido abierto (ambos marcan y 3+ goles) (70 %) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas | Ambos 2+ tarjetas: Sí | 1.50 | 66 % | 57 % | Expulsión antes del 70′ (82 %) | Favorito golpea temprano y gana (57 %) | Alta probabilidad |
| Remates | Remates Menos 31.5 | 1.25 | 75 % | 62 % | Empate (81 %) | Partido abierto (ambos marcan y 3+ goles) (62 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco Argentinos Juniors Menos 6.5 | 1.28 | 75 % | 58 % | Sorpresa: gana el no favorito (86 %) | Partido abierto (ambos marcan y 3+ goles) (58 %) | Alta probabilidad |
| Quién saca más | Más corners: CA Independiente | 3.60 | 34 % | 29 % | Favorito golpea temprano y gana (41 %) | Sorpresa: gana el no favorito (29 %) | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Menos 12.0 | 1.28 | 80 % | 79 % | 80 % | +0 pts | +2 % | 69 % | +0.8 | 1.29 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners Más 7.0 | 1.30 | 79 % | 79 % | 79 % | +0 pts | +3 % | 68 % | +0.8 | 1.30 | Expulsión antes del 70′ | Alta probabilidad · asiática: devuelve 11 % |
| Córners 1.er tiempo Menos 6.0 | 1.39 | 79 % | 76 % | 79 % | +0 pts | +10 % | 70 % | +0.8 | 1.30 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Hándicap CA Independiente +2 | 1.25 | 78 % | 78 % | 78 % | +0 pts | -2 % | 78 % | — | 1.32 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners CA Independiente Más 2.5 | 1.32 | 76 % | 71 % | 76 % | +0 pts | +0 % | 72 % | +0.9 | 1.36 | Sorpresa: gana el no favorito | Alta probabilidad |
| Remates Menos 31.5 | 1.25 | 75 % | 77 % | 75 % | +0 pts | -6 % | 62 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Argentinos Juniors Menos 6.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -4 % | 58 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Menos 1.5 | 1.30 | 75 % | 75 % | 75 % | +0 pts | -3 % | 75 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Córners Menos 11.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -4 % | 71 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 2.º tiempo Menos 6.5 | 1.25 | 75 % | 78 % | 75 % | +0 pts | -6 % | 73 % | +0.5 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Más 3.0 | 1.42 | 75 % | 76 % | 75 % | +0 pts | +6 % | 61 % | +0.6 | 1.38 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 2.º tiempo Más 3.5 | 1.32 | 75 % | 73 % | 75 % | +0 pts | -2 % | 72 % | +0.7 | 1.38 | Expulsión antes del 70′ | Alta probabilidad |
| Goles Argentinos Juniors Más 0.5 | 1.30 | 74 % | 74 % | 74 % | +0 pts | -3 % | 74 % | +0.7 | 1.39 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Más 7.5 | 1.30 | 73 % | 74 % | 73 % | +0 pts | -5 % | 70 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Argentinos Juniors Más 3.5 | 1.31 | 73 % | 74 % | 73 % | +0 pts | -5 % | 58 % | +0.6 | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tiros al arco CA Independiente Más 2.5 | 1.31 | 72 % | 74 % | 72 % | +0 pts | -5 % | 55 % | +0.6 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Goles Más 1.25 | 1.36 | 72 % | 72 % | 72 % | +0 pts | -2 % | 72 % | +0.6 | 1.43 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 13 % |
| Remates Argentinos Juniors Menos 18.5 | 1.31 | 72 % | 74 % | 72 % | +0 pts | -6 % | 64 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Menos 5.5 | 1.39 | 71 % | 69 % | 71 % | +0 pts | -1 % | 70 % | +0.6 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Menos 2.75 | 1.38 | 71 % | 71 % | 71 % | +0 pts | -2 % | 71 % | +0.4 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % · ★ enfoque a favor |
| Remates Más 24.5 | 1.34 | 71 % | 72 % | 71 % | +0 pts | -5 % | 66 % | +0.6 | 1.45 | Empate | Alta probabilidad |
| Remates CA Independiente Menos 13.5 | 1.33 | 71 % | 73 % | 71 % | +0 pts | -6 % | 63 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Argentinos Juniors Más 13.5 | 1.32 | 70 % | 73 % | 70 % | +0 pts | -7 % | 65 % | +0.5 | 1.46 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates CA Independiente Más 9.5 | 1.34 | 70 % | 72 % | 70 % | +0 pts | -6 % | 63 % | +0.5 | 1.46 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Córners Menos 11.0 | 1.50 | 70 % | 69 % | 70 % | +0 pts | +5 % | 59 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners CA Independiente Más 6.5 | 6.80 | 19 % | 14 % | 19 % | +0 pts | +26 % | 15 % | -0.7 | 6.04 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: CA Independiente | 3.60 | 34 % | 23 % | 34 % | +0 pts | +23 % | 29 % | — | 3.11 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners CA Independiente Más 5.5 | 4.20 | 29 % | 22 % | 29 % | +0 pts | +21 % | 24 % | -0.3 | 3.73 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners CA Independiente Más 7.5 | 10.00 | 12 % | 9 % | 12 % | +0 pts | +20 % | 10 % | -1.0 | 10.00 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 4.0 | 2.77 | 43 % | 40 % | 43 % | +0 pts | +19 % | 33 % | -0.1 | 2.45 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.83 | 63 % | 60 % | 63 % | +0 pts | +16 % | 52 % | +0.3 | 1.63 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 3.0 | 4.80 | 24 % | 22 % | 24 % | +0 pts | +14 % | 18 % | -0.6 | 4.60 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners CA Independiente Más 4.5 | 2.65 | 43 % | 35 % | 43 % | +0 pts | +13 % | 38 % | +0.1 | 2.46 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 6.0 | 1.39 | 79 % | 76 % | 79 % | +0 pts | +10 % | 70 % | +0.8 | 1.30 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 3.0 | 1.42 | 75 % | 76 % | 75 % | +0 pts | +6 % | 61 % | +0.6 | 1.38 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners Menos 9.0 | 2.35 | 45 % | 45 % | 45 % | +0 pts | +6 % | 36 % | -0.2 | 2.32 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.82 | 58 % | 58 % | 58 % | +0 pts | +6 % | 48 % | +0.1 | 1.78 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners CA Independiente Más 3.5 | 1.78 | 59 % | 52 % | 59 % | +0 pts | +5 % | 54 % | +0.5 | 1.75 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Menos 11.0 | 1.50 | 70 % | 69 % | 70 % | +0 pts | +5 % | 59 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners 1.er tiempo Más 4.0 | 1.91 | 55 % | 58 % | 55 % | +0 pts | +5 % | 43 % | +0.1 | 1.89 | Expulsión antes del 70′ | Valor · asiática: devuelve 19 % |
| Córners Más 9.0 | 1.93 | 54 % | 55 % | 54 % | +0 pts | +5 % | 44 % | +0.2 | 1.91 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.55 | 67 % | 68 % | 67 % | +0 pts | +5 % | 57 % | +0.5 | 1.53 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Menos 7.0 | 1.18 | 89 % | 86 % | 89 % | +0 pts | +4 % | 81 % | +1.3 | 1.16 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 7 % |
| Córners 1.er tiempo Más 2.0 | 1.16 | 89 % | 88 % | 89 % | +0 pts | +4 % | 76 % | +1.1 | 1.15 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 13 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners CA Independiente Más 6.5 1.1 % de la banca; Más corners: CA Independiente 2.2 % de la banca; Córners CA Independiente Más 5.5 1.6 % de la banca; Córners CA Independiente Más 7.5 0.6 % de la banca; Córners 1.er tiempo Menos 4.0 2.7 % de la banca; Córners 1.er tiempo Menos 5.0 4.7 % de la banca; Córners 1.er tiempo Menos 3.0 0.9 % de la banca; Córners CA Independiente Más 4.5 2.0 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5 | empate 2,90–3,20 (señal de pocos goles) | Goles Menos 2.5 | 18423 partidos: acierto 59.9 % contra 59.5 % del precio; ROI -3.9 % ± 1.1 (con la mejor cuota -0.3 %) |
| Ingeniero Analista #26 | parejo (ambos ≥2,00) y Más 1.5 >1,40 | Goles Menos 2.5 | 58298 partidos: acierto 53.4 % contra 53.3 % del precio; ROI -5.2 % ± 0.7 (con la mejor cuota -1.3 %) |
| Ingeniero Analista #420 | empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas | Empate | 48947 partidos: acierto 29.9 % contra 29.2 % del precio; ROI -5.0 % ± 1.3 (con la mejor cuota -0.1 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Tarjetas Más 3.5 + Argentinos Juniors o empate | 61 % | 62 % | 57 % | 1.65 | 1.70 | 1.07 | 8 % | Empate | 0 % |
| Ambos 1+ tarjetas: Sí + Tarjetas Más 3.5 + Remates Más 23.5 | 60 % | 60 % | 56 % | 1.67 | 1.72 | 1.07 | 8 % | Expulsión antes del 70′ | 52 % |
| Córners 1.er tiempo Menos 5.5 + Hándicap CA Independiente +3 + Tiros al arco Argentinos Juniors Menos 8.5 | 62 % | 64 % | 58 % | 1.61 | 1.66 | 1.02 | 7 % | Sorpresa: gana el no favorito | 48 % |
| Córners 1.er tiempo Menos 5.5 + Goles 1.er tiempo Menos 2.5 + Hándicap CA Independiente +3 | 62 % | 65 % | 58 % | 1.61 | 1.66 | 1.02 | 7 % | Empate | 51 % |
| Córners 2.º tiempo Más 2.5 + Tiros al arco Menos 13.5 + Remates Más 23.5 | 62 % | 61 % | 58 % | 1.61 | 1.66 | 0.99 | 7 % | Sorpresa: gana el no favorito | 59 % |
| Córners 2.º tiempo Más 2.5 + Goles 2.º tiempo Menos 2.5 + Argentinos Juniors o empate | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.0 | 6 % | Empate | 0 % |
| Goles Argentinos Juniors Menos 3.5 + Tarjetas CA Independiente Más 2.5 | 57 % | 57 % | 52 % | 1.76 | 1.81 | 1.01 | 6 % | Expulsión antes del 70′ | 46 % |
| Córners CA Independiente Más 3.5 + Goles Argentinos Juniors Menos 3.5 | 57 % | 63 % | 52 % | 1.76 | 1.81 | 1.0 | 8 % | Favorito golpea temprano y gana | 54 % |
| ↳ Línea contra el guion (Más de un equipo que perdió: 2/11) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.