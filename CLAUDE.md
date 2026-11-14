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

## Entregas (memoria de lo que se publica en el chat) — vale para CUALQUIER chat, cuenta o sesión
Todo **informe, análisis, balance, combinada, lectura en vivo o resumen con líneas/probabilidades** que se entregue al usuario en el chat se guarda en el repo **en la misma respuesta**, sin que él lo pida:
1. Copia del contenido en `entregas/AAAA-MM-DD/HHMM_tema[_partido].md` (hora de Bogotá de la entrega; `.html` si fue una página o artefacto; texto íntegro, no un resumen). Debe llevar arriba: fecha y hora, fuente y hora de las cuotas, y los límites (qué no se leyó).
2. Una línea nueva (la más reciente arriba) en `entregas/INDICE.md`: fecha, hora, tema, partido(s), archivo.
3. `git add`, commit y push **a la rama en uso**; si estás en `main`, crea una rama primero (`entregas/AAAA-MM-DD`). Nunca force-push ni reescribir historia. Si el push es rechazado: `git pull --rebase` y reintentar.
4. Al terminar la respuesta, decir en una línea que quedó guardada y dónde.
No se guardan las respuestas cortas o de conversación (sin líneas, probabilidades ni balances). Si una sesión no tiene acceso a git, decirlo y dejar el texto en el chat para que el usuario lo guarde. `entregas/` no reemplaza a `registro/` (datos para calificar) ni a `jornadas/` (datos y salidas del pipeline).

## Informes en HTML interactivo (valen para CUALQUIER chat, cuenta o sesión)
Los informes, análisis y balances de una jornada **no se entregan como texto plano**: se entregan como **HTML interactivo** (filtros, gráficos, cupón), hecho con el generador del repo, no a mano:
- `python3 recoleccion/informe_html.py jornadas/AAAA-MM-DD` → `jornadas/AAAA-MM-DD/informe.html` (lo genera también `correr_jornada.py` al final de la etapa 2). Lee `registro/lineas.csv` + `ranking.json` + `ESTADO.md`; autónomo (sin red); pestañas Resumen, Líneas de equipo, Jugadores, Cupón y Datos y límites; filtros por partido, mercado, ámbito, lado, cuota, p modelo, EV, cumple ≥5 de 7, titular y búsqueda; el colchón es informativo y no oculta ninguna línea.
- Antes de entregarlo: abrirlo (por ejemplo con Playwright), comprobar que los filtros responden y que no hay errores de consola. Entregarlo con SendUserFile o como artefacto, y guardar la copia en `entregas/` según la regla de Entregas.
- Mejoras al informe se hacen **en `recoleccion/informe_html.py`** (para que todas las sesiones las hereden), no en una copia suelta. Un análisis de un solo partido o un balance puede añadir su propia sección al HTML o un `.md` junto a él, pero la base interactiva siempre sale del generador. Si falta `registro/lineas.csv` para esa jornada, correr antes `correr_jornada.py`.

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
- **Registro de líneas (la «base de datos»):** `registro/lineas.csv` (separador `;`, abre en Excel/Sheets). `correr_jornada.py` agrega TODAS las líneas de Betano de la jornada, cumplan o no, con la lectura de la ficha (X de 7, esperado, colchón, cumple) y la del modelo (p, p_mercado, EV, alerta) en la misma fila; correr de nuevo la jornada reemplaza sus filas. Las columnas `apostada`, `stake`, `resultado` y `cuota_cierre` las llena `calificacion` (y el usuario si apostó). No hay otra base de datos. Junto a él, el historial anterior: `registro/historial_lineas.csv` (323 líneas del 9, 11 y 12-nov con cuota, p, EV; resultado real en 9 y 11-nov; apuesta vacía), `registro/metodos.csv` y `registro/BITACORA.md` (qué se entregó cada día, con qué modelo y criterios, qué se midió).
- Una jornada vive en `jornadas/AAAA-MM-DD/` (entradas, fichas, informes, picks). `_scripts_legacy/` es solo referencia: tiene rutas absolutas viejas y no se ejecuta.

## Calidad
- Antes de entregar: revisar cifras contra su fuente, correr las pruebas, abrir el informe.
- Si un dato falta (alineación, estadística, árbitro), decirlo en la ficha; no rellenar con supuestos.
- No tocar nada del GitHub del usuario fuera de este repositorio.
