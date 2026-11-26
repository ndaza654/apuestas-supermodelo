# CF Pachuca - Guadalajara Chivas
México Liga MX · 2026-11-26 20:00

**Tipo de partido:** Parejo · medio · caliente · **Favorito:** Guadalajara Chivas · primer gol: local 43 %, visitante 49 %, nadie 8 % · gol del favorito antes del 35′: 30 %

**Base de la liga:** México Liga MX · 2.83 goles/partido, Más 2.5 55 %, ambos marcan 57 % (740 partidos ago-2022/nov-2026)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso, Empate / doble oportunidad / HT-FT X, Tarjetas y faltas (Más). Poco favorecidos: Hándicap y victoria.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | parejo y con mucho en juego: se cuidan |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Tarjetas y faltas (Más) | ✅ favorece | árbitro sin dato; los dos se juegan algo importante; parejo: más duelos y más faltas |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Sorpresa: gana el no favorito | 29 % |
| Partido abierto (ambos marcan y 3+ goles) | 22 % |
| Empate | 19 % |
| Expulsión antes del 70′ | 11 % |
| Favorito gana en partido trabado | 10 % |
| Favorito golpea temprano y gana | 9 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.18 | 13.2 | 4.4 | 5.3 | 12.1 | 2.6 |
| visitante | 1.33 | 13.2 | 4.8 | 5.3 | 12.1 | 2.5 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.5 (2.6) · 1–5 | 1.2 (1.2) · 0–3 | 1.3 (1.4) · 0–3 | 1.1 (1.1) · 0–3 | 1.4 (1.5) · 0–3 |
| Córners | 10.5 (10.6) · 6–15 | 5.3 · 2–9 | 5.3 · 2–9 | 4.7 (5.1) · 2–8 | 5.8 (5.6) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 5.0 (4.8) · 2–8 | 2.6 (2.5) · 1–5 | 2.5 (2.4) · 1–4 | 1.7 (1.7) · 0–3 | 3.4 · 1–6 |
| Remates | 26.4 (26.3) · 19–34 | 13.2 (13.2) · 8–19 | 13.2 (13.2) · 8–19 | 11.7 · 7–16 | 14.7 · 10–20 |
| Tiros al arco | 9.2 (9.2) · 5–13 | 4.4 (4.4) · 2–7 | 4.8 (4.8) · 2–8 | 4.1 · 2–7 | 5.1 · 2–8 |
| Faltas | 24.3 · 18–31 | 12.1 · 8–17 | 12.2 · 8–17 | 10.9 · 7–15 | 13.4 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 39.8 · 29–52 | 19.9 · 12–28 | 19.9 · 12–28 | 17.8 · 11–25 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.5 · 1–6 | 3.2 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Más 0.5 | 1.26 | 76 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (96 %) | Favorito golpea temprano y gana (49 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: No | 2.00 | 48 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Justa |
| Resultado y hándicap | No hay empate | 1.31 | 72 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 7.0 | 1.26 | 84 % | 75 % | Favorito gana en partido trabado (79 %) | Partido abierto (ambos marcan y 3+ goles) (75 %) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Tarjetas | Tarjetas 1.er tiempo Menos 2.5 | 1.32 | 75 % | 79 % | Partido abierto (ambos marcan y 3+ goles) (79 %) | Expulsión antes del 70′ (39 %) | Alta probabilidad |
| Remates | Remates Más 22.5 | 1.26 | 76 % | 69 % | Partido abierto (ambos marcan y 3+ goles) (86 %) | Favorito gana en partido trabado (69 %) | Alta probabilidad |
| Tiros al arco | Tiros al arco CF Pachuca Menos 5.5 | 1.34 | 72 % | 58 % | Favorito gana en partido trabado (89 %) | Sorpresa: gana el no favorito (58 %) | Alta probabilidad |
| Jugadores | Javier Nicolas Vallejo anota o asiste | 3.25 | 29 % | 19 % | Sorpresa: gana el no favorito (47 %) | Favorito golpea temprano y gana (0 %) | Cara |
| Quién saca más | Más tarjetas: empate | 4.00 | 24 % | 25 % | Favorito golpea temprano y gana (27 %) | Expulsión antes del 70′ (11 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 7.0 | 1.26 | 84 % | 81 % | 84 % | +0 pts | +6 % | 75 % | +1.0 | 1.22 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners 1.er tiempo Más 3.0 | 1.30 | 80 % | 81 % | 81 % | -1 pts | +4 % | 66 % | +0.8 | 1.28 | Empate | Alta probabilidad · Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 6.5 | 1.26 | 79 % | 77 % | 78 % | +0 pts | -1 % | 76 % | +0.8 | 1.31 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 13.0 | 1.30 | 78 % | 78 % | 78 % | +0 pts | +2 % | 70 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners Más 8.0 | 1.33 | 78 % | 77 % | 78 % | +0 pts | +4 % | 69 % | +0.7 | 1.32 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles 2.º tiempo Más 0.5 | 1.26 | 76 % | 77 % | 77 % | -1 pts | -5 % | 76 % | +0.8 | 1.36 | Favorito golpea temprano y gana | Alta probabilidad |
| Remates Más 22.5 | 1.26 | 76 % | 77 % | 76 % | -0 pts | -5 % | 69 % | +0.7 | 1.36 | Favorito gana en partido trabado | Alta probabilidad |
| Goles Menos 3.5 | 1.32 | 76 % | 74 % | 74 % | +2 pts | -0 % | 76 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Tarjetas CF Pachuca Menos 3.5 | 1.26 | 75 % | 77 % | 77 % | -2 pts | -6 % | 77 % | +0.6 | 1.37 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas Menos 6.5 | 1.26 | 75 % | 77 % | 77 % | -2 pts | -6 % | 77 % | +0.6 | 1.38 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas 1.er tiempo Menos 2.5 | 1.32 | 75 % | 73 % | 75 % | -1 pts | -2 % | 79 % | +0.6 | 1.38 | Expulsión antes del 70′ | Alta probabilidad |
| Goles Guadalajara Chivas Más 0.5 | 1.29 | 74 % | 75 % | 76 % | -1 pts | -4 % | 74 % | +0.7 | 1.39 | Sorpresa: gana el no favorito | Alta probabilidad |
| Remates CF Pachuca Más 10.5 | 1.27 | 74 % | 76 % | 73 % | +1 pts | -6 % | 72 % | +0.6 | 1.39 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Remates Guadalajara Chivas Menos 15.5 | 1.29 | 74 % | 75 % | 73 % | +1 pts | -5 % | 66 % | +0.5 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates Guadalajara Chivas Más 10.5 | 1.27 | 74 % | 76 % | 74 % | -1 pts | -7 % | 67 % | +0.6 | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Córners Menos 12.5 | 1.30 | 74 % | 74 % | 73 % | +0 pts | -4 % | 71 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Guadalajara Chivas Más 3.5 | 1.25 | 73 % | 75 % | 74 % | -0 pts | -8 % | 72 % | +0.7 | 1.40 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Remates Menos 29.5 | 1.30 | 73 % | 74 % | 73 % | +0 pts | -5 % | 61 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates CF Pachuca Menos 15.5 | 1.29 | 73 % | 75 % | 74 % | -1 pts | -6 % | 67 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas CF Pachuca Más 1.5 | 1.37 | 73 % | 70 % | 71 % | +2 pts | +0 % | 71 % | +0.7 | 1.41 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Goles Menos 3.25 | 1.38 | 73 % | 71 % | 71 % | +2 pts | +0 % | 73 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |
| Córners CF Pachuca Más 3.5 | 1.28 | 73 % | 73 % | 73 % | -0 pts | -7 % | 68 % | +0.7 | 1.42 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Menos 6.0 | 1.55 | 72 % | 69 % | 72 % | +1 pts | +12 % | 62 % | +0.6 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 13 % |
| No hay empate | 1.31 | 72 % | 72 % | 71 % | +1 pts | -6 % | 72 % | — | 1.43 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners Más 8.5 | 1.33 | 72 % | 73 % | 71 % | +0 pts | -4 % | 71 % | +0.6 | 1.43 | Expulsión antes del 70′ | Alta probabilidad |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrés Micolta anota o asiste | 13.00 | 10 % | 7 % | 11 % | -0 pts | +31 % | 6 % | — | 12.37 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Pedro Martinez anota o asiste | 13.00 | 10 % | 7 % | 11 % | -1 pts | +31 % | 6 % | — | 12.40 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Carlos Hernandez anota o asiste | 12.00 | 11 % | 7 % | 11 % | -1 pts | +27 % | 5 % | — | 11.70 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Pedro Budib anota o asiste | 9.50 | 13 % | 9 % | 13 % | -0 pts | +20 % | 8 % | — | 9.43 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Sergio Barreto anota o asiste | 7.90 | 15 % | 11 % | 16 % | -1 pts | +18 % | 9 % | — | 7.71 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Rene Lopez anota o asiste | 8.75 | 13 % | 10 % | 14 % | -1 pts | +18 % | 8 % | — | 8.74 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 4.0 | 3.30 | 36 % | 33 % | 35 % | +1 pts | +18 % | 28 % | -0.3 | 2.97 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Fernando Gonzalez anota o asiste | 7.70 | 15 % | 11 % | 16 % | -1 pts | +17 % | 7 % | — | 7.56 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 5.0 | 2.10 | 55 % | 52 % | 54 % | +1 pts | +16 % | 45 % | +0.1 | 1.88 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % |
| Jose Castillo anota o asiste | 6.60 | 17 % | 13 % | 18 % | -0 pts | +14 % | 8 % | — | 6.54 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Córners 1.er tiempo Menos 6.0 | 1.55 | 72 % | 69 % | 72 % | +1 pts | +12 % | 62 % | +0.6 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners 1.er tiempo Menos 7.0 | 1.26 | 84 % | 81 % | 84 % | +0 pts | +6 % | 75 % | +1.0 | 1.22 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners Menos 10.0 | 2.35 | 45 % | 45 % | 45 % | -0 pts | +6 % | 37 % | -0.2 | 2.32 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners Menos 11.0 | 1.82 | 58 % | 58 % | 58 % | +0 pts | +5 % | 48 % | +0.1 | 1.79 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners Más 10.0 | 1.93 | 54 % | 55 % | 54 % | +0 pts | +5 % | 47 % | +0.2 | 1.91 | Expulsión antes del 70′ | Valor · asiática: devuelve 11 % |
| Córners 1.er tiempo Más 4.0 | 1.67 | 63 % | 65 % | 64 % | -1 pts | +5 % | 51 % | +0.3 | 1.65 | Expulsión antes del 70′ | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 3.0 | 1.30 | 80 % | 81 % | 81 % | -1 pts | +4 % | 66 % | +0.8 | 1.28 | Empate | Alta probabilidad · Valor · asiática: devuelve 16 % |
| Córners Menos 12.0 | 1.50 | 69 % | 69 % | 69 % | +0 pts | +4 % | 60 % | +0.4 | 1.49 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners Más 9.0 | 1.55 | 67 % | 67 % | 67 % | +0 pts | +4 % | 58 % | +0.4 | 1.54 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Más 8.0 | 1.33 | 78 % | 77 % | 78 % | +0 pts | +4 % | 69 % | +0.7 | 1.32 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Andrés Micolta anota o asiste 0.7 % de la banca; Pedro Martinez anota o asiste 0.6 % de la banca; Carlos Hernandez anota o asiste 0.6 % de la banca; Pedro Budib anota o asiste 0.6 % de la banca; Sergio Barreto anota o asiste 0.7 % de la banca; Rene Lopez anota o asiste 0.6 % de la banca; Córners 1.er tiempo Menos 4.0 1.9 % de la banca; Fernando Gonzalez anota o asiste 0.6 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #420 | empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas | Empate | 48947 partidos: acierto 29.9 % contra 29.2 % del precio; ROI -5.0 % ± 1.3 (con la mejor cuota -0.1 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 2+ tarjetas: Sí + Tarjetas CF Pachuca Más 1.5 | 55 % | 57 % | 50 % | 1.83 | 1.88 | 1.36 | 10 % | Expulsión antes del 70′ | 52 % |
| Ambos 2+ tarjetas: Sí + Tarjetas Guadalajara Chivas Más 1.5 | 54 % | 57 % | 49 % | 1.84 | 1.89 | 1.4 | 10 % | Expulsión antes del 70′ | 51 % |
| Hándicap Guadalajara Chivas +2 + Goles CF Pachuca Menos 2.5 + Tarjetas 1.er tiempo Menos 2.5 | 62 % | 64 % | 58 % | 1.61 | 1.66 | 1.07 | 8 % | Favorito gana en partido trabado | 44 % |
| Tarjetas CF Pachuca Más 1.5 + Hándicap Guadalajara Chivas +2 + Goles CF Pachuca Menos 2.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.08 | 8 % | Expulsión antes del 70′ | 40 % |
| Tarjetas 1.er tiempo Menos 2.5 + Goles 1.er tiempo Menos 2.5 + Tiros al arco Menos 13.5 | 62 % | 63 % | 58 % | 1.61 | 1.65 | 1.02 | 7 % | Empate | 50 % |
| Tarjetas Más 2.5 + Córners 2.º tiempo Más 3.5 + Goles 1.er tiempo Menos 2.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.01 | 7 % | Empate | 52 % |
| Goles Guadalajara Chivas Menos 3.5 + Tiros al arco Guadalajara Chivas Menos 8.5 + CF Pachuca o empate | 58 % | 58 % | 53 % | 1.72 | 1.78 | 1.08 | 6 % | Empate | 25 % |
| Tarjetas Guadalajara Chivas Más 1.5 + Goles Guadalajara Chivas Menos 3.5 + Tiros al arco Menos 13.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.01 | 7 % | Expulsión antes del 70′ | 50 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.