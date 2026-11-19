# SL Benfica (F) - AS Roma (F)
UEFA Clubs Champions League (F) · 2026-11-19 15:00

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** SL Benfica (F) · primer gol: local 53 %, visitante 43 %, nadie 4 % · gol del favorito antes del 35′: 35 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Resultado / hándicap | ➖ neutro | SL Benfica (F) favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; los dos se juegan algo importante |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 34 % |
| Sorpresa: gana el no favorito | 28 % |
| Empate | 12 % |
| Favorito golpea temprano y gana | 9 % |
| Favorito gana en partido trabado | 9 % |
| Expulsión antes del 70′ | 8 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.76 | 12.5 | 4.3 | 4.7 | 12.1 | 1.8 |
| visitante | 1.43 | 12.5 | 4.3 | 4.7 | 12.1 | 1.8 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.2 (3.3) · 1–6 | 1.8 (1.8) · 0–3 | 1.4 (1.5) · 0–3 | 1.4 (1.4) · 0–3 | 1.8 (1.8) · 0–4 |
| Córners | 9.4 (9.4) · 5–14 | 4.7 · 2–8 | 4.7 · 2–8 | 4.2 (4.5) · 2–7 | 5.3 (5.1) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 3.6 (3.4) · 1–6 | 1.8 (1.7) · 0–4 | 1.8 (1.7) · 0–4 | 1.2 (1.1) · 0–3 | 2.4 · 0–5 |
| Remates | 25.2 · 18–33 | 12.6 · 8–18 | 12.6 · 7–18 | 11.1 · 7–16 | 14.1 · 9–19 |
| Tiros al arco | 8.7 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.8 · 1–6 | 4.8 · 2–8 |
| Faltas | 24.3 · 18–31 | 12.1 · 8–17 | 12.1 · 8–17 | 10.9 · 7–15 | 13.4 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 15.9 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 39.9 · 29–52 | 20.0 · 12–28 | 20.0 · 12–28 | 17.8 · 12–24 | 22.1 · 15–30 |
| Atajadas del portero | — | 2.9 · 1–5 | 2.5 · 0–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.26 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (62 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.45 | 65 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Resultado y hándicap | No hay empate | 1.26 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad |
| Córners | Córners Más 7.0 | 1.34 | 78 % | 70 % | Partido abierto (ambos marcan y 3+ goles) (73 %) | Favorito golpea temprano y gana (65 %) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Tarjetas | Ambos 1+ tarjetas: Sí | 1.40 | 72 % | 70 % | Expulsión antes del 70′ (86 %) | Favorito golpea temprano y gana (66 %) | Alta probabilidad |
| Quién saca más | Más corners: AS Roma (F) | 2.87 | 36 % | 31 % | Favorito golpea temprano y gana (45 %) | Sorpresa: gana el no favorito (31 %) | Justa · ⚠ Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Más 7.0 | 1.34 | 78 % | 77 % | 78 % | +0 pts | +5 % | 70 % | +0.8 | 1.32 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles Menos 4.5 | 1.26 | 78 % | 77 % | 77 % | +1 pts | -2 % | 78 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles AS Roma (F) Más 0.5 | 1.25 | 78 % | 78 % | 78 % | -0 pts | -3 % | 78 % | +0.8 | 1.33 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| No hay empate | 1.26 | 77 % | 75 % | 75 % | +3 pts | -2 % | 78 % | — | 1.33 | Empate | Alta probabilidad |
| Hándicap AS Roma (F) +2 | 1.28 | 77 % | 76 % | 77 % | +0 pts | -2 % | 77 % | — | 1.34 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 11.5 | 1.25 | 76 % | 78 % | 76 % | -1 pts | -5 % | 73 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Más 0.5 | 1.27 | 75 % | 76 % | 76 % | -2 pts | -5 % | 75 % | +0.8 | 1.38 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners 2.º tiempo Más 3.5 | 1.33 | 75 % | 73 % | 74 % | +1 pts | -1 % | 75 % | +0.7 | 1.38 | Expulsión antes del 70′ | Alta probabilidad |
| Goles SL Benfica (F) Menos 2.5 | 1.32 | 74 % | 73 % | 73 % | +1 pts | -2 % | 74 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 1.er tiempo Menos 5.5 | 1.35 | 74 % | 71 % | 73 % | +1 pts | -0 % | 72 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.34 | 73 % | 72 % | 73 % | +0 pts | -2 % | 73 % | +0.5 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Ambos 1+ tarjetas: Sí | 1.40 | 72 % | 69 % | 69 % | +3 pts | +1 % | 70 % | — | 1.43 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.45 | 72 % | 72 % | 73 % | -1 pts | +4 % | 59 % | +0.6 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners Más 7.5 | 1.34 | 72 % | 72 % | 71 % | +1 pts | -4 % | 71 % | +0.6 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 11.0 | 1.44 | 71 % | 72 % | 72 % | -1 pts | +3 % | 62 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 10 % |
| Goles 1.er tiempo Más 0.75 | 1.36 | 70 % | 72 % | 72 % | -2 pts | -4 % | 70 % | +0.6 | 1.47 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| SL Benfica (F) o empate | 1.40 | 69 % | 70 % | 70 % | -1 pts | -4 % | 69 % | — | 1.50 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap SL Benfica (F) +1 | 1.40 | 69 % | 69 % | 70 % | -1 pts | -4 % | 69 % | — | 1.50 | Sorpresa: gana el no favorito | Alta probabilidad |
| Tarjetas 1.er tiempo Más 0.5 | 1.47 | 68 % | 65 % | 65 % | +3 pts | -0 % | 65 % | +0.6 | 1.52 | Empate | Alta probabilidad |
| Goles 1.er tiempo Menos 1.75 | 1.47 | 67 % | 66 % | 66 % | +2 pts | -1 % | 67 % | +0.3 | 1.53 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % |
| Ambos 2+ tarjetas: No | 1.38 | 66 % | 70 % | 70 % | -4 pts | -8 % | 65 % | — | 1.55 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 8.0 | 1.60 | 66 % | 66 % | 66 % | +1 pts | +6 % | 59 % | +0.4 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Menos 5.0 | 1.75 | 66 % | 62 % | 65 % | +1 pts | +15 % | 55 % | +0.4 | 1.56 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners Menos 10.5 | 1.44 | 66 % | 67 % | 66 % | -0 pts | -5 % | 63 % | +0.3 | 1.57 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Ambos marcan: Sí | 1.45 | 65 % | 66 % | 66 % | -1 pts | -6 % | 65 % | — | 1.59 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 | 2.15 | 47 % | 43 % | 42 % | +4 pts | +0 % | 43 % | +0.0 | 2.24 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.60 | 46 % | 43 % | 45 % | +1 pts | +19 % | 37 % | -0.1 | 2.29 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 20 % |
| Córners 1.er tiempo Menos 5.0 | 1.75 | 66 % | 62 % | 65 % | +1 pts | +15 % | 55 % | +0.4 | 1.56 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 15 % |
| Córners Más 9.0 | 2.02 | 53 % | 52 % | 52 % | +0 pts | +7 % | 47 % | +0.1 | 1.97 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.60 | 66 % | 66 % | 66 % | +1 pts | +6 % | 59 % | +0.4 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Más 10.0 | 2.67 | 39 % | 39 % | 39 % | +0 pts | +5 % | 35 % | -0.2 | 2.67 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.75 | 60 % | 60 % | 60 % | -0 pts | +5 % | 51 % | +0.2 | 1.73 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Más 7.0 | 1.34 | 78 % | 77 % | 78 % | +0 pts | +5 % | 70 % | +0.8 | 1.32 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Menos 9.0 | 2.25 | 46 % | 47 % | 47 % | -0 pts | +5 % | 38 % | -0.1 | 2.25 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 3.0 | 1.45 | 72 % | 72 % | 73 % | -1 pts | +4 % | 59 % | +0.6 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Más 4.0 | 2.00 | 52 % | 55 % | 53 % | -1 pts | +4 % | 41 % | +0.1 | 2.00 | Favorito gana en partido trabado | Valor · asiática: devuelve 20 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.9 % de la banca; Córners 1.er tiempo Menos 5.0 5.1 % de la banca; Córners Más 9.0 1.6 % de la banca; Córners Más 8.0 2.5 % de la banca; Córners Más 10.0 0.8 % de la banca; Córners Menos 10.0 1.6 % de la banca; Córners Más 7.0 3.4 % de la banca; Córners Menos 9.0 0.9 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles 2.º tiempo Más 0.5 + Ambos marcan: Sí | 61 % | 61 % | 56 % | 1.64 | 1.69 | 1.11 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 58 % |
| Hándicap AS Roma (F) +3 + Goles SL Benfica (F) Menos 3.5 + Córners Más 7.5 | 62 % | 62 % | 58 % | 1.62 | 1.67 | 1.06 | 7 % | Empate | 58 % |
| Hándicap AS Roma (F) +3 + Goles 2.º tiempo Más 0.5 + Ambos marcan: Sí | 57 % | 57 % | 52 % | 1.76 | 1.82 | 1.15 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 58 % |
| Ambos 1+ tarjetas: Sí + Tarjetas 1.er tiempo Más 0.5 | 56 % | 57 % | 52 % | 1.79 | 1.84 | 1.15 | 8 % | Expulsión antes del 70′ | 54 % |
| Ambos 1+ tarjetas: Sí + Tarjetas 1.er tiempo Más 0.5 + Goles Más 0.5 | 54 % | 55 % | 50 % | 1.86 | 1.91 | 1.14 | 10 % | Expulsión antes del 70′ | 41 % |
| Córners AS Roma (F) Más 3.5 + Goles Más 0.5 | 58 % | 62 % | 54 % | 1.71 | 1.76 | 1.0 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 46 % |
| Córners AS Roma (F) Más 3.5 + Goles AS Roma (F) Menos 3.5 | 57 % | 62 % | 53 % | 1.74 | 1.79 | 1.0 | 8 % | Favorito golpea temprano y gana | 48 % |
| Córners 2.º tiempo Más 4.5 + Goles 1.er tiempo Menos 3.5 | 55 % | 57 % | 50 % | 1.82 | 1.88 | 1.0 | 7 % | Empate | 54 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.