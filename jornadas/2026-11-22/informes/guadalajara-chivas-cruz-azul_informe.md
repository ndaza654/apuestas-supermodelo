# Guadalajara Chivas - Cruz Azul
México Liga MX · 2026-11-22 18:07

**Tipo de partido:** Parejo · abierto · caliente · **Favorito:** Guadalajara Chivas · primer gol: local 51 %, visitante 44 %, nadie 5 % · gol del favorito antes del 35′: 34 %

**Base de la liga:** México Liga MX · 2.83 goles/partido, Más 2.5 55 %, ambos marcan 57 % (740 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

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
| Partido abierto (ambos marcan y 3+ goles) | 30 % |
| Sorpresa: gana el no favorito | 28 % |
| Empate | 15 % |
| Expulsión antes del 70′ | 11 % |
| Favorito golpea temprano y gana | 8 % |
| Favorito gana en partido trabado | 8 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.64 | 16.1 | 5.4 | 5.4 | 11.8 | 2.5 |
| visitante | 1.43 | 13.0 | 4.4 | 5.4 | 11.8 | 2.7 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.1 (3.1) · 1–5 | 1.6 (1.6) · 0–3 | 1.4 (1.4) · 0–3 | 1.4 (1.3) · 0–3 | 1.7 (1.8) · 0–3 |
| Córners | 10.8 (10.8) · 6–15 | 5.4 · 2–9 | 5.4 · 2–9 | 4.9 (5.2) · 2–8 | 5.9 (5.7) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 5.2 (5.2) · 2–9 | 2.5 (2.5) · 1–5 | 2.7 (2.7) · 1–5 | 1.7 (1.8) · 0–4 | 3.5 · 1–6 |
| Remates | 29.2 (28.8) · 21–37 | 16.1 (16.1) · 10–23 | 13.0 (13.0) · 8–19 | 13.1 · 8–18 | 16.1 · 11–22 |
| Tiros al arco | 9.8 (9.8) · 6–14 | 5.4 (5.4) · 2–9 | 4.4 (4.4) · 2–7 | 4.4 · 2–7 | 5.4 · 2–9 |
| Faltas | 23.6 · 17–30 | 11.8 · 7–16 | 11.9 · 8–16 | 10.6 · 7–15 | 13.1 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.1 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 39.9 · 29–52 | 19.9 · 12–28 | 20.0 · 12–28 | 17.8 · 12–24 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.0 · 1–6 | 3.8 · 1–7 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Guadalajara Chivas Menos 2.5 | 1.25 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (51 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.55 | 63 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | Hándicap Guadalajara Chivas +1 | 1.45 | 67 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 7.0 | 1.29 | 83 % | 74 % | Favorito gana en partido trabado (78 %) | Partido abierto (ambos marcan y 3+ goles) (74 %) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Tarjetas | Tarjetas Menos 6.5 | 1.33 | 72 % | 74 % | Favorito golpea temprano y gana (83 %) | Expulsión antes del 70′ (35 %) | Alta probabilidad |
| Remates | Remates Cruz Azul Menos 15.5 | 1.25 | 75 % | 69 % | Favorito gana en partido trabado (85 %) | Partido abierto (ambos marcan y 3+ goles) (69 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco Más 7.5 | 1.28 | 75 % | 58 % | Partido abierto (ambos marcan y 3+ goles) (90 %) | Favorito gana en partido trabado (58 %) | Alta probabilidad |
| Jugadores | Agustín Palavecino anota o asiste | 2.92 | 32 % | 22 % | Sorpresa: gana el no favorito (49 %) | Favorito golpea temprano y gana (0 %) | Cara |
| Quién saca más | Más corners: Cruz Azul | 3.10 | 36 % | 30 % | Favorito golpea temprano y gana (46 %) | Sorpresa: gana el no favorito (30 %) | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 7.0 | 1.29 | 83 % | 80 % | 83 % | +0 pts | +7 % | 74 % | +0.9 | 1.25 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners 1.er tiempo Más 3.0 | 1.27 | 82 % | 82 % | 82 % | +0 pts | +5 % | 70 % | +0.8 | 1.25 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 14 % |
| Córners Más 8.0 | 1.29 | 80 % | 79 % | 80 % | +0 pts | +3 % | 72 % | +0.8 | 1.29 | Expulsión antes del 70′ | Alta probabilidad · asiática: devuelve 9 % |
| Goles Guadalajara Chivas Menos 2.5 | 1.25 | 78 % | 78 % | 78 % | +0 pts | -3 % | 78 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Cruz Azul Más 0.5 | 1.27 | 77 % | 76 % | 77 % | +0 pts | -3 % | 76 % | +0.8 | 1.35 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Menos 6.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -2 % | 75 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 13.0 | 1.34 | 76 % | 76 % | 76 % | +0 pts | +2 % | 68 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Remates Cruz Azul Menos 15.5 | 1.25 | 75 % | 78 % | 75 % | +0 pts | -6 % | 69 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Más 7.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -4 % | 58 % | +0.7 | 1.37 | Favorito gana en partido trabado | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.31 | 75 % | 74 % | 75 % | +0 pts | -2 % | 75 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| No hay empate | 1.25 | 75 % | 76 % | 75 % | +0 pts | -6 % | 75 % | — | 1.38 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners Más 8.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -4 % | 73 % | +0.7 | 1.39 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.32 | 74 % | 73 % | 74 % | +0 pts | -2 % | 74 % | +0.8 | 1.39 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Remates Menos 32.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 64 % | +0.5 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Más 3.5 | 1.27 | 74 % | 76 % | 74 % | +0 pts | -6 % | 72 % | +0.6 | 1.40 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Remates Guadalajara Chivas Menos 18.5 | 1.28 | 73 % | 76 % | 73 % | +0 pts | -7 % | 67 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas Menos 6.5 | 1.33 | 72 % | 72 % | 72 % | +0 pts | -4 % | 74 % | +0.5 | 1.42 | Expulsión antes del 70′ | Alta probabilidad |
| Tarjetas Más 3.5 | 1.34 | 72 % | 72 % | 72 % | +0 pts | -3 % | 67 % | +0.7 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad |
| Tiros al arco Cruz Azul Menos 5.5 | 1.33 | 72 % | 73 % | 72 % | +0 pts | -4 % | 56 % | +0.5 | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Remates Más 25.5 | 1.34 | 72 % | 72 % | 72 % | +0 pts | -4 % | 62 % | +0.6 | 1.43 | Favorito gana en partido trabado | Alta probabilidad |
| Tiros al arco Menos 11.5 | 1.33 | 72 % | 73 % | 72 % | +0 pts | -4 % | 57 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates Cruz Azul Más 10.5 | 1.31 | 72 % | 74 % | 72 % | +0 pts | -6 % | 65 % | +0.6 | 1.43 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Luis Gabriel Rey remates 1+ | 1.25 | 71 % | 71 % | 71 % | +0 pts | -11 % | 70 % | — | 1.45 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Córners Menos 12.5 | 1.34 | 71 % | 72 % | 71 % | +0 pts | -5 % | 69 % | +0.5 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Guadalajara Chivas Menos 6.5 | 1.36 | 70 % | 71 % | 70 % | +0 pts | -5 % | 55 % | +0.4 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Erik Lira anota o asiste | 8.75 | 15 % | 10 % | 15 % | +0 pts | +28 % | 9 % | — | 7.95 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Willer Ditta anota o asiste | 9.75 | 13 % | 9 % | 13 % | +0 pts | +22 % | 8 % | — | 9.52 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Jesús Orozco anota o asiste | 7.40 | 16 % | 12 % | 16 % | +0 pts | +20 % | 10 % | — | 7.04 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Fernando Gonzalez anota o asiste | 6.90 | 17 % | 13 % | 17 % | +0 pts | +19 % | 9 % | — | 6.53 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Córners Cruz Azul Más 7.5 | 6.80 | 17 % | 14 % | 17 % | +0 pts | +18 % | 14 % | -0.8 | 6.54 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Cruz Azul Más 6.5 | 4.40 | 26 % | 21 % | 26 % | +0 pts | +15 % | 22 % | -0.4 | 4.15 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 5.0 | 2.20 | 52 % | 50 % | 52 % | +0 pts | +15 % | 44 % | +0.1 | 2.00 | Favorito golpea temprano y gana | Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 4.0 | 3.50 | 32 % | 31 % | 32 % | +0 pts | +14 % | 26 % | -0.4 | 3.28 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 6.0 | 1.60 | 70 % | 67 % | 70 % | +0 pts | +12 % | 61 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 14 % |
| Más corners: Cruz Azul | 3.10 | 36 % | 27 % | 36 % | +0 pts | +11 % | 30 % | — | 2.95 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Cruz Azul Más 5.5 | 2.85 | 38 % | 33 % | 38 % | +0 pts | +9 % | 34 % | -0.0 | 2.75 | Expulsión antes del 70′ | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 7.0 | 1.29 | 83 % | 80 % | 83 % | +0 pts | +7 % | 74 % | +0.9 | 1.25 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners 1.er tiempo Más 4.0 | 1.62 | 66 % | 67 % | 66 % | +0 pts | +6 % | 53 % | +0.4 | 1.57 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 3.0 | 1.27 | 82 % | 82 % | 82 % | +0 pts | +5 % | 70 % | +0.8 | 1.25 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 14 % |
| Córners Más 10.0 | 1.82 | 58 % | 58 % | 58 % | +0 pts | +5 % | 51 % | +0.2 | 1.80 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Menos 11.0 | 1.91 | 55 % | 55 % | 55 % | +0 pts | +4 % | 46 % | +0.1 | 1.90 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners Más 9.0 | 1.50 | 70 % | 69 % | 70 % | +0 pts | +4 % | 62 % | +0.5 | 1.48 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 12.0 | 1.57 | 66 % | 66 % | 66 % | +0 pts | +4 % | 58 % | +0.3 | 1.55 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Erik Lira anota o asiste 0.9 % de la banca; Willer Ditta anota o asiste 0.6 % de la banca; Jesús Orozco anota o asiste 0.8 % de la banca; Fernando Gonzalez anota o asiste 0.8 % de la banca; Córners Cruz Azul Más 7.5 0.8 % de la banca; Córners Cruz Azul Más 6.5 1.1 % de la banca; Córners 1.er tiempo Menos 5.0 3.0 % de la banca; Córners 1.er tiempo Menos 4.0 1.4 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #16 | liga con Ambos Sí ≥55 %, Más 2.5 ≤1,80 y Ambos Sí ≤1,75 | Ambos marcan: Sí | 27602 partidos: Ambos Sí 56.0 % contra 56.5 % que ya da el precio (-0.5 pts ± 0.6) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles Cruz Azul Menos 3.5 + Guadalajara Chivas o empate + Tiros al arco Guadalajara Chivas Más 2.5 | 62 % | 63 % | 58 % | 1.60 | 1.65 | 1.09 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 0 % |
| Córners 1.er tiempo Menos 8.5 + Goles Cruz Azul Menos 3.5 + Guadalajara Chivas o empate | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.04 | 6 % | Favorito gana en partido trabado | 0 % |
| Córners 1.er tiempo Menos 8.5 + Tiros al arco Guadalajara Chivas Más 2.5 + Remates Más 25.5 | 62 % | 62 % | 58 % | 1.61 | 1.66 | 1.04 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 51 % |
| Tiros al arco Cruz Azul Más 1.5 + Ambos marcan: Sí | 61 % | 62 % | 56 % | 1.64 | 1.69 | 1.05 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 58 % |
| Tiros al arco Más 5.5 + Ambos marcan: Sí | 61 % | 61 % | 56 % | 1.65 | 1.70 | 1.05 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 57 % |
| Ambos 1+ tarjetas: Sí + Hándicap Cruz Azul +3 + Goles 2.º tiempo Menos 2.5 | 62 % | 64 % | 58 % | 1.62 | 1.67 | 1.03 | 6 % | Empate | 46 % |
| Ambos 1+ tarjetas: Sí + Tiros al arco Más 5.5 + Remates Más 25.5 | 60 % | 61 % | 56 % | 1.66 | 1.71 | 1.05 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 49 % |
| Córners Cruz Azul Más 3.5 + Hándicap Cruz Azul +3 + Goles Guadalajara Chivas Menos 3.5 | 61 % | 65 % | 56 % | 1.64 | 1.69 | 1.04 | 10 % | Empate | 58 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.