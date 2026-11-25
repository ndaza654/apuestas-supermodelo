# Recolección (desde el navegador del computador del usuario)

> **Actualizado el 23-nov-2026.** Al final hay una sección «Procedimiento probado 22–23-nov» con lo que funciona hoy y los fallos conocidos. Sofascore (sección más abajo) ya no se usa: da 403; la fuente es Flashscore. Si algo de arriba contradice esa sección, manda la sección final.

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

## Árbitro y goleador (regla desde el 19-nov-2026)
- **Árbitro, SIEMPRE y en todos los partidos:** Flashscore `df_sui_1_<mid>` (árbitro anunciado; ya sale en `flashscore/<clave>.json`) + ValueStats (`/en/referees?name=<apellido>` → `/en/referee/<id-slug>`; hace falta `request_access` a valuestats.com una vez).
  De la página se guardan: partidos registrados, amarillas y rojas por partido (historial total), y del texto «Frequently asked questions» la muestra de los últimos 20: amarillas/rojas por partido, penales, % de superar 3,5/4,5/5,5 tarjetas. Va a `arbitros/<clave>.json`; `armar_entrada.arbitro_de` lo pasa a `ficha.arbitro` y `contexto_mercado.texto_arbitro` lo muestra en el Resumen y en los factores de tarjetas.
  Límites: faltas por partido y penales por partido (tabla) requieren cuenta de ValueStats; árbitras de torneos femeninos pueden tener muestra corta (3–5 partidos). Si no se anuncia, se dice.
- **Goleador/goleadora (cuando el usuario lo pide; siempre en Champions femenina):** incidentes de Flashscore `df_su_1_<mid>` de los últimos 10 partidos de cada equipo (se pide con `fetch` a `global.flashscore.ninja/2/x/feed/df_su_1_<mid>` con la cabecera `x-fsign` de la página; ~0,1 s por partido, no depende del panel visible).
  OJO al parsear: un gol con asistencia viene en el mismo bloque `~` con dos `IK` (Goal y Assistance); hay que leer los campos EN ORDEN (un diccionario pierde al goleador). Se guarda `flashscore/goles_crudo.json` y `python3 recoleccion/goleadores.py jornadas/AAAA-MM-DD` escribe `goleadores/<clave>.md|json`: por equipo, quién marcó (con penales y asistencias), en cuántos de los 10 partidos, y el cruce con las líneas «anota» y «anota o asiste» de Betano.
  Límite: no trae minutos ni titularidad (sin goles por 90; «sin gol» no prueba que jugó). La tabla de jugadores de Flashscore (`flashscore_jugadores_iframe.js`) solo existe para algunos partidos femeninos.
- **URL de partidos pasados en Flashscore:** `/partido/futbol/<slug-1>-<id>/<slug-2>-<id>/?mid=<mid>` con los dos equipos en ORDEN ALFABÉTICO de slug (no local/visitante). Con otro orden el iframe no carga la tabla de jugadores (falló la mitad de los partidos el 19-nov).
- **Panel del navegador:** con el panel oculto o la pestaña en segundo plano, los iframes de Flashscore van ~1 min por partido (o se congelan); visible, ~15 s. Guardar el avance en `localStorage` (`pj19_<mid>`) por si la pestaña se cae.

