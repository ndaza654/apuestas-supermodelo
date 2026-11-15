# Bélgica - Italia
UEFA Liga de Naciones · 2026-11-15 14:45

**Tipo de partido:** Parejo · abierto · caliente · **Favorito:** Bélgica · primer gol: local 52 %, visitante 43 %, nadie 5 % · gol del favorito antes del 35′: 33 %

## ⚠ Alertas (revisar antes de usar las líneas marcadas)
- Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?)

## Enfoque de mercados (qué mercados le quedan bien al contexto)
Enfoque: mirar primero Goles del partido (Más), 1.er tiempo (Menos) y empate al descanso, Ambos marcan, Empate / doble oportunidad / HT-FT X, Tarjetas y faltas (Más). Poco favorecidos: Hándicap y victoria, Líneas de jugador.

| Mercado | Encaje | Por qué |
|---|---|---|
| Goles del partido (Más) | ✅ favorece | el modelo espera un partido de muchos goles; parejo y con mucho en juego: se cuidan; hay rotación: baja la producción |
| 1.er tiempo (Menos) y empate al descanso | ✅ favorece | partidos que se miden o parejos arrancan despacio |
| Ambos marcan | ✅ favorece | los dos tienen producción para marcar |
| Empate / doble oportunidad / HT-FT X | ✅ favorece | sin dominador claro el empate pesa más |
| Tarjetas y faltas (Más) | ✅ favorece | árbitro sin dato; los dos se juegan algo importante; parejo: más duelos y más faltas |
| Córners totales | ➖ neutro | rotación: el control sigue, pero baja el empuje |
| Hándicap y victoria | ⛔ en contra | partido parejo: ningún equipo manda |
| Líneas de jugador | ⛔ en contra | hay rotación: sin once confirmado no se sabe quién juega |

Es una hipótesis para decidir dónde analizar a fondo; no cambia probabilidades. Si el número dice otra cosa, manda el número.

## Guiones del partido (solo para medir qué línea aguanta; el enfoque de arriba es lo que orienta)
| Guion | Probabilidad |
|---|---|
| Partido abierto (ambos marcan y 3+ goles) | 30 % |
| Sorpresa: gana el no favorito | 27 % |
| Empate | 15 % |
| Expulsión antes del 70′ | 11 % |
| Favorito gana en partido trabado | 9 % |
| Favorito golpea temprano y gana | 8 % |

## Lo que cambió el contexto
- Importancia alta: más tensión (tarjetas ×1,10) y algo menos de gol (×0,95).
- Árbitro sin promedio: tarjetas en neutro (confianza baja en tarjetas).
- local necesita ganar: con empate después del 60′ se vuelca como si perdiera.
- visitante rota titulares: producción ×0,93.
- Cada efecto se aplica solo en la parte que se supone que Betano todavía no puso en el precio (config.FUERZA_CONTEXTO). Hechos frescos que van completos: ninguno.

## Medias esperadas (con contexto)
| | Goles | Remates | Al arco | Córners | Faltas | Tarjetas |
|---|---|---|---|---|---|---|
| local | 1.59 | 16.0 | 5.1 | 5.5 | 11.8 | 2.5 |
| visitante | 1.37 | 13.3 | 4.4 | 4.2 | 12.9 | 2.6 |

## Media esperada por mercado (modelo con contexto; entre paréntesis lo que espera Betano; rango del 80 % de los partidos simulados)
| Mercado | Total | Local | Visitante | 1.er tiempo | 2.º tiempo |
|---|---|---|---|---|---|
| Goles | 3.0 (3.1) · 1–5 | 1.6 (1.6) · 0–3 | 1.4 (1.5) · 0–3 | 1.3 (1.3) · 0–3 | 1.6 (1.8) · 0–3 |
| Córners | 9.7 (9.8) · 6–14 | 5.4 (5.5) · 2–9 | 4.2 (4.4) · 1–7 | 4.3 (4.7) · 2–7 | 5.3 (5.2) · 2–9 |
| Tarjetas (amarilla 1, roja 2) | 5.1 (4.8) · 2–8 | 2.5 (2.4) · 1–5 | 2.6 (2.4) · 1–5 | 1.7 (1.7) · 0–4 | 3.4 · 1–6 |
| Remates | 29.1 (29.7) · 21–37 | 15.9 (16.0) · 10–23 | 13.2 (14.0) · 8–19 | 12.9 · 8–18 | 16.2 · 11–22 |
| Tiros al arco | 9.5 (9.7) · 6–14 | 5.1 (5.1) · 2–8 | 4.3 (4.6) · 2–7 | 4.2 (4.5) · 2–7 | 5.3 · 2–8 |
| Faltas | 24.7 (24.5) · 18–31 | 11.8 (11.5) · 7–16 | 12.9 (13.0) · 8–18 | 11.1 · 7–15 | 13.6 · 9–18 |
| Fueras de lugar | 2.9 (2.9) · 1–5 | 1.2 (1.2) · 0–3 | 1.7 (1.7) · 0–4 | 1.3 (1.5) · 0–3 | 1.6 · 0–3 |
| Saques de meta | 15.2 (15.0) · 9–22 | 6.8 (6.8) · 3–11 | 8.4 (8.4) · 4–13 | 6.8 (7.0) · 3–11 | 8.5 · 4–13 |
| Saques de banda | 30.6 (30.2) · 21–41 | 15.3 (15.2) · 9–22 | 15.3 (15.2) · 9–22 | 13.7 (15.9) · 8–19 | 17.0 · 11–24 |
| Atajadas del portero | — | 3.0 · 1–6 | 3.5 · 1–6 | — | — |

