# Colo Colo - Universidad Catolica
Chile Liga de Primera · 2026-11-22 16:00

**Tipo de partido:** Parejo · abierto · caliente · **Favorito:** Colo Colo · primer gol: local 51 %, visitante 44 %, nadie 5 % · gol del favorito antes del 35′: 34 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 25 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

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
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 29 % |
| Sorpresa: gana el no favorito | 28 % |
| Empate | 15 % |
| Expulsión antes del 70′ | 13 % |
| Favorito gana en partido trabado | 8 % |
| Favorito golpea temprano y gana | 7 % |

## Lo que cambió el contexto
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.60 | 12.5 | 4.3 | 5.0 | 11.8 | 2.9 |
| visitante | 1.40 | 12.5 | 4.3 | 5.0 | 11.8 | 3.2 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.0) · 1–5 | 1.6 (1.6) · 0–3 | 1.4 (1.4) · 0–3 | 1.3 (1.3) · 0–3 | 1.7 (1.7) · 0–3 |
| Córners | 10.0 (10.0) · 6–14 | 5.0 · 2–9 | 4.9 · 2–8 | 4.5 (4.8) · 2–7 | 5.5 (5.3) · 3–9 |
| Tarjetas (amarilla 1, roja 2) | 6.2 (6.2) · 3–10 | 2.9 (2.9) · 1–5 | 3.2 (3.2) · 1–6 | 2.0 (2.2) · 0–4 | 4.1 · 1–7 |
| Remates | 25.1 · 18–32 | 12.6 · 7–18 | 12.5 · 7–18 | 11.2 · 7–16 | 13.8 · 9–19 |
| Tiros al arco | 8.7 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.9 · 1–7 | 4.8 · 2–8 |
| Faltas | 23.6 · 17–30 | 11.7 · 7–16 | 11.9 · 7–17 | 10.6 · 6–15 | 13.1 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.9 · 5–14 |
| Saques de banda | 39.6 · 28–52 | 19.8 · 12–28 | 19.9 · 12–28 | 17.7 · 11–24 | 22.0 · 15–30 |
| Atajadas del portero | — | 2.9 · 1–5 | 2.8 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Universidad Catolica Más 0.5 | 1.27 | 77 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (0 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: Sí | 1.55 | 63 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | No hay empate | 1.28 | 74 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners | Córners 2.º tiempo Más 3.5 | 1.26 | 78 % | 75 % | Partido abierto (ambos marcan y 3+ goles) (79 %) | Favorito golpea temprano y gana (75 %) | Alta probabilidad |
| Tarjetas | Tarjetas Más 4.5 | 1.37 | 70 % | 65 % | Expulsión antes del 70′ (95 %) | Favorito golpea temprano y gana (58 %) | Alta probabilidad |
| Quién saca más | Más corners: Universidad Catolica | 4.00 | 32 % | 26 % | Favorito golpea temprano y gana (40 %) | Sorpresa: gana el no favorito (26 %) | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 2.º tiempo Más 3.5 | 1.26 | 78 % | 77 % | 78 % | +0 pts | -2 % | 75 % | +0.8 | 1.33 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 1.er tiempo Más 3.0 | 1.37 | 78 % | 78 % | 78 % | +0 pts | +6 % | 64 % | +0.7 | 1.33 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Goles Universidad Catolica Más 0.5 | 1.27 | 77 % | 76 % | 77 % | +0 pts | -3 % | 77 % | +0.8 | 1.34 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners Universidad Catolica Más 2.5 | 1.32 | 77 % | 71 % | 77 % | +0 pts | +1 % | 73 % | +0.9 | 1.34 | Expulsión antes del 70′ | Alta probabilidad |
| Córners 1.er tiempo Menos 6.0 | 1.44 | 76 % | 74 % | 76 % | +0 pts | +10 % | 66 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Goles 2.º tiempo Menos 2.5 | 1.30 | 76 % | 75 % | 76 % | +0 pts | -2 % | 76 % | +0.6 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Menos 12.0 | 1.36 | 75 % | 75 % | 75 % | +0 pts | +3 % | 66 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| No hay empate | 1.28 | 74 % | 74 % | 74 % | +0 pts | -6 % | 74 % | — | 1.40 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Goles 1.er tiempo Más 0.5 | 1.35 | 73 % | 72 % | 73 % | +0 pts | -2 % | 73 % | +0.7 | 1.41 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners Más 8.0 | 1.44 | 72 % | 72 % | 72 % | +0 pts | +4 % | 60 % | +0.6 | 1.42 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Goles 1.er tiempo Menos 1.75 | 1.36 | 71 % | 72 % | 71 % | +0 pts | -4 % | 71 % | +0.3 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % · ★ enfoque a favor |
| Córners 2.º tiempo Menos 6.5 | 1.32 | 71 % | 73 % | 71 % | +0 pts | -7 % | 68 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Goles Menos 3.75 | 1.39 | 71 % | 71 % | 71 % | +0 pts | -2 % | 71 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Córners Menos 11.5 | 1.36 | 70 % | 71 % | 70 % | +0 pts | -5 % | 67 % | +0.5 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas Más 4.5 | 1.37 | 70 % | 70 % | 70 % | +0 pts | -4 % | 65 % | +0.6 | 1.47 | Favorito golpea temprano y gana | Alta probabilidad |
| Ambos 2+ tarjetas: Sí | 1.42 | 69 % | 68 % | 69 % | +0 pts | -2 % | 65 % | — | 1.49 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 1.er tiempo Menos 5.5 | 1.44 | 69 % | 66 % | 69 % | +0 pts | -1 % | 66 % | +0.5 | 1.50 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Colo Colo o empate | 1.44 | 68 % | 67 % | 68 % | +0 pts | -3 % | 68 % | — | 1.52 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Hándicap Colo Colo +0.5 | 1.45 | 68 % | 67 % | 68 % | +0 pts | -2 % | 68 % | — | 1.52 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Hándicap Colo Colo +1 | 1.44 | 67 % | 67 % | 67 % | +0 pts | -3 % | 68 % | — | 1.53 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Más 3.5 | 1.37 | 67 % | 70 % | 67 % | +0 pts | -8 % | 66 % | +0.5 | 1.53 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Más 0.75 | 1.47 | 67 % | 66 % | 67 % | +0 pts | -1 % | 67 % | +0.5 | 1.53 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 18 % · ★ enfoque a favor |
| Hándicap Universidad Catolica +0.75 | 1.47 | 66 % | 66 % | 66 % | +0 pts | -2 % | 66 % | — | 1.55 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |
| Córners Más 8.5 | 1.44 | 66 % | 66 % | 66 % | +0 pts | -5 % | 61 % | +0.4 | 1.57 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Goles Más 2.25 | 1.50 | 65 % | 65 % | 65 % | +0 pts | -2 % | 65 % | +0.4 | 1.58 | Empate | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Universidad Catolica Más 6.5 | 6.80 | 19 % | 14 % | 19 % | +0 pts | +30 % | 15 % | -0.6 | 5.84 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: Universidad Catolica | 4.00 | 32 % | 20 % | 32 % | +0 pts | +27 % | 26 % | — | 3.37 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Universidad Catolica Más 5.5 | 4.20 | 29 % | 22 % | 29 % | +0 pts | +24 % | 24 % | -0.2 | 3.64 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Universidad Catolica Más 7.5 | 9.75 | 13 % | 10 % | 13 % | +0 pts | +24 % | 9 % | -1.0 | 9.37 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 4.0 | 2.95 | 40 % | 37 % | 40 % | +0 pts | +17 % | 32 % | -0.2 | 2.66 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 5.0 | 1.93 | 60 % | 57 % | 60 % | +0 pts | +15 % | 49 % | +0.2 | 1.73 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners Universidad Catolica Más 4.5 | 2.65 | 44 % | 35 % | 44 % | +0 pts | +15 % | 39 % | +0.2 | 2.41 | Sorpresa: gana el no favorito | Valor · ⚠ Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Menos 6.0 | 1.44 | 76 % | 74 % | 76 % | +0 pts | +10 % | 66 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners Universidad Catolica Más 3.5 | 1.78 | 60 % | 52 % | 60 % | +0 pts | +7 % | 56 % | +0.5 | 1.72 | Expulsión antes del 70′ | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Menos 10.0 | 2.02 | 53 % | 52 % | 53 % | +0 pts | +6 % | 43 % | +0.0 | 1.97 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 12 % |
| Córners 1.er tiempo Más 3.0 | 1.37 | 78 % | 78 % | 78 % | +0 pts | +6 % | 64 % | +0.7 | 1.33 | Favorito gana en partido trabado | Alta probabilidad · Valor · asiática: devuelve 17 % |
| Córners 1.er tiempo Más 4.0 | 1.82 | 58 % | 61 % | 58 % | +0 pts | +6 % | 46 % | +0.2 | 1.77 | Favorito gana en partido trabado | Valor · asiática: devuelve 19 % |
| Córners 1.er tiempo Menos 7.0 | 1.21 | 87 % | 84 % | 87 % | +0 pts | +5 % | 79 % | +1.2 | 1.19 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 8 % |
| Córners Más 10.0 | 2.25 | 47 % | 47 % | 47 % | +0 pts | +5 % | 38 % | -0.0 | 2.24 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Más 9.0 | 1.75 | 60 % | 60 % | 60 % | +0 pts | +5 % | 50 % | +0.3 | 1.73 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Menos 11.0 | 1.60 | 65 % | 65 % | 65 % | +0 pts | +4 % | 56 % | +0.3 | 1.58 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Córners Más 8.0 | 1.44 | 72 % | 72 % | 72 % | +0 pts | +4 % | 60 % | +0.6 | 1.42 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners Universidad Catolica Más 6.5 1.3 % de la banca; Más corners: Universidad Catolica 2.2 % de la banca; Córners Universidad Catolica Más 5.5 1.8 % de la banca; Córners Universidad Catolica Más 7.5 0.7 % de la banca; Córners 1.er tiempo Menos 4.0 2.1 % de la banca; Córners 1.er tiempo Menos 5.0 4.1 % de la banca; Córners Universidad Catolica Más 4.5 2.3 % de la banca; Córners 1.er tiempo Menos 6.0 5.6 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Córners 2.º tiempo Más 2.5 + Tarjetas Más 4.5 | 62 % | 62 % | 57 % | 1.63 | 1.67 | 1.07 | 8 % | Expulsión antes del 70′ | 58 % |
| Goles Más 0.5 + Ambos marcan: Sí | 62 % | 64 % | 57 % | 1.60 | 1.65 | 1.05 | 6 % | Partido abierto (ambos marcan y 3+ goles) | 57 % |
| Goles Más 0.5 + Córners Menos 15.5 + Ambos marcan: Sí | 61 % | 60 % | 56 % | 1.65 | 1.70 | 1.08 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 54 % |
| Ambos 1+ tarjetas: Sí + Goles Universidad Catolica Menos 3.5 + Colo Colo o empate | 62 % | 63 % | 57 % | 1.62 | 1.67 | 1.05 | 6 % | Empate | 0 % |
| Hándicap Universidad Catolica +3 + Córners Menos 15.5 + Tarjetas Más 4.5 | 62 % | 62 % | 58 % | 1.61 | 1.66 | 1.02 | 7 % | Expulsión antes del 70′ | 58 % |
| Córners 2.º tiempo Más 2.5 + Goles Universidad Catolica Menos 3.5 + Colo Colo o empate | 60 % | 61 % | 56 % | 1.66 | 1.71 | 1.04 | 6 % | Favorito gana en partido trabado | 0 % |
| Tarjetas 1.er tiempo Menos 2.5 + Goles 1.er tiempo Menos 3.5 | 61 % | 63 % | 56 % | 1.63 | 1.68 | 1.0 | 6 % | Favorito golpea temprano y gana | 31 % |
| Tarjetas 1.er tiempo Menos 2.5 + Córners 1.er tiempo Menos 8.5 | 61 % | 64 % | 56 % | 1.64 | 1.69 | 1.0 | 6 % | Favorito golpea temprano y gana | 31 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.