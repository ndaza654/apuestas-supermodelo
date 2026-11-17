# Dinamarca - Noruega
UEFA Liga de Naciones · 2026-11-17 14:45

**Tipo de partido:** Parejo · abierto · normal · **Favorito:** Noruega · primer gol: local 48 %, visitante 49 %, nadie 3 % · gol del favorito antes del 35′: 34 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

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
| Partido abierto (ambos marcan y 3+ goles) | 34 % |
| Sorpresa: gana el no favorito | 32 % |
| Empate | 12 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 6 % |
| Favorito gana en partido trabado | 6 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.68 | 15.4 | 5.2 | 5.1 | 11.5 | 2.2 |
| visitante | 1.77 | 14.3 | 5.0 | 5.3 | 12.6 | 2.2 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.5 (3.5) · 1–6 | 1.7 (1.7) · 0–3 | 1.8 (1.8) · 0–3 | 1.5 (1.5) · 0–3 | 1.9 (2.0) · 0–4 |
| Córners | 10.5 (10.3) · 6–15 | 5.2 (5.1) · 2–9 | 5.2 (5.3) · 2–9 | 4.7 (5.0) · 2–8 | 5.8 (5.5) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 4.5 (4.2) · 2–8 | 2.2 (2.1) · 0–4 | 2.3 (2.1) · 1–4 | 1.5 (1.4) · 0–3 | 3.0 · 1–5 |
| Remates | 29.7 (29.4) · 22–38 | 15.4 (15.4) · 10–22 | 14.3 (14.3) · 9–20 | 13.2 · 8–18 | 16.5 · 11–22 |
| Tiros al arco | 10.1 (10.1) · 6–14 | 5.1 (5.2) · 2–8 | 5.0 (5.0) · 2–8 | 4.5 (4.5) · 2–7 | 5.6 · 3–9 |
| Faltas | 24.2 (23.5) · 18–31 | 11.6 (11.3) · 7–16 | 12.6 (12.2) · 8–17 | 10.8 · 7–15 | 13.3 · 9–18 |
| Fueras de lugar | 3.6 (3.7) · 1–6 | 2.3 (2.4) · 0–5 | 1.3 (1.3) · 0–3 | 1.6 (2.0) · 0–3 | 2.0 · 0–4 |
| Saques de meta | 14.1 (14.2) · 8–20 | 6.2 (6.3) · 3–10 | 7.9 (7.9) · 4–13 | 6.3 (6.6) · 3–10 | 7.8 · 4–12 |
| Saques de banda | 32.2 (32.2) · 23–42 | 16.6 (16.6) · 10–24 | 15.6 (15.6) · 9–22 | 14.4 (17.0) · 9–20 | 17.9 · 12–25 |
| Atajadas del portero | — | 3.2 · 1–6 | 3.4 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Más 0.5 | 1.25 | 78 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Favorito gana en partido trabado (25 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: Sí | 1.38 | 70 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · ★ enfoque a favor |
| Resultado y hándicap | Hándicap Noruega +0.75 | 1.40 | 71 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad · asiática: devuelve 10 % · ★ enfoque a favor |
| Córners | Córners Menos 12.5 | 1.26 | 75 % | 73 % | Expulsión antes del 70′ (80 %) | Partido abierto (ambos marcan y 3+ goles) (73 %) | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas | Tarjetas Más 2.5 | 1.28 | 79 % | 76 % | Expulsión antes del 70′ (99 %) | Favorito golpea temprano y gana (75 %) | Alta probabilidad · Contexto a favor (+4 pts) · ★ enfoque a favor |
| Faltas | Faltas Más 23.5 | 1.93 | 55 % | 54 % | Expulsión antes del 70′ (59 %) | Empate (54 %) | Contexto a favor (+7 pts) · Valor |
| Remates | Remates Noruega Más 12.5 | 1.47 | 64 % | 63 % | Partido abierto (ambos marcan y 3+ goles) (73 %) | Expulsión antes del 70′ (55 %) | Cara |
| Tiros al arco | Tiros al arco Más 8.5 | 1.42 | 68 % | 69 % | Partido abierto (ambos marcan y 3+ goles) (83 %) | Empate (44 %) | Alta probabilidad |
| Fueras de lugar | Fueras de lugar Noruega Menos 1.5 | 1.52 | 63 % | 62 % | Favorito golpea temprano y gana (68 %) | Sorpresa: gana el no favorito (62 %) | Justa |
| Saques de meta | Saques de meta Dinamarca Menos 6.5 | 1.67 | 58 % | 52 % | Favorito golpea temprano y gana (66 %) | Sorpresa: gana el no favorito (52 %) | Justa |
| Saques de banda | Saques de banda 1.er tiempo Menos 16.5 | 1.93 | 60 % | 59 % | Favorito golpea temprano y gana (61 %) | Empate (59 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jugadores | Mads Hermansen atajadas 5+ | 4.05 | 23 % | 23 % | Favorito gana en partido trabado (28 %) | Favorito golpea temprano y gana (21 %) | Cara |
| Parejas de jugadores | Pierre Hojbjerg o Thelo Aasgaard (da una asistencia) | 3.40 | 28 % | 30 % | Partido abierto (ambos marcan y 3+ goles) (35 %) | Favorito gana en partido trabado (14 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 2.5 | 1.28 | 79 % | 76 % | 75 % | +4 pts | +2 % | 76 % | +0.8 | 1.30 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+4 pts) · ★ enfoque a favor |
| Goles 1.er tiempo Más 0.5 | 1.25 | 78 % | 78 % | 78 % | -1 pts | -3 % | 78 % | +0.8 | 1.33 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Tarjetas 1.er tiempo Más 0.5 | 1.32 | 76 % | 73 % | 73 % | +3 pts | +0 % | 74 % | +0.8 | 1.35 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Goles Dinamarca Menos 2.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -2 % | 76 % | +0.7 | 1.36 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Menos 12.5 | 1.26 | 75 % | 77 % | 75 % | -0 pts | -5 % | 73 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles Noruega Menos 2.5 | 1.33 | 74 % | 73 % | 73 % | +1 pts | -2 % | 74 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Dinamarca Menos 6.5 | 1.31 | 74 % | 74 % | 74 % | +0 pts | -3 % | 60 % | +0.6 | 1.39 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles 1.er tiempo Más 0.75 | 1.32 | 74 % | 74 % | 74 % | -1 pts | -3 % | 74 % | +0.6 | 1.40 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 16 % · ★ enfoque a favor |
| Córners Noruega Más 3.5 | 1.27 | 74 % | 76 % | 74 % | -1 pts | -6 % | 73 % | +0.6 | 1.40 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Córners Dinamarca Más 3.5 | 1.30 | 73 % | 74 % | 73 % | +0 pts | -5 % | 69 % | +0.6 | 1.41 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles Menos 4.5 | 1.36 | 73 % | 72 % | 72 % | +1 pts | -1 % | 73 % | +0.6 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Dinamarca Menos 6.5 | 1.29 | 72 % | 75 % | 73 % | -1 pts | -7 % | 68 % | +0.5 | 1.42 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Noruega Más 3.5 | 1.33 | 72 % | 73 % | 71 % | +1 pts | -4 % | 59 % | +0.6 | 1.42 | Empate | Alta probabilidad |
| Córners Noruega Menos 6.5 | 1.33 | 72 % | 73 % | 72 % | +1 pts | -4 % | 68 % | +0.5 | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Patrick Berg faltas cometidas 1+ | 1.27 | 71 % | 70 % | 70 % | +1 pts | -10 % | 71 % | — | 1.45 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Gustav Isaksen entradas 1+ | 1.25 | 71 % | 71 % | 71 % | -0 pts | -12 % | 69 % | — | 1.46 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Hándicap Noruega +0.75 | 1.40 | 71 % | 70 % | 71 % | -0 pts | -1 % | 70 % | — | 1.46 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 10 % · ★ enfoque a favor |
| Goles Menos 4.25 | 1.42 | 70 % | 69 % | 69 % | +1 pts | -0 % | 70 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Mads Bidstrup remates 1+ | 1.25 | 70 % | 71 % | 70 % | +0 pts | -12 % | 71 % | — | 1.47 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Mathias Jensen remates 1+ | 1.25 | 70 % | 71 % | 70 % | +0 pts | -12 % | 70 % | — | 1.47 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Torbjorn Heggem entradas 1+ | 1.28 | 70 % | 70 % | 69 % | +1 pts | -10 % | 66 % | — | 1.47 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 8.5 | 1.37 | 70 % | 70 % | 70 % | -0 pts | -4 % | 70 % | +0.6 | 1.47 | Expulsión antes del 70′ | Alta probabilidad |
| Erling Haaland o Rasmus Hojlund (anota) | 1.26 | 70 % | 71 % | 70 % | +0 pts | -12 % | 67 % | — | 1.47 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Más 3.5 | 1.32 | 70 % | 73 % | 71 % | -1 pts | -8 % | 70 % | +0.5 | 1.47 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Martin Odegaard entradas 1+ | 1.28 | 70 % | 70 % | 69 % | +1 pts | -10 % | 66 % | — | 1.47 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Faltas Más 23.5 | 1.93 | 55 % | 48 % | 48 % | +7 pts | +6 % | 54 % | +0.1 | 1.89 | Empate | Contexto a favor (+7 pts) · Valor |
| Tarjetas Más 4.5 | 2.22 | 46 % | 41 % | 40 % | +6 pts | +2 % | 40 % | -0.0 | 2.27 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · ★ enfoque a favor |
| Tarjetas Más 3.5 | 1.62 | 63 % | 58 % | 58 % | +6 pts | +2 % | 58 % | +0.4 | 1.63 | Favorito golpea temprano y gana | Contexto a favor (+6 pts) · ★ enfoque a favor |
| Tarjetas Noruega Más 2.5 | 2.50 | 40 % | 36 % | 35 % | +6 pts | +1 % | 35 % | -0.1 | 2.61 | Sorpresa: gana el no favorito | Contexto a favor (+5 pts) · ★ enfoque a favor |
| Tarjetas Más 5.5 | 3.20 | 31 % | 27 % | 26 % | +5 pts | -0 % | 26 % | -0.4 | 3.43 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) · ★ enfoque a favor |
| Ambos 2+ tarjetas: Sí | 2.12 | 48 % | 43 % | 43 % | +5 pts | +2 % | 44 % | — | 2.17 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Faltas Noruega Más 12.5 | 2.05 | 50 % | 45 % | 45 % | +5 pts | +2 % | 47 % | +0.0 | 2.10 | Sorpresa: gana el no favorito | Contexto a favor (+5 pts) |
| Tarjetas Noruega Más 1.5 | 1.52 | 67 % | 63 % | 63 % | +5 pts | +2 % | 64 % | +0.5 | 1.53 | Sorpresa: gana el no favorito | Alta probabilidad · Contexto a favor (+5 pts) · ★ enfoque a favor |
| Faltas Dinamarca Más 11.5 | 2.05 | 49 % | 45 % | 45 % | +4 pts | +1 % | 48 % | +0.0 | 2.12 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) |
| Tarjetas Dinamarca Más 2.5 | 2.60 | 37 % | 34 % | 33 % | +4 pts | -3 % | 33 % | -0.2 | 2.83 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · ★ enfoque a favor |
| Tarjetas 1.er tiempo Más 1.5 | 2.10 | 46 % | 44 % | 42 % | +4 pts | -4 % | 42 % | +0.0 | 2.28 | Favorito gana en partido trabado | Contexto a favor (+4 pts) · ★ enfoque a favor |
| Tarjetas Más 2.5 | 1.28 | 79 % | 76 % | 75 % | +4 pts | +2 % | 76 % | +0.8 | 1.30 | Favorito golpea temprano y gana | Alta probabilidad · Contexto a favor (+4 pts) · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Saques de banda 1.er tiempo Menos 16.5 | 1.93 | 60 % | 48 % | 59 % | +1 pts | +15 % | 59 % | +0.5 | 1.73 | Empate | Valor · ⚠ Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Faltas Más 23.5 | 1.93 | 55 % | 48 % | 48 % | +7 pts | +6 % | 54 % | +0.1 | 1.89 | Empate | Contexto a favor (+7 pts) · Valor |

