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

## 12-nov, cierre (resultados y apuestas)
- Resultados reales de los 9 partidos del 12-nov (Flashscore, `jornadas/2026-11-12/resultados/`). De las 38 líneas de `picks.json`: 24 cumplieron, 9 fallaron y 5 fueron asiáticas con pago parcial (media ganada/perdida, no cuentan como acierto ni fallo). Sobre las 33 completas: 73 % (p media del modelo 69 %). Por tipo: alta 7/8, valor 4/7, extra 13/18. Senegal–Sudán (4-1) tumbó 3 de 3 líneas de goles Menos.
- Boletos del usuario 9–12 nov (13; Betano, solo lectura): en `registro/libro_apuestas.xlsx`, hoja «Boletos 9-12». Dinero real 153.875 apostado, 91.375 cobrado, neto −62.500; 2 de 11 ganados. Sumado a 4–8 nov: neto +12.125 en 59 boletos con dinero real.
- 16 líneas del historial fueron patas exactas de un boleto suyo (columna `apostada` = Sí); solo 4 cumplieron. El resto de sus patas (atajadas, tiros al arco, anota o asiste) no está en el análisis de líneas.

## 13-nov · Serbia–Alemania con Boss Builder (+25 %; 3 patas ≥ 1,50; total ≥ 5)
- Entregado: `jornadas/2026-11-13/boss_builder_serbia-alemania.md`. Mejor trío con precio real ≥ 5: Goles Menos 3.5 + Córners Más 9.5 + Ambos marcan No = 5,00 (p modelo ≈ 19–21 %). Se leyeron ~20 precios del Bet Builder en la página; precio × p del modelo ≈ 1,0 (0,76–1,05): el builder no regala ventaja salvo el bono.
- Hallazgo: con «total ≥ 5» el techo de probabilidad es ≈ 20 %; cualquier trío más probable paga menos de 5.
- Error del lector corregido: líneas por equipo de otros periodos («Serbia tarjetas 1T 0.5») se mezclaban con las de partido completo. Jornadas previas (11 y 12-nov) pueden tener líneas mal puestas; releer si se reutilizan.
- Se midió: nada todavía; resultado del partido se califica mañana (la apuesta la decide el usuario).

## 13-nov · tres informes completos por probabilidad (Países Bajos–Grecia, Escocia–Macedonia del Norte, Eslovenia–Suiza)
- Entregado: `jornadas/2026-11-13/informes_completos/<partido>.md` (generados por `recoleccion/informe_completo.py`; enfoque escrito a mano en `notas/`). Cada uno abre con «Enfoque de mercados» y cubre resultado/goles, córners, estadísticas de partido, tarjetas, jugadores (+ atajadas), parejas y tríos con patas ≥ 1,50, ordenado por probabilidad, no por valor contra la cuota.
- Datos: Betano releído 13:06 Bogotá; alineaciones predichas y últimos 7 de cada jugador, equipo y árbitro desde Sofascore (13:06–13:19, `confirmed:false`), comparadas con las probables de Flashscore del 12-nov (diferencias listadas en cada informe). Jugadores sin historial en Sofascore no se analizan.
- Método de jugadores (cambia respecto a Serbia–Alemania): mezcla Poisson (tasa/90 × minutos) + X de 7 + 1/cuota con pesos 35/35/30 en volumen y 25/15/60 en eventos raros (goles, asistencias, tarjeta), porque con 7 partidos los raros se inflaban frente al mercado. Ajuste favorito/no favorito supuesto, sin calibrar.
- Tarjetas: Poisson con esperado de equipos de Sofascore mezclado 65/35 con el promedio del árbitro; discrepa del modelo en varias líneas (confianza baja, se muestran ambas).
- Corrección: las etiquetas «leído ~13:25–13:35» de los json de Sofascore eran anteriores a la hora real; quedaron como «entre 13:06 y 13:19».
- Se midió: nada todavía; se califica con los resultados del 14-nov.

## 14-nov · recolección de los 21 partidos (sin análisis todavía)
- Entregado: datos en `jornadas/2026-11-14/` (Betano 21/21, contexto Flashscore 21/21, XI probable y bajas 16/21, clima 21/21, clasificación 18/21), con hash verificado archivo por archivo contra el navegador (cada archivo se copió por heredoc y se borró y repitió si no coincidía; hubo 2 desajustes por mi transcripción, corregidos). Pipeline corrido (fichas, informes del modelo, ranking, `registro/lineas.csv` con 12.232 líneas de la jornada).
- Fuentes: Betano (API interna de cuotas, leída 13-nov); Flashscore (feed `df_hh/df_st/df_sui` con `x-fsign`, páginas de alineaciones y clasificación); Open-Meteo (pronóstico). Sofascore no se usó; no se evadió ningún bloqueo.
- Ajuste del extractor de Betano: auto-selección de la pestaña `bt` más completa y filtro FXH2/FYH2; el conteo «14 con id» de la lista era 14 de 21 (los otros 7 se ubicaron con el calendario de la página).
- Código: `armar_entrada.py` ahora lee alineaciones, clima y clasificación (+6 pruebas). Clima a la ficha con umbrales fijos (lluvia fuerte ≥ 7,6 mm/h; viento ≥ 30 km/h; el modelo aplica sus multiplicadores solo si se cumplen o si temperatura < 5 °C: Kosovo, Noruega, Rumanía y Suecia).
- Límites: sin historial por jugador (ningún partido pasa de «no apto» en Jugadores), sin XI en 5 partidos (Banfield–Boca y 4 de Colombia), 3 árbitros sin publicar, sin estadísticas de árbitros. Alineaciones solo probables.
- Se midió: nada todavía; se califica con los resultados del 14-nov (agente `calificacion`).

## 13-nov, 21:55 · balance PARCIAL del 12 y 13-nov (boletos, picks del 12-nov y goles del pipeline)
- Entregado: `entregas/2026-11-13/2155_balance-12-13nov_parcial.html` (generado por `recoleccion/balance_html.py`; datos en `jornadas/2026-11-13/balance/`). Libro `registro/libro_apuestas.xlsx`: boletos 65–77 en «Boletos 9-12» (ahora hasta el 13-nov), nueva hoja «Líneas 12-13 nov» (384 líneas de goles calificadas), lecciones 17–19, Panorama actualizado (4–13 nov: 71 boletos reales, −$1.925).
- Boletos 12–13 nov: 17 reales, 5 ganados, neto −$34.050 (apostado $254.375, cobrado $220.325). Simples +$7.375 vs combinadas/dobles −$41.425.
- Líneas de goles del pipeline (368 con resultado completo): «cumple ≥ 5 de 7» 75 % real vs 42 % «no cumple», pero el precio decía 83 % vs 40 %: sin ventaja sobre el mercado. Picks del 12-nov: 24/33 (73 % vs 69 %); «valor» 4/7.
- Límites: sin estadísticas finales del 13-nov (la ventana emergente de inicio de sesión de Betano bloqueó el navegador y Flashscore no se pudo abrir); marcadores de Moldavia, Andorra, Bulgaria, Eslovaquia, Liechtenstein, Luxemburgo y Morelia tomados del título de la página de Flashscore. Sin leer la apuesta abierta de Betano ni la pata que falló en cada boleto. Inter Bogotá–Santa Fe en curso. Pendiente: córners, tarjetas, remates, jugadores y 1T/2T.
- Nuevo: `recoleccion/calificar_lineas.py` (califica líneas de equipo con un JSON de resultados) y `recoleccion/balance_html.py`.

