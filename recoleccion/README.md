# Recolección (desde el navegador del computador del usuario)

El shell de la nube no llega a Betano ni a Sofascore; se recolecta con el **navegador integrado** (pestaña ya con sesión) y se guarda JSON en `jornadas/AAAA-MM-DD/`.
Después `ficha.py` y el modelo trabajan sin red.

## Betano  (verificado en vivo 12-nov-2026)
1. Abrir `https://www.betano.co/sport/futbol/proximos-partidos-hoy/` y listar partidos:
   `[...document.querySelectorAll('a[href*="/cuotas-de-partido/"]')].map(a=>a.getAttribute('href'))`
   → `/cuotas-de-partido/<slug>/<id>/`
2. Todos los mercados de un partido, desde una pestaña de betano.co (devuelve 200 y JSON con `data`):
   ```js
   const r = await fetch(`/api/cuotas-de-partido/${slug}/${id}/?bt=12&req=s,stnf,c,mb`); const j = await r.json();
   ```
3. Guardar el JSON crudo en `raw/` y convertirlo con la lógica de `jornadas/2026-11-12/_scripts_legacy/parse_betano.py` (referencia).
   Códigos de mercado: córners `CNOU`, córners por equipo `XOF2/YOF2`, tiros al arco `X002/X133/X134`, remates `4159–4161`,
   faltas `4629/X135/X136`, fueras `X013/X131/X132`, saques de meta `X328/4165/4166`, saques de banda `X128/4167/4168`,
   jugadores `PALS/PLST/PLTA/1000679/1000678/PALA/1000115/PTRC/1000661/PSCR/PTS2/X006`, parejas `1001133–1001137`.
   Primero se lee qué mercados trae el partido; solo se analiza lo que Betano ofrece.

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
