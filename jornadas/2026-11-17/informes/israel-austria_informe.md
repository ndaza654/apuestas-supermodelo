# Israel - Austria
UEFA Liga de Naciones · 2026-11-17 14:45

**Tipo de partido:** Favorito leve · abierto · normal · **Favorito:** Austria · primer gol: local 36 %, visitante 60 %, nadie 5 % · gol del favorito antes del 35′: 40 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Resultado / hándicap | ➖ neutro | Austria favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Tarjetas y faltas | ❔ sin señal | árbitro sin dato |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 34 % |
| Sorpresa: gana el no favorito | 20 % |
| Empate | 14 % |
| Favorito golpea temprano y gana | 12 % |
| Favorito gana en partido trabado | 11 % |
| Expulsión antes del 70′ | 9 % |

## Lo que cambió el contexto
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.18 | 12.5 | 4.3 | 4.3 | 11.8 | 2.2 |
| visitante | 1.84 | 12.5 | 4.3 | 4.3 | 11.8 | 1.6 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.0) · 1–5 | 1.2 (1.2) · 0–3 | 1.8 (1.9) · 0–4 | 1.3 (1.3) · 0–3 | 1.7 (1.7) · 0–3 |
| Córners | 8.7 (8.7) · 5–13 | 4.3 · 1–7 | 4.3 · 2–7 | 3.9 (4.2) · 1–7 | 4.8 (4.6) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 3.8 (3.8) · 1–7 | 2.2 (2.2) · 1–4 | 1.6 (1.6) · 0–3 | 1.3 (1.4) · 0–3 | 2.5 · 0–5 |
| Remates | 24.9 · 18–32 | 12.4 · 7–18 | 12.4 · 7–18 | 11.0 · 7–16 | 13.8 · 9–19 |
| Tiros al arco | 8.6 · 5–12 | 4.2 · 2–7 | 4.3 · 2–7 | 3.8 · 1–6 | 4.8 · 2–8 |
| Faltas | 23.5 · 17–30 | 11.8 · 7–16 | 11.7 · 7–16 | 10.5 · 6–15 | 12.9 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 40.2 · 29–52 | 20.2 · 12–28 | 20.1 · 12–28 | 17.9 · 12–25 | 22.3 · 15–30 |
| Atajadas del portero | — | 2.5 · 0–5 | 3.1 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Menos 2.5 | 1.30 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (56 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.57 | 60 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Cara · ★ enfoque a favor |
| Resultado y hándicap | Austria o empate | 1.27 | 77 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 5.5 | 1.27 | 78 % | 76 % | Favorito gana en partido trabado (81 %) | Partido abierto (ambos marcan y 3+ goles) (76 %) | Alta probabilidad |
| Tarjetas | Ambos 1+ tarjetas: Sí | 1.33 | 73 % | 68 % | Expulsión antes del 70′ (86 %) | Favorito golpea temprano y gana (68 %) | Alta probabilidad |
| Jugadores | Konrad Laimer anota o asiste | 3.25 | 30 % | 15 % | Partido abierto (ambos marcan y 3+ goles) (43 %) | Empate (15 %) | Justa |
| Quién saca más | Más tarjetas: Israel | 1.82 | 52 % | 49 % | Expulsión antes del 70′ (59 %) | Favorito golpea temprano y gana (49 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 5.5 | 1.27 | 78 % | 76 % | 78 % | +0 pts | -1 % | 76 % | +0.8 | 1.31 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Austria o empate | 1.27 | 77 % | 77 % | 77 % | +0 pts | -2 % | 77 % | — | 1.33 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Austria +1 | 1.27 | 77 % | 77 % | 77 % | +0 pts | -2 % | 77 % | — | 1.33 | Sorpresa: gana el no favorito | Alta probabilidad |
| No hay empate | 1.26 | 76 % | 76 % | 75 % | +1 pts | -4 % | 76 % | — | 1.35 | Empate | Alta probabilidad |
| Córners Más 6.5 | 1.26 | 76 % | 77 % | 75 % | +1 pts | -4 % | 75 % | +0.7 | 1.36 | Favorito gana en partido trabado | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.30 | 76 % | 75 % | 75 % | +0 pts | -1 % | 76 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 10.5 | 1.29 | 75 % | 75 % | 74 % | +0 pts | -4 % | 72 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Ambos 1+ tarjetas: Sí | 1.33 | 73 % | 73 % | 74 % | -1 pts | -3 % | 68 % | — | 1.41 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Austria Menos 2.5 | 1.34 | 73 % | 72 % | 72 % | +0 pts | -3 % | 72 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.34 | 72 % | 72 % | 73 % | -1 pts | -3 % | 72 % | +0.7 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners Israel Más 2.5 | 1.37 | 72 % | 68 % | 72 % | -0 pts | -1 % | 69 % | +0.8 | 1.42 | Expulsión antes del 70′ | Alta probabilidad |
| Hándicap Israel +2 | 1.36 | 71 % | 71 % | 71 % | -0 pts | -3 % | 71 % | — | 1.44 | Favorito golpea temprano y gana | Alta probabilidad |
| Hándicap Israel +1.5 | 1.38 | 71 % | 71 % | 71 % | -0 pts | -2 % | 71 % | — | 1.45 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles 1.er tiempo Menos 1.75 | 1.37 | 71 % | 71 % | 70 % | +0 pts | -3 % | 71 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % |
| Goles Menos 3.75 | 1.40 | 70 % | 70 % | 70 % | +0 pts | -1 % | 70 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Hándicap Austria -0 | 1.42 | 70 % | 69 % | 70 % | +0 pts | -0 % | 70 % | — | 1.47 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 24 % |
| Goles Israel Más 0.5 | 1.37 | 70 % | 70 % | 70 % | -0 pts | -5 % | 70 % | +0.6 | 1.48 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners 2.º tiempo Más 3.5 | 1.44 | 69 % | 67 % | 67 % | +2 pts | -1 % | 65 % | +0.6 | 1.49 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 2.º tiempo Menos 5.5 | 1.38 | 68 % | 70 % | 68 % | +0 pts | -7 % | 66 % | +0.3 | 1.52 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Hándicap Israel +1.25 | 1.45 | 67 % | 67 % | 68 % | -0 pts | -2 % | 67 % | — | 1.53 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 13 % |
| Goles Israel Menos 1.5 | 1.44 | 67 % | 67 % | 67 % | +0 pts | -4 % | 67 % | +0.3 | 1.54 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles 1.er tiempo Más 0.75 | 1.47 | 67 % | 66 % | 67 % | -0 pts | -2 % | 67 % | +0.5 | 1.54 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| Córners Austria Más 3.5 | 1.31 | 66 % | 71 % | 65 % | +0 pts | -14 % | 58 % | +0.3 | 1.57 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Goles Más 2.25 | 1.50 | 65 % | 65 % | 65 % | -0 pts | -2 % | 65 % | +0.4 | 1.58 | Empate | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Eli Dasa anota o asiste | 7.80 | 15 % | 11 % | 16 % | -0 pts | +20 % | 0 % | — | 7.51 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Ilay Feingold anota o asiste | 7.00 | 16 % | 12 % | 17 % | -0 pts | +15 % | 0 % | — | 6.91 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Roy Revivo anota o asiste | 6.80 | 17 % | 13 % | 17 % | +0 pts | +15 % | 0 % | — | 6.74 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Felix Bacher anota o asiste | 6.40 | 18 % | 14 % | 17 % | +0 pts | +13 % | 8 % | — | 6.40 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Kevin Danso anota o asiste | 5.50 | 20 % | 16 % | 20 % | +0 pts | +12 % | 10 % | — | 5.45 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Más corners: Israel | 3.20 | 35 % | 26 % | 35 % | -0 pts | +12 % | 29 % | — | 3.03 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Israel Más 5.5 | 4.65 | 24 % | 20 % | 24 % | -0 pts | +11 % | 20 % | -0.5 | 4.58 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Israel Más 4.5 | 2.92 | 37 % | 32 % | 37 % | +0 pts | +9 % | 34 % | -0.1 | 2.83 | Expulsión antes del 70′ | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |

Kelly ¼ (dato informativo, no una orden de stake): Eli Dasa anota o asiste 0.7 % de la banca; Ilay Feingold anota o asiste 0.6 % de la banca; Roy Revivo anota o asiste 0.6 % de la banca; Felix Bacher anota o asiste 0.6 % de la banca; Kevin Danso anota o asiste 0.7 % de la banca; Más corners: Israel 1.4 % de la banca; Córners Israel Más 5.5 0.7 % de la banca; Córners Israel Más 4.5 1.2 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Hándicap Austria +2 + Austria o empate + Descanso o final: Austria | 58 % | 59 % | 54 % | 1.71 | 1.76 | 1.34 | 10 % | Favorito golpea temprano y gana | 0 % |
| Goles Israel Menos 2.5 + Austria o empate + Descanso o final: Austria | 57 % | 57 % | 52 % | 1.76 | 1.82 | 1.35 | 11 % | Favorito golpea temprano y gana | 0 % |
| Hándicap Austria +2 + Córners Israel Más 2.5 + Goles Israel Menos 2.5 | 62 % | 66 % | 58 % | 1.61 | 1.66 | 1.05 | 10 % | Favorito golpea temprano y gana | 37 % |
| Córners 1.er tiempo Menos 4.5 + Goles 1.er tiempo Menos 3.5 | 61 % | 63 % | 56 % | 1.65 | 1.70 | 1.01 | 6 % | Favorito gana en partido trabado | 56 % |
| Córners 1.er tiempo Menos 4.5 + Goles Menos 6.5 | 61 % | 64 % | 56 % | 1.64 | 1.69 | 1.0 | 6 % | Favorito gana en partido trabado | 57 % |
| Goles Menos 6.5 + Tarjetas Israel Menos 2.5 | 61 % | 61 % | 56 % | 1.65 | 1.70 | 1.0 | 6 % | Favorito golpea temprano y gana | 62 % |
| Goles Austria Menos 4.5 + Tarjetas Israel Menos 2.5 | 60 % | 61 % | 56 % | 1.65 | 1.70 | 1.0 | 6 % | Favorito golpea temprano y gana | 62 % |
| Goles Austria Menos 4.5 + Tarjetas 1.er tiempo Menos 1.5 | 60 % | 62 % | 55 % | 1.67 | 1.72 | 1.0 | 6 % | Empate | 62 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.