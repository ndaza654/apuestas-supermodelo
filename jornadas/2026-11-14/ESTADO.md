# Estado · sábado 14-nov-2026 (21 partidos)

Actualizado: vie 13-nov-2026 ~21:00 Bogotá. Rama `recoleccion/2026-11-14` (no está en `main`).

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
8. Flashscore no cuenta rojas en las tarjetas (`y` = amarillas + 2·rojas solo cuando el feed trae rojas): ver la nota de la ficha de tarjetas.

## Cambios al código (este día)
- `recoleccion/armar_entrada.py`: lee `alineaciones/`, `clima/clima.json` y `clasificacion/clasificacion.json` (antes solo Betano + Flashscore); el clima pasa a la ficha como dict con umbrales fijos (lluvia fuerte ≥ 7,6 mm/h, viento fuerte ≥ 30 km/h); la tabla se casa por nombre y, si hay duda, no se adivina.
- `recoleccion/ficha.py`: la ficha imprime la tabla del equipo.
- `pruebas/test_recoleccion.py`: +6 pruebas de lo anterior.
- `recoleccion/betano_extraer.js`: ya corregido antes (elige la pestaña `bt` más completa; filtro FXH2/FYH2).
