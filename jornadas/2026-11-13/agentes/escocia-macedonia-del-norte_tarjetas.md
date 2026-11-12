# Tarjetas de equipo/partido: Escocia - Macedonia del Norte (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Ocenas M.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=7, directos n=1 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (2.0 a favor + 1.29 que concede el visitante)/2 = **1.64**
- Visitante: (2.57 a favor + 2.29 que concede el local)/2 = **2.43**
- Total = **4.07** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 4.56 / sin contexto 4.76 / implícita Betano 4.78; local: modelo 1.73 / sin contexto 1.74 / implícita Betano 1.74; visitante: modelo 2.83 / sin contexto 3.02 / implícita Betano 3.07

## Series (a favor, en contra) por partido
- Local (7): [(2, 4), (3, 5), (3, 0), (1, 3), (1, 2), (1, 1), (3, 1)]
- Visitante (7): [(1, 0), (5, 3), (2, 1), (4, 0), (2, 0), (3, 0), (1, 5)]
- Directos (1, [local, visitante]): [(3, 5)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 4.5 | Más | 1.85 | 4.07 | -0.43 | 2 de 7 | 2 de 7 | 1 de 1 | no | sí | -0.47 |
| total | 4.5 | Menos | 1.88 | 4.07 | +0.43 | 5 de 7 | 5 de 7 | 0 de 1 | SÍ | sí | +0.34 |
| local | 1.5 | Más | 1.82 | 1.64 | +0.14 | 4 de 7 | 2 de 7 | 1 de 1 | no | sí | -0.22 |
| local | 1.5 | Menos | 1.91 | 1.64 | -0.14 | 3 de 7 | 5 de 7 | 0 de 1 | no | sí | +0.09 |
| visitante | 2.5 | Más | 1.62 | 2.43 | -0.07 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.31 |
| visitante | 2.5 | Menos | 2.2 | 2.43 | +0.07 | 4 de 7 | 4 de 7 | 0 de 1 | no | sí | +0.26 |
| 1T | 1.5 | Más | 1.88 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 1.85 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Para cada N: en cuántos de n partidos cada equipo recibió ≥ N (a favor), y cuántos partidos del rival concedieron ≥ N. Directos: en cuántos ambos recibieron ≥ N en el mismo partido. «Sí» cumple si ambos equipos ≥5 de n; «No» (el evento «algún equipo no llega a N») se marca cumple solo si AMBOS equipos tienen <N en ≥5 de n (criterio conservador, la unión sería más probable). Dependencia entre equipos no modelada.

| N | Lado | Cuota | Esperado L / V | Local ≥N (a favor) | Visitante ≥N (a favor) | Local concede ≥N | Visitante concede ≥N | Directos ambos ≥N | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sí | 1.23 | 1.64 / 2.43 | 7 de 7 | 7 de 7 | 6 de 7 | 3 de 7 | 1 de 1 | SÍ | sí | +0.23 |
| 1 | No | 3.85 | 1.64 / 2.43 | 0 de 7 (<N) | 0 de 7 (<N) | 6 de 7 | 3 de 7 | 0 de 1 | no | sí | -1.00 |
| 2 | Sí | 2.1 | 1.64 / 2.43 | 4 de 7 | 5 de 7 | 4 de 7 | 2 de 7 | 1 de 1 | no | sí | +0.35 |
| 2 | No | 1.67 | 1.64 / 2.43 | 3 de 7 (<N) | 2 de 7 (<N) | 4 de 7 | 2 de 7 | 0 de 1 | no | sí | -0.28 |

EV aprox: «Sí» p = promedio de las dos frecuencias; «No» p = la mayor de las dos frecuencias de quedar <N (cota inferior de la unión). Tosco, informativo.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 1.64 vs visitante 2.43.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 5.2 | 2 de 7 | 1 de 7 | 0 de 1 | no | sí | +0.11 |
| X (igual) | 5.0 | 1 de 7 | 0 de 7 | 0 de 1 | no | sí | -0.64 |
| 2 (visitante más) | 1.47 | 4 de 7 | 6 de 7 | 1 de 1 | no | sí | +0.05 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 1 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(3, 5)]; totales [8]. Con n=1 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: normal; motivación local/visitante: alta / baja; necesita ganar local/visitante: True / False; árbitro: Ocenas M. (sin estadísticas).
- Dudas abiertas en la ficha: ['Historial: sin casar con Betano → Gannon-Doak B.', 'Alineación probable: sin casar con Betano → Gannon-Doak B.', 'Luis Binks: Flashscore lo lista en el XI probable y también como baja; se toma como baja']
- Fuentes del contexto: Tabla calculada con los resultados de Flashscore (4 jornadas jugadas hasta el 6-oct-2026): Grupo B1 → Suiza 12, Eslovenia 7, Escocia 4, Macedonia del Norte 0 (0 goles a favor, 10 en contra). Escocia necesita ganar para seguir en la pelea por el 2.º puesto (repesca de ascenso); Macedonia ya está en el fondo.; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- total Menos 4.5 @1.88 · colchón +0.43 · L 5 de 7 · V 5 de 7
- Ambos ≥1 tarjetas Sí @1.23 (L 7 de 7, V 7 de 7)

## Lectura
Esperado total 4.07 vs línea 4.5: Menos 4.5 @1.88 cumple justo (5/7 y 5/7, colchón +0.43), línea ajustada y las rojas no contadas pueden subirla. Ambos ≥1 Sí @1.23 cumple (7/7 y 7/7, cuota apenas sobre el mínimo). «Más tarjetas que» visitante @1.47 no cumple por el lado local (4/7).
Contexto: Escocia necesita ganar, motivación del visitante baja; 3 dudas de alineación en la ficha (no afectan a tarjetas de equipo). Directos n=1.

_Cifras recalculadas desde las series de la ficha y verificadas contra `ficha.tarjetas.lineas` (coinciden las X de n y los cumple). EV = p·cuota−1 informativo._
