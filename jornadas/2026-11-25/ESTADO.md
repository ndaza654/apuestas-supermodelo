# Estado de la recolección · jornada del 25-nov-2026
Leída la noche del 24-nov (Bogotá). Favoritos de Flashscore: 35 partidos = Champions League (9), UEFA Youth League (9), J1 Japón (7) y Champions asiática (10).
Mercados: leídos primero de Betano (`betano/<clave>.json`); lo que Betano no ofrece no se analizó.

## Cobertura por bloque
| Bloque | Betano | Historial de equipos (10) + directos | Árbitro | Alineaciones y bajas | Tabla y contexto | Historial por jugador |
|---|---|---|---|---|---|---|
| Champions (9) | 35/35 leídos | 9/9 | **9/9** (ValueStats) | 9/9 «probables» (oficiales ~1 h antes) | 9/9 | 72 de 91 partidos-equipo leídos (ver abajo) |
| Youth League (9) | sí | 9/9 | 8/9 (Kuzma L. sin página en ValueStats) | no publicada | 9/9 | no se pide (solo 1X2/córners/goles) |
| J1 (7) | sí | 7/7 | **0/7: no anunciado todavía** | no publicada | 7/7 | no se pide |
| ACL (10) | sí | 10/10 | 3/10 (Gamba, Kashima, Melbourne); 7 no anunciados | no publicada | 10/10 | no se pide |

## Historial por jugador (Champions): cobertura real
Detalle por equipo en `jugadores/LEEME.md`. De los 10 partidos de cada equipo: **completos** Atlético, Liverpool, Barcelona, Fenerbahce, Inter, Stuttgart, Lille, Bayern, PSG, Roma, Man Utd; **9 de 10** Viking, Brugge, Slavia, Villarreal, Sporting.
**Huecos reales:** Sabah FC 3 de 10 y Shakhtar 3 de 10 — Flashscore no publica «Player stats» de las ligas de Azerbaiyán y Ucrania (y copas menores). Los mercados de jugador de Sabah y Shakhtar no se recomiendan por historial, salvo con el poco que hay (declarar siempre n). Otros partidos sin tabla: Madla–Viking, Lokeren–Brugge, Unión da Serra–Sporting, Manacor–Villarreal, Brno–Slavia.
Límites que se declaran: la tabla en inglés de Flashscore sí trae faltas recibidas (posición 13 de cada fila); «entradas» ganadas/intentadas ≠ entradas totales de Betano; lo recogido pasa transcrito por el chat y se verifica con hash (jugadores 1366217621, contexto 332066942 y 3239356243: todos OK).

## Lo que NO se pudo leer o queda pendiente
- **Árbitro:** J1 (7) y 7 de ACL no anunciados (releer `df_sui_1_<mid>` ~1 h antes y completar ValueStats). Kuzma L. (Youth, Atlético–Viking) sin historial en ValueStats. Los análisis de tarjetas de esos partidos deben decirlo.
- **Bajas sin lado:** Flashscore no marca de qué equipo es cada baja en el texto; las que no calzan con el historial de jugadores quedan en `alineaciones/<clave>.json → bajas_sin_lado` (por ejemplo Bradley y Nallo de Liverpool): no se asigna lado a ciegas.
- **Alineaciones oficiales y cuotas:** releer ~1 h antes de cada partido (Champions 12:45 y 15:00 Bogotá). Antes de volver a leer Betano, copiar `betano/` a `betano_previo/` (regla de «Releer cuotas»).
- **Goleador:** hay mercados `an/aoa` en J1, ACL y Youth; no se trajo historial de goles por jugador de esos partidos (el usuario no ha dicho que el goleador importe en esta jornada). Pendiente si lo pide.
- **Contexto «animo/necesita ganar/rotación»:** solo hechos leídos (tabla, forma, bajas, zona de la tabla). Sin lectura de prensa más allá de la previa de Flashscore (AFC no tiene previa).

