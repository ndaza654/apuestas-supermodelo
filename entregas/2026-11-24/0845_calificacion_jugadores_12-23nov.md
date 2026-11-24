# Líneas de jugador calificadas: 12-nov (noche) a 23-nov
**Fecha y hora:** 24-nov-2026, 08:45 (Bogotá). **Fuente:** Flashscore, pestaña Player stats (lectura del 24-nov ~08:20–08:40) y feeds `df_st`/`df_su`. **Cuotas:** las de cada jornada en `registro/lineas.csv` (no se releyeron). **Límites:** ver abajo.

## Enfoque de mercados
Esta entrega no recomienda apuestas: mide cómo le fue a las líneas de jugador que Betano ofreció (todas, cumplan o no el filtro) para decidir cuánta confianza darles. Pesan los mercados donde más líneas hubo: tiros al arco, remates, faltas, entradas y goleador.

## Qué se hizo
- Tablas de jugadores leídas de **63 de 65 partidos** pendientes y verificadas contra los totales del partido: remates, tiros al arco, faltas y goles cuadran en 58 de 62 partidos revisados.
- Calificadas las líneas de jugador de 12-nov (noche), 13, 14, 15, 16, 20, 21, 22 y 23-nov. Total de líneas de jugador de 12–23 nov: 43.562 con resultado («cumplió»/«falló») y 22.720 «nula» (el jugador no jugó; Betano anula).
- Siguen sin calificar: 57 líneas de goleador del 17-nov (América de Cali–Inter de Bogotá y Atl. Nacional–Once Caldas: Flashscore no publica tabla) y 174 líneas de remates/tiros al arco de CFR Cluj–Otelul del 21-nov (la tabla no trae remates). Las líneas de faltas de Tractor–Al Wasl no se califican (la tabla no trae faltas).
- Estudiantes (12-nov noche) y Gimnasia LP–Newell's (23-nov) tuvieron prórroga: sus tablas incluyen el tiempo extra; los «cumplió» de remates/faltas/entradas llevan aviso.

## Cómo le fue al modelo de jugador (12–23 nov, solo quienes jugaron)
| Mercado (lado) | Líneas | Acierto real | p del modelo |
|---|---|---|---|
| Tiros al arco (Más) | 10.982 | 9,7 % | 17,5 % |
| Remates (Más) | 9.506 | 13,7 % | 23,8 % |
| Faltas (Más) | 5.963 | 14,5 % | 23,9 % |
| Entradas (Más) | 5.390 | 17,2 % | 31,5 % |
| Anota (Sí) | 5.027 | 9,0 % | 17,1 % |
| Tarjeta (Sí) | 2.442 | 13,2 % | 17,0 % |
| Anota o asiste (Sí) | 2.011 | 14,3 % | 26,2 % |
| Asiste (Sí) | 1.802 | 6,8 % | 19,2 % |

- **Con todas las líneas juntas el modelo sale inflado**: en p ≥ 50 % acertó el 45,5 % (decía 64,7 %); en p de 35 a 50 %, 24,1 % (decía 41,9 %); en p < 10 %, 1,9 % (decía 5,2 %). Casi todo ese exceso viene de líneas sin alineación (18.961 de 43.562) o sin muestra suficiente (10.222).
- **Las líneas que sí pasan el filtro completo (cumple ≥ 7 de 10 y alineación) son pocas (371) y el modelo les acertó cerca de lo que decía**: remates 74 % real (decía 68 %, n 117), entradas 76 % (76 %, n 91), faltas 68 % (71 %, n 75), tiros al arco 65 % (62 %, n 49). Pero quedan por debajo de la probabilidad que da la cuota (76 %, 86 %, 80 % y 71 %): acertaron mucho y aun así sin ventaja sobre el precio. Muestra pequeña: es una pista, no una prueba.
- **Titular o no pesa mucho**: con alineación probable o confirmada (titular ≈ 0,9) acertaron más que sin alineación: tiros al arco 12,0 % frente a 6,6 %, remates 16,0 % frente a 10,5 %, goleador 11,9 % frente a 6,7 %. Es la regla 1 del repo.
- Tarjeta (13,2 % real frente a 17,0 %) y remates de titulares (16,0 %) son los mercados menos inflados.

## Límites
Flashscore no trae faltas recibidas ni atajadas por jugador (atajadas = las del equipo); «entradas» son las intentadas de Flashscore (Betano cuenta entradas totales: no son idénticas); en prórroga los remates, faltas y entradas no se pueden separar; lo recogido pasa transcrito por el chat y se verifica con hash. El criterio «cumple» y la p del modelo vienen de tipsters y medios sin resultados verificados. Archivos: `jornadas/2026-11-24/calificacion_jugadores/` (LEEME.md, tablas y feeds), `recoleccion/calificar_jugadores_pendientes.py`.
