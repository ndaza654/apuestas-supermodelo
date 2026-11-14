# Revisión crítica de las combinadas · jornada 14-nov-2026 (agente combinadas)

Fecha de la revisión: 14-nov-2026 (horas de Bogotá, tomadas de `analisis.json`). Fuente: `analisis.json` (combinadas, lotería, real),
`informes/<slug>_resultado.json` (alertas, guiones) y recálculo con `python3 -m supermodelo --combos` (combos en carpeta temporal fuera del repo).
Cuotas: producto de cuotas individuales = TECHO; no tenemos el precio del cupón de Betano (las combinadas del mismo partido suelen pagar menos que el producto, sobre todo con correlación > 1).
Muestra de 7 partidos (cumple = 5 de 7). Tarjetas y jugadores fuera (sin árbitro / sin historial). No se leyeron los JSON crudos de flashscore/ ni betano/.

## Enfoque de mercados
Las 6 combinadas son de 2 patas del mismo partido, todas con cuotas 1,20–1,30 por pata (2 de ellas «Más», 10 de 12 patas «Menos»). El peso está en mercados de volumen
(córners, tiros al arco, remates) y goles «Menos». Son apuestas de «partido de poco volumen»: una sola idea repetida en 5 de los 7 boletos.

## Hechos que afectan a toda la lectura
1. **Todas tienen EV negativo con la p recortada** (entre −17 % y −25 %). Solo Mirassol sale en positivo (+3,4 %) con `p_ajust` SIN recortar y esa lectura es la menos fiable (misma historia dos veces).
2. **Historial real propio:** combinadas de 2 patas 7 de 21 (33 % real contra 55 % dicho); del mismo partido 9 de 29 (31 % contra 47 %). Aplicar ×0,80 a `p_ajust` (resultado 0,48–0,55) sigue siendo más optimista que lo que ha pasado (ratio real/dicho ≈ 0,6 → p ≈ 0,36–0,42). Con cuota 1,5 y p 0,33, EV ≈ −50 %.
3. **Idea repetida (cartera):** «poco volumen / pocos córners / pocos goles» aparece en Mirassol, Kosovo, Banfield, Portugal, Mallorca y en la lotería. Si el día sale con partidos abiertos, caen juntas. Cuentan como una apuesta repetida (regla 5).
4. **Patrón repetido:** «córners Menos + goles Menos» en Portugal y Mallorca; «tiros al arco Menos + córners Menos» en Kosovo y Banfield (y la lotería reusa las patas de Banfield y de Portugal, así que no es independiente de ellas).
5. Alertas del modelo (`informes/*_resultado.json`): Noruega–Gales (sim. a 21 pts del mercado), Portugal–Dinamarca (22 pts), Atlético Nacional–Once Caldas (15 y 16 pts). Las alertas están en saques de banda 1T (Noruega, Portugal) y «más córners que» (Nacional); NINGUNA coincide con la familia de las patas, así que el filtro del script no se rompe, pero la simulación de esos tres partidos no es fiable en conjunto: las probabilidades conjuntas de Noruega, Portugal y la lotería (pata de Nacional) hay que leerlas con reserva.

## Cifras por combinada
p_rec = p_ajust × 0,80 (del script). Stress = p_rec con la pata más débil (menor p_rec) 5 pts peor: p_rec × (p_pata − 0,05)/p_pata. Cuota de equilibrio = 1/p_rec (con stress, 1/p_stress). EV = p_rec × cuota − 1.