## 13-nov, 22:40 · balance COMPLETO del 12 y 13-nov
- Entregado: `entregas/2026-11-13/2240_balance-12-13nov.html` (reemplaza al parcial de las 21:55). Libro: notas por pata en los boletos 65–77, hoja «Líneas 12-13 nov» con 4.258 líneas calificadas, lecciones 18–22.
- Equipo (1.460 líneas, 14 partidos, estadística final de Flashscore): «cumple ≥ 5 de 7» 73 % real vs 77 % esperado, ROI −7,5 % con 1 u por línea (sin filtro −6,5 %): separa líneas probables, no da valor. Menos 57 % (ROI −0,9 %) vs Más 44 % (ROI −11,7 %).
- Jugadores (4 partidos con alineación, Sofascore): 1.912 líneas con resultado, 848 anuladas por no jugar; solo 5 «cumple» (4 se dieron); las «no cumple» ROI −61 %; probabilidades de remates/al arco sobrestimadas (41 % vs 59 % en remates 1+).
- Patas de tus boletos: tarjetas Más, goles y patas de jugador tumbaron; córners Más ✓ en 7 patas. Sin identificar: 66, 68 (prórroga) y 75. Apuesta abierta (1): pendiente (sesión de Betano expirada; no se entró con credenciales).
- Límites: jugadores solo en 4 de 14 partidos; Estudiantes–Rivadavia con prórroga en el feed; 1T de saques/al arco/fueras sin estadística por tiempo; Inter Bogotá–Santa Fe pendiente.
- Nuevo: `recoleccion/calificar_jugadores.py`; `balance_html.py` muestra «qué pasó con cada pata» (`patas_calificadas.json`).

## 13-nov, 22:08 · auditoría de todo lo que sugerí (combinadas y sencillas)
- Entregado: `entregas/2026-11-13/2208_auditoria-sugerencias.html` (generador `recoleccion/auditoria_html.py`; datos `registro/sugerencias.csv` armado por `recoleccion/sugerencias.py`). Libro: hojas «Sugeridas» (336 filas) y «Auditoría sugeridas» (fórmulas) + 3 lecciones.
- Sencillas 200/283 (71 %) vs 75 % dicho; cuota < 1,50: 78 % pero −13,6 u a 1 u c/u; 1,50–1,99: 53 %. Combinadas del mismo partido 9/29 (31 %) vs 47 % dicho (las del informe final del 13-nov 3/12 vs 59 %); 2 patas 7/21 (33 % vs 55 %); 3 patas 5/21; 5–6 patas 0/3; Bet Builder Serbia–Alemania 0/4; en vivo 9/12 (75 %). Tuyas de mis variantes: 1 de 3.
- 33 de 46 combinadas fallaron, 17 por una sola pata (goles/resultado 19, córners 15, tarjetas 6). Cambios: máx. 2 patas ≥ 70 % c/u, p conjunta por simulación y recortada, no repetir «córners Más + goles Menos» en varios partidos, cuota < 1,50 = protección.
- Límites: 4–8 nov y combos de misión del 9-nov solo como agregados; una combinada del 12-noche (prórroga) y Luis Suárez «anota» sin verificar; cuota de combinadas = producto/estimada (techo).

## 13-nov, 23:10 · análisis e informe de la jornada del 14-nov (21 partidos, sin navegador)
- Entregado: `entregas/2026-11-13/2310_informe-jornada-14nov.html` (generado por `recoleccion/informe_html.py`, con la pestaña nueva «Análisis»: enfoque de mercados, real hasta hoy, sugerencias con filtros). Texto en `jornadas/2026-11-14/informe_final.md`; detalle de los agentes en `jornadas/2026-11-14/agentes/jornada_<agente>.md` (córners, partido, goles-resultado, tarjetas, combinadas).
- Corrección: al recorrer el pipeline, las fichas calificaban con «7 de 10» una muestra de 7 (nada cumplía). Ahora `ficha.py` detecta la muestra real de la jornada (`muestra_de` / `fijar_muestra`) y usa «5 de 7, n mínimo 5» en fichas, ranking, registro e informe. Con eso cumplen 446 líneas de equipo.
- Nuevo: `recoleccion/analisis_jornada.py` (lo corre también `correr_jornada.py`). Aplica la auditoría: p recortada = p del modelo × el menor factor real (mercado-lado y banda de cuota, suavizado con 20 líneas hacia el global); cuota < 1,50 = protección; 1,50–1,99 = sencilla; combinadas de máximo 2 patas del mismo partido (cada una ≥ 70 % recortada, conjunta de la simulación × 0,80, sin familias con alerta, remates y tiros al arco como una sola familia, cada patrón una vez por día); 3 patas solo lotería; tarjetas y jugadores fuera.
- Sugerencias registradas en `registro/sugerencias.csv` como «pendiente» (58): 38 protecciones, 15 sencillas de 1,50–1,99, 4 combinadas de 2 patas, 1 lotería. `sugerencias.py` las califica solas cuando `registro/lineas.csv` tenga el resultado.
- Real hasta hoy usado para recortar (213 líneas con «cumple» calificadas, 12 partidos): 73 % real contra 77 % dicho; córners Más 24 de 39 (62 % contra 76 %), córners Menos 17 de 20, goles Menos 46 de 59 (78 % contra 87 %), goles Más 21 de 30, tiros al arco 18 de 20, tarjetas Menos 7 de 15.
- Lectura: la p del modelo está pegada al mercado (1 punto de diferencia en promedio); con la p recortada ninguna de las 58 sugerencias tiene EV positivo (el mejor, −8 %). Las 4 combinadas quedan en 48–54 % recortada a cuota producto 1,49–1,61; el agente de combinadas recomienda no apostar ninguna.
- Anomalía Mirassol–Atlético-MG: cerrada. Betano publica escaleras de 23 líneas en tiros al arco, remates y saques de meta; no hay línea mal leída. Series de remates del visitante y saques de meta infladas por partidos desiguales.
- Límites: cuotas del 13-nov 19:01–19:15 sin releer; muestra de 7; alineaciones solo probables en 16 partidos; sin historial por jugador, sin estadísticas de árbitro; situación (previa, motivación, rotación) sin leer, los 21 siguen en «reserva». Pruebas: modelo 106, ficha 27, betano 11, recolección 56.
- Se midió: nada todavía; se califica con los resultados del 14-nov.

## 14-nov, 03:49 · auditoría de todo el repo (tarea programada, solo lectura)
- Entregado: `entregas/2026-11-14/0349_auditoria-repo.html` (filtros por severidad, área y veredicto) y `0349_auditoria-repo.md`. Evidencia y scripts en `jornadas/2026-11-14/auditoria/`. Commit auditado: `11ce7af`. No se cambió código ni datos.
- Conclusión: el repo sirve como registro y análisis honesto, pero no demuestra ventaja sobre Betano. 48 hallazgos: 4 críticos (A1 sin ventaja demostrada, A2 el modelo no mejora al precio, C1 datos transcritos por el chat, G1 reglas de stake del libro sin cumplir), 13 altos, 15 medios, 7 bajos y 9 cosas que están bien.
- Medido (12 partidos de equipo, 4 de jugador): apostar todas las líneas ROI −6,5 % (IC por partidos −11 % a −1 %); «cumple» −7,5 % (IC −21 % a +5 %); Brier mercado 0,2020 contra modelo 0,2047; líneas con el modelo 3 puntos o más sobre el mercado: 35 % real contra 44 % del mercado; «cumple» menos mercado −4,1 puntos; jugadores 11,4 % real contra 23 % dicho.
- El «recorte de p» de `analisis_jornada.py` (13-nov) no pasa la validación dejando un partido fuera: Brier 0,1964 recortada contra 0,1808 cruda. Queda marcado para retirar.
- Boletos reales: 71 con dinero, neto −$1.925; 9–13 nov −$76.550 (ROI −23 %); sin los 2 mejores −$345.316; 17 de 23 boletos del 9 al 13-nov superan el máximo de 7.500 de la hoja «Reglas».
- Pendiente de decisión del usuario: regla de banca, retirar «valor»/EV/recorte, medir cuota de cierre, reconstruir recolección y registro. Nada de eso se hizo en esta tarea.