## Lectura por mercado (la línea que mejor encaja con este partido en cada mercado)
| Mercado | Línea | Cuota | Prob. | Robustez | Brilla si… | La mata si… | Etiqueta |
|---|---|---|---|---|---|---|---|
| Goles | Goles Bélgica Menos 2.5 | 1.25 | 78 % | (lo define el marcador) | Empate (100 %) | Partido abierto (ambos marcan y 3+ goles) (52 %) | Alta probabilidad |
| Ambos marcan | Ambos marcan: No | 2.47 | 40 % | (lo define el marcador) | Favorito golpea temprano y gana (100 %) | Partido abierto (ambos marcan y 3+ goles) (0 %) | Justa |
| Resultado y hándicap | No hay empate | 1.27 | 76 % | (lo define el marcador) | Sorpresa: gana el no favorito (100 %) | Empate (0 %) | Alta probabilidad · ★ enfoque a favor |
| Córners | Córners 2.º tiempo Más 3.5 | 1.27 | 76 % | 76 % | Empate (78 %) | Favorito golpea temprano y gana (69 %) | Alta probabilidad |
| Tarjetas | Tarjetas Bélgica Menos 3.5 | 1.25 | 76 % | 78 % | Favorito golpea temprano y gana (83 %) | Expulsión antes del 70′ (46 %) | Alta probabilidad |
| Faltas | Faltas Bélgica Más 11.5 | 1.93 | 51 % | 49 % | Expulsión antes del 70′ (55 %) | Sorpresa: gana el no favorito (49 %) | Justa |
| Remates | Remates Italia Menos 14.5 | 1.60 | 65 % | 59 % | Favorito gana en partido trabado (75 %) | Partido abierto (ambos marcan y 3+ goles) (59 %) | Contexto a favor (+6 pts) · Valor |
| Tiros al arco | Tiros al arco Italia Menos 5.5 | 1.40 | 73 % | 58 % | Favorito gana en partido trabado (92 %) | Sorpresa: gana el no favorito (58 %) | Alta probabilidad · Contexto a favor (+5 pts) |
| Fueras de lugar | Fueras de lugar Bélgica Más 0.5 | 1.42 | 66 % | 66 % | Sorpresa: gana el no favorito (69 %) | Favorito golpea temprano y gana (64 %) | Alta probabilidad · cuota por debajo de la justa |
| Saques de meta | Saques de meta Más 14.5 | 1.82 | 52 % | 49 % | Expulsión antes del 70′ (58 %) | Favorito gana en partido trabado (49 %) | Cara |
| Saques de banda | Saques de banda 1.er tiempo Menos 15.5 | 1.91 | 58 % | 57 % | Favorito gana en partido trabado (59 %) | Favorito golpea temprano y gana (57 %) | Valor · ⚠ Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Jugadores | Gianluigi Donnarumma atajadas 5+ | 3.45 | 28 % | 26 % | Partido abierto (ambos marcan y 3+ goles) (30 %) | Expulsión antes del 70′ (25 %) | Justa · enfoque en contra |
| Quién saca más | Más corners: Bélgica | 1.65 | 57 % | 54 % | Sorpresa: gana el no favorito (62 %) | Favorito golpea temprano y gana (45 %) | Cara |

Si el guion que la mata es justo el que tu lectura del partido ve probable, esa línea no va, aunque el número sea alto.

## Alta probabilidad y robustas (aguantan en los guiones principales)
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Goles Bélgica Menos 2.5 | 1.25 | 78 % | 78 % | 78 % | +0 pts | -2 % | 78 % | +0.8 | 1.32 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas Bélgica Menos 3.5 | 1.25 | 76 % | 78 % | 78 % | -2 pts | -5 % | 78 % | +0.6 | 1.35 | Expulsión antes del 70′ | Alta probabilidad |
| Goles 2.º tiempo Menos 2.5 | 1.32 | 76 % | 73 % | 74 % | +2 pts | +0 % | 76 % | +0.7 | 1.35 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Córners 2.º tiempo Más 3.5 | 1.27 | 76 % | 76 % | 77 % | -1 pts | -4 % | 76 % | +0.8 | 1.36 | Favorito golpea temprano y gana | Alta probabilidad |
| No hay empate | 1.27 | 76 % | 75 % | 74 % | +1 pts | -4 % | 76 % | — | 1.36 | Empate | Alta probabilidad · ★ enfoque a favor |
| Tarjetas Italia Menos 3.5 | 1.26 | 75 % | 77 % | 77 % | -2 pts | -5 % | 76 % | +0.6 | 1.37 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Goles Italia Más 0.5 | 1.25 | 75 % | 78 % | 78 % | -3 pts | -6 % | 75 % | +0.8 | 1.37 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners Italia Menos 5.5 | 1.35 | 74 % | 71 % | 71 % | +3 pts | +0 % | 71 % | +0.5 | 1.39 | Favorito golpea temprano y gana | Alta probabilidad |
| Tiros al arco Bélgica Menos 6.5 | 1.29 | 74 % | 75 % | 74 % | -0 pts | -5 % | 58 % | +0.6 | 1.39 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Tarjetas 1.er tiempo Menos 2.5 | 1.32 | 74 % | 73 % | 75 % | -1 pts | -2 % | 77 % | +0.6 | 1.39 | Expulsión antes del 70′ | Alta probabilidad |
| Córners Menos 11.5 | 1.34 | 74 % | 72 % | 71 % | +3 pts | -1 % | 71 % | +0.6 | 1.40 | Empate | Alta probabilidad |
| Córners 2.º tiempo Menos 6.5 | 1.30 | 74 % | 74 % | 71 % | +2 pts | -4 % | 69 % | +0.5 | 1.40 | Empate | Alta probabilidad |
| Tarjetas Menos 6.5 | 1.27 | 74 % | 76 % | 76 % | -2 pts | -7 % | 76 % | +0.5 | 1.40 | Expulsión antes del 70′ | Alta probabilidad · cuota por debajo de la justa |
| Córners Más 7.5 | 1.26 | 73 % | 77 % | 76 % | -3 pts | -8 % | 74 % | +0.7 | 1.41 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa |
| Tiros al arco Italia Menos 5.5 | 1.40 | 73 % | 69 % | 68 % | +5 pts | +2 % | 58 % | +0.5 | 1.41 | Sorpresa: gana el no favorito | Alta probabilidad · Contexto a favor (+5 pts) |
| Tarjetas Italia Más 1.5 | 1.38 | 72 % | 70 % | 71 % | +1 pts | -0 % | 70 % | +0.7 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Tarjetas Bélgica Más 1.5 | 1.39 | 72 % | 69 % | 70 % | +2 pts | +0 % | 70 % | +0.7 | 1.43 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Goles 1.er tiempo Más 0.5 | 1.32 | 72 % | 73 % | 74 % | -2 pts | -5 % | 72 % | +0.7 | 1.43 | Favorito gana en partido trabado | Alta probabilidad · cuota por debajo de la justa · ★ enfoque a favor |
| Córners 1.er tiempo Menos 5.5 | 1.42 | 71 % | 67 % | 69 % | +2 pts | +2 % | 70 % | +0.6 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad |
| Goles 1.er tiempo Menos 1.75 | 1.40 | 71 % | 70 % | 69 % | +2 pts | +0 % | 72 % | +0.4 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 12 % · ★ enfoque a favor |
| Goles Menos 3.75 | 1.44 | 71 % | 68 % | 68 % | +3 pts | +3 % | 72 % | +0.5 | 1.44 | Partido abierto (ambos marcan y 3+ goles) | Alta probabilidad · asiática: devuelve 8 % |
| Kevin De Bruyne entradas 1+ | 1.25 | 71 % | 71 % | 71 % | +1 pts | -11 % | 68 % | — | 1.44 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa · enfoque en contra |
| Tarjetas Más 3.5 | 1.42 | 71 % | 68 % | 68 % | +3 pts | +1 % | 68 % | +0.6 | 1.45 | Favorito golpea temprano y gana | Alta probabilidad · ★ enfoque a favor |
| Maxim De Cuyper remates 1+ | 1.26 | 71 % | 71 % | 70 % | +1 pts | -11 % | 70 % | — | 1.45 | Favorito golpea temprano y gana | Alta probabilidad · cuota por debajo de la justa · enfoque en contra |
| Hans Vanaken entradas 1+ | 1.25 | 71 % | 71 % | 70 % | +1 pts | -12 % | 67 % | — | 1.46 | Sorpresa: gana el no favorito | Alta probabilidad · cuota por debajo de la justa · enfoque en contra |

