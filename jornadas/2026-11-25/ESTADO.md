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
