# Bitácora de análisis y métodos · 4 al 13 de noviembre de 2026

Qué se entregó cada día, con qué modelo y qué criterios, qué se midió y qué límites tiene. Hecha el 12-nov a partir de los documentos del proyecto y del repo. Es la versión legible de `registro/metodos.csv`; las líneas del 9, 11 y 12 de noviembre están en `registro/historial_lineas.csv` (323 líneas con cuota, probabilidad y EV; las del 9 y 11 ya tienen resultado real, las del 12 se califican esta noche; la columna de apuesta está vacía).

## 2026-11-04 a 2026-11-08 · Modelo viejo (v1→v2), antes del supermodelo

- **Qué se entregó:** Líneas sugeridas por partido y boletos recomendados; etiquetas VALOR / «justa» / RIESGO
- **Criterios:** Probabilidad propia con promedios; etiqueta VALOR si el modelo veía ventaja sobre el precio; dominio del día en el simulador (corr. gol–remates 0,34)
- **Medido:** 151 líneas calificadas: 72/151 acertadas (48 %) contra ~50 % del precio. VALOR 5/11, «justa» 10/14, RIESGO 8/22. Boletos recomendados 27/51 (53 %) contra 39/77 (51 %) del resto. En vivo 3 de 13 boletos. Por mercado frente al precio: tarjetas +8, tiros al arco +12, fueras +20, faltas −2, córners −1, goles −7, remates −12
- **Límites:** Muestras de 4 a 30 por grupo: alertas, no reglas. No se calificaron líneas de jugador. 4 partidos sin resultado. El detalle por línea está en la hoja Balance_lineas_sugeridas_4-8_nov_2026.xlsx, no en el repo
- **Fuente:** claude/balance_lineas_sugeridas_4-8nov.md

## 2026-11-09 · Modelo v2 con calibración parcial (DOMINIO q 0,15; FORMA_RITMO 40; FORMA_EQUIPO c 24) y convención sim./ajust. de los combos

- **Qué se entregó:** 6 partidos: «justo», «evitar», líneas con valor y 3 combos de misión
- **Criterios:** Probabilidad = 50 % modelo + 50 % mercado; combos con EV simulado y ajustado; «justo» si EV sim ≥ −1 % y ajustado ≥ −7 %; cuota mínima; leer el total del cupón, no la tarjeta
- **Medido:** Boletos «justo» 5/12 (esperados 4,4; +4,65 u); «evitar» 1/7; combos de misión 0/3; 4 líneas con valor 0/4. Brier modelo 0,1900, combinada 0,1917, mercado 0,1937: no distinguible de cero. Día de pocos goles (11 reales contra 17,2 esperados)
- **Límites:** 6 partidos: nada concluyente. No se sabe qué boletos jugó el usuario. 7 errores propios (combos que dependían de la misma idea, stress de una sola pata, Ambos No con stake pese al aviso, entre otros)
- **Fuente:** claude/balance_9nov.md · claude/calibracion_9nov.md

## 2026-11-10 · SM-1 (supermodelo): calibración con 238.858 partidos reales

- **Qué se entregó:** Sin partidos nuevos: reconstrucción del modelo y prueba de los sistemas de tipsters
- **Criterios:** Base = precio de Betano sin margen por método de potencia; simulador minuto a minuto calibrado con 62.164 partidos; corrección de dependencia entre patas; prior de 38 ligas; alertas de discrepancia (15 pts) y de contexto (10 pts); CLV con cuota de cierre; modo en vivo; revisión independiente
- **Medido:** El mercado le gana a los promedios de goles en todas las ligas (log loss 0,969 contra 0,988). Los sistemas de filtros de tipsters (Ingeniero Analista, Jeke, Sharpods): 20 probados en 160.000+ partidos, ninguno supera el margen. Backtest 5-nov: SM-1 iguala al mercado (Brier 0,2322)
- **Límites:** Las cuotas de calibración son europeas, no de Betano.co. Ningún tipster de córners, tarjetas o jugadores tiene historial verificado
- **Fuente:** claude/calibracion_10nov.md · claude/mapa_de_origen_10nov.md

## 2026-11-11 · SM-1.1 y SM-1.2

