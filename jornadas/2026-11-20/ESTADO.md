# Estado de la recolección · viernes 20-nov-2026 (partidos 03:30–10:30 Bogotá)

Recolección hecha el jue 19-nov entre ≈21:55 y 22:35 Bogotá. Cuotas de Betano leídas ≈21:59 (una sola lectura, **sin releer**: faltan los movimientos del día). Alcance: los 19 partidos del bloque 00:00–10:30 con más mercados en Betano; los demás partidos del día (y los 7 de nivel medio) quedan para cuando el usuario los mande.

## Qué se recogió y dónde
| Dato | Carpeta | Cobertura |
|---|---|---|
| Betano: líneas, jugadores, mercados únicos (1X2, doble oportunidad, ambos marcan) | `betano/`, `raw/bet_*.txt` | 19 de 19 |
| Flashscore: últimos 10 de cada equipo con estadísticas de equipo + directos (hasta 6) + árbitro anunciado + estadio | `flashscore/<clave>.json` | 19 de 19. Menos de 10 con estadísticas: Hammam-Sousse (7), Sakiet Eddaier (8), East Bengal–SC Delhi (6 del SC Delhi), FC Bihor (9). Directos: 0 en Vissel–Mito, 1 en South Melbourne–Canberra, Al-Sadd–Lusail, Hammam-Sousse–Sakiet y Hammam-Lif–Metlaoui |
| Tabla, forma, estadio, bajas (texto de la página del partido) | `paginas/<clave>.txt`, `notas/<clave>.json` | 18 de 19 con tabla; **Beijing–Shanghai Port: Flashscore no publica tabla** (situación sin leer). Las notas solo traen hechos de la tabla y la forma: no hay lectura de motivación ni de «necesita ganar» |
| **Árbitro (regla fija)** | `arbitros/<clave>.json`, `arbitros_valuestats_crudo.json` | Anunciado en **5 de 19**: King (WSW–Adelaide), Flueran (Botosani–Voluntari), Al Jassim (Al-Duhail–Qatar SC) y Falahi (Al Gharafa–Al Arabi) con historial de ValueStats; **Al Sharshani (Al-Sadd–Lusail) anunciado pero no está en ValueStats: sin historial**. Los otros 14 **no estaban anunciados** a las 22:30 del jueves |
| Alineaciones probables + bajas | `alineaciones/` | Solo **WSW–Adelaide y Botosani–Voluntari** (probables, no oficiales; Flashscore publica las oficiales ~1 h antes). Los otros 17 no tienen pestaña/alineación todavía |
| Historial por jugador (todas las columnas de Flashscore, últimos 10) | `jugadores/<partido>.json`, `jugadores/LEEME.md`, `jugadores/crudo_flashscore_en.json` | Solo los 2 partidos con mercado de jugador de estadística (ver abajo) |
| Contexto por partido y mercado | `contexto/` | 19 de 19 (solo datos y tabla; situación sin leer) |

## Historial por jugador: cobertura real
| Partido | Local | Visitante | Qué faltó |
|---|---|---|---|
| Western Sydney – Adelaide United | 10 de 10 (28 jugadores) | 9 de 10 (25) | Adelaide vs Cong An Ha Noi (11-ago, copa asiática): Flashscore no publica estadísticas de jugadores |
| FC Botosani – FC Voluntari | 8 de 10 (24) | 8 de 10 (21) | Botosani vs UTA Arad (27-oct) y vs Corvinul (2-sep); Voluntari vs Univ. Craiova (29-oct) y vs Chindia Târgoviște (1-sep): sin estadísticas de jugadores en Flashscore |

Los 3 partidos de Japón (Kashiwa, Kashima, Vissel) solo ofrecen goleador (`anota`): no necesitan historial de estadística, y el usuario no pidió goleador para esta jornada, así que no se trajo historial de goles por jugador. Los otros 14 no traen mercado de jugador.
Los jugadores con menos de 7 partidos de historial no pasan el filtro «7 de 10»; sus líneas salen como «sin muestra».
**Novedad:** la versión en inglés de Flashscore sí trae «faltas recibidas» (`Fouls suffered`); se guarda en la posición 14 de cada aparición. Betano no ofrece mercado de faltas recibidas en estos dos partidos.

## Límites que se declaran
- Una sola lectura de cuotas: no hay CLV ni movimiento. Releer cuotas y onces ≈ 1 h antes de cada partido.
- BB Boost leído 13:54 Bogotá en 7 de 10 partidos; las combinadas de equipo del informe (producto de cuotas) siguen siendo un techo, no un precio de Betano; el precio real está en `bb/`.
- «Entradas» de Flashscore son ganadas/intentadas; Betano cuenta entradas totales. Flashscore solo trae amarillas y rojas para tarjetas (Betano cuenta en puntos).
- Lo recogido pasa transcrito por el chat y se verificó con hash: `fs_20nov.json` 527643060, `fs_paginas_20nov.json` 2535844691, `arb_20nov.json` 3040378702, `pj_20nov.json` 804547518, `lu_20nov.json` 1245359337.
- Criterios de tipsters y medios sin resultados verificados; el «cumple 7 de 10» acierta cerca de lo que ya descuenta el precio (ver `CLAUDE.md`, «Hallazgos 4–18 nov»).

