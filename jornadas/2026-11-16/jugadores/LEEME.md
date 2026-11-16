# Historial por jugador · jornada lun 16-nov-2026

Regla (CLAUDE.md, 14-nov): los partidos con mercado de jugador de estadística en Betano necesitan el historial de los últimos 10 partidos de cada equipo antes de analizar.

**Partidos con historial (5):** Alemania–Países Bajos, Grecia–Serbia, Suiza–Escocia, Estonia–Bulgaria, Macedonia del Norte–Eslovenia (en Betano traen remates, tiros al arco, entradas, faltas, atajadas y/o asistencias de jugador).
**Partidos sin historial (6):** Somalia–Ghana y RCA–Benín (sin mercados de jugador), Islas Feroe–Moldavia, Islandia–Luxemburgo, Albacete–Celta B y Canadá–Guatemala (solo goleador y/o tarjeta) → no se recolectó (el usuario no los apuesta).

## Fuente y hora
Flashscore (flashscore.co), pestaña «Estadísticas de jugadores» de cada partido pasado (General, Remates, Defensa, Paradas), leída desde el navegador del usuario el 15-nov-2026 entre ~21:05 y ~21:50 Bogotá (horas aproximadas). Los datos pasaron transcritos por el chat y se verificaron con hash (y hash por línea donde falló el primero: 3 erratas de transcripción halladas y corregidas).

## Cobertura real (partidos de los últimos 10 con tabla de jugadores en Flashscore)
| Partido | Local | Visitante |
|---|---|---|
| Alemania–Países Bajos | 10/10 partidos · 51 jugadores | 10/10 · 35 |
| Suiza–Escocia | 10/10 · 32 | 7/10 · 31 |
| Grecia–Serbia | **4/10** · 25 | 7/10 · 39 |
| Macedonia del Norte–Eslovenia | 8/10 · 34 | 6/10 · 26 |
| Estonia–Bulgaria | **4/10** · 25 | **4/10** · 30 |

Total: 78 partidos pasados distintos (algunos los comparten dos equipos), **50 con tabla de jugadores y 28 sin ella**. Los 28 fallaron en la primera pasada y se reintentaron dos veces más (≈ 10 y luego todos); en los reintentos solo se recuperó 1 (Estonia–Islandia 6-oct) y los otros 28 siguen sin tabla («filas 0» con la página cargada). Lo más probable es que Flashscore no publique la tabla de jugadores de esos partidos (cobertura baja en amistosos y eliminatorias menores), pero no se confirmó uno por uno: se declaran como **no leídos**.

Partidos sin tabla (no se pueden completar desde Flashscore):
- **Grecia** (6): Serbia–Grecia 24-sep-26, Bielorrusia–Grecia 18-nov-25, Grecia–Escocia 15-nov-25, Dinamarca–Grecia 12-oct-25, Escocia–Grecia 9-oct-25, Grecia–Dinamarca 8-sep-25.
- **Serbia** (3): Serbia–Grecia 24-sep-26, Serbia–Letonia 16-nov-25, Serbia–Albania 11-oct-25.
- **Escocia** (3): Escocia–Brasil 24-jun-26, Haití–Escocia 14-jun-26, Grecia–Escocia 15-nov-25.
- **Macedonia del Norte** (2): Bélgica–Macedonia 10-oct-25, Macedonia–Liechtenstein 7-sep-25.
- **Eslovenia** (4): Suecia–Eslovenia 18-nov-25, Eslovenia–Suiza 13-oct-25, Kosovo–Eslovenia 10-oct-25, Suiza–Eslovenia 8-sep-25.
- **Estonia** (6): Estonia–Luxemburgo 3-oct-26, Islandia–Estonia 26-sep-26, Estonia–Lituania 9-jun-26, Estonia–Islas Feroe 6-jun-26, Ruanda–Estonia 30-mar-26, Kenia–Estonia 27-mar-26.
- **Bulgaria** (6): Bulgaria–Islandia 13-nov-26, Luxemburgo–Bulgaria 6-oct-26, Indonesia–Bulgaria 30-mar-26, Islas Salomón–Bulgaria 27-mar-26, Bulgaria–Georgia 18-nov-25, España–Bulgaria 14-oct-25.

**Consecuencia para las recomendaciones:** con menos de 7 partidos con datos, la regularidad «X de 10» de un jugador se mide sobre una muestra corta y no se declara «cumple». Los jugadores de **Grecia, Estonia y Bulgaria** (4/10 o 4/10) y de Macedonia del Norte, Eslovenia y Escocia (6–8/10) llevan esa limitación. Mercados de jugador más sólidos por cobertura: **Alemania, Países Bajos y Suiza** (≥ 10/10 o casi). Estonia–Bulgaria no tiene además alineación publicada: sus mercados de jugador **no se recomiendan**.

## Archivos
- `<partido>.json`: por equipo (L = local, V = visitante), jugadores con sus apariciones. Crudos en `../raw/pj_<partido>__<L|V>.txt` (incluyen rating y xG).
- Columnas guardadas por aparición: `[mid, fecha, minutos, remates, a puerta, goles, asistencias, amarillas, rojas, faltas cometidas, entradas ganadas, atajadas, entradas totales]`.

## Límites que se declaran
- Flashscore **no trae «faltas recibidas»**: ese mercado no se puede recomendar con este historial.
- «Entradas» = entradas **ganadas** (la columna trae ganadas/intentadas); Betano cuenta entradas totales: no son idénticas.
- Los remates/tiros a puerta de Flashscore pueden diferir levemente de los de Betano (criterio de cada proveedor).
- Alineaciones: ver `../alineaciones/`; solo Alemania–Países Bajos, Grecia–Serbia y Suiza–Escocia tienen alineación probable (11+11); Estonia–Bulgaria y Macedonia del Norte–Eslovenia no tenían pestaña de alineaciones al leer (~20:42 del 15-nov).
- Cruce de nombres Flashscore↔Betano: **pendiente** (se hace en la etapa 2 con `recoleccion/alias_jugadores.json`); los que ningún partido leído jugó quedan sin historial.
