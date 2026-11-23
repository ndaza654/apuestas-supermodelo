# Recolección y análisis de los 17 partidos del 24-nov (Champions + AFC Elite)

Fecha y hora de la entrega: 2026-11-23 ~18:55 (Bogotá). Cuotas: Betano, leídas 23-nov 17:21 (Bogotá), **sin releer**. Alineaciones de la Champions: probables (Flashscore ~18:10); oficiales ~1 h antes. Límites completos al final y en `jornadas/2026-11-24/ESTADO.md`. Informe interactivo: `entregas/2026-11-23/1855_informe_24nov.html` (mismo de `jornadas/2026-11-24/informe.html`).

## Enfoque de mercados

- **Champions League (9 partidos, 12:45–15:00): todos los mercados que Betano ofrece** — córners, goles, tarjetas, remates, tiros al arco, saques de meta, fueras de juego, faltas, ambos marcan, resultado y jugadores. Pesan sobre todo **córners y goles** (en jornadas anteriores las líneas con «cumple» se dieron 84–86 % y el modelo estaba calibrado) y las **sencillas de 1,50–1,99** con la probabilidad recortada.
- **Tiros al arco Menos y remates Menos: con cautela.** Con «cumple», el real hasta hoy fue 76 % (tiros al arco Menos, se decía 82 %) y 61 % (remates Menos, se decía 66 %): el análisis les recorta la probabilidad ×0,93.
- **Tarjetas:** los 9 árbitros de la Champions están leídos (ValueStats); Napoli es, según Flashscore, el equipo con más tarjetas de la competición este año; Leipzig–Lens (6 líneas que cumplen), Arsenal–Dortmund, City–Napoli y Feyenoord–Porto (4 cada una) son los que más líneas de tarjetas traen con «cumple».
- **Jugadores (remates, tiros al arco, entradas, faltas):** historial por jugador leído en los 18 equipos de la Champions, de **8 a 10 de sus últimos 10 partidos** (10 de 10: Dortmund, Como, Galatasaray, Aston Villa, Man City, Leipzig, Lens, Slovan; el que menos, 8 de 10: AEK, Feyenoord, Porto, PSV). Los partidos que faltan (14 de 180 partidos-equipo) son de ligas o copas sin tabla de jugadores en Flashscore y se listan en `jugadores/LEEME.md`.
- **AFC Champions League Elite (8 partidos, 02:45–13:15):** Betano solo ofrece **resultado, hándicap, goles y córners** (y goleador en 5 de los 8: Daejeon, Ratchaburi, Shanghai Port, Shabab Al Ahli y Al-Nassr; Newcastle Jets, Kyoto y Cong An no tienen goleador en Betano). No hay remates, faltas ni tarjetas de equipo ni de jugador. Pesan resultado/hándicap y goles; los córners tienen líneas muy parejas (p del modelo 47–53 % en la línea central).
- **Contexto que cambia la lectura:** Bodø, Feyenoord, Porto, Napoli, Leipzig, Lens, AEK y Slovan están fuera de los 24 primeros de la tabla (necesitan sumar); Arsenal llega sin Raya ni Zubimendi y Real Madrid sin Endrick, Mendy ni Rodrygo (lista de bajas de Flashscore). En la AFC, 9 de los 16 equipos llegan fuera de los 8 puestos que clasifican de su zona.
- **Límites:** cuotas leídas el 23-nov 17:21 (sin releer); alineaciones de Champions son PROBABLES (oficiales ~1 h antes); AFC sin alineaciones ni previa en Flashscore; árbitros de la AFC sin anunciar; todo lo de contexto es lectura de datos de Flashscore, sin resultados verificados de los criterios.


## AFC Elite: mercados foco (resultado, hándicap, goles, córners, goleador)

p = probabilidad del modelo (simulación mezclada con el precio); EV = p·cuota − 1. Heurísticas sin validar; goleador: «p mezcla» = (partidos con gol de 10 + 10·p_cuota/1,08)/20.

