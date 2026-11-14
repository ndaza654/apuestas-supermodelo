# Combinadas de la jornada 2026-11-14 (agente combinadas)

Límites: cuotas de Betano de la hoja (precio techo = producto de cuotas, no cupón real). Muestra de 7, cumple >=5 de 7. Reglas de la auditoría 13-nov: máx. 2 patas, cada pata >=70 % (p_modelo) y cumple ficha; la conjunta del mismo partido sale de la simulación (`combos.evaluar`, p_ajust) y se recorta 17,5 % relativo; entre partidos = producto (sin simulación). No evalué jugadores (sin alineaciones en la hoja de líneas) ni patas sin cumple. Alertas del modelo (simulación a 16-24 pts del mercado) en Suecia-Bosnia, Chapecoense-Vasco, Noruega-Gales y Portugal-Dinamarca: sus p conjuntas no son fiables.

## Conclusión: NINGUNA combinada cumple (todas EV < 0)
Solo 11 líneas pasan (cumple + p>=70 % + cuota>=1.10) y son de cuota 1.10-1.39: combinadas de ellas pagan 1.3-1.8 con p recortada 47-66 %. Los builders del modelo (3 patas, p~60 %) incumplen la regla de 2 patas y de >=70 % por pata, y quedan descartados.

## Mismo partido (p de simulación, recorte 17,5 %). «Real hasta hoy» combinadas mismo partido 31 %, 2 patas 33 %
| Partido | Patas | Cuota (techo) | p sim | p ajust | p recortada | EV | p_stress | Pata frágil |
|---|---|---|---|---|---|---|---|---|
| Japón-Brasil | Goles Menos 4.5 (1.20) + Brasil Menos 3.5 (1.10) | 1.32 | 0.803 | 0.797 | 0.657 | -13 % | 0.748 | Goles Menos 4.5 |
| Mallorca-Córdoba | Córners Más 6.5 (1.10) + Goles Mallorca Menos 3.5 (1.10) | 1.21 | 0.785 | 0.789 | 0.651 | -21 % | 0.744 | Córners Más 6.5 |
| Mallorca-Córdoba | Córners Más 7.5 (1.19) + Goles Mallorca Menos 3.5 | 1.31 | 0.712 | 0.719 | 0.593 | -22 % | 0.674 | Córners Más 7.5 |
| Noruega-Gales | Córners Más 5.5 (1.13) + Gales córners Más 1.5 (1.19) | 1.34 | 0.710 | 0.723 | 0.596 | -20 % | 0.677 | Gales Más 1.5 |
| Noruega-Gales | Córners Más 5.5 + Noruega Menos 4.5 (1.15) | 1.30 | 0.733 | 0.735 | 0.606 | -21 % | 0.691 | Córners Más 5.5 |
| Noruega-Gales | Córners Más 5.5 + Noruega Menos 3.5 (1.39) | 1.57 | 0.603 | 0.608 | 0.502 | -21 % | 0.566 | Noruega Menos 3.5 |

Todas son cuota<1.50 (salvo la última): «protección», no valor. La receta «córners Más + goles Menos» aparece en Mallorca y Noruega: como mucho una de ellas en el día.

## Entre partidos, 2 patas (producto de p individuales, sin recorte; dependencia no simulada)
| Patas | Cuota techo | p | EV |
|---|---|---|---|
| Japón Goles Menos 4.5 (1.20, 82 %) + Noruega Menos 4.5 (1.15, 87 %) | 1.38 | 0.711 | -1.9 % |
| Noruega-Gales Noruega Menos 4.5 + Suecia córners Menos 10.5 (1.29, 76 %) | 1.48 | 0.661 | -2.0 % |
| Japón Goles Menos 4.5 + Suecia córners Menos 10.5 | 1.55 | 0.623 | -3.5 % |

Ambas «Goles Menos» dependen de un guion de pocos goles del favorito (un mismo guion de jornada; no son la misma apuesta pero se mueven parecido). Suecia-Bosnia tiene alerta de simulación 16-24 pts: su pata es la más frágil. Si el cupón paga más que el producto, el EV mejora; hoy ninguna lo supera.

## Lotería (stake mínimo, solo si el usuario quiere)
Japón Goles Menos 4.5 + Noruega Menos 4.5 + Mallorca córners Más 7.5: cuota techo 1.64, p 0.572, EV -6 %. No la recomiendo; solo si el cupón paga >1.75.

## Lo que no pude evaluar
Jugadores (sin alineaciones), 1T/2T sin ficha, precio real del cupón, y la dependencia entre partidos distintos.
