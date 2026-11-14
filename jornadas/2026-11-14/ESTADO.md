# Estado · sábado 14-nov-2026 (21 partidos)

Actualizado: vie 13-nov-2026 ~23:10 Bogotá (análisis e informe entregados). Rama `recoleccion/2026-11-14` (no está en `main`).

## Análisis entregado (13-nov ~23:10)
- Pipeline corrido de nuevo con la **muestra de 7** bien declarada: «cumple» = 5 de 7 en ambos (n mínimo 5). 446 líneas de equipo cumplen (goles 178, córners 130, tiros al arco 52, remates 35, tarjetas 30, saques de meta 10, fueras 8, faltas 2, saques de banda 1).
- Informe interactivo con la pestaña «Análisis» (enfoque de mercados, real hasta hoy, sugerencias): copia en `entregas/2026-11-13/2310_informe-jornada-14nov.html`; texto en `informe_final.md`; enfoque en `enfoque.md`; datos en `analisis.json`.
- Sugerencias registradas (58, todas «pendiente» en `registro/sugerencias.csv`): 38 protecciones (cuota < 1,50), 15 sencillas de 1,50–1,99, 4 combinadas de 2 patas y 1 lotería. Con la p recortada ninguna tiene EV positivo.
- Agentes (detalle en `agentes/jornada_<agente>.md`): córners, partido, goles-resultado, tarjetas y combinadas. Jugadores no se corrió: sin historial no hay nada que analizar.
- Anomalía Mirassol–Atlético-MG: revisada, es coherente (Betano publica escaleras de 23 líneas en tiros al arco, remates y saques de meta; no hay línea mal leída ni equipo cambiado). Cuidado con remates del visitante y saques de meta: series infladas por partidos muy desiguales.
- Situación: se leyó lo que hay en las fichas (tabla, clima, tipo de competición); sigue sin previa, motivación ni rotación, así que los 21 quedan en «reserva».
- Boleto abierto del usuario (captura suya, 13-nov 23:22): combinada de 3 Bet Builder, $13.450 a 7,60 (Japón–Brasil, Valladolid–Castellón, Kosovo–Israel), **pendiente**. Guardado en `boletos_usuario.json`; lectura en `entregas/2026-11-13/2324_lectura-boleto-abierto.md` (p conjunta 11 % por simulación, EV −13 %).

## Reanálisis de la tarde (14-nov, 14:05 y 14:12)
- 8 partidos (4 de Liga de Naciones a las 14:45 y 4 de Primera A a las 15:30) con cuotas de Betano releídas hoy (13:56 y 14:06; solo líneas de equipo, apertura en `raw_13nov/`) y alineaciones oficiales en los 4 de Europa. Entregas `1405_reanalisis-bloque-1445.md` y `1412_reanalisis-bloque-1530.md`; 45 sugerencias pendientes en `sugerencias_tarde.json`.
- En `registro/lineas.csv` esos 8 partidos ya no tienen filas de jugadores (no se releyeron); los otros 13 siguen con las cuotas del 13-nov.
- El análisis de la tarea programada (04:00) está en `main`, no en esta rama.

## Recolectado y en el repo (todo con hash verificado contra el navegador)
| Qué | Dónde | Cobertura |
|---|---|---|
| Cuotas y mercados de Betano | `raw/`, `betano/` | 21/21 |
| Contexto Flashscore: últimos 7 de cada equipo (con estadísticas), directos, árbitro, estadio | `flashscore/` | 21/21 |
| XI probable + bajas (Flashscore, probables, 13-nov ~19:15–19:45) | `alineaciones/` | 16/21 (5 sin pestaña) |
| Clima (Open-Meteo, pronóstico 13-nov ~20:00, ciudad del estadio) | `clima/` | 21/21 |
| Clasificación (Flashscore, antes de la jornada) | `clasificacion/` | 18/21 |

Análisis automático ya corrido (`python3 recoleccion/correr_jornada.py jornadas/2026-11-14`): `entradas/`, `fichas/` (21), `informes/` (modelo SM-1.2, 21), `ranking.md` y `registro/lineas.csv` (12.232 líneas de esta jornada). Pruebas: modelo 106, ficha 18, betano 11, recolección 28; todas superadas.

## Lo que falta o se declara (no se rellenó con supuestos)
1. **Historial por jugador** (remates, tiros al arco, faltas, tarjetas por partido): no recolectado. Por eso «Jugadores» sale `no apto` (datos 20–50 < 60) en todos los partidos y las líneas de jugadores quedan sin filtrar por regularidad.
2. **XI/bajas de 5 partidos** (Banfield–Boca y los 4 de Colombia): Flashscore no tiene la pestaña; hay que buscar otra fuente o esperar las oficiales.
3. **Árbitro** sin publicar: Japón–Brasil, Banfield–Boca, Querétaro–Monterrey. **Estadísticas del árbitro** (B-Soccer) no recolectadas en ninguno.
4. **Situación** («sin leer» en el ranking): tabla, motivación, rotación y previa se juzgan en el análisis; las tablas ya están en `clasificacion/` y salen en cada ficha.
5. Betano: sin parejas «cualquiera de los jugadores…» en ningún partido; Colombia, Segunda y Jamaica–México sin remates/al arco/faltas ni tarjetas de jugador; Japón–Brasil solo 175 mercados.
6. Alineaciones **probables**, no oficiales: releer ~1 h antes de cada partido antes de apostar a jugadores. Clima = pronóstico, también se relee.
7. Contexto de competición: Banfield–Boca = semifinal de Copa Argentina (sede neutral, Mendoza); Jamaica–México = Concacaf NL Liga A, playoffs, cuartos de final (ida/vuelta sin verificar).
8. Tarjetas: Betano cuenta en puntos (amarilla 1, roja 2) y la serie de Flashscore puede quedar por debajo si hubo rojas (ver la nota de la ficha de tarjetas).

## Cambios al código (este día)
- `recoleccion/armar_entrada.py`: lee `alineaciones/`, `clima/clima.json` y `clasificacion/clasificacion.json` (antes solo Betano + Flashscore); el clima pasa a la ficha como dict con umbrales fijos (lluvia fuerte ≥ 7,6 mm/h, viento fuerte ≥ 30 km/h); la tabla se casa por nombre y, si hay duda, no se adivina.
- `recoleccion/ficha.py`: la ficha imprime la tabla del equipo.
- `pruebas/test_recoleccion.py`: +6 pruebas de lo anterior.
- `recoleccion/betano_extraer.js`: ya corregido antes (elige la pestaña `bt` más completa; filtro FXH2/FYH2).
