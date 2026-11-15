# Análisis de tu estrategia (cuota 1,40–2,20 · ≥ 7 de 10 en ambos equipos · colchón > 0)

**Entrega:** dom 15-nov-2026, 18:50 Bogotá.
**Fuentes:** `registro/lineas.csv` (líneas de equipo con resultado real de Flashscore y cuota de Betano leída por el pipeline; jornadas 12-nov noche, 13, 14 y 15), `registro/sugerencias.csv` (596 sugerencias entregadas) y tus boletos 4–15-nov leídos de Betano (94 boletos, 354 selecciones; solo lectura).
**Límites:** 4 jornadas y 45 partidos terminados con líneas de equipo (Panamá–Curazao, 18:00, sin cerrar: sus líneas no cuentan). Las líneas del mismo partido se parecen entre sí, así que los datos efectivos son partidos, no líneas. Líneas de jugador: muestra muy chica con «cumple» (10 líneas), no se evalúan. El filtro se afinó mirando los días 12–14; solo el 15-nov es una prueba hacia adelante (se entregó 01:45, antes de los partidos). Los criterios de tipsters no tienen resultados verificados fuera de estos datos.

## 1. Lo que sentiste, con números
| Jornada | Tu filtro: líneas | Partidos | Acierto | Lo que decía la cuota | ROI plano | Tus patas reales (✓/total) |
|---|---|---|---|---|---|---|
| 12-nov noche | 16 | 3 | 68,8 % | 62,5 % | +14,7 % | 21/28 = 75 % (todo el 12-nov) |
| 13-nov | 37 | 9 | 51,4 % | 60,6 % | −14,5 % | 25/39 = 64 % |
| 14-nov | 108 | 20 | 71,3 % | 61,7 % | +16,2 % | 22/34 = 65 % |
| **15-nov** | **48** | **11** | **68,8 %** | **62,8 %** | **+10,3 %** | **22/31 = 71 %** |
| **Total** | **209** | **43** | **67,0 %** | **61,8 %** | **+9,3 %** | |

- Sí acertamos más que el 13 y el 14 en tus patas reales (71 % contra 64–65 %), pero **no es un récord**: el 12-nov fue 75 % y el 4-nov 71 %.
- El filtro como tal acertó **lo mismo hoy que el 14-nov y el 12-nov noche (≈ 69–71 %)**. El único día malo fue el 13-nov (51 %).
- Fuera del filtro la misma cuota rinde peor: «no cumple» 52,8 % de acierto, ROI −7,2 % (1.533 líneas). «Todas con cuota 1,40–2,20»: 54,6 %, ROI −5,5 % (2.348 líneas). La casa cobra su margen; el filtro lo supera en los 4 días menos el 13.

## 2. ¿Está probado? Todavía no
- Intervalo de confianza 95 % del ROI (remuestreando por partido): **−6,6 % a +22,7 %**. Probabilidad de que el ROI real sea mayor que 0 con estos datos: ~88 %. Es prometedor, **no demostrado**.
- Diferencia acierto − cuota: +5,2 puntos, IC95 −4,4 a +13,3.
- Para confirmar +9 % con cuotas de ~1,64 hacen falta ~290 apuestas independientes; con 43 partidos y días de 40–110 líneas, **unas 3 a 5 jornadas más** con la misma regla, sin tocarla.
- La prueba hacia adelante (15-nov 01:45): sencillas de «Tu estrategia» 39 de 54 (72 %), ROI +17 %; en tabla de equipo, 33 de 48 (+10 %). Las 7 combinadas armadas con esas líneas: 0 de 7.

## 3. Qué funciona y qué no, dentro del filtro
| Mercado | Líneas | Partidos | Acierto | Cuota decía | ROI | Por día |
|---|---|---|---|---|---|---|
| Tarjetas | 29 | 21 | 79 % | 62 % | +31 % | +12, +28, +28, +44 (positivo los 4 días) |
| Remates | 38 | 14 | 74 % | 61 % | +23 % | −27, +63, +43, **−76** (hoy 1 de 6) |
| Goles | 52 | 26 | 69 % | 63 % | +10 % | +7, −31, +9, +32 |
| Tiros al arco | 35 | 16 | 69 % | 63 % | +11 % | +55, −23, +20, −9 |
| **Córners** | **36** | **21** | **44 %** | **63 %** | **−29 %** | +65 (2 líneas), −64, −21, −28 |
| Faltas | 6 | 5 | 33 % | 54 % | −36 % | muestra muy chica |