| Partido (hora) | Patas | Cuota prod. | p_sim | p_ajust | p_rec | p_stress | EV (p_rec) | EV (p_ajust) | Cuota equilibrio (stress) | Pata frágil |
|---|---|---|---|---|---|---|---|---|---|---|
| Kosovo–Israel (09:00) | Córners Menos 10.5 + Tiros al arco Israel Menos 4.5 | 1,61 | 59,3 % | 60,4 % | 48,3 % | 44,8 % | −22,3 % | −2,8 % | 2,07 (2,23) | Tiros al arco Israel (p_rec 70,01 %, colchón 0,93) |
| Noruega–Gales (12:00) | Córners Noruega Menos 7.5 + Tiros al arco Gales Más 1.5 | 1,49 | 60,6 % | 62,6 % | 50,1 % | 46,6 % | −25,4 % | −6,8 % | 2,00 (2,14) | Tiros al arco Gales Más 1.5 (Gales cumple 5 de 7) |
| Mallorca–Córdoba (12:30) | Goles Menos 4.5 + Córners Menos 12.5 | 1,57 | 60,1 % | 60,5 % | 48,4 % | 45,0 % | −24,0 % | −5,1 % | 2,07 (2,22) | Córners Menos 12.5 (colchón 1,07; visitante 5 de 7) |
| Portugal–Dinamarca (14:45) | Goles Portugal Menos 3.5 + Córners Menos 11.5 | 1,50 | 62,4 % | 62,5 % | 50,0 % | 46,5 % | −25,0 % | −6,2 % | 2,00 (2,15) | Córners Menos 11.5 (L 5 de 7, directos 1 de 3) |
| Mirassol–Atlético MG (16:30) | Tiros al arco Mirassol Menos 7.5 + Remates Mirassol Menos 19.5 | 1,50 | 66,7 % | 68,9 % | 55,2 % | 51,3 % | −17,3 % | +3,4 % | 1,81 (1,95) | Remates Menos 19.5 (directos 1 de 3) |
| Banfield–Boca (17:00) | Córners Menos 10.5 + Tiros al arco Banfield Menos 4.5 | 1,56 | 58,6 % | 59,7 % | 47,8 % | 44,4 % | −25,5 % | −6,9 % | 2,09 (2,25) | Tiros al arco Banfield Menos 4.5 (local 5 de 7, directos 3 de 5) |
| Lotería: Nacional Goles Más 1.5 + Banfield al arco local Menos 4.5 + Portugal córners Menos 11.5 | 1,97 | — | 45,3 % (producto de p) | — | 37,3 % | 34,7 % | −26,4 % | −10,8 % | 2,68 (2,88) | Córners Portugal 11.5 y al arco Banfield (p_rec 71,6–71,9 %) |

El stress del modelo (sobre p_ajust, sin recortar) coincide en la pata frágil con la de arriba: Mirassol −3,4 % de EV, Noruega −12,8 %, Portugal −12,4 %, Mallorca −11,4 %, Kosovo −9,3 %, Banfield −13,0 % (todas «evitar» menos Mirassol «justo»).

