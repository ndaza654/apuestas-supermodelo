# Sábado 14-nov-2026 · partidos de la lista de la app (Favoritos)

Hora: Bogotá (UTC−5). Fecha confirmada en Betano (pestaña «MAÑANA» de proximos-partidos-hoy, 14/11).
Estado de la recolección al cierre de esta sesión: ver columna «Betano» y «Sofascore/Flashscore».

| # | Hora | Partido | Liga | Betano (slug · id) | Betano en repo | Sofascore/Flashscore |
|---|---|---|---|---|---|---|
| 1 | 05:15 | Japón – Brasil | Amistosos internacionales | japon-brasil · 95430133 | no (pendiente) | pendiente |
| 2 | 08:00 | Real Valladolid – Castellón | LaLiga Hypermotion | no encontrado en la lista | — | pendiente |
| 3 | 09:00 | Kosovo – Israel | UEFA NL Liga B | kosovo-israel · 94655022 | no (pendiente) | pendiente |
| 4 | 10:15 | Real Sociedad B – Real Sporting | LaLiga Hypermotion | no encontrado en la lista | — | pendiente |
| 5 | 12:00 | Noruega – Gales | UEFA NL Liga A | noruega-gales · 94654191 | no (pendiente) | pendiente |
| 6 | 12:00 | Georgia – Hungría | UEFA NL Liga B | georgia-hungria · 94655045 | no (pendiente) | pendiente |
| 7 | 12:30 | Almería – Andorra | LaLiga Hypermotion | no encontrado en la lista | — | pendiente |
| 8 | 12:30 | Mallorca – Córdoba | LaLiga Hypermotion | no encontrado en la lista | — | pendiente |
| 9 | 14:45 | Portugal – Dinamarca | UEFA NL Liga A | portugal-dinamarca · 94654196 | no (pendiente) | pendiente |
| 10 | 14:45 | Irlanda del Norte – Ucrania | UEFA NL Liga B | irlanda-del-norte-ucrania · 94655063 | no (pendiente) | pendiente |
| 11 | 14:45 | Rumanía – Polonia | UEFA NL Liga B | rumania-polonia · 94655190 | no (pendiente) | pendiente |
| 12 | 14:45 | Suecia – Bosnia y Herzegovina | UEFA NL Liga B | suecia-bosnia-y-herzegovina · 94655081 | no (pendiente) | pendiente |
| 13 | 15:30 | Águilas Doradas – Ind. Medellín | Colombia Primera A Clausura | aguilas-doradas-independiente-medellin · 94698378 | no (pendiente) | pendiente |
| 14 | 15:30 | Atl. Nacional – Once Caldas | Colombia Primera A Clausura | atletico-nacional-once-caldas · 95502674 | no (pendiente) | pendiente |
| 15 | 15:30 | Deportivo Cali – Tolima | Colombia Primera A Clausura | deportivo-cali-deportes-tolima · 95502672 | no (pendiente) | pendiente |
| 16 | 15:30 | Millonarios – Alianza | Colombia Primera A Clausura | millonarios-fc-alianza-fc · 94772407 | no (pendiente) | pendiente |
| 17 | 16:30 | Mirassol – Atlético-MG | Brasil Serie A | mirassol-sp-clube-atletico-mg · 95049971 | no (pendiente) | pendiente |
| 18 | 17:00 | Banfield – Boca Juniors | Copa Argentina | no encontrado en la lista | — | pendiente |
| 19 | 18:00 | Querétaro – Monterrey | Liga MX Apertura | no encontrado en la lista | — | pendiente |
| 20 | 18:30 | Chapecoense – Vasco da Gama | Brasil Serie A | chapecoense-sc-vasco-da-gama-rj · 95049973 | no (pendiente) | pendiente |
| 21 | 20:00 | Jamaica – México | CONCACAF Nations League | no encontrado en la lista | — | pendiente |

## Pendientes de esta sesión
1. Betano: extraer el texto compacto (`extraerBetano`) de los 17 partidos con id y guardarlo en `raw/bet_<slug>.txt`, después `python3 recoleccion/betano.py jornadas/2026-11-14/raw`. Hay que copiar el texto completo (líneas E, L, U, P y R); verificar con `recoleccion/verificar_hash.py` contra el hash del navegador.
2. Betano: ubicar los 4 partidos sin id (Valladolid–Castellón, Real Sociedad B–Sporting, Almería–Andorra, Mallorca–Córdoba) en la página de LaLiga Hypermotion, y Banfield–Boca, Querétaro–Monterrey y Jamaica–México en sus competencias.
3. Sofascore/Flashscore: contexto (últimos 7 de cada equipo, directos, árbitro, alineaciones probables) para cada partido. Sofascore/api.sofascore.com respondió 403 desde la pestaña en esta sesión; las rutas de `/api/v1/event/<id>` sí responden desde la pestaña de sofascore.com.
4. Las cuotas y el marcador de los 3 partidos de la noche anterior ya están en `jornadas/2026-11-13/`; no se mezclan con esta jornada.

Nota: esta sesión no completó la recolección. Se dejó el inventario de los 21 partidos y los ids de Betano, para terminar en una sesión nueva (una sesión por jornada, según CLAUDE.md).
