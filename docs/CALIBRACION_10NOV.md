# Calibración del supermodelo con datos reales (10-nov-2026)

**Fuente.** Copia pública en GitHub de los datos de football-data.co.uk
(github.com/xgabora/Club-Football-Match-Data-2000-2025, `data/Matches.csv`): 238.858 partidos de 2000 a 2026 en 38 ligas.
Incluye resultado y descanso, cuota 1X2, Más/Menos 2.5 y la mejor cuota del mercado; en 22 ligas, además, remates, tiros
al arco, faltas, córners, amarillas y rojas. Las cuotas son de casas europeas, no de Betano.co. Los scripts van en `pruebas/calibracion/` (con su LEEME; las rutas
hay que ajustarlas a la carpeta donde se baje `Matches.csv`, que no va en el paquete por tamaño). Los resultados que usa
el modelo están en `datos/`.

**Método de condicionamiento.** Para comparar el simulador con la realidad hay que mirar la variación que NO explica
lo que ya sabe la casa. Se usaron dos versiones, que dieron lo mismo:
- residuos dentro de liga × goles esperados × diferencia de fuerza, con λ local y visitante ajustados al 1X2 y al
  Más/Menos 2.5 de cada partido;
- regresión por liga y temporada con efecto de cada equipo como local y como visitante, más el precio.

## 1. Quitar margen
| Prueba | n | Proporcional | Potencia | Shin | Diferencia potencia − proporcional |
|---|---|---|---|---|---|
| 1X2, log loss | 160.256 | 1,00411 | 1,00356 | 1,00364 | −0,00055 ± 0,00008 |
| Más/Menos 2.5, log loss | 107.318 | 0,67828 | 0,67814 | 0,67816 | −0,00013 ± 0,00005 |

- La ventaja de la potencia se mantiene con todos los márgenes, también con 8 % o más (como Betano).
- **Sesgo favorito–longshot** (proporcional, 2022+, 5 ligas):
  - no favorito con <35 % de probabilidad justa: gana 2–3 pts menos de lo que dice la cuota;
  - favorito >65 %: gana 3–4 pts más.
- **Empates:** bien calibrados.
- **Adoptado:** `METODO_SIN_MARGEN = 'potencia'`.

## 2. Marcador desde el precio (76.096 partidos con 1X2 + Más/Menos 2.5, 2016–2026)
λ local y visitante ajustados al precio con Poisson independiente, contra la realidad:

| | Poisson del precio | Real | Diferencia |
|---|---|---|---|
| Ambos marcan | 50,07 % | 52,32 % | +2,25 ± 0,18 pts |
| Empate | 24,26 % | 26,20 % | +1,94 ± 0,16 |
| 0-0 | 7,37 % | 7,45 % | +0,08 ± 0,10 |
| Local no marca | 24,63 % | 23,59 % | −1,04 ± 0,15 |
| Visitante no marca | 32,67 % | 31,54 % | −1,13 ± 0,17 |

- El patrón se repite en las 17 ligas con ≥2.500 partidos (Ambos: de +0,9 a +6,1 pts).
- **Dixon-Coles:** ρ ≈ −0,005, sin mejora. **Poisson bivariada:** mejora un poco el log loss con λ₃ = 0,05, pero no
  reproduce el patrón (sube el 0-0).
- El patrón (más empates y más Ambos, menos «un equipo no marca», el 0-0 igual) lo genera el **efecto marcador**: el que
  va perdiendo se vuelca. Real: el que pierde al descanso marca en el 2T un 13 % más que si fuera empatado.
- **SM-1:** Ambos +2,3, empate +1,7, local no marca −1,2, visitante no marca −0,8.

## 3. Momentos del simulador contra la realidad
Real: 62.164 partidos, condicionados. Sim: 24 partidos representativos × 3.000 simulaciones. v2 = configuración del 9-nov.

| Momento | Real | v2 (9-nov) | SM-1 |
|---|---|---|---|
| Ambos marcan − Poisson | +0,022 | −0,046 | +0,023 |
| Empate − Poisson | +0,019 | −0,014 | +0,017 |
| corr(dif. goles, dif. remates) | 0,14 | 0,30 | 0,12 |
| corr(dif. goles, dif. al arco) | 0,50 | 0,56 | 0,48 |
| corr(dif. goles, dif. córners) | −0,12 | −0,14 | −0,11 |
| var/media córners total / equipo | 1,11 / 1,34 | 1,47 / 1,39 | 1,16 / 1,40 |
| var/media remates total | 1,18 | 1,98 | 1,23 |
| var/media al arco total | 1,05 | 1,31 | 1,08 |
| var/media faltas total / equipo | 1,06 / 0,97 | 3,19 / 2,29 | 1,02 / 1,02 |
| var/media tarjetas total (amarilla 1, roja 2) | 1,23 | 1,68 | 1,24 |
| var/media amarillas por equipo | 0,85 | 1,13 | 0,83 |
| var/media goles total | 0,95 | 1,09 | 1,01 |
| corr remates–córners (total) | 0,28 | 0,22 | 0,23 |
| corr faltas–tarjetas | 0,29 | 0,58 | 0,25 |
| corr córners local–visitante | −0,18 | +0,05 | −0,18 |
| corr goles–remates (total) | 0,23 | — | 0,33 |
| corr goles–córners (total) | −0,04 | 0,08 | 0,05 |
| Tarjetas según dif. final 0 / 1 / 2 / 3+ (× media) | 1,03 / 1,05 / 0,95 / 0,82 | 1,05 / 1,05 / 0,98 / 0,85 | 1,04 / 1,04 / 0,97 / 0,84 |
| Rojas por equipo y partido | 0,099 | 0,096 | 0,097 |
| Goles del 1T | 44,3 % | 45,4 % | 45,0 % |
| Tarjetas del 1T | ~35 % (amarilla media al 59 % del partido, StatsBomb) | 43 % | 34 % |
| Goles 2T del que pierde al HT (× empate) | 1,13 | 0,93 | 1,09 |
| Goles 2T del que gana al HT (× empate) | 0,98 | 1,10 | 0,95 |

Diferencias que quedan: la relación goles–remates y goles–córners sigue algo alta en el simulador. Para las parejas de
patas donde eso pesa se aplica la corrección de la sección 4.

## 4. Dependencia entre patas de un combo
Lift = P(A y B) / (P(A)·P(B)), con la línea de cada estadística en su media:

| Pareja | Real | Simulador | Corrección |
|---|---|---|---|
| Gana el favorito + córners del favorito Más | 0,878 | 0,926 | ×0,948 |
| Gana el favorito + remates del favorito Más | 1,034 | 1,067 | ×0,969 |
| Gana el favorito + al arco del favorito Más | 1,272 | 1,281 | ×0,993 |
| Gana el favorito + Más 2.5 | 1,203 | 1,188 | ×1,013 |
| Gana el favorito + córners del no favorito Más | 1,071 | 1,059 | ×1,012 |
| Gana el favorito + tarjetas Más | 0,962 | 0,970 | ×0,991 |
| Más 2.5 + córners Más | 0,980 | 1,035 | ×0,947 |
| Ambos Sí + córners Más | 1,015 | 1,046 | ×0,970 |
| Más 2.5 + tarjetas Más | 1,004 | 0,950 | ×1,057 |
| Córners Más + tarjetas Más | 0,993 | 0,997 | ×0,996 |
| Más 2.5 + remates Más | 1,162 | 1,220 | ×0,953 |
| Ambos Sí + Más 2.5 | 1,550 | 1,565 | ×0,990 |
| Menos 2.5 + córners Menos | 0,977 | 1,028 | ×0,950 |
| Gana el favorito + Ambos Sí | 0,847 | 0,859 | ×0,987 |

## 5. Sistemas de tipsters con cuotas reales
38 ligas, ago-2012 → 2026. ROI a 1 u con la cuota media del archivo, y entre paréntesis con la mejor cuota del mercado:

| Sistema | n | Acierto | Precio | ROI (mejor cuota) |
|---|---|---|---|---|
| Referencia: Más 2.5 en todos | 107.273 | 49,9 % | 49,8 % | −5,8 % (−1,9 %) |
| Referencia: Menos 2.5 en todos | 107.273 | 50,1 % | 50,2 % | −6,2 % (−2,1 %) |
| IA #400: local ≤1,50 → Más 2.5 | 11.239 | 61,3 % | 60,7 % | −3,4 % (0,0 %) |
| IA #453: + empate ≥4,10 | 10.604 | 61,9 % | 61,4 % | −3,5 % (−0,2 %) |
| IA #5/#14: empate ≥3,60 → Más 2.5 | 42.643 | 56,8 % | 56,3 % | −4,0 % (−0,5 %) |
| IA #5: empate 2,90–3,20 → Menos 2.5 | 18.423 | 59,9 % | 59,5 % | −3,9 % (−0,3 %) |
| IA #26: parejo → Menos 2.5 | 58.298 | 53,4 % | 53,3 % | −5,2 % (−1,3 %) |
| IA #45: Bundesliga, empate 3,60–4,33, parejo → Empate | 534 | 27,3 % | 25,3 % | +1,5 % ± 14 (+5,9 %) |
| IA #45 completo (+ ≥2 empates en el H2H) | 175 | 30,3 % | 25,4 % | +12,7 % ± 25 (+17,7 %): muestra chica, sin significancia |
| IA #420: empate ≤3,40, parejo, sin rachas → Empate | 48.947 | 29,9 % | 29,3 % | −5,0 % (−0,2 %) |
| Referencia: empate en todos | 160.258 | 26,3 % | 25,8 % | −6,7 % (−1,3 %) |
| IA #414: favorito local siempre | 113.419 | 51,3 % | 51,6 % | −4,8 % (−0,4 %) |
| Favorito local 1,00–1,30 | 6.333 | 82,8 % | 81,5 % | −0,4 % (+2,9 %) |
| No favorito visitante 8–50 | 9.231 | 6,6 % | 7,1 % | −28,8 % (−15,0 %) |
| Jeke: contra el último (local gana) | 5.178 | 57,7 % | 58,7 % | −5,4 % (−1,7 %) |
| Jeke: contra el último (visitante gana) | 5.478 | 42,8 % | 42,8 % | −4,7 % (0,0 %) |

**Ambos Marcan.** No hay cuota de Ambos en la fuente, así que se compara contra la estimación corregida del precio:

| Sistema | n | Acierto | Estimación del precio | Diferencia |
|---|---|---|---|---|
| IA #429 (empate ≥3,90, visitante ≤2,00, local con 2 Ambos Sí seguidos) | 1.314 | 55,5 % | 55,5 % | 0,0 pts |
| Racha de 2 Ambos Sí del local, sola | 20.933 | — | — | 0,0 pts |
| IA #16 parcial | — | — | — | −0,5 pts |

Las rachas no agregan nada al precio.

## 6. Modelo de goles por promedios contra el mercado (5 ligas, 7.128 partidos, 2022–2026)
- **1X2:** log loss del modelo 0,9884 contra 0,9692 del mercado. Mezclar empeora con cualquier peso.
- **Más/Menos 2.5:** Brier 0,2420 contra 0,2387.
- **Apostar donde el modelo ve valor:** −14 % a −17 %, contra −6,8 % de apostar a todo.
- **Dixon-Coles:** sin mejora.
- **Decaimiento temporal** (vida media 180–365 d): −0,017 de log loss en la Premier 2022–2025, solo con historia de
  varias temporadas.

## 7. Backtests propios
| Prueba | Mercado | v2 | SM-1 | Lectura |
|---|---|---|---|---|
| 5-nov (17 partidos, 450 líneas), Brier | 0,2322 (potencia; 0,2328 proporcional) | 0,2331 | 0,2322 | SM-1 iguala al mercado; el v2 quedaba algo peor |
| 5-nov, log loss | 0,6566 | 0,6585 | 0,6566 | — |
| 9-nov (6 partidos, 273 líneas), Brier | 0,1959 proporcional / 0,2006 potencia | 0,1996 | 0,2005 | Diferencias dentro del ruido (SM-1 − mercado −0,0001 ± 0,0007). Día de pocos goles (11 contra 17,2 esperados), así que todo lo que favorecía goles quedó peor |

## 8. En vivo (desde el marcador real al descanso)
400 partidos reales al azar (2016–2026). El simulador arranca desde el marcador del descanso con las medias previas del
partido. Brier de la base: Más 2.5 0,2499, Ambos 0,2500, gana el local 0,2436, empate 0,2005.

| Versión | Goles del 2T (real 1,39 ± 0,06) | Brier Más 2.5 | Brier Ambos | Brier local gana | Brier empate | Suma |
|---|---|---|---|---|---|---|
| Sin actualizar la intensidad de gol | 1,49 | 0,1581 | 0,1730 | 0,1605 | 0,1810 | 0,6726 |
| Actualizando con los goles, forma 3 | 1,44 | 0,1569 | 0,1744 | 0,1617 | 0,1797 | 0,6727 |
| **Actualizando con los goles, forma 6 (adoptado)** | 1,47 | 0,1567 | 0,1724 | 0,1608 | 0,1799 | **0,6698** |

Goles del 2T según el marcador al descanso (forma 6):

| Marcador al HT | n | Real | SM-1 | Sin actualizar |
|---|---|---|---|---|
| 0-0 | 119 | 1,22 | 1,32 | 1,47 |
| 0-1 | 60 | 1,28 | 1,44 | 1,51 |
| 1-0 | 81 | 1,48 | 1,46 | 1,50 |
| 1-1 | 39 | 1,59 | 1,60 | 1,52 |
| Otros | 101 | 1,51 | 1,62 | 1,50 |

- Un 0-0 al descanso es información: es un partido de menos gol de lo que decía la cuota. Ahora entra en el modo en vivo
  (`VIVO_FORMA_GOLES = 6`).
- Con muchos goles en el 1T la actualización exagera un poco. Muestra de 400: cada grupo tiene ±0,1–0,2 goles de error.
- Lo observado (remates, córners y faltas) actualiza el ritmo con el mismo previo gamma del simulador. Prueba: con mucho
  ritmo en el 1T se esperan 2 córners más en lo que falta.
