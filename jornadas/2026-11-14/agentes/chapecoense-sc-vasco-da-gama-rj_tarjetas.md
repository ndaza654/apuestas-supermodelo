# Tarjetas · Chapecoense SC - Vasco da Gama RJ (muestra de 7; cumple >=5 de 7)

## Enfoque de mercados
Tarjetas de equipo/partido (jugadores los analiza `jugadores`). Fuente: ficha Flashscore (solo amarillas) + cuotas Betano (puntos: amarilla 1, roja 2) + modelo (registro/lineas.csv). La serie queda por debajo si hubo rojas. Sin estadistica de arbitro. 1T: sin estadistica por tiempo.

n local=6, visitante=7, directos=2. Esperado local 2.5, visitante 1.73, total 4.23.

Serie local (tarjetas propias, mas reciente primero): [3.0, 2.0, 1.0, 2.0, 3.0, 1.0]
Serie visitante: [5.0, 1.0, 6.0, 0.0, 1.0, 1.0, 2.0]
Directos [loc,vis]: [[5.0, 8.0], [0.0, 1.0]]

## Contexto
Arbitro: Pereira R. · derbi: False · importancia: normal · necesita ganar L/V: False/False · bajas: []

## Lineas (todas las de Betano)
| Ambito | Linea | Lado | Cuota | Esperado | Colchon | L | V | D | Cumple | p modelo | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1T | 1.5 | Más | 2.07 | - | - | n/d | n/d | n/d |  | 0.4315 | -0.1068 |
| 1T | 1.5 | Menos | 1.7 | - | - | n/d | n/d | n/d |  | 0.5685 | -0.0336 |
| local | 2.5 | Más | 2.2 | 2.5 | 0.0 | 2 de 6 | 3 de 7 | 1 de 2 | no | 0.4095 | -0.0992 |
| local | 2.5 | Menos | 1.62 | 2.5 | 0.0 | 4 de 6 | 4 de 7 | 1 de 2 | no | 0.5905 | -0.0433 |
| total | 1.5 | Más | 1.09 | 4.23 | 2.73 | 5 de 6 | 7 de 7 | 1 de 2 | no | 0.9014 | -0.0175 |
| total | 1.5 | Menos | 6.4 | 4.23 | -2.73 | 1 de 6 | 0 de 7 | 1 de 2 | no | 0.0986 | -0.3687 |
| total | 2.5 | Más | 1.27 | 4.23 | 1.73 | 5 de 6 | 6 de 7 | 1 de 2 | no | 0.764 | -0.0297 |
| total | 2.5 | Menos | 3.55 | 4.23 | -1.73 | 1 de 6 | 1 de 7 | 1 de 2 | no | 0.236 | -0.1622 |
| total | 3.5 | Más | 1.6 | 4.23 | 0.73 | 2 de 6 | 5 de 7 | 1 de 2 | no | 0.5921 | -0.0527 |
| total | 3.5 | Menos | 2.25 | 4.23 | -0.73 | 4 de 6 | 2 de 7 | 1 de 2 | no | 0.4079 | -0.0822 |
| total | 4.5 | Más | 2.2 | 4.23 | -0.27 | 1 de 6 | 3 de 7 | 1 de 2 | no | 0.4123 | -0.093 |
| total | 4.5 | Menos | 1.62 | 4.23 | 0.27 | 5 de 6 | 4 de 7 | 1 de 2 | no | 0.5877 | -0.0479 |
| total | 5.5 | Más | 3.15 | 4.23 | -1.27 | 0 de 6 | 3 de 7 | 1 de 2 | no | 0.2705 | -0.148 |
| total | 5.5 | Menos | 1.33 | 4.23 | 1.27 | 6 de 6 | 4 de 7 | 1 de 2 | no | 0.7295 | -0.0297 |
| total | 6.5 | Más | 4.7 | 4.23 | -2.27 | 0 de 6 | 2 de 7 | 1 de 2 | no | 0.1613 | -0.242 |
| total | 6.5 | Menos | 1.17 | 4.23 | 2.27 | 6 de 6 | 5 de 7 | 1 de 2 | no | 0.8387 | -0.0187 |
| total | 7.5 | Más | 6.9 | 4.23 | -3.27 | 0 de 6 | 2 de 7 | 1 de 2 | no | 0.0896 | -0.3817 |
| total | 7.5 | Menos | 1.08 | 4.23 | 3.27 | 6 de 6 | 5 de 7 | 1 de 2 | no | 0.9104 | -0.0168 |
| total | 8.5 | Más | 9.5 | 4.23 | -4.27 | 0 de 6 | 1 de 7 | 1 de 2 | no | 0.0491 | -0.5331 |
| total | 8.5 | Menos | 1.04 | 4.23 | 4.27 | 6 de 6 | 6 de 7 | 1 de 2 | no | 0.9509 | -0.0111 |
| visitante | 1.5 | Más | 1.67 | 1.73 | 0.23 | 2 de 6 | 3 de 7 | 1 de 2 | no | 0.5642 | -0.0577 |
| visitante | 1.5 | Menos | 2.12 | 1.73 | -0.23 | 4 de 6 | 4 de 7 | 1 de 2 | no | 0.4358 | -0.0762 |

## Ambos con N tarjetas (calculado con las series; sin cuota de Betano en ficha/CSV)
| N | Local >=N | Visitante >=N | Producto ingenuo |
|---|---|---|---|
| 1 | 6 de 6 | 6 de 7 | 0.86 |
| 2 | 4 de 6 | 3 de 7 | 0.29 |
| 3 | 2 de 6 | 2 de 7 | 0.10 |
| 4 | 0 de 6 | 2 de 7 | 0.00 |

## Mas tarjetas que
Esperado local 2.5 vs visitante 1.73 (diferencia +0.77). Promedios propios: local 2.00, visitante 2.29. La dependencia entre equipos no esta modelada en la ficha; no hay cuota en el CSV.

## Limites
Puntos Betano vs solo amarillas; sin arbitro estadistico; 1T sin estadistica; EV = p*cuota-1 informativo; colchon sin umbral.
