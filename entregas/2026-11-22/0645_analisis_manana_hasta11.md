# Análisis y combinadas · partidos hasta las 11:00 · dom 22-nov-2026
Entrega 22-nov 06:45 Bogotá · Cuotas de Betano releídas 06:22 (BB Boost: precios reales mc-leg 06:31) · Alineaciones: probables (oficiales ≈ 1 h antes de cada partido; sin releer todavía) · Informe interactivo completo: `jornadas/2026-11-22/informe.html` (pestaña «Análisis»).

## Enfoque de mercados
Juventus–Venezia (6:30) ya había empezado: no se analiza para apostar. Los otros 10 partidos hasta las 11:00:
- **Barcelona–Villarreal (8:00):** Barça 84 % (1.º, 11 victorias en 12). El resultado paga poco; cumplen líneas de ritmo: tiros al arco Menos 12.5 y faltas Menos 23.5.
- **Paris FC–Angers (9:00):** Paris 77 % (3.º vs 17.º). Pesan córners y remates de cada lado; es el partido con más BB Boost que cumple precio.
- **Bologna–Udinese (9:00):** Bologna 56 %; Udinese (20.º) lleva 25 goles en contra. Goles del visitante Menos 1.5 y «Bologna o empate».
- **Hull–Brighton (9:00):** Brighton 66 %. Goles/remates/córners de Brighton; Hull Menos goles. Alerta en saques de banda (modelo a 23 pts del mercado): no se usa.
- **Sassuolo–Genoa (9:00) y Augsburg–Mainz (9:30):** parejos (35/28/37 y 34/25/41): 1.er tiempo Menos, empate al descanso, ambos marcan; no el resultado.
- **Racing–Real Sociedad (10:15):** Real Sociedad 48 %. Tarjetas Más 3.5, córners Más 8.0, remates de Racing Menos.
- **Córdoba–Oviedo (8:00), Huachipato–Concepción (10:00), Gijón–Las Palmas (10:15):** Betano solo ofrece goles, córners, tarjetas y goleador. **Alerta en córners de Córdoba y Gijón** (la simulación se aleja 15–23 pts del mercado): no se recomiendan córners ahí.

## Combinadas del mismo partido (máx. 2 patas, ambas «cumple» ≥ 7 de 10)
| Hora | Partido | Patas | Cuota | p recortada |
|---|---|---|---|---|
| 9:00 | Bologna–Udinese | Goles visitante Menos 1.5 @1,26 + Bologna o empate @1,21 | 1,52 | 56,5 % |
| 9:00 | Hull–Brighton | Tiros al arco local Menos 4.5 @1,20 + Goles local Menos 1.5 @1,23 | 1,48 | 55,7 % |
| 10:15 | Racing–Real Sociedad | Tarjetas Más 3.5 @1,23 + Córners Más 8.0 @1,31 | 1,61 | 53,3 % |

Con la p recortada (conjunta de la simulación − 20 %) las tres tienen valor esperado negativo (≈ −14 %): se dan ≈ 1 de 2, pero a cuota 1,5 no pagan. Son lo único que las reglas de combinadas dejan pasar hoy por la mañana.

## BB Boost (Bet Builder mismo partido, ≥ 3 patas, cada una > 1,50, total > 5,00) · precio REAL de Betano
- **Racing–Real Sociedad: sí cumple.** A: Real Sociedad remates Más 14.5 @1,62 + Racing remates Menos 14.5 @2,15 + Racing tiros al arco Menos 4.5 @2,30 → precio **5,80** (producto 8,01), p modelo 18,2 % (stress 16,0 %), EV con boost +27 % (con p stress +12 %).
- **Paris FC–Angers: sí cumple (16 combos).** A: Córners Angers Más 2.5 @1,55 + Goles Menos 3.5 @1,75 + Córners Paris Menos 5.5 @2,07 → precio **6,10**, p 16,6 %, EV con boost +22 %. B: Córners Angers Más 2.5 + Fueras Paris Menos 1.5 @1,70 + Córners Paris Menos 5.5 → 5,50, p 17,6 %, EV +17 %.
- **Sassuolo–Genoa: sí cumple (1 combo, EV ≈ +2 %).** Barça, Bologna, Hull, Augsburg: **no cumplen** (Betano comprime el precio cuando las patas se parecen; ninguno llega a 5,05).
- Lotería (p 15–18 %, punto de equilibrio con boost +25 % ≈ 14–16 %): stake mínimo. Leer el % del boost en el cupón (el 21-nov cobró +50 %). La p es la del modelo, sin validar contra el precio.

## Sencillas con valor esperado ≥ 0 (informativas)
- Córdoba–Oviedo Tarjetas Más 5.5 @1,50 (p 69 %, 10 de 10 y 7 de 10, directos 2 de 2). La tasa histórica de clubes es 59 % («en contra»): con esa p el EV sería negativo.
- Hull–Brighton Córners Más 9.0 @1,55 (p 67 %, 7 y 8 de 10, esperado 10,95, colchón +1,95; sin tasa histórica).
- Protección (cuota < 1,50, se dan pero no pagan): Racing–Real Sociedad Tarjetas Más 3.5 @1,23 (84 %), Barça tarjetas local Más 0.5 @1,20 (81 %, directos 6 de 6), Paris fueras local Menos 2.5 @1,20 (81 %).

## Jugadores
Sin recomendaciones: los mercados de jugador del modelo van inflados 7–26 pts frente a lo liquidado (balance 21-nov) y no hay alineaciones oficiales. Lo que cumple en la ficha (para mirar, no para apostar): Gregoritsch remates 1+ @1,98 (8 de 9), Bernardeschi remates 1+ @2,60 (8 de 10), Tzolakis atajadas 2+ @1,53 (7 de 9), Ferguson entradas 2+ @1,65 (8 de 10).

## Arreglo de «entradas» (hecho hoy)
Betano «Tackles totales» cuenta entradas **intentadas**; la ficha usaba las **ganadas** de Flashscore. Medido en 200+ jugadores del 22-nov: con ganadas la frecuencia real quedaba muy por debajo de la implícita en los precios (0,51 contra 0,82 en «1+»); con intentadas guarda la misma relación que remates. Corregido en `armar_entrada.hist_de` (`entradas` = intentadas, `entradas_gan` = ganadas; prueba añadida). Las líneas de entradas de jornadas anteriores se calcularon con ganadas: el «Más» salía subestimado y el «Menos» sobrestimado.

## Límites
- Cuotas 6:22; alineaciones probables, sin oficiales; Juventus no analizado. Sin tasa histórica en ambos marcan, resultado ni estadísticas de partido de Hull/Sassuolo.
- Segunda de España y Chile solo con goles/córners/tarjetas; faltas recibidas, fueras de juego, pases y 1T de jugador están recogidos pero no analizados.
- Ni el filtro «cumple», ni la p del modelo, ni el contexto han mejorado al precio de mercado fuera de muestra (hallazgos 4–21 nov): el valor esperado de lo anterior es informativo, no una ventaja demostrada.
