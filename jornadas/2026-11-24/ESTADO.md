# Estado de la recolección · jornada 24-nov-2026 (hecha el 23-nov, 17:20–18:55 Bogotá)

17 partidos: 9 de la Champions League (datos completos) y 8 de la AFC Champions League Elite (resultado, hándicap, goles, córners y goleador).

| Qué | Champions (9) | AFC Elite (8) |
|---|---|---|
| Cuotas y mercados de Betano (leídas 23-nov ~17:21) | todos los mercados (≈200 líneas de equipo, ≈22 únicos, 290–350 de jugador, parejas) | 35–38 líneas de equipo, 14 únicos; goleador solo en 5 partidos |
| Historial de equipos (10 partidos) + directos | sí (directos: 0–1 partido con estadísticas) | sí (igual) |
| Historial por jugador (10 partidos por equipo) | **sí, los 18 equipos: 8–10 de 10 partidos** (`jugadores/LEEME.md` lista los 14 que faltan) | no aplica (Betano no ofrece mercados de jugador de estadística) |
| Árbitro | los 9 (Flashscore + ValueStats) | **no anunciado** todavía en ninguno |
| Goleadores/goleadoras (incidentes de los 10 partidos de cada equipo) | sí (34 equipos, 306 partidos) | sí; Newcastle Jets, Kyoto y Cong An no tienen mercado de goleador en Betano |
| Alineaciones | **probables** de Flashscore (leídas 23-nov ~18:10 Bogotá); las oficiales salen ~1 h antes | Flashscore no las publica; sin leer |
| Tabla, bajas y contexto (notas/) | sí (previa de Flashscore: bajas, tabla, forma) | tabla y forma; sin previa ni bajas |

## Lo que NO se pudo leer (declarado)
- **Árbitros de la AFC:** sin anunciar el 23-nov. Los mercados de tarjetas de la AFC no existen en Betano para estos partidos.
- **Directos:** la mayoría de los cruces no tienen enfrentamientos recientes con estadísticas (0–1); la ficha lo dice.
- **Jugadores:** 14 partidos-equipo de 180 sin tabla de jugadores (Flashscore no la publica para esas ligas/copas o no cargó); esos jugadores quedan con menos de 10 partidos de historial.
- **Cuotas:** una sola lectura (23-nov 17:21), sin releer; hay que releer ~1 h antes (12:45 y 15:00 Bogotá para la Champions) junto con las alineaciones oficiales.
- **Contexto:** lectura de Flashscore (tabla, bajas, previa resumida con palabras propias); los criterios de contexto son reglas generales sin resultados verificados.

## Cómo se recogió (prueba del método nuevo, 23-nov)
Betano y el historial de equipos por feeds (segundos/minutos); goleadores por feeds `df_su` (306 partidos en ≈8 s); tablas de jugadores con iframe + caché de jornadas anteriores (52 de 180 partidos-equipo ya estaban); previas de Flashscore navegando cada partido. Detalle y lecciones: `recoleccion/README.md`.