## 14-nov, 04:00 · análisis de la jornada del sábado (21 partidos, corrida programada)
- Entregado: `entregas/2026-11-14/0400_analisis-jornada-14nov.html` (generado por `informe_html.py`) y `.md` (Enfoque de mercados, 5 mejores líneas por partido, combinadas). Detalle de agentes en `jornadas/2026-11-14/agentes/` (córners, goles-resultado, partido, tarjetas, jugadores, combinadas; 8 partidos con análisis profundo, 13 solo con ficha e informe). Combinadas y sencillas nuevas registradas en `recoleccion/sugerencias.py` (pendientes de calificar).
- Datos/método: Betano leído 13-nov 19:02–19:15 Bogotá; muestra de 7 (cumple ≥5 de 7); modelo SM-1.2; reglas de combinadas de la auditoría del 13-nov (máx. 2 patas ≥70 %, p conjunta por simulación recortada 17,5 %, cuota <1,50 = protección).
- Hallazgo: ninguna línea con ≥5 de 7 en ambos equipos y cuota ≥1,50; los EV son todos negativos salvo ruido y córners Chapecoense local Más 3.5 (+2,3 %, 5/7 y 5/7, partido con alerta del modelo). Jugadores: no apto en los 21.
- Límites: alineaciones probables sin releer, 3 árbitros sin publicar, sin estadísticas de árbitro ni historial por jugador, 5 partidos sin alineación, 13 partidos sin análisis profundo.
- Se midió: nada todavía; se califica con los resultados del 14-nov (agente `calificacion`).

## 14-nov, 14:05 y 14:12 · reanálisis de los 8 partidos de la tarde (a pedido del usuario)
- Entregado: `entregas/2026-11-14/1405_reanalisis-bloque-1445.md` (Portugal–Dinamarca, Irlanda del Norte–Ucrania, Rumanía–Polonia, Suecia–Bosnia) y `1412_reanalisis-bloque-1530.md` (los 4 de Primera A). Líneas de 1,35 o más (preferencia 1,45+) con «cumple 5 de 7», tres Bet Builder de Portugal–Dinamarca (3+ patas de 1,50+, producto 5+) y combinadas entre partidos.
- Datos: Betano releído 13:56 (Europa) y 14:06 (Colombia), solo líneas de equipo (jugadores no releídos); la apertura del 13-nov quedó en `jornadas/2026-11-14/raw_13nov/`. Alineaciones oficiales de Flashscore en los 4 de Europa (~14:00–14:02); Colombia sin alineaciones, con la previa de Flashscore. Pipeline recorrido (muestra de 7).
- Método: p del modelo sin recorte (la auditoría del repo marcó el recorte para retirar); conjunta de las combinadas = producto de las p, sin simulación. Ninguna línea con EV positivo; se dijo en cada entrega junto al «real hasta hoy».
- Registro: 45 sugerencias nuevas «pendiente» (`jornadas/2026-11-14/sugerencias_tarde.json`; `sugerencias.py` ahora lee `sugerencias*.json`).
- Hallazgo aparte: la tarea programada de las 3:45 subió su análisis de la jornada a `main` (commit `2e9d503`, `entregas/2026-11-14/0400_*`), no a esta rama. Sin mezclar; pendiente de decisión del usuario.
- Límites: sin noticias fuera de Flashscore, sin estadísticas de árbitro, clima del 13-nov, el precio real del Bet Builder no se leyó.

## 14-nov, 14:25–14:34 · informe interactivo de la tarde y jugadores de Portugal–Dinamarca
- Entregado: `entregas/2026-11-14/1425_informe-tarde.html`, `1430_jugadores-portugal-dinamarca.md` y `1434_informe-tarde-con-jugadores.html`.
- `informe_html.py`: tarjetas `reanalisis*.md` arriba en «Análisis», tablas en el markdown, filtro «Colchón ≥» (equipo y jugadores), «p modelo ≥» en jugadores y columnas p, EV, esperado, colchón e historial en la pestaña Jugadores.
- Historial por jugador: recolectado solo para Portugal–Dinamarca (Flashscore, pestaña «Estadísticas de jugadores», 10 partidos pasados; `jornadas/2026-11-14/jugadores/`). Sofascore respondió 403/404: no se evadió. Datos transcritos por el chat, sin hash.
- Lectura: en jugadores la p del modelo va pegada al precio y el EV ronda −12 %; solo se informó la regularidad (muestras de 4–6, por debajo del mínimo).
- Corrección: las entregas de los dos bloques se hicieron ~14:05 y ~14:12 (se habían nombrado 1430 y 1448 por una hora mal estimada).

## 14-nov, ~19:00–19:15 · balance parcial e informe v2
- Entregado: `entregas/2026-11-14/1910_balance-parcial.{html,md}` y `1910_informe-v2-{A,B,C}.html`. Libro `registro/libro_apuestas.xlsx`: boletos 78–87 y hoja «Líneas 14-nov» (6.273 líneas calificadas).
- Balance: tus 10 boletos liquidados perdieron o fueron cash-out (neto −$98.450); 2 Bet Builders abiertos. Líneas de equipo con cuota ≥ 1,35: 41 % real contra 41 % del mercado; con «cumple» 5 de 7: 73 % contra 59 % (118 líneas, un día, correlacionadas). Sugerencias: 62 de 93 liquidadas.
- Código: `recoleccion/informe_v2.py` + `plantillas_v2/` (tres diseños, un motor; K, N, n mínimo y equipos ajustables; series por partido y gráficos); `calificar_jugadores.casar_flashscore` («Apellido I.» ↔ nombre de Betano); `recoleccion/flashscore_jugadores.js` (recolector de jugadores con todas las columnas de Flashscore).
- Pendiente: calificar Banfield, Chapecoense, Querétaro y Jamaica–México y los 2 BB abiertos; historial de jugadores de los demás partidos.

## 14-nov, ~19:40 · dashboard: tres prototipos
- Entregado: `entregas/2026-11-14/1940_dashboard-prototipos.md` y tres HTML (A «Mando», B «Móvil», C «Laboratorio»). Código en `dashboard/` (`datos.py`, `src/`, `construir_prototipos.py`); plan en `docs/PLAN_DASHBOARD.md`.
- Mismo motor, 16 páginas, datos del repo en memoria; cambia navegación/densidad. Probado con Playwright a 1440 y 390 px sin errores de consola.
- Pendiente: que el usuario elija diseño y señale mejoras; sigue abierta la lista de decisiones (hosting, entrada de apuestas desde el celular, automatización).

## 14-nov, ~21:20 · recolección de la jornada del 15-nov con historial de jugadores (regla nueva)
- Recolectados 13 partidos del domingo (Betano 19:55, Flashscore, alineaciones 20:16). Historial por jugador completo (10 de 10 partidos por equipo) para los 5 partidos con mercado de jugador de estadística; ver `jornadas/2026-11-15/jugadores/LEEME.md` y `ESTADO.md`.
- Regla nueva en `CLAUDE.md`, `recoleccion/README.md` y el skill `analizar-partido`: sin el historial de esos partidos la recolección no está completa.
- Errores de código hallados y corregidos: (1) con nombres ambiguos (Bellingham, Pašalić, Esposito) el cruce escogía «el primero» y marcaba a Jobe como titular en vez de Jude; ahora se usa el id de Flashscore (`alias_jugadores.json`) y, sin alias, no se asigna; (2) la «ı» turca no se normalizaba (Çakır, Yılmaz, Kadıoğlu, Bardakcı sin historial).
- Chipre–Montenegro sin alineación: sin recomendaciones de jugador. 8 de ~21 favoritos de las capturas no se recolectaron.

## 15-nov, 05:05 · dashboard v2 «Mando»
- Rediseño completo en `dashboard/v2/` (generador `dashboard/construir_v2.py`): estrategia del usuario como filtro en vivo con su resultado en lo ya jugado, gráficos por partido con rival/sede/marcador, escalera de líneas, armador de combinadas con probabilidad y avisos, registro de apuestas. Prueba con las jornadas del 14 y 15-nov. El dashboard anterior (`dashboard/src/`) queda sin tocar.

## 15-nov, ~06:50 · dashboard en línea (GitHub Pages) y unión de ramas
- Hecho: flujo `.github/workflows/dashboard.yml` (cada push a `main` reconstruye `dashboard/construir_v2.py` con todo el registro y publica en Pages), regla «Dashboard en línea» en `CLAUDE.md`, revisión de secretos (archivos e historial: sin claves, tokens ni correos personales; sí códigos y montos de boletos). Link previsto: https://ndaza654.github.io/apuestas-supermodelo/
- Unión: `recoleccion/2026-11-14` se fusionó en `main` (avance simple, sin force). Del 14-nov se conservó la versión de la rama (reanálisis de la tarde); de `main` se añadieron las 6 sugerencias de las 4:00 (S494–S499), sus archivos de agentes, bitácora e índice. 39 marcas «cumple» de Banfield–Boca difieren entre ambas versiones y quedó la de la rama.
- Pendiente del usuario: poner el repo público y activar Pages (Settings → Pages → Source: GitHub Actions); desde aquí el proxy bloquea esos ajustes. La primera corrida construyó bien y solo falló en «configure-pages».

