# Jornada sáb 21-nov-2026 · estado de la recolección (actualizado 21-nov 01:10 Bogotá)

Selección: los 40 partidos con más mercados en Betano (lectura 20-nov 23:00). 29 con mercado de jugador de estadística (26 completos + 1 casi + 1 medio + 1) y 11 sin mercado de jugador.
**Recolección INCOMPLETA** (se cayó la conexión con el computador a las ~01:00 Bogotá). No hay análisis de esta jornada todavía.

## Hecho
- Betano: mercados y cuotas de los 40 (`betano/`, `raw/`; hash bet_21nov 1240989148).
- Flashscore: últimos 10 de cada equipo + directos + árbitro anunciado de los 40 (`flashscore/`; hash fs_21nov 2891340397).
- Árbitros (ValueStats): 39 de 40 leídos (`arbitros/`). Sin muestra: Falkirk (Stirling C., 0 PJ), Sevilla–Betis (Sánchez, 0 PJ). Dinamo Bucuresti–Petrolul: árbitro no anunciado todavía. Hash arb_21nov_b 985480313.
- Historial de jugadores (29 partidos): 251 de 465 partidos pasados leídos (+8 sin tabla de jugadores en Flashscore). Crudo en `jugadores/crudo_flashscore_en.json`. **Sin decodificar** por corrimiento de columnas (ver `jugadores/LEEME.md`). Hashes de lotes pj_21nov_01..07; 06 = 2386503687, 07 = 4175145318.

## Falta
- Terminar historial de jugadores: ~206 partidos pasados, y volver a leer con el extractor corregido (guarda celdas crudas) para decodificar con alineación verificada.
- Alineaciones probables/oficiales, bajas, previa y tabla de los 40 (la lectura quedó en 6 de 40 y se perdió con la conexión). Sin `alineaciones/`, `notas/`, `paginas/`.
- Notas de contexto, `correr_jornada.py`, informe, BB Boost. Relecturas de cuotas (tarea de las 9:50), onces oficiales y árbitros ~1 h antes de cada partido.

## Límites
- Hasta que se decodifique, ningún mercado de jugador de estadística de esta jornada es recomendable. Goleador/tarjeta no necesitan este historial.
- Flashscore no trae «faltas recibidas» fiable en esta lectura; «entradas» ganadas ≠ entradas totales de Betano.
