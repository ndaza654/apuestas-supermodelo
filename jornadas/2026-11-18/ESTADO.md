# Estado de la recolección · miércoles 18-nov-2026 (Bogotá)

Recolección hecha entre ≈10:45 y 11:35 Bogotá (cuotas de Betano leídas 10:45; los partidos empiezan 12:45). **No se entregó análisis ni sugerencias**: `correr_jornada.py` corrió para comprobar que todo cuadra (fichas, contexto, registro e informe quedan en el repo), pero las sugerencias no se han enviado ni registrado en `registro/sugerencias.csv`. 11 partidos.

## Qué se recogió y dónde
| Dato | Carpeta | Cobertura |
|---|---|---|
| Betano: líneas, jugadores, parejas, mercados únicos (1X2, doble oportunidad, **ambos marcan**, descanso/final, hándicap…) | `betano/`, `raw/bet_*.txt` | 11 partidos |
| Flashscore: últimos 10 de cada equipo con estadísticas de equipo (+1T), directos (hasta 6), árbitro anunciado | `flashscore/<clave>.json` | 11 partidos, 10 + 10 cada uno (Leuven F: un partido de Copa belga sin estadísticas) |
| Flashscore: tabla, qué se juega, ánimo, bajas | `notas/<clave>.json` | 11 (Copa del Rey: sin tabla; solo datos de la página) |
| Flashscore: alineaciones probables + bajas/suspendidos | `alineaciones/`, `raw/lu_*.txt` | 5 de Brasil (11+11, publicadas «probables»; las oficiales salen ~1 h antes). Femeninos y Copa del Rey: Flashscore no las publica todavía |
| Flashscore: historial por jugador de los últimos 10 partidos oficiales de cada equipo (todas las columnas) | `jugadores/<partido>.json`, `jugadores/LEEME.md`, `raw/pj_*` | 5 partidos de Brasil: **10 de 10 equipos con 10 de 10 partidos** (≈1.500 apariciones) |
| Contexto por partido y mercado | `contexto/` | 11 |

## Betano por partido
| Partido | Líneas de equipo | Mercados únicos | Líneas de jugador | de ellas, de estadística | Mercados en Betano |
|---|---|---|---|---|---|
| BK Hacken (F) – Manchester City (F) | 56 | 15 | 44 | 0 | 166 |
| CD Alcoyano – RCD Mallorca | 14 | 6 | 0 | 0 | 37 |
| Chelsea LFC (F) – Paris Saint-Germain (F) | 55 | 15 | 39 | 0 | 166 |
| Corinthians SP – Botafogo RJ | 199 | 15 | 349 | 258 | 601 |
| Cruzeiro – Palmeiras SP | 201 | 15 | 336 | 248 | 575 |
| Flamengo RJ – Athletico PR | 201 | 15 | 335 | 246 | 569 |
| Gremio RS – EC Bahia BA | 200 | 15 | 358 | 266 | 598 |
| Juventus FC (F) – Oud-Heverlee Leuven (F) | 55 | 15 | 43 | 0 | 164 |
| Real Madrid (F) – Inter de Milán (F) | 56 | 15 | 49 | 0 | 166 |
| Remo PA – Chapecoense SC | 202 | 15 | 419 | 309 | 662 |
| Utebo FC – CE Sabadell FC | 14 | 6 | 0 | 0 | 37 |

- Brasil (5 partidos): remates, tiros al arco, entradas, faltas, atajadas, asistencias, anota/asiste y tarjeta de jugador → **necesitan historial (hecho)**.
- Femeninos (4): córners, goles y tarjetas de equipo; de jugador solo «anota» → no necesitan historial.
- Copa del Rey (Utebo–Sabadell, Alcoyano–Mallorca): Betano solo ofrece goles (total/equipo/1T/2T), 1X2, doble oportunidad, descanso/final, ambos marcan y hándicap; **no ofrece córners ni tarjetas** (no se inventaron).

## Mercados nuevos de esta jornada (petición del usuario)
**Ambos marcan** y **resultado (1X2 y doble oportunidad)** entran como cualquier mercado en los 11 partidos: ficha («X de 10» por equipo y directos), `registro/lineas.csv` (88 filas con p del modelo y EV), análisis, calificación y dashboard (Partido → Resumen). Detalle en `CLAUDE.md`. Para los dos partidos de Copa del Rey el modelo corre solo con goles/1X2/BTTS.

## Límites
- Flashscore no trae «faltas recibidas»; «entradas» son ganadas/intentadas de Flashscore (Betano cuenta entradas totales).
- Lo recogido pasó transcrito por el chat y se verificó con hash (UTF-16, h=h·31+código).
- **No se recolectó:** estadísticas del árbitro (ValueStats/B-Soccer) de Brasil ni de los femeninos — solo el nombre anunciado por Flashscore; volcado completo de mercados (`betano_full/`); clima; qué se juegan los equipos de Copa del Rey (sin tabla).
- «Ambos marcan» y «resultado» no tienen tasa histórica del backtest (no se midieron): el semáforo histórico sale «sin dato»; el «real hasta hoy» usa el factor global hasta tener líneas calificadas.
- Tarjetas: Flashscore solo trae amarillas; Betano cuenta puntos (rojas = 2).

## Pendiente antes de apostar
- Releer cuotas de Betano justo antes de cada partido (copiar `betano/` a `betano_previo/` antes, ver CLAUDE.md) y las alineaciones oficiales (~1 h antes: actualizar `raw/lu_<clave>.txt`).
- Brasil: los mercados de jugador solo con alineación confirmada; hoy son «probables».