## Procedimiento probado 22–23-nov-2026 (12 partidos en 1 h 15 min; 30+ partidos en 2 días)
**Lista y mercados.** `mercados_dia.js` lee de Betano qué mercados ofrece cada partido (conteo por tipo: goleador, estadística de jugador, tarjeta) para decidir qué partidos necesitan historial completo y cuáles solo goleador. Betano (`betano_extraer.js`) y Flashscore (`flashscore_extraer.js`) se cargan en la pestaña con `fetch('https://raw.githubusercontent.com/ndaza654/apuestas-supermodelo/main/recoleccion/<archivo>')` + `(0,eval)`.
**Resultados y goles (rápido, sin iframes).** Los feeds `https://global.flashscore.ninja/2/x/feed/df_st_1_<mid>` (estadísticas), `df_su_1_<mid>` (incidentes/goles) y `df_sui_1_<mid>` (árbitro) con la cabecera `x-fsign: SW9D1eZo` responden en ~0,1 s y no dependen de que el panel esté visible. Todo lo que se pueda sacar de feeds se saca de feeds.
**Tabla de jugadores (lo lento).** Solo existe en la página renderizada: `flashscore_jugadores_en_par.js` + `flashscore_jugadores_en_lotes.js` (iframe por partido pasado; selector `tr[data-testid="wcl-tableBodyRow"]`).
- Fijar `window.__esperaTabla = 60000` (con 20 s salían «filas 0»); máximo 3 trabajadores en paralelo; pestaña nueva (se degrada tras ~80–100 cargas); reencolar trabajadores atascados.
- Orden de slugs en la URL de partidos pasados: alfabético.
- Fila de jugador: `[mid, fecha, min, remates, al_arco, goles, asist, amarillas, rojas, faltas, entradas_ganadas, atajadas, entradas_tot]`.
- Ligas menores a veces no publican tabla (el 22-nov faltaron 8 de 23): se declara, no se inventa.
**Sacar datos del navegador sin pasarlos por el chat:** Blob → `a.download` → `~/mnt/Downloads/<uuid>.tmp` → `device_bash cp` a un nombre → `device_stage_files` → `python3 recoleccion/verificar_hash.py <archivo> <hash>` (h=(h*31+code)>>>0 sobre unidades UTF-16) → copiar al repo. `javascript_tool` corta a ~45 s: esperar con `sleep` en Bash y volver a leer `localStorage`.
**Alineaciones:** la pestaña de alineaciones de Flashscore no publica el once hasta ~1 h antes; hasta entonces solo «probables». Releer ~1 h antes (también cuotas) y actualizar `raw/lu_<clave>.txt`.
**Tabla de posiciones (AFC y copas):** `paginas_a_notas.py`; si el texto trae líneas tipo «2-2» que no son tabla, quitarlas antes (`--forzar`).
**Goleador:** `goleadores.py` (de los incidentes `df_su`); `p mezcla` = (partidos con gol + 10·p_cuota/1,08)/20 es una heurística propia SIN validar.
**Balance:** Betano → `https://www.betano.co/mybets/` (clic en «Resueltas»; «Abiertas (n)»; no muestra fechas; el boost aparece como «Ganancias $X» + «Bet Builder Boost +25 % +$Y»). La ruta `/myaccount/my-bets/settled` da 404. Resultados: feeds `df_st`/`df_su`; jugadores: `flashscore_jugadores_en_par.js`.
**Cada combo enviado por el chat** se registra en `jornadas/AAAA-MM-DD/bb/bb_boost_resumen.json` (o `combinadas_enviadas_HHMM.json`) en el momento de enviarlo.

## Prueba del 23-nov (recolección del 24-nov): lo que se midió del método nuevo
- **Calendario con ids (rápido):** Flashscore `f_1_1_-5_en_1` (feed del día; cabecera `x-fsign`) devuelve todos los partidos con su `mid` (`AA`), local (`AE`), visitante (`AF`) y hora (`AD`); la cabecera de cada liga es `ZA` (p. ej. `EUROPE: Champions League - League phase`, `ASIA: AFC Champions League - League phase`). Sustituye buscar los `mid` uno a uno.
- **Betano de 17 partidos:** segundos (`mercados_dia.js` + `betano_extraer.js`). **Historial de equipos de 17 partidos (feeds `df_hh`, `df_st`, `df_su`, `df_sui`):** ≈2 min. **Goles/goleadores de 306 partidos (`df_su`):** ≈8 s, un solo JSON.
- **Tabla de jugadores:** no hay feed directo (se probaron `df_lps`, `df_pl`, `df_pst`, `df_stp`; `df_ps_1_` vuelve vacío y `df_li_1_` solo sirve con el once publicado). Sigue siendo el iframe. **Caché:** `python3 recoleccion/cache_jugadores.py cola jornadas/AAAA-MM-DD` indexa lo ya leído en `jornadas/*/jugadores/*.json` y deja en `flashscore/jugadores_cola.json` solo los partidos que faltan; `fusionar` completa `jugadores/<partido>.json` con las filas en caché. El 24-nov ya había 52 de 180 partidos-equipo (Aston Villa 8/10, Dortmund 9, Como 9…).
- **El iframe se atrasa si la pestaña no está al frente:** con 5 trabajadores y la pestaña en segundo plano muchas tablas salían «sin tabla (filas 32)» (la tabla sí cargó, pero después del tiempo de espera). Poner la pestaña al frente (`tabs_select`), 3 trabajadores y `__esperaTabla = 45000`, y vaciar `pjFail` antes de reintentar.
- **Previa y bajas de Flashscore (contexto):** `https://www.flashscore.com/match/football/<mid>/#/match-summary` en la pestaña (navegar, esperar a «MATCH INFORMATION», guardar `main.innerText` en `localStorage` y bajar un solo JSON con hash) → `paginas/<clave>.txt` → `paginas_a_notas.py` (si la tabla no cargó en esa página, la toma de otra página de la misma competición) → `notas_previa.py` (bajas y dudas como hechos; `previa_resumen.json` con el resumen PROPIO de Claude, nunca copiado). Los partidos de la AFC no traen previa, solo tabla y forma. Con un `iframe` esta página llega vacía (solo el esqueleto): hay que navegar la pestaña.

