# Auditoría: qué está flojo en recolección, análisis y apuestas (25-nov-2026 ≈ 12:35 Bogotá)

**Fuente:** `registro/lineas.csv` (líneas calificadas del 12 al 25 nov), `jornadas/*` (notas, árbitro, alineaciones, relectura de cuotas), `registro/analisis_historial_boletos.json` (162 boletos del usuario). **Cuotas:** las de cada jornada. **Límites:** el conteo de árbitro es aproximado (archivo con datos); ROI plano = apostar 1 a cada línea ofrecida, no es lo que el usuario jugó; muestras de partidos pequeñas.

## Recolección
1. **Banderas de contexto casi desaparecieron.** Partidos con alguna bandera (necesita ganar, le sirve el empate, rota, derbi, decisivo, nada en juego) en las notas: 19-nov 10 de 10 · 20-nov 1 de 37 · 21-nov 0 de 40 · 22-nov 0 de 29 · 23-nov 0 de 12 · 24-nov 15 de 19 · 25-nov 3 de 44 · 26-nov 0 de 36. Las notas quedaron narrativas (tabla, ánimo, bajas) y por eso el contexto no se puede medir ni entra bien en los factores del dashboard. *Arreglo propuesto:* plantilla obligatoria por partido (banderas por equipo + `guion` + qué se juega) y un partido sin ella queda «reserva» en el ranking.
2. **Una sola lectura de cuotas la mayoría de los días.** Hay `cambios_cuotas.json` (dos lecturas) en 7 de 17 jornadas. Sin segunda lectura no hay CLV ni se sabe si la cuota que se analizó es la que se jugó. *Arreglo:* relectura ≈ 1 h antes de cada bloque como paso fijo de los partidos que se van a jugar.
3. **Árbitro irregular pese a la regla «siempre».** Con datos (aprox.): 20-nov 18 de 37 · 24-nov 5 de 19 · 25-nov 27 de 44 (otros días 90–100 %). *Arreglo:* el cierre de recolección (`ESTADO.md`) lista cuántos partidos tienen árbitro y bloquea tarjetas de los que no.
4. **Onces oficiales:** 24-nov 9 de 19; 25-nov 16 de 44 (a la mañana). Los mercados de jugador dependen de esto.
5. **Historial de jugadores del 26-nov incompleto** (315 equipo-partido con tabla; ≈ 350 partidos pasados pendientes) — ya declarado.

## Análisis
6. **El modelo calibra, pero no sabe más que el precio.** En 48.597 líneas de equipo el Brier es igual (0,1836 modelo, 0,1836 precio); por bandas de p el acierto real sigue a la p del modelo (p 0,6–0,7 → real 0,640). Es decir, el modelo reproduce al mercado; la información nueva tiene que venir de fuera (contexto leído, onces, árbitro, guion).
7. **Líneas de jugador: el precio es caro y el modelo infla.** Apostando 1 a cada línea de jugador ofrecida: acierto 12,4 % (modelo decía 22,0 %, precio 22,8 %), ROI plano −61,6 % (cuota media 5–11). Excepción por vigilar: tarjeta de jugador +7,5 % (n 2.699, cuota media 9). Las líneas de equipo: Más −9,5 %, Menos −7,5 %. Las líneas de jugador que el usuario eligió salen mejor que el promedio (43 % goleador, 54 % remates), pero son selección propia, no regla.
8. **«Cumple» (X de 10) no separa aciertos de fallos frente al precio** en las líneas del usuario (66 % contra 67 %) y en `lineas.csv` ≈ el precio. El contexto estructurado tampoco se confirmó (`1215_medicion_contexto.md`): por eso importa el guion.
9. **Regularidad ajustada por rival** (aprobada el 23-nov) sigue «sin validar»: ningún análisis la usa todavía.

## Apuestas (162 boletos, 30 ganados, −$149.594, ROI −5,8 %)
10. **La fuga está en los boletos de cuota 5–8:** 59 boletos, $1.148.858 apostados (45 % de todo lo jugado), 7 ganados, −$204.998 (−17,8 %). Los de cuota 3–5 salen en −2,1 % (40 boletos); los de cuota 8+ en +15,3 % pero con 3 ganados de 38 (suerte de pocos aciertos).
11. **Por número de patas:** 1 pata 4 de 14 · 2 patas 8 de 20 (40 %) · 3 patas 7 de 42 · 4 patas 6 de 39. El salto fuerte está de 2 a 3 patas.
12. **Pérdidas:** 45 % por una sola pata caída, casi la mitad por una unidad (ya en `CLAUDE.md`). No hay regla de **cuánto apostar por boleto** (stake) ligada a la confianza; no se ha analizado.

## Qué se puede analizar a continuación (propuesto, sin aprobar)
- Tablero de criterios con n e intervalo, y una regla pasa a «activa» solo con n ≥ 25 y el intervalo sin cruzar cero (hoy solo existe para combinadas).
- Calificar el guion todos los días (`calificar_guion.py`, ya creado) y medir cuándo acierta mi lectura: por liga, por tipo de partido, por mercado.
- Analizar stake: monto por boleto frente a patas y cuota.
- Probar «tarjeta de jugador» y «tiros al arco Menos con cumple» en jornadas nuevas, sin recomendarlos aún.
- Medir cuánto vale la relectura de cuotas (CLV) cuando haya dos lecturas por día.
