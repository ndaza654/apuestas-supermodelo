# Tarjetas · Kosovo - Israel (muestra de 7; cumple >=5 de 7)

## Enfoque de mercados
Tarjetas de equipo/partido (jugadores los analiza `jugadores`). Fuente: ficha Flashscore (solo amarillas) + cuotas Betano (puntos: amarilla 1, roja 2) + modelo (registro/lineas.csv). La serie queda por debajo si hubo rojas. Sin estadistica de arbitro. 1T: sin estadistica por tiempo.

n local=6, visitante=6, directos=2. Esperado local 1.92, visitante 2.08, total 4.0.

Serie local (tarjetas propias, mas reciente primero): [1.0, 2.0, 0.0, 3.0, 3.0, 2.0]
Serie visitante: [3.0, 1.0, 6.0, 2.0, 1.0, 1.0]
Directos [loc,vis]: [[3.0, 5.0], [2.0, 4.0]]

## Contexto
Arbitro: Kruzliak I. · derbi: False · importancia: normal · necesita ganar L/V: False/False · bajas: []

## Lineas (todas las de Betano)
| Ambito | Linea | Lado | Cuota | Esperado | Colchon | L | V | D | Cumple | p modelo | EV |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1T | 1.5 | Más | 2.07 | - | - | n/d | n/d | n/d |  | 0.4268 | -0.1165 |
| 1T | 1.5 | Menos | 1.7 | - | - | n/d | n/d | n/d |  | 0.5732 | -0.0256 |
| local | 1.5 | Más | 1.7 | 1.92 | 0.42 | 4 de 6 | 4 de 6 | 2 de 2 | no | 0.5504 | -0.0643 |
| local | 1.5 | Menos | 2.07 | 1.92 | -0.42 | 2 de 6 | 2 de 6 | 0 de 2 | no | 0.4496 | -0.0694 |
| total | 4.5 | Más | 2.2 | 4.0 | -0.5 | 2 de 6 | 2 de 6 | 2 de 2 | no | 0.4132 | -0.0909 |
| total | 4.5 | Menos | 1.62 | 4.0 | 0.5 | 4 de 6 | 4 de 6 | 0 de 2 | no | 0.5868 | -0.0494 |
| visitante | 2.5 | Más | 2.15 | 2.08 | -0.42 | 1 de 6 | 2 de 6 | 2 de 2 | no | 0.424 | -0.0884 |
| visitante | 2.5 | Menos | 1.65 | 2.08 | 0.42 | 5 de 6 | 4 de 6 | 0 de 2 | no | 0.576 | -0.0496 |

## Ambos con N tarjetas (calculado con las series; sin cuota de Betano en ficha/CSV)
| N | Local >=N | Visitante >=N | Producto ingenuo |
|---|---|---|---|
| 1 | 5 de 6 | 6 de 6 | 0.83 |
| 2 | 4 de 6 | 3 de 6 | 0.33 |
| 3 | 2 de 6 | 2 de 6 | 0.11 |
| 4 | 0 de 6 | 1 de 6 | 0.00 |

## Mas tarjetas que
Esperado local 1.92 vs visitante 2.08 (diferencia -0.16). Promedios propios: local 1.83, visitante 2.33. La dependencia entre equipos no esta modelada en la ficha; no hay cuota en el CSV.

## Limites
Puntos Betano vs solo amarillas; sin arbitro estadistico; 1T sin estadistica; EV = p*cuota-1 informativo; colchon sin umbral.
