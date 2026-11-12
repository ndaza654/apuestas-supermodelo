# Cómo leer TODOS los mercados de un partido de Betano (navegador abierto) — SM-1.2

Probado el 11-nov-2026 en `https://www.betano.co` (co.betano.com devolvió 502 de Cloudflare; betano.com.co no se abrió). La página es una SPA:
`window.initial_state` solo trae ~20 mercados, pero la API que usa la propia página entrega todos (599 en Turquía–Bélgica).

1. Abre la página del partido (`/cuotas-de-partido/<equipos>/<id>/`) en el navegador integrado.
2. Desde esa página ejecuta (misma sesión, mismo origen):
   `fetch('/api/cuotas-de-partido/<equipos>/<id>/?bt=12&req=s,stnf,c,mb').then(r => r.json())` → `data.event.markets`
   (`bt=12` = pestaña «Todo»; 0–11 son las demás pestañas). Guárdalo en `window.__j` y filtra DENTRO de la página: el JSON pesa ~830 KB.
3. Cada mercado: `type`, `name`, `handicap`, `selections[{name, price, handicap}]`. Los mercados «de tabla» (goleador `PSCR`, tiros al arco por jugador `PLST`)
   vienen con `selections` vacío y los datos en `tableLayout.rows[].groupSelections[0].selections` (PSCR: columnas En cualquier momento / Primero / Último);
   además traen `lastGamesStats` (lo que hizo el jugador en sus últimos partidos) y `labels` (media).
4. Códigos útiles: `MRES` 1X2 · `DBLC` doble oportunidad · `DNOB` sin empate · `BTSC` ambos · `HCTG` goles totales · `OUHG/OUAG` goles por equipo ·
   `OUH1/OU1H/OU1A/OUH2` goles por tiempo · `CNOU` córners · `XOF2/YOF2` córners por equipo · `COU1/COU2` córners 1T/2T · `TCOU/HCOU/ACOU/1COU` tarjetas ·
   `4151/4152` ambos reciben 1+/2+ tarjetas · `X002/X133/X134` tiros al arco · `4159/4160/4161` remates · `4629/X135/X136` faltas · `X013/X131/X132` fueras ·
   `X328/4165/4166` saques de meta · `X128/4167/4168` saques de banda · `H1RS/H2RS` resultado por tiempo · `HTFT` descanso/final (9 opciones) ·
   `HOFR` «resultado medio tiempo o tiempo completo» · `NTYC` quién recibe más tarjetas · `TWMC` quién saca más córners · `AHRF/AHRH` hándicap asiático ·
   jugadores: `PALS` remates · `PLST` tiros al arco · `PLTA` entradas · `1000679` faltas cometidas · `1000678` faltas recibidas · `PALA` asistencias ·
   `1000115` atajadas · `PTRC` recibe tarjeta · `1000661` anota o asiste · `PSCR` anota · `PTS2` anota 2+ · `X006` anota en el 1.er tiempo ·
   parejas: `1001134` asiste · `1001133` anota · `1001135` primer gol · `1001136` tarjeta · `1001137` anota o asiste.
5. Convierte a la entrada del modelo (`betano.lineas / unicos / jugadores / parejas`). Ejemplo completo: `partidos/2026-11-12_turquia_belgica/construir.py`.

Ojo: las cuotas cambian; anota la hora de lectura (`cuotas_leidas`). Betano deja abiertas las líneas de jugadores lesionados o suspendidos.