## Newcastle Jets - Kashiwa Reysol (02:45 Bogotá)
- **Resultado (modelo):** Newcastle Jets 14 % · empate 18 % · Kashiwa Reysol 68 % · tipo: Favorito claro · abierto · normal.
- **Goles esperados:** total 3.77 (Betano 3.72); intervalo 10–90 %: 1–6.
- **Hándicap (las 3 más probables):** Newcastle Jets +3 @1.31 p 75 % EV -2 %; Kashiwa Reysol -0.75 @1.52 p 63 % EV -4 %; Newcastle Jets +1.75 @1.57 p 62 % EV -3 %.
  - Mayor EV: Newcastle Jets +3 @1.31 p 75 % EV -2 %.
- **Goles, línea más pareja:** Goles Más 3.5 @1.82 p 52 % EV -6 %. Línea 2.5: Goles Más 2.5 @1.34 p 73 %; Goles Menos 2.5 @3.00 p 27 %.
- **Córners, línea más pareja:** Córners Menos 10.0 @2.00 p 52 % EV +4 % (esperado 10.1).
- **Goleador:** Betano no ofrece mercados de goleador para este partido (sin leer).

## Daejeon Citizen - Beijing Guoan (05:00 Bogotá)
- **Resultado (modelo):** Daejeon Citizen 65 % · empate 20 % · Beijing Guoan 16 % · tipo: Favorito claro · abierto · normal.
- **Goles esperados:** total 3.07 (Betano 3.07); intervalo 10–90 %: 1–5.
- **Hándicap (las 3 más probables):** Beijing Guoan +3 @1.20 p 82 % EV -2 %; Daejeon Citizen -0.5 @1.53 p 64 % EV -2 %; Beijing Guoan +2 @1.55 p 62 % EV -4 %.
  - Mayor EV: Beijing Guoan +3 @1.20 p 82 % EV -2 %.
- **Goles, línea más pareja:** Goles Más 3.0 @1.95 p 48 % EV -6 %. Línea 2.5: Goles Más 2.5 @1.60 p 59 %; Goles Menos 2.5 @2.22 p 41 %.
- **Córners, línea más pareja:** Córners Menos 9.0 @2.00 p 52 % EV +3 % (esperado 9.1).
- **Goleador (anota; mayor p mezcla):** Diogo Oliveira @1.98 · gol en 6 de 10 partidos · p mezcla 53 %; Yuning Zhang @3.00 · gol en 3 de 10 partidos · p mezcla 30 %; Masatoshi Ishida @2.27 · gol en 2 de 10 partidos · p mezcla 30 %.

## Kyoto Sanga FC - Pohang Steelers (05:00 Bogotá)
- **Resultado (modelo):** Kyoto Sanga FC 59 % · empate 24 % · Pohang Steelers 17 % · tipo: Favorito leve · medio · normal.
- **Goles esperados:** total 2.68 (Betano 2.68); intervalo 10–90 %: 1–5.
- **Hándicap (las 3 más probables):** Kyoto Sanga FC +1 @1.18 p 82 % EV -3 %; Pohang Steelers +2 @1.44 p 67 % EV -3 %; Kyoto Sanga FC -0.25 @1.44 p 67 % EV -4 %.
  - Mayor EV: Kyoto Sanga FC +1 @1.18 p 82 % EV -3 %.
- **Goles, línea más pareja:** Goles Más 2.5 @1.85 p 50 % EV -7 %. Línea 2.5: Goles Más 2.5 @1.85 p 50 %; Goles Menos 2.5 @1.85 p 50 %.
- **Córners, línea más pareja:** Córners Más 9.0 @2.07 p 50 % EV +3 % (esperado 9.2).
- **Goleador:** Betano no ofrece mercados de goleador para este partido (sin leer).

