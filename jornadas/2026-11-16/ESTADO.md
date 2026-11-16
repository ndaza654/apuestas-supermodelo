# Jornada 2026-11-16 · estado de la recolección (etapa 1) — cerrada ~21:55 Bogotá del 15-nov

**Etapa 1 COMPLETA con límites** para los 11 partidos que el usuario marcó como favoritos en Flashscore (sus capturas mostraban un contador de 13 favoritos; solo 11 son del lunes 16). **El análisis (etapa 2, `correr_jornada.py`) no se ha corrido**: el usuario pidió solo la recolección. Hash de cada archivo verificado contra el navegador.

| Dato | Estado |
|---|---|
| Betano (cuotas leídas 15-nov 20:13–20:14 Bogotá, 11 partidos) | En el repo: `raw/bet_*.txt` y `betano/`. 5 partidos con mercado de jugador de estadística (Alemania–Países Bajos, Grecia–Serbia, Suiza–Escocia con remates/tiros al arco/entradas/faltas; Estonia–Bulgaria y Macedonia–Eslovenia con asistencias); Islas Feroe–Moldavia, Islandia–Luxemburgo, Albacete–Celta B y Canadá–Guatemala solo goleador/tarjeta; Somalia–Ghana y RCA–Benín sin mercado de jugador. |
| Flashscore (10+10 últimos, directos ≤ 6) | En el repo: `flashscore/` (11 partidos). Forma 10/10 en ambos equipos de los 11. Directos: Somalia–Ghana 1, Feroe–Moldavia 3, RCA–Benín 1, Estonia–Bulgaria 1, Islandia–Lux. 3, Alemania–P. Bajos 3, Grecia–Serbia 1, Macedonia–Eslovenia 1, Suiza–Escocia 2, Canadá–Guatemala 3, Albacete–Celta B **0**. Somalia: 9/10 con estadísticas (un partido, Mauricio 31-mar, sin ellas). |
| Alineaciones probables + bajas (Flashscore, ~20:42) | **3 partidos:** Alemania–P. Bajos, Grecia–Serbia, Suiza–Escocia (11+11 cada uno, con bajas). **Los otros 8: sin pestaña de alineaciones** → Estonia–Bulgaria y Macedonia–Eslovenia (que sí traen mercado de jugador) **no recomiendan mercados de jugador** hasta que haya alineación probable o confirmada. |
| **Historial por jugador** (regla obligatoria) | Hecho para los **5 partidos con mercado de jugador de estadística**, pero **cobertura parcial**: 50 de 78 partidos pasados con tabla en Flashscore (28 sin tabla tras 3 intentos). Por equipo: Alemania 10/10, P. Bajos 10/10, Suiza 10/10, Escocia 7/10, Macedonia 8/10, Eslovenia 6/10, Serbia 7/10, **Grecia 4/10, Estonia 4/10, Bulgaria 4/10**. Detalle y partidos faltantes en `jugadores/LEEME.md`. |
| Estadísticas del árbitro | Designado leído para 9 de 11 (`arbitros.json`); **Somalia–Ghana y RCA–Benín sin árbitro publicado**. Referencia de la muestra: 190 partidos recogidos, 4,28 puntos de tarjeta y 25,14 faltas por partido (ambos equipos). Partidos propios de cada árbitro en Flashscore: Jorgji 1, Minakovic 1, Barbu 1, Mallo 1, Nyberg 2, Oliver 3, Makkelie 1, Gozubuyuk 0, Ramos 0 → **muestra mínima, no es base para recomendar tarjetas ni faltas por árbitro**; solo da contexto. |
| Lectura de la situación (tabla, qué se juega, ánimo) | En el repo: `notas/<clave>.json` (11), tablas leídas en Flashscore ~21:00. Detalle de cada equipo (`necesita_ganar`, `le_sirve_empate`, `rotacion`) solo para Canadá–Guatemala; en los demás solo la tabla y lo que se juega. Sin clima ni descanso. |

## Límites declarados
- Flashscore no trae «faltas recibidas»: ese mercado no se recomienda.
- «Entradas» = ganadas; Betano cuenta entradas totales (no son idénticas).
- Los árbitros salen solo de Flashscore (`df_sur`, designado) y de sus partidos en esa misma base; Sofascore da 403 y Transfermarkt no se usó (acceso desde el navegador poco fiable). **Canadá–Guatemala:** el árbitro leído figura con país «Esp» (Ramos C.) para un partido de Concacaf; dato **sin verificar**, puede ser un cruce erróneo de la fuente.
- 28 partidos pasados sin tabla de jugadores en Flashscore (lista en `jugadores/LEEME.md`): el historial de Grecia, Estonia y Bulgaria se apoya en 4 partidos cada uno; la regularidad «X de 10» de esos jugadores no se declara «cumple».
- Cruce de nombres Flashscore↔Betano: pendiente para la etapa 2 (`recoleccion/alias_jugadores.json`).
- Cuotas de Betano del 15-nov 20:13–20:14; si el análisis se hace otro día, hay que **releer** (guardar antes en `betano_previo/` y `raw/previo_HHMM/`, regla de relectura).
- Los datos pasaron transcritos por el chat y se verificaron con hash (3 erratas de transcripción halladas y corregidas por hash de línea en el historial de jugadores).