## Pregunta 1 y 2: ¿dos eventos o una historia?, dependencia, reglas
- **Mirassol:** la MISMA historia dos veces. Los tiros al arco son un subconjunto de los remates; ambas «Menos» sobre el mismo equipo (local) en el mismo partido. Dependencia a favor (corr. 1,13; el conjunto es 13 % más probable que el producto 0,61 → 0,69), por eso el conjunto pierde poco respecto a la pata débil, pero el cupón real casi seguro paga menos que 1,21×1,24 = 1,50 (la casa precia la correlación). Remates: directos 1 de 3 en contra, p con cumple de ese tipo 9 de 13. Frágil: remates. Regla: no rompe ninguna (p_rec 75,0 % y 71,9 %); sí es lo que la auditoría llama «misma historia».
- **Noruega–Gales:** dos eventos distintos (córners de Noruega, tiros de Gales) pero ambos dependen de que Noruega (favorito 81 %) NO domine: si domina, caen los dos Menos/Más en contra (más córners Noruega, menos tiros Gales). El guion más probable (37 %) es «partido abierto», que ayuda al tiro de Gales pero perjudica a córners Menos. Corr. 1,0 en el modelo, pero la simulación está a 21 pts del mercado (alerta); no es fiable. Gales cumple 5 de 7 (borde) y es el lado de 5,7 %.
- **Portugal–Dinamarca:** goles local Menos 3.5 y córners totales Menos 11.5: ambos «pocos», dependencia ligera a favor (el modelo da 1,0). Ambas patas con directos 1 de 3 en contra y L 5 de 7 en córners; alerta de la simulación (22 pts). Guion común «Empate» pero el 38,5 % del modelo es «partido abierto» que rompe las dos.
- **Mallorca–Córdoba:** goles Menos 4.5 (casi gratis; colchón 2,0) + córners Menos 12.5 (colchón 1,07, visitante en el borde). Casi independientes (corr. 1,01); la combinada es en la práctica el córners solo con una pata de relleno que paga 1,24. Sin enfrentamientos directos.
- **Kosovo–Israel:** córners totales Menos 10.5 (esperado 6,79) + tiros al arco Israel Menos 4.5 (esperado 3,57, colchón 0,93, p_rec 70,01 % = justo el umbral, cuota 1,30 donde el historial real es 24 de 37, 65 % contra 70 % dicho). Dependencia a favor leve (guion «favorito gana en partido trabado»). Sin alertas.
- **Banfield–Boca:** córners Menos 10.5 (colchón 0,93, L y V en 5 de 7) + tiros al arco Banfield Menos 4.5 (colchón 2,0, directos 3 de 5). Banfield es el no-favorito (12 %): el guion «Boca gana trabado» sostiene ambas «Menos». Es la misma idea «poco volumen» que Kosovo y Mirassol.
- **Lotería:** 3 partidos, independientes entre sí por partido pero no por idea (2 de 3 patas son «poco volumen»); Nacional Goles Más 1.5 en un partido con alerta (corners) y p_rec 72,5 % con colchón 0,79 y historial de «Goles Más con cumple» 21 de 30 (70 %). La p_rec 37,3 % es el producto de p_rec de patas (no ×0,80; ver abajo).
- **Reglas:** ninguna combinada rompe formalmente las reglas del script (todas las patas «cumple», p_rec ≥ 70 %, familias distintas, máx. 2 por partido). Matices: Kosovo al arco Israel está en el umbral (70,01 %); las patas con directos en contra (Mirassol remates, Portugal goles y córners) y con 5 de 7 justo (Noruega-Gales visitante, Portugal local córners, Banfield, Kosovo local ya 7 de 7) pasan «cumple» en el borde; el patrón «córners Menos + goles Menos» sale 2 veces y «al arco Menos + córners Menos» 2 veces; Mirassol es misma familia estadística (remates / al arco).

## Cifras que no cuadran o limitan
- La p_rec de las combinadas es `p_ajust × 0,80`; la de la lotería es el producto de `p_rec` de las patas (0,7248 × 0,7194 × 0,7161 = 0,3734, ratio 0,825 sobre p), no ×0,80. Distinta convención.
- El historial «Tiros al arco Menos con cumple 9 de 10» (Mirassol, Kosovo, Banfield) y «Tiros al arco Más con cumple 9 de 10» (Noruega) son los mismos 9 de 10: el contador no distingue lado en este caso; n = 10 es poco.
- «Cuota < 1,30: 109 de 133 (82 % real contra 87 %)»: todas las patas están en ese tramo y se queda ~5 pts por debajo de lo dicho; el recorte 0,941 aplicado se acerca, pero la combinación de dos patas ha rendido peor (33 % vs 55 %).
- Sin precio del cupón: el EV real puede ser peor (SGM con correlación) o ligeramente distinto; Betano puede no ofrecer estas parejas como combinada del mismo partido (no verifiqué el cupón).
- Sin árbitro (tarjetas) y sin alineaciones (jugadores) no se evaluó nada de esos mercados. La hora de los partidos es la de `analisis.json`, no la comprobé de nuevo contra Betano.

## Veredicto
Ninguna como apuesta: con la p recortada todas están en −17 % a −26 % de EV y necesitan cuotas de 1,8–2,1 (2,7 la lotería) para dejar de perder, contra 1,49–1,61 de techo; y el historial propio de 2 patas (33 %) es peor que el supuesto. Como lectura menos mala, solo Kosovo–Israel (sin alerta, directos 3 de 3, pero pata de Israel en el umbral) y Mirassol (mejor p, pero misma historia dos veces y cupón probablemente < 1,50); si el usuario apuesta, las patas que mejor pasan por separado son sencillas (colchón > 3: Noruega córners local Menos 7.5, Mirassol al arco Menos 7.5, Kosovo córners Menos 10.5), no la pareja. No apostar: Noruega–Gales, Portugal–Dinamarca (alerta de simulación), Mallorca, Banfield y la lotería.
