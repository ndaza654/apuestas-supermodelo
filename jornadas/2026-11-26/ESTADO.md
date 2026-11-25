# Estado de la recolección · jornada 2026-11-26 (Europa League + Conference League, 36 partidos)

Recolectado el 25-nov-2026 (cuotas ~08:56–08:59 Bogotá; previas, alineaciones probables y tablas ~10:25; historial de jugadores 10:00–11:00). Kickoffs el 26-nov: Kairat 10:30; 12:45 (Besiktas, Plzen, Salzburg, Marseille, Zagreb, Celta, Olympiacos, Union SG y otros); 15:00 el resto. **Cuotas sin releer**: hay que releerlas ≈ 1 h antes de cada partido (copiar antes `betano/` a `betano_previo/`).

## Qué se leyó
| Dato | Cobertura |
|---|---|
| Mercados de Betano | 36 de 36. Todos traen partido, equipos, córners, tarjetas, goles, ambos marcan y resultado. **Mercados de jugador en los 36** (remates, tiros al arco, atajadas, asiste, anota o asiste, goleador). Quedaron en `registro/mercados_betano_por_liga.*` (Europa League y Conference League). |
| Historial de equipos (últimos 10 + directos) | 36 de 36. Directos casi inexistentes entre estos equipos; parejas de jugadores solo en 2 partidos. |
| Previa, tabla, forma, alineaciones probables | 36 de 36 (Flashscore, ~10:25). Bajas «sin lado»: no se asignan a un equipo si no calzan con el historial. |
| Árbitro nombrado | 36 de 36. **Con historial en ValueStats: 32.** Sin historial (no aparece en ValueStats): Jollenbeck M. (Brighton–Craiova), Fesnic H. (Iberia–Getafe), Menelaos A. (Brann–Aarhus), Sanchez J. (Union SG–Lech). Tarjetas y penales de esos 4 partidos salen sin dato de árbitro. |
| **Historial por jugador** | **Incompleto.** Ver abajo. |

## Historial por jugador (regla de recolección: no se da por completa)
- Cola: 492 partidos pasados distintos (últimos 10 de cada equipo). Se leyeron las tablas «Player stats» de **136**; con la caché de jornadas anteriores quedan 315 partidos-equipo con estadísticas por jugador (de 360 posibles, ver `jugadores/LEEME.md`).
- **Historial completo (≥ 7 de 10 en ambos equipos): 5 partidos** — Sparta–AZ, Ajax–Thun, Besiktas–Beer Sheva, Brighton–Craiova, Crystal Palace–Real Sociedad. Parcial: Jablonec–Lugano (5 y 4 de 10).
- **Los otros 30 partidos: mercados de jugador de estadística NO se recomiendan** (cobertura de 0 a 4 de 10 por equipo).
- Por qué: (1) muchas ligas no publican «Player stats» en Flashscore (las probadas a mano: Kazajistán, Bosnia y la Copa de Suiza; probablemente otras ligas menores): sin tabla real; (2) el método de iframes dio falsos «sin tabla» en lecturas largas (comprobado a mano con partidos de Zagreb–Anderlecht, Riga, Sunderland–Zagreb, que sí tienen tabla) y leer el resto uno por uno no cabía antes de los partidos de las 12:45. Quedan pendientes unos 350 partidos; lista en `flashscore/jugadores_cola.json`.
- Control de sumas (remates y tiros al arco por jugador = totales del equipo en `forma[..].stats`): **309 de 315 partidos-equipo cuadran exacto**. 6 no cuadraban (KWOeJ6jf, Yyn2xsCs, 2Z4xMLR0, ImWz7i0f, 6qmGdP1U): se **quitaron** 110 filas de esos partidos.
- Límites de siempre: Flashscore no trae algunas columnas en ligas menores; «entradas» = ganadas/intentadas de Flashscore, no las totales de Betano; lo recogido pasa transcrito por el chat y se verifica con hash (todos los bloques OK).

## Otros límites
- Situación (`notas/`): solo hechos de la página de Flashscore (tabla, forma, zonas); sin lectura de rotaciones, derbis ni motivación fuera de eso. El ranking marca «situación sin leer» → todos «reserva».
- Tarjetas: Flashscore solo trae amarillas; Betano cuenta en puntos.
- Criterios de tipsters sin resultados verificados.

## Actualización 25-nov ~14:30 Bogotá: Sofascore como fuente principal (decisión del usuario 14:10)
- Leídos con Sofascore (`sofascore_extraer.js`, 3 trabajadores, ≈8 min) los **36 de 36 partidos**: últimos 10 oficiales de cada equipo (10/10 en todos), estadísticas por partido y 1T, historial por jugador de esos 10 partidos (≈31–40 jugadores con ≥ 5 apariciones por partido), once probable + ausentes, árbitro y estadio. Cobertura y diferencias: `sofascore/LEEME.md` y `sofascore/contraste.json`.
- **El historial por jugador ya no está incompleto**: los 30 partidos que antes no tenían historial ahora lo tienen (Sofascore), con faltas recibidas, centros, xA y rating que Flashscore no trae.
- Contraste con Flashscore en los mismos partidos: ≈ 97 % de las cifras iguales; 222 celdas difieren en más de 1 (sobre todo remates y tiros al arco en copas y ligas menores: Bosnia, Kazajistán, Albania, Armenia, Georgia). No se sabe cuál fuente acierta: se declara en las dudas de cada ficha. 8 partidos pasados sin estadísticas en Sofascore se rellenaron con las de Flashscore.
- Once: cuando Sofascore y Flashscore no coinciden, el jugador que figura en uno solo va con titular 0,5 (declarado); esperar el once oficial.
- Pipeline corrido de nuevo (`correr_jornada.py`); `registro/sugerencias.csv` no se tocó. Cuotas siguen siendo las de las 08:56–08:59 del 25-nov.