## 15-nov, ~07:45 · histórico del 4 al 15-nov en el dashboard
- Entregado: pestaña «Histórico» (7 vistas) y todos los boletos desde el 4-nov en «Mis apuestas»; análisis en `entregas/2026-11-15/0745_historico-4-15nov-en-dashboard.md`. Datos del 4–8 nov extraídos del libro a `registro/historico_libro.json` (`recoleccion/libro_a_json.py`); cuadran con el libro (48 boletos con dinero, +74.625, 110 de 185 selecciones).
- Hallazgo: elegir solo por cuota 1,40–2,20 pierde claro (−18,7 %, rango −22,9 a −12,9). Tu filtro (regularidad + colchón) separa buenas de malas (+26,5 pts, rango +6,2 a +44,8) pero el grupo que pasa no prueba ganar dinero (+6,5 %, rango −10,0 a +20,0; por jornada +1 %, −17 %, +17 %).
- Corrección: un +13,5 % inicial en selecciones 4–8 era un error (cuota del Bet Builder repetida por selección); ahora solo se calcula precio y ganancia con las 53 selecciones de precio propio.
- Límites: 21–42 partidos por capa; cada capa trae criterios distintos; banca solo 4–8; 15-nov sin resultados.

## 15-nov, 13:36–14:30 · relectura de cuotas, onces oficiales, combinadas BB y contexto por mercado
- Relectura de Betano 13:36 (España–Inglaterra y Bélgica–Italia; hash verificado) y onces oficiales de Flashscore 13:40. Lectura anterior guardada en `betano_previo/` y `raw/previo_1955/`. 310 y 394 cuotas movidas (`cambios_cuotas.json`).
- Entregado: 2 combinadas BB por partido (`entregas/2026-11-15/1400_bb-espana-inglaterra_belgica-italia.md`); recomendado España–Inglaterra. Probabilidades de jugador estimadas por regularidad (7–9 partidos), no del modelo.
- Nuevo: `recoleccion/contexto_mercado.py` (contexto del partido y factores a favor/en contra por mercado, con `notas/<clave>.json`), `recoleccion/cambios_cuotas.py`, y en el dashboard «Contexto del partido», «Contexto de <mercado> en este partido» y «Cuotas que se movieron». Notas escritas para los 4 partidos de Liga de Naciones A con tabla leída; los otros 9 quedan «situación sin leer».
- Límites: criterios de tipsters sin verificar (los del proyecto «Apuestas» no están en el repo); sin estadísticas de árbitro; `registro/sugerencias.csv` no se reescribió en la relectura.

## 15-nov-2026 ~14:45 · Dashboard: orden en Jugadores y filtro de colchón
- Jugadores: selector «Ordenar por» (sentido, probabilidad, colchón, regularidad, cuota) y «Dirección» (mayor a menor / menor a mayor); filtro «Colchón desde».
- Todas las líneas: filtros «Colchón desde» y «Colchón hasta» (las líneas sin colchón calculado se excluyen al usar el filtro). El CSV respeta el filtro.
- El colchón sigue siendo informativo: sin filtro puesto no oculta nada.

## 15-nov-2026 ~14:55 · Dashboard: filtros nuevos en «Lo que te envié»
- Modalidad (sencilla, combinada mismo partido, combinada entre partidos, Bet Builder, en vivo, combinada sin detalle), patas (sencilla, doble, triple, 4 o más), cuota desde/hasta, p desde/hasta (%), resultado (con «parcial») y búsqueda de texto.
- Las barras de acierto ahora van por modalidad y por número de patas, y siguen los filtros. Resumen bajo los filtros: cuántas resueltas se dieron frente a lo que decía la cuota.
- `dashboard/datos.py` agrega `n_patas` a cada sugerencia. En combinadas la cuota es la que estimé en «Crear apuesta», no la de Betano.

## 15-nov-2026 ~17:35 · balance del día (boletos 88–94, líneas y sugerencias calificadas)
- Hecho: leídos los boletos de Betano (solo lectura): hoy 5 boletos, $72.500, todos Perdida (n.º 90–94); los BB del sábado n.º 88 (Chapecoense) y 89 (Banfield) también Perdida (−$15.000). Resultados reales de 12 partidos con Flashscore (`jornadas/2026-11-15/resultados/`) y estadística por jugador de 5 partidos (`jugadores_resultado/`); también se completaron los 4 partidos que seguían pendientes del 14-nov (Chapecoense, Banfield, Querétaro, Jamaica).
- Calificado: 4.619 líneas de jugador y 1.714 de equipo del 15-nov en `registro/lineas.csv`; 151 sugerencias del 15-nov en `registro/sugerencias.csv` (bloque `quince()` en `recoleccion/sugerencias.py`: estrategia 01:45, sugerencias 11:45, BB 14:00, en vivo 16:00). Balance HTML: `jornadas/2026-11-15/balance/balance.html` (copia en `entregas/2026-11-15/`).
- Libro: hojas «Líneas 15-nov» y «Sugeridas 15-nov», boletos 88–94 en «Boletos 9-12», 4 lecciones nuevas.
- Hallazgos: en vivo, mi p media 78 % frente a 25 % real (7 de 24; Betano decía 50 %); tu filtro como sencillas 33 de 48 (+10 % plano) pero sus combinadas 0 de 7; modelo pre-partido bien calibrado. Un solo día: pistas, no pruebas.
- Corrección: `calificar_jugadores.py` no reconocía la «ı» turca y anulaba como «no jugó» a Bardakcı, Yılmaz y Kadıoğlu.
- Pendiente: Panamá–Curazao (18:00); goleador/tarjeta por jugador de 7 partidos sin leer; tarjetas de Jamaica–México no vienen en el feed.


## 15-nov-2026 ~18:20 · Histórico reorganizado: selecciones, picks y partidos de todos los días (4–15 nov)
- Problema: Selecciones y Partidos solo traían el 4–8-nov (libro) y Picks solo el 9 y 11. Ahora cada pestaña cubre 4–15-nov y el Resumen trae «Día por día» (boletos, selecciones, partidos con estadísticas, líneas analizadas, sugerencias, documentos) para ver de un vistazo qué hay de cada día.
- Datos nuevos: `registro/crudo_partidos/2026-11-09…15.txt` (77 partidos leídos de los feeds de Flashscore, estadísticas por tiempo y árbitro), `recoleccion/historico_extra.py` → `registro/historico_9-15nov.json` (168 selecciones de los boletos 52–94 y 79 partidos) y `registro/patas_calificadas_9-12nov.json`.
- Rectificaciones en `patas_calificadas.json`: 13-nov entradas 66, 72, 73, 74 (Más 7,5 córners marcado ✓ con el 9 de otro partido; real 5 en Saint Martin–El Salvador → ✗), 75; 14-nov entrada 78.
- Banca: del 4 al 8-nov el saldo real viene del libro; del 9 al 15 se derivó de los boletos (apostado/cobrado), porque la sesión de Betano está cerrada y no se entró con credenciales.
- Límites declarados: (1) los picks del 4–8-nov eran del modelo viejo y sus líneas por partido no quedaron en el repo (solo el agregado: 72 de 151); (2) 10-nov sin entrega del modelo; (3) Sheffield Wednesday–Accrington y Barnsley–Oldham con estadísticas parciales; (4) Guerreros del Pacífico–FC Santiago sin lista de Flashscore (solo marcador 1-1); (5) Atajadas de Flashscore pueden contradecir el marcador (D. Costa 14-nov) → «sin verificar»; (6) en un Bet Builder solo las selecciones con precio propio (84) sirven para precio; (7) pendientes: Panamá–Curazao, goleador/tarjeta por jugador de 7 partidos del 15-nov, tarjetas de Jamaica–México, y las líneas de jugador de partidos no apostados sin estadística por jugador.

