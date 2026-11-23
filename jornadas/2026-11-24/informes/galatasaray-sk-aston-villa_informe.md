# Galatasaray SK - Aston Villa
Champions League Champions League · 2026-11-24 12:45

**Tipo de partido:** Parejo · abierto · caliente · **Favorito:** Aston Villa · primer gol: local 44 %, visitante 52 %, nadie 3 % · gol del favorito antes del 35′: 37 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), 1.er tiempo (Menos) y empate al descanso, Ambos marcan, Empate / doble oportunidad / HT-FT X, Tarjetas y faltas (Más). Poco favorecidos: Hándicap y victoria.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles; parejo y con mucho en juego: se cuidan |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Tarjetas y faltas (Más) | ✅ favorece | árbitro sin dato; los dos se juegan algo importante; parejo: más duelos y más faltas |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 36 % |
| Sorpresa: gana el no favorito | 29 % |
| Empate | 12 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 7 % |
| Favorito gana en partido trabado | 6 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.63 | 14.2 | 5.2 | 4.9 | 12.6 | 2.2 |
| visitante | 1.89 | 14.2 | 5.7 | 4.9 | 12.6 | 2.5 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.5 (3.6) · 1–6 | 1.6 (1.7) · 0–3 | 1.9 (1.9) · 0–4 | 1.6 (1.6) · 0–3 | 1.9 (2.1) · 0–4 |
| Córners | 9.7 (9.7) · 6–14 | 4.9 (4.9) · 2–8 | 4.8 (4.9) · 2–8 | 4.4 (4.6) · 2–7 | 5.3 (5.1) · 2–9 |
| Tarjetas (amarilla 1, roja 2) | 4.8 (4.5) · 2–8 | 2.2 (2.1) · 1–4 | 2.5 (2.4) · 1–5 | 1.6 (1.5) · 0–3 | 3.2 · 1–6 |
| Remates | 28.3 (28.1) · 21–36 | 14.2 (14.2) · 9–20 | 14.1 (14.2) · 9–20 | 12.7 · 8–18 | 15.6 · 10–21 |
| Tiros al arco | 10.8 (10.8) · 7–15 | 5.2 (5.2) · 2–8 | 5.6 (5.7) · 2–9 | 4.8 (5.0) · 2–8 | 5.9 · 3–9 |
| Faltas | 25.2 (24.5) · 19–32 | 12.6 (12.2) · 8–17 | 12.6 (12.2) · 8–17 | 11.3 · 7–16 | 13.9 · 9–19 |
| Fueras de lugar | 5.7 (5.8) · 2–9 | 3.7 (3.7) · 1–7 | 2.1 (2.1) · 0–4 | 2.6 (3.1) · 1–5 | 3.2 · 1–6 |
| Saques de meta | 14.1 (14.1) · 8–20 | 7.1 (7.0) · 3–12 | 7.0 (7.0) · 3–11 | 6.2 (6.6) · 3–10 | 7.8 · 4–12 |
| Saques de banda | 31.9 (31.6) · 22–42 | 16.2 (16.2) · 10–23 | 15.7 (15.6) · 9–23 | 14.2 (16.7) · 9–20 | 17.7 · 11–24 |
| Atajadas del portero | — | 3.7 · 1–7 | 3.5 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Galatasaray SK Menos 2.5 | 1.26 | 78 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Sorpresa: gana el no favorito (50 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.36 | 70 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · ★ enfoque a favor |
| Resultado y hándicap | Hándicap Galatasaray SK +2 | 1.28 | 78 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (26 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.39 | 78 % | 68 % | Favorito gana en partido trabado (72 %) | Partido abierto (ambos marcan y 3+ goles) (68 %) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Tarjetas | Tarjetas 1.er tiempo Más 0.5 | 1.28 | 78 % | 75 % | Expulsión antes del 70′ (94 %) | Partido abierto (ambos marcan y 3+ goles) (75 %) | Alta probabilidad · ★ enfoque a favor |
| Faltas | Faltas Más 24.5 | 1.93 | 55 % | 53 % | Expulsión antes del 70′ (58 %) | Sorpresa: gana el no favorito (53 %) | Contexto a favor (+7 pts) · Valor |
| Remates | Remates Galatasaray SK Menos 16.5 | 1.28 | 74 % | 70 % | Favorito gana en partido trabado (85 %) | Partido abierto (ambos marcan y 3+ goles) (70 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco Galatasaray SK Más 3.5 | 1.28 | 74 % | 59 % | Sorpresa: gana el no favorito (90 %) | Favorito gana en partido trabado (44 %) | Alta probabilidad · cuota por debajo de la justa |
| Fueras de lugar | Fueras de lugar Galatasaray SK Menos 4.5 | 1.35 | 70 % | 68 % | Sorpresa: gana el no favorito (73 %) | Favorito golpea temprano y gana (66 %) | Alta probabilidad · cuota por debajo de la justa |
| Saques de meta | Saques de meta Menos 16.5 | 1.28 | 74 % | 74 % | Favorito gana en partido trabado (77 %) | Expulsión antes del 70′ (71 %) | Alta probabilidad · cuota por debajo de la justa |
| Saques de banda | Saques de banda 1.er tiempo Menos 16.5 | 1.83 | 61 % | 60 % | Expulsión antes del 70′ (63 %) | Sorpresa: gana el no favorito (60 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jugadores | Wilfried Singo anota o asiste | 5.30 | 18 % | 10 % | Sorpresa: gana el no favorito (27 %) | Favorito golpea temprano y gana (0 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Más 7.0 | 1.29 | 80 % | 80 % | 80 % | -0 pts | +4 % | 70 % | +0.8 | 1.28 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Menos 12.0 | 1.30 | 78 % | 78 % | 78 % | +0 pts | +2 % | 69 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Hándicap Galatasaray SK +2 | 1.28 | 78 % | 76 % | 77 % | +2 pts | +0 % | 78 % | — | 1.32 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Menos 6.0 | 1.39 | 78 % | 76 % | 78 % | -0 pts | +9 % | 68 % | +0.8 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Goles Galatasaray SK Menos 2.5 | 1.26 | 78 % | 77 % | 77 % | +1 pts | -2 % | 78 % | +0.7 | 1.32 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tarjetas 1.er tiempo Más 0.5 | 1.28 | 78 % | 76 % | 76 % | +2 pts | -1 % | 75 % | +0.8 | 1.33 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Más 3.0 | 1.42 | 76 % | 76 % | 76 % | +0 pts | +8 % | 61 % | +0.7 | 1.36 | Empate | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 2.º tiempo Más 3.5 | 1.29 | 76 % | 75 % | 76 % | -0 pts | -2 % | 74 % | +0.8 | 1.36 | Expulsión antes del 70′ | Alta probabilidad |
| Tiros al arco Galatasaray SK Más 3.5 | 1.28 | 74 % | 76 % | 74 % | -0 pts | -5 % | 59 % | +0.7 | 1.39 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Remates Galatasaray SK Menos 16.5 | 1.28 | 74 % | 76 % | 73 % | +1 pts | -5 % | 70 % | +0.5 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 7.5 | 1.29 | 74 % | 75 % | 74 % | -0 pts | -5 % | 71 % | +0.7 | 1.39 | Expulsión antes del 70′ | Alta probabilidad |
| Saques de meta Menos 16.5 | 1.28 | 74 % | 76 % | 73 % | +1 pts | -5 % | 74 % | +0.5 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Remates Aston Villa Menos 16.5 | 1.28 | 74 % | 76 % | 74 % | -0 pts | -6 % | 68 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Remates Menos 31.5 | 1.29 | 74 % | 75 % | 73 % | +1 pts | -5 % | 65 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Más 8.5 | 1.29 | 74 % | 75 % | 75 % | -1 pts | -5 % | 50 % | +0.7 | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Menos 2.0 | 1.35 | 73 % | 73 % | 72 % | +2 pts | -1 % | 73 % | +0.3 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 25 % · ★ enfoque a favor |
| Córners Menos 11.5 | 1.30 | 73 % | 74 % | 73 % | +0 pts | -5 % | 71 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates Más 24.5 | 1.30 | 73 % | 74 % | 74 % | -0 pts | -5 % | 60 % | +0.6 | 1.40 | Empate | Alta probabilidad |
| Tiros al arco Galatasaray SK Menos 6.5 | 1.31 | 73 % | 74 % | 73 % | -0 pts | -4 % | 59 % | +0.5 | 1.41 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners 2.º tiempo Menos 6.5 | 1.28 | 73 % | 76 % | 73 % | +0 pts | -7 % | 71 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles Menos 4.5 | 1.38 | 73 % | 70 % | 70 % | +2 pts | +0 % | 73 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas Aston Villa Más 1.5 | 1.40 | 72 % | 69 % | 69 % | +4 pts | +1 % | 69 % | +0.7 | 1.42 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Saques de meta Aston Villa Menos 8.5 | 1.32 | 72 % | 73 % | 71 % | +1 pts | -4 % | 69 % | +0.5 | 1.42 | Favorito golpea temprano y gana | Alta probabilidad |
| Remates Aston Villa Más 11.5 | 1.31 | 72 % | 74 % | 72 % | +0 pts | -5 % | 62 % | +0.6 | 1.43 | Empate | Alta probabilidad · cuota por debajo de la justa |
| John McGinn faltas cometidas 1+ | 1.25 | 72 % | 71 % | 71 % | +1 pts | -10 % | 72 % | — | 1.43 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Faltas Más 24.5 | 1.93 | 55 % | 48 % | 48 % | +7 pts | +5 % | 53 % | +0.1 | 1.90 | Sorpresa: gana el no favorito | Contexto a favor (+7 pts) · Valor |
| Faltas Galatasaray SK Más 12.5 | 2.05 | 49 % | 45 % | 45 % | +5 pts | +1 % | 48 % | +0.0 | 2.11 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Faltas Aston Villa Más 12.5 | 2.05 | 49 % | 45 % | 45 % | +5 pts | +1 % | 46 % | +0.0 | 2.11 | Sorpresa: gana el no favorito | Contexto a favor (+5 pts) |
| Tarjetas Más 4.5 | 2.02 | 50 % | 46 % | 46 % | +4 pts | +2 % | 45 % | +0.1 | 2.07 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · ★ enfoque a favor |
| Tarjetas Más 5.5 | 2.85 | 35 % | 31 % | 31 % | +4 pts | -0 % | 30 % | -0.3 | 3.04 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · ★ enfoque a favor |
| Tarjetas Aston Villa Más 2.5 | 2.15 | 46 % | 43 % | 42 % | +4 pts | -1 % | 42 % | +0.0 | 2.26 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.75 | 42 % | 40 % | 42 % | -0 pts | +15 % | 34 % | -0.2 | 2.52 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.82 | 62 % | 60 % | 62 % | -0 pts | +13 % | 52 % | +0.3 | 1.66 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Saques de banda 1.er tiempo Menos 16.5 | 1.83 | 61 % | 51 % | 61 % | -0 pts | +12 % | 60 % | +0.5 | 1.69 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Menos 6.0 | 1.39 | 78 % | 76 % | 78 % | -0 pts | +9 % | 68 % | +0.8 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 3.0 | 1.42 | 76 % | 76 % | 76 % | +0 pts | +8 % | 61 % | +0.7 | 1.36 | Empate | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Más 4.0 | 1.91 | 56 % | 58 % | 56 % | +0 pts | +7 % | 43 % | +0.2 | 1.85 | Empate | Valor · asiática: devuelve 19 % |
| Córners Más 10.0 | 2.45 | 43 % | 43 % | 43 % | -0 pts | +6 % | 35 % | -0.1 | 2.43 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Faltas Más 24.5 | 1.93 | 55 % | 48 % | 48 % | +7 pts | +5 % | 53 % | +0.1 | 1.90 | Sorpresa: gana el no favorito | Contexto a favor (+7 pts) · Valor |
| Córners Más 9.0 | 1.87 | 56 % | 56 % | 57 % | -0 pts | +5 % | 46 % | +0.2 | 1.84 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.87 | 56 % | 56 % | 56 % | +0 pts | +5 % | 48 % | +0.1 | 1.84 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.52 | 69 % | 69 % | 69 % | -0 pts | +5 % | 58 % | +0.5 | 1.49 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 2.0 | 1.16 | 90 % | 88 % | 90 % | +0 pts | +4 % | 76 % | +1.1 | 1.15 | Empate | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Menos 11.0 | 1.52 | 68 % | 68 % | 68 % | +0 pts | +4 % | 58 % | +0.4 | 1.51 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Menos 7.0 | 1.18 | 88 % | 86 % | 88 % | -0 pts | +4 % | 80 % | +1.2 | 1.17 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 8 % |
| Córners Más 7.0 | 1.29 | 80 % | 80 % | 80 % | -0 pts | +4 % | 70 % | +0.8 | 1.28 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.1 % de la banca; Córners 1.er tiempo Menos 5.0 4.0 % de la banca; Saques de banda 1.er tiempo Menos 16.5 3.6 % de la banca; Córners 1.er tiempo Menos 6.0 5.5 % de la banca; Córners 1.er tiempo Más 3.0 4.5 % de la banca; Córners 1.er tiempo Más 4.0 2.0 % de la banca; Córners Más 10.0 1.0 % de la banca; Faltas Más 24.5 1.5 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #313 | Más 2.5 ≤1,45 → gol en el 1.er tiempo | Goles 1.er tiempo Más 0.5 | sin historial con cuotas (medir en el registro) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí + Córners 1.er tiempo Menos 8.5 | 62 % | 63 % | 57 % | 1.62 | 1.67 | 1.15 | 8 % | Expulsión antes del 70′ | 58 % |
| Ambos 1+ tarjetas: Sí + Tarjetas Galatasaray SK Más 1.5 | 62 % | 63 % | 57 % | 1.62 | 1.67 | 1.12 | 7 % | Expulsión antes del 70′ | 59 % |
| Hándicap Galatasaray SK +2 + Goles Aston Villa Menos 3.5 + Tiros al arco Aston Villa Menos 6.5 | 57 % | 57 % | 52 % | 1.76 | 1.82 | 1.21 | 9 % | Empate | 38 % |
| Goles Aston Villa Menos 3.5 + Córners 1.er tiempo Menos 8.5 + Tiros al arco Aston Villa Menos 6.5 | 62 % | 62 % | 58 % | 1.61 | 1.66 | 1.08 | 7 % | Empate | 43 % |
| Goles Menos 5.5 + Tarjetas 1.er tiempo Más 0.5 + Tiros al arco Menos 14.5 | 61 % | 61 % | 57 % | 1.64 | 1.69 | 1.06 | 7 % | Expulsión antes del 70′ | 49 % |
| Goles 2.º tiempo Menos 2.5 + Tiros al arco Menos 14.5 + Córners Galatasaray SK Más 1.5 | 60 % | 59 % | 55 % | 1.68 | 1.73 | 1.06 | 7 % | Empate | 42 % |
| Tarjetas Aston Villa Más 1.5 + Goles Menos 5.5 | 62 % | 63 % | 58 % | 1.60 | 1.65 | 1.01 | 6 % | Expulsión antes del 70′ | 54 % |
| Tarjetas Más 3.5 + Goles Galatasaray SK Menos 3.5 | 62 % | 63 % | 58 % | 1.61 | 1.65 | 1.01 | 6 % | Expulsión antes del 70′ | 52 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.