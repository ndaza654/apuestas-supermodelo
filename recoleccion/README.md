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

## Flashscore  (verificado en vivo el 12-nov-2026; fuente principal de contexto)
Dos piezas: `flashscore_extraer.js` (en la pestaña de flashscore.co) y `armar_entrada.py` (lo une con Betano). Usa el servidor de datos de la propia página
(`global.flashscore.ninja/2/x/feed/…` con la cabecera `x-fsign` que la web ya manda), solo lectura y con pausa de 120 ms entre llamadas (~10 s por partido).
- Lista del día (incluye mañana): `f_1_<día 0|1>_-5_en_1` → `mid`, hora, liga, local, visitante (nombres en inglés).
- Contexto de un partido: `df_hh_1_<mid>` (últimos de cada equipo + directos) → por cada partido terminado `df_st_1_<id>` (córners, remates, tiros al arco, faltas, fueras,
  saques de banda y de meta, amarillas/rojas, xG; total y por tiempo) y `df_sui_1_<mid>` (árbitro anunciado, estadio).
- Probado con Colombia (Pasto–Junior) y con la Liga de Naciones (Italia–Francia): 7 + 7 + 7 partidos con estadísticas (prueba del 12-nov, con la muestra anterior de 7); coincide con la fuente anterior (Sofascore) en córners,
  remates, faltas, fueras, saques y tarjetas de los mismos partidos. Algunos partidos viejos no traen saques de meta: la ficha muestra el n real.
- Emparejar con Betano: misma hora de inicio + nombres (Betano en español, Flashscore en inglés).
- No hay (todavía): historial por jugador (remates/tiros al arco por partido), alineaciones probables, estadísticas del árbitro (B-Soccer).
- Uso:  `const ctx = await extraerFlashscore(mid)` → guardar como `jornadas/<día>/flashscore/<clave>.json`.

## Historial por jugador (Flashscore) — OBLIGATORIO para los partidos con mercado de jugador de estadística
Regla (CLAUDE.md, desde el 14-nov-2026): si Betano ofrece en un partido remates, tiros al arco, entradas, faltas, atajadas o asistencias de jugador, la recolección de ese partido incluye el historial por jugador de los últimos 10 partidos de cada equipo y las alineaciones. Partidos sin mercado de jugador o con solo goleador/tarjeta no lo necesitan.
- Alineaciones: `flashscore_alineaciones.js` (navegando a la pestaña del partido) → `raw/lu_<clave>.txt` → `alineaciones_decod.py` → `alineaciones/<clave>.json`.
- Historial: `flashscore_jugadores_iframe.js` (carga cada partido pasado en un iframe de flashscore.co, espera a que la tabla tenga filas, recorre General/Remates/Defensa/Paradas; sirve de 1 a 3 pestañas en paralelo, un partido por pestaña a la vez) → `__exportar('<partido>:<L|V>')` → `raw/pj_<partido>__<L|V>[__sufijo].txt` con hash → `jugadores_decod.py` → `jugadores/<partido>.json` (que lee `armar_entrada.hist_de`: min, remates, al arco, goles, asistencias, tarjetas, faltas, entradas ganadas, atajadas, entradas totales).
- Se pregunta la tabla de jugadores al abrir cada partido; si Flashscore no la publica (p. ej. un amistoso menor) se declara la ausencia, no se rellena.
- Límites: sin «faltas recibidas»; «entradas» = entradas ganadas (la columna también trae el total); las atajadas salen de «Paradas del arquero».

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
`betano` (líneas, jugadores, parejas), `jugadores` (alineación probable/confirmada con fuente y hora), `ficha.forma` (últimos 10 de cada equipo con `stats`:
`g, xg, c, sh, sot, f, off, ti, gk, y` como [a favor, en contra]), `ficha.h2h` (hasta 6 directos con `stats` orientadas al local/visitante actual; opcional),
`ficha.jugadores_hist`, `ficha.arbitro`, `ficha.clima`, `ficha.bajas`. Lo que falte se declara en la ficha; no se inventa.

## Pila de recolección «todo el día» (probada el 16/17-nov-2026 con 13 partidos)
Orden y fuente de cada dato (todo se guarda en `jornadas/AAAA-MM-DD/` apenas se lee; el navegador pierde lo que no se baja):
1. **Lista de partidos**: API de calendario de Betano (`/api/sports/upcoming/calendar/FOOT/?timeZoneId=America/Bogota&day=<ms 00:00 Bogotá>&sort=Leagues`, todas las ligas, ~167 partidos).
2. **Betano**: `betano_extraer.js` (se carga con `fetch` de raw.githubusercontent.com + `(0,eval)`) → `raw/bet_<slug>.txt` → `betano.py` → `betano/<slug>.json`. Además el volcado completo de mercados (`betano_full/<slug>.json`, ~600 mercados/partido).
3. **Flashscore** (`flashscore_extraer.js`, 10 partidos por equipo con estadísticas de equipo + directos + árbitro) → `flashscore/<slug>.json`.
   `/partido/<mid>/` redirige a la URL completa (sirve para armar iframes). Tabla: iframe a `<url>clasificacion/?mid=<mid>#/clasificacion/tabla/general`. Previa y bajas: pestaña alineaciones (texto «PREVIA DE FLASHSCORE»). Probables: en formato «cancha» (`[class*="fp-formation_"]`), ver `alineaciones_pitch.py`.
4. **Jugadores**: Opta (optaplayerstats.statsperform.com, solo DOM renderizado) para los partidos de la Nations League → `opta_decod.py`; Flashscore (`flashscore_jugadores_iframe.js`) para el resto. Opta y Flashscore coinciden (318/320 cifras en 40 partidos).
5. **Árbitros**: ValueStats (`/en/referee/<id-slug>`, servidor renderizado, un `fetch` por árbitro; directorio `/en/referees?name=`). Sin cuenta: tarjetas por partido y totales por competición; faltas por partido requieren cuenta.
**Cómo sacar datos del navegador sin pasarlos por el chat:** crear un Blob con el JSON y hacer `a.download` → queda un `.tmp` en `~/Downloads` (Electron) → `device_stage_files` → copiar al repo. Pedir acceso a Descargas una vez.
**Ritmo:** con el panel del navegador oculto, los iframes de Flashscore van lentos (~1 min por partido); repartir la cola en 3 pestañas (módulo 3 por pestaña, cola en `localStorage`).
