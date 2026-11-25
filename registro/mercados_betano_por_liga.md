# Mercados que ofrece Betano por liga (aprendido de las recolecciones)

Se regenera con `python3 recoleccion/mercados_por_liga.py`. Fracción = en qué parte de los partidos vistos apareció la familia la noche anterior (el día del partido Betano puede abrir más, sobre todo de jugador). Regla: si una liga trae estadística de jugador en la mayoría de partidos, traer el historial por jugador aunque esa noche no salga; si la trae pocas veces, releer Betano el día del partido y traerlo solo si aparece.

| Liga | Partidos | Córners | Tarjetas equipo | Goleador | Tarjeta jugador | Partidos con estadística de jugador | Cuáles (→ historial por jugador) | Última |
|---|---|---|---|---|---|---|---|---|
| Liga de Naciones | 46 | 91% | 96% | 91% | 91% | 70% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-17 |
| Brasileirao - Serie A | 19 | 100% | 100% | 100% | 84% | 100% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-25 |
| Champions League | 18 | 100% | 100% | 100% | 100% | 100% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-25 |
| AFC Champions League Elite | 15 | 100% | 0% | 80% | 0% | 0% | — | 2026-11-25 |
| Categoría Primera A | 12 | 100% | 92% | 67% | 0% | 0% | — | 2026-11-25 |
| Ligue 1 | 12 | 100% | 75% | 75% | 25% | 75% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-22 |
| Segunda División | 12 | 100% | 100% | 100% | 0% | 0% | — | 2026-11-22 |
| Champions League (F) | 10 | 100% | 90% | 100% | 0% | 0% | — | 2026-11-19 |
| J1 League | 10 | 100% | 0% | 100% | 0% | 0% | — | 2026-11-25 |
| Premier League | 10 | 100% | 100% | 100% | 30% | 100% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-23 |
| Serie A | 10 | 100% | 100% | 100% | 60% | 100% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-23 |
| Bundesliga | 9 | 100% | 100% | 100% | 22% | 100% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-22 |
| LaLiga | 9 | 100% | 100% | 100% | 44% | 100% | al_arco, anota_o_asiste, asiste, atajadas, entradas, faltas, remates | 2026-11-22 |
| Youth League | 9 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-25 |
| AFC Champions League Two | 8 | 88% | 0% | 0% | 0% | 0% | — | 2026-11-25 |
| Liga MX | 8 | 100% | 50% | 100% | 25% | 50% | al_arco, anota_o_asiste, asiste, remates | 2026-11-25 |
| Liga Profesional | 8 | 100% | 100% | 100% | 12% | 100% | al_arco, anota_o_asiste, asiste, atajadas, remates | 2026-11-25 |
| Copa Africana de Naciones - Eliminatorias | 6 | 67% | 0% | 0% | 0% | 0% | — | 2026-11-17 |
| Liga de Primera | 5 | 100% | 100% | 100% | 0% | 0% | — | 2026-11-22 |
| Nations League Play-offs | 5 | 80% | 80% | 100% | 0% | 0% | — | 2026-11-17 |
| Premiership | 5 | 100% | 100% | 100% | 0% | 100% | al_arco | 2026-11-21 |
| Liga1 | 4 | 100% | 100% | 100% | 25% | 100% | al_arco, anota_o_asiste, asiste, remates | 2026-11-21 |
| MLS | 4 | 100% | 75% | 100% | 75% | 75% | al_arco, anota_o_asiste, asiste, remates | 2026-11-23 |
| Championship | 3 | 100% | 100% | 100% | 100% | 100% | al_arco, anota_o_asiste, asiste, remates | 2026-11-25 |
| Stars League | 3 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-20 |
| Australian Championship | 2 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-20 |
| Copa Colombia | 2 | 0% | 0% | 100% | 0% | 0% | — | 2026-11-17 |
| Copa Del Rey | 2 | 0% | 0% | 0% | 0% | 0% | — | 2026-11-18 |
| Pro League | 2 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-20 |
| Superliga | 2 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-20 |
| 1A Pro League | 1 | 100% | 100% | 100% | 0% | 100% | al_arco | 2026-11-20 |
| A-League | 1 | 100% | 100% | 100% | 100% | 100% | al_arco, remates | 2026-11-20 |
| Amistosos | 1 | 100% | 100% | 100% | 100% | 0% | — | 2026-11-14 |
| CFA Cup | 1 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-20 |
| Copa Argentina | 1 | 100% | 100% | 100% | 100% | 100% | al_arco, anota_o_asiste, asiste, atajadas, remates | 2026-11-14 |
| Copa Sudamericana | 1 | 100% | 100% | 100% | 0% | 100% | al_arco | 2026-11-21 |
| Liga 2 | 1 | 0% | 0% | 0% | 0% | 0% | — | 2026-11-20 |
| Liga de Expansion MX | 1 | 100% | 0% | 0% | 0% | 0% | — | 2026-11-12-noche |
| Primera A | 1 | 100% | 100% | 0% | 0% | 0% | — | 2026-11-21-noche |
| Professional League | 1 | 100% | 100% | 100% | 0% | 100% | al_arco | 2026-11-20 |
| Serie B | 1 | 100% | 100% | 100% | 0% | 0% | — | 2026-11-20 |
| Super League 1 | 1 | 100% | 100% | 100% | 0% | 100% | al_arco | 2026-11-21 |
| Supercopa | 1 | 100% | 100% | 100% | 100% | 100% | al_arco, anota_o_asiste, asiste, atajadas, remates | 2026-11-12-noche |
| Superligaen | 1 | 100% | 100% | 100% | 0% | 100% | al_arco | 2026-11-20 |
