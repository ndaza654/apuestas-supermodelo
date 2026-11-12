---
name: analizar-partido
description: Flujo en dos etapas para analizar los partidos de un día en Betano.co (recolección con navegador + análisis sin navegador) con las fichas de córners, estadísticas de partido y jugadores. Úsalo cuando el usuario pida analizar una jornada o un partido.
---
# Analizar una jornada (dos etapas)

El usuario decide y apuesta; tú entregas probabilidad, cuota, regularidad y límites de los datos. Carpeta de trabajo: `jornadas/AAAA-MM-DD/`.

## Etapa 1 — Recolección (necesita el navegador del computador del usuario; ~22–23 h Bogotá del día anterior)
1. **Betano:** `recoleccion/betano_extraer.js` en la pestaña de betano.co → texto compacto de cada partido → `raw/bet_<clave>.txt` → `python3 recoleccion/betano.py jornadas/<día>/raw` → `betano/<clave>.json`. Primero se lee qué mercados ofrece cada partido.
2. **Flashscore:** `recoleccion/flashscore_extraer.js` en la pestaña de flashscore.co → `flashscore/<clave>.json` (últimos 7 de cada equipo con estadísticas, directos, árbitro, estadio). Emparejar cada partido de Betano con su `mid` de Flashscore (misma hora de inicio + nombres; Flashscore usa nombres en inglés). Pausas entre llamadas; si hay 403/429, parar y avisar.
3. **Situación (la lee Claude, no se adivina):** con la previa de Flashscore, la tabla y las bajas, escribir `notas/<clave>.json` (formato en `recoleccion/armar_entrada.py`, NOTAS_EJEMPLO): importancia, derbi, motivación, rotación, necesita ganar, bajas, dudas, fuentes. Sin esa lectura el partido queda «reserva», nunca «apto».
4. Guardar y subir al repo (commit + push) **antes** de que corra la etapa 2.

## Etapa 2 — Análisis (no necesita navegador; puede correr en la nube de madrugada)
1. `python3 recoleccion/correr_jornada.py jornadas/<día>` → entradas, fichas, informes del modelo, `ranking.md`.
   Si no hay `betano/*.json`, dice que la etapa 1 no dejó nada y termina: no se inventa.
2. Lanzar los agentes `corners`, `partido` y `jugadores` con las fichas de los partidos apto/reserva.
3. Escribir `jornadas/<día>/informe_final.md` (español, hora de Bogotá): abre con **«Enfoque de mercados»**; por partido y mercado, las líneas que cumplen (≥5 de 7 en ambos equipos) con cuota, esperado, colchón y «X de 7»; luego lo que no cumple, resumido; y los límites (datos que faltaron, partidos no aptos y por qué).
4. Verificar: `python3 pruebas/test_ficha.py`, cifras contra la ficha. Commit y push del resultado.

## Puntuación de contexto (`recoleccion/puntuar.py`)
Siempre las dos juntas: **datos** (por familia de mercado que Betano ofrece) y **situación**. Apto = datos ≥ 60 y situación ≥ 45 por mercado; reserva = datos suficientes pero situación sin leer; no apto = el resto. Nada se descarta en silencio.
Límites conocidos: sin historial por jugador ni alineación probable, el mercado de jugadores no es apto; las estadísticas del árbitro (B-Soccer) no están recolectadas; sin estadística por tiempo no hay ficha de 1T/2T.