## Bloque 12:30–16:00 (10 partidos; recolección 11:27–13:00 Bogotá)
| Qué | Dónde | Estado |
|---|---|---|
| Betano (lectura 11:27–11:28; hash `bet_20nov_pm` 760018290) | `betano/`, `raw/bet_*.txt` | 10 de 10 |
| Flashscore últimos 10 de cada equipo + directos (`fs_20nov_pm_b` 47020405) | `flashscore/` | 10 de 10 |
| Árbitro (ValueStats; `arb_20nov_pm` 2107428813) | `arbitros/` | 9 de 10; **Al-Ahli–Al-Nassr no estaba anunciado** |
| Tabla, forma y bajas (`fs_paginas_20nov_pm` 3123788724; `lu_st_20nov_pm` 1801034947) | `paginas/`, `notas/` | 10 de 10; solo hechos de tabla, forma y bajas (sin lectura de rotación ni objetivos) |
| Alineaciones | `alineaciones/` | Oficiales en Al-Ahli–Al-Nassr y Aarhus–Lyngby; probables en 8; **Cobresal–Audax sin pestaña** |
| **Historial por jugador (7 partidos con tiros al arco)** | `jugadores/<partido>.json` | Al-Ahli 10+10 de 10; Aarhus 10 y 9 (falta vs VSK Aarhus 9-sep); Farul 10 y 9 (falta Cluj vs CFR 28-oct); Bayern 10+10; Troyes 10+10; Cercle 9 y 6 (faltan Hasselt 16-oct; Beveren, Patro Eisden, Mechelen y Waregem del visitante); **Athletic 3 y 4 de 10 (13 partidos sin leer: cobertura insuficiente, sus mercados de jugador no se recomiendan)**. Hash del lote final (`pjb_20nov_3`): 2135175239 |
| Andorra–Leganés, Verona–Cesena, Cobresal–Audax | — | Solo goleador (`anota`): no necesitan historial de estadística |
| BB Boost (catálogo `bb/catalogo_1400.json` hash 152596482; precios `bb/precios_1400.json`) | `bb/` | **Leído 13:54 Bogotá** en 7 partidos (Al-Ahli, Aarhus y Farul ya empezados). Resumen `bb/bb_boost_resumen.json`, texto `bb/BB_BOOST_1354.md` |
Límites: una sola lectura de cuotas (sin CLV); releer cuotas y onces ≈ 1 h antes; «entradas» de Flashscore no son idénticas a las de Betano; criterios de tipsters sin resultados verificados. Hash del lote de historiales Al-Ahli/Aarhus (`pjb_20nov_1`): 1924190433.


## Bloque 16:00–22:10 (9 partidos; recolección 14:51–15:50 Bogotá)
| Qué | Dónde | Estado |
|---|---|---|
| Betano (lectura 14:51; hash `bet_20nov_tarde` 3620562271) | `betano/`, `raw/bet_*.txt` | 9 de 9. **Límite de la fuente:** la API de Betano entrega 215 de los 625–685 mercados anunciados de Vélez, Tijuana y Juárez; los mercados de remates, asistencias y atajadas de jugador solo traen el jugador destacado |
| Flashscore últimos 10 de cada equipo + directos (`fs_20nov_tarde` 3682558057) | `flashscore/` | 9 de 9 (10+10 con estadísticas completas; directos: Tijuana–Atlante 0 (no se han enfrentado en el periodo), Vélez–Belgrano 3, resto 6) |
| Árbitro (ValueStats; hash `vs_20nov_tarde` 3525050358) | `arbitros/` | 6 de 9. **Sin anunciar a las 15:40:** Tijuana–Atlante, Juárez–Atlas, Puebla–San Luis (ni Flashscore ni ValueStats ni prensa lo tenían); releer antes del partido |
| Tabla y qué se juegan (hash `lust_20nov_tarde` 1736476756) | `paginas/`, `notas/` | 8 de 9. **Vélez–Belgrano: Flashscore no tiene pestaña de posiciones** |
| Alineaciones | `alineaciones/` | Oficiales: Cobresal–Audax (leídas ~15:50). Probables: Vélez, Tijuana, Juárez, Puebla. **Sin publicar a las 15:45: Palestino, Medellín, Bucaramanga, Cali** (se releen ~1 h antes) |
| **Historial por jugador (Vélez–Belgrano, Tijuana–Atlante, Juárez–Atlas)** | `jugadores/` | **NO disponible en Flashscore:** su pestaña «Player stats» está vacía para Liga MX y Liga Profesional argentina (13 partidos probados dieron «filas 0»: 8 de Vélez y 5 de Tijuana, más una comprobación manual del Necaxa–Tijuana del 7-nov con la pestaña vacía; los de Juárez no se probaron porque era la misma liga). Sofascore da 403. Los mercados de jugador de estadística de esos 3 partidos **no se recomiendan** |
| Cobresal, Palestino, Puebla, Medellín, Bucaramanga, Cali | — | Solo goleador (`anota`): no necesitan historial de estadística |
Límites: una sola lectura de cuotas (sin CLV); «entradas» de Flashscore no son idénticas a las de Betano; Flashscore no trae «faltas recibidas» en Liga MX/Argentina; criterios de tipsters sin resultados verificados.