Kelly ¼ (dato informativo, no una orden de stake): Saques de banda 1.er tiempo Menos 16.5 4.2 % de la banca; Faltas Más 23.5 1.6 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |
| Ingeniero Analista #313 | Más 2.5 ≤1,45 → gol en el 1.er tiempo | Goles 1.er tiempo Más 0.5 | sin historial con cuotas (medir en el registro) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí | 61 % | 61 % | 56 % | 1.64 | 1.69 | 1.18 | 8 % | Expulsión antes del 70′ | 56 % |
| Ambos 1+ tarjetas: Sí + Tarjetas Dinamarca Más 1.5 | 61 % | 61 % | 56 % | 1.65 | 1.70 | 1.14 | 8 % | Expulsión antes del 70′ | 57 % |
| Goles Dinamarca Menos 3.5 + Córners Dinamarca Más 1.5 + Noruega o empate | 60 % | 60 % | 55 % | 1.67 | 1.72 | 1.08 | 6 % | Favorito golpea temprano y gana | 0 % |
| Goles Dinamarca Menos 3.5 + Córners Noruega Menos 9.5 + Noruega o empate | 60 % | 59 % | 55 % | 1.67 | 1.72 | 1.08 | 7 % | Favorito golpea temprano y gana | 0 % |
| Hándicap Dinamarca +3 + Goles 2.º tiempo Menos 2.5 + Córners Dinamarca Más 1.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.02 | 6 % | Empate | 46 % |
| Tarjetas Noruega Más 1.5 + Hándicap Dinamarca +3 + Goles Noruega Menos 3.5 | 60 % | 60 % | 55 % | 1.68 | 1.73 | 1.05 | 8 % | Expulsión antes del 70′ | 53 % |
| Tarjetas Noruega Más 1.5 + Goles Noruega Menos 3.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.01 | 6 % | Expulsión antes del 70′ | 53 % |
| Tarjetas Dinamarca Más 1.5 + Córners Noruega Menos 9.5 | 61 % | 60 % | 57 % | 1.63 | 1.68 | 1.0 | 6 % | Expulsión antes del 70′ | 57 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.