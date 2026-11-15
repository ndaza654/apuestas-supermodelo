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
