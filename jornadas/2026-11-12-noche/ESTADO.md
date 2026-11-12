# Jornada 2026-11-12-noche · estado de la recolección (etapa 1) — completa a las ~17:35 Bogotá del 12-nov

Tres partidos de la noche del 12-nov. **Etapa 1 completa** (hash SHA-256 de los `flashscore/*.json` verificado contra el navegador); **etapa 2 ya corrida una vez** (`python3 recoleccion/correr_jornada.py jornadas/2026-11-12-noche`), 3 informes del modelo, 4 pruebas en verde.

| Partido | Hora Bogotá | Torneo | Betano (cuotas leídas ~17:29) | Flashscore |
|---|---|---|---|---|
| Estudiantes de La Plata – Independiente Rivadavia | 18:00 | Supercopa Argentina, **final**, cancha neutra (Córdoba) | 445 mercados: córners, tarjetas, tiros al arco, remates, goles, 1T/2T, jugadores (67) | 7+7, 3 directos, árbitro Pérez Y. |
| Curazao – Panamá | 19:30 | CONCACAF Nations League Liga A, cuartos, **ida** | 197 mercados: goles, córners, tarjetas, 1X2…; **sin** tiros/faltas; jugadores solo «anota» | 7+7, 1 directo, árbitro Penso M. |
| Atl. Morelia – Leones Negros | 21:00 | Liga de Expansión MX, semifinal, **ida** | 37 mercados: goles (total/1T/2T/equipo), resultado, descanso/final, hándicap, 1 línea de córners total (10.5) y 1 de 1T (4.5) | 7+7, 7 directos, árbitro Sánchez M. E. L. |

## Límites (declarados, nada rellenado)
- **Sin alineaciones publicadas** a las 17:35 en Flashscore para ninguno: por la regla 1 no hay mercados de jugadores filtrados. Si salen antes del partido (~1 h antes), leerlas con `recoleccion/flashscore_alineaciones.js` y guardar `jugadores/<clave>.json`.
- **Sin historial por jugador** (no se recolectó) y **sin estadísticas del árbitro**.
- Estudiantes–Rivadavia: bajas de la previa de Flashscore (Correa y Castro en Estudiantes; Arce en Rivadavia) pero Betano aún trae líneas de esos tres. Final: verificar si el mercado se liquida a 90 min o con prórroga.
- Curazao–Panamá: los últimos 7 mezclan Mundial, Nations League y la Kirin Cup (que Flashscore marca como oficial); un solo directo (2023).
- Morelia–Leones: los últimos 7 mezclan fase regular y cuartos de liguilla; casi sin mercados de estadísticas.
- Notas de situación escritas desde la previa de Flashscore; las tablas/clasificación de las ligas no se leyeron.
