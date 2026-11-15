# Bélgica - Italia
UEFA Liga de Naciones · 2026-11-15 14:45

**Tipo de partido:** Parejo · abierto · caliente · **Favorito:** Bélgica · primer gol: local 52 %, visitante 43 %, nadie 5 % · gol del favorito antes del 35′: 34 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

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
| Empate | 16 % |
| Expulsión antes del 70′ | 10 % |
| Favorito golpea temprano y gana | 8 % |
| Favorito gana en partido trabado | 8 % |

## Lo que cambió el contexto
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.61 | 15.7 | 5.1 | 4.7 | 11.5 | 2.4 |
| visitante | 1.39 | 13.7 | 4.6 | 5.0 | 13.0 | 2.4 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.0) · 1–5 | 1.6 (1.6) · 0–3 | 1.4 (1.4) · 0–3 | 1.3 (1.3) · 0–3 | 1.7 (1.7) · 0–3 |
| Córners | 9.6 (9.5) · 6–14 | 4.6 (4.7) · 2–8 | 5.0 (5.0) · 2–8 | 4.3 (4.6) · 2–7 | 5.3 (5.0) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 4.8 (4.8) · 2–8 | 2.4 (2.4) · 1–4 | 2.4 (2.4) · 1–4 | 1.6 (1.7) · 0–3 | 3.2 · 1–6 |
| Remates | 29.3 (29.3) · 22–37 | 15.7 (15.7) · 10–22 | 13.6 (13.7) · 8–20 | 13.1 · 8–18 | 16.2 · 11–22 |
| Tiros al arco | 9.7 (9.7) · 6–14 | 5.1 (5.1) · 2–8 | 4.6 (4.6) · 2–8 | 4.3 (4.5) · 2–7 | 5.3 · 2–8 |
| Faltas | 24.6 (24.5) · 18–31 | 11.5 (11.5) · 7–16 | 13.1 (13.0) · 8–18 | 11.0 · 7–15 | 13.6 · 9–19 |
| Fueras de lugar | 2.9 (2.9) · 1–5 | 1.2 (1.2) · 0–3 | 1.7 (1.7) · 0–4 | 1.3 (1.5) · 0–3 | 1.6 · 0–3 |
| Saques de meta | 15.2 (15.0) · 9–22 | 6.8 (6.8) · 3–11 | 8.4 (8.4) · 4–13 | 6.7 (7.0) · 3–11 | 8.5 · 4–13 |
| Saques de banda | 30.6 (30.2) · 21–41 | 15.3 (15.2) · 9–22 | 15.3 (15.2) · 9–22 | 13.7 (15.9) · 8–19 | 16.9 · 11–24 |
| Atajadas del portero | — | 3.2 · 1–6 | 3.5 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 2.º tiempo Menos 2.5 | 1.29 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (56 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: Sí | 1.57 | 62 % | (lo define el marcador) | Partido abierto (ambos marcan y 3+ goles) (100 %) | Favorito golpea temprano y gana (0 %) | Justa · ★ enfoque a favor |
| Resultado y hándicap | Hándicap Italia +2 | 1.25 | 79 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (29 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 2.º tiempo Más 3.5 | 1.31 | 75 % | 75 % | Partido abierto (ambos marcan y 3+ goles) (77 %) | Favorito golpea temprano y gana (71 %) | Alta probabilidad |
| Tarjetas | Tarjetas Menos 6.5 | 1.26 | 77 % | 78 % | Favorito golpea temprano y gana (86 %) | Expulsión antes del 70′ (41 %) | Alta probabilidad |
| Faltas | Faltas Italia Más 12.5 | 1.75 | 54 % | 52 % | Expulsión antes del 70′ (57 %) | Favorito golpea temprano y gana (49 %) | Cara |
| Remates | Remates Italia Menos 14.5 | 1.55 | 61 % | 55 % | Favorito gana en partido trabado (73 %) | Partido abierto (ambos marcan y 3+ goles) (55 %) | Cara |
| Tiros al arco | Tiros al arco Bélgica Menos 6.5 | 1.29 | 74 % | 59 % | Empate (86 %) | Partido abierto (ambos marcan y 3+ goles) (59 %) | Alta probabilidad |
| Fueras de lugar | Fueras de lugar Bélgica Más 0.5 | 1.42 | 67 % | 66 % | Sorpresa: gana el no favorito (69 %) | Favorito golpea temprano y gana (65 %) | Alta probabilidad |
| Saques de meta | Saques de meta Más 14.5 | 1.82 | 52 % | 51 % | Expulsión antes del 70′ (58 %) | Favorito gana en partido trabado (49 %) | Cara |
| Saques de banda | Saques de banda 1.er tiempo Menos 15.5 | 1.91 | 58 % | 58 % | Favorito gana en partido trabado (60 %) | Partido abierto (ambos marcan y 3+ goles) (58 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jugadores | Riccardo Calafiori anota o asiste | 5.90 | 16 % | 9 % | Sorpresa: gana el no favorito (28 %) | Favorito golpea temprano y gana (0 %) | Justa |
| Parejas de jugadores | Youri Tielemans o Romeo Lavia (da una asistencia) | 3.55 | 27 % | 14 % | Partido abierto (ambos marcan y 3+ goles) (42 %) | Empate (14 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hándicap Italia +2 | 1.25 | 79 % | 78 % | 79 % | +0 pts | -1 % | 79 % | — | 1.31 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Tarjetas Menos 6.5 | 1.26 | 77 % | 77 % | 77 % | +0 pts | -3 % | 78 % | +0.7 | 1.34 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -2 % | 76 % | +0.7 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas 1.er tiempo Menos 2.5 | 1.31 | 76 % | 74 % | 76 % | +0 pts | -1 % | 79 % | +0.7 | 1.36 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Italia Menos 6.5 | 1.26 | 76 % | 77 % | 76 % | +0 pts | -4 % | 72 % | +0.6 | 1.36 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Italia Más 0.5 | 1.29 | 75 % | 75 % | 75 % | +0 pts | -3 % | 76 % | +0.8 | 1.36 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners 2.º tiempo Más 3.5 | 1.31 | 75 % | 74 % | 75 % | +0 pts | -2 % | 75 % | +0.7 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 11.5 | 1.28 | 75 % | 76 % | 75 % | +0 pts | -5 % | 72 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| No hay empate | 1.26 | 74 % | 76 % | 74 % | +0 pts | -6 % | 74 % | — | 1.38 | Empate | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners 2.º tiempo Menos 6.5 | 1.26 | 74 % | 77 % | 74 % | +0 pts | -6 % | 72 % | +0.5 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Bélgica Menos 6.5 | 1.29 | 74 % | 75 % | 74 % | +0 pts | -4 % | 59 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 7.5 | 1.31 | 73 % | 74 % | 73 % | +0 pts | -4 % | 73 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.34 | 73 % | 72 % | 73 % | +0 pts | -3 % | 73 % | +0.7 | 1.42 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Menos 5.5 | 1.38 | 72 % | 70 % | 72 % | +0 pts | -1 % | 70 % | +0.6 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles Menos 3.75 | 1.38 | 71 % | 71 % | 71 % | +0 pts | -2 % | 71 % | +0.4 | 1.45 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Kevin De Bruyne entradas 1+ | 1.25 | 71 % | 71 % | 71 % | +0 pts | -11 % | 66 % | — | 1.45 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Goles 1.er tiempo Menos 1.75 | 1.37 | 71 % | 71 % | 71 % | +0 pts | -3 % | 71 % | +0.4 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % · ★ enfoque a favor |
| Córners Italia Más 3.5 | 1.34 | 70 % | 72 % | 70 % | +0 pts | -6 % | 66 % | +0.6 | 1.47 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Hans Vanaken entradas 1+ | 1.25 | 70 % | 71 % | 70 % | +0 pts | -12 % | 66 % | — | 1.47 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Issa Doumbia remates 1+ | 1.27 | 70 % | 70 % | 70 % | +0 pts | -11 % | 69 % | — | 1.47 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Maxim De Cuyper remates 1+ | 1.27 | 70 % | 70 % | 70 % | +0 pts | -11 % | 68 % | — | 1.48 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Samuele Ricci faltas cometidas 1+ | 1.26 | 70 % | 71 % | 70 % | +0 pts | -12 % | 69 % | — | 1.48 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa |
| Nathan Ngoy entradas 1+ | 1.28 | 70 % | 70 % | 70 % | +0 pts | -11 % | 64 % | — | 1.48 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Tarjetas Bélgica Más 1.5 | 1.39 | 69 % | 69 % | 69 % | +0 pts | -3 % | 66 % | +0.6 | 1.48 | Favorito golpea temprano y gana | Alta probabilidad |
| Kevin De Bruyne tiros al arco 1+ | 1.27 | 69 % | 70 % | 69 % | +0 pts | -12 % | 63 % | — | 1.48 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Saques de banda 1.er tiempo Menos 15.5 | 1.91 | 58 % | 49 % | 58 % | +0 pts | +12 % | 58 % | +0.4 | 1.77 | Partido abierto (ambos marcan y 3+ goles) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |

Kelly ¼ (dato informativo, no una orden de stake): Saques de banda 1.er tiempo Menos 15.5 3.2 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Hándicap Bélgica +2 + Goles Menos 5.5 + Bélgica o empate | 62 % | 64 % | 57 % | 1.62 | 1.67 | 1.14 | 6 % | Empate | 0 % |
| Hándicap Bélgica +2 + Goles Bélgica Menos 3.5 + Bélgica o empate | 60 % | 62 % | 56 % | 1.66 | 1.71 | 1.11 | 7 % | Empate | 0 % |
| Ambos 1+ tarjetas: Sí + Goles 2.º tiempo Menos 2.5 + Tarjetas Más 2.5 | 59 % | 61 % | 55 % | 1.70 | 1.75 | 1.12 | 8 % | Empate | 42 % |
| Córners 1.er tiempo Menos 8.5 + Ambos 1+ tarjetas: Sí + Goles 2.º tiempo Menos 2.5 | 62 % | 63 % | 58 % | 1.62 | 1.67 | 1.0 | 6 % | Empate | 44 % |
| Fueras de lugar 1.er tiempo Menos 1.5 + Córners 1.er tiempo Menos 8.5 | 59 % | 62 % | 54 % | 1.69 | 1.74 | 1.0 | 6 % | Favorito gana en partido trabado | 58 % |
| Fueras de lugar 1.er tiempo Menos 1.5 + Córners 2.º tiempo Más 1.5 | 59 % | 62 % | 54 % | 1.70 | 1.75 | 1.0 | 6 % | Favorito gana en partido trabado | 58 % |
| Saques de banda 1.er tiempo Menos 15.5 + Córners 2.º tiempo Más 1.5 | 56 % | 66 % | 51 % | 1.78 | 1.83 | 1.0 | 8 % | Favorito gana en partido trabado | 56 % |
| ↳ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |  |  |  |  |  |  |  |  |  |
| Saques de banda 1.er tiempo Menos 15.5 + Goles 1.er tiempo Menos 3.5 | 56 % | 65 % | 51 % | 1.79 | 1.84 | 1.0 | 8 % | Favorito gana en partido trabado | 53 % |
| ↳ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.