## Balance del 23-nov (procedimiento probado el 24-nov)
- **Betano «Mis apuestas»:** con el navegador integrado, `navigate` a `https://www.betano.co/mybets/`, esperar unos segundos (el `get_page_text` inicial sale vacío), clic en «Resueltas» (coordenadas del botón; la lista sale con «Resueltas (n)») y `get_page_text`. Las tarjetas salen de la más nueva a la más vieja: los últimos boletos de la lista son los de días anteriores; la numeración 151… se asigna por orden.
- **Resultados por feed sin que se cuelgue el `javascript_tool` (corta a 45 s, y con el panel oculto va lento):** `tabs_select` para poner la pestaña de Flashscore al frente, lanzar el `fetch` de todos los `df_st_1_`/`df_su_1_` **sin esperar** (guardando en `window.__res23` y poniendo `window.__fin = true` al final) y leer después. 12 partidos tardaron ≈ 5 s. Bajar con `Blob` + `a.download` (un solo JSON), mover el archivo a `Documents\Claude-Apuestas\recoleccion` (ver CLAUDE.md «Archivos de trabajo»), `device_stage_files`, `verificar_hash.py`.
- **Calificar:** `resultados_flashscore.py` → `resultados_por_clave.json`; el mapa clave → partido de `lineas.csv` (`mapa_partidos.json`) se arma con los nombres de la columna `partido`; luego `calificar_lineas.py`, `calificar_bb.py`, `calificar_combinadas_enviadas.py`, `marcar_apostadas.py`, `calificar_anota_incidentes.py` (un partido a la vez con los goleadores de los incidentes), `sugerencias.py`, `aprender_combos.py`, `libro_dia.py`, `balance_html.py --titulo "<fecha>"` (sin `--titulo` sale «12 y 13 de noviembre») y `analisis_historial_boletos.py`.
- **Nota sobre el ranking:** en `ranking.md` «situación sin leer» significa «sin factores que sumen o resten» (todo por defecto: importancia normal, nadie necesita ganar): puede aparecer aunque la tabla sí se leyó (p. ej. Shabab Al Ahli–Al-Qadsiah el 24-nov). Es una etiqueta, no un dato que falte.


## Lecciones del 24-nov (recolección del 25-nov): panel oculto, scripts de nivel superior y lotes
- **Con el panel oculto los iframes de Flashscore salen vacíos o se congelan** (`document.visibilityState = "hidden"`, temporizadores frenados, capturas grises). Lo que sí funciona es **navegar la pestaña** a la página del partido y leer el DOM en esa misma pestaña. Scripts: `flashscore_jugadores_toplevel.js` (`pjTop()` lee las subpestañas general/shots/attack/defense/goalkeeping y guarda `pjE_<mid>` en localStorage; `pjTodo(nombre)` descarga todo con hash) y `flashscore_partido_toplevel.js` (`leerPartido()`: resumen, alineaciones, formaciones y tabla → `recp_<mid>`).
- **`browser_batch`:** una llamada con `[navigate, javascript_tool]` repetidos recorre varios partidos; dentro del lote la herramienta se llama `javascript_tool` (entrada `{tabId, action:"javascript_exec", text}`). El tiempo por llamada es ~50 s: **2 partidos por pestaña y 4 pestañas en paralelo** (~8 partidos por ronda, ~25 s por partido). Si una llamada se corta, el script de la página **sigue y termina**: se mira localStorage antes de reintentar.
- **Cargar los scripts una vez:** guardar el código en `localStorage` (`pjsrc`, `ptsrc`) con `fetch` de raw.githubusercontent.com y luego `(0,eval)(localStorage.pjsrc)`; el localStorage se comparte entre pestañas del mismo origen (www.flashscore.com), así que **todo lo recogido por cualquier pestaña se descarga desde una sola**.
- **No navegar una pestaña con datos sin guardar** (se perdieron lecturas de contexto de la ACL): primero guardar en localStorage o descargar.
- **Descargas:** el Blob aparece como `<uuid>.tmp` unos segundos y a veces no se renombra: si el tamaño ya coincide, copiar el `.tmp` y **verificar el hash** (`verificar_hash.py`) antes de usarlo.
- **Esperas de ≤ 20 s por `await` dentro de un `javascript_tool`** (corta a 45 s); no usar `return` suelto, usar expresión.
- **Ligas sin «Player stats»:** Azerbaiyán, Ucrania, Noruega inferior, 2.ª de Portugal/Chequia/Bélgica copa, amistosos: `pjTop()` responde «sin pestaña de jugadores»; se declara en `jugadores/LEEME.md`, no se inventa.
- **Adaptador:** `ctx_top_a_repo.py` convierte `recp_*` en `paginas/`, `alineaciones/`, `notas/` (las bajas se asignan por nombre contra `jugadores/<clave>.json`; las que no calzan quedan en `bajas_sin_lado`). `jugadores_en_decod.py` pide además un `spec` {mid: [[clave:L|V, L|V, fecha, rival]]} que se arma de `flashscore/<clave>.json → forma`.
- **ValueStats (árbitros):** buscar con tilde y sin país; se parcheó `arbitros_valuestats.js` (CP, acentos, sin país) y `arbitros_vs_decod.py` (`D.get(c) or D.get(c[:12])`).
- **Avance guardado:** `flashscore/jugadores_progreso.json` (hechos / sin tabla) para retomar sin repetir.