- **Córners es el hueco del filtro:** cumpliendo ≥ 7 de 10 y con colchón, acierta 44 % cuando la cuota pedía 63 %; peor que sus líneas «no cumple» (56 %). Cae 3 de los 4 días (n=36, 21 partidos: es una pista fuerte, no una prueba).
- **Lado:** Menos 69 % (+13,7 %), Más 64,6 % (+4,1 %). Diferencia pequeña y sin soporte estadístico.
- **Cuota:** 1,40–1,50: 76 % (+9 %); 1,50–1,65: 66 % (+3 %); 1,65–1,80: 55 % (−6 %); 1,80–2,00: 65 % (+23 %); 2,00–2,20: 80 % (+66 %, solo 10 líneas). No hay una banda claramente mejor.
- **Colchón:** ≥ 20 % de la línea 69 % (+10,7 %); 10–20 % 65 % (+8,7 %); 5–10 % 57 % (+1 %). Más colchón ayuda un poco; con muy poco colchón la ventaja desaparece.
- **Regularidad vs colchón:** con colchón > 0 pero sin cumplir regularidad el ROI es −8 %; regularidad + colchón da +9 %. La combinación es lo que separa, ninguna sola.
- **Calibración del modelo dentro del filtro:** p 60–70 % → acierto 72 %; p < 60 % → 61 %. Bien calibrado o conservador.

## 4. Dónde se pierde la plata: no en las líneas, en los boletos
Tus patas aciertan ~62–71 %, pero los boletos suman patas:
| Patas por boleto (4–15 nov) | Boletos | Ganados | Apostado | Neto | ROI |
|---|---|---|---|---|---|
| 1–2 | 23 | 9 | $380.596 | −$6.091 | −2 % |
| 3–4 | 43 | 8 | $793.236 | **−$365.365** | **−46 %** |
| 5 o más | 22 | 4 | $310.100 | +$183.581 | +59 % |
- Los 5+ salen positivos **solo por un boleto** (n.º 7 del 4-nov, combinada de 5 patas, +$268.591). Sin él, el grupo es −$85.010.
- Hoy: 22 de 31 patas (71 %) y **0 de 5 boletos**. Dos boletos grandes (n.º 93 $35.000 y n.º 94 $15.000) cayeron cada uno por **una sola pata** (Remates totales Menos 29,5 con 32; De Ketelaere 1+ a puerta con 0): $50.000 de los $72.500.
- Por tamaño de apuesta: **10 boletos de $30.000 o más, 0 ganados, −$393.095**: más que todo tu resultado neto de los 12 días (−$187.875). Sin esos 10 boletos, el resto es +$205.220 (+18,8 %). Cortar por tamaño después de ver el resultado es una pista, no una ley: con probabilidad de ganar ~18 %, 0 de 10 ocurre ~14 % de las veces. Pero explica que el resultado en plata depende más de cuánto pones por boleto que de cuántas líneas aciertas.
- En las sugerencias que te entregué: sencillas 72 % de acierto (ROI −2 %); combinadas del mismo partido 29 % (−45 %); Bet Builders 1 de 8; en vivo 44 % (−19 %; hoy 7 de 24, −49 %). Mi probabilidad en vivo (65–78 %) estuvo muy por encima de lo real (25–44 %): el en vivo mío no es fiable.

## 5. Para dónde vamos (lo que haría con estos datos)
1. **Mantener la regla tal cual y medirla 3–5 jornadas más** como sencillas de la misma cantidad por línea. No tocar los umbrales cada día: así se contaminan los datos.
2. **Córners con el filtro: pausarlos** (o apostarlos aparte con stake mínimo) hasta que haya más muestra; tarjetas, goles y remates son lo que sostiene el +9 %.
3. **Combinar con tope bajo:** el filtro vale como sencillas o dobles (23 boletos de 1–2 patas: −2 %, casi tablas). Cada pata extra multiplica el riesgo y sube la varianza; los boletos de 3–4 patas pierden ~46 %.
4. **Tope de stake por boleto** (p. ej. no pasar de $20.000–25.000 en combinadas): los 10 boletos grandes sin ganar son más que toda la pérdida neta.
5. **Dejar en vivo fuera hasta tener datos:** 36 sugerencias en vivo mías, 16 se dieron (44 %) contra 55 % que decía la cuota.
6. Cuando termine Panamá–Curazao se suman sus líneas al total (programado 20:05) y se recalcula.

*Cifras reproducibles con `registro/lineas.csv` (filtro: mercado de equipo, cuota 1,40–2,20, `cumple_ficha = sí`, `colchon > 0`, resultado cumplió/falló; ROI plano = cuota de las acertadas / líneas − 1) y `registro/sugerencias.csv`; boletos desde el dashboard (`dashboard/datos.py`).*
