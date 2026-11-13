# Eslovenia - Suiza
UEFA Liga de Naciones · 2026-11-13 14:45

**Tipo de partido:** Favorito leve · cerrado · normal · **Favorito:** Suiza · primer gol: local 28 %, visitante 60 %, nadie 13 % · gol del favorito antes del 35′: 34 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 44 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso. Poco favorecidos: Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Resultado / hándicap | ➖ neutro | Suiza favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; los dos se juegan algo importante |
| Líneas de jugador | ➖ neutro | se pueden mirar con la alineación de la ficha |
| Ambos marcan | ⛔ en contra | Eslovenia marca poco en este partido |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Empate | 23 % |
| Favorito gana en partido trabado | 18 % |
| Partido abierto (ambos marcan y 3+ goles) | 18 % |
| Favorito golpea temprano y gana | 17 % |
| Sorpresa: gana el no favorito | 16 % |
| Expulsión antes del 70′ | 9 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 0.65 | 12.8 | 4.3 | 4.4 | 12.3 | 2.4 |
| visitante | 1.36 | 12.8 | 4.3 | 4.4 | 12.3 | 1.8 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.0 (2.1) · 0–4 | 0.7 (0.7) · 0–2 | 1.4 (1.4) · 0–3 | 0.9 (0.9) · 0–2 | 1.1 (1.1) · 0–2 |
| Córners | 8.9 (8.7) · 5–13 | 4.4 · 2–8 | 4.5 · 2–8 | 3.9 (3.9) · 1–7 | 5.0 (4.6) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 4.3 (4.0) · 2–7 | 2.5 (2.3) · 1–4 | 1.8 (1.7) · 0–4 | 1.4 (1.4) · 0–3 | 2.9 · 1–5 |
| Remates | 25.7 · 19–33 | 12.9 · 7–19 | 12.8 · 8–18 | 11.3 · 7–16 | 14.3 · 9–20 |
| Tiros al arco | 8.7 · 5–13 | 4.3 · 2–8 | 4.3 · 2–7 | 3.9 · 1–7 | 4.8 · 2–8 |
| Faltas | 24.7 · 18–31 | 12.3 · 8–17 | 12.4 · 8–17 | 11.1 · 7–15 | 13.6 · 9–19 |
| Fueras de lugar | 3.7 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.1 · 0–4 |
| Saques de meta | 15.9 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.1 · 3–11 | 8.8 · 5–14 |
| Saques de banda | 39.6 · 28–52 | 19.8 · 12–28 | 19.8 · 12–28 | 17.7 · 11–24 | 22.0 · 15–30 |
| Atajadas del portero | — | 3.0 · 1–6 | 3.7 · 1–7 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Menos 1.5 | 1.29 | 76 % | (lo define el marcador) | Favorito gana en partido trabado (98 %) | Partido abierto (ambos marcan y 3+ goles) (44 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: No | 1.55 | 63 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Justa |
| Resultado y hándicap | Hándicap Eslovenia +2 | 1.32 | 74 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Favorito golpea temprano y gana (34 %) | Alta probabilidad |
| Córners | Córners 1.er tiempo Más 1.5 | 2.02 | 68 % | 67 % | Partido abierto (ambos marcan y 3+ goles) (69 %) | Expulsión antes del 70′ (67 %) | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 44 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Tarjetas | Ambos 1+ tarjetas: Sí | 1.29 | 79 % | 75 % | Expulsión antes del 70′ (87 %) | Favorito golpea temprano y gana (75 %) | Alta probabilidad |
| Jugadores | Jost Urbancic anota o asiste | 9.00 | 14 % | 0 % | Sorpresa: gana el no favorito (32 %) | Favorito golpea temprano y gana (0 %) | Valor frágil (depende de un guion) |
| Quién saca más | Más tarjetas: Eslovenia | 1.82 | 52 % | 50 % | Expulsión antes del 70′ (56 %) | Favorito golpea temprano y gana (50 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí | 1.29 | 79 % | 75 % | 76 % | +3 pts | +2 % | 75 % | — | 1.31 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners 1.er tiempo Menos 5.5 | 1.27 | 77 % | 76 % | 77 % | -0 pts | -2 % | 75 % | +0.8 | 1.33 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 6.5 | 1.26 | 77 % | 77 % | 76 % | +1 pts | -2 % | 74 % | +0.8 | 1.33 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles 1.er tiempo Menos 1.5 | 1.29 | 76 % | 75 % | 76 % | +0 pts | -1 % | 76 % | +0.6 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Goles Suiza Más 0.5 | 1.27 | 75 % | 76 % | 76 % | -1 pts | -4 % | 75 % | +0.8 | 1.37 | Sorpresa: gana el no favorito | Alta probabilidad |
| Goles Menos 2.75 | 1.35 | 74 % | 73 % | 73 % | +1 pts | -0 % | 74 % | +0.5 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % · ★ enfoque a favor |
| Hándicap Eslovenia +2 | 1.32 | 74 % | 74 % | 74 % | -0 pts | -3 % | 74 % | — | 1.40 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Menos 10.5 | 1.29 | 72 % | 75 % | 74 % | -1 pts | -7 % | 70 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| No hay empate | 1.32 | 72 % | 71 % | 71 % | +1 pts | -5 % | 72 % | — | 1.43 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Córners Eslovenia Más 2.5 | 1.47 | 72 % | 64 % | 70 % | +1 pts | +5 % | 69 % | +0.8 | 1.44 | Expulsión antes del 70′ | Alta probabilidad · Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Goles 1.er tiempo Menos 1.25 | 1.39 | 71 % | 70 % | 71 % | +0 pts | -1 % | 71 % | +0.4 | 1.44 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 18 % · ★ enfoque a favor |
| Córners 2.º tiempo Más 3.5 | 1.44 | 70 % | 67 % | 68 % | +2 pts | +1 % | 66 % | +0.6 | 1.47 | Favorito golpea temprano y gana | Alta probabilidad |
| Hándicap Eslovenia +1.25 | 1.40 | 70 % | 70 % | 70 % | -0 pts | -2 % | 70 % | — | 1.48 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 14 % |
| Goles Más 1.25 | 1.39 | 70 % | 71 % | 71 % | -1 pts | -3 % | 70 % | +0.5 | 1.48 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 14 % |
| Goles 2.º tiempo Menos 1.5 | 1.42 | 70 % | 68 % | 68 % | +1 pts | -1 % | 70 % | +0.4 | 1.48 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Córners Suiza Más 3.5 | 1.25 | 68 % | 75 % | 68 % | +0 pts | -15 % | 59 % | +0.4 | 1.52 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Córners 1.er tiempo Más 1.5 | 2.02 | 68 % | 46 % | 68 % | -0 pts | +37 % | 67 % | +1.2 | 1.52 | Expulsión antes del 70′ | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 44 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Goles 2.º tiempo Más 0.5 | 1.42 | 68 % | 68 % | 68 % | -0 pts | -4 % | 68 % | +0.6 | 1.52 | Empate | Alta probabilidad |
| Goles Menos 2.5 | 1.47 | 67 % | 66 % | 66 % | +1 pts | -1 % | 67 % | +0.3 | 1.54 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Córners 2.º tiempo Menos 5.5 | 1.37 | 65 % | 70 % | 67 % | -2 pts | -10 % | 63 % | +0.2 | 1.58 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 7.5 | 1.50 | 65 % | 64 % | 64 % | +2 pts | -2 % | 62 % | +0.4 | 1.59 | Expulsión antes del 70′ | Alta probabilidad |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 3.5 | 1.72 | 59 % | 55 % | 55 % | +5 pts | +2 % | 51 % | +0.3 | 1.74 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) |
| Ambos 2+ tarjetas: Sí | 2.40 | 42 % | 38 % | 38 % | +4 pts | +2 % | 36 % | — | 2.47 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) |
| Tarjetas Suiza Más 1.5 | 1.85 | 54 % | 51 % | 50 % | +4 pts | +1 % | 49 % | +0.2 | 1.91 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Más 1.5 | 2.02 | 68 % | 46 % | 68 % | -0 pts | +37 % | 67 % | +1.2 | 1.52 | Expulsión antes del 70′ | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 44 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Eslovenia Más 5.5 | 5.70 | 24 % | 16 % | 22 % | +1 pts | +35 % | 20 % | -0.4 | 4.61 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: Eslovenia | 3.85 | 33 % | 21 % | 32 % | +1 pts | +27 % | 28 % | — | 3.22 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 23 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jost Urbancic anota o asiste | 9.00 | 14 % | 10 % | 14 % | -0 pts | +26 % | 0 % | — | 8.36 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners Eslovenia Más 4.5 | 3.40 | 36 % | 27 % | 35 % | +1 pts | +24 % | 33 % | -0.0 | 2.91 | Expulsión antes del 70′ | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Srdjan Kuzmic anota o asiste | 9.00 | 13 % | 10 % | 13 % | -0 pts | +19 % | 0 % | — | 8.87 | Favorito golpea temprano y gana | Valor frágil (depende de un guion) |
| Córners Eslovenia Más 3.5 | 2.12 | 54 % | 44 % | 52 % | +2 pts | +14 % | 50 % | +0.4 | 1.94 | Expulsión antes del 70′ | Valor · ⚠ Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners 1.er tiempo Más 0.5 | 1.23 | 88 % | 79 % | 88 % | +0 pts | +9 % | 88 % | +1.7 | 1.17 | Expulsión antes del 70′ | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Eslovenia Más 2.5 | 1.47 | 72 % | 64 % | 70 % | +1 pts | +5 % | 69 % | +0.8 | 1.44 | Expulsión antes del 70′ | Alta probabilidad · Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Más 1.5 9.0 % de la banca; Córners Eslovenia Más 5.5 1.9 % de la banca; Más corners: Eslovenia 2.4 % de la banca; Jost Urbancic anota o asiste 0.8 % de la banca; Córners Eslovenia Más 4.5 2.5 % de la banca; Srdjan Kuzmic anota o asiste 0.6 % de la banca; Córners Eslovenia Más 3.5 3.1 % de la banca; Córners 1.er tiempo Más 0.5 9.4 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Goles Eslovenia Menos 1.5 + Suiza o empate + Descanso o final: Suiza | 55 % | 56 % | 51 % | 1.80 | 1.86 | 1.31 | 11 % | Favorito golpea temprano y gana | 0 % |
| Suiza o empate + Descanso o final: Suiza | 59 % | 59 % | 54 % | 1.71 | 1.76 | 1.19 | 9 % | Favorito golpea temprano y gana | 0 % |
| Goles Menos 3.5 + Ambos marcan: No | 61 % | 61 % | 56 % | 1.64 | 1.69 | 1.13 | 6 % | Favorito gana en partido trabado | 0 % |
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí | 56 % | 57 % | 51 % | 1.78 | 1.83 | 1.2 | 9 % | Expulsión antes del 70′ | 48 % |
| Goles 2.º tiempo Menos 2.5 + Ambos marcan: No | 61 % | 62 % | 57 % | 1.63 | 1.68 | 1.08 | 6 % | Favorito golpea temprano y gana | 0 % |
| Tarjetas Más 3.5 + Ambos 1+ tarjetas: Sí + Goles Suiza Menos 3.5 | 54 % | 55 % | 50 % | 1.85 | 1.90 | 1.21 | 10 % | Expulsión antes del 70′ | 45 % |
| Goles Suiza Menos 3.5 + Hándicap Eslovenia +3 + Córners Suiza Más 3.5 | 61 % | 55 % | 57 % | 1.63 | 1.68 | 1.04 | 9 % | Sorpresa: gana el no favorito | 42 % |
| Córners Eslovenia Más 2.5 + Goles 1.er tiempo Menos 2.5 + Hándicap Eslovenia +3 | 62 % | 68 % | 57 % | 1.62 | 1.67 | 1.02 | 10 % | Empate | 52 % |
| ↳ Línea contra el guion (Más de un equipo que perdió: 2/11) |  |  |  |  |  |  |  |  |  |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.