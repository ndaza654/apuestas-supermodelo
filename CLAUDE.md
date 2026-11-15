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

## Regla de recolección: historial de jugadores obligatorio (desde el 14-nov-2026, vale para CUALQUIER chat, cuenta o sesión)
La recolección de una jornada **no se da por completa** sin el historial por jugador de los partidos que lo necesitan:
1. **Qué partidos lo necesitan:** los que en Betano ofrecen al menos un mercado de jugador de **estadística** (`sh` remates, `sot` tiros al arco, `tk` entradas, `fc` faltas cometidas, faltas recibidas, `sv` atajadas, `as` asistencias, anota-o-asiste con estadística). Los que no traen mercado de jugador, o solo goleador (`an`/`aoa`) y/o tarjeta (`tj`), **no** necesitan historial (el usuario no los apuesta).
2. **Qué se trae:** para cada equipo de esos partidos, las estadísticas por jugador de sus **últimos 10 partidos oficiales** (los mismos de la ficha de equipo) con **todas** las columnas de Flashscore (minutos, goles, asistencias, remates, a puerta, entradas, faltas cometidas, atajadas, rating…), el equipo de cada jugador y las alineaciones probables/confirmadas. Se guarda en `jornadas/AAAA-MM-DD/jugadores/<partido>.json` + `LEEME.md` (cobertura real: cuántos de los 10 partidos y cuántos jugadores; qué faltó).
3. **Cuándo:** en la **etapa 1, antes de entregar cualquier análisis** de esa jornada; no se espera a que el usuario lo pida a media jornada. Si algo no se pudo leer, se dice en `ESTADO.md` y en el informe (qué partido, qué jugadores) y esos mercados de jugador no se recomiendan.
4. **Límites que se declaran siempre:** Flashscore no trae «faltas recibidas»; «entradas» son entradas ganadas/intentadas de Flashscore (Betano cuenta entradas totales: no son idénticas); lo recogido pasa transcrito por el chat y se verifica con hash.
5. **Cómo:** `recoleccion/flashscore_jugadores_iframe.js` (carga cada partido pasado en un iframe de la propia pestaña de Flashscore, 3 en paralelo) → `recoleccion/jugadores_decod.py`.

## Criterio de las fichas por mercado (mercados de prueba: córners, estadísticas de partido, estadísticas de jugadores)
- **Muestra (regla desde el 13-nov-2026, para TODAS las recolecciones nuevas):** últimos **10 partidos oficiales** del local + últimos 10 del visitante, **combinados y en cualquier sede**, + enfrentamientos directos con sus estadísticas: **6 como máximo** (si hay menos, los que existan; si no hay, se dice). Antes era 7 + directos: los datos recogidos con 7 se declaran «muestra de 7» y no se comparan sin más con los de 10. Constantes únicas en `recoleccion/ficha.py` (`N`, `N_H2H`, `MIN_N`, `CUMPLE`) y `flashscore_extraer.js` (`n`, `nH2H`). El pipeline detecta la muestra real de la jornada (`ficha.muestra_de` / `fijar_muestra`): con 7 partidos usa solo «5 de 7, n mínimo 5» en fichas, ranking, registro e informe.
- **Regularidad:** se muestra «X de 10» por equipo. **Cumple con ≥ 7 de 10** (6 de 10 se muestra, no cumple; n mínimo 7). El 7 de 10 es la proporción del 5 de 7 anterior; el usuario puede cambiarlo en `CUMPLE`/`MIN_N`.
- **Colchón** = esperado por los datos − línea de Betano (Más) / línea − esperado (Menos). Es **solo informativo**: sin umbral, sin desviaciones, y **no se evita ni se excluye ninguna línea de Betano por su colchón**. La línea de Betano va siempre en la hoja.
- Esperado por equipo = (lo que el equipo hace a favor + lo que el rival concede)/2; total = suma.
- Jugadores: tasa por 90 × minutos esperados; regularidad en los últimos ≤10 partidos jugados.
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
- `python3 recoleccion/informe_html.py jornadas/AAAA-MM-DD` → `jornadas/AAAA-MM-DD/informe.html` (lo genera también `correr_jornada.py` al final de la etapa 2). Lee `registro/lineas.csv` + `ranking.json` + `ESTADO.md`; autónomo (sin red); pestañas Resumen, Líneas de equipo, Jugadores, Cupón y Datos y límites; filtros por partido, mercado, ámbito, lado, cuota, p modelo, EV, cumple ≥7 de 10, titular y búsqueda; el colchón es informativo y no oculta ninguna línea.
- Antes de entregarlo: abrirlo (por ejemplo con Playwright), comprobar que los filtros responden y que no hay errores de consola. Entregarlo con SendUserFile o como artefacto, y guardar la copia en `entregas/` según la regla de Entregas.
- **El «cumple» es un filtro ajustable dentro del informe** (barra de arriba): «al menos K de N», n mínimo, y en qué equipos (ambos / local / visitante / cualquiera), con atajos y una tabla que muestra cuántas líneas cumplen con cada K por partido. Por defecto 7 de 10 (5 de 7 si la jornada se recogió con 7 partidos). Todo el informe se recalcula; sigue siendo solo lectura y el colchón no oculta nada.
- **Pestaña «Análisis» (la primera del informe, desde el 14-nov):** abre con **«Enfoque de mercados»** (lo escribe Claude en `jornadas/AAAA-MM-DD/enfoque.md`, con cifras revisadas) y sigue con las **sugerencias** y el **«real hasta hoy»**. Las arma `python3 recoleccion/analisis_jornada.py jornadas/AAAA-MM-DD` (lo corre también `correr_jornada.py`) con las reglas de la auditoría: p recortada = p del modelo × el menor factor real (mercado-lado y banda de cuota); cuota < 1,50 = «protección»; 1,50–1,99 = sencilla con la p recortada; combinadas de máximo 2 patas del mismo partido (cada una ≥ 70 % recortada, conjunta de la simulación recortada 20 %, sin familias con alerta del modelo, máximo una «córners Más + goles Menos» por día); 3+ patas solo «lotería»; tarjetas y jugadores sin historial no entran. Escribe `analisis.json`, `informe_final.md` y `sugerencias.json`; `python3 recoleccion/sugerencias.py` las agrega a `registro/sugerencias.csv` como «pendiente» y las califica solas cuando `registro/lineas.csv` tenga el resultado.
- Mejoras al informe se hacen **en `recoleccion/informe_html.py`** (para que todas las sesiones las hereden), no en una copia suelta. Un análisis de un solo partido o un balance puede añadir su propia sección al HTML o un `.md` junto a él, pero la base interactiva siempre sale del generador. Si falta `registro/lineas.csv` para esa jornada, correr antes `correr_jornada.py`.

