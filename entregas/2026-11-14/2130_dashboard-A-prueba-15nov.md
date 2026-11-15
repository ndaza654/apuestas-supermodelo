# Dashboard A «Mando» · prueba con datos de 12-nov (noche), 13-nov y 15-nov
**Entrega:** sáb 14-nov-2026, 21:30 Bogotá.
**Fuentes y horas:** Betano (cuotas del 15-nov leídas 14-nov 19:55; 12 y 13-nov con su lectura propia); Flashscore (10+10 últimos, alineaciones ~20:16–20:18, historial por jugador 20:20–21:05).
**Archivos:** `2130_dashboard-A-prueba-15nov.html` (el dashboard) y `2130_informe-15nov.html` (informe interactivo de la jornada con «Enfoque de mercados»).

## Qué se verificó
- Playwright a 1400 y 390 px: 90 controles probados (2 por tipo en cada una de las 16 páginas); todos cambian el estado salvo «Descargar CSV», que descarga `lineas_filtradas.csv` (3.437 filas). Cero errores de consola.
- Pruebas del repo: modelo 106, ficha 27, Betano 11, recolección 56.

## Historial de jugadores (regla obligatoria) — jornada 15-nov
Completo (10 de 10 partidos por equipo) para los 5 partidos con mercado de jugador de estadística: Bélgica–Italia, Croacia–Rep. Checa, España–Inglaterra, Francia–Turquía, Chipre–Montenegro. Los otros 8 partidos no ofrecen ese tipo de mercado. Detalle en `jornadas/2026-11-15/jugadores/LEEME.md`.

## Límites
- Chipre–Montenegro sin alineación publicada: sin recomendaciones de jugador.
- Solo 13 de ~21 partidos de las capturas del usuario se recolectaron.
- Flashscore no trae «faltas recibidas»; «entradas» son ganadas, Betano cuenta totales.
- El criterio de jugador por defecto es 7 de 10, n mínimo 7 (ajustable); en jornadas anteriores con historial más corto muchos jugadores caen en «sin muestra».
- Errores de código corregidos en esta tarea: cruce de nombres ambiguos (Bellingham, Pašalić, Esposito) por id de Flashscore verificado, y la «ı» turca. Los dos informes se regeneraron con la corrección.
