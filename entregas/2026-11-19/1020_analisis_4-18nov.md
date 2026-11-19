# Análisis completo del 4 al 18 de noviembre (15 días)
Fecha y hora: 19-nov-2026 10:20 Bogotá.
Fuentes: tus 124 boletos (Betano → Mis apuestas y libro), `registro/lineas.csv` (líneas calificadas del 12-nov noche al 18-nov), `registro/sugerencias.csv`, `registro/metodos.csv`, resultados de Flashscore. Cuotas: las leídas en Betano antes de cada partido.
Límites: de las líneas solo hay detalle por línea desde el 12-nov noche (80 partidos, 11.275 líneas de equipo); del 4 al 11-nov solo están los boletos y cifras agregadas. Las líneas de un mismo partido están correlacionadas: los márgenes de error de abajo son optimistas. Nada de esto prueba el futuro.

## 1. Respuesta corta
1. **El filtro no bajó.** En las líneas registradas acierta entre 70 % y 84 % cada día (promedio 81 %), sin tendencia. Lo que sí pasa es que acierta **lo que ya paga la cuota**: ~80 % de acierto contra 82 % de probabilidad implícita en el precio.
2. **Tus patas tampoco bajaron:** 60,6 % (4–8), 59,0 % (9–13), 60,5 % (14–18). Lo que se hundió fue el dinero: **+74.625 → −100.000 → −391.500 COP**.
3. **Por qué:** boletos con más patas (3,7 → 3,3 → 4,3 por boleto), patas que aciertan ~3–5 puntos por debajo de lo que paga la cuota (el margen de Betano), y mala suerte: con precios justos, un resultado tan malo como el del 14–18 saldría ~1 vez de cada 100 si los boletos fueran independientes (comparten partidos, así que es algo más frecuente).
4. **Un segundo paso (cumple + colchón + modelo + contexto) no le gana al precio de mercado** en la prueba día a día. No es que falte un filtro: el precio ya contiene casi todo lo que miran las fichas.

## 2. Tus boletos (dinero real: 117; 7 gratis aparte)
| Periodo | Boletos | Apostado | Neto | ROI | Ganados | Patas por boleto | Acierto por pata |
|---|---|---|---|---|---|---|---|
| 4–8 nov | 48 | 950.232 | +74.625 | +7,9 % | 12 | 3,7 | 60,6 % |
| 9–13 nov | 25 | 356.200 | −100.000 | −28,1 % | 6 | 3,3 | 59,0 % |
| 14–18 nov | 44 | 469.227 | −391.500 | −83,4 % | 3 | 4,3 | 60,5 % |
| **Total** | **117** | **1.775.659** | **−416.875** | **−23,5 %** | 21 (+5 cash out) | | |

- **Por tipo:** Simple (56, incluye Bet Builders) −32 %; Doble (30) −22 %; Combinada de 3 (14) −33 %; de 4 (11) −100 %; de 5 (5) +168 % (un solo boleto); de 6 (1) −100 %. Por cuota: de 2 a 4 (33 boletos) −4,5 %; de 4 a 8 (48) −57 %; de 8 a 20 (26) +41 %.
- **Todo el +7,9 % del 4–8 vino de un boleto** (combinada de 5 a 10,77: +268.591). Sin los 3 mayores aciertos del periodo completo, el neto sería −833.241.
- Con ~60 % por pata, la probabilidad de acertar un boleto es 36 % con 2 patas, 22 % con 3, 13 % con 4, 8 % con 5. **42 de los 91 boletos perdidos (46 %) cayeron por una sola pata.**
- Tus patas son 80 % «Más» (293 contra 68 «Menos»): «Más» acierta 55–59 %; «Menos» 71–77 %.
- Concentración 14–18: el 13 % de lo apostado tocó Dinamarca–Noruega (4 boletos); México–Jamaica y América–Inter también en 4 boletos cada uno.

## 3. Las líneas (equipo) y el filtro
- 11.275 líneas calificadas. Modelo y mercado están bien calibrados (promedio 49,8 % contra 49,9 % real) y **empatan en error**: log-loss 0,5607 (modelo) contra 0,5603 (mercado).
- **Filtro «cumple ≥ 7 de 10»:** 1.662 líneas, acierto 80,8 %; las que no cumplen, 41,9 %. Pero el precio decía 81,8 %: ROI plano −0,6 %. Sobre la probabilidad del mercado, «cumple» suma +1,3 puntos (no significativo).
- **Dentro de tu rango de cuota 1,40–2,20:** 336 líneas, 65,2 % contra 62,0 % implícito, ROI plano +5,9 % (±11 %: no se distingue de cero). Por día: 69 %, 51 %, 71 %, 68 %, 65 %, 54 %, 68 % (n por día de 16 a 108; los dos días bajos, 13 y 17-nov, tienen 37 y 41 líneas: una oscilación de ±8 a ±15 puntos es ruido).
- Con cuota < 1,40 acierta 85 % pero el precio también (ROI −2,8 %).
- Más estricto no ayuda: con muestra de 10, «mín 8 de 10» +0,3 puntos, «9 de 10» +2,6, «10 de 10» +1,2 (todos dentro del ruido). Con la muestra de 7 (12-nov) el exceso era +3 puntos, tampoco significativo.
- **Lado:** «Más» 5.832 líneas, acierto 43,7 %, ROI plano **−15,2 %** (±3,1); «Menos» 5.355 líneas, acierto 56,7 %, ROI **−0,7 %** (±3,1). Se repite en todos los mercados (Más / Menos): goles −16,2 / −0,9; córners −13,1 / −1,9; tarjetas −17,5 / −3,3; tiros al arco −16,0 / −1,8; remates −11,1 / −0,7. El margen de Betano está cargado en el «Más».
- **Contexto (se juega, necesita ganar, rotación, derbi):** 32 partidos con notas (15–18 nov): diferencia contra el precio ≈ 0 en todos los grupos; las celdas con ±10 puntos tienen ~13 partidos: ruido. Árbitro y alineaciones: solo hay datos desde el 19-nov, aún no se pueden medir.

