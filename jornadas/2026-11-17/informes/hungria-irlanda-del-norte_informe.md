# Hungría - Irlanda del Norte
UEFA Liga de Naciones · 2026-11-17 14:45

**Tipo de partido:** Favorito leve · cerrado · caliente · **Favorito:** Hungría · primer gol: local 57 %, visitante 32 %, nadie 11 % · gol del favorito antes del 35′: 32 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Resultado / hándicap | ➖ neutro | Hungría favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; los dos se juegan algo importante |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Empate | 21 % |
| Partido abierto (ambos marcan y 3+ goles) | 19 % |
| Sorpresa: gana el no favorito | 19 % |
| Favorito gana en partido trabado | 16 % |
| Favorito golpea temprano y gana | 13 % |
| Expulsión antes del 70′ | 12 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.32 | 14.2 | 4.6 | 4.5 | 13.6 | 2.5 |
| visitante | 0.79 | 10.1 | 2.9 | 4.5 | 13.6 | 3.1 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.1 (2.2) · 0–4 | 1.3 (1.4) · 0–3 | 0.8 (0.8) · 0–2 | 0.9 (0.9) · 0–2 | 1.2 (1.2) · 0–3 |
| Córners | 9.1 (9.0) · 5–13 | 4.5 · 2–8 | 4.6 · 2–8 | 4.0 (4.4) · 2–7 | 5.0 (4.7) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.6 (5.3) · 2–9 | 2.5 (2.4) · 1–5 | 3.1 (2.9) · 1–5 | 1.8 (1.9) · 0–4 | 3.8 · 1–7 |
| Remates | 24.3 (24.1) · 17–32 | 14.2 (14.2) · 9–20 | 10.1 (10.1) · 6–15 | 10.8 · 7–15 | 13.5 · 9–19 |
| Tiros al arco | 7.5 (7.5) · 4–11 | 4.6 (4.6) · 2–8 | 2.9 (2.9) · 1–5 | 3.3 · 1–6 | 4.2 · 2–7 |
| Faltas | 26.8 (26.5) · 20–34 | 13.4 (13.2) · 9–18 | 13.4 (13.2) · 9–18 | 12.0 · 8–17 | 14.8 · 10–20 |
| Fueras de lugar | 4.0 (4.0) · 1–7 | 1.7 (1.7) · 0–4 | 2.3 (2.3) · 0–5 | 1.8 · 0–4 | 2.2 · 0–4 |
| Saques de meta | 16.1 · 10–23 | 8.0 · 4–13 | 8.1 · 4–13 | 7.2 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 40.1 · 29–52 | 20.0 · 12–28 | 20.1 · 13–28 | 17.9 · 12–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 2.1 · 0–4 | 3.3 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Menos 1.5 | 1.28 | 76 % | (lo define el marcador) | Favorito gana en partido trabado (98 %) | Partido abierto (ambos marcan y 3+ goles) (45 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: No | 1.62 | 59 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Justa |
| Resultado y hándicap | Hándicap Hungría +1 | 1.25 | 78 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Sorpresa: gana el no favorito (0 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 5.5 | 1.31 | 76 % | 74 % | Favorito gana en partido trabado (78 %) | Partido abierto (ambos marcan y 3+ goles) (74 %) | Alta probabilidad |
| Tarjetas | Ambos 2+ tarjetas: Sí | 1.65 | 61 % | 54 % | Expulsión antes del 70′ (79 %) | Favorito golpea temprano y gana (54 %) | Justa |
| Faltas | Faltas Más 26.5 | 1.93 | 51 % | 49 % | Expulsión antes del 70′ (57 %) | Favorito gana en partido trabado (49 %) | Justa |
| Remates | Remates Irlanda del Norte Más 8.5 | 1.44 | 66 % | 58 % | Partido abierto (ambos marcan y 3+ goles) (75 %) | Expulsión antes del 70′ (58 %) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco | Tiros al arco Hungría Más 3.5 | 1.42 | 67 % | 49 % | Partido abierto (ambos marcan y 3+ goles) (89 %) | Sorpresa: gana el no favorito (49 %) | Cara |
| Fueras de lugar | Fueras de lugar Más 3.5 | 1.78 | 53 % | 51 % | Partido abierto (ambos marcan y 3+ goles) (54 %) | Expulsión antes del 70′ (51 %) | Cara |
| Jugadores | Zsolt Nagy anota o asiste | 3.05 | 31 % | 12 % | Partido abierto (ambos marcan y 3+ goles) (53 %) | Sorpresa: gana el no favorito (12 %) | Cara |
| Quién saca más | Más corners: Irlanda del Norte | 3.00 | 37 % | 32 % | Favorito golpea temprano y gana (45 %) | Sorpresa: gana el no favorito (32 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hándicap Hungría +1 | 1.25 | 78 % | 78 % | 78 % | -0 pts | -2 % | 78 % | — | 1.32 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hungría o empate | 1.25 | 78 % | 78 % | 78 % | -0 pts | -2 % | 78 % | — | 1.32 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Irlanda del Norte +2 | 1.27 | 77 % | 77 % | 77 % | -0 pts | -2 % | 77 % | — | 1.33 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles 1.er tiempo Menos 1.5 | 1.28 | 76 % | 76 % | 76 % | +1 pts | -2 % | 76 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Menos 5.5 | 1.31 | 76 % | 74 % | 76 % | +1 pts | -0 % | 74 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Hungría Más 0.5 | 1.30 | 75 % | 74 % | 75 % | +0 pts | -3 % | 75 % | +0.8 | 1.37 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners Irlanda del Norte Más 2.5 | 1.31 | 75 % | 71 % | 75 % | -0 pts | -2 % | 69 % | +0.8 | 1.37 | Expulsión antes del 70′ | Alta probabilidad |
| Goles Más 1.25 | 1.34 | 73 % | 73 % | 73 % | -0 pts | -3 % | 73 % | +0.6 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 13 % |
| No hay empate | 1.31 | 73 % | 72 % | 71 % | +2 pts | -5 % | 73 % | — | 1.42 | Empate | Alta probabilidad |
| Córners 2.º tiempo Más 3.5 | 1.39 | 72 % | 69 % | 71 % | +1 pts | -1 % | 68 % | +0.7 | 1.44 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Menos 1.25 | 1.38 | 71 % | 71 % | 71 % | +1 pts | -2 % | 71 % | +0.3 | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 18 % · ★ enfoque a favor |
| Goles Menos 2.75 | 1.40 | 71 % | 70 % | 70 % | +1 pts | -0 % | 71 % | +0.4 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 10 % · ★ enfoque a favor |
| Goles 2.º tiempo Más 0.5 | 1.36 | 71 % | 71 % | 70 % | +0 pts | -4 % | 71 % | +0.6 | 1.46 | Empate | Alta probabilidad |
| Hándicap Hungría +0 | 1.42 | 70 % | 69 % | 70 % | +0 pts | -1 % | 70 % | — | 1.47 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 29 % |
| Córners Menos 10.5 | 1.35 | 70 % | 71 % | 70 % | -1 pts | -6 % | 66 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Eoin Kenny remates 1+ | 1.27 | 69 % | 70 % | 69 % | +0 pts | -12 % | 66 % | — | 1.49 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| András Schäfer remates 1+ | 1.29 | 69 % | 69 % | 69 % | +0 pts | -11 % | 66 % | — | 1.49 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Willi Orban remates 1+ | 1.28 | 69 % | 70 % | 69 % | +0 pts | -12 % | 67 % | — | 1.49 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Paul Smyth remates 1+ | 1.27 | 69 % | 70 % | 69 % | -0 pts | -12 % | 66 % | — | 1.49 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Aron Doktorics remates 1+ | 1.29 | 68 % | 69 % | 68 % | -0 pts | -12 % | 67 % | — | 1.51 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Jozef Urblik remates 1+ | 1.29 | 68 % | 69 % | 68 % | -0 pts | -12 % | 66 % | — | 1.52 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Milan Vitalis remates 1+ | 1.29 | 68 % | 69 % | 68 % | -0 pts | -13 % | 66 % | — | 1.52 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 7.5 | 1.42 | 68 % | 68 % | 67 % | +1 pts | -4 % | 64 % | +0.5 | 1.52 | Expulsión antes del 70′ | Alta probabilidad |
| Akos Szendrei tiros al arco 1+ | 1.30 | 67 % | 69 % | 67 % | -0 pts | -12 % | 60 % | — | 1.53 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Córners Hungría Más 3.5 | 1.28 | 67 % | 73 % | 68 % | -0 pts | -14 % | 57 % | +0.4 | 1.53 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bence Varkonyi anota o asiste | 11.75 | 11 % | 7 % | 11 % | -0 pts | +27 % | 4 % | — | 11.38 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Akos Markgraf anota o asiste | 10.50 | 12 % | 8 % | 12 % | -0 pts | +22 % | 4 % | — | 10.42 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Mark Csinger anota o asiste | 9.00 | 13 % | 10 % | 13 % | +0 pts | +21 % | 5 % | — | 8.75 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Attila Osvath anota o asiste | 7.10 | 17 % | 12 % | 17 % | +0 pts | +19 % | 6 % | — | 6.75 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) |
| Córners Irlanda del Norte Más 5.5 | 4.15 | 27 % | 23 % | 27 % | +0 pts | +12 % | 22 % | -0.4 | 3.99 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: Irlanda del Norte | 3.00 | 37 % | 28 % | 36 % | +0 pts | +10 % | 32 % | — | 2.90 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Irlanda del Norte Más 4.5 | 2.62 | 41 % | 36 % | 41 % | +0 pts | +7 % | 36 % | +0.0 | 2.57 | Expulsión antes del 70′ | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |

Kelly ¼ (dato informativo, no una orden de stake): Bence Varkonyi anota o asiste 0.6 % de la banca; Akos Markgraf anota o asiste 0.6 % de la banca; Mark Csinger anota o asiste 0.7 % de la banca; Attila Osvath anota o asiste 0.8 % de la banca; Córners Irlanda del Norte Más 5.5 1.0 % de la banca; Más corners: Irlanda del Norte 1.2 % de la banca; Córners Irlanda del Norte Más 4.5 1.1 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles Menos 3.5 + Tiros al arco Menos 8.5 | 61 % | 61 % | 56 % | 1.64 | 1.69 | 1.1 | 6 % | Empate | 23 % |
| Hándicap Irlanda del Norte +3 + Goles Menos 3.5 + Tiros al arco Hungría Menos 5.5 | 59 % | 60 % | 55 % | 1.68 | 1.73 | 1.12 | 8 % | Empate | 25 % |
| Hándicap Irlanda del Norte +3 + Goles 2.º tiempo Menos 2.5 + Tiros al arco Hungría Menos 5.5 | 61 % | 62 % | 56 % | 1.65 | 1.70 | 1.09 | 7 % | Empate | 32 % |
| Goles 2.º tiempo Menos 2.5 + Tiros al arco Menos 8.5 | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.06 | 6 % | Empate | 28 % |
| Goles Irlanda del Norte Menos 2.5 + Hungría o empate + Córners Más 6.5 | 62 % | 62 % | 58 % | 1.63 | 1.67 | 1.04 | 7 % | Empate | 0 % |
| Córners Más 6.5 + Tiros al arco Irlanda del Norte Más 1.5 | 62 % | 61 % | 58 % | 1.60 | 1.65 | 1.01 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 48 % |
| Goles 1.er tiempo Menos 2.5 + Ambos marcan: No | 58 % | 57 % | 53 % | 1.72 | 1.77 | 1.06 | 7 % | Favorito gana en partido trabado | 0 % |
| Córners 2.º tiempo Más 2.5 + Goles 1.er tiempo Menos 2.5 + Tiros al arco Irlanda del Norte Más 1.5 | 62 % | 62 % | 58 % | 1.62 | 1.67 | 0.99 | 7 % | Sorpresa: gana el no favorito | 50 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.