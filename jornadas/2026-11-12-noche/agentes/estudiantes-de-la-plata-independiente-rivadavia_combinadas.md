# Combinadas · Estudiantes de La Plata – Independiente Rivadavia (Supercopa Argentina, final, 18:00 Bogotá)

Fuentes: agentes corners / partido / tarjetas / goles-resultado de este partido; `informes/..._resultado.json` (líneas, `alertas`, `builders`); combinadas calculadas con `python3 -m supermodelo --combos` (mismo motor que los builders del informe: simulación + dependencia medida + corrección a la probabilidad de decisión de cada pata). Jugadores no aplica (sin alineaciones).

## Enfoque de mercados
Pesan córners (esperado 9.86), tiros al arco (8.86) y tarjetas totales; goles/resultado son parejo y cerrado. Final a partido único, cancha neutra.

## Advertencias arriba (leer primero)
1. **Los builders propios del informe NO sirven como base:** sus 8 combinadas llevan patas que no cumplen (Tarjetas 1T, Córners Más 4.5, Remates Más 25.5, Ambos No, Tarjetas Estudiantes Más 0.5, etc.). Por eso armé combinadas nuevas solo con patas que cumplen (≥5 de 7 en ambos, n≥5, cuota ≥1.20) y las evalué con el mismo motor.
2. **Alertas del modelo (10, de 16 a 40 pts):** todas en tarjetas. La simulación se aleja del mercado en esa familia. Evité patas de tarjetas con alerta (Menos 7.5 y Menos 3.5 de Rivadavia llevan aviso); `Tarjetas Menos 8.5` y `Rivadavia Menos 4.5` no lo llevan, pero la probabilidad conjunta que incluye tarjetas es menos fiable.
3. **Goles/resultado: el modelo copia el mercado** (fuente_objetivos g = mercado; distancia sin contexto vs mercado ≤ 2 pts). Para la pata «Estudiantes o empate» p del modelo = p del mercado: no es segunda opinión.
4. **Liquidación NO verificada:** no está confirmado en el repo si Betano liquida a 90 min o con prórroga/penales. Afecta a «Estudiantes o empate» (y a cualquier goles/resultado/hándicap); para córners, tiros y tarjetas tampoco está escrita la regla.
5. **Precio real:** no tengo la cuota del cupón. La «cuota total» es el producto de las individuales (techo); el cupón de Betano suele pagar menos. La «cuota mínima» es la del modelo (1.03/p), NO una exigencia de Betano: no verificado si el builder de Betano combina estos mercados ni cuánto paga. EV = p·cuota−1 se informa, no decide.
6. Sin alineaciones, sin estadísticas de árbitro (Pérez Y.), sin estadística por tiempo; criterios de tipsters sin resultados verificados. Bajas de la previa: Correa y Castro (Estudiantes), Arce (Rivadavia), sin hora.

## Combinadas (todas del mismo partido, mercados distintos, sin escalones del mismo mercado)

### 1. Volumen sin exceso de tarjetas (E1) — la de mejor precio relativo
| Pata | Cuota | X de 7 (Estudiantes / Rivadavia) | Directos |
|---|---|---|---|
| Córners total Más 6.5 | 1.24 | 7 / 6 | 3 de 3 |
| Tiros al arco total Más 6.5 | 1.30 | 5 / 5 | 2 de 3 |
| Tarjetas total Menos 8.5 | 1.24 | 6 / 5 | 3 de 3 |

- Cuota total (producto, techo): **2.00**. p ajustada **50 %** (p_sim 53 %), cuota justa 2.01, cuota mínima 2.07. EV si paga el producto: **−0.4 %**. Si el cupón paga menos que 2.07 queda por debajo del precio mínimo del modelo.
- Correlación del modelo 1.02 (casi independientes). Esperada: córners Más y tiros Más positiva (mismo volumen); tarjetas Menos con las otras dos, leve negativa (un partido con mucho juego y duelos suele traer tarjetas).
- Stress (cada pata 5 pts peor): **46 %**; pata más frágil **Tiros al arco total Más 6.5** (73 % de decisión, 5 de 7 y 5 de 7, justo en el umbral). Margen acumulado 9 %. Guion común: partido abierto; robustez 44 %.
- Aviso: tarjetas Menos 8.5 se mide en puntos de Betano (roja = 2) y la serie es solo amarillas: una roja temprana en una final la rompe.

### 2. Córners con tope de tiros (E6) — 2 patas, solo estadísticas
| Pata | Cuota | X de 7 (Estudiantes / Rivadavia) | Directos |
|---|---|---|---|
| Córners total Más 6.5 | 1.24 | 7 / 6 | 3 de 3 |
| Tiros al arco total Menos 10.5 | 1.27 | 5 / 6 | 3 de 3 |