## 15-nov-2026 ~18:50 · análisis de tu estrategia (4 jornadas, 45 partidos)
- Filtro (cuota 1,40–2,20, ≥ 7 de 10 en ambos, colchón > 0), líneas de equipo: 209 líneas / 43 partidos, acierto 67,0 % (la cuota decía 61,8 %), ROI plano +9,3 % (IC95 por partido −6,6 % a +22,7 %). Por día: +14,7, −14,5, +16,2, +10,3 %. «No cumple»: 52,8 %, −7,2 %.
- Por mercado: tarjetas +31 % (positivo 4 de 4 días), remates +23 %, goles +10 %, al arco +11 %; **córners 44 % contra 63 % de la cuota (−29 %, n=36)**.
- Boletos reales 4–15-nov: 1–2 patas −2 %; 3–4 patas −46 % (43 boletos, 8 ganados); 5+ patas +59 % solo por el boleto 7 del 4-nov (sin él −$85.010). Boletos de $30.000 o más: 10, 0 ganados, −$393.095.
- Hoy: patas 22 de 31 (71 %), 0 de 5 boletos; el filtro acertó igual que el 12 y el 14 (~69–71 %), no es récord. Informe: `entregas/2026-11-15/1850_analisis-estrategia-usuario.md`.
- Límites: solo 15-nov es prueba hacia adelante; Panamá–Curazao sin cerrar; criterio sin verificar fuera de estos datos.

## 15-nov-2026 ~19:45 · mapa del supermodelo y los tipsters frente a la estrategia
- El supermodelo SM-1.2 y los sistemas de tipsters siguen en el repo y corren en cada jornada. Medido en 5.875 líneas de equipo: Brier mercado 0,1922, modelo 0,1932, simulación 0,1936 (el modelo no mejora al precio); modelo ≥ 3 pts sobre el precio → 41,6 % de acierto (−25,6 %); dentro del filtro 17 líneas, 35 %. Solo pistas. Informe: `entregas/2026-11-15/1945_donde-esta-el-modelo-y-los-tipsters.md`.
- Límites: `criterios_por_mercado_12nov.md` e `idea_chats_por_mercado.md` están en el proyecto «Apuestas», no en el repo; no existe `sombra.csv`.

## 15-nov-2026 ~20:10 · cierre de Panamá–Curazao (2-0)
- Leído de Flashscore: marcador, estadísticas por tiempo, árbitro, goleadores y quién jugó. Agregado a `registro/crudo_partidos/2026-11-15.txt` y `recoleccion/historico_extra.py` (80 partidos en el Histórico). Calificadas 90 líneas de equipo y 36 de goleador (`jornadas/2026-11-15/resultados/resultados_panama_2005.json`, `jugadores_resultado/..._solo_goles.txt`, solo goles y quién jugó); sugerencias pendientes 16 → 8. Sin boleto tuyo en este partido.
- Estrategia: 211 líneas, 66,8 %, ROI +9,0 % en 44 partidos; sin cambios en las conclusiones.

## 15-nov-2026 ~21:55 · recolección de la jornada del 16-nov (etapa 1, sin análisis)
- Hecho: Betano (11 partidos), Flashscore 10+10 y directos, alineaciones probables (3 de 11), tablas y situación (11), árbitros designados (9 de 11) e historial por jugador de los 5 partidos con mercado de estadística (`jornadas/2026-11-16/`; estado en `ESTADO.md`).
- Cobertura del historial: 50 de 78 partidos pasados con tabla; Grecia, Estonia y Bulgaria con 4/10. 28 partidos sin tabla en Flashscore tras 3 intentos.
- Límites: sin alineación en Estonia–Bulgaria y Macedonia–Eslovenia; árbitros con muestra mínima; Canadá–Guatemala con árbitro de país «Esp» sin verificar. Etapa 2 no corrida.

## 16-nov-2026 ~01:05 · análisis (etapa 2) de la jornada del 16-nov
- `correr_jornada.py` completo con muestra de 10: 166 líneas de equipo con «cumple», 33 protecciones (cuota < 1,50), 7 sencillas 1,50–1,99, 3 combinadas de 2 patas (p recortada 46–49 %), 1 lotería; 44 sugerencias registradas como «pendiente». Situación: 9 aptos, 2 reserva (RCA–Benín, Somalia–Ghana).
- Notas de situación ajustadas (importancia «media»→«normal», alta donde la tabla muestra una definición; «necesita ganar» solo donde la tabla lo respalda). `analisis_jornada.py` ahora toma tabla y árbitro de `contexto/` cuando la ficha no los trae.
- Límites: cuotas del 15-nov 20:13–20:14 sin releer; alineaciones en 3 de 11; árbitros sin tasa fiable; historial de jugadores parcial (Grecia 4/10 → sin recomendación de jugador).

## 16-nov-2026 ~02:04 · backtest de la regla «X de N» en ligas de clubes
- `pruebas/backtest/` (preparar_datos.py, motor.js, hallazgos.js, plantilla.html, construir.py): 50.408 partidos (5 grandes + Brasil, 2000/01–2026/27), misma lectura que la ficha (regularidad, esperado, colchón), sin mirar el futuro. Solo % de acierto.
- Medido con 7 de 10 en ambos: córners Más 8.5 70,6 % (base 65,8 %), Más 9.5 63,3 % (54,4 %), goles Más 2.5 59,3 % (50,0 %), remates Más 22.5 76,8 % (63,8 %), tarjetas Más 3.5 75,9 % (61,2 %). A igual colchón, cumplir o no la regularidad cambia 0–4 puntos. Goles 2.5: acierto con filtro 59,8 % = probabilidad de la cuota 59,7 %.
- Límites: sin líneas ni cuotas de Betano; cuotas solo 1X2 y goles 2.5; Brasil solo goles; sin jugadores ni mitades. La primera versión (01:50, `pruebas/calibracion/backtest_*.py`) se retiró: contaba distinto a la ficha.

## 16-nov-2026 ~02:48 · backtest dentro del análisis y del dashboard
- Tarjetas entran a sugerencias y resumen de la ficha (la exclusión era una regla del código, sin respaldo: con «cumple» Más 24/27, Menos 33/45 = lo que decía el modelo). Hoy entran 3 líneas de tarjetas (1 protección, 2 sencillas) y cambia la lotería.
- `registro/tasas_historicas.json` + `recoleccion/tasas_historicas.py`: tasa de clubes por línea, conteo y colchón; en `analisis_jornada.py` es semáforo (`p_hist`, `hist_sem`), no recorta p. Validada con 817 líneas jugadas (`registro/validacion_tasas.json`): Brier modelo 0,1434, histórico 0,1490, mezcla 75/25 0,1423.
- Dashboard: página «Backtest histórico» (explorador con pestañas Hoy y Mi línea). Datos compactos en `pruebas/backtest/datos.json` (van en el repo para que el workflow construya).
- Límites: clubes y cuotas europeas, sin Betano; solo % de acierto; 9 líneas de hoy sin tasa (asiáticas o mercados no medidos).

## 16-nov-2026 ~17:30 · balance del lunes 16-nov
- Tus boletos (capturas de Betano): 11 de hoy, $97.036 apostados (+$15.000 gratis), $6.536 devueltos (cash out $725 y $5.811), neto −$90.500 (≈24,5 u); con Panamá–Curazao (15-nov, $9.000) −$99.500. 25 de 39 patas se dieron; 6 boletos cayeron por una sola pata (fueras de juego, córners ×3, goles Más 1.5 ×2).
- Mis 6 combinadas: 1 ganada (triple de protecciones 1,80), 5 perdidas (BB Grecia–Serbia: goles de ambos fallaron con 1-0; BB Alemania–P. Bajos: córners 5 y tarjetas P. Bajos 1 punto; «Menos goles» con Alemania 5-0 y Suiza 4-0). Combinada 5 con una pata pendiente (Canadá–Guatemala 20:00) ya perdida por las otras dos. Filas en `registro/sugerencias_extra.csv` (las agrega `sugerencias.py`).
- Líneas de equipo (1.194 calificadas): con «cumple» 125/161 (78 %), sin cumplir 477/1.033 (46 %); estrategia de sencillas 20/31 (65 %), ROI +9,6 %. Un solo día.
- Límites: Canadá–Guatemala y jugadores sin calificar; boletos leídos de capturas, patas sin marca inferidas del BB.
- Archivos: `jornadas/2026-11-16/balance/`, `jornadas/2026-11-16/resultados/resultados_1730.json`, libro (hojas «Boletos 16-nov» y «Líneas 16-nov»).