## Donde el contexto mueve la línea a tu favor
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Remates Italia Menos 13.5 | 1.93 | 55 % | 48 % | 49 % | +6 pts | +7 % | 49 % | +0.1 | 1.88 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) · Valor |
| Remates Italia Menos 14.5 | 1.60 | 65 % | 59 % | 59 % | +6 pts | +4 % | 59 % | +0.3 | 1.59 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) · Valor |
| Remates Menos 30.5 | 1.65 | 62 % | 57 % | 56 % | +6 pts | +2 % | 52 % | +0.2 | 1.67 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) |
| Remates Menos 29.5 | 1.87 | 55 % | 50 % | 49 % | +6 pts | +3 % | 44 % | +0.1 | 1.89 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) |
| Remates Italia Menos 12.5 | 2.40 | 45 % | 38 % | 39 % | +6 pts | +8 % | 40 % | -0.2 | 2.31 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) · Valor |
| Remates Menos 28.5 | 2.15 | 48 % | 43 % | 42 % | +6 pts | +3 % | 37 % | -0.1 | 2.18 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) |
| Tiros al arco Italia Menos 4.5 | 1.83 | 57 % | 51 % | 52 % | +6 pts | +5 % | 38 % | +0.1 | 1.81 | Sorpresa: gana el no favorito | Contexto a favor (+6 pts) · Valor |
| Tiros al arco Italia Menos 3.5 | 2.72 | 39 % | 33 % | 33 % | +5 pts | +5 % | 20 % | -0.4 | 2.73 | Sorpresa: gana el no favorito | Contexto a favor (+5 pts) |
| Tiros al arco Italia Menos 5.5 | 1.40 | 73 % | 69 % | 68 % | +5 pts | +2 % | 58 % | +0.5 | 1.41 | Sorpresa: gana el no favorito | Alta probabilidad · Contexto a favor (+5 pts) |
| Goles Italia Menos 1.5 | 1.67 | 61 % | 57 % | 56 % | +4 pts | +1 % | 61 % | +0.1 | 1.70 | Sorpresa: gana el no favorito | Contexto a favor (+4 pts) |
| Tiros al arco Menos 9.5 | 1.88 | 53 % | 50 % | 49 % | +4 pts | +1 % | 34 % | +0.0 | 1.94 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+4 pts) |

## Con valor según el modelo
| Selección | Cuota | Prob. | Mercado | Sin contexto | Movimiento | EV | Robustez | Colchón | Cuota mínima | Peor guion | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Saques de banda 1.er tiempo Menos 15.5 | 1.91 | 58 % | 49 % | 59 % | -2 pts | +10 % | 57 % | +0.4 | 1.80 | Favorito golpea temprano y gana | Valor · ⚠ Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?) |
| Remates Italia Menos 12.5 | 2.40 | 45 % | 38 % | 39 % | +6 pts | +8 % | 40 % | -0.2 | 2.31 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) · Valor |
| Remates Italia Menos 13.5 | 1.93 | 55 % | 48 % | 49 % | +6 pts | +7 % | 49 % | +0.1 | 1.88 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) · Valor |
| Córners 1.er tiempo Menos 4.5 | 1.90 | 55 % | 49 % | 52 % | +3 pts | +5 % | 54 % | +0.1 | 1.88 | Partido abierto (ambos marcan y 3+ goles) | Valor |
| Tiros al arco Italia Menos 4.5 | 1.83 | 57 % | 51 % | 52 % | +6 pts | +5 % | 38 % | +0.1 | 1.81 | Sorpresa: gana el no favorito | Contexto a favor (+6 pts) · Valor |
| Goles Menos 3.0 | 1.88 | 55 % | 52 % | 52 % | +3 pts | +4 % | 55 % | +0.0 | 1.87 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 23 % · Historial propio en contra (goles menos: 2/6 contra 53 % del precio) |
| Goles Menos 3.25 | 1.70 | 61 % | 57 % | 58 % | +3 pts | +4 % | 61 % | +0.2 | 1.69 | Partido abierto (ambos marcan y 3+ goles) | Valor · asiática: devuelve 11 % · Historial propio en contra (goles menos: 2/6 contra 53 % del precio) |
| Remates Italia Menos 14.5 | 1.60 | 65 % | 59 % | 59 % | +6 pts | +4 % | 59 % | +0.3 | 1.59 | Partido abierto (ambos marcan y 3+ goles) | Contexto a favor (+6 pts) · Valor |

