# Estado de la recolección · martes 17-nov-2026 (Bogotá)

Recolección hecha la noche del lun 16-nov (≈22:45–00:15 Bogotá). **No hay análisis ni sugerencias todavía** (el usuario las pedirá después). 13 partidos.

## Qué se recogió y dónde
| Dato | Carpeta | Cobertura |
|---|---|---|
| Betano: líneas, jugadores, parejas, mercados únicos | `betano/`, `raw/bet_*.txt` | 13 partidos |
| Betano: volcado completo de mercados | `betano_full/` | 13 partidos (70–679 mercados únicos leídos; declarados 130–926) |
| Flashscore: últimos 10 de cada equipo con estadísticas de equipo (+1T), directos, árbitro anunciado | `flashscore/<clave>.json` | 13 partidos, 10 + 10 cada uno |
| Flashscore: tabla de posiciones | `flashscore/tabla_lineups_crudo.json` | 10 de 13 (Copa Colombia ×2 y México–Jamaica: sin tabla) |
| Flashscore: previa y bajas | `flashscore/previa_bajas_crudo.json` | 8 Nations League con previa; resto sin previa publicada |
| Flashscore: alineaciones probables | `alineaciones/` | 9 (8 NL + México–Jamaica), 11+11; las oficiales salen ~1 h antes |
| Opta: jugadores y equipos de la Nations League | `opta/`, `jugadores/`, `equipos/` | 40 partidos, 5 por equipo de los 16 equipos de NL, todos con minutos |
| Flashscore: historial por jugador de clasificatorios del Mundial | `jugadores/`, `flashscore/jugadores_pj_crudo.json` | 76 de 78 partidos |
| Árbitros (ValueStats) | `arbitros/` | NL ×8 + Sorto (México–Jamaica) + Athoumani (Tanzania–Nigeria) |
| Contexto de situación por partido | `notas/` | 13 (solo hechos de tabla y previa) |

## Historial de jugadores (regla de CLAUDE.md)
Necesitan historial los 8 partidos de Nations League (Betano ofrece remates, tiros al arco, entradas, faltas, atajadas y/o asistencias de jugador). **No** lo necesitan: México–Jamaica, Atlético Nacional–Once Caldas y América de Cali–Inter Bogotá (solo goleador/tarjeta) ni Malaui–Egipto y Tanzania–Nigeria (sin mercados de jugador).
Cobertura de los últimos 10 partidos oficiales por equipo: **14 de 16 equipos con 10/10**; Bosnia 9/10 y Irlanda 9/10 (un clasificatorio sin tabla de jugadores en Flashscore). Detalle en `jugadores/LEEME.md` y `opta/LEEME.md`.

## Control de calidad
- Opta vs Flashscore en los 40 partidos de Nations League (remates, tiros al arco, córners, faltas por equipo): 318 de 320 cifras iguales; 2 de córners difieren por 1.
- El pipeline (`correr_jornada.py`) corrió sobre una copia temporal del repo con estos datos sin errores (13 fichas, 13 contextos, informe). No se ejecutó en el repo: `registro/lineas.csv` y `registro/sugerencias.csv` quedan sin tocar hasta que se pida el análisis.

## Qué falta / límites
- **Árbitros sin leer:** Malaui–Egipto (Flashscore no lo anuncia), Atl. Nacional–Once Caldas y América–Inter Bogotá (sin árbitro publicado). ValueStats: faltas por partido de cada árbitro requieren cuenta; sin ella solo hay tarjetas por partido y totales por competición. Maļcevs y Matoša tienen casi nada en selecciones.
- Alineaciones: sin publicar en Copa Colombia ni Copa Africana. Son «probables» de Flashscore; confirmar con las oficiales antes de apostar mercados de jugador.
- Sin historial de jugadores: 2 partidos (ver arriba). Flashscore no trae «faltas recibidas» (Opta sí, en el campo `opta` de los 8 partidos NL).
- Nombres de jugador: Opta («I. Apellido») se convirtió a «Apellido I.»; unos pocos jugadores pueden figurar duplicados entre fuentes (p. ej. Sudakov G./H.). Revisar con `alias_jugadores.json` antes de usarlos.
- Columna «C» del resumen Opta sin confirmar (despejes o centros).
- Los datos pasaron por el navegador y se bajaron como archivo (no transcritos por el chat). Cuotas Betano leídas el 16-nov ~23:05 Bogotá: releer antes de apostar.

## Actualización 17-nov 13:55 Bogotá (Dinamarca–Noruega)
- Cuotas de Dinamarca–Noruega releídas 13:40 (`raw/bet_dinamarca-noruega.txt`); lo anterior (01:00) en `raw/previo_0100/`. Resto de partidos: cuotas de las 01:00 sin releer.
- Onces oficiales de Dinamarca–Noruega leídos 13:42 (Flashscore). Los demás partidos siguen con alineación probable.
- Árbitro de Dinamarca–Noruega con promedio de tarjetas y faltas (ValueStats, sesión del usuario): `arbitros/valuestats_meler_20.json`.
- Muestra incompleta: saques de meta (Dinamarca 5 de 10, Noruega 8 de 10; Flashscore no trae el dato en clasificatorios del Mundial) y tarjetas de Noruega (9). Esas líneas no se recomiendan. Hermansen: 5 partidos (los otros 5 jugó otro arquero).
- Corregida la fusión de nombres con ø/æ/ł (Ødegaard, Højlund…) en `pj_json_decod.py` + `jugadores_fusionar.py`.

## Actualización 17-nov 14:10 Bogotá (los 7 partidos de las 14:45)
- Cuotas releídas 13:58 (`raw/bet_*.txt`; las de las 13:40 en `raw/previo_1340/`). Onces oficiales leídos 13:59 en 6 de 7; **Polonia–Suecia sin pestaña de alineaciones** (solo probables).
- Árbitros con 20 partidos (tarjetas y faltas, ValueStats): `arbitros/valuestats_arbitros_1400.json` y en `notas/`.
- Colombia y México–Jamaica siguen con cuotas de las 01:00 y sin árbitro.
