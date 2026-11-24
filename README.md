# Apuestas · súper modelo

Apuestas de fútbol en Betano.co (COP; 1 u = 3.700 COP). **El usuario decide y apuesta; Claude analiza, calcula y entrega la lectura, y nunca coloca apuestas.**

**Dashboard en línea (se reconstruye solo en cada push a `main`):** https://ndaza654.github.io/apuestas-supermodelo/

## Flujo (actualizado 23-nov-2026)
1. **Recolección** (navegador del PC del usuario): Betano (mercados y cuotas) → Flashscore (últimos 10 partidos de cada equipo, directos, árbitro, tabla, alineaciones, historial por jugador o goles por jugador) → ValueStats (árbitros). Todo a `jornadas/AAAA-MM-DD/`.
2. **Análisis** (sin navegador): `python3 recoleccion/correr_jornada.py jornadas/AAAA-MM-DD` → fichas por mercado, modelo SM-1.2, `registro/lineas.csv`, informe HTML, sugerencias.
3. **Entrega**: informe interactivo + copia en `entregas/` + `registro/BITACORA.md`.
4. **Balance** (día siguiente): boletos de Betano, resultados de Flashscore, calificación de todo lo enviado, libro `registro/libro_apuestas.xlsx`, aprendizaje de combinadas.

## Carpetas
- `CLAUDE.md` — reglas fijas (se leen solas al abrir el repo). Es la fuente de verdad del proceso.
- `recoleccion/` — scripts de recolección y de pipeline (`README.md` explica la recolección y sus fallos conocidos).
- `supermodelo/` — el modelo (`MODELO_README.md`, `GUIA_RAPIDA.md`: históricos de la etapa de diseño del modelo; las reglas vigentes están en `CLAUDE.md`).
- `dashboard/` — generador del dashboard v2 «Mando» (`construir_v2.py`, `datos.py`, `v2/`). `docs/PLAN_DASHBOARD.md` es la propuesta original (ya construida).
- `.claude/agents/` — `corners`, `partido`, `jugadores`, `goles-resultado`, `tarjetas`, `combinadas`, `calificacion`. `.claude/skills/` — `analizar-partido`, `registrar-resultados`.
- `registro/` — base de datos (`lineas.csv`, `sugerencias.csv`, libro, bitácora). `jornadas/AAAA-MM-DD/` — datos y salidas de cada día. `entregas/` — copia de todo lo enviado por el chat. `pruebas/` — pruebas y backtest histórico.

## Pruebas
`python3 pruebas/test_modelo.py`, `test_ficha.py`, `test_betano.py`, `test_recoleccion.py`, `test_dashboard.py`; y `python3 dashboard/construir_v2.py /tmp/d.html`.

Los criterios de filtro (X de 10, colchón, contexto) vienen de tipsters y medios y **no tienen resultados verificados**; el modelo y las heurísticas de jugadores/goleador se declaran como no validadas hasta que los balances lo demuestren.

## Análisis del historial de boletos
`python3 recoleccion/analisis_historial_boletos.py` lee los boletos del usuario (4-nov en adelante) y escribe `registro/analisis_historial_boletos.json`: cómo se pierden (una pata o varias), cuántas patas conviene, mercados con más acierto. Se ve en el dashboard (Mi estrategia → «Tu historial de boletos») y su foco está en `CLAUDE.md`.