## Errores de método encontrados (y arreglos)
Ver `recoleccion/README.md → «Lecciones del 24-nov (recolección del 25-nov)»`.

---
# Segunda tanda (agregada el 25-nov 00:00–00:40 Bogotá): 9 partidos de la noche
Championship (Bolton–West Brom, Burnley–Birmingham, Watford–Blackburn, 14:45), Brasileirão (Atlético-MG–Corinthians, 18:00), Colombia (Santa Fe–Once Caldas 18:20, Nacional–Medellín 20:30), Argentina (Boca–Ind. Rivadavia, 19:00), Liga MX (Toluca–Atlas 20:00; Monterrey–América: Betano 22:00, Flashscore 22:10).

| Bloque | Betano (mercados leídos primero) | Equipos (10 + directos) | Árbitro | Jugadores (10 de 10) | Onces/bajas | Tabla/contexto |
|---|---|---|---|---|---|---|
| Championship ×3 | goles, córners, tarjetas, remates, tiros al arco, jugador (remates, arco, asistencia, anota, tarjeta) | 3/3 | 3/3 (Bell E. corregido) | 6/6 equipos 10 de 10 | probables + bajas | 3/3 |
| Brasileirão | igual + atajadas | 1/1 | 1/1 | 2/2 (Corinthians: 3 partidos de caché releídos) | probables + bajas | 1/1 |
| Boca | goles, córners, tarjetas, remates; jugador casi nada (1 línea por estadística) | 1/1 | 1/1 | 2/2 | probables + bajas | sin tabla (playoff: octavos a partido único) |
| Colombia ×2 | goles, córners, 1 línea de tarjetas, goleador | 2/2 | 2/2 | no se pide | sin once publicado | 2/2 (cuadrangular) |
| Liga MX ×2 | goles, córners, goleador (sin tarjetas ni jugador a esta hora) | 2/2 | 0/2: no anunciados | no se pide hoy (Liga MX trae jugador en el 50 % de los partidos vistos: releer al mediodía) | probables; bajas sin lado | sin tabla (playoff: ida de cuartos) |

Hashes verificados: Betano 2043207391, Flashscore 926656371, árbitros 3784910166, jugadores 2884050065, contexto 1856287718 (y la relectura de Corinthians, jug25c, 3031171621).

## Controles hechos (y lo que encontraron)
- **Remates por jugador contra el total del equipo:** cuadraban en 97 de 100 partidos-equipo; los 3 que no eran de Corinthians, venían de la caché de una lectura anterior (faltaban de 1 a 4 remates) y **se releyeron: ahora 100 de 100**.
- **Nombres Betano–Flashscore:** los 9 coinciden en local/visitante; Monterrey–América difiere en la hora (22:00 contra 22:10).
- **Árbitros ValueStats:** se encontró un bug (el filtro por inicial estaba dentro de un comentario): Bell E. salía como James Bell. Corregido; auditoría de todo el repo: 2 mal emparejados del 22-nov (Sepúlveda M. → Galaz Sepúlveda; Dóvalo P. → Sandoval), marcados con `emparejamiento_invalido`.
- **Tarjetas por equipo:** en 7 partidos-equipo de Championship/Liga MX Flashscore no trae la fila de tarjetas (suele ser 0-0); queda «sin dato», no se pone 0.
- **Colombia:** faltas/fueras/saques ausentes en 1–3 partidos de Copa Colombia por equipo (Betano no ofrece esos mercados en Colombia: sin efecto).

## Pendiente de la segunda tanda
- Árbitros de Toluca–Atlas y Monterrey–América (sin anunciar); onces oficiales ~1 h antes; releer Betano al mediodía (Liga MX puede abrir mercados de jugador: entonces traer su historial).
- Bajas «sin lado» en Liga MX (sin historial de jugadores para casar nombres) y algunas de Championship: ver `alineaciones/<clave>.json`.
