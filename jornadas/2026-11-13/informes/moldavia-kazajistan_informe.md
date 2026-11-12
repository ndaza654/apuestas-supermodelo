# Moldavia - Kazajistán
UEFA Liga de Naciones · 2026-11-13 12:00

**Tipo de partido:** Parejo · cerrado · caliente · **Favorito:** Moldavia · primer gol: local 45 %, visitante 44 %, nadie 11 % · gol del favorito antes del 35′: 25 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)
- Revisar: la simulación sin contexto se aleja 38 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Menos), 1.er tiempo (Menos) y empate al descanso, Empate / doble oportunidad / HT-FT X, Tarjetas y faltas (Más). Poco favorecidos: Hándicap y victoria.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Menos) | ✅ favorece | el modelo espera un partido de pocos goles; parejo y con mucho en juego: se cuidan |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Tarjetas y faltas (Más) | ✅ favorece | árbitro sin dato; los dos se juegan algo importante; parejo: más duelos y más faltas |
| Ambos marcan | ➖ neutro | sin ventaja clara para ninguna de las dos opciones |
| Córners totales | ➖ neutro | ni a favor ni en contra |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Sorpresa: gana el no favorito | 31 % |
| Empate | 22 % |
| Partido abierto (ambos marcan y 3+ goles) | 17 % |
| Favorito gana en partido trabado | 12 % |
| Expulsión antes del 70′ | 11 % |
| Favorito golpea temprano y gana | 8 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- visitante necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.09 | 12.8 | 4.3 | 4.5 | 12.3 | 2.2 |
| visitante | 1.04 | 12.8 | 4.3 | 4.5 | 12.3 | 2.8 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 2.1 (2.2) · 0–4 | 1.1 (1.1) · 0–2 | 1.1 (1.1) · 0–2 | 0.9 (1.0) · 0–2 | 1.2 (1.2) · 0–3 |
| Córners | 9.0 (8.8) · 5–13 | 4.5 · 2–8 | 4.5 · 2–8 | 3.9 (3.4) · 1.9–7 | 5.1 (4.7) · 2–8 |
| Tarjetas (amarilla 1, roja 2) | 5.0 (4.7) · 2–8 | 2.2 (2.1) · 1–4 | 2.8 (2.6) · 1–5 | 1.6 (1.6) · 0–3 | 3.4 · 1–6 |
| Remates | 25.5 · 19–33 | 12.8 · 7–19 | 12.8 · 8–18 | 11.2 · 7–16 | 14.4 · 9–20 |
| Tiros al arco | 8.6 · 5–13 | 4.3 · 2–7 | 4.3 · 2–7 | 3.8 · 1–6 | 4.8 · 2–8 |
| Faltas | 24.6 · 18–31 | 12.3 · 8–17 | 12.3 · 8–17 | 11.1 · 7–15 | 13.6 · 9–18 |
| Fueras de lugar | 3.6 · 1–6 | 1.8 · 0–4 | 1.8 · 0–4 | 1.6 · 0–3 | 2.0 · 0–4 |
| Saques de meta | 16.0 · 10–23 | 8.0 · 4–13 | 8.0 · 4–13 | 7.2 · 3–11 | 8.8 · 5–13 |
| Saques de banda | 40.0 · 29–52 | 20.0 · 12–28 | 20.0 · 12–28 | 17.9 · 11–25 | 22.2 · 15–30 |
| Atajadas del portero | — | 3.3 · 1–6 | 3.2 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles 1.er tiempo Menos 1.5 | 1.33 | 75 % | (lo define el marcador) | Favorito gana en partido trabado (99 %) | Partido abierto (ambos marcan y 3+ goles) (46 %) | Alta probabilidad · ★ enfoque a favor |
| Ambos marcan | Ambos marcan: No | 1.72 | 56 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Justa |
| Resultado y hándicap | No hay empate | 1.37 | 71 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 1.er tiempo Más 1.5 | 1.60 | 75 % | 74 % | Sorpresa: gana el no favorito (75 %) | Favorito golpea temprano y gana (74 %) | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Tarjetas | Tarjetas Moldavia Más 1.5 | 1.53 | 66 % | 63 % | Expulsión antes del 70′ (84 %) | Favorito golpea temprano y gana (62 %) | Alta probabilidad · ★ enfoque a favor |
| Quién saca más | Más tarjetas: Kazajistán | 1.90 | 50 % | 49 % | Expulsión antes del 70′ (57 %) | Favorito golpea temprano y gana (48 %) | Justa |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Menos 5.5 | 1.27 | 78 % | 76 % | 77 % | +1 pts | -1 % | 76 % | +0.8 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Menos 1.5 | 1.33 | 75 % | 73 % | 73 % | +2 pts | +0 % | 75 % | +0.6 | 1.37 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Córners 1.er tiempo Más 1.5 | 1.60 | 75 % | 59 % | 75 % | -0 pts | +19 % | 74 % | +1.2 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 2.º tiempo Más 3.5 | 1.40 | 72 % | 69 % | 70 % | +3 pts | +1 % | 72 % | +0.7 | 1.42 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Kazajistán Menos 1.5 | 1.36 | 72 % | 71 % | 71 % | +1 pts | -3 % | 72 % | +0.5 | 1.44 | Sorpresa: gana el no favorito | Alta probabilidad · ★ enfoque a favor |
| No hay empate | 1.37 | 71 % | 69 % | 69 % | +2 pts | -3 % | 71 % | — | 1.45 | Empate | Alta probabilidad · ★ enfoque a favor |
| Córners Menos 10.5 | 1.31 | 71 % | 74 % | 72 % | -1 pts | -7 % | 68 % | +0.5 | 1.45 | Empate | Alta probabilidad · cuota por debajo de la justa |
| Goles 2.º tiempo Más 0.5 | 1.39 | 70 % | 69 % | 70 % | +0 pts | -2 % | 70 % | +0.7 | 1.46 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles Moldavia Menos 1.5 | 1.39 | 70 % | 69 % | 69 % | +1 pts | -2 % | 70 % | +0.4 | 1.47 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Goles 1.er tiempo Menos 1.25 | 1.44 | 70 % | 67 % | 68 % | +2 pts | +1 % | 70 % | +0.3 | 1.47 | Favorito golpea temprano y gana | Alta probabilidad · asiática: devuelve 18 % · ★ enfoque a favor |
| Goles Moldavia Más 0.5 | 1.40 | 68 % | 69 % | 69 % | -1 pts | -5 % | 68 % | +0.6 | 1.53 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 7.5 | 1.45 | 67 % | 66 % | 65 % | +1 pts | -3 % | 66 % | +0.5 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad |
| Goles 2.º tiempo Menos 1.5 | 1.45 | 66 % | 67 % | 66 % | +0 pts | -4 % | 66 % | +0.2 | 1.55 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · ★ enfoque a favor |
| Goles Kazajistán Más 0.5 | 1.45 | 66 % | 66 % | 66 % | -0 pts | -4 % | 66 % | +0.6 | 1.55 | Favorito golpea temprano y gana | Alta probabilidad |
| Tarjetas Moldavia Más 1.5 | 1.53 | 66 % | 62 % | 63 % | +3 pts | +0 % | 63 % | +0.5 | 1.57 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Moldavia o empate | 1.45 | 65 % | 67 % | 67 % | -2 pts | -5 % | 65 % | — | 1.58 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Hándicap Moldavia +1 | 1.45 | 65 % | 67 % | 67 % | -2 pts | -5 % | 65 % | — | 1.58 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Hándicap Moldavia +0.5 | 1.44 | 65 % | 67 % | 67 % | -2 pts | -6 % | 65 % | — | 1.58 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjetas Más 4.5 | 1.90 | 54 % | 49 % | 49 % | +5 pts | +3 % | 49 % | +0.2 | 1.91 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) · ★ enfoque a favor |
| Tarjetas Kazajistán Más 2.5 | 1.93 | 52 % | 48 % | 47 % | +5 pts | +0 % | 48 % | +0.2 | 2.00 | Favorito golpea temprano y gana | Contexto a favor (+5 pts) · ★ enfoque a favor |
| Ambos 2+ tarjetas: Sí | 1.91 | 54 % | 49 % | 50 % | +4 pts | +4 % | 52 % | — | 1.91 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · Valor |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Córners 1.er tiempo Más 2.5 | 2.45 | 55 % | 37 % | 56 % | -1 pts | +36 % | 55 % | +0.7 | 1.87 | Empate | Valor · ⚠ Revisar: la simulación sin contexto se aleja 38 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Córners 1.er tiempo Más 1.5 | 1.60 | 75 % | 59 % | 75 % | -0 pts | +19 % | 74 % | +1.2 | 1.38 | Favorito golpea temprano y gana | Alta probabilidad · Valor · ⚠ Revisar: la simulación sin contexto se aleja 31 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Ambos 2+ tarjetas: Sí | 1.91 | 54 % | 49 % | 50 % | +4 pts | +4 % | 52 % | — | 1.91 | Favorito golpea temprano y gana | Contexto a favor (+4 pts) · Valor |

