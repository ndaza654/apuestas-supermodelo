# Qué cambia en el análisis de hoy (16-nov) tras el backtest, y página nueva del dashboard

- **Fecha y hora:** 16-nov-2026, 02:48 (Bogotá). **Cuotas:** Betano, leídas el 15-nov 20:13–20:14 (sin releer). **Datos del backtest:** 50.408 partidos de 5 grandes ligas y Brasil (football-data.co.uk); cuotas de la base europeas.
- **Límites:** la tasa histórica es de clubes, no de selecciones; no hay cuotas de Betano; mercados fueras de juego y saques no medidos; líneas asiáticas sin tasa (9 de las 166 líneas que cumplen: «sin dato»).

## 1. Las tarjetas entran
La exclusión («sin árbitro y peor calibración») era una regla de `analisis_jornada.py` de la auditoría del 13-nov, no una decisión del usuario, y los datos no la respaldan: con «cumple», tarjetas Más se dieron 24 de 27 y Menos 33 de 45, igual a lo que decía el modelo. Se quitó; también entran al resumen de la ficha. Las 12 líneas de tarjetas que cumplen hoy:

| Partido | Línea | Cuota | p recortada | Histórico (clubes) | Resultado del filtro |
|---|---|---|---|---|---|
| Grecia–Serbia | Tarjetas visitante Menos 3.5 | 1,25 | 76 % | 85 % | **entra como protección** |
| Albacete–Celta II | Tarjetas Más 4.5 | 1,55 | 64 % | 61 % | **entra como sencilla** |
| Estonia–Bulgaria | Tarjetas local Menos 2.5 | 1,53 | 60 % | 77 % (a favor) | **entra como sencilla** |
| Alemania–P. Bajos | local Más 0.5 / Más 1.5 | 1,17 / 1,15 | 85 % / 87 % | 84 % / 90 % | no (cuota < 1,20) |
| Grecia–Serbia | local Más 0.5; Menos 6.5 | 1,18 / 1,15 | 84 % / 83 % | 82 % / 86 % | no (cuota < 1,20) |
| Grecia–Serbia | visitante Menos 2.5 | 1,67 | 54 % | 68 % (a favor) | no (p recortada < 55 %) |
| Feroe–Moldavia | Menos 4.5; visitante Menos 2.5 | 2,02 / 2,05 | 46 % / 45 % | 79 % / 74 % (a favor) | no (cuota ≥ 2,00 / p) |
| Macedonia–Eslovenia | local Menos 2.5; Menos 4.5 | 1,75 / 1,78 | 54 % / 53 % | 75 % / 64 % (a favor) | no (p recortada < 55 %) |

## 2. Segunda opinión histórica (no recorta p)
Cada línea muestra la tasa de acierto, en ligas de clubes, de las líneas iguales con el mismo X de 10 y el mismo tramo de colchón (tabla `registro/tasas_historicas.json`). Se probó contra 817 líneas ya jugadas (4 jornadas, selecciones y otras): error de Brier modelo 0,1434, histórico solo 0,1490, promedio 0,1429, mezcla 75/25 0,1423. Cuando el histórico estaba por debajo del modelo (≥ 10 puntos) el modelo acertó (88 % real contra 88 % del modelo); cuando estaba por encima, lo real quedó entre los dos (69 % real, modelo 61 %, histórico 82 %). Mezclar mejora 0,001: no justifica cambiar p. Se usa como semáforo.

Semáforo en las 166 líneas que cumplen hoy: 129 sin discrepancia, 25 a favor (histórico ≥ 10 puntos por encima), 3 en contra, 9 sin dato. Las 3 en contra: Estonia–Bulgaria Goles Menos 3.5 (p recortada 83 %, histórico 73 %), Macedonia–Eslovenia Goles local Menos 1.5 (86 % / 70 %) y R. C. Africana–Benín Goles local Menos 1.5 (84 % / 70 %); las tres son «protecciones» de cuota ~1,15–1,18. Ninguna sugerencia queda «en contra».

## 3. Qué cambia en las sugerencias de hoy
- Protecciones: 33 → 34 (entra Grecia–Serbia tarjetas visitante Menos 3.5).
- Sencillas 1,50–1,99: 7 → 9 (entran Albacete tarjetas Más 4.5 y Estonia–Bulgaria tarjetas local Menos 2.5).
- Combinadas de 2 patas: iguales (3).
- Lotería: cambia (cuota 2,05 → 2,02; p recortada 44 % → 46 %): ahora incluye Grecia–Serbia tarjetas visitante Menos 3.5.
- `registro/sugerencias.csv` se regeneró con la versión nueva (ningún partido de hoy había empezado); las filas de otros días se recalificaron solas con los resultados ya guardados.

## 4. Página nueva del dashboard: «Backtest histórico»
https://ndaza654.github.io/apuestas-supermodelo/#/backtest (menú Explorar; tarda ~1 min tras el push). Pestañas: Hallazgos (con la prueba contra tus líneas jugadas), **Hoy** (las 166 líneas con su tasa histórica y semáforo; tocar una abre su cohorte), Explorar (mercado, ámbito, línea, lado, K de N, colchón, cuota del favorito, liga, temporada, equipo; escalera de líneas, por regularidad, mismo colchón, liga, temporada, cuota), **Mi línea** (calculadora), Ranking de líneas (con CSV) y Partidos (con CSV).
