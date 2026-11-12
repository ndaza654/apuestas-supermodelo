# Apuestas · súper modelo + fichas por mercado

Proyecto de apuestas de fútbol en **Betano.co** (COP; 1 u = 3.700 COP; tarjetas en puntos: amarilla 1, roja 2).
**El usuario decide y apuesta él mismo.** Claude analiza, calcula probabilidades y entrega la lectura; nunca coloca apuestas.
Responder siempre en **español**; horas en **Bogotá (UTC−5)**.

## Reglas fijas
1. Mercados de jugadores: solo con alineaciones confirmadas o probables (fuente y hora en la ficha).
2. Analizar las parejas «cualquiera de los jugadores…» y los mercados descanso/final cuando Betano los ofrezca.
3. **Primero leer qué mercados ofrece Betano, después analizar** (no inventar líneas que no existen).
4. Usar el navegador para visitar las páginas (Betano, Sofascore); no trabajar de memoria con datos que cambian.
5. Todo informe abre con un bloque **«Enfoque de mercados»** (qué mercados pesan en este partido y por qué).

## Criterio de las fichas por mercado (mercados de prueba: córners, estadísticas de partido, estadísticas de jugadores)
- **Muestra:** últimos **7 partidos oficiales** del local + últimos 7 del visitante, **combinados y en cualquier sede**, + enfrentamientos directos (los que existan, con sus estadísticas).
- **Regularidad:** se muestra «X de 7» por equipo. **Cumple con ≥ 5 de 7** (4 de 7 se muestra, no cumple; n mínimo 5).
- **Colchón** = esperado por los datos − línea de Betano (Más) / línea − esperado (Menos). Es **solo informativo**: sin umbral, sin desviaciones, y **no se evita ni se excluye ninguna línea de Betano por su colchón**. La línea de Betano va siempre en la hoja.
- Esperado por equipo = (lo que el equipo hace a favor + lo que el rival concede)/2; total = suma.
- Jugadores: tasa por 90 × minutos esperados; regularidad en los últimos ≤7 partidos jugados.
- El objetivo es la **probabilidad de la línea**, no el error de cuota. EV = p·cuota − 1 se informa, no manda.
- Cada criterio lleva dato, referencia, n, fuente y cumple/no cumple. Honestidad: los criterios vienen de tipsters y medios sin resultados verificados; sin estadística por tiempo no hay ficha de 1T/2T; sin `ficha.h2h` no hay directos.

## Agentes por mercado (`.claude/agents/`)
`corners`, `partido`, `jugadores` (los 3 mercados de prueba) y `goles-resultado`, `tarjetas`, `combinadas`, `calificacion`. Cada uno trabaja sobre la ficha y el informe del partido; `combinadas` va después de los demás y `calificacion` al día siguiente con los resultados en `jornadas/AAAA-MM-DD/resultados/`.
Goles y tarjetas salen en la ficha (`goles`, `tarjetas`) pero **no entran en el ranking** de aptos. Tarjetas: Betano cuenta en puntos y Flashscore solo trae amarillas (la serie queda por debajo si hubo rojas).

## Contexto de la sesión (que no se llene)
- Una sesión por jornada. Empezar leyendo `jornadas/AAAA-MM-DD/ranking.md` y `ESTADO.md`; la ficha de un partido solo cuando se va a analizar. No abrir los JSON crudos de `flashscore/` ni `betano/`.
- Los agentes escriben su detalle en archivos (`jornadas/AAAA-MM-DD/agentes/<partido>_<agente>.md`) y devuelven al chat solo un resumen corto (las 5 mejores líneas y los límites).

## Cómo se corre
- Dependencias: `pip install -r requirements.txt` (numpy, scipy; sin scipy el modelo falla).
- Modelo: `python3 -m supermodelo <entrada.json>`  ·  pruebas: `python3 pruebas/test_modelo.py`, `python3 pruebas/test_ficha.py` y `python3 pruebas/test_betano.py` y `python3 pruebas/test_recoleccion.py`
- Ficha por mercado: `python3 recoleccion/ficha.py <entrada.json> [carpeta_salida]`
- Flujo de un partido: ver `.claude/skills/analizar-partido/SKILL.md`. Resultados y calificación: `.claude/skills/registrar-resultados/SKILL.md`.
- Recolección desde el navegador de su computador: Betano (`recoleccion/betano_extraer.js` + `betano.py`, verificado), contexto en Flashscore (preferida por el usuario) o Sofascore (hoy da 403), árbitro en B-Soccer. Detalle: `recoleccion/README.md`.
- **Dos etapas:** (1) recolección con el navegador del PC, sube los datos al repo; (2) análisis sin navegador: `python3 recoleccion/correr_jornada.py jornadas/AAAA-MM-DD` (corre solo con lo que hay en el repo; si falta, lo dice y no inventa).
- Una jornada vive en `jornadas/AAAA-MM-DD/` (entradas, fichas, informes, picks). `_scripts_legacy/` es solo referencia: tiene rutas absolutas viejas y no se ejecuta.

## Calidad
- Antes de entregar: revisar cifras contra su fuente, correr las pruebas, abrir el informe.
- Si un dato falta (alineación, estadística, árbitro), decirlo en la ficha; no rellenar con supuestos.
- No tocar nada del GitHub del usuario fuera de este repositorio.