## 17-nov-2026 (recolección, sin análisis)
Prueba de la pila de recolección «todo el día»: 13 partidos (8 Nations League, México–Jamaica, Copa Colombia ×2, Copa Africana ×2). Betano completo, Flashscore (forma, tabla, previa, bajas, probables), Opta (jugadores NL), historial Flashscore (76/78 partidos de clasificatorio), árbitros ValueStats. Opta y Flashscore coinciden en 318/320 cifras de equipo. Detalle y límites en `jornadas/2026-11-17/ESTADO.md`. Sin sugerencias ni líneas registradas.

### 17-nov-2026 15:00 · Dashboard: filtro propio en «Mi estrategia», orden y estado vacío
- «Mi estrategia» ahora tiene su propio filtro (`ST.est`); lo que se mueva ahí no cambia las otras pestañas (que siguen con `ST.strat`). Botones: «Usar este filtro en todas las pestañas» / «Volver al de las demás pestañas». Presets y «Guardar filtro» actúan sobre el filtro de la pestaña.
- Lista de Estrategia con «Ordenar por» (sentido, probabilidad, cuota, colchón, colchón relativo, regularidad, valor de la línea, mercado, hora) y vista de tabla con columnas ordenables.
- «Todas las líneas»: el estado vacío nombra los filtros activos (p. ej. Resultado «Se dio» en un día sin resultados) con botón «Quitar estos filtros».
- Pendiente anotado: textos fijos «-nov» en pag_historico.js quedarán viejos al cambiar de mes.

## 17-nov-2026 ~17:20 · balance del martes 17-nov
- Tus boletos (Betano → Resueltas, navegador): 8 registrados (n.º 107–114), $96.752 apostados, $56.191 cobrados, neto −$40.561. Los 4 de hoy cayeron ($61.500): Simple BB Dinamarca–Noruega (córners 8 vs Más 9.5), combinada de 4 (Polonia 2 córners y Bosnia–Rumanía 8), combinada de 6 (4 de 10 patas) y combinada de 5 (los 5 grupos fallaron: Ratiu, Gales–Portugal 7 córners, Price/Tóth, Hjulmand, Israel–Austria 13 córners). Ganados: Irlanda U21, Japón–Paraguay, Singapur–Brasil (estaban liquidados y sin registrar).
- Líneas de equipo (1.294 calificadas, 10 partidos): con «cumple» 126/165 (76 %), sin cumplir 530/1.129 (47 %). Jugadores: 4.247 líneas calificadas con Flashscore (343 cumplieron, 1.309 anuladas por no jugar); 318 líneas de México–Jamaica y los dos partidos colombianos siguen pendientes.
- Sugerencias del informe: 28 de 41 sencillas cumplidas, 3 pendientes. Mis picks en vivo (16 líneas añadidas a `registro/sugerencias.csv`): «Menos tarjetas» 3/7; córners/goles 5/6.
- Límites: Flashscore no trae faltas recibidas ni las entradas totales de Betano; los porteros de Rumanía, Austria, Suecia e Irlanda del Norte no vinieron en Flashscore; 2 boletos viejos sin fecha de partido verificada; la cuota 2,02 de «Polonia córners Más 2.5» se transcribió tal cual.
- Archivos: `jornadas/2026-11-17/balance/` (boletos_betano.json, patas_calificadas.json, pendientes.json, balance.html), `jornadas/2026-11-17/resultados/` (resultados_1650.json, jugadores_resultado.txt), libro (hojas «Boletos 17-nov», «Líneas 17-nov», «Sugeridas 17-nov» y 3 lecciones).

## 18-nov-2026 ~22:35 · balance adelantado del miércoles (sin boletos)
- Resultados por investigación web (sin navegador del PC): marcadores de los 11 partidos y estadísticas de equipo parciales en `jornadas/2026-11-18/resultados/resultados_2232.json`.
- Líneas de equipo: 1.446 con resultado; con «cumple» 205/243 (84 %), sin cumplir 506/1.203 (42 %); a igual p del modelo la diferencia es pequeña. Modelo calibrado (27/26, 55/51, 65/64, 75/75, 89/91).
- Sugerencias del informe: 54 se dieron, 17 no, 40 pendientes. Sencillas 1,50–1,99: 7 de 11 con dato. Combinadas mismo partido 2 de 3.
- Límites: sin tus boletos; sin estadística por jugador (solo Kaio Jorge); datos de una sola fuente en Flamengo–Athletico, Corinthians–Botafogo, Häcken–City.
- Archivos: `jornadas/2026-11-18/balance/` (balance.html, pendientes.json), `entregas/2026-11-18/2234_balance-adelantado.md`.


## 2026-11-19 · recolección (sin análisis)
- Recolectados 10 partidos: Champions F ×5, Brasil ×3, MLS Playoffs ×2. Cuotas de Betano ≈08:10 Bogotá. Estado completo: `jornadas/2026-11-19/ESTADO.md`.
- Nuevo: árbitro obligatorio en todos los partidos (ValueStats → `ficha.arbitro`); historial de goleadoras desde incidentes de Flashscore (`goleadores/`).
- Jugadores: Brasil 8–10 de 10 partidos por equipo; MLS 4–9 de 10 (Cincinnati y Seattle cortos); femeninos casi sin tabla en Flashscore (solo goles/asistencias).
- Sin sugerencias enviadas; `registro/sugerencias.csv` no se tocó.


## 2026-11-19 (mañana) · balance completo de la noche del 17 y del 18-nov
- Boletos 115–124 leídos de Betano → Mis apuestas (marca ✓/✗ por selección): los 10 perdidos, apostado 88.939 COP, cobrado 0; 27 de 50 patas se dieron (54 %).
- Resultados reales de Flashscore (feeds df_st/df_su + tablas de jugadores): líneas de equipo de los 17 partidos del 17 y 18-nov calificadas (17-nov 1.462 con resultado, 18-nov 2.448; 2 de Chelsea–PSG 1T sin dato); líneas de jugador 17-nov 3.003 y 18-nov 3.312 (Nations League, México–Jamaica, Brasil ×5 y Champions F ×4).
- Medido: con «cumple ≥ 7 de 10» 79 % (194) el 17-nov y 83 % (403) el 18-nov, sin cumplir 44 % y 40 %. Sugerencias: 17-nov 32 de 48, 18-nov 84 de 115. Jugadores: el modelo daba 22–26 % y se dio 13–14 %.
- Sin tabla de jugadores en Flashscore: Atl. Nacional–Once Caldas, América de Cali–Inter, Utebo–Sabadell, Alcoyano–Mallorca. «anota» de los dos colombianos calificada con incidentes (5 ✓, 35 ✗ jugaron, 57 sin resultado porque no se sabe si jugaron).
- Nuevo: `recoleccion/resultados_flashscore.py`, `recoleccion/jugadores_resultado_pj.py`, `recoleccion/calificar_anota_incidentes.py`, `recoleccion/libro_dia.py` (hojas del libro).
- Libro: hojas «Boletos 17n-18», «Líneas 17-nov» y «Líneas 18-nov» (actualizadas), «Sugeridas 17-nov» y «Sugeridas 18-nov» (reconstruidas desde sugerencias.csv; los id de sugerencias.csv cambian al regenerar), 5 lecciones nuevas.
- Archivos: `jornadas/2026-11-17/balance/` y `jornadas/2026-11-18/balance/` (balance.html, pendientes.json, patas_calificadas.json), `jornadas/2026-11-18/resultados/`.


