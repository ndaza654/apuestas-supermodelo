# Stack de fuentes: Betano + Flashscore + ESPN + Opta

Fecha y hora: 25-nov-2026, ≈14:30 Bogotá. Probado en el navegador integrado del usuario con la final Atlético-MG–Boca como caso. Límites: una sola liga/partido contrastado ESPN–Opta; velocidad de Opta no cronometrada; nada de esto está implementado en el pipeline todavía.

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
