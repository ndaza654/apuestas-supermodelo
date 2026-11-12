# Tarjetas de equipo/partido: Eslovenia - Suiza (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Vergoote J.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=7, directos n=3 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (2.86 a favor + 2.86 que concede el visitante)/2 = **2.86**
- Visitante: (1.14 a favor + 1.29 que concede el local)/2 = **1.21**
- Total = **4.07** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 2.86 / sin contexto 2.75 / implícita Betano 4.0; local: modelo 1.63 / sin contexto 1.57 / implícita Betano 1.54; visitante: modelo 1.23 / sin contexto 1.18 / implícita Betano 1.15

## Series (a favor, en contra) por partido
- Local (7): [(4, 2), (5, 1), (1, 2), (3, 1), (1, 2), (5, 1), (1, 0)]
- Visitante (7): [(0, 1), (1, 5), (0, 3), (0, 4), (4, 3), (3, 2), (0, 2)]
- Directos (3, [local, visitante]): [(5, 1), (1, 0), (2, 0)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 3.5 | Más | 1.72 | 4.07 | +0.57 | 4 de 7 | 4 de 7 | 1 de 3 | no | sí | -0.02 |
| total | 3.5 | Menos | 2.05 | 4.07 | -0.57 | 3 de 7 | 3 de 7 | 2 de 3 | no | sí | -0.12 |
| local | 0.5 | Más | 1.67 | 2.86 | +2.36 | 7 de 7 | 7 de 7 | 3 de 3 | SÍ | sí | +0.67 |
| local | 0.5 | Menos | 2.12 | 2.86 | -2.36 | 0 de 7 | 0 de 7 | 0 de 3 | no | sí | -1.00 |
| local | 1.5 | Más | 2.12 | 2.86 | +1.36 | 4 de 7 | 6 de 7 | 2 de 3 | no | sí | +0.51 |
| local | 1.5 | Menos | 1.67 | 2.86 | -1.36 | 3 de 7 | 1 de 7 | 1 de 3 | no | sí | -0.52 |
| local | 2.5 | Más | 2.27 | 2.86 | +0.36 | 4 de 7 | 4 de 7 | 1 de 3 | no | sí | +0.30 |
| local | 2.5 | Menos | 1.6 | 2.86 | -0.36 | 3 de 7 | 3 de 7 | 2 de 3 | no | sí | -0.31 |
| visitante | 0.5 | Más | 2.02 | 1.21 | +0.71 | 6 de 7 | 3 de 7 | 1 de 3 | no | sí | +0.30 |
| visitante | 0.5 | Menos | 1.75 | 1.21 | -0.71 | 1 de 7 | 4 de 7 | 2 de 3 | no | sí | -0.38 |
| visitante | 1.5 | Más | 1.85 | 1.21 | -0.29 | 3 de 7 | 2 de 7 | 0 de 3 | no | sí | -0.34 |
| visitante | 1.5 | Menos | 1.9 | 1.21 | +0.29 | 4 de 7 | 5 de 7 | 3 de 3 | no | sí | +0.22 |
| 1T | 1.5 | Más | 2.22 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 1.62 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.29 | 2.86 / 1.21 | 7 de 7 | 3 de 7 | 6 de 7 | 7 de 7 | 1 de 3 | no | sí | -0.08 |
| 1 | No | 3.35 | 2.86 / 1.21 | 0 de 7 (<N) | 4 de 7 (<N) | 6 de 7 | 7 de 7 | 2 de 3 | no | sí | +0.91 |
| 2 | Sí | 2.4 | 2.86 / 1.21 | 4 de 7 | 2 de 7 | 3 de 7 | 6 de 7 | 0 de 3 | no | sí | +0.03 |
| 2 | No | 1.53 | 2.86 / 1.21 | 3 de 7 (<N) | 5 de 7 (<N) | 3 de 7 | 6 de 7 | 3 de 3 | no | sí | +0.09 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 2.86 vs visitante 1.21.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 1.82 | 5 de 7 | 5 de 7 | 3 de 3 | SÍ | sí | +0.30 |
| X (igual) | 3.9 | 0 de 7 | 0 de 7 | 0 de 3 | no | sí | -1.00 |
| 2 (visitante más) | 3.6 | 2 de 7 | 2 de 7 | 0 de 3 | no | sí | +0.03 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 3 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(5, 1), (1, 0), (2, 0)]; totales [6, 1, 2]. Con n=3 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: alta; motivación local/visitante: alta / alta; necesita ganar local/visitante: True / False; árbitro: Vergoote J. (sin estadísticas).
- Dudas abiertas en la ficha: ['Historial: sin casar con Betano → Gnezda Cerin A.', 'Alineación probable: sin casar con Betano → Gnezda Cerin A.']
- Fuentes del contexto: Tabla calculada con los resultados de Flashscore (4 jornadas jugadas hasta el 6-oct-2026): Grupo B1 → Suiza 12 (4 de 4), Eslovenia 7, Escocia 4, Macedonia del Norte 0. Suiza lidera con 11-1 de gol; Eslovenia pelea el 2.º puesto.; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- local Más 0.5 @1.67 · colchón +2.36 · L 7 de 7 · V 7 de 7
- Más tarjetas que: 1 (local más) @1.82 (L 5 de 7, V 5 de 7)

## Lectura
(ver resumen del chat; cifras arriba copiadas/recalculadas de la ficha y verificadas contra `ficha.tarjetas.lineas`)