## Cong An Ha Noi - Vissel Kobe (07:15 Bogotá)
- **Resultado (modelo):** Cong An Ha Noi 21 % · empate 24 % · Vissel Kobe 55 % · tipo: Favorito leve · abierto · normal.
- **Goles esperados:** total 2.90 (Betano 2.90); intervalo 10–90 %: 1–5.
- **Hándicap (las 3 más probables):** Vissel Kobe +1 @1.24 p 78 % EV -3 %; Cong An Ha Noi +2 @1.37 p 70 % EV -4 %; Cong An Ha Noi +1.25 @1.45 p 66 % EV -4 %.
  - Mayor EV: Vissel Kobe +1 @1.24 p 78 % EV -3 %.
- **Goles, línea más pareja:** Goles Menos 2.75 @1.85 p 50 % EV -8 %. Línea 2.5: Goles Más 2.5 @1.70 p 56 %; Goles Menos 2.5 @2.05 p 44 %.
- **Córners, línea más pareja:** Córners Más 8.5 @1.85 p 50 % EV -7 % (esperado 8.8).
- **Goleador:** Betano no ofrece mercados de goleador para este partido (sin leer).

## Ratchaburi FC - Johor Darul Takzim (07:15 Bogotá)
- **Resultado (modelo):** Ratchaburi FC 18 % · empate 21 % · Johor Darul Takzim 60 % · tipo: Favorito claro · abierto · normal.
- **Goles esperados:** total 3.29 (Betano 3.27); intervalo 10–90 %: 1–6.
- **Hándicap (las 3 más probables):** Johor Darul Takzim +1 @1.20 p 81 % EV -3 %; Ratchaburi FC +2 @1.50 p 65 % EV -3 %; Ratchaburi FC +1.5 @1.50 p 65 % EV -3 %.
  - Mayor EV: Johor Darul Takzim +1 @1.20 p 81 % EV -3 %.
- **Goles, línea más pareja:** Goles Menos 3.0 @1.98 p 48 % EV -6 %. Línea 2.5: Goles Más 2.5 @1.50 p 64 %; Goles Menos 2.5 @2.42 p 36 %.
- **Córners, línea más pareja:** Córners Más 9.0 @2.00 p 52 % EV +4 % (esperado 9.3).
- **Goleador (anota; mayor p mezcla):** Bergson @1.82 · gol en 5 de 10 partidos · p mezcla 50 %; Marcos Guilherme @2.12 · gol en 5 de 10 partidos · p mezcla 47 %; Shahab Zahedi @2.00 · gol en 4 de 10 partidos · p mezcla 43 %.

## Shanghai Port - Buriram United (07:15 Bogotá)
- **Resultado (modelo):** Shanghai Port 50 % · empate 25 % · Buriram United 25 % · tipo: Favorito leve · abierto · normal.
- **Goles esperados:** total 3.01 (Betano 2.99); intervalo 10–90 %: 1–5.
- **Hándicap (las 3 más probables):** Shanghai Port +1 @1.29 p 74 % EV -4 %; Buriram United +2 @1.31 p 74 % EV -3 %; Shanghai Port +0 @1.45 p 66 % EV -4 %.
  - Mayor EV: Buriram United +2 @1.31 p 74 % EV -3 %.
- **Goles, línea más pareja:** Goles Menos 2.75 @1.93 p 48 % EV -8 %. Línea 2.5: Goles Más 2.5 @1.65 p 58 %; Goles Menos 2.5 @2.12 p 42 %.
- **Córners, línea más pareja:** Córners Más 9.5 @1.85 p 51 % EV -6 % (esperado 9.8).
- **Goleador (anota; mayor p mezcla):** Leonardo @1.87 · gol en 6 de 10 partidos · p mezcla 55 %; Prince Ampem @3.15 · gol en 7 de 10 partidos · p mezcla 50 %; Lei Wu @2.27 · gol en 4 de 10 partidos · p mezcla 40 %.

