# Fuentes de datos probadas

Fecha y hora: 25-nov-2026, ≈14:00 Bogotá. Probado en el navegador integrado del usuario, una carga por sitio. Límites: ESPN sin árbitros ni clima en los partidos probados; ligas probadas: 5.

# Fuentes de datos probadas (25-nov-2026, ≈14:00 Bogotá) — para aprobar

Prueba hecha **en el navegador integrado del usuario** (la misma vía de la recolección), una carga por sitio, solo lectura. Criterio de «fácil»: JSON o HTML que se lee con un `fetch`, sin cuenta, sin CAPTCHA, que un solo script pueda recorrer.

## Funcionan (verificadas hoy)
| Fuente | Qué da | Cobertura probada | Para qué sirve | Límite |
|---|---|---|---|---|
| **Flashscore feeds** (ya en uso) | estadísticas de equipo (las 25 nuevas incluidas, total y 1T), incidentes, árbitro anunciado, estadio, alineaciones, tabla, historial por jugador | todas las ligas de la jornada | base de la ficha | árbitro: solo el nombre; sin faltas recibidas por jugador |
| **ESPN API pública** `site.api.espn.com/apis/site/v2/sports/soccer/<liga>/scoreboard?dates=AAAAMMDD` y `/summary?event=<id>` | marcador oficial y estado (FT, penales), **28 estadísticas por equipo** (faltas, tarjetas, fueras de juego, córners, atajadas, posesión, remates, pases, **centros intentados/acertados**, pases largos, bloqueos, entradas, intercepciones, despejes), once con formación y 23 jugadores, cuotas, `venue.address.city` | `bra.1`, `eng.1`, `arg.1`, `uefa.champions`, `conmebol.sudamericana` | **segunda fuente para verificar resultados** (hoy corrigió un error mío con la final), contraste de estadísticas, alineaciones, ciudad del estadio | sin xG, sin ocasiones claras ni toques en el área; **sin árbitros ni clima** en los partidos probados; cuotas de ESPN no son las de Betano |
| **Open-Meteo** `api.open-meteo.com/v1/forecast` + `geocoding-api.open-meteo.com/v1/search` | temperatura, lluvia y viento por hora en una coordenada; búsqueda de ciudad | probado con Berlín y Barranquilla | **clima** (falta en la ficha): lluvia fuerte y viento para córners, saques, remates | busca ciudades, **no estadios** (probé «Mineirão Belo Horizonte» y no devolvió nada): la ciudad sale de ESPN `venue.address.city` |
| **ValueStats** (ya en uso) | árbitro: tarjetas por partido, penales, % de superar 3,5/4,5/5,5 (muestra de 20) | ligas grandes y medianas | árbitro para tarjetas y penales | faltas por partido y penales por partido (tabla) piden cuenta |

## No sirven hoy
| Fuente | Motivo (probado hoy) |
|---|---|
| Transfermarkt (árbitros) | «Human Verification» (CAPTCHA): no se evade |
| Understat (xG) | la página muestra «We will come back soon»; además solo cubre 6 ligas |
| Sportradar StatsHub (árbitros por torneo) | el navegador lo bloquea por restricciones de seguridad |
| FootyStats `referee-stats` | carga, pero la tabla de la Premier trae árbitros retirados (Mike Dean, Clattenburg) y la de «próximos partidos» sale vacía: desactualizada. Las páginas `/<país>/<liga>/card-stats` existen pero no las probé a fondo |
| Sofascore | 403 (desde el 23-nov) |
| FBref, WhoScored | por lo que dicen fuentes web, FBref perdió xG y pases progresivos en 2026 y WhoScored usa protección anti-bot fuerte; no probados en el navegador |
| FotMob | tiene xG en las páginas de partido pero su API cambió y exige encabezados propios; no probado |
| APIs de pago (Sportmonks, etc.) | existen con estadísticas de árbitro (penales, faltas, rojas) desde ≈ 99 €/mes; solo si el usuario quiere pagar |

## Qué sigue faltando (no apareció una fuente fácil)
- **Faltas por partido de cada árbitro** (solo ValueStats con cuenta o API de pago).
- **Cobradores de penales, tiros libres y córners**, y **altura de la línea defensiva**.
- **Faltas recibidas por jugador** (Flashscore no las trae).
- **xG por jugador**: la última columna de la tabla de Flashscore parece xG; por confirmar.

## Propuesta (el usuario aprueba cada una)
1. **Clima en la ficha** con ESPN (ciudad) + Open-Meteo, a la hora del partido: lluvia (mm) y viento (km/h); entra como factor de córners, saques y remates.
2. **ESPN como segunda fuente de resultados**: en cada balance, contrastar el marcador y las estadísticas de Flashscore con ESPN y declarar las diferencias antes de calificar (hoy hubiera evitado el error de la final).
3. **ESPN como respaldo de alineaciones y de estadísticas** cuando Flashscore no traiga tabla (ligas menores, como los 8 de 23 del 22-nov), solo en las ligas que ESPN cubre.
4. Pedir cuenta gratuita de ValueStats solo si el usuario quiere faltas por árbitro (no se crea sin su permiso).