- **Qué se entregó:** Combi de 6 partidos (2 líneas cada uno); Turquía–Bélgica a fondo. Reglas fijas: primero leer lo que ofrece Betano, jugadores y parejas siempre, enfoque de mercados al inicio
- **Criterios:** Hoja con media esperada por bloque (modelo contra Betano); «Enfoque de mercados» en palabras; cuota mínima del cupón. Confiables ≥1,30 y de más riesgo 1,50–1,70
- **Medido:** El modelo coincide con el mercado en los 6 partidos; la única «ventaja» (Londrina–Náutico) viene del ajuste de contexto, una hipótesis no medida. Turquía–Bélgica: sin valor verificable. Combinar las 6 patas confiables: cuota 6,77, p ~13 %, EV ≈ −12 %
- **Límites:** Resultados de estos partidos sin calificar todavía. Saques de banda 1T daba un falso valor (+16 %) por un defecto del reparto por tiempos
- **Fuente:** claude/combi_11nov.md · claude/turquia_belgica_12nov.md · claude/supermodelo_guia_rapida.md

## 2026-11-12 (mañana) · SM-1.2 + enfoque de mercados

- **Qué se entregó:** 9 partidos con 3 combinadas; 38 líneas en 3 tipos: alta probabilidad, valor y extra
- **Criterios:** Igual a SM-1.2; contexto = árbitro frente a una referencia de 47 partidos, bajas de 1 a 4 días y clima. Cuotas de las 00:05 (cuota mínima obligatoria)
- **Medido:** El modelo casi no se aparta de Betano; el EV de 1,7 % a 6,7 % viene de hipótesis de contexto, sin validar. Las combinadas tienen una pata por partido; la «exótica» (5 patas, ~11 %) es de alta varianza
- **Límites:** Sin calificar: los partidos se juegan el 12-nov. Curazao–Panamá no tenía cuotas. Referencia de árbitros débil (47 partidos de la Nations League). Bug conocido: saques de banda 1T
- **Fuente:** claude/analisis_12nov.md · claude/retrospectiva_12nov.md · jornadas/2026-11-12/picks.json

## 2026-11-12 (tarde) a 2026-11-13 · Fichas por mercado + agentes en el repo (cambio de método)

- **Qué se entregó:** Jornada del 13-nov: 10 partidos aptos, 87 líneas que cumplen (córners 26, goles 23, partido 19, tarjetas 13, jugadores 6) y 12 combinadas
- **Criterios:** Muestra de 7+7 partidos y directos; regularidad «X de 7» (cumple con 5 o más en ambos); colchón informativo; el objetivo es la probabilidad de la línea, no el error de cuota; el modelo SM-1.2 solo se usa en combinadas, 1X2 y alertas
- **Medido:** Nada medido todavía: la jornada del 13-nov se juega después. Registro lado a lado de ficha y modelo en registro/lineas.csv
- **Límites:** Sin estadística de árbitro, de 1T/2T ni de directos en varios partidos; alineaciones en 4 de 11 partidos; tarjetas solo con amarillas. Los criterios vienen de tipsters y medios sin resultados verificados
- **Fuente:** jornadas/2026-11-13/informe_final.md · claude/criterios_por_mercado_12nov.md

## Lo que falta para cerrar el ciclo

- **Qué apostó el usuario:** ningún documento lo registra (el balance del 9-nov ya lo decía). Las columnas `apostada`, `stake` y `resultado` de `historial_lineas.csv` y `lineas.csv` esperan ese dato.
- **Resultados reales:** los del 11-nov ya están (6 de 12 líneas cumplidas, `jornadas/2026-11-11/resultados/`). Faltan los del 12-nov (esta noche) y los de la jornada del 13-nov; se recogen de Flashscore con el navegador del PC.
- **Líneas del 4 al 8-nov:** solo existen como cifras agregadas y en la hoja Balance_lineas_sugeridas_4-8_nov_2026.xlsx (hoja «Líneas», 151 líneas). Esa hoja no está en el repo ni en el proyecto: hay que subirla para pasarla al historial. Las del 9-nov sí se recuperaron (273 líneas, del apéndice del balance).
- **Lectura honesta hasta hoy:** en todas las pruebas el modelo quedó igual al mercado, y ninguna regla de tipsters o de ficha tiene todavía resultados propios que la respalden.


## Libro consolidado (`registro/libro_apuestas.xlsx`)
Hoja de cálculo para filtrar y auditar: «Panorama» (fórmulas), «Líneas» (las 323 de `historial_lineas.csv`, con columnas amarillas de apuesta), «Métodos» (de `metodos.csv`) y, debajo, las hojas del balance real del 4 al 8-nov del usuario (Boletos, Selecciones, Banca…). Se regenera desde los CSV; el valor de 1 u en su hoja es 3.750 COP (CLAUDE.md dice 3.700: por confirmar).
