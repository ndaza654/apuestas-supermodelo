# Prompt para continuar la recolección del 14-nov (copiar y pegar en una sesión nueva)

Continúa el proyecto de apuestas de fútbol en Betano.co. Repo: github.com/ndaza654/apuestas-supermodelo, rama `recoleccion/2026-11-14`.
Lee primero CLAUDE.md, recoleccion/README.md y jornadas/2026-11-14/lista/partidos.md.

## Reglas
- Español siempre; horas en Bogotá (UTC−5). Yo decido y apuesto; tú analizas y recolectas, nunca apuestas.
- No toques nada del GitHub fuera de este repo. Commits terminan con `Co-Authored-By: Claude <noreply@anthropic.com>` y el enlace de la sesión.
- Dato que falte: dilo en la ficha, no lo inventes.

## Encargo
Recolecta TODA la información posible de los 21 partidos del sábado 14-nov-2026 listados en jornadas/2026-11-14/lista/partidos.md y súbela al repo. No hay afán: prefiero completo y verificado.
Por partido: Betano (todos los mercados, jugadores y parejas) + contexto (últimos 7 de cada equipo con estadísticas, directos, alineaciones probables o confirmadas con fuente y hora, bajas, árbitro, estadio, clima, tabla, importancia, historial por jugador).

## Cómo
- Navegador integrado (mcp__remote-devices__Claude_Browser__*, cargar con ToolSearch). El shell de la nube no llega a Betano ni Sofascore.
- Betano es https://www.betano.co (no co.betano.com). Lista del 14: /sport/futbol/proximos-partidos-hoy/ → clic en «MAÑANA» → scroll → enlaces /cuotas-de-partido/<slug>/<id>/.
- Extraer: pegar recoleccion/betano_extraer.js en la pestaña y `await extraerBetano(slug,id)` → raw/bet_<slug>.txt → `python3 recoleccion/betano.py jornadas/2026-11-14/raw`. En vivo Betano da 302 en /api/cuotas-de-partido/: usar /api/live/<slug>/<id>/ o leer /live/....
- Sofascore: desde una pestaña de www.sofascore.com las rutas relativas /api/v1/event/<id>(/statistics,/lineups,/incidents,/h2h/events) y /team/<id>/events/last/0 funcionan. api.sofascore.com da 403 y scheduled-events da 404: no evadir bloqueos.
- Los textos pasan por tu contexto y los escribes con Bash (heredoc con comillas simples). Verifica CADA archivo con el hash: calcula la misma suma en el navegador y compárala con `python3 recoleccion/verificar_hash.py archivo <hash>`. Sin archivos parciales: si no coincide, bórralo y repite. De 1 a 3 partidos por llamada y commit seguido.
- Agentes del proyecto en .claude/agents/ (corners, partido, jugadores, goles-resultado, tarjetas, combinadas, calificacion); escriben su detalle en archivos.

## Herramientas
Usa todas las que la sesión tenga (navegador integrado, Chrome, Bash, Agent, WebSearch/WebFetch, Artifact, Projects, conectores, MCP). Si necesitas una que no está cargada, búscala con ToolSearch o SearchMcpRegistry. Si pide aprobación o falta acceso, pídemelo en el chat y espera; no esquives permisos ni bloqueos.

## Estado
Hecho: inventario de 21 partidos con ids de Betano (17 con id). Pendiente: (1) Betano completo de esos 17, (2) ids de Valladolid–Castellón, Real Sociedad B–Sporting, Almería–Andorra, Mallorca–Córdoba, Banfield–Boca, Querétaro–Monterrey, Jamaica–México, (3) contexto Sofascore/Flashscore de los 21, (4) correr `python3 recoleccion/correr_jornada.py jornadas/2026-11-14`, pruebas pruebas/test_*.py, actualizar ESTADO.md y registro/BITACORA.md y subir todo.
Cuando esté recolectado: análisis, siempre abriendo con «Enfoque de mercados».