## Lecciones del 25-nov (segunda tanda, modelo Opus 5.5): controles que encontraron errores
- **Mercados por liga:** `python3 recoleccion/mercados_por_liga.py` → `registro/mercados_betano_por_liga.{json,md}` (44 ligas). Leer ANTES de recolectar para saber qué traer: si la liga trae estadística de jugador en la mayoría de partidos, historial por jugador; si pocas veces (Liga MX 50 %), releer Betano el día del partido. J1 y ACL: 0 % tarjetas.
- **Control remates jugador = remates equipo** (por partido y lado) después de `cache_jugadores.py fusionar`: detectó 3 partidos de caché incompletos (Corinthians). La caché no es infalible: comprobar siempre.
- **ValueStats:** el filtro por inicial nunca se aplicaba (estaba dentro de un comentario `//`). Comprobar siempre que la inicial de Flashscore coincida con `vs_nombre`.
- **`ctx_top_a_repo.py --hora`:** la hora se perdía. Corregido.
- **No pisar archivos de la tanda anterior:** `cache_jugadores.py cola` reescribe `jugadores_cola.json` y `jugadores_en_decod.py` reescribe `jugadores/crudo_flashscore_en.json`: renombrarlos antes (`*_champions.json`).
- **Playoffs sin tabla:** en Flashscore la pestaña «Standings» de un playoff es el cuadro; la fase sale en el rótulo del resumen («QUARTER-FINALS», «First leg»): anotarla a mano en `notas/<clave>.json → se_juega`.
- **Ritmo medido:** 86 partidos de jugadores en 11 rondas de 4 pestañas × 2 partidos (≈ 25 min), 0 fallos.

## Lecciones 25-nov (historial por jugador, 492 partidos)
- El iframe (`pjPar`) da falsos «sin tabla de jugadores (filas 0)» en lecturas largas (comprobado a mano: Zagreb–Anderlecht, Riga, Sunderland–Zagreb sí tienen tabla). Solo fiarse de él en las primeras ~40 lecturas con la página recién cargada, ≤ 4 trabajadores; la pestaña se cae a los ~10 min («page load failed»): navegar de nuevo y relanzar (lo leído sigue en localStorage).
- Lectura fiable: pestaña de nivel superior, `navigate` a `/match/football/<mid>/?mid=<mid>` + `(0,eval)(localStorage.pjsrc); await window.pjTop()` (guarda `pjE_<mid>`; ~7 s por partido; hasta 3 pestañas en paralelo, 3 partidos por llamada). La URL con otro slug da 404.
- No usar `__descargarLote` (borra todos los `pjE_`); bajar con Blob propio + hash.
- Orden de la cola: priorizar por hora del partido deja primero ligas sin tabla (Kazajistán, Bosnia, Copa de Suiza): mejor leer primero equipos de ligas grandes. El orden de `forma[..].stats` es [equipo, rival], no [local, visitante].
- Ligas probadas sin «Player stats»: Kazajistán, Bosnia, Copa de Suiza.
