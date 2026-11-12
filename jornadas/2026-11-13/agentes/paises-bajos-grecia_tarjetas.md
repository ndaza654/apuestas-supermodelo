# Tarjetas de equipo/partido: Países Bajos - Grecia (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Saggi R.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=6, visitante n=7, directos n=3 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (0.83 a favor + 1.57 que concede el visitante)/2 = **1.2**
- Visitante: (2.57 a favor + 2.0 que concede el local)/2 = **2.29**
- Total = **3.49** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 4.85 / sin contexto 4.51 / implícita Betano 4.73; local: modelo 2.02 / sin contexto 1.89 / implícita Betano 1.92; visitante: modelo 2.83 / sin contexto 2.61 / implícita Betano 2.69

## Series (a favor, en contra) por partido
- Local (6): [(1, 4), (0, 2), (1, 1), (3, 1), (0, 1), (0, 3)]
- Visitante (7): [(3, 3), (2, 0), (4, 1), (1, 2), (1, 1), (4, 3), (3, 1)]
- Directos (3, [local, visitante]): [(0, 2), (2, 4), (2, 4)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 2.5 | Más | 1.19 | 3.49 | +0.99 | 3 de 6 | 5 de 7 | 2 de 3 | no | no | -0.28 |
| total | 2.5 | Menos | 4.35 | 3.49 | -0.99 | 3 de 6 | 2 de 7 | 1 de 3 | no | sí | +0.71 |
| total | 3.5 | Más | 1.44 | 3.49 | -0.01 | 2 de 6 | 4 de 7 | 2 de 3 | no | sí | -0.35 |
| total | 3.5 | Menos | 2.67 | 3.49 | +0.01 | 4 de 6 | 3 de 7 | 1 de 3 | no | sí | +0.46 |
| total | 4.5 | Más | 1.88 | 3.49 | -1.01 | 1 de 6 | 3 de 7 | 2 de 3 | no | sí | -0.44 |
| total | 4.5 | Menos | 1.87 | 3.49 | +1.01 | 5 de 6 | 4 de 7 | 1 de 3 | no | sí | +0.31 |
| total | 5.5 | Más | 2.6 | 3.49 | -2.01 | 0 de 6 | 2 de 7 | 2 de 3 | no | sí | -0.63 |
| total | 5.5 | Menos | 1.45 | 3.49 | +2.01 | 6 de 6 | 5 de 7 | 1 de 3 | SÍ | sí | +0.24 |
| total | 6.5 | Más | 3.8 | 3.49 | -3.01 | 0 de 6 | 1 de 7 | 0 de 3 | no | sí | -0.73 |
| total | 6.5 | Menos | 1.24 | 3.49 | +3.01 | 6 de 6 | 6 de 7 | 3 de 3 | SÍ | sí | +0.15 |
| local | 0.5 | Más | 1.15 | 1.2 | +0.7 | 3 de 6 | 6 de 7 | 2 de 3 | no | no | -0.22 |
| local | 0.5 | Menos | 5.1 | 1.2 | -0.7 | 3 de 6 | 1 de 7 | 1 de 3 | no | sí | +0.64 |
| local | 1.5 | Más | 1.67 | 1.2 | -0.3 | 1 de 6 | 3 de 7 | 2 de 3 | no | sí | -0.50 |
| local | 1.5 | Menos | 2.12 | 1.2 | +0.3 | 5 de 6 | 4 de 7 | 1 de 3 | no | sí | +0.49 |
| local | 2.5 | Más | 2.92 | 1.2 | -1.3 | 1 de 6 | 2 de 7 | 0 de 3 | no | sí | -0.34 |
| local | 2.5 | Menos | 1.37 | 1.2 | +1.3 | 5 de 6 | 5 de 7 | 3 de 3 | SÍ | sí | +0.06 |
| visitante | 0.5 | Más | 1.5 | 2.29 | +1.79 | 6 de 6 | 7 de 7 | 3 de 3 | SÍ | sí | +0.50 |
| visitante | 0.5 | Menos | 2.5 | 2.29 | -1.79 | 0 de 6 | 0 de 7 | 0 de 3 | no | sí | -1.00 |
| visitante | 1.5 | Más | 1.26 | 2.29 | +0.79 | 3 de 6 | 5 de 7 | 3 de 3 | no | sí | -0.23 |
| visitante | 1.5 | Menos | 3.65 | 2.29 | -0.79 | 3 de 6 | 2 de 7 | 0 de 3 | no | sí | +0.43 |
| visitante | 2.5 | Más | 1.75 | 2.29 | -0.21 | 2 de 6 | 4 de 7 | 2 de 3 | no | sí | -0.21 |
| visitante | 2.5 | Menos | 2.0 | 2.29 | +0.21 | 4 de 6 | 3 de 7 | 1 de 3 | no | sí | +0.10 |
| visitante | 3.5 | Más | 2.85 | 2.29 | -1.21 | 1 de 6 | 2 de 7 | 2 de 3 | no | sí | -0.36 |
| visitante | 3.5 | Menos | 1.39 | 2.29 | +1.21 | 5 de 6 | 5 de 7 | 1 de 3 | SÍ | sí | +0.08 |
| 1T | 1.5 | Más | 1.9 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 1.83 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 2.5 | Más | 3.3 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 2.5 | Menos | 1.3 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.2 | 1.2 / 2.29 | 3 de 6 | 7 de 7 | 6 de 6 | 6 de 7 | 2 de 3 | no | sí | -0.10 |
| 1 | No | 4.2 | 1.2 / 2.29 | 3 de 6 (<N) | 0 de 7 (<N) | 6 de 6 | 6 de 7 | 1 de 3 | no | sí | +1.10 |
| 2 | Sí | 1.98 | 1.2 / 2.29 | 1 de 6 | 5 de 7 | 3 de 6 | 3 de 7 | 2 de 3 | no | sí | -0.13 |
| 2 | No | 1.78 | 1.2 / 2.29 | 5 de 6 (<N) | 2 de 7 (<N) | 3 de 6 | 3 de 7 | 1 de 3 | no | sí | +0.48 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 1.2 vs visitante 2.29.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 3.75 | 1 de 6 | 1 de 7 | 0 de 3 | no | sí | -0.42 |
| X (igual) | 4.5 | 1 de 6 | 2 de 7 | 0 de 3 | no | sí | +0.02 |
| 2 (visitante más) | 1.65 | 4 de 6 | 4 de 7 | 3 de 3 | no | sí | +0.02 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 3 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(0, 2), (2, 4), (2, 4)]; totales [2, 6, 6]. Con n=3 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: alta; motivación local/visitante: alta / alta; necesita ganar local/visitante: False / False; árbitro: Saggi R. (sin estadísticas).
- Dudas abiertas en la ficha: ninguna
- Fuentes del contexto: Tabla calculada con los resultados de Flashscore (4 jornadas jugadas hasta el 6-oct-2026): Grupo A2 → Grecia 8 pts, Países Bajos 8, Alemania 5, Serbia 0. Choque directo por la cima del grupo.; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- total Menos 5.5 @1.45 · colchón +2.01 · L 6 de 6 · V 5 de 7
- total Menos 6.5 @1.24 · colchón +3.01 · L 6 de 6 · V 6 de 7
- local Menos 2.5 @1.37 · colchón +1.3 · L 5 de 6 · V 5 de 7
- visitante Más 0.5 @1.5 · colchón +1.79 · L 6 de 6 · V 7 de 7
- visitante Menos 3.5 @1.39 · colchón +1.21 · L 5 de 6 · V 5 de 7

## Lectura
(ver resumen del chat; cifras arriba copiadas/recalculadas de la ficha y verificadas contra `ficha.tarjetas.lineas`)
