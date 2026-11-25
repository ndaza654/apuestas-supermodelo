# Stack de fuentes: Betano + Flashscore + ESPN + Opta (decisión del usuario, 25-nov-2026)

El usuario pidió usar las cuatro **en paralelo**, cada una en lo que es más fácil y sirve. Pruebas hechas hoy en su navegador integrado. **Sin clima** (decisión del usuario: no aporta; no se recolecta).

## Qué hace cada una
| Fuente | Úsala para | Cómo se lee | Velocidad | Límites |
|---|---|---|---|---|
| **Betano** | cuotas, mercados y precio real de los Bet Builder / BB Boost | API de Betano (`betano_extraer.js`, `mc-leg`) | rápida | solo cuotas |
| **Flashscore** | calendario y emparejar partidos, previas, alineaciones probables y bajas, tabla y qué se juega, últimos 10 de cada equipo con 35 estadísticas (xG, ocasiones, toques en el área, posesión…) total y 1T, incidentes, árbitro anunciado | feeds `df_*` con `fetch` (≈0,1 s) | muy rápida | historial por jugador: lento (iframes) y vacío en ligas menores; sin faltas recibidas por jugador |
| **ESPN** (`site.api.espn.com/apis/site/v2/sports/soccer/<liga>/…`) | **marcador oficial y estado**, estadísticas de equipo (28), once con formación, **por jugador: titular, posición, faltas cometidas y RECIBIDAS, remates, tiros al arco, atajadas, goles, asistencias, tarjetas**, historial de un equipo (`teams/<id>/schedule` por liga), cuotas propias | JSON con `fetch`, sin clave | rápida | sin minutos, entradas ni centros por jugador; sin xG; sin árbitro; se pide por slug de liga (probados: `bra.1`, `eng.1`, `arg.1`, `uefa.champions`, `conmebol.sudamericana`) |
| **Opta** (`optaplayerstats.statsperform.com`, «Betting Showcase»; la fuente que Betano usa para liquidar) | **verificar líneas de jugador** y traer lo que falta en las otras: por jugador G A RC YC Crn S SOnT BS P **C (centros)** **Tk (entradas totales)** O **FC (faltas cometidas)** **FW (faltas recibidas)** SAV, puntos Opta con minutos, detalle por evento; **árbitro y estadio del partido**; calendario JSON `/api/en_GB/soccer/livescores?offset=` (ids y enlaces); lista de partidos de una competición en `…/results` (cientos de enlaces `match/view/<id>`) | lectura del DOM de una página por partido | más lenta (una página por partido) | ver «Truco de la visibilidad»; cobertura amplia: Champions, Libertadores, Sudamericana, Liga Argentina, Brasileirão, MLS, Liga MX, Championship, Serie A/B, J1, AFC, Concacaf… |

## Lo comprobado en la final Atlético-MG–Boca (21-nov)
- **ESPN y Opta dan el mismo marcador (Boca 2–0) y las mismas cifras de equipo**: remates 9–16, tiros al arco 2–7, faltas 10–9, amarillas 3–1, córners 4–4, **centros 20–16**, **entradas 13–17**, pases 368–496/497. Opta es la base de ESPN: para equipo, ESPN basta (JSON, sin renderizar).
- Eso **confirma que «C» de Opta = centros y «Tk» = entradas totales** (la columna «C» estaba sin confirmar en `opta_decod.py`).
- Opta añade a nivel jugador lo que ESPN no trae (minutos, entradas, centros) y ESPN añade la titularidad y la posición.
- Árbitro de esa final según Opta: Andrés Matonte.

## Truco de la visibilidad (importante para la recolección con Opta)
Los widgets de Opta no cargan si la pestaña «está oculta» (`document.visibilityState = hidden`, aunque el panel se vea): se quedan en «Loading». Se arregla en la página con
`Object.defineProperty(document,'visibilityState',{get:()=>'visible'}); Object.defineProperty(document,'hidden',{get:()=>false}); document.dispatchEvent(new Event('visibilitychange'))` y esperar a que `.Opta_F_MS_container` traiga «Referee». Luego, tablas en `.Opta_F_MP_container` (todas las filas salen **duplicadas** en el DOM: dividir sumas entre 2).

