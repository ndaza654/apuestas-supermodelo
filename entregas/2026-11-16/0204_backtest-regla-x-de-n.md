# Backtest de la regla «X de N» en ligas de clubes (versión profunda)

- **Fecha y hora:** 16-nov-2026, 02:04 (Bogotá).
- **Datos:** 50.408 partidos de Premier League, La Liga, Bundesliga, Serie A, Ligue 1 y Brasileirão (2000/01 a 2026/27), football-data.co.uk (copia xgabora, `data/Matches.csv`). **Sin cuotas de Betano**: solo 1X2 y goles 2.5 de casas europeas.
- **Informe interactivo:** `0204_backtest-regla-x-de-n.html` (generador: `pruebas/backtest/`).
- **Corrección:** la entrega de las 01:50 decía «~230k partidos»; eran unos 50 mil (las 6 ligas). Además contaba el historial distinto a la ficha. Esta versión la reemplaza.

## Cómo se midió
Para cada partido, solo los partidos de liga anteriores de cada equipo (hasta 10, máximo 400 días). Regularidad, esperado y colchón calculados como en `recoleccion/ficha.py`. Regla por defecto: al menos 7 de 10 en ambos equipos, n mínimo 7. Motor verificado con un cálculo independiente en Python (córners Más 9.5: 3.621 partidos, 63,3 %; base 37.766, 54,4 %).

## Hallazgos (7 de 10 en ambos, todas las temporadas)
1. El filtro sube el acierto en todos los mercados, poco en goles y córners: córners Más 8.5 70,6 % (base 65,8 %); Más 9.5 63,3 % (54,4 %); goles Más 1.5 76,5 % (74,6 %); goles Más 2.5 59,3 % (50,0 %). Más en remates Más 22.5 76,8 % (63,8 %), tarjetas en puntos Más 3.5 75,9 % (61,2 %), faltas Más 24.5 86,3 % (62,0 %).
2. «7 de 10» no es 70 %: córners Más 9.5 da 63 %, goles Más 2.5 da 59 %. Remates, faltas y tiros al arco se sostienen en 77–86 %.
3. A igual colchón, cumplir o no la regularidad da casi lo mismo (0 a 4 puntos): córners Más 8.5 con colchón 2,1–2,7: 70,1 % cumple, 72,0 % no cumple; remates Más 22.5 con colchón 3,5–4,6: 74,6 % y 74,2 %; tarjetas Más 3.5 con colchón 1,4–2,1: 74,5 % y 70,6 %. El colchón explica el acierto tanto como el conteo.
4. Goles 2.5 contra el mercado: con filtro, Más acierta 59,8 % y la cuota sin margen decía 59,7 % (1.764 partidos); Menos 57,3 % y 57,3 % (1.486). El precio ya lo descuenta. En los demás mercados no hay cuotas para comprobarlo.
5. 8 de 10: córners Más 8.5 72,9 % (4.129) contra 70,6 % (11.678); remates Más 22.5 80,5 %; tarjetas Más 3.5 80,0 %.
6. Ligas: Ligue 1 floja en córners Más (8.5: 62,1 %; 9.5: 49,2 %, n 120); tarjetas Más 3.5 en La Liga 80,0 % y Serie A 77,4 %; Premier tarjetas Menos 5.5 83,2 %; faltas Más 24.5 en Premier solo 37,4 % de base.
7. Tiempo: córners Más 8.5 con filtro 72,0 % (2000–2011) → 67,4 % (2023–2026); Más 9.5 66,2 % → 58,8 %; Menos 10.5 63,9 % → 67,1 %; faltas Más 24.5 de base 77,6 % → 41,8 %.
8. Frecuencia: córners Más 8.5 aparece en 31 % de los partidos, Más 9.5 en 10 %, goles Más 2.5 en 4 %, tarjetas Más 3.5 en 28 %, remates Más 22.5 en 31 %.

## Límites (qué no se leyó)
Sin líneas ni cuotas de Betano (rejilla fija); cuotas solo en 1X2 y goles 2.5; Brasil solo goles; historial solo de liga, sin directos ni copas; tarjetas en puntos = amarillas + 2 × rojas con posible diferencia en dobles amarillas; tiros al arco y faltas con cambios de conteo en la fuente según el año; sin jugadores, fueras de juego, saques ni mitades; sin el supermodelo; clubes, no selecciones.