## 4. Líneas de jugador (13.214 con resultado)
Acierto 12,2 % contra 24,4 % que decía el precio: ROI plano −67 %. Es una brecha demasiado grande para ser solo margen. Dos cosas a verificar antes de concluir: (1) Flashscore cuenta algunas cosas distinto a Betano (entradas, faltas); (2) lo corregí hoy para tarjetas, pero no he podido contrastar las liquidaciones de Betano pata por pata (las 3 patas de jugador que pude comparar coinciden). Mientras tanto: **no hay señal de valor en jugadores, hay señal en contra.**

## 5. Sugerencias del informe (auditoría)
793 sugerencias con resultado: acierto 65,4 %, ROI plano −6,4 %. Por tipo: «protección» (230) 76,1 % contra 79,5 % implícito (−4,5 %); sencillas 1,50–1,99 (64) 60,9 % contra 63,8 % (−5,0 %); estrategia tuya 1,40–2,20 + X de 10 (64) 64,1 % contra 58,1 % (+6,8 %, n pequeño); combinadas de 2 patas (18) −21 %; combinadas del 13-nov (12) −59 %; en vivo 2.º tiempo del 15-nov (24) −49 %. Las sencillas rondan el punto de equilibrio; todo lo que suma patas pierde.

## 6. Qué se puede mejorar (en orden de peso)
1. **Cambiar lo que se mide.** El objetivo no es el % de acierto sino «ventaja = acierto real − probabilidad del precio» y el ROI plano. Un 80 % con cuota 1,25 no gana nada.
2. **Menos patas.** Sencillas y dobles; combinadas de 3+ solo como lotería con stake pequeño. Cada pata añade ~6 % de margen (1/cuota promedio 53 % contra 49,9 % real) y se compone.
3. **Menos «Más».** Donde el filtro cumple, preferir el «Menos»; el «Más» pierde −15 % en 5.800 líneas.
4. **Limitar la exposición por partido** (no más de ~5 % de lo apostado en un mismo partido sumando boletos).
5. **Jugadores en pausa** hasta validar contra las liquidaciones de Betano.
6. **Medir la línea de cierre (CLV):** leer las cuotas dos veces (mañana y ~1 h antes del partido). Si tus líneas se acortan antes del inicio, hay ventaja; es la prueba más rápida y barata.
7. **Hacer crecer la muestra con las variables que el mercado tarda en incorporar:** alineación oficial, árbitro, rotación, clima. Hoy son 80 partidos independientes; para ver una ventaja de 3 puntos hacen falta del orden de 400–600 (unos 2 meses; estimación).

## 7. El «supermodelo» de segundo paso
Lo que pediste (tomar las líneas buenas, analizarlas con simulaciones, estadística, árbitro, alineaciones, qué se juega, y ordenarlas) está implementado como herramienta de medición y orden:
- `python3 recoleccion/segundo_paso.py validar` → prueba día a día, sin mirar el futuro, si «cumple + colchón + lado» o la p del modelo mejoran al precio. Hoy: **no mejoran** (log-loss 0,5566 solo precio; 0,5583 con filtro; 0,5588 con modelo). Resultado en `registro/validacion_segundo_paso.json`.
- `python3 recoleccion/segundo_paso.py ordenar jornadas/AAAA-MM-DD` → para cada jornada, las líneas de cuota 1,40–2,20 que cumplen, ordenadas por probabilidad combinada (modelo + mercado) con etiqueta de calidad (cumple, Menos, muestra completa). Es un orden de **probabilidad y calidad de datos**, no una promesa de ventaja.
- Cómo puede mejorar: cuando haya ~2 semanas con árbitro, alineaciones oficiales y notas de contexto en todos los partidos, se agregan esas columnas a `validar`; si alguna suma, entrará al orden con su peso medido.

## 8. Cambios hechos hoy mientras analizaba
Error corregido: las tarjetas de jugador del 17 y 18-nov se habían calificado todas como falladas (ya recalificadas; libro, balances y lecciones actualizados).