## Balances (valen para CUALQUIER chat, cuenta o sesión)
Cuando el usuario pida un balance (de un día o de varios):
1. Leer sus apuestas en Betano (Mis apuestas → historial, solo lectura). Las que siguen **en vivo o sin liquidar** se anotan como `pendiente` y se completan cuando terminen (en el balance siguiente); nunca se dan por ganadas o perdidas antes.
2. Calificar **todas mis líneas y sugerencias** de esos días (las apostadas y las que no): cuáles se dieron, cuáles no, con el resultado real (Flashscore) y la regularidad/p/EV que tenían. Llenar `registro/lineas.csv` (`apostada`, `stake`, `resultado`, `cuota_cierre`). Agente: `calificacion`.
3. Entregar al usuario un **informe HTML dinámico con filtros solo de ese día o esos días** (por partido, mercado, familia, lado, apostada/no, acierto, cumple con K de N, cuota, p, EV; retroalimentación fácil de leer: qué criterios funcionaron y cuáles no). Se hace con un generador del repo (`recoleccion/balance_html.py`, a crear en el primer balance y mejorar ahí), no a mano.
4. **Además**, agregar ese balance al **libro de apuestas** `registro/libro_apuestas.xlsx` (historial acumulado desde el 4-nov-2026: boletos, selecciones, líneas, resultados, lecciones) y a `registro/BITACORA.md`. Son dos entregas distintas: el informe del periodo es para leer; el libro es la memoria acumulada. Las apuestas pendientes quedan en el libro marcadas y se actualizan después.
5. Guardar la copia del informe según la regla de Entregas (`entregas/`), commit y push.
Las conclusiones sobre los filtros/criterios de tipsters se sacan en estos balances, no antes.

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
- **Registro de líneas (la «base de datos»):** `registro/lineas.csv` (separador `;`, abre en Excel/Sheets). `correr_jornada.py` agrega TODAS las líneas de Betano de la jornada, cumplan o no, con la lectura de la ficha (X de 10, esperado, colchón, cumple) y la del modelo (p, p_mercado, EV, alerta) en la misma fila; correr de nuevo la jornada reemplaza sus filas. Las columnas `apostada`, `stake`, `resultado` y `cuota_cierre` las llena `calificacion` (y el usuario si apostó). No hay otra base de datos. Junto a él, el historial anterior: `registro/historial_lineas.csv` (323 líneas del 9, 11 y 12-nov con cuota, p, EV; resultado real en 9 y 11-nov; apuesta vacía), `registro/metodos.csv` y `registro/BITACORA.md` (qué se entregó cada día, con qué modelo y criterios, qué se midió).
- Una jornada vive en `jornadas/AAAA-MM-DD/` (entradas, fichas, informes, picks). `_scripts_legacy/` es solo referencia: tiene rutas absolutas viejas y no se ejecuta.

## Calidad
- Antes de entregar: revisar cifras contra su fuente, correr las pruebas, abrir el informe.
- Si un dato falta (alineación, estadística, árbitro), decirlo en la ficha; no rellenar con supuestos.
- No tocar nada del GitHub del usuario fuera de este repositorio.
