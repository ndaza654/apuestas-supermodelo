# Tarjetas de equipo/partido: Eslovaquia - Islas Feroé (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Al-Emara M.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=7, directos n=1 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (1.0 a favor + 0.71 que concede el visitante)/2 = **0.86**
- Visitante: (1.86 a favor + 2.57 que concede el local)/2 = **2.21**
- Total = **3.07** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 4.29 / sin contexto 4.19 / implícita Betano 4.2; local: modelo 1.64 / sin contexto 1.58 / implícita Betano 1.61; visitante: modelo 2.65 / sin contexto 2.6 / implícita Betano 2.62

## Series (a favor, en contra) por partido
- Local (7): [(0, 2), (0, 3), (2, 2), (2, 1), (2, 3), (0, 1), (1, 6)]
- Visitante (7): [(5, 3), (3, 0), (1, 0), (0, 2), (1, 0), (1, 0), (2, 0)]
- Directos (1, [local, visitante]): [(0, 3)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 3.5 | Más | 1.62 | 3.07 | -0.43 | 3 de 7 | 1 de 7 | 0 de 1 | no | sí | -0.54 |
| total | 3.5 | Menos | 2.2 | 3.07 | +0.43 | 4 de 7 | 6 de 7 | 1 de 1 | no | sí | +0.57 |
| local | 1.5 | Más | 1.95 | 0.86 | -0.64 | 3 de 7 | 2 de 7 | 0 de 1 | no | sí | -0.30 |
| local | 1.5 | Menos | 1.78 | 0.86 | +0.64 | 4 de 7 | 5 de 7 | 1 de 1 | no | sí | +0.14 |
| visitante | 2.5 | Más | 1.93 | 2.21 | -0.29 | 3 de 7 | 2 de 7 | 1 de 1 | no | sí | -0.31 |
| visitante | 2.5 | Menos | 1.8 | 2.21 | +0.29 | 4 de 7 | 5 de 7 | 0 de 1 | no | sí | +0.16 |
| 1T | 1.5 | Más | 2.12 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 1.67 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.29 | 0.86 / 2.21 | 4 de 7 | 6 de 7 | 7 de 7 | 2 de 7 | 0 de 1 | no | sí | -0.08 |
| 1 | No | 3.4 | 0.86 / 2.21 | 3 de 7 (<N) | 1 de 7 (<N) | 7 de 7 | 2 de 7 | 1 de 1 | no | sí | +0.46 |
| 2 | Sí | 2.4 | 0.86 / 2.21 | 3 de 7 | 3 de 7 | 5 de 7 | 2 de 7 | 0 de 1 | no | sí | +0.03 |
| 2 | No | 1.53 | 0.86 / 2.21 | 4 de 7 (<N) | 4 de 7 (<N) | 5 de 7 | 2 de 7 | 1 de 1 | no | sí | -0.13 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 0.86 vs visitante 2.21.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 4.6 | 1 de 7 | 1 de 7 | 0 de 1 | no | sí | -0.34 |
| X (igual) | 4.4 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | -0.69 |
| 2 (visitante más) | 1.57 | 5 de 7 | 6 de 7 | 1 de 1 | SÍ | sí | +0.23 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 1 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(0, 3)]; totales [3]. Con n=1 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: normal; motivación local/visitante: alta / normal; necesita ganar local/visitante: False / True; árbitro: Al-Emara M. (sin estadísticas).
- Dudas abiertas en la ficha: ninguna
- Fuentes del contexto: Tabla calculada con los resultados de Flashscore (4 jornadas jugadas hasta el 6-oct-2026): Grupo C3 → Eslovaquia 10 (líder), Islas Feroe 4, Moldavia 4, Kazajistán 2. Eslovaquia casi ascendida; Feroe pelea el 2.º puesto.; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- Más tarjetas que: 2 (visitante más) @1.57 (L 5 de 7, V 6 de 7)

## Lectura
Esperado total 3.07 vs línea 3.5: Menos 3.5 @2.2 queda en L 4/7 (no cumple) pese a V 6/7. Por equipo, ninguna línea cumple. Cumple «más tarjetas que» visitante (Feroe) @1.57 (L 5/7, V 6/7); es de baja confianza porque la serie del local muestra pocas tarjetas propias (0 amarillas en 3 de 7) y la dependencia entre equipos no está modelada.
Eslovaquia no necesita ganar según el contexto; Feroe sí. Directos n=1.

_Cifras recalculadas desde las series de la ficha y verificadas contra `ficha.tarjetas.lineas` (coinciden las X de n y los cumple). EV = p·cuota−1 informativo._
