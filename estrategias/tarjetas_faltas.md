# Tarjetas y faltas

Betano cuenta tarjetas en **puntos** (amarilla 1, roja 2); Flashscore solo trae amarillas (la serie queda por debajo si hubo rojas).

## Lectura obligatoria por partido
1. **Árbitro primero** (el factor que más pesa, *tipster*): amarillas, faltas y penales por partido, y si el dato es de la liga o de torneos europeos; con menos de 6 partidos de ese nivel, confianza baja. Si el modelo de equipos dice «menos» pero el árbitro promedia mucho más que la línea, la señal de Menos no vale (*lección: esta corrección refutó Unders falsos*). Dato: `arbitros/<clave>.json` (ValueStats). Si no hay árbitro, se dice y no se sugiere tarjetas.
2. **Qué se juegan:** derbi, decisivo, necesidad de puntos (+ tarjetas); nada en juego (−) (`notas/`).
3. **Estilo:** presión alta que pierde balones = más faltas tácticas; el equipo que defiende mucho comete más faltas; **el favorito comete menos faltas** (*tipster*). Faltas «Más» de un equipo que domina la pelota fallaron (*lección Milan, 8-nov*).
4. **Marcador:** partidos cerrados y tardíos traen más tarjetas; las goleadas, menos (*tipster*).
5. **Faltas esperadas** (≥ 26 sube tarjetas, ≤ 21 baja) (`ficha.faltas`).
6. **Rivalidad e historial entre los dos** (directos).
7. **Regularidad** ≥ 7 de 10 en ambos; «ambos con N tarjetas» y «equipo con más tarjetas» desde las series por equipo (dependencia entre equipos no modelada).
8. Nivel europeo: puntos de tarjetas = amarillas × 1,04; faltas × 1,06 (*tipster*, sin verificar).

## Medición
Tarjetas Menos 81 % y faltas Menos 82 % en tus boletos (n 21 y 11): pistas, no leyes. Tarjetas del modelo ≈ precio (Brier 0,1821 / 0,1820).
