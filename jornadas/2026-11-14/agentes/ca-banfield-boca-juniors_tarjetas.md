# Tarjetas · CA Banfield - Boca Juniors (muestra de 7; cumple >=5 de 7)

## Enfoque de mercados
Tarjetas de equipo/partido (jugadores los analiza `jugadores`). Fuente: ficha Flashscore (solo amarillas) + cuotas Betano (puntos: amarilla 1, roja 2) + modelo (registro/lineas.csv). La serie queda por debajo si hubo rojas. Sin estadistica de arbitro. 1T: sin estadistica por tiempo.

n local=7, visitante=7, directos=5. Esperado local 2.93, visitante 2.36, total 5.29.

Serie local (tarjetas propias, mas reciente primero): [2.0, 0.0, 4.0, 1.0, 3.0, 2.0, 2.0]
Serie visitante: [1.0, 7.0, 4.0, 2.0, 1.0, 1.0, 3.0]
Directos [loc,vis]: [[0.0, 1.0], [0.0, 5.0], [4.0, 2.0], [3.0, 2.0], [2.0, 3.0]]

## Contexto
Arbitro: sin publicar · derbi: False · importancia: normal · necesita ganar L/V: False/False · bajas: []

## Lineas (todas las de Betano)
| Ambito | Linea | Lado | Cuota | Esperado | Colchon | L | V | D | Cumple | p modelo | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1T | 1.5 | Más | 1.6 | - | - | n/d | n/d | n/d |  | 0.5831 | -0.067 |
| 1T | 1.5 | Menos | 2.25 | - | - | n/d | n/d | n/d |  | 0.4169 | -0.0621 |
| local | 3.5 | Más | 2.22 | 2.93 | -0.57 | 1 de 7 | 4 de 7 | 1 de 5 | no | 0.4106 | -0.0884 |
| local | 3.5 | Menos | 1.62 | 2.93 | 0.57 | 6 de 7 | 3 de 7 | 4 de 5 | no | 0.5894 | -0.0452 |
| total | 5.5 | Más | 1.82 | 5.29 | -0.21 | 1 de 7 | 5 de 7 | 1 de 5 | no | 0.5149 | -0.0629 |
| total | 5.5 | Menos | 1.93 | 5.29 | 0.21 | 6 de 7 | 2 de 7 | 4 de 5 | no | 0.4851 | -0.0638 |
| visitante | 2.5 | Más | 1.95 | 2.36 | -0.14 | 3 de 7 | 3 de 7 | 2 de 5 | no | 0.4735 | -0.0766 |
| visitante | 2.5 | Menos | 1.8 | 2.36 | 0.14 | 4 de 7 | 4 de 7 | 3 de 5 | no | 0.5265 | -0.0524 |

## Ambos con N tarjetas (calculado con las series; sin cuota de Betano en ficha/CSV)
| N | Local >=N | Visitante >=N | Producto ingenuo |
|---|---|---|---|
| 1 | 6 de 7 | 7 de 7 | 0.86 |
| 2 | 5 de 7 | 4 de 7 | 0.41 |
| 3 | 2 de 7 | 3 de 7 | 0.12 |
| 4 | 1 de 7 | 2 de 7 | 0.04 |

## Mas tarjetas que
Esperado local 2.93 vs visitante 2.36 (diferencia +0.57). Promedios propios: local 2.00, visitante 2.71. La dependencia entre equipos no esta modelada en la ficha; no hay cuota en el CSV.

## Limites
Puntos Betano vs solo amarillas; sin arbitro estadistico; 1T sin estadistica; EV = p*cuota-1 informativo; colchon sin umbral.
