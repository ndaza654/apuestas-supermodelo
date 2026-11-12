# Tarjetas de equipo/partido: Andorra - Gibraltar (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Hennessy R.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=6, directos n=1 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (3.43 a favor + 1.83 que concede el visitante)/2 = **2.63**
- Visitante: (2.17 a favor + 1.57 que concede el local)/2 = **1.87**
- Total = **4.5** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 6.28 / sin contexto 5.99 / implícita Betano 6.02; local: modelo 3.05 / sin contexto 2.9 / implícita Betano 2.93; visitante: modelo 3.23 / sin contexto 3.09 / implícita Betano 3.13

## Series (a favor, en contra) por partido
- Local (7): [(3, 2), (3, 2), (5, 2), (3, 2), (4, 1), (5, 1), (1, 1)]
- Visitante (6): [(1, 3), (2, 3), (5, 2), (2, 2), (1, 0), (2, 1)]
- Directos (1, [local, visitante]): [(3, 2)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 5.5 | Más | 1.75 | 4.5 | -1.0 | 2 de 7 | 1 de 6 | 0 de 1 | no | sí | -0.60 |
| total | 5.5 | Menos | 2.0 | 4.5 | +1.0 | 5 de 7 | 5 de 6 | 1 de 1 | SÍ | sí | +0.55 |
| local | 2.5 | Más | 1.7 | 2.63 | +0.13 | 6 de 7 | 2 de 6 | 1 de 1 | no | sí | +0.01 |
| local | 2.5 | Menos | 2.07 | 2.63 | -0.13 | 1 de 7 | 4 de 6 | 0 de 1 | no | sí | -0.16 |
| visitante | 2.5 | Más | 1.6 | 1.87 | -0.63 | 0 de 7 | 1 de 6 | 0 de 1 | no | sí | -0.87 |
| visitante | 2.5 | Menos | 2.27 | 1.87 | +0.63 | 7 de 7 | 5 de 6 | 1 de 1 | SÍ | sí | +1.08 |
| 1T | 1.5 | Más | 1.57 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 2.3 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.08 | 2.63 / 1.87 | 7 de 7 | 6 de 6 | 7 de 7 | 5 de 6 | 1 de 1 | SÍ | no | +0.08 |
| 1 | No | 6.8 | 2.63 / 1.87 | 0 de 7 (<N) | 0 de 6 (<N) | 7 de 7 | 5 de 6 | 0 de 1 | no | sí | -1.00 |
| 2 | Sí | 1.44 | 2.63 / 1.87 | 6 de 7 | 4 de 6 | 4 de 7 | 4 de 6 | 1 de 1 | no | sí | +0.10 |
| 2 | No | 2.65 | 2.63 / 1.87 | 1 de 7 (<N) | 2 de 6 (<N) | 4 de 7 | 4 de 6 | 0 de 1 | no | sí | -0.12 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 2.63 vs visitante 1.87.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 2.57 | 6 de 7 | 2 de 6 | 1 de 1 | no | sí | +0.53 |
| X (igual) | 4.55 | 1 de 7 | 1 de 6 | 0 de 1 | no | sí | -0.30 |
| 2 (visitante más) | 2.1 | 0 de 7 | 3 de 6 | 0 de 1 | no | sí | -0.47 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 1 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(3, 2)]; totales [5]. Con n=1 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: alta; motivación local/visitante: alta / alta; necesita ganar local/visitante: True / True; árbitro: Hennessy R. (sin estadísticas).
- Dudas abiertas en la ficha: ninguna
- Fuentes del contexto: Grupo D1 de 3 equipos, calculado con resultados de Flashscore: Malta 7 pts (3 jugados), Gibraltar 2 (2 jugados), Andorra 1 (3 jugados). Se juega el 2.º puesto (repesca de ascenso).; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- total Menos 5.5 @2.0 · colchón +1.0 · L 5 de 7 · V 5 de 6
- visitante Menos 2.5 @2.27 · colchón +0.63 · L 7 de 7 · V 5 de 6

## Lectura
(ver resumen del chat; cifras arriba copiadas/recalculadas de la ficha y verificadas contra `ficha.tarjetas.lineas`)
