# Tarjetas de equipo/partido: Liechtenstein - Azerbaiyán (2026-11-13 14:45, hora Bogotá)

## Enfoque de mercados
Tarjetas de equipo y partido (total, por equipo, 1T), «ambos con N tarjetas» y «más tarjetas que». Tarjetas de jugadores: no se analizan aquí (agente `jugadores`). Solo se analizan las líneas que Betano ofrece en este partido.

## Límites (leer primero)
- Betano cuenta en puntos (amarilla = 1, roja = 2); Flashscore solo trae amarillas. Las series quedan POR DEBAJO de los puntos reales si hubo rojas; en líneas ajustadas (colchón cercano a 0 o conteos 4-5 de 7) puede cambiar el resultado.
- Árbitro: **Tohver K.** (solo el nombre; no hay estadísticas del árbitro, no se inventa su promedio).
- Las líneas de 1T no tienen estadística por tiempo en la muestra: se listan con su cuota, sin regularidad ni esperado.
- Muestra: local n=7, visitante n=7, directos n=1 (series de la ficha, partido completo; fuente Flashscore). La dependencia entre equipos (si un equipo recibe más, el otro tiende a recibir menos/más, el árbitro, el marcador) NO está modelada en la ficha.
- Regla de cumple: ≥ 5 de n en AMBOS equipos (n mínimo 5). «Cumplen» en el resumen = cumple y cuota ≥ 1.20.

## Criterio 2: esperado vs línea
- Local: (1.86 a favor + 2.14 que concede el visitante)/2 = **2.0**
- Visitante: (2.43 a favor + 2.0 que concede el local)/2 = **2.21**
- Total = **4.21** (fuente: ficha, `tarjetas.esperado`). Colchón informativo, sin umbral.
- Referencia (solo referencia, no decide): medias de tarjetas del informe del modelo = total: modelo 5.39 / sin contexto 5.08 / implícita Betano 5.01; local: modelo 2.97 / sin contexto 2.79 / implícita Betano 2.77; visitante: modelo 2.42 / sin contexto 2.29 / implícita Betano 2.26

## Series (a favor, en contra) por partido
- Local (7): [(3, 2), (1, 1), (3, 5), (1, 1), (1, 0), (2, 3), (2, 2)]
- Visitante (7): [(3, 5), (2, 3), (3, 1), (0, 4), (3, 0), (2, 0), (4, 2)]
- Directos (1, [local, visitante]): [(3, 2)]

## Líneas de Betano (todas, sin excluir por colchón)
Formato regularidad: L = local, V = visitante, D = directos (informativo, no cuenta para el cumple). EV aprox = p·cuota−1 con p = promedio de las dos frecuencias L y V (muy tosco: n pequeño, sin dependencia); informativo, no decide.

| Ámbito | Línea | Lado | Cuota | Esperado | Colchón | L | V | D | Cumple | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|---|---|---|---|
| total | 4.5 | Más | 1.72 | 4.21 | -0.29 | 3 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.26 |
| total | 4.5 | Menos | 2.0 | 4.21 | +0.29 | 4 de 7 | 4 de 7 | 0 de 1 | no | sí | +0.14 |
| local | 2.5 | Más | 1.8 | 2.0 | -0.5 | 2 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.36 |
| local | 2.5 | Menos | 1.91 | 2.0 | +0.5 | 5 de 7 | 4 de 7 | 0 de 1 | no | sí | +0.23 |
| visitante | 2.5 | Más | 2.3 | 2.21 | -0.29 | 2 de 7 | 4 de 7 | 0 de 1 | no | sí | -0.01 |
| visitante | 2.5 | Menos | 1.55 | 2.21 | +0.29 | 5 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.11 |
| 1T | 1.5 | Más | 1.8 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |
| 1T | 1.5 | Menos | 1.91 | n/d | n/d | n/d | n/d | n/d | sin estadística por tiempo | sí | n/d |

Nota de lectura de L/V: en el ámbito «total» L y V son la suma de tarjetas del partido en cada serie; en «local» L = tarjetas a favor del local y V = tarjetas que concedió el visitante; en «visitante» L = tarjetas que concedió el local y V = a favor del visitante.

## Criterio 5: «Ambos con N tarjetas»
Betano no ofrece «ambos con N tarjetas» en este partido.

## Criterio 5: «Más tarjetas que» (1 = local, X = empate, 2 = visitante)
Se compara, en la serie de cada equipo, partidos con más tarjetas propias que el rival de ese partido (los rivales de cada serie son distintos; la dependencia no está modelada). Esperado: local 2.0 vs visitante 2.21.

| Opción | Cuota | Local en su serie | Visitante en su serie | Directos | Cumple (ambos ≥5) | Cuota ≥1.20 | EV aprox |
|---|---|---|---|---|---|---|---|
| 1 (local más) | 1.87 | 2 de 7 | 3 de 7 | 1 de 1 | no | sí | -0.33 |
| X (igual) | 4.2 | 3 de 7 | 0 de 7 | 0 de 1 | no | sí | -0.10 |
| 2 (visitante más) | 3.1 | 2 de 7 | 4 de 7 | 0 de 1 | no | sí | +0.33 |

Lectura de columnas: para «1», Local = partidos del local con más tarjetas que su rival y Visitante = partidos del visitante con menos que su rival; para «X», partidos empatados en cada serie; para «2», Local = partidos del local con menos y Visitante = partidos del visitante con más. Betano cuenta puntos (rojas = 2) y la serie solo trae amarillas.

## Criterio 3: directos
n = 1 directo(s) (Flashscore, `ficha.tarjetas.series.directos`, [local, visitante]): [(3, 2)]; totales [5]. Con n=1 es solo referencia (n < 5, no concluyente). El criterio de directos no entra en el cumple.

## Criterio 4: contexto (matiz, sin inventar)
- Derbi: no; importancia: alta; motivación local/visitante: normal / alta; necesita ganar local/visitante: True / False; árbitro: Tohver K. (sin estadísticas).
- Dudas abiertas en la ficha: ninguna
- Fuentes del contexto: Grupo D2 de 3 equipos, calculado con resultados de Flashscore: Azerbaiyán 5 pts (3 jugados), Lituania 4 (3), Liechtenstein 1 (2). El ganador del grupo asciende.; Formato Liga de Naciones 2026-27 (Wikipedia, tablas desactualizadas; solo se usaron las reglas de ascenso/descenso)
- No hay en la ficha datos de ritmo, marcador esperado ni cierre del partido que respalden un matiz cuantitativo sobre tarjetas; no se aplica ajuste.

## Líneas que cumplen (≥5 de n en ambos equipos y cuota ≥1.20)
- Ninguna.

## Lectura
(ver resumen del chat; cifras arriba copiadas/recalculadas de la ficha y verificadas contra `ficha.tarjetas.lineas`)