Kelly ¼ (dato informativo, no una orden de stake): Córners 1.er tiempo Más 2.5 6.2 % de la banca; Córners 1.er tiempo Más 1.5 8.0 % de la banca; Ambos 2+ tarjetas: Sí 1.1 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5 | empate 2,90–3,20 (señal de pocos goles) | Goles Menos 2.5 | 18423 partidos: acierto 59.9 % contra 59.5 % del precio; ROI -3.9 % ± 1.1 (con la mejor cuota -0.3 %) |
| Ingeniero Analista #26 | parejo (ambos ≥2,00) y Más 1.5 >1,40 | Goles Menos 2.5 | 58298 partidos: acierto 53.4 % contra 53.3 % del precio; ROI -5.2 % ± 0.7 (con la mejor cuota -1.3 %) |
| Ingeniero Analista #420 | empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas | Empate | 48947 partidos: acierto 29.9 % contra 29.2 % del precio; ROI -5.0 % ± 1.3 (con la mejor cuota -0.1 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 1+ tarjetas: Sí + Tarjetas Moldavia Más 1.5 + Hándicap Kazajistán +3 | 61 % | 63 % | 56 % | 1.64 | 1.69 | 1.12 | 8 % | Expulsión antes del 70′ | 59 % |
| Ambos 1+ tarjetas: Sí + Tarjetas Moldavia Más 1.5 + Goles Kazajistán Menos 2.5 | 58 % | 59 % | 53 % | 1.73 | 1.78 | 1.13 | 9 % | Expulsión antes del 70′ | 49 % |
| Goles Menos 3.5 + Ambos marcan: No | 55 % | 54 % | 50 % | 1.83 | 1.89 | 1.18 | 9 % | Favorito gana en partido trabado | 0 % |
| Hándicap Kazajistán +3 + Goles Menos 3.5 + Ambos marcan: No | 53 % | 52 % | 48 % | 1.90 | 1.96 | 1.17 | 10 % | Favorito gana en partido trabado | 0 % |
| Goles 2.º tiempo Más 0.5 + No hay empate | 55 % | 55 % | 51 % | 1.82 | 1.88 | 1.1 | 9 % | Favorito gana en partido trabado | 0 % |
| Goles Moldavia Menos 2.5 + Descanso o final: Empate | 57 % | 57 % | 52 % | 1.77 | 1.82 | 1.05 | 8 % | Empate | 41 % |
| Goles 1.er tiempo Menos 1.5 + Córners Más 6.5 | 59 % | 59 % | 55 % | 1.69 | 1.74 | 1.0 | 7 % | Favorito gana en partido trabado | 37 % |
| Goles Kazajistán Menos 2.5 + Descanso o final: Empate | 57 % | 57 % | 52 % | 1.77 | 1.82 | 1.04 | 8 % | Empate | 36 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.