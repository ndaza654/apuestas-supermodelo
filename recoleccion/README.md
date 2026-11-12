# Recolección (desde el navegador del computador del usuario)

El shell de la nube no llega a Betano ni a Sofascore; se recolecta con el **navegador integrado** (pestaña ya con sesión) y se guarda JSON en `jornadas/AAAA-MM-DD/`.
Después `ficha.py` y el modelo trabajan sin red.

## Betano  (extractor verificado en vivo el 12-nov-2026)
Dos piezas: `betano_extraer.js` (corre en la pestaña de betano.co y devuelve un texto compacto) y `betano.py` (texto → JSON del modelo).
1. Abrir `https://www.betano.co/sport/futbol/proximos-partidos-hoy/` (hay que desplazarse para que carguen todos) y cargar `betano_extraer.js`
   en la pestaña (el navegador integrado ejecuta el archivo con `javascript_tool`).
2. `listarPartidos()` → `[{slug,id}]` de los partidos de la página. Para cada uno: `await extraerBetano(slug, id)` → texto compacto.
   Usa `fetch('/api/cuotas-de-partido/<slug>/<id>/?bt=12&req=s,stnf,c,mb')` (solo lectura, ~580 mercados por partido).
3. Guardar el texto en `jornadas/AAAA-MM-DD/raw/bet_<slug>.txt` y convertir: `python3 recoleccion/betano.py jornadas/AAAA-MM-DD/raw`
   → `jornadas/AAAA-MM-DD/betano/<slug>.json` (bloque `betano` de la entrada). Pruebas: `python3 pruebas/test_betano.py`.
Qué extrae: líneas Más/Menos de goles, córners, tarjetas, tiros al arco, remates, faltas, fueras, saques de meta y de banda (total, local, visitante, 1T, 2T;
y asiáticos de goles); 1X2, doble oportunidad, ambos marcan, descanso/final, hándicaps; jugadores (anota, anota o asiste, tarjeta, asistencias, remates, tiros al arco,
entradas, faltas, atajadas) y las parejas «cualquiera de los jugadores…». Se descartan las líneas con un lado < 1.03 (sin información).
Primero se lee qué ofrece Betano en ese partido; solo se analiza lo que existe (partidos con pocos mercados salen con pocas líneas, sin inventar).
Códigos de mercado de la API (por si Betano cambia nombres): córners `CNOU`, por equipo `XOF2/YOF2`, tiros al arco `X002/X133/X134`, remates `4159–4161`, faltas `4629/X135/X136`,
fueras `X013/X131/X132`, saques de meta `X328/4165/4166`, de banda `X128/4167/4168`, jugadores `PALS/PLST/PLTA/1000679/PALA/1000115/PTRC/1000661/PSCR`, parejas `1001133–1001137`.

## Flashscore  (verificado cargando en el navegador integrado, 12-nov-2026)
Fuente preferida por el usuario para el contexto: «está todo». La página previa de un partido (`flashscore.co/partido/futbol/<local>/<visitante>/?mid=<id>`) trae
árbitro, estadio, forma, enfrentamientos directos (H2H), clasificación, cuotas 1X2/Más-Menos/ambos/hándicap y una previa escrita; la pestaña de estadísticas
(`.../resumen/estadisticas/?mid=<id>`) trae las estadísticas de partidos terminados. La lista del día son los enlaces `a[href*="/partido/"]` de la portada.
Pendiente: el recolector de «últimos 7 de cada equipo» y directos con estadísticas (córners, remates, faltas, fueras, saques) → `ficha.forma` / `ficha.h2h`.
No hay estadísticas de árbitro en Flashscore: se completan con la fuente que indique el usuario (B-Soccer; falta la dirección exacta).

## Sofascore  (⚠ NO verificado hoy)
Endpoints usados en la sesión del 12-nov desde una pestaña de sofascore.com: `event/<id>`, `event/<id>/lineups` (probables),
`event/<id>/h2h/events`, `team/<id>/events/last/0`, `event/<id>/statistics`, `event/<id>/pregame-form`, `referee/<id>/statistics`,
`unique-tournament/<id>/season/<id>/standings/total` (prefijo `https://api.sofascore.com/api/v1/`).
**Estado al escribir esto:** `api.sofascore.com` respondió **403** (también navegando directo) y desde la pestaña de www.sofascore.com las rutas relativas dan 404.
Probable bloqueo por exceso de llamadas; reintentar más tarde, con pausas entre llamadas, y no insistir si sigue el 403
(no se evade el bloqueo). Alternativas: leer la página del partido con `get_page_text`, o pedir al usuario que abra la página.

## Clima
Open-Meteo (`api.open-meteo.com/v1/forecast?latitude=..&longitude=..&hourly=temperature_2m,precipitation,wind_speed_10m`) desde la pestaña de open-meteo.com.

## Qué debe quedar en cada entrada (`pub/entradas/<partido>.json`)
`betano` (líneas, jugadores, parejas), `jugadores` (alineación probable/confirmada con fuente y hora), `ficha.forma` (últimos 7 de cada equipo con `stats`:
`g, xg, c, sh, sot, f, off, ti, gk, y` como [a favor, en contra]), `ficha.h2h` (directos con `stats` orientadas al local/visitante actual; opcional),
`ficha.jugadores_hist`, `ficha.arbitro`, `ficha.clima`, `ficha.bajas`. Lo que falte se declara en la ficha; no se inventa.
