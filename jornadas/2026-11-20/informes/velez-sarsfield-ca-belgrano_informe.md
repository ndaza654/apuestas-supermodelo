# Velez Sarsfield - CA Belgrano
Argentina Liga Profesional · 2026-11-20 18:00

**Tipo de partido:** Parejo · cerrado · caliente · **Favorito:** Velez Sarsfield · primer gol: local 50 %, visitante 40 %, nadie 10 % · gol del favorito antes del 35′: 29 %

**Base de la liga:** Argentina Liga Profesional · 2.11 goles/partido, Más 2.5 35 %, ambos marcan 43 % (1268 partidos ago-2022/nov-2026)

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso, Empate / doble oportunidad / HT-FT X. Poco favorecidos: Hándicap y victoria.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; parejo: más duelos y más faltas |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Sorpresa: gana el no favorito | 26 % |
| Empate | 21 % |
| Partido abierto (ambos marcan y 3+ goles) | 20 % |
| Expulsión antes del 70′ | 12 % |
| Favorito gana en partido trabado | 12 % |
| Favorito golpea temprano y gana | 10 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.27 | 15.6 | 5.0 | 4.7 | 11.8 | 2.4 |
| visitante | 1.03 | 12.6 | 4.0 | 4.7 | 11.8 | 3.0 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.3 (2.3) · 0–4 | 1.3 (1.3) · 0–3 | 1.0 (1.1) · 0–2 | 1.0 (1.1) · 0–2 | 1.3 (1.3) · 0–3 |
| Córners | 9.3 (9.4) · 5–14 | 4.6 · 2–8 | 4.7 · 2–8 | 4.2 (4.5) · 2–7 | 5.2 (5.0) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.4 (5.4) · 2–9 | 2.4 (2.4) · 1–4 | 3.0 (3.0) · 1–5 | 1.8 (1.9) · 0–4 | 3.6 · 1–6 |
| Remates | 28.2 (28.1) · 21–36 | 15.5 (15.6) · 9–22 | 12.6 (12.6) · 7–18 | 12.7 · 8–18 | 15.5 · 10–21 |
| Tiros al arco | 8.9 (9.0) · 5–13 | 4.9 (5.0) · 2–8 | 4.0 (4.0) · 1–7 | 4.0 · 2–7 | 4.9 · 2–8 |
| Faltas | 23.6 · 17–30 | 11.8 · 8–16 | 11.8 · 7–16 | 10.6 · 7–15 | 13.0 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.2 · 10–23 | 8.2 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 9.0 · 5–14 |
| Saques de banda | 39.9 · 28–52 | 20.1 · 12–28 | 19.8 · 12–28 | 17.8 · 11–25 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.0 · 1–6 | 3.7 · 1–7 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 3.0 | 1.32 | 75 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Alta probabilidad · asiática: devuelve 20 % · ★ enfoque a favor |
| Resultado y hándicap | Velez Sarsfield o empate | 1.37 | 71 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.35 | 81 % | 70 % | Favorito gana en partido trabado (74 %) | Partido abierto (ambos marcan y 3+ goles) (70 %) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Tarjetas | Tarjetas Más 3.5 | 1.29 | 75 % | 72 % | Expulsión antes del 70′ (97 %) | Favorito golpea temprano y gana (68 %) | Alta probabilidad |
| Remates | Remates Más 24.5 | 1.30 | 73 % | 66 % | Partido abierto (ambos marcan y 3+ goles) (84 %) | Empate (66 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco CA Belgrano Más 2.5 | 1.27 | 75 % | 69 % | Sorpresa: gana el no favorito (91 %) | Favorito gana en partido trabado (54 %) | Alta probabilidad |
| Quién saca más | Más corners: CA Belgrano | 2.82 | 38 % | 33 % | Favorito golpea temprano y gana (47 %) | Sorpresa: gana el no favorito (33 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Menos 12.0 | 1.25 | 81 % | 80 % | 81 % | +0 pts | +1 % | 72 % | +0.8 | 1.27 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners 1.er tiempo Menos 6.0 | 1.35 | 81 % | 78 % | 81 % | +0 pts | +9 % | 70 % | +0.9 | 1.28 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners CA Belgrano Más 2.5 | 1.25 | 78 % | 75 % | 78 % | +0 pts | -3 % | 76 % | +0.9 | 1.32 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Más 7.0 | 1.34 | 77 % | 77 % | 77 % | +0 pts | +4 % | 69 % | +0.7 | 1.33 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Menos 11.5 | 1.25 | 77 % | 78 % | 77 % | +0 pts | -4 % | 73 % | +0.7 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tiros al arco Velez Sarsfield Menos 6.5 | 1.27 | 76 % | 76 % | 76 % | +0 pts | -3 % | 59 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas Más 3.5 | 1.29 | 75 % | 75 % | 75 % | +0 pts | -3 % | 72 % | +0.7 | 1.37 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Menos 3.0 | 1.32 | 75 % | 75 % | 75 % | +0 pts | -1 % | 75 % | +0.5 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 20 % · ★ enfoque a favor |
| Tiros al arco CA Belgrano Más 2.5 | 1.27 | 75 % | 76 % | 75 % | +0 pts | -5 % | 69 % | +0.7 | 1.38 | Favorito gana en partido trabado | Alta probabilidad |
| Remates Velez Sarsfield Más 12.5 | 1.26 | 74 % | 77 % | 74 % | +0 pts | -7 % | 70 % | +0.6 | 1.39 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Córners 2.º tiempo Más 3.5 | 1.33 | 73 % | 73 % | 73 % | +0 pts | -2 % | 73 % | +0.7 | 1.40 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.45 | 73 % | 75 % | 73 % | +0 pts | +7 % | 59 % | +0.6 | 1.40 | Empate | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Remates Menos 31.5 | 1.29 | 73 % | 75 % | 73 % | +0 pts | -5 % | 61 % | +0.6 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Menos 5.5 | 1.35 | 73 % | 71 % | 73 % | +0 pts | -1 % | 71 % | +0.6 | 1.41 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Remates Más 24.5 | 1.30 | 73 % | 74 % | 73 % | +0 pts | -5 % | 66 % | +0.6 | 1.41 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Goles Velez Sarsfield Más 0.5 | 1.33 | 73 % | 73 % | 73 % | +0 pts | -3 % | 73 % | +0.7 | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Menos 11.0 | 1.44 | 72 % | 72 % | 72 % | +0 pts | +4 % | 62 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles 1.er tiempo Menos 1.5 | 1.36 | 72 % | 71 % | 72 % | +0 pts | -2 % | 72 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Goles CA Belgrano Menos 1.5 | 1.34 | 72 % | 72 % | 72 % | +0 pts | -3 % | 72 % | +0.5 | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Goles 2.º tiempo Más 0.5 | 1.35 | 72 % | 72 % | 72 % | +0 pts | -3 % | 72 % | +0.7 | 1.43 | Empate | Alta probabilidad |
| Tiros al arco Velez Sarsfield Más 3.5 | 1.31 | 72 % | 74 % | 72 % | +0 pts | -6 % | 59 % | +0.6 | 1.44 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas 1.er tiempo Menos 2.5 | 1.40 | 71 % | 69 % | 71 % | +0 pts | -0 % | 74 % | +0.5 | 1.45 | Expulsión antes del 70′ | Alta probabilidad |
| Velez Sarsfield o empate | 1.37 | 71 % | 71 % | 71 % | +0 pts | -3 % | 71 % | — | 1.45 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Hándicap Velez Sarsfield +0.5 | 1.38 | 71 % | 71 % | 71 % | +0 pts | -2 % | 71 % | — | 1.45 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Hándicap Velez Sarsfield +1 | 1.37 | 71 % | 71 % | 71 % | +0 pts | -3 % | 71 % | — | 1.45 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.60 | 45 % | 43 % | 45 % | +0 pts | +17 % | 36 % | -0.1 | 2.32 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.75 | 65 % | 62 % | 65 % | +0 pts | +14 % | 55 % | +0.4 | 1.58 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 3.0 | 4.55 | 25 % | 24 % | 25 % | +0 pts | +13 % | 20 % | -0.6 | 4.37 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 6.0 | 1.35 | 81 % | 78 % | 81 % | +0 pts | +9 % | 70 % | +0.9 | 1.28 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Más corners: CA Belgrano | 2.82 | 38 % | 30 % | 38 % | +0 pts | +7 % | 33 % | — | 2.78 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Más 3.0 | 1.45 | 73 % | 75 % | 73 % | +0 pts | +7 % | 59 % | +0.6 | 1.40 | Empate | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners Menos 9.0 | 2.25 | 47 % | 47 % | 47 % | +0 pts | +6 % | 38 % | -0.1 | 2.21 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.75 | 60 % | 60 % | 60 % | +0 pts | +6 % | 50 % | +0.2 | 1.71 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 4.0 | 2.00 | 53 % | 55 % | 53 % | +0 pts | +5 % | 41 % | +0.1 | 1.97 | Empate | Valor · asiática: devuelve 19 % |
| Córners Más 9.0 | 2.02 | 52 % | 52 % | 52 % | +0 pts | +5 % | 44 % | +0.1 | 2.00 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.60 | 65 % | 66 % | 65 % | +0 pts | +5 % | 57 % | +0.4 | 1.58 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 2.0 | 1.18 | 89 % | 88 % | 89 % | +0 pts | +4 % | 76 % | +1.0 | 1.16 | Favorito golpea temprano y gana | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners Menos 11.0 | 1.44 | 72 % | 72 % | 72 % | +0 pts | +4 % | 62 % | +0.5 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners 1.er tiempo Menos 7.0 | 1.16 | 90 % | 87 % | 90 % | +0 pts | +4 % | 82 % | +1.3 | 1.15 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 7 % |
| Córners Más 7.0 | 1.34 | 77 % | 77 % | 77 % | +0 pts | +4 % | 69 % | +0.7 | 1.33 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.7 % de la banca; Córners 1.er tiempo Menos 5.0 4.8 % de la banca; Córners 1.er tiempo Menos 3.0 0.9 % de la banca; Córners 1.er tiempo Menos 6.0 6.3 % de la banca; Más corners: CA Belgrano 1.0 % de la banca; Córners 1.er tiempo Más 3.0 3.6 % de la banca; Córners Menos 9.0 1.3 % de la banca; Córners Menos 10.0 1.9 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5 | empate 2,90–3,20 (señal de pocos goles) | Goles Menos 2.5 | 18423 partidos: acierto 59.9 % contra 59.5 % del precio; ROI -3.9 % ± 1.1 (con la mejor cuota -0.3 %) |
| Ingeniero Analista #26 | parejo (ambos ≥2,00) y Más 1.5 >1,40 | Goles Menos 2.5 | 58298 partidos: acierto 53.4 % contra 53.3 % del precio; ROI -5.2 % ± 0.7 (con la mejor cuota -1.3 %) |
| Ingeniero Analista #420 | empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas | Empate | 48947 partidos: acierto 29.9 % contra 29.2 % del precio; ROI -5.0 % ± 1.3 (con la mejor cuota -0.1 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Tarjetas 1.er tiempo Menos 2.5 + Hándicap CA Belgrano +3 + Goles Velez Sarsfield Menos 2.5 | 62 % | 64 % | 57 % | 1.62 | 1.67 | 1.06 | 7 % | Empate | 46 % |
| Tarjetas 1.er tiempo Menos 2.5 + Goles CA Belgrano Menos 2.5 + Tiros al arco CA Belgrano Menos 7.5 | 62 % | 64 % | 58 % | 1.61 | 1.66 | 1.02 | 7 % | Favorito gana en partido trabado | 53 % |
| Córners 2.º tiempo Más 2.5 + Goles Velez Sarsfield Menos 2.5 + Tarjetas CA Belgrano Más 1.5 | 62 % | 64 % | 58 % | 1.61 | 1.66 | 1.01 | 7 % | Empate | 45 % |
| Córners 2.º tiempo Más 2.5 + Tarjetas CA Belgrano Más 1.5 + Goles 2.º tiempo Menos 2.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.0 | 7 % | Empate | 44 % |
| Ambos 1+ tarjetas: Sí + Goles 1.er tiempo Menos 2.5 + Tarjetas Menos 7.5 | 62 % | 63 % | 58 % | 1.60 | 1.65 | 0.97 | 6 % | Favorito gana en partido trabado | 54 % |
| Ambos 1+ tarjetas: Sí + Tiros al arco Menos 13.5 + Tarjetas Velez Sarsfield Menos 3.5 | 62 % | 63 % | 58 % | 1.61 | 1.66 | 0.97 | 7 % | Favorito gana en partido trabado | 59 % |
| Córners CA Belgrano Más 3.5 + Hándicap CA Belgrano +3 | 58 % | 62 % | 53 % | 1.73 | 1.78 | 1.0 | 8 % | Partido abierto (ambos marcan y 3+ goles) | 58 % |
| Córners CA Belgrano Más 3.5 + Tiros al arco Velez Sarsfield Menos 8.5 | 57 % | 60 % | 53 % | 1.75 | 1.80 | 1.01 | 8 % | Favorito golpea temprano y gana | 56 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.