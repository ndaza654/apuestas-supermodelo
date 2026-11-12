# Tarjetas de equipo/partido: Luxemburgo - Estonia (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Barbara I.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=7, directos n=1 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (3.0 a favor + 3.29 que concede el visitante)/2 = **3.14**
- Visitante: (1.86 a favor + 3.14 que concede el local)/2 = **2.5**
- Total = **5.64** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 6.23 / sin contexto 5.95 / implícita Betano 5.92; local: modelo 2.94 / sin contexto 2.81 / implícita Betano 2.82; visitante: modelo 3.29 / sin contexto 3.14 / implícita Betano 3.13

## Series (a favor, en contra) por partido
- Local (7): [(1, 3), (6, 3), (2, 4), (2, 2), (3, 4), (0, 2), (7, 4)]
- Visitante (7): [(1, 1), (3, 6), (2, 3), (2, 1), (4, 10), (0, 1), (1, 1)]
- Directos (1, [local, visitante]): [(6, 3)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 5.5 | Más | 1.8 | 5.64 | +0.14 | 4 de 7 | 2 de 7 | 1 de 1 | no | sí | -0.23 |
| total | 5.5 | Menos | 1.95 | 5.64 | -0.14 | 3 de 7 | 5 de 7 | 0 de 1 | no | sí | +0.11 |
| local | 2.5 | Más | 1.78 | 3.14 | +0.64 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.24 |
| local | 2.5 | Menos | 1.98 | 3.14 | -0.64 | 4 de 7 | 4 de 7 | 0 de 1 | no | sí | +0.13 |
| visitante | 2.5 | Más | 1.6 | 2.5 | +0.0 | 5 de 7 | 2 de 7 | 1 de 1 | no | sí | -0.20 |
| visitante | 2.5 | Menos | 2.27 | 2.5 | +0.0 | 2 de 7 | 5 de 7 | 0 de 1 | no | sí | +0.14 |
| 1T | 1.5 | Más | 1.6 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 2.27 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.09 | 3.14 / 2.5 | 6 de 7 | 6 de 7 | 7 de 7 | 7 de 7 | 1 de 1 | SÍ | no | -0.07 |
| 1 | No | 6.6 | 3.14 / 2.5 | 1 de 7 (<N) | 1 de 7 (<N) | 7 de 7 | 7 de 7 | 0 de 1 | no | sí | -0.06 |
| 2 | Sí | 1.47 | 3.14 / 2.5 | 5 de 7 | 4 de 7 | 7 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.06 |
| 2 | No | 2.57 | 3.14 / 2.5 | 2 de 7 (<N) | 3 de 7 (<N) | 7 de 7 | 3 de 7 | 0 de 1 | no | sí | +0.10 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 3.14 vs visitante 2.5.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 2.72 | 2 de 7 | 4 de 7 | 1 de 1 | no | sí | +0.17 |
| X (igual) | 4.5 | 1 de 7 | 2 de 7 | 0 de 1 | no | sí | -0.04 |
| 2 (visitante más) | 2.05 | 4 de 7 | 1 de 7 | 0 de 1 | no | sí | -0.27 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 1 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(6, 3)]; totales [9]. Con n=1 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: alta; motivación local/visitante: alta / alta; necesita ganar local/visitante: True / False; árbitro: Barbara I. (sin estadísticas).
- Dudas abiertas en la ficha: ninguna
- Fuentes del contexto: Tabla calculada con los resultados de Flashscore (4 jornadas jugadas hasta el 6-oct-2026): Grupo C4 → Islandia 8, Estonia 6, Bulgaria 4, Luxemburgo 3. Luxemburgo es último y necesita ganar.; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- Ninguna.

## Lectura
Ninguna línea cumple. El esperado total (5.64) es el más alto de la jornada y queda justo sobre la línea 5.5 (Más col +0.14; L 4/7 y V 2/7). La serie de Estonia incluye un 4 a favor / 10 en contra, que infla la media de lo que concede. Ambos ≥1 Sí @1.09 cumple (6/7 y 6/7) pero cuota < 1.20.
Línea ajustada: el recuento real con rojas puede diferir. Directos n=1.

_Cifras recalculadas desde las series de la ficha y verificadas contra `ficha.tarjetas.lineas` (coinciden las X de n y los cumple). EV = p·cuota−1 informativo._
