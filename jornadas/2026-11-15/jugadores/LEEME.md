# Historial por jugador · jornada dom 15-nov-2026

Regla (CLAUDE.md, 14-nov): los partidos con mercado de jugador de estadística en Betano necesitan el historial de los últimos 10 partidos de cada equipo antes de analizar.

**Partidos con historial (5):** Bélgica–Italia, Croacia–República Checa, España–Inglaterra, Francia–Turquía, Chipre–Montenegro.
**Partidos sin historial (8):** no traen mercado de jugador de estadística en Betano (solo goleador/tarjeta o ninguno) → no se recolectó (el usuario no los apuesta).

## Fuente y hora
Flashscore (flashscore.co), pestaña «Estadísticas de jugadores» de cada partido pasado (General, Remates, Defensa, Paradas), leída desde el navegador del usuario el 14-nov-2026 entre ~20:20 y ~21:05 Bogotá. Los datos pasaron transcritos por el chat y se verificaron uno a uno con hash (y hash por línea donde falló el primero).

## Cobertura real
| Partido | Local | Visitante |
|---|---|---|
| Bélgica–Italia | 10/10 partidos · 30 jugadores | 10/10 · 41 |
| Croacia–Rep. Checa | 10/10 · 27 | 10/10 · 44 |
| España–Inglaterra | 10/10 · 31 | 10/10 · 34 |
| Francia–Turquía | 10/10 · 33 | 10/10 · 31 |
| Chipre–Montenegro | 10/10 · 34 | 10/10 · 39 |

Los 10 partidos de cada equipo son los mismos de su ficha (últimos 10 oficiales, cualquier sede). Un jugador con pocos partidos aparece con pocas apariciones; la regularidad se mide sobre sus partidos jugados.

## Columnas guardadas por aparición
`[mid, fecha, minutos, remates, a puerta, goles, asistencias, amarillas, rojas, faltas cometidas, entradas ganadas, atajadas, entradas totales]` (más rating y xG en el archivo crudo `raw/pj_*`).

## Límites que se declaran
- Flashscore **no trae «faltas recibidas»**: ese mercado no se puede recomendar con este historial.
- «Entradas» = entradas **ganadas** (la columna trae ganadas/intentadas); Betano cuenta entradas totales: no son idénticas.
- Los remates/tiros a puerta de Flashscore pueden diferir levemente de los de Betano (criterio de cada proveedor).
- Alineaciones: ver `alineaciones/`; **Chipre–Montenegro no tiene alineación publicada** (sin pestaña a las 20:18 del 14-nov), así que sus mercados de jugador no se recomiendan hasta que haya alineación probable o confirmada.
- Hubo fallos temporales de lectura en 9 partidos pasados (tabla sin cargar); se reintentaron y quedaron completos (75/75 con tabla de jugadores).