## Shabab Al Ahli Dubai - Al-Qadsiah FC (11:00 Bogotá)
- **Resultado (modelo):** Shabab Al Ahli Dubai 31 % · empate 28 % · Al-Qadsiah FC 41 % · tipo: Parejo · medio · normal.
- **Goles esperados:** total 2.72 (Betano 2.74); intervalo 10–90 %: 1–5.
- **Hándicap (las 3 más probables):** Shabab Al Ahli Dubai +2 @1.21 p 81 % EV -2 %; Al-Qadsiah FC +1 @1.40 p 69 % EV -3 %; Shabab Al Ahli Dubai +0.75 @1.45 p 67 % EV -3 %.
  - Mayor EV: Shabab Al Ahli Dubai +2 @1.21 p 81 % EV -2 %.
- **Goles, línea más pareja:** Goles Más 2.5 @1.80 p 51 % EV -8 %. Línea 2.5: Goles Más 2.5 @1.80 p 51 %; Goles Menos 2.5 @1.90 p 49 %.
- **Córners, línea más pareja:** Córners Menos 9.0 @1.98 p 53 % EV +4 % (esperado 9.0).
- **Goleador (anota; mayor p mezcla):** Julián Quiñones @2.20 · gol en 7 de 10 partidos · p mezcla 56 %; Mateo Retegui @2.55 · gol en 5 de 10 partidos · p mezcla 43 %; Mateusao Dias @3.05 · gol en 4 de 10 partidos · p mezcla 35 %.

## Al-Nassr FC - Al-Sadd SC (13:15 Bogotá)
- **Resultado (modelo):** Al-Nassr FC 80 % · empate 12 % · Al-Sadd SC 8 % · tipo: Favorito claro · abierto · normal.
- **Goles esperados:** total 3.85 (Betano 3.86); intervalo 10–90 %: 2–6.
- **Hándicap (las 3 más probables):** Al-Sadd SC +2.5 @1.50 p 64 % EV -4 %; Al-Sadd SC +3 @1.52 p 64 % EV -3 %; Al-Sadd SC +2.25 @1.60 p 60 % EV -4 %.
  - Mayor EV: Al-Sadd SC +3 @1.52 p 64 % EV -3 %.
- **Goles, línea más pareja:** Goles Más 3.75 @1.91 p 49 % EV -7 %. Línea 2.5: Goles Más 2.5 @1.30 p 74 %; Goles Menos 2.5 @3.25 p 26 %.
- **Córners, línea más pareja:** Córners Más 10.5 @2.00 p 47 % EV -6 % (esperado 10.4).
- **Goleador (anota; mayor p mezcla):** Cristiano Ronaldo @1.39 · gol en 5 de 10 partidos · p mezcla 58 %; Abdullah Al-Hamdan @1.95 · gol en 4 de 10 partidos · p mezcla 44 %; Akram Afif @3.90 · gol en 5 de 10 partidos · p mezcla 37 %.


## Combinadas de 2 patas del mismo partido — 6

Cada pata con p recortada ≥ 70 %; la conjunta sale de la simulación y se recorta 20 %; la cuota es el producto de las cuotas (techo).

