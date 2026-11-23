# Manchester City - SSC Napoli
Champions League Champions League · 2026-11-24 15:00

**Tipo de partido:** Favorito claro · abierto · normal · **Favorito:** Manchester City · primer gol: local 76 %, visitante 22 %, nadie 2 % · gol del favorito antes del 35′: 56 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Hándicap y victoria de Manchester City, Goles de Manchester City (Más), Remates / tiros al arco de Manchester City, Córners de Manchester City (Más) / Más córners: Manchester City.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Hándicap y victoria de Manchester City | ✅ favorece | favorito claro: manda en el marcador y en el territorio |
| Goles de Manchester City (Más) | ✅ favorece | favorito claro contra rival que sufre |
| Remates / tiros al arco de Manchester City | ✅ favorece | el que domina remata más |
| Córners de Manchester City (Más) / Más córners: Manchester City | ✅ favorece | Manchester City empuja más y el rival se encierra o cede territorio |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Córners totales | ➖ neutro | si el favorito marca pronto, sus córners se apagan; si el rival forzara, suben |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; los dos se juegan algo importante; favorito claro: poca fricción y, si hay goleada, menos tarjetas |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 41 % |
| Favorito golpea temprano y gana | 22 % |
| Favorito gana en partido trabado | 12 % |
| Expulsión antes del 70′ | 10 % |
| Empate | 8 % |
| Sorpresa: gana el no favorito | 8 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 2.73 | 21.0 | 7.9 | 6.6 | 9.7 | 1.5 |
| visitante | 0.94 | 9.3 | 3.4 | 3.1 | 13.3 | 2.6 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.6 (3.8) · 1–6 | 2.7 (2.8) · 1–5 | 0.9 (1.0) · 0–2 | 1.7 (1.7) · 0–3 | 2.0 (2.1) · 0–4 |
| Córners | 9.6 (9.6) · 5–14 | 6.5 (6.6) · 3–11 | 3.1 (3.1) · 1–6 | 4.4 (4.7) · 2–7 | 5.2 (4.9) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 4.1 (3.9) · 1–7 | 1.5 (1.4) · 0–3 | 2.6 (2.5) · 1–5 | 1.5 (1.4) · 0–3 | 2.6 · 1–5 |
| Remates | 30.4 (30.1) · 23–39 | 21.1 (21.0) · 14–29 | 9.4 (9.3) · 5–14 | 14.0 · 9–19 | 16.5 · 11–22 |
| Tiros al arco | 11.4 (11.3) · 7–16 | 7.9 (7.9) · 4–12 | 3.4 (3.4) · 1–6 | 5.2 (5.2) · 2–8 | 6.1 · 3–10 |
| Faltas | 23.2 (22.5) · 17–30 | 9.8 (9.5) · 6–14 | 13.4 (13.0) · 9–18 | 10.4 · 6–15 | 12.8 · 8–17 |
| Fueras de lugar | 3.9 (3.9) · 1–7 | 1.3 (1.3) · 0–3 | 2.6 (2.6) · 0–5 | 1.7 (2.1) · 0–4 | 2.2 · 0–4 |
| Saques de meta | 15.0 (15.1) · 9–22 | 5.0 (5.0) · 2–9 | 10.0 (10.1) · 5–16 | 6.8 (7.1) · 3–11 | 8.2 · 4–13 |
| Saques de banda | 30.3 (30.2) · 21–40 | 15.1 (15.2) · 9–22 | 15.2 (15.2) · 9–22 | 13.5 (15.9) · 8–19 | 16.8 · 11–23 |
| Atajadas del portero | — | 2.5 · 0–5 | 5.2 · 2–9 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Menos 2.5 | 1.28 | 77 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (63 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: No | 2.20 | 43 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Cara |
| Resultado y hándicap | Gana Manchester City | 1.30 | 76 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.42 | 78 % | 69 % | Favorito golpea temprano y gana (71 %) | Sorpresa: gana el no favorito (67 %) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Tarjetas | Tarjetas SSC Napoli Menos 3.5 | 1.27 | 74 % | 78 % | Favorito golpea temprano y gana (83 %) | Expulsión antes del 70′ (38 %) | Alta probabilidad · cuota por debajo de la justa |
| Faltas | Faltas SSC Napoli Más 12.5 | 1.75 | 58 % | 55 % | Expulsión antes del 70′ (66 %) | Favorito golpea temprano y gana (55 %) | Contexto a favor (+5 pts) |
| Remates | Remates SSC Napoli Menos 11.5 | 1.25 | 75 % | 69 % | Favorito gana en partido trabado (86 %) | Sorpresa: gana el no favorito (68 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco Manchester City Más 6.5 | 1.42 | 66 % | 73 % | Partido abierto (ambos marcan y 3+ goles) (75 %) | Empate (39 %) | Alta probabilidad · cuota por debajo de la justa |
| Fueras de lugar | Fueras de lugar SSC Napoli Menos 3.5 | 1.29 | 74 % | 71 % | Sorpresa: gana el no favorito (77 %) | Favorito golpea temprano y gana (71 %) | Alta probabilidad |
| Saques de meta | Saques de meta Manchester City Menos 6.5 | 1.27 | 76 % | 73 % | Sorpresa: gana el no favorito (82 %) | Favorito golpea temprano y gana (73 %) | Alta probabilidad |
| Saques de banda | Saques de banda 1.er tiempo Menos 15.5 | 1.91 | 59 % | 59 % | Sorpresa: gana el no favorito (60 %) | Expulsión antes del 70′ (58 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jugadores | Gianluigi Donnarumma atajadas 3+ | 2.18 | 43 % | 42 % | Empate (47 %) | Expulsión antes del 70′ (39 %) | Cara |
| Quién saca más | Más tarjetas: SSC Napoli | 1.55 | 63 % | 61 % | Expulsión antes del 70′ (67 %) | Favorito golpea temprano y gana (61 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Menos 12.0 | 1.29 | 79 % | 79 % | 79 % | +0 pts | +2 % | 71 % | +0.7 | 1.30 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 8 % |
| Córners Más 7.0 | 1.30 | 79 % | 79 % | 79 % | -0 pts | +3 % | 66 % | +0.8 | 1.30 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 10 % |
| Tarjetas Manchester City Más 0.5 | 1.27 | 78 % | 76 % | 76 % | +2 pts | -1 % | 73 % | +0.8 | 1.32 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 1.er tiempo Menos 6.0 | 1.42 | 78 % | 75 % | 77 % | +1 pts | +10 % | 69 % | +0.7 | 1.33 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Goles 1.er tiempo Menos 2.5 | 1.28 | 77 % | 76 % | 75 % | +2 pts | -1 % | 77 % | +0.6 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Manchester City Más 1.5 | 1.26 | 77 % | 77 % | 78 % | -1 pts | -3 % | 77 % | +0.8 | 1.34 | Empate | Alta probabilidad · ★ enfoque a favor |
| Goles SSC Napoli Menos 1.5 | 1.29 | 76 % | 75 % | 75 % | +2 pts | -1 % | 76 % | +0.6 | 1.35 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.39 | 76 % | 77 % | 77 % | -0 pts | +6 % | 63 % | +0.7 | 1.35 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Gana Manchester City | 1.30 | 76 % | 76 % | 76 % | -0 pts | -1 % | 76 % | — | 1.35 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Saques de meta Manchester City Menos 6.5 | 1.27 | 76 % | 76 % | 75 % | +1 pts | -4 % | 73 % | +0.6 | 1.36 | Favorito golpea temprano y gana | Alta probabilidad |
| Remates SSC Napoli Menos 11.5 | 1.25 | 75 % | 78 % | 77 % | -2 pts | -6 % | 69 % | +0.6 | 1.37 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas 1.er tiempo Más 0.5 | 1.34 | 75 % | 72 % | 73 % | +2 pts | +0 % | 72 % | +0.8 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad |
| Tiros al arco Menos 13.5 | 1.28 | 75 % | 76 % | 75 % | -0 pts | -4 % | 64 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Manchester City Más 4.5 | 1.25 | 75 % | 78 % | 75 % | -1 pts | -7 % | 69 % | +0.7 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Tarjetas Menos 5.5 | 1.25 | 75 % | 78 % | 78 % | -3 pts | -7 % | 78 % | +0.6 | 1.38 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas Más 2.5 | 1.33 | 75 % | 72 % | 72 % | +2 pts | -1 % | 64 % | +0.7 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 11.5 | 1.29 | 74 % | 75 % | 74 % | +1 pts | -4 % | 72 % | +0.6 | 1.39 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tarjetas SSC Napoli Menos 3.5 | 1.27 | 74 % | 76 % | 77 % | -3 pts | -6 % | 78 % | +0.6 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Ambos 1+ tarjetas: Sí | 1.35 | 74 % | 71 % | 72 % | +2 pts | -0 % | 68 % | — | 1.39 | Favorito golpea temprano y gana | Alta probabilidad |
| Fueras de lugar SSC Napoli Menos 3.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -5 % | 71 % | +0.5 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad |
| Remates Manchester City Más 17.5 | 1.28 | 74 % | 76 % | 73 % | +1 pts | -6 % | 70 % | +0.6 | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Goles 1.er tiempo Menos 2.25 | 1.35 | 74 % | 72 % | 72 % | +2 pts | -1 % | 74 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 13 % |
| Tiros al arco SSC Napoli Menos 4.5 | 1.30 | 74 % | 74 % | 74 % | -0 pts | -4 % | 65 % | +0.5 | 1.40 | Sorpresa: gana el no favorito | Alta probabilidad |
| Remates Más 26.5 | 1.32 | 73 % | 73 % | 72 % | +2 pts | -3 % | 66 % | +0.6 | 1.40 | Favorito gana en partido trabado | Alta probabilidad |
| Tarjetas SSC Napoli Más 1.5 | 1.36 | 73 % | 71 % | 71 % | +2 pts | -0 % | 65 % | +0.7 | 1.40 | Favorito golpea temprano y gana | Alta probabilidad |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Faltas Más 22.5 | 1.93 | 54 % | 48 % | 49 % | +5 pts | +5 % | 53 % | +0.1 | 1.91 | Empate | Contexto a favor (+5 pts) · Valor |
| Faltas SSC Napoli Más 12.5 | 1.75 | 58 % | 54 % | 54 % | +5 pts | +2 % | 55 % | +0.3 | 1.77 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.87 | 41 % | 38 % | 41 % | +0 pts | +18 % | 34 % | -0.2 | 2.56 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.88 | 61 % | 58 % | 61 % | +1 pts | +16 % | 52 % | +0.3 | 1.68 | Sorpresa: gana el no favorito | Valor · asiática: devuelve 16 % |
| Saques de banda 1.er tiempo Menos 15.5 | 1.91 | 59 % | 49 % | 59 % | +0 pts | +13 % | 59 % | +0.5 | 1.75 | Expulsión antes del 70′ | Valor · ⚠ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Menos 3.0 | 5.00 | 22 % | 21 % | 22 % | +0 pts | +11 % | 18 % | -0.7 | 4.95 | Empate | Valor frágil (depende de un guion) · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.42 | 78 % | 75 % | 77 % | +1 pts | +10 % | 69 % | +0.7 | 1.33 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 3.0 | 1.39 | 76 % | 77 % | 77 % | -0 pts | +6 % | 63 % | +0.7 | 1.35 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners Menos 9.0 | 2.37 | 45 % | 44 % | 44 % | +0 pts | +6 % | 38 % | -0.2 | 2.34 | Sorpresa: gana el no favorito | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.82 | 58 % | 58 % | 57 % | +0 pts | +5 % | 49 % | +0.1 | 1.79 | Sorpresa: gana el no favorito | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 4.0 | 1.85 | 57 % | 60 % | 57 % | -1 pts | +5 % | 44 % | +0.2 | 1.82 | Favorito golpea temprano y gana | Valor · asiática: devuelve 19 % |
| Faltas Más 22.5 | 1.93 | 54 % | 48 % | 49 % | +5 pts | +5 % | 53 % | +0.1 | 1.91 | Empate | Contexto a favor (+5 pts) · Valor |
| Córners Más 8.0 | 1.55 | 67 % | 68 % | 68 % | -0 pts | +4 % | 54 % | +0.5 | 1.53 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 11.0 | 1.50 | 70 % | 69 % | 69 % | +1 pts | +4 % | 60 % | +0.4 | 1.48 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Más 9.0 | 1.91 | 55 % | 55 % | 55 % | -0 pts | +4 % | 42 % | +0.2 | 1.90 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Menos 7.0 | 1.19 | 87 % | 85 % | 87 % | +0 pts | +4 % | 80 % | +1.2 | 1.18 | Sorpresa: gana el no favorito | Alta probabilidad · Valor · asiática: devuelve 7 % |
| Córners 1.er tiempo Más 2.0 | 1.15 | 90 % | 89 % | 90 % | +0 pts | +4 % | 78 % | +1.1 | 1.14 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 12 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.4 % de la banca; Córners 1.er tiempo Menos 5.0 4.4 % de la banca; Saques de banda 1.er tiempo Menos 15.5 3.6 % de la banca; Córners 1.er tiempo Menos 3.0 0.7 % de la banca; Córners 1.er tiempo Menos 6.0 6.0 % de la banca; Córners 1.er tiempo Más 3.0 4.0 % de la banca; Córners Menos 9.0 1.1 % de la banca; Córners Menos 10.0 1.6 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #400 | local ≤1,50 y 1T Más 1.5 ≤2,15 | Goles Más 2.5 | 11239 partidos: acierto 61.3 % contra 60.7 % del precio; ROI -3.4 % ± 1.5 (con la mejor cuota -0.0 %) |
| Ingeniero Analista #453 | local ≤1,50 y empate ≥4,10 | Goles Más 2.5 | 10604 partidos: acierto 61.9 % contra 61.4 % del precio; ROI -3.5 % ± 1.5 (con la mejor cuota -0.1 %) |
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #313 | Más 2.5 ≤1,45 → gol en el 1.er tiempo | Goles 1.er tiempo Más 0.5 | sin historial con cuotas (medir en el registro) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Gana Manchester City + Tarjetas Manchester City Más 0.5 | 55 % | 56 % | 52 % | 1.81 | 1.86 | 1.26 | 9 % | Favorito gana en partido trabado | 63 % |
| Ambos 1+ tarjetas: Sí + Hándicap SSC Napoli +4 + Goles Manchester City Menos 4.5 | 61 % | 63 % | 57 % | 1.65 | 1.70 | 1.14 | 8 % | Empate | 44 % |
| Tarjetas SSC Napoli Más 1.5 + Hándicap SSC Napoli +4 + Goles Manchester City Menos 4.5 | 60 % | 62 % | 56 % | 1.66 | 1.71 | 1.14 | 8 % | Empate | 43 % |
| Tarjetas Más 1.5 + Córners 1.er tiempo Menos 5.5 | 62 % | 64 % | 58 % | 1.61 | 1.66 | 1.0 | 6 % | Expulsión antes del 70′ | 60 % |
| Goles Menos 4.5 + Tarjetas Más 1.5 + Córners 2.º tiempo Más 1.5 | 60 % | 61 % | 56 % | 1.65 | 1.70 | 1.01 | 6 % | Empate | 44 % |
| Gana Manchester City + Tarjetas Manchester City Más 0.5 + Goles SSC Napoli Menos 2.5 | 57 % | 58 % | 53 % | 1.75 | 1.81 | 1.02 | 6 % | Favorito gana en partido trabado | 63 % |
| Saques de banda 1.er tiempo Menos 15.5 + Córners 2.º tiempo Más 1.5 | 57 % | 66 % | 52 % | 1.77 | 1.82 | 1.0 | 8 % | Sorpresa: gana el no favorito | 56 % |
| ↳ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |  |  |  |  |  |  |  |  |  |
| Saques de banda 1.er tiempo Menos 15.5 + Córners Más 4.5 | 56 % | 66 % | 52 % | 1.77 | 1.83 | 1.0 | 8 % | Sorpresa: gana el no favorito | 55 % |
| ↳ Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.