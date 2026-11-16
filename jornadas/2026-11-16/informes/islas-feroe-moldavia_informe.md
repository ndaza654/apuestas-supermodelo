# Islas Feroé - Moldavia
UEFA Liga de Naciones · 2026-11-16 10:00

**Tipo de partido:** Favorito leve · cerrado · normal · **Favorito:** Islas Feroé · primer gol: local 61 %, visitante 30 %, nadie 10 % · gol del favorito antes del 35′: 35 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso. Poco favorecidos: Ambos marcan.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Resultado / hándicap | ➖ neutro | Islas Feroé favorito leve: el precio ya lo recoge |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Ambos marcan | ⛔ en contra | Moldavia marca poco en este partido |
| Tarjetas y faltas | ❔ sin señal | árbitro sin dato |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 22 % |
| Empate | 19 % |
| Favorito gana en partido trabado | 16 % |
| Sorpresa: gana el no favorito | 16 % |
| Favorito golpea temprano y gana | 16 % |
| Expulsión antes del 70′ | 11 % |

## Lo que cambió el contexto
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.52 | 12.5 | 4.3 | 4.8 | 11.8 | 2.1 |
| visitante | 0.79 | 12.5 | 4.3 | 4.8 | 11.8 | 2.9 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.3 (2.3) · 1–4 | 1.5 (1.5) · 0–3 | 0.8 (0.8) · 0–2 | 1.0 (1.1) · 0–2 | 1.3 (1.3) · 0–3 |
| Córners | 9.5 (9.6) · 6–14 | 4.7 · 2–8 | 4.8 · 2–8 | 4.3 (4.7) · 2–7 | 5.3 (5.1) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.0 (5.0) · 2–8 | 2.1 (2.1) · 0–4 | 2.9 (2.9) · 1–5 | 1.7 (1.8) · 0–3 | 3.3 · 1–6 |
| Remates | 25.1 · 18–32 | 12.6 · 7–18 | 12.6 · 7–18 | 11.2 · 7–16 | 14.0 · 9–19 |
| Tiros al arco | 8.7 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.9 · 1–6 | 4.8 · 2–8 |
| Faltas | 23.7 · 18–30 | 11.9 · 8–16 | 11.9 · 8–16 | 10.6 · 7–15 | 13.1 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 15.8 · 10–23 | 7.9 · 4–13 | 7.9 · 4–13 | 7.1 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 39.9 · 29–52 | 19.9 · 12–28 | 20.0 · 12–28 | 17.8 · 11–25 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.6 · 1–6 | 2.8 · 1–5 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 3.0 | 1.32 | 76 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Alta probabilidad · asiática: devuelve 21 % · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: No | 1.67 | 56 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Cara |
| Resultado y hándicap | No hay empate | 1.29 | 74 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad |
| Córners | Córners Moldavia Más 2.5 | 1.27 | 78 % | 75 % | Favorito golpea temprano y gana (82 %) | Expulsión antes del 70′ (72 %) | Alta probabilidad |
| Tarjetas | Tarjetas Islas Feroé Más 1.5 | 1.53 | 62 % | 56 % | Expulsión antes del 70′ (82 %) | Favorito golpea temprano y gana (56 %) | Justa |
| Quién saca más | Más tarjetas: Moldavia | 1.72 | 55 % | 53 % | Expulsión antes del 70′ (60 %) | Favorito golpea temprano y gana (53 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Moldavia Más 2.5 | 1.27 | 78 % | 74 % | 78 % | +0 pts | -1 % | 75 % | +0.9 | 1.33 | Expulsión antes del 70′ | Alta probabilidad |
| Goles Menos 3.0 | 1.32 | 76 % | 75 % | 75 % | +1 pts | -0 % | 76 % | +0.5 | 1.36 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 21 % · ★ enfoque a favor |
| Córners 2.º tiempo Más 3.5 | 1.32 | 75 % | 73 % | 75 % | +1 pts | -1 % | 73 % | +0.8 | 1.37 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Menos 11.5 | 1.29 | 75 % | 75 % | 74 % | +1 pts | -3 % | 73 % | +0.6 | 1.38 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 2.º tiempo Menos 6.5 | 1.26 | 74 % | 77 % | 75 % | -0 pts | -6 % | 72 % | +0.5 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · cuota por debajo de la justa |
| No hay empate | 1.29 | 74 % | 73 % | 73 % | +1 pts | -4 % | 74 % | — | 1.39 | Empate | Alta probabilidad |
| Hándicap Moldavia +2 | 1.34 | 74 % | 72 % | 72 % | +1 pts | -1 % | 74 % | — | 1.40 | Favorito golpea temprano y gana | Alta probabilidad |
| Hándicap Moldavia +1.5 | 1.36 | 73 % | 72 % | 72 % | +1 pts | -0 % | 73 % | — | 1.40 | Favorito golpea temprano y gana | Alta probabilidad |
| Córners Más 7.5 | 1.30 | 73 % | 74 % | 73 % | -0 pts | -5 % | 72 % | +0.6 | 1.41 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Menos 1.5 | 1.36 | 72 % | 71 % | 72 % | +1 pts | -1 % | 72 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Goles 2.º tiempo Más 0.5 | 1.35 | 72 % | 72 % | 72 % | +1 pts | -2 % | 72 % | +0.7 | 1.42 | Empate | Alta probabilidad |
| Córners 1.er tiempo Menos 5.5 | 1.40 | 72 % | 69 % | 71 % | +1 pts | +1 % | 71 % | +0.6 | 1.43 | Sorpresa: gana el no favorito | Alta probabilidad |
| Hándicap Moldavia +1.25 | 1.44 | 69 % | 68 % | 68 % | +1 pts | -1 % | 69 % | — | 1.49 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 15 % |
| Goles Menos 2.75 | 1.47 | 67 % | 66 % | 66 % | +1 pts | -2 % | 67 % | +0.3 | 1.54 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 11 % · ★ enfoque a favor |
| Goles Más 1.5 | 1.44 | 67 % | 67 % | 67 % | -1 pts | -4 % | 67 % | +0.5 | 1.55 | Favorito gana en partido trabado | Alta probabilidad |
| Goles 1.er tiempo Menos 1.25 | 1.50 | 66 % | 65 % | 65 % | +1 pts | -1 % | 66 % | +0.2 | 1.56 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 18 % · ★ enfoque a favor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Moldavia Más 6.5 | 5.90 | 19 % | 16 % | 20 % | -0 pts | +14 % | 15 % | -0.7 | 5.78 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Más corners: Moldavia | 3.10 | 36 % | 27 % | 36 % | +0 pts | +13 % | 30 % | — | 2.92 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Moldavia Más 5.5 | 3.70 | 30 % | 25 % | 30 % | -0 pts | +12 % | 26 % | -0.3 | 3.55 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · Línea contra el guion (Más de un equipo que perdió: 2/11) |
| Córners Moldavia Más 4.5 | 2.37 | 44 % | 39 % | 45 % | -0 pts | +5 % | 40 % | +0.1 | 2.36 | Sorpresa: gana el no favorito | Valor · Línea contra el guion (Más de un equipo que perdió: 2/11) |

Kelly ¼ (dato informativo, no una orden de stake): Córners Moldavia Más 6.5 0.7 % de la banca; Más corners: Moldavia 1.5 % de la banca; Córners Moldavia Más 5.5 1.1 % de la banca; Córners Moldavia Más 4.5 0.9 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Gana Islas Feroé + Descanso o final: Islas Feroé | 55 % | 56 % | 50 % | 1.82 | 1.88 | 1.61 | 9 % | Favorito golpea temprano y gana | 0 % |
| Goles Más 0.5 + Gana Islas Feroé + Descanso o final: Islas Feroé | 55 % | 56 % | 50 % | 1.82 | 1.88 | 1.78 | 11 % | Favorito golpea temprano y gana | 0 % |
| Ambos 1+ tarjetas: Sí + Tarjetas Islas Feroé Más 1.5 | 60 % | 61 % | 55 % | 1.67 | 1.72 | 1.14 | 7 % | Expulsión antes del 70′ | 53 % |
| Goles Islas Feroé Menos 3.5 + Ambos 1+ tarjetas: Sí + Tarjetas Islas Feroé Más 1.5 | 57 % | 58 % | 53 % | 1.74 | 1.79 | 1.16 | 8 % | Expulsión antes del 70′ | 49 % |
| Córners 1.er tiempo Menos 5.5 + Goles 2.º tiempo Menos 2.5 | 62 % | 64 % | 58 % | 1.60 | 1.65 | 1.0 | 6 % | Empate | 45 % |
| Goles 2.º tiempo Menos 2.5 + Ambos marcan: No | 54 % | 54 % | 50 % | 1.84 | 1.89 | 1.11 | 8 % | Favorito golpea temprano y gana | 0 % |
| Goles 1.er tiempo Menos 2.5 + Ambos marcan: No | 55 % | 55 % | 50 % | 1.82 | 1.87 | 1.06 | 7 % | Favorito gana en partido trabado | 0 % |
| Hándicap Moldavia +1.5 + Goles Islas Feroé Menos 3.5 + Córners 2.º tiempo Más 3.5 | 55 % | 56 % | 51 % | 1.82 | 1.87 | 1.06 | 7 % | Empate | 23 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.