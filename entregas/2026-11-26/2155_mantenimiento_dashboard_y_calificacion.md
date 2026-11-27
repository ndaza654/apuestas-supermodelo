# Mantenimiento del dashboard y calificación (26-nov-2026, 21:55 Bogotá)
Fuente: Sofascore /api/v1 (leído 21:50–22:00, navegador integrado) y los resultados ya guardados en el repo. Cuotas: sin cambios (Betano 26-nov 15:53 y BB 21:32).

## Qué estaba mal
- La jornada `2026-11-26-noche` se recolectó con Sofascore y el dashboard solo leía las carpetas de Flashscore: salían «no hay alineación» y «falta el historial de jugadores» aunque los datos estaban en el repo.
## Qué se arregló
- `dashboard/datos.py` y `dashboard/construir_v2.py`: leen `sofascore/`, `jugadores_sofascore/` y `alineaciones_sofascore/` cuando no existe la carpeta de Flashscore; el árbitro sale también de `arbitros/<clave>.json`.
- Recorrido en navegador sin cabeza de todas las páginas (15 rutas × 3 jornadas + todas las pestañas de los partidos de las dos últimas jornadas): 245 vistas, 0 errores de consola. Pruebas: dashboard 15, modelo 106, ficha 39, Betano 17, recolección 77.
## Calificación
- 24-nov: tarjetas 1T de Arsenal–Dortmund, Bodø/Glimt–Linz y City–Napoli (0 en el 1T, de los incidentes con minuto).
- 26-nov tarde: Nordsjælland–Panathinaikos con el desglose de 1T de Sofascore.
- 26-nov noche: São Paulo–Remo (3-1) y Montevideo–Nacional (0-1) calificados en equipo; São Paulo–Remo también en jugador (608 líneas; 241 «nula» por no jugar).
- BB São Paulo–Remo: **falló** (principal y alternativa; remates y córners del visitante no se dieron). Combinadas enviadas 22:55 y 23:25: cumplieron.
## Pendiente / límites
- Pachuca–Chivas (2T al momento de leer, 1-1) y León–Cruz Azul (22:10): sin calificar, quedan pendientes (incluido el BB de León).
- Sin dato en ninguna fuente: fueras de juego de Jablonec–Lugano (8 líneas) y Sunderland–Jagiellonia (24 líneas); Montevideo–Nacional no publica 1T ni remates (líneas sin calificar, 100 − las calificadas).
- No hay líneas de jugador de Montevideo–Nacional.