## Reparto propuesto (el usuario aprueba)
1. **Cuotas y combinadas con precio real:** Betano.
2. **Previas, alineaciones probables, bajas, tabla, qué se juega:** Flashscore.
3. **Últimos 10 de cada equipo (con xG, ocasiones, toques en el área, posesión):** Flashscore; ESPN como contraste y como respaldo cuando Flashscore no trae estadísticas.
4. **Historial por jugador:** Flashscore (completo en ligas grandes) → ESPN para **faltas recibidas, titularidad y posición** (rápido) → Opta para entradas, centros y minutos cuando haga falta o una liga menor no tenga tabla.
5. **Resultado oficial y calificación:** ESPN (rápido) contrastado con Flashscore; las líneas de **jugador** se califican con Opta (la fuente de Betano). Si ESPN/Flashscore/Opta difieren, se declara antes de calificar.
6. **Árbitro:** Flashscore (nombre) + ValueStats (historial); Opta confirma nombre y estadio del partido. Idea: sacar faltas y tarjetas por partido de cada árbitro cruzando el árbitro de cada partido pasado (Flashscore `df_sui`) con las estadísticas de ese partido.
Pendiente de implementar (nada de esto está en el código todavía): lector de ESPN, lector de Opta con el truco, y la regla de reparto en `correr_jornada.py`.

## Sofascore (probado 25-nov 14:20; el usuario pidió probarlo) — **funciona y es la más rápida y completa**
- **Cómo:** pestaña en `www.sofascore.com` y `fetch('/api/v1/...')` (ruta del mismo sitio). `api.sofascore.com` sigue dando 403 / «Failed to fetch»; el 403 de antes era por esa ruta. El navegador pide aprobación en cada uso.
- **Rutas probadas (todas 200, ≈0,1 s por llamada):** `unique-tournament/<id>/scheduled-events/<AAAA-MM-DD>` (Sudamericana = 480) · `event/<id>` (árbitro con tarjetas y partidos de carrera, estadio) · `event/<id>/statistics` · `event/<id>/lineups` · `team/<id>/events/last/0` · `player/<id>/events/last/0` · `event/<id>/player/<pid>/statistics` · `referee/<id>` · `referee/<id>/statistics` · `referee/<id>/events/last/0`.
- **Qué trae:** estadísticas de equipo (≈55: posesión, xG, xGOT, ocasiones claras, remates dentro/fuera del área, toques en el área, centros intentados/acertados, entradas, faltas, tiros libres, fueras de juego, saques de banda y de meta, intercepciones, despejes, recuperaciones, duelos, goles evitados); por jugador ≈70 (minutos, rating, faltas cometidas y **recibidas**, entradas totales/ganadas, centros, remates, a puerta, xA, pases, duelos, atajadas); últimos 30 partidos de un equipo o de un jugador; **ficha del árbitro** (partidos, amarillas, rojas) y sus últimos partidos.
- **Cotejo con la final Atlético-MG–Boca:** marcador 0–2, remates 9–16, a puerta 2–7, faltas 10–9, amarillas 3–1, córners 4–4, entradas 13–17, centros 6/20–5/16, pases 368–496: **idéntico a ESPN y Opta**. Árbitro: Andrés Matonte (292 partidos, ≈5,5 amarillas por partido en su carrera).
- **Límites:** API no oficial (puede cambiar o bloquear: pausas y parar ante 403/429); aprobación por uso en el navegador; cuotas de Sofascore no sirven (Betano manda).
- **Qué cambia en el reparto:** Sofascore pasa a ser la **primera opción** para estadísticas de equipo y de jugador por partido (rápida y con minutos, faltas recibidas y xG), con Flashscore para previas, alineaciones probables, bajas y tabla; ESPN y Opta quedan para contrastar marcador y para líneas de jugador (Opta = fuente de liquidación de Betano). Árbitros: ValueStats (decisión del usuario); Sofascore da un respaldo (carrera y últimos partidos).