## 2026-11-19 (10:20) · análisis completo 4–18 nov
- 124 boletos: −416.875 COP en dinero real (117 boletos, ROI −23,5 %); 4–8 +74.625, 9–13 −100.000, 14–18 −391.500. Acierto por pata estable (~60 %); el hundimiento viene de más patas por boleto (4,3 en 14–18), margen de Betano y mala suerte (≈1 % si fueran independientes).
- Filtro «cumple ≥ 7 de 10»: 70–84 % cada día (promedio 81 %), sin tendencia; igual a lo que ya paga el precio (82 %): ROI plano −0,6 %. En 1,40–2,20: 65 % contra 62 % (+5,9 %, ±11 %). «Más»: −15,2 % plano (5.832 líneas); «Menos»: −0,7 % (5.355).
- Segundo paso (cumple + colchón + modelo): no mejora el log-loss del precio fuera de muestra. Herramienta nueva `recoleccion/segundo_paso.py` (validar / ordenar) y `registro/validacion_segundo_paso.json`.
- Jugadores: acierto 12 % contra 24 % del precio (a verificar contra liquidaciones de Betano). Corregido error de calificación de tarjetas de jugador (17 y 18-nov).
- Informe: `entregas/2026-11-19/1020_analisis_4-18nov.md`.


## 2026-11-19 (23:05) · balance del día 19-nov (sin Seattle–RSL, pendiente)
- Boletos 125–131 leídos de Betano → Mis apuestas: 7 liquidados, apostado 118.500 COP, cobrado 201.533 → **+83.033 COP** (1 ganado: doble de 35.000 → 186.533; 1 cash out de 15.000; 5 perdidos). Abierto: Seattle–RSL BB 35.000 @4,00 (pendiente, mañana).
- Calificación con Flashscore (feeds df_st/df_su + Player stats en inglés): 1.831 líneas de equipo (cumple ≥7/10 81,5 % vs no 42,6 %), 2.441 de jugador (1.643 nulas); p del modelo de jugador muy inflada (50–65 % → 30 % real). Sugerencias: 54 de 74 (73 %), ROI plano −3,3 %.
- Patas de tus boletos: cumple 12/15, no cumple 3/7. Fallos típicos: una pata en la mediana (saques de banda 34 vs 36.5, córners 7 vs 8.5), córners Más de femeninas, Ambos anotan Sí, Orlando Menos remates (27 reales vs 12,4 esperados).
- Combinadas/misiones enviadas (no jugadas): BB Boost Vasco A–D ✓ (5,10–5,50), E/F ✗; Vitória A/B ✗; São Paulo ✗; m1 Vitória ✓ 3,25, São Paulo alterna ✓ 3,95, Orlando ✗.
- Libro: hojas «Boletos 19-nov», «Líneas 19-nov», «Sugeridas 19-nov» y 6 lecciones. Pendiente: Seattle–RSL (líneas, sugerencias S7xx, S794, boleto abierto, m1/m2 con Seattle).
- Archivos: `jornadas/2026-11-19/balance/` (balance.html, boletos_betano.json, patas_calificadas.json, pendientes.json, conclusiones.html), `jornadas/2026-11-19/resultados/`.
- (23:25) Nuevo: `recoleccion/calificar_bb.py` califica pata por pata los combos de BB Boost y las misiones (`resultado`, `patas_real`) y el dashboard los muestra en «BB Boost» (SE DIO ✓ / FALLÓ ✗ + valor real). 19-nov: 5 de 17 BB Boost se dieron (Vasco A–D y G); misiones m1 Vitória ✓ y São Paulo alterna ✓, Orlando ✗; Seattle pendiente.
- (23:40) «Lo que te envié» ahora incluye los combos de BB Boost y las misiones (`sugerencias.py → bb_y_misiones()`): 19-nov = 17 BB Boost (5 se dieron) + 7 misiones (2 se dieron, 1 falló, 3 pendientes por Seattle). Regla fija añadida a CLAUDE.md («Lista fija de cada balance») y al agente `calificacion`.

## 19-nov-2026 · Aprender de las combinadas (23:45 Bogotá)
- Nuevo `recoleccion/aprender_combos.py` → `registro/combos_patas.csv` y `registro/aprendizaje_combos.json`: 159 combinadas calificadas (enviadas + boletos tuyos), 40 se dieron (25 %); 72 de 119 perdidas cayeron por una sola pata. 2 patas 43 %, 3 patas 31 %, 4+ patas 4 % (2 de 53). El colchón no predice cuál pata cae (11 de 33 vs ≈ 12,6 por azar); «cumple 7 de 10» sí separa (69 % vs 57 %).
- Reglas: «máx. 2 patas» y «todas las patas cumplen» activas; «evitar pata en la mediana» y «ambos Sí solo con ≥ 7 de 10» en observación (n < 25).
- Integrado en `analisis_jornada.py` (sección «Lo aprendido de las combinadas», columna «Pata de menor colchón») y en el dashboard (Qué funciona y Mi estrategia: «Todo lo enviado y apostado» y «Combinadas: por qué se pierden»). Regla fija añadida a CLAUDE.md y al agente `combinadas`.

## 21-nov-2026 (08:55) · balance del día 20-nov + cierre de Seattle–RSL (19-nov)
- Boletos 132–139 leídos de Betano (Resueltas y Abiertas; ninguna abierta). 20-nov: 7 boletos, $116.000 propios + $15.000 gratis → $220.210 devueltos = **+$104.210** (+$119.585 si el BB Boost de $15.375 del boleto 135 entra en efectivo; por confirmar). Ganaron 3 (BB Bayern–Köln 5,10; combinada de 4 córners/tarjetas 3,02; doble de 2 BB 4,21). Seattle–RSL (1-1) perdió −$35.000 → el 19-nov cierra en +$48.033; los dos días +$152.243.
- Calificado: 6.242 líneas de equipo (38 partidos + Seattle), 3.421 de jugador con las tablas Player stats de 19 partidos (127 líneas sin resultado en 5 partidos sin tabla; solo «anota» con incidentes), sugerencias del informe (sencillas 159/226 = 70,4 %, ROI plano −8,4 %), 8/8 combinadas mismo partido, 13/17 cruzadas, BB Boost 3/15 (las 3 de Bayern–Köln), combinadas enviadas 14:20 (4/4) y 15:52 (8/12). Misiones del 19-nov cerradas con Seattle (m1 Seattle ✗; m2 ✓✓✓).
- Filtro «cumple 7 de 10» en equipo: 80,0 % (772/965) contra 41,4 % sin cumplir; el precio ya descontaba 82,5 %: ROI plano −5,9 %. «Más» con cumple +1,0 %, «Menos» con cumple −10,2 % (lo contrario del acumulado: un día no cuenta). «Menos remates» con cumple 23/53. Modelo en equipo calibrado (±2 pts); en jugador sobreestimado 5–12 pts.
- Herramientas nuevas: `jugadores_resultado_en.py` (tablas EN realineadas → .txt de calificar_jugadores; descuenta goles de prórroga), `calificar_combinadas_enviadas.py` (califica `combinadas_enviadas_HHMM.json` pata por pata), `marcar_apostadas.py` (apostada = Sí desde los boletos), `balance_resumen.py` (cifras de calibración), `calificar_bb.py` ahora califica «Ambos marcan», «X o empate», «Gana» y doble oportunidad, `balance_html.py` acepta `--jornadas AAAA-MM-DD|Prefijo`.
- Libro: hojas «Boletos 20-nov», «Líneas 20-nov», «Sugeridas 20-nov» (y «Líneas 19-nov»/«Sugeridas 19-nov» rehechas con Seattle) + 4 lecciones. Archivos: `jornadas/2026-11-20/balance/`, `jornadas/2026-11-20/resultados/`, `entregas/2026-11-21/0855_balance_20nov.*`.