| Hora | Partido | Patas | Cuota (producto) | p simulación | p ajustada | p recortada | Pata más frágil | Pata de menor colchón |
|---|---|---|---|---|---|---|---|---|
| 15:00 | Arsenal FC - Borussia Dortmund | Goles Menos 4.5 + Tiros al arco Menos 12.5 | 1,50 | 69 % | 69 % | 55 % | Tiros al arco Menos 12.5 | Tiros al arco Menos 12.5 (colchón 30 % de la línea) |
| 15:00 | Manchester City - SSC Napoli | Remates Más 25.5 + Córners Más 7.0 | 1,60 | 58 % | 65 % | 52 % | Remates Más 25.5 | Remates Más 25.5 (colchón 17 % de la línea) |
| 15:00 | SK Slovan Bratislava - Real Betis Balompié | Córners Menos 12.5 + Remates Menos 32.5 | 1,51 | 61 % | 64 % | 51 % | Remates Menos 32.5 | Remates Menos 32.5 (colchón 7 % de la línea) |
| 05:00 | Daejeon Citizen - Beijing Guoan | Goles Menos 4.5 + Resultado: gana alguno (sin empate) | 1,45 | 62 % | 62 % | 50 % | No hay empate | Goles Menos 4.5 (colchón 36 % de la línea) |
| 07:15 | Cong An Ha Noi - Vissel Kobe | Goles Más 1.5 + Resultado: gana alguno (sin empate) | 1,54 | 60 % | 60 % | 48 % | No hay empate | Goles Más 1.5 (colchón 67 % de la línea) |
| 15:00 | RB Leipzig - RC Lens | Córners Más 8.0 + Tarjetas visitante Más 1.5 | 1,99 | 48 % | 53 % | 42 % | Tarjetas RC Lens Más 1.5 | Tarjetas visitante Más 1.5 (colchón 27 % de la línea) |

## Estado de la recolección

17 partidos: 9 de la Champions League (datos completos) y 8 de la AFC Champions League Elite (resultado, hándicap, goles, córners y goleador).

| Qué | Champions (9) | AFC Elite (8) |
|---|---|---|
| Cuotas y mercados de Betano (leídas 23-nov ~17:21) | todos los mercados (≈200 líneas de equipo, ≈22 únicos, 290–350 de jugador, parejas) | 35–38 líneas de equipo, 14 únicos; goleador solo en 5 partidos |
| Historial de equipos (10 partidos) + directos | sí (directos: 0–1 partido con estadísticas) | sí (igual) |
| Historial por jugador (10 partidos por equipo) | **sí, los 18 equipos: 8–10 de 10 partidos** (`jugadores/LEEME.md` lista los 14 que faltan) | no aplica (Betano no ofrece mercados de jugador de estadística) |
| Árbitro | los 9 (Flashscore + ValueStats) | **no anunciado** todavía en ninguno |
| Goleadores/goleadoras (incidentes de los 10 partidos de cada equipo) | sí (34 equipos, 306 partidos) | sí; Newcastle Jets, Kyoto y Cong An no tienen mercado de goleador en Betano |
| Alineaciones | **probables** de Flashscore (leídas 23-nov ~18:10 Bogotá); las oficiales salen ~1 h antes | Flashscore no las publica; sin leer |
| Tabla, bajas y contexto (notas/) | sí (previa de Flashscore: bajas, tabla, forma) | tabla y forma; sin previa ni bajas |

## Lo que NO se pudo leer (declarado)
- **Árbitros de la AFC:** sin anunciar el 23-nov. Los mercados de tarjetas de la AFC no existen en Betano para estos partidos.
- **Directos:** la mayoría de los cruces no tienen enfrentamientos recientes con estadísticas (0–1); la ficha lo dice.
- **Jugadores:** 14 partidos-equipo de 180 sin tabla de jugadores (Flashscore no la publica para esas ligas/copas o no cargó); esos jugadores quedan con menos de 10 partidos de historial.
- **Cuotas:** una sola lectura (23-nov 17:21), sin releer; hay que releer ~1 h antes (12:45 y 15:00 Bogotá para la Champions) junto con las alineaciones oficiales.
- **Contexto:** lectura de Flashscore (tabla, bajas, previa resumida con palabras propias); los criterios de contexto son reglas generales sin resultados verificados.

## Cómo se recogió (prueba del método nuevo, 23-nov)
Betano y el historial de equipos por feeds (segundos/minutos); goleadores por feeds `df_su` (306 partidos en ≈8 s); tablas de jugadores con iframe + caché de jornadas anteriores (52 de 180 partidos-equipo ya estaban); previas de Flashscore navegando cada partido. Detalle y lecciones: `recoleccion/README.md`.
