# Palestino - Unión La Calera
Chile Liga de Primera · 2026-11-20 18:30

**Tipo de partido:** Favorito leve · medio · caliente · **Favorito:** Palestino · primer gol: local 55 %, visitante 39 %, nadie 6 % · gol del favorito antes del 35′: 35 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Goles del partido | ➖ neutro | ni muchos ni pocos goles esperados |
| Resultado / hándicap | ➖ neutro | Palestino favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 27 % |
| Sorpresa: gana el no favorito | 24 % |
| Empate | 16 % |
| Expulsión antes del 70′ | 12 % |
| Favorito golpea temprano y gana | 10 % |
| Favorito gana en partido trabado | 10 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.56 | 12.5 | 4.3 | 4.8 | 11.8 | 2.6 |
| visitante | 1.19 | 12.5 | 4.3 | 4.8 | 11.8 | 2.9 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.8 (2.8) · 1–5 | 1.6 (1.6) · 0–3 | 1.2 (1.2) · 0–3 | 1.2 (1.2) · 0–3 | 1.5 (1.6) · 0–3 |
| Córners | 9.6 (9.7) · 6–14 | 4.8 · 2–8 | 4.8 · 2–8 | 4.3 (4.7) · 2–7 | 5.3 (5.1) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.5 (5.5) · 2–9 | 2.6 (2.6) · 1–5 | 2.9 (2.9) · 1–5 | 1.8 (1.9) · 0–4 | 3.7 · 1–7 |
| Remates | 24.9 · 18–32 | 12.5 · 7–18 | 12.5 · 7–18 | 11.1 · 7–16 | 13.8 · 9–19 |
| Tiros al arco | 8.6 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.9 · 1–7 | 4.8 · 2–8 |
| Faltas | 23.6 · 17–30 | 11.7 · 7–16 | 11.8 · 8–16 | 10.6 · 7–15 | 13.0 · 8–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.8 · 5–14 |
| Saques de banda | 40.2 · 29–52 | 20.2 · 13–28 | 20.1 · 12–28 | 17.9 · 12–25 | 22.3 · 15–30 |
| Atajadas del portero | — | 3.2 · 1–6 | 2.7 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Más 1.5 | 1.28 | 76 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito gana en partido trabado (43 %) | Alta probabilidad |
| Resultado y hándicap | Hándicap Unión La Calera +2 | 1.25 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (29 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.40 | 79 % | 69 % | Favorito gana en partido trabado (73 %) | Partido abierto (ambos marcan y 3+ goles) (69 %) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Tarjetas | Tarjetas Menos 6.5 | 1.42 | 68 % | 71 % | Favorito golpea temprano y gana (78 %) | Expulsión antes del 70′ (30 %) | Alta probabilidad |
| Quién saca más | Más corners: Unión La Calera | 3.20 | 35 % | 30 % | Favorito golpea temprano y gana (41 %) | Sorpresa: gana el no favorito (30 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Más 7.0 | 1.29 | 80 % | 80 % | 80 % | -1 pts | +3 % | 72 % | +0.8 | 1.29 | Expulsión antes del 70′ | Alta probabilidad · asiática: devuelve 10 % |
| Córners 1.er tiempo Menos 6.0 | 1.40 | 79 % | 76 % | 78 % | +1 pts | +11 % | 69 % | +0.8 | 1.30 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Menos 12.0 | 1.30 | 79 % | 78 % | 79 % | +1 pts | +3 % | 70 % | +0.7 | 1.30 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners Unión La Calera Más 2.5 | 1.26 | 78 % | 74 % | 78 % | -0 pts | -2 % | 75 % | +0.9 | 1.32 | Expulsión antes del 70′ | Alta probabilidad |
| Hándicap Unión La Calera +2 | 1.25 | 77 % | 78 % | 78 % | -1 pts | -4 % | 77 % | — | 1.34 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Más 1.5 | 1.28 | 76 % | 76 % | 76 % | -0 pts | -3 % | 76 % | +0.8 | 1.36 | Favorito gana en partido trabado | Alta probabilidad |
| Córners 2.º tiempo Más 3.5 | 1.30 | 76 % | 74 % | 75 % | +0 pts | -2 % | 76 % | +0.8 | 1.36 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.40 | 75 % | 76 % | 75 % | -0 pts | +5 % | 61 % | +0.6 | 1.37 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners Menos 11.5 | 1.30 | 74 % | 74 % | 73 % | +1 pts | -3 % | 72 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| No hay empate | 1.29 | 74 % | 74 % | 74 % | +0 pts | -4 % | 74 % | — | 1.39 | Empate | Alta probabilidad |
| Córners 2.º tiempo Menos 6.5 | 1.28 | 74 % | 76 % | 73 % | +0 pts | -6 % | 71 % | +0.5 | 1.40 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 7.5 | 1.29 | 73 % | 75 % | 74 % | -1 pts | -6 % | 73 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Palestino o empate | 1.35 | 72 % | 72 % | 72 % | +0 pts | -2 % | 72 % | — | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Palestino +1 | 1.35 | 72 % | 72 % | 72 % | +0 pts | -2 % | 72 % | — | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Palestino +0.5 | 1.36 | 72 % | 72 % | 72 % | +0 pts | -2 % | 72 % | — | 1.42 | Sorpresa: gana el no favorito | Alta probabilidad |
| Córners 1.er tiempo Menos 5.5 | 1.40 | 72 % | 69 % | 71 % | +1 pts | +1 % | 70 % | +0.6 | 1.43 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Menos 3.5 | 1.39 | 70 % | 70 % | 70 % | -0 pts | -2 % | 70 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 11.0 | 1.52 | 70 % | 68 % | 69 % | +1 pts | +6 % | 60 % | +0.4 | 1.48 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles 1.er tiempo Más 0.5 | 1.40 | 69 % | 69 % | 70 % | -1 pts | -3 % | 69 % | +0.7 | 1.49 | Favorito gana en partido trabado | Alta probabilidad |
| Goles Unión La Calera Más 0.5 | 1.38 | 69 % | 70 % | 71 % | -1 pts | -5 % | 69 % | +0.6 | 1.49 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Más 2.0 | 1.42 | 69 % | 69 % | 69 % | -1 pts | -2 % | 69 % | +0.5 | 1.50 | Empate | Alta probabilidad · asiática: devuelve 24 % |
| Hándicap Palestino +0.25 | 1.44 | 68 % | 68 % | 68 % | +0 pts | -1 % | 68 % | — | 1.51 | Sorpresa: gana el no favorito | Alta probabilidad · asiática: devuelve 13 % |
| Tarjetas Menos 6.5 | 1.42 | 68 % | 67 % | 68 % | +0 pts | -4 % | 71 % | +0.4 | 1.52 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Más 8.0 | 1.52 | 68 % | 69 % | 69 % | -1 pts | +3 % | 60 % | +0.5 | 1.52 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Goles Unión La Calera Menos 1.5 | 1.44 | 67 % | 67 % | 66 % | +1 pts | -3 % | 67 % | +0.3 | 1.53 | Sorpresa: gana el no favorito | Alta probabilidad |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.80 | 43 % | 40 % | 42 % | +1 pts | +20 % | 34 % | -0.1 | 2.44 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.83 | 64 % | 60 % | 63 % | +1 pts | +17 % | 53 % | +0.3 | 1.62 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 3.0 | 4.85 | 24 % | 22 % | 23 % | +0 pts | +14 % | 18 % | -0.6 | 4.63 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 18 % |
| Más corners: Unión La Calera | 3.20 | 35 % | 26 % | 36 % | -0 pts | +13 % | 30 % | — | 3.00 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Menos 6.0 | 1.40 | 79 % | 76 % | 78 % | +1 pts | +11 % | 69 % | +0.8 | 1.30 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Unión La Calera Más 5.5 | 3.70 | 30 % | 25 % | 30 % | -1 pts | +10 % | 26 % | -0.3 | 3.61 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Menos 10.0 | 1.87 | 58 % | 56 % | 57 % | +1 pts | +8 % | 48 % | +0.1 | 1.80 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Menos 9.0 | 2.42 | 44 % | 43 % | 44 % | +1 pts | +8 % | 36 % | -0.2 | 2.35 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners Menos 8.0 | 3.40 | 31 % | 31 % | 31 % | +1 pts | +7 % | 25 % | -0.5 | 3.39 | Partido abierto (ambos marcan y 3+ goles) | Valor frágil (depende de un guion) · asiática: devuelve 12 % |
| Córners Unión La Calera Más 4.5 | 2.40 | 44 % | 39 % | 45 % | -0 pts | +7 % | 41 % | +0.1 | 2.36 | Expulsión antes del 70′ | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Menos 11.0 | 1.52 | 70 % | 68 % | 69 % | +1 pts | +6 % | 60 % | +0.4 | 1.48 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners 1.er tiempo Más 3.0 | 1.40 | 75 % | 76 % | 75 % | -0 pts | +5 % | 61 % | +0.6 | 1.37 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 7.0 | 1.18 | 88 % | 85 % | 88 % | +0 pts | +4 % | 82 % | +1.3 | 1.16 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 7 % |
| Córners 1.er tiempo Más 4.0 | 1.90 | 55 % | 58 % | 56 % | -1 pts | +4 % | 43 % | +0.1 | 1.89 | Favorito gana en partido trabado | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Más 2.0 | 1.16 | 89 % | 89 % | 90 % | -0 pts | +4 % | 77 % | +1.1 | 1.15 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 13 % |
| Córners Más 8.0 | 1.52 | 68 % | 69 % | 69 % | -1 pts | +3 % | 60 % | +0.5 | 1.52 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 12 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.8 % de la banca; Córners 1.er tiempo Menos 5.0 5.0 % de la banca; Córners 1.er tiempo Menos 3.0 0.9 % de la banca; Más corners: Unión La Calera 1.5 % de la banca; Córners 1.er tiempo Menos 6.0 7.0 % de la banca; Córners Unión La Calera Más 5.5 0.9 % de la banca; Córners Menos 10.0 2.2 % de la banca; Córners Menos 9.0 1.4 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles Unión La Calera Menos 2.5 + Ambos 1+ tarjetas: Sí + Palestino o empate | 62 % | 63 % | 58 % | 1.61 | 1.66 | 1.09 | 7 % | Empate | 0 % |
| Goles Unión La Calera Menos 2.5 + Córners 2.º tiempo Más 2.5 + Palestino o empate | 62 % | 62 % | 58 % | 1.61 | 1.66 | 1.08 | 7 % | Empate | 0 % |
| Córners 2.º tiempo Más 2.5 + Tarjetas Menos 6.5 | 60 % | 61 % | 56 % | 1.65 | 1.70 | 1.0 | 6 % | Favorito golpea temprano y gana | 64 % |
| Hándicap Palestino +2 + Tarjetas Menos 6.5 | 61 % | 61 % | 56 % | 1.64 | 1.69 | 0.99 | 6 % | Favorito golpea temprano y gana | 45 % |
| Hándicap Palestino +2 + Goles 2.º tiempo Menos 2.5 + Córners Palestino Más 2.5 | 60 % | 58 % | 56 % | 1.67 | 1.72 | 1.0 | 11 % | Empate | 46 % |
| Ambos 1+ tarjetas: Sí + Goles 2.º tiempo Menos 2.5 + Córners Palestino Más 2.5 | 59 % | 58 % | 55 % | 1.70 | 1.75 | 1.0 | 11 % | Empate | 43 % |
| Córners Unión La Calera Más 3.5 + Goles Menos 5.5 | 58 % | 62 % | 53 % | 1.73 | 1.78 | 1.0 | 8 % | Favorito golpea temprano y gana | 54 % |
| Córners Unión La Calera Más 3.5 + Goles Palestino Menos 3.5 | 57 % | 62 % | 52 % | 1.76 | 1.81 | 1.0 | 8 % | Empate | 54 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.