---
name: analizar-partido
description: Flujo completo para analizar un partido en Betano.co con las fichas de córners, estadísticas de partido y jugadores. Úsalo cuando el usuario pida analizar un partido o una jornada.
---
# Analizar un partido

1. **Leer qué ofrece Betano** (navegador del computador; ver `recoleccion/README.md`): mercados, líneas, cuotas, jugadores y parejas. No analices líneas que Betano no ofrece.
2. **Recolectar contexto** (Sofascore + clima): alineaciones probables/confirmadas, bajas, últimos 7 partidos con estadísticas de cada equipo, directos, árbitro, tabla.
3. **Armar la entrada** `jornadas/AAAA-MM-DD/pub/entradas/<partido>.json` (formato en `MODELO_README.md` y `docs/`).
4. **Modelo:** `python3 -m supermodelo <entrada.json>` (probabilidad = 50 % simulación + 50 % mercado).
5. **Fichas:** `python3 recoleccion/ficha.py <entrada.json> jornadas/AAAA-MM-DD/fichas`.
6. **Especialistas:** lanza en paralelo los agentes `corners`, `partido` y `jugadores` con la ficha del partido; cada uno devuelve su lectura.
7. **Informe** (en español, hora de Bogotá): abre con «Enfoque de mercados»; luego, por mercado, las líneas que cumplen (≥5 de 7 en ambos equipos) con cuota, esperado, colchón y «X de 7»; después lo que no cumple, resumido; límites y datos que faltaron.
8. **Verificar** antes de entregar: cifras contra la fuente, `python3 pruebas/test_ficha.py`.

El usuario decide y apuesta. No recomiendes montos; informa probabilidad, cuota y EV.