- Cuota total (producto): **1.57**. p ajustada **59 %** (p_sim 58 %), cuota justa 1.70, mínima 1.75. EV si paga el producto: **−7.7 %** (el producto queda 0.18 por debajo de la mínima).
- Correlación del modelo 0.98. Esperada: ligeramente negativa en concepto (córners Más pide volumen, tiros Menos lo limita); aquí las líneas están lejos (6.5 córners vs esperado 9.86 es bajo; 10.5 tiros vs esperado 8.86 es alto), por eso casi no se estorban.
- Stress: **55 %**; pata más frágil **Tiros al arco total Menos 10.5** (76 %, 5 de 7 en Estudiantes). Margen acumulado 6 %. Guion común: empate; robustez 43 %.
- Comparte la pata «Córners Más 6.5» con la combinada 1: si juegas ambas es la misma apuesta repetida en esa pata.

### 3. Córners de Rivadavia + Estudiantes no pierde (E11) — incluye pata de resultado (liquidación NO verificada)
| Pata | Cuota | X de 7 (Estudiantes / Rivadavia) | Directos |
|---|---|---|---|
| Córners Independiente Rivadavia Más 2.5 | 1.29 | 5 / 6 | 2 de 3 |
| Estudiantes de La Plata o empate (= Hándicap Estudiantes +1) | 1.31 | 5 / 5 | 3 de 3 |

- Cuota total (producto): **1.69**. p ajustada **57 %** (p_sim 59 %), cuota justa 1.74, mínima 1.80. EV si paga el producto: **−3.0 %**.
- Correlación del modelo 1.01. Esperada: levemente negativa (si Rivadavia presiona y acumula córners tiende a ganar, y eso rompe la doble).
- Stress: **54 %**; pata más frágil **Estudiantes o empate** (75 %). Margen acumulado 10 %. Guion común: favorito golpea temprano y gana; robustez 0 % (en el reparto de guiones no sostiene un guion propio). La pata de resultado es p del mercado (el modelo la copia).
- Si Betano liquida con prórroga o penales, «o empate» cambia de significado. Verificar antes.

## Stress de la rotación de Estudiantes (escenario mío, NO estimado por el modelo)
Estudiantes juega la final de Libertadores contra Palmeiras tras este partido. Ilustración: −10 pts en cada pata que depende de su once (no una probabilidad medida):
- Comb. 1: córners −10 y tiros Más −10 → p ≈ **38 %** (cuota justa ≈ 2.67 vs techo 2.00). Tarjetas Menos no cambia o mejora.
- Comb. 2: córners −10; tiros Menos no sufre (un once alterno remata menos) → p ≈ **51 %**. Es la más resistente.
- Comb. 3: la doble −10; córners de Rivadavia probablemente suben con un Estudiantes alterno → p ≈ **50 %** (cobertura parcial: una pata mejora, la otra empeora, pero deben cumplirse las dos).
Esto no está confirmado: la ficha marca `rotacion=False` y la lista de dudas dice «posible rotación, sin confirmar».

## Descartadas (para que no se vean como alternativas independientes)
- Escalones del mismo mercado (p. ej. Córners Más 6.5 y 7.5, Remates Estudiantes Menos 15.5 y 16.5, Tiros total Más 4.5-7.5): son una sola apuesta.
- Cualquier pata de tarjetas «Más 0.5» de equipo y «Ambos 1+» (cuotas incoherentes, sin verificar, por instrucción); «Estudiantes Más 1.5» (2.87) tampoco la usé.
- 3 patas con Tarjetas Menos 7.5 o Rivadavia Menos 3.5: llevan la alerta del modelo (17-18 pts).
- Variantes que calculé y quedaron peor: córners + goles Estudiantes Menos 1.5 + tarjetas (p 48 %, EV −2.4 %, colchón del Menos 1.5 es +0.07: no hay), córners + Estudiantes marca + tarjetas (44 %), doble + tiros Menos + córners (44 %, EV −8.8 %), córners Más 7.5 + tiros Rivadavia + tarjetas (42 %).
- Dos combinadas empatan en precio a favor del producto (EV +1.7 % «doble + córners Rivadavia + tarjetas Menos 8.5», +2.2 % «córners + tiros Más 6.5 + tarjetas Menos 7.5») pero con p de 45-48 %, pata de resultado sin verificar o aviso de tarjetas: no las incluyo; el EV con producto es un techo y no manda.

## Hándicap
Las líneas que cumplen son Estudiantes +1 @1.31 (5/5, = doble oportunidad), +2 @1.07 (cuota < 1.20), Rivadavia +0.5 @1.60, +1 @1.57, +0.75 @1.40 (asiática: media devolución, no «gana/pierde»). La regularidad de la diferencia de goles viene de la ficha de goles (n 7+7, directos 3). El modelo copia el mercado (≤2 pts). No armé combinadas con hándicap porque duplican la pata de resultado ya incluida.

## No pude evaluar
Cuota real del cupón de Betano y si el builder de Betano admite estas combinaciones; liquidación a 90 min vs prórroga; jugadores (sin alineaciones); 1T/2T (sin estadística por tiempo); el modelo no trae probabilidad propia independiente en goles/resultado.
