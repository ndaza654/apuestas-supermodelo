# Tarjetas de equipo/partido: Moldavia - Kazajistán (2026-11-13 12:00, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Colombo A.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=7, directos n=3 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (1.86 a favor + 1.57 que concede el visitante)/2 = **1.71**
- Visitante: (3.29 a favor + 1.29 que concede el local)/2 = **2.29**
- Total = **4.0** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 5.02 / sin contexto 4.71 / implícita Betano 4.71; local: modelo 2.24 / sin contexto 2.13 / implícita Betano 2.14; visitante: modelo 2.78 / sin contexto 2.58 / implícita Betano 2.62

## Series (a favor, en contra) por partido
- Local (7): [(2, 0), (0, 2), (0, 1), (1, 2), (4, 2), (3, 0), (3, 2)]
- Visitante (7): [(3, 5), (2, 0), (2, 2), (2, 0), (3, 0), (5, 3), (6, 1)]
- Directos (3, [local, visitante]): [(0, 2), (5, 3), (1, 2)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 4.5 | Más | 1.9 | 4.0 | -0.5 | 2 de 7 | 3 de 7 | 1 de 3 | no | sí | -0.32 |
| total | 4.5 | Menos | 1.85 | 4.0 | +0.5 | 5 de 7 | 4 de 7 | 2 de 3 | no | sí | +0.19 |
| local | 1.5 | Más | 1.53 | 1.71 | +0.21 | 4 de 7 | 3 de 7 | 1 de 3 | no | sí | -0.23 |
| local | 1.5 | Menos | 2.4 | 1.71 | -0.21 | 3 de 7 | 4 de 7 | 2 de 3 | no | sí | +0.20 |
| visitante | 2.5 | Más | 1.93 | 2.29 | -0.21 | 0 de 7 | 4 de 7 | 1 de 3 | no | sí | -0.45 |
| visitante | 2.5 | Menos | 1.8 | 2.29 | +0.21 | 7 de 7 | 3 de 7 | 2 de 3 | no | sí | +0.29 |
| 1T | 1.5 | Más | 1.91 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 1.83 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.19 | 1.71 / 2.29 | 5 de 7 | 7 de 7 | 5 de 7 | 4 de 7 | 2 de 3 | SÍ | no | +0.02 |
| 1 | No | 4.4 | 1.71 / 2.29 | 2 de 7 (<N) | 0 de 7 (<N) | 5 de 7 | 4 de 7 | 1 de 3 | no | sí | +0.26 |
| 2 | Sí | 1.91 | 1.71 / 2.29 | 4 de 7 | 7 de 7 | 4 de 7 | 3 de 7 | 1 de 3 | no | sí | +0.50 |
| 2 | No | 1.83 | 1.71 / 2.29 | 3 de 7 (<N) | 0 de 7 (<N) | 4 de 7 | 3 de 7 | 2 de 3 | no | sí | -0.22 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 1.71 vs visitante 2.29.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 3.2 | 4 de 7 | 1 de 7 | 1 de 3 | no | sí | +0.14 |
| X (igual) | 4.15 | 0 de 7 | 1 de 7 | 0 de 3 | no | sí | -0.70 |
| 2 (visitante más) | 1.9 | 3 de 7 | 5 de 7 | 2 de 3 | no | sí | +0.09 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 3 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(0, 2), (5, 3), (1, 2)]; totales [2, 8, 3]. Con n=3 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: alta; motivación local/visitante: alta / alta; necesita ganar local/visitante: True / True; árbitro: Colombo A. (sin estadísticas).
- Dudas abiertas en la ficha: ninguna
- Fuentes del contexto: Tabla calculada con los resultados de Flashscore (4 jornadas jugadas hasta el 6-oct-2026): Grupo C3 → Eslovaquia 10, Islas Feroe 4, Moldavia 4, Kazajistán 2. Duelo directo por el 2.º puesto (repesca de ascenso).; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- Ninguna.

## Lectura
Ninguna línea cumple con cuota ≥1.20. Esperado total 4.0 vs 4.5: Menos @1.85 con L 5/7 pero V 4/7. Visitante Menos 2.5: Moldavia concede ≤2 en 7/7 pero Kazajistán a favor solo 3/7. Ambos ≥1 Sí @1.19 cumple (5/7 y 7/7) pero cuota < 1.20. Directos n=3 sin conclusión.
Ambos necesitan ganar, importancia alta. Partido a las 12:00 Bogotá.

_Cifras recalculadas desde las series de la ficha y verificadas contra `ficha.tarjetas.lineas` (coinciden las X de n y los cumple). EV = p·cuota−1 informativo._
