# Cobresal - Audax Italiano
Chile Liga de Primera · 2026-11-20 16:00

**Tipo de partido:** Parejo · medio · normal · **Favorito:** Cobresal · primer gol: local 49 %, visitante 45 %, nadie 6 % · gol del favorito antes del 35′: 32 %

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero 1.er tiempo (Menos) y empate al descanso, Ambos marcan, Empate / doble oportunidad / HT-FT X. Poco favorecidos: Hándicap y victoria.

| Mercado | Encaje | Por qué |
|---|---|---|
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Goles del partido | ➖ neutro | ni muchos ni pocos goles esperados |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; parejo: más duelos y más faltas |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Sorpresa: gana el no favorito | 29 % |
| Partido abierto (ambos marcan y 3+ goles) | 27 % |
| Empate | 17 % |
| Expulsión antes del 70′ | 11 % |
| Favorito golpea temprano y gana | 8 % |
| Favorito gana en partido trabado | 8 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.54 | 12.5 | 4.3 | 5.3 | 11.8 | 2.5 |
| visitante | 1.34 | 12.5 | 4.3 | 5.3 | 11.8 | 2.7 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.9 (2.9) · 1–5 | 1.5 (1.5) · 0–3 | 1.4 (1.4) · 0–3 | 1.3 (1.2) · 0–3 | 1.6 (1.6) · 0–3 |
| Córners | 10.7 (10.7) · 6–15 | 5.4 · 2–9 | 5.3 · 2–9 | 4.8 (5.1) · 2–8 | 5.9 (5.7) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 5.1 (5.1) · 2–8 | 2.5 (2.5) · 1–4 | 2.7 (2.7) · 1–5 | 1.7 (1.8) · 0–4 | 3.4 · 1–6 |
| Remates | 25.0 · 18–32 | 12.5 · 7–18 | 12.5 · 7–18 | 11.2 · 7–16 | 13.8 · 9–19 |
| Tiros al arco | 8.6 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.9 · 1–6 | 4.8 · 2–8 |
| Faltas | 23.6 · 17–30 | 11.8 · 7–16 | 11.8 · 7–16 | 10.6 · 6–15 | 13.0 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.2 · 3–11 | 9.0 · 5–14 |
| Saques de banda | 39.9 · 29–52 | 20.0 · 12–28 | 19.9 · 12–28 | 17.8 · 11–25 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.0 · 1–6 | 2.8 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Menos 2.5 | 1.26 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (58 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.60 | 60 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | Hándicap Audax Italiano +0.75 | 1.47 | 67 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 7.0 | 1.28 | 83 % | 75 % | Favorito gana en partido trabado (79 %) | Partido abierto (ambos marcan y 3+ goles) (75 %) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Tarjetas | Tarjetas Más 3.5 | 1.34 | 72 % | 68 % | Expulsión antes del 70′ (97 %) | Favorito golpea temprano y gana (62 %) | Alta probabilidad |
| Quién saca más | Más corners: Audax Italiano | 2.47 | 40 % | 33 % | Favorito golpea temprano y gana (51 %) | Sorpresa: gana el no favorito (33 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 7.0 | 1.28 | 83 % | 81 % | 83 % | +0 pts | +7 % | 75 % | +1.0 | 1.24 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners 1.er tiempo Más 3.0 | 1.29 | 82 % | 82 % | 82 % | +0 pts | +5 % | 69 % | +0.8 | 1.26 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners Más 8.0 | 1.31 | 79 % | 78 % | 79 % | +0 pts | +3 % | 71 % | +0.8 | 1.30 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles 2.º tiempo Menos 2.5 | 1.26 | 78 % | 77 % | 78 % | +0 pts | -1 % | 78 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Más 1.5 | 1.25 | 78 % | 78 % | 78 % | +0 pts | -2 % | 78 % | +0.8 | 1.32 | Favorito gana en partido trabado | Alta probabilidad |
| Córners 1.er tiempo Menos 6.5 | 1.28 | 77 % | 76 % | 77 % | +0 pts | -1 % | 76 % | +0.8 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 13.0 | 1.32 | 77 % | 77 % | 77 % | +0 pts | +2 % | 67 % | +0.6 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Goles Audax Italiano Más 0.5 | 1.30 | 75 % | 74 % | 75 % | +0 pts | -2 % | 75 % | +0.8 | 1.37 | Favorito golpea temprano y gana | Alta probabilidad |
| No hay empate | 1.28 | 73 % | 74 % | 73 % | +0 pts | -6 % | 73 % | — | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners Más 8.5 | 1.31 | 73 % | 74 % | 73 % | +0 pts | -4 % | 72 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.5 | 1.29 | 72 % | 75 % | 72 % | +0 pts | -7 % | 72 % | +0.6 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas Más 3.5 | 1.34 | 72 % | 72 % | 72 % | +0 pts | -3 % | 68 % | +0.6 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 12.5 | 1.32 | 72 % | 73 % | 72 % | +0 pts | -5 % | 68 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Más 2.0 | 1.36 | 72 % | 72 % | 72 % | +0 pts | -2 % | 72 % | +0.5 | 1.43 | Empate | Alta probabilidad · asiática: devuelve 24 % |
| Goles 1.er tiempo Más 0.5 | 1.36 | 72 % | 71 % | 72 % | +0 pts | -3 % | 72 % | +0.7 | 1.44 | Favorito gana en partido trabado | Alta probabilidad |
| Córners Audax Italiano Más 3.5 | 1.34 | 71 % | 70 % | 71 % | +0 pts | -4 % | 68 % | +0.7 | 1.44 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners 1.er tiempo Menos 6.0 | 1.57 | 71 % | 68 % | 71 % | +0 pts | +11 % | 60 % | +0.5 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 14 % |
| Córners Más 9.0 | 1.52 | 68 % | 68 % | 68 % | +0 pts | +4 % | 61 % | +0.5 | 1.51 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners 2.º tiempo Más 4.5 | 1.45 | 68 % | 66 % | 68 % | +0 pts | -2 % | 67 % | +0.6 | 1.52 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Menos 12.0 | 1.53 | 68 % | 68 % | 68 % | +0 pts | +3 % | 58 % | +0.4 | 1.52 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles Menos 3.5 | 1.44 | 68 % | 67 % | 68 % | +0 pts | -3 % | 68 % | +0.4 | 1.52 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Hándicap Audax Italiano +0.75 | 1.47 | 67 % | 66 % | 67 % | +0 pts | -1 % | 67 % | — | 1.53 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |
| Hándicap Cobresal +0.5 | 1.45 | 67 % | 67 % | 67 % | +0 pts | -3 % | 67 % | — | 1.54 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Cobresal o empate | 1.44 | 67 % | 67 % | 67 % | +0 pts | -3 % | 67 % | — | 1.54 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Hándicap Cobresal +1 | 1.44 | 67 % | 67 % | 67 % | +0 pts | -3 % | 67 % | — | 1.54 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 3.40 | 34 % | 32 % | 34 % | +0 pts | +15 % | 27 % | -0.4 | 3.15 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 5.0 | 2.15 | 53 % | 51 % | 53 % | +0 pts | +14 % | 44 % | +0.1 | 1.95 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Menos 6.0 | 1.57 | 71 % | 68 % | 71 % | +0 pts | +11 % | 60 % | +0.5 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 14 % |
| Córners 1.er tiempo Menos 7.0 | 1.28 | 83 % | 81 % | 83 % | +0 pts | +7 % | 75 % | +1.0 | 1.24 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 9 % |
| Córners 1.er tiempo Más 4.0 | 1.65 | 64 % | 66 % | 64 % | +0 pts | +6 % | 52 % | +0.4 | 1.60 | Favorito gana en partido trabado | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 3.0 | 1.29 | 82 % | 82 % | 82 % | +0 pts | +5 % | 69 % | +0.8 | 1.26 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners Más 10.0 | 1.87 | 56 % | 56 % | 56 % | +0 pts | +5 % | 50 % | +0.2 | 1.85 | Expulsión antes del 70′ | Valor · asiática: devuelve 11 % |
| Córners Menos 11.0 | 1.87 | 56 % | 56 % | 56 % | +0 pts | +5 % | 47 % | +0.1 | 1.85 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % |
| Córners Más 9.0 | 1.52 | 68 % | 68 % | 68 % | +0 pts | +4 % | 61 % | +0.5 | 1.51 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 12.0 | 1.53 | 68 % | 68 % | 68 % | +0 pts | +3 % | 58 % | +0.4 | 1.52 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Más 8.0 | 1.31 | 79 % | 78 % | 79 % | +0 pts | +3 % | 71 % | +0.8 | 1.30 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 1.5 % de la banca; Córners 1.er tiempo Menos 5.0 3.1 % de la banca; Córners 1.er tiempo Menos 6.0 4.9 % de la banca; Córners 1.er tiempo Menos 7.0 5.9 % de la banca; Córners 1.er tiempo Más 4.0 2.5 % de la banca; Córners 1.er tiempo Más 3.0 4.5 % de la banca; Córners Más 10.0 1.4 % de la banca; Córners Menos 11.0 1.3 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Tarjetas Más 3.5 + Córners Cobresal Más 2.5 | 60 % | 61 % | 56 % | 1.66 | 1.71 | 1.11 | 12 % | Expulsión antes del 70′ | 58 % |
| Goles Audax Italiano Menos 3.5 + Córners 1.er tiempo Menos 8.5 + Cobresal o empate | 62 % | 63 % | 57 % | 1.61 | 1.66 | 1.04 | 6 % | Favorito gana en partido trabado | 0 % |
| Goles Audax Italiano Menos 3.5 + Córners 2.º tiempo Más 2.5 + Cobresal o empate | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.04 | 6 % | Favorito gana en partido trabado | 0 % |
| Ambos 1+ tarjetas: Sí + Córners 2.º tiempo Más 2.5 + Goles 2.º tiempo Menos 2.5 | 62 % | 64 % | 58 % | 1.60 | 1.65 | 1.0 | 6 % | Empate | 46 % |
| Tarjetas Más 3.5 + Córners Cobresal Más 2.5 | 62 % | 62 % | 58 % | 1.60 | 1.65 | 1.0 | 10 % | Expulsión antes del 70′ | 60 % |
| Hándicap Audax Italiano +3 + Ambos marcan: Sí | 57 % | 58 % | 52 % | 1.75 | 1.80 | 1.02 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 53 % |
| Hándicap Audax Italiano +3 + Goles Cobresal Menos 3.5 + Ambos marcan: Sí | 54 % | 56 % | 50 % | 1.84 | 1.89 | 1.04 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 52 % |
| Goles 1.er tiempo Menos 3.5 + Córners Audax Italiano Más 4.5 | 53 % | 55 % | 49 % | 1.87 | 1.93 | 1.0 | 8 % | Favorito golpea temprano y gana | 49 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.