# Apuestas · súper modelo

Flujo: **Betano + Sofascore (navegador) → entrada JSON → modelo SM-1.2 + fichas por mercado → agentes especialistas → informe → registro de resultados.**

- `CLAUDE.md` — reglas fijas que Claude Code lee solo al abrir el repositorio.
- `recoleccion/` — cómo traer los datos (`README.md`) y `ficha.py` (ficha de córners, estadísticas de partido y jugadores).
- `supermodelo/` — el modelo (ver `MODELO_README.md`, `GUIA_RAPIDA.md`). `pruebas/` — `test_modelo.py`, `test_ficha.py`.
- `.claude/agents/` — `corners`, `partido`, `jugadores`. `.claude/skills/` — `analizar-partido`, `registrar-resultados`.
- `criterios/` — decisiones de criterio. `registro/` — picks y calificación. `jornadas/AAAA-MM-DD/` — datos, fichas e informes del día.

Uso en Claude Code: abrir esta carpeta en la pestaña *Code* y pedir «analiza la jornada de hoy». Claude sigue `analizar-partido`.
Mercados de prueba: córners, estadísticas de partido, jugadores. Tarjetas, goles, primer tiempo y resultados se suman si la prueba funciona.
El usuario decide y apuesta; el sistema entrega probabilidad, cuota y regularidad.