## 22-nov-2026 (01:45) · balance del 21-nov + histórico 9–21 nov
- Boletos 140–144 leídos de Betano (Abiertas vacío). 21-nov: $102.089 propios → $209.472 = **+$107.383 (+29 u)**; ganó solo el BB de Boca @5,30 con **Bet Builder Boost +50 %** (+$60.452; sin boost +$46.931). Perdieron #140, #141, el gratis #142 y #144 (Once–Nacional BB @5,70 por una pata: tarjetas 1T 3 amarillas de Nacional).
- Calificado: líneas de equipo 13.419 (cumple 82,3 % vs 40,1 %; con cuota < 1,50 ROI −2,5 %; calibración ±0,7 pts), jugadores 7.046 líneas de 35 partidos (4.424 resueltas, 2.622 nulas; 5 partidos sin tabla = 1.047 sin calificar; modelo inflado 7–26 pts), sugerencias 422/594 sencillas, combinadas mismo partido 5/9, cruzadas 3/12, BB Boost 4/22 (Boca 2/4, Once 2/18), combinadas 12:20 2/11.
- Histórico 9–21 nov: −$231.874 (−62,7 u, ROI −19,4 %); 13–18 −$429.000, 19–21 +$259.626. Sugeridas 31 % → 62 %; tus boletos 4,4 → 4,8 patas; BB Boost 12/54 pero 4 de 12 partidos; segundo paso: el precio solo sigue ganando en log-loss (0,5433 vs 0,5449/0,5451); «Menos» y «Más» cambiaron de signo entre 13–18 y 19–21; tarjetas el peor ROI (−13,1 %).
- Libro: hojas «Boletos 21-nov», «Líneas 21-nov», «Sugeridas 21-nov», «Sugeridas 21-nov noche» + 5 lecciones. CLAUDE.md: boost leído del cupón (+50 % en Boca) y «Menos» sin preferencia fija. Archivos: `jornadas/2026-11-21/balance/`, `entregas/2026-11-22/0145_balance_21nov.*`.

## 23-nov-2026 · balance del 22-nov
- Boletos 145–150 leídos de Betano (numeración por orden): propios $129.687 → $207.188 = **+$77.501 (+21 u)**; ganó solo el BB de Liverpool–Man United @5,30 con Boost +25 % (+$34.938). Perdieron #145, #147 (gratis), #148 Getafe (una pata), #149 y #150. Patas 25 de 34 (74 %). Abierto: boleto del 23-nov ($7.500 @7,38).
- Calificado: líneas de equipo 8.739 (cumple 80,6 % vs 40,3 %), jugadores de 15 de 23 partidos (modelo inflado 17–19 pts), sugerencias 224/333 sencillas, BB Boost 3/10 (Liverpool ×2 se agregó al JSON; no se había registrado), combinadas mismo partido 6/8.
- Acumulado 9–22 nov: −$154.373 (ROI ≈ −11,7 %). Sencillas sugeridas 67–74 % todos los días desde el 13-nov; combinadas ≤ 2 patas con «cumple» 24 % → 55–75 %; BB un partido 2/4 vs combinadas multipartido 0/7 en 21–22 nov.
- Archivos: `jornadas/2026-11-22/balance/`, `entregas/2026-11-23/*_balance_22nov.*`. Arreglo: `sugerencias.py` acepta `precio_estimado` numérico.

## 24-nov-2026 (07:50) · balance del 23-nov + análisis del historial de boletos 4–23 nov
- Boletos 151–160 leídos de Betano (Resueltas 16, Abiertas ninguna; numeración por orden): propios $219.442 → $220.642 = **+$1.200**. Ganaron #152 (Inter–Vitória), #156 (doble de 2 BB) y #160 (Taremi + ambos marcan + córners Menos 9.5); #154 y #158 fueron cash out al valor del stake (se habrían perdido); #153 y #159 cayeron por una pata.
- Calificado: líneas de equipo 2.588 (cumple 83,0 % vs 40,3 %; el precio descontaba ≈ 85 %), goleadores con incidentes, sugerencias sencillas 79/108, BB Boost 3/46 (un partido de cinco), combinadas del chat C2 y C3 ✓, C1 y T1 ✗. Líneas de jugador sin tabla (no leída): pendientes.
- Nuevo `recoleccion/analisis_historial_boletos.py` → `registro/analisis_historial_boletos.json`: 160 boletos (4–23 nov), neto −$78.548 (ROI −3,1 %); 45 % de las pérdidas por UNA pata (43 % de ellas por una sola unidad); ≤ 3 patas 25 % ganados vs 4+ 13 %; mercados: córners 31 % de las patas y 51 % de acierto, tiros al arco/faltas/saques de meta/tarjetas Menos los de mayor acierto, remates en 40 boletos con 2 ganados.
- Libro: hoja «Boletos 23-nov», «Líneas 23-nov», «Sugeridas 23-nov» + 4 lecciones. Archivos: `jornadas/2026-11-23/balance/`, `jornadas/2026-11-23/resultados/`, `entregas/2026-11-24/`. CLAUDE.md: regla «Foco por mercados según tu historial».

## 24-nov-2026 (08:45) · líneas de jugador pendientes de 12-nov (noche) a 23-nov
- Tablas Player stats de Flashscore leídas de 63 de 65 partidos con líneas de jugador sin resultado (verificadas contra los totales del partido: 58 de 62 cuadran); calificadas 9 jornadas con `recoleccion/calificar_jugadores_pendientes.py` (nuevo). Pendientes: 57 de goleador del 17-nov (sin tabla), 174 de remates de CFR Cluj–Otelul (la tabla no trae remates).
- Modelo de jugador (12–23 nov, 43.562 líneas jugadas): con todas las líneas acierta 55–70 % de lo que promete (p ≥ 50 % → 45,5 % real contra 64,7 %), pero las 371 que pasan «cumple» + alineación acertaron cerca de la p del modelo (remates 74 % contra 68 %; entradas 76 % contra 76 %) y por debajo de la probabilidad de la cuota; titular acierta más que sin alineación. Detalle: `entregas/2026-11-24/0845_calificacion_jugadores_12-23nov.md`.
- `calificar_jugadores.py`: casa variantes de apellido (Abdullazade/Abdullazada) y limpia la nota «no jugó» al recalificar.

## 24-nov-2026 (22:00) · balance del 24-nov
- Boletos: solo los 2 enviados por captura (#161 Arsenal–Dortmund BB @5,00 $37.500; #162 Millonarios–Bucaramanga BB @5,00 $33.546): **−$71.046**, ambos perdidos por 2 patas (Arsenal 30 remates y 8 córners; Millonarios 2 pts de tarjetas y 10 córners). Betano «Mis apuestas» sin sesión en el navegador: resultados calculados con Flashscore, no con la liquidación.
- Calificado: líneas de equipo 4.304 (cumple 78,5 % vs 43,9 %; el precio daba 79,5 %; Menos 63 % / Más 37 %), sugerencias sencillas 110/166, combinadas mismo partido 5/7, combinadas del chat: A, B, C ✗ (misma pata de Galatasaray) y D1, D2 ✓, D3 ✗; BB Boost 0/4 combos. Pendiente: América–Cali (2-1 en juego), jugadores de estadística (sin tabla), anota solo con incidentes.
- `calificar_combinadas_enviadas.py` ahora entiende saques de meta y de banda. Archivos: `jornadas/2026-11-24/balance/`, `jornadas/2026-11-24/resultados/`, `entregas/2026-11-24/2200_balance_24nov.*`.

## 24-nov-2026 (23:55) · recolección 25-nov, combis de la mañana y pendientes del 24-nov
- Recolección 25-nov (35 partidos: Champions, Youth, J1, ACL): ver `jornadas/2026-11-25/ESTADO.md`. Historial por jugador de la Champions 72 de 91 partidos leídos (Sabah y Shakhtar 3 de 10: ligas sin Player stats). Árbitros: Champions 9/9; J1 y 7 de ACL sin anunciar.
- Combis de la mañana (C1–C3, 3 patas, cuota 2,97–3,26, p modelo 27–33 %): `jornadas/2026-11-25/combinadas_enviadas_2340.json`. Con «cumple» y cuota ≥ 1,60 solo había 2 líneas (mismo partido): no se pudo hacer de 2 patas a cuota 3.
- 24-nov completado: América 2-1 Cali calificado (equipo 48/46; cumple 8 de 10) y 8.955 líneas de jugador con las tablas Player stats de los 16 partidos (`resultados/jugadores_resultado.txt`, nuevo `recoleccion/jugadores_resultado_top.py` para las tablas leídas con `pjTop`). Jugador con «cumple»: 42 de 63 (67 %) contra 74 % del precio. Balance, libro (Líneas/Sugeridas 24-nov), sugerencias, aprendizaje de combos e historial de boletos rehechos.
- Informe 25-nov con «Enfoque de mercados» (`enfoque.md`) regenerado y revisado sin errores de consola.
