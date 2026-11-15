# Dashboard v2 «Mando» (blanco y azul) · prueba funcional completa
**Entrega:** dom 15-nov-2026, 05:05 Bogotá. **Archivo:** `0505_dashboard-v2-mando.html` (autónomo, sin red).
**Datos:** jornada del 14-nov (resultados, líneas calificadas, sugerencias y boletos) y jornada del 15-nov (recolección: Betano leído 14-nov 19:55 Bogotá; Flashscore, alineaciones e historial de jugadores 14-nov ~20:16–21:05; las 10 combinadas y 52 líneas de tu estrategia).
**Cómo se genera:** `python3 dashboard/construir_v2.py salida.html 2026-11-14 2026-11-15` (código en `dashboard/v2/`).

## Páginas
Inicio · Partidos · Partido (resumen, gráficos por mercado con rival/sede/marcador, escalera, líneas, jugadores, cómo salió) · Mi estrategia (filtro en vivo + cómo le fue a ese filtro en lo ya jugado) · Cupón (armador de combinadas, probabilidad real, avisos, guardar, «ya lo aposté») · Todas las líneas (CSV) · Jugadores · Mis apuestas · Qué funciona · Lo que te envié · Datos y límites · Documentos · buscador global.

## Verificado
Playwright a 1400 y 390 px: 209 controles probados en cada tamaño (botones, filtros, pestañas, selectores, cabeceras de tabla, descargas), ninguno sin efecto; buscador; cero errores de consola; sin desborde horizontal.

## Límites
- Muestra chica: 17 partidos resueltos. Lo de «Qué funciona» son pistas, no conclusiones.
- La jornada del 14-nov se recogió con 7 partidos por equipo (la regularidad usa la misma proporción); solo 1 partido del 14 tiene historial de jugadores.
- El «índice de sentido» ordena; no es una probabilidad. El modelo queda casi igual al precio de Betano.
- No hay ranking del rival: el contexto «fácil/difícil» es rival, sede y marcador de cada partido.
- Lo que anotas (cupón, filtros, apuestas) vive en el navegador donde abras el archivo; hay botón para descargar y cargar una copia.
- Sin faltas recibidas (Flashscore no las trae); entradas = ganadas; tarjetas = solo amarillas.
