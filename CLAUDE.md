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

## Cómo se corre
- Modelo: `python3 -m supermodelo <entrada.json>`  ·  pruebas: `python3 pruebas/test_modelo.py` y `python3 pruebas/test_ficha.py`
- Ficha por mercado: `python3 recoleccion/ficha.py <entrada.json> [carpeta_salida]`
- Flujo de un partido: ver `.claude/skills/analizar-partido/SKILL.md`. Resultados y calificación: `.claude/skills/registrar-resultados/SKILL.md`.
- Recolección (Betano y Sofascore desde el navegador de su computador): `recoleccion/README.md`.
- Una jornada vive en `jornadas/AAAA-MM-DD/` (entradas, fichas, informes, picks). `_scripts_legacy/` es solo referencia: tiene rutas absolutas viejas y no se ejecuta.

## Calidad
- Antes de entregar: revisar cifras contra su fuente, correr las pruebas, abrir el informe.
- Si un dato falta (alineación, estadística, árbitro), decirlo en la ficha; no rellenar con supuestos.
- No tocar nada del GitHub del usuario fuera de este repositorio.
