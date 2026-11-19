# Paris FC (F) - HB Koge (F)
UEFA Clubs Champions League (F) · 2026-11-19 12:45

**Tipo de partido:** Favorito claro · abierto · normal · **Favorito:** Paris FC (F) · primer gol: local 66 %, visitante 31 %, nadie 3 % · gol del favorito antes del 35′: 45 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), Ambos marcan, Hándicap y victoria de Paris FC (F), Goles de Paris FC (F) (Más), Remates / tiros al arco de Paris FC (F).

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Hándicap y victoria de Paris FC (F) | ✅ favorece | favorito claro: manda en el marcador y en el territorio |
| Goles de Paris FC (F) (Más) | ✅ favorece | favorito claro contra rival que sufre |
| Remates / tiros al arco de Paris FC (F) | ✅ favorece | el que domina remata más |
| Córners totales | ➖ neutro | si el favorito marca pronto, sus córners se apagan; si el rival forzara, suben |
| Tarjetas y faltas | ➖ neutro | árbitro sin dato; los dos se juegan algo importante; favorito claro: poca fricción y, si hay goleada, menos tarjetas |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 39 % |
| Sorpresa: gana el no favorito | 16 % |
| Favorito golpea temprano y gana | 16 % |
| Favorito gana en partido trabado | 12 % |
| Empate | 11 % |
| Expulsión antes del 70′ | 7 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro con promedio pero sin media de la liga (ni en la ficha ni en el prior): tarjetas en neutro.
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 2.10 | 12.5 | 4.3 | 4.8 | 12.1 | 1.0 |
| visitante | 1.10 | 12.5 | 4.3 | 4.8 | 12.1 | 1.5 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.2 (3.3) · 1–6 | 2.1 (2.2) · 0–4 | 1.1 (1.1) · 0–2 | 1.4 (1.4) · 0–3 | 1.8 (1.9) · 0–4 |
| Córners | 9.7 (9.7) · 6–14 | 4.9 · 2–8 | 4.8 · 2–8 | 4.3 (4.8) · 2–7 | 5.4 (5.2) · 2–9 |
| Tarjetas (amarilla 1, roja 2) | 2.4 (2.3) · 0–5 | 1.0 (0.9) · 0–2 | 1.5 (1.4) · 0–3 | 0.9 (0.8) · 0–2 | 1.6 · 0–3 |
| Remates | 25.0 · 18–32 | 12.5 · 8–18 | 12.5 · 7–18 | 11.1 · 7–16 | 14.0 · 9–19 |
| Tiros al arco | 8.6 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.8 · 1–6 | 4.8 · 2–8 |
| Faltas | 24.1 · 18–31 | 12.1 · 8–17 | 12.0 · 8–17 | 10.8 · 7–15 | 13.3 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 39.8 · 29–52 | 20.0 · 12–28 | 19.8 · 12–28 | 17.7 · 11–24 | 22.1 · 15–30 |
| Atajadas del portero | — | 3.2 · 1–6 | 2.2 · 0–4 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Menos 4.5 | 1.26 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (59 %) | Alta probabilidad |
| Resultado y hándicap | Descanso o final: Paris FC (F) | 1.40 | 69 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Sorpresa: gana el no favorito (10 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Menos 6.0 | 1.42 | 77 % | 67 % | Empate (70 %) | Partido abierto (ambos marcan y 3+ goles) (67 %) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Tarjetas | Tarjetas Paris FC (F) Más 0.5 | 1.57 | 63 % | 58 % | Expulsión antes del 70′ (80 %) | Favorito golpea temprano y gana (58 %) | Justa |
| Quién saca más | Más tarjetas: HB Koge (F) | 1.95 | 49 % | 44 % | Expulsión antes del 70′ (55 %) | Favorito golpea temprano y gana (44 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners Menos 12.0 | 1.31 | 78 % | 78 % | 78 % | -0 pts | +2 % | 69 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 9 % |
| Goles Menos 4.5 | 1.26 | 78 % | 77 % | 77 % | +1 pts | -2 % | 78 % | +0.7 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 1.er tiempo Menos 6.0 | 1.42 | 77 % | 72 % | 76 % | +0 pts | +9 % | 67 % | +0.8 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Córners 2.º tiempo Más 3.5 | 1.31 | 76 % | 74 % | 75 % | +1 pts | +0 % | 73 % | +0.8 | 1.35 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 1.er tiempo Más 0.5 | 1.28 | 75 % | 76 % | 77 % | -1 pts | -4 % | 75 % | +0.8 | 1.37 | Favorito gana en partido trabado | Alta probabilidad · ★ enfoque a favor |
| Córners Más 7.5 | 1.28 | 75 % | 76 % | 74 % | +1 pts | -4 % | 70 % | +0.7 | 1.37 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Menos 11.5 | 1.31 | 73 % | 74 % | 73 % | -0 pts | -5 % | 70 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.36 | 72 % | 71 % | 72 % | +0 pts | -2 % | 72 % | +0.5 | 1.42 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Más 0.75 | 1.37 | 71 % | 71 % | 72 % | -1 pts | -3 % | 71 % | +0.6 | 1.46 | Favorito gana en partido trabado | Alta probabilidad · asiática: devuelve 17 % · ★ enfoque a favor |
| Córners 1.er tiempo Menos 5.5 | 1.42 | 70 % | 68 % | 70 % | +0 pts | -0 % | 69 % | +0.6 | 1.46 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners Más 8.0 | 1.52 | 70 % | 69 % | 69 % | +1 pts | +6 % | 58 % | +0.5 | 1.47 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Goles HB Koge (F) Menos 1.5 | 1.39 | 70 % | 69 % | 69 % | +1 pts | -3 % | 70 % | +0.4 | 1.48 | Sorpresa: gana el no favorito | Alta probabilidad |
| Descanso o final: Paris FC (F) | 1.40 | 69 % | 67 % | 68 % | +1 pts | -4 % | 69 % | — | 1.50 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| Córners Menos 11.0 | 1.52 | 68 % | 68 % | 68 % | -1 pts | +3 % | 59 % | +0.4 | 1.52 | Empate | Alta probabilidad · Valor · asiática: devuelve 10 % |
| Goles 1.er tiempo Menos 1.75 | 1.45 | 68 % | 67 % | 66 % | +2 pts | -2 % | 68 % | +0.3 | 1.53 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % |
| Goles HB Koge (F) Más 0.5 | 1.42 | 67 % | 68 % | 68 % | -1 pts | -5 % | 67 % | +0.6 | 1.54 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Más 3.5 | 1.39 | 65 % | 69 % | 66 % | -1 pts | -10 % | 63 % | +0.4 | 1.59 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 4.0 | 2.85 | 42 % | 39 % | 41 % | +1 pts | +20 % | 34 % | -0.1 | 2.50 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 18 % |
| Córners 1.er tiempo Menos 5.0 | 1.88 | 62 % | 58 % | 62 % | +0 pts | +17 % | 52 % | +0.3 | 1.67 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 16 % |
| Córners 1.er tiempo Menos 6.0 | 1.42 | 77 % | 72 % | 76 % | +0 pts | +9 % | 67 % | +0.8 | 1.34 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · Valor · asiática: devuelve 12 % |
| Más corners: HB Koge (F) | 3.05 | 35 % | 26 % | 36 % | -1 pts | +7 % | 29 % | — | 3.02 | Sorpresa: gana el no favorito | Valor frágil (depende de un guion) · ⚠ Revisar: la simulación sin contexto se aleja 19 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners Más 9.0 | 1.87 | 57 % | 56 % | 56 % | +1 pts | +6 % | 45 % | +0.2 | 1.82 | Favorito golpea temprano y gana | Valor · asiática: devuelve 12 % |
| Córners Más 8.0 | 1.52 | 70 % | 69 % | 69 % | +1 pts | +6 % | 58 % | +0.5 | 1.47 | Expulsión antes del 70′ | Alta probabilidad · Valor · asiática: devuelve 11 % |
| Córners Más 10.0 | 2.42 | 44 % | 43 % | 43 % | +1 pts | +6 % | 35 % | -0.1 | 2.40 | Expulsión antes del 70′ | Valor · asiática: devuelve 12 % |
| Córners Menos 10.0 | 1.87 | 56 % | 56 % | 56 % | -1 pts | +4 % | 47 % | +0.1 | 1.86 | Empate | Valor · asiática: devuelve 12 % |
| Córners Menos 11.0 | 1.52 | 68 % | 68 % | 68 % | -1 pts | +3 % | 59 % | +0.4 | 1.52 | Empate | Alta probabilidad · Valor · asiática: devuelve 10 % |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Menos 4.0 2.6 % de la banca; Córners 1.er tiempo Menos 5.0 4.7 % de la banca; Córners 1.er tiempo Menos 6.0 5.3 % de la banca; Más corners: HB Koge (F) 0.9 % de la banca; Córners Más 9.0 1.9 % de la banca; Córners Más 8.0 3.0 % de la banca; Córners Más 10.0 1.0 % de la banca; Córners Menos 10.0 1.2 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Gana Paris FC (F) + Descanso o final: Paris FC (F) | 61 % | 63 % | 56 % | 1.64 | 1.69 | 1.43 | 10 % | Favorito golpea temprano y gana | 0 % |
| Goles Más 0.5 + Gana Paris FC (F) + Descanso o final: Paris FC (F) | 61 % | 63 % | 56 % | 1.64 | 1.69 | 1.48 | 11 % | Favorito golpea temprano y gana | 0 % |
| Ambos 2+ tarjetas: No + Tarjetas Menos 2.5 | 57 % | 57 % | 52 % | 1.77 | 1.82 | 1.16 | 7 % | Favorito golpea temprano y gana | 58 % |
| Ambos 2+ tarjetas: No + Tarjetas HB Koge (F) Menos 1.5 | 57 % | 57 % | 52 % | 1.77 | 1.82 | 1.16 | 8 % | Favorito golpea temprano y gana | 57 % |
| Goles Más 0.5 + Ambos marcan: Sí | 60 % | 60 % | 55 % | 1.67 | 1.72 | 1.03 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 0 % |
| Hándicap HB Koge (F) +4 + Goles Paris FC (F) Menos 4.5 + Tarjetas Paris FC (F) Más 0.5 | 58 % | 58 % | 53 % | 1.73 | 1.78 | 1.05 | 8 % | Expulsión antes del 70′ | 47 % |
| Goles Paris FC (F) Menos 4.5 + Tarjetas Paris FC (F) Más 0.5 | 60 % | 59 % | 55 % | 1.68 | 1.73 | 1.01 | 6 % | Expulsión antes del 70′ | 55 % |
| Hándicap HB Koge (F) +4 + Ambos marcan: Sí | 58 % | 58 % | 53 % | 1.74 | 1.79 | 1.03 | 7 % | Partido abierto (ambos marcan y 3+ goles) | 0 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.