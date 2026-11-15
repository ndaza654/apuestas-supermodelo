# Tarjetas · Suecia - Bosnia y Herzegovina (muestra de 7; cumple >=5 de 7)

## Enfoque de mercados
Tarjetas de equipo/partido (jugadores los analiza `jugadores`). Fuente: ficha Flashscore (solo amarillas) + cuotas Betano (puntos: amarilla 1, roja 2) + modelo (registro/lineas.csv). La serie queda por debajo si hubo rojas. Sin estadistica de arbitro. 1T: sin estadistica por tiempo.

n local=5, visitante=6, directos=0. Esperado local 1.63, visitante 2.63, total 4.27.

Serie local (tarjetas propias, mas reciente primero): [2.0, 1.0, 0.0, 2.0, 3.0]
Serie visitante: [3.0, 2.0, 5.0, 1.0, 1.0, 4.0]
Directos [loc,vis]: []

## Contexto
Arbitro: Sozza S. · derbi: False · importancia: normal · necesita ganar L/V: False/False · bajas: []

## Lineas (todas las de Betano)
| Ambito | Linea | Lado | Cuota | Esperado | Colchon | L | V | D | Cumple | p modelo | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1T | 1.5 | Más | 2.1 | - | - | n/d | n/d | n/d |  | 0.4236 | -0.1104 |
| 1T | 1.5 | Menos | 1.67 | - | - | n/d | n/d | n/d |  | 0.5764 | -0.0375 |
| local | 1.5 | Más | 1.95 | 1.63 | 0.13 | 3 de 5 | 3 de 6 | n/d | no | 0.4699 | -0.0838 |
| local | 1.5 | Menos | 1.8 | 1.63 | -0.13 | 2 de 5 | 3 de 6 | n/d | no | 0.5301 | -0.0458 |
| total | 3.5 | Más | 1.62 | 4.27 | 0.77 | 3 de 5 | 3 de 6 | n/d | no | 0.5811 | -0.0587 |
| total | 3.5 | Menos | 2.22 | 4.27 | -0.77 | 2 de 5 | 3 de 6 | n/d | no | 0.4189 | -0.07 |
| visitante | 2.5 | Más | 1.93 | 2.63 | 0.13 | 3 de 5 | 3 de 6 | n/d | no | 0.4718 | -0.0895 |
| visitante | 2.5 | Menos | 1.82 | 2.63 | -0.13 | 2 de 5 | 3 de 6 | n/d | no | 0.5282 | -0.0386 |

## Ambos con N tarjetas (calculado con las series; sin cuota de Betano en ficha/CSV)
| N | Local >=N | Visitante >=N | Producto ingenuo |
|---|---|---|---|
| 1 | 4 de 5 | 6 de 6 | 0.80 |
| 2 | 3 de 5 | 4 de 6 | 0.40 |
| 3 | 1 de 5 | 3 de 6 | 0.10 |
| 4 | 0 de 5 | 2 de 6 | 0.00 |

## Mas tarjetas que
Esperado local 1.63 vs visitante 2.63 (diferencia -1.00). Promedios propios: local 1.60, visitante 2.67. La dependencia entre equipos no esta modelada en la ficha; no hay cuota en el CSV.

## Limites
Puntos Betano vs solo amarillas; sin arbitro estadistico; 1T sin estadistica; EV = p*cuota-1 informativo; colchon sin umbral.