Kelly ¼ (dato informativo, no una orden de stake): Saques de banda 1.er tiempo Menos 15.5 2.7 % de la banca; Remates Italia Menos 12.5 1.5 % de la banca; Remates Italia Menos 13.5 1.8 % de la banca; Córners 1.er tiempo Menos 4.5 1.3 % de la banca; Tiros al arco Italia Menos 4.5 1.4 % de la banca; Goles Menos 3.0 1.1 % de la banca; Goles Menos 3.25 1.4 % de la banca; Remates Italia Menos 14.5 1.6 % de la banca. Con muestra chica y sin hecho fresco, el EV del modelo suele ser optimista: Sharpods e Ingeniero Analista usan 0,5–3 %.

## Sistemas de tipsters que este partido cumple (solo para medir, no para decidir)
| Sistema | Regla | Selección que propone | Historial con cuotas reales |
|---|---|---|---|
| Ingeniero Analista #5/#14 | empate ≥3,60 (señal de goles) | Goles Más 2.5 | 42643 partidos: acierto 56.8 % contra 56.3 % del precio; ROI -4.0 % ± 0.8 (con la mejor cuota -0.4 %) |

## Builders del mismo guion
| Patas | Prob. ajustada | Prob. simulación | Si una pata está 5 pts peor | Cuota justa | Cuota mínima en Betano | Correlación | Margen acumulado | Guion común | Robustez |
|---|---|---|---|---|---|---|---|---|---|
| Ambos 2+ tarjetas: Sí + Tarjetas Bélgica Más 1.5 | 55 % | 57 % | 50 % | 1.81 | 1.86 | 1.37 | 10 % | Expulsión antes del 70′ | 53 % |
| Tarjetas Más 3.5 + Ambos 2+ tarjetas: Sí | 55 % | 57 % | 50 % | 1.81 | 1.86 | 1.39 | 10 % | Expulsión antes del 70′ | 53 % |
| Hándicap Bélgica +0.5 + Bélgica o empate + Goles 2.º tiempo Menos 2.5 | 52 % | 53 % | 48 % | 1.91 | 1.97 | 1.45 | 8 % | Empate | 0 % |
| Hándicap Bélgica +0.5 + Bélgica o empate + Tarjetas Bélgica Más 1.5 | 49 % | 50 % | 46 % | 2.03 | 2.09 | 1.44 | 9 % | Empate | 0 % |
| Goles Italia Menos 2.5 + Tiros al arco Menos 10.5 | 60 % | 59 % | 55 % | 1.67 | 1.72 | 1.07 | 7 % | Favorito gana en partido trabado | 46 % |
| Goles Menos 3.5 + Tiros al arco Menos 10.5 | 52 % | 52 % | 48 % | 1.93 | 1.99 | 1.2 | 8 % | Empate | 21 % |
| Goles Italia Menos 2.5 + Tarjetas Más 3.5 | 61 % | 62 % | 57 % | 1.64 | 1.69 | 1.01 | 6 % | Expulsión antes del 70′ | 44 % |
| Tiros al arco 1.er tiempo Menos 4.5 + Goles 1.er tiempo Menos 3.5 | 58 % | 59 % | 53 % | 1.72 | 1.77 | 1.04 | 7 % | Favorito gana en partido trabado | 46 % |

Prob. ajustada: la conjunta de la simulación llevando cada pata a su probabilidad de decisión y corrigiendo la dependencia entre patas que se midió con 62 000 partidos (p. ej. «gana el favorito + sus córners Más» se estorban más de lo que creía el simulador). Margen acumulado: lo que la casa cobra por pata, multiplicado.

Colchón: cuántas desviaciones típicas separan la media esperada de la línea, a favor (+) o en contra (−). Cuanto más alto, menos depende la línea de un córner o un remate de diferencia.

Arma el builder en Betano: si la cuota que muestra es igual o mayor a la "cuota mínima", el precio es bueno. Correlación > 1 = las patas se ayudan (mismo guion); < 1 = se estorban.