# Balance del domingo 15-nov-2026 (leído ~17:15–17:45 Bogotá)

- **Fuentes y hora:** boletos de Betano → Mis apuestas → Resueltas (solo lectura, ~17:15); resultados de Flashscore (feed del partido, 17:25; crudo `jornadas/2026-11-15/resultados/flashscore_raw_1725.json`, sha256 8b5c82c2097a) y estadísticas por jugador de Flashscore (17:45, 5 partidos). Cuotas de mis líneas: las leídas por el pipeline (`registro/lineas.csv`); las del 16:00 en vivo, las leídas en Betano ≈15:44–15:49.
- **Límites:** Panamá–Curazao (18:00) pendiente (90 líneas de equipo, 36 de jugador, 11 sugerencias). 396 líneas de jugador (goleador y tarjeta) de 7 partidos sin calificar (no se leyó el detalle por jugador). Tarjetas de Jamaica–México (14-nov) no vienen en el feed. Flashscore no trae faltas recibidas; «entradas» no equivale a las de Betano. La cuota de las combinadas 90–92 es el producto de las cuotas de sus selecciones (Betano no la muestra). Un solo día, líneas del mismo partido correlacionadas: son pistas, no pruebas.

## Tus apuestas
5 boletos (n.º 90–94), $72.500 apostados, $0 devueltos, **neto −$72.500 (19,6 u)**. Además los BB del sábado n.º 88 (Chapecoense) y 89 (Banfield) se liquidaron Perdida (−$15.000, anotados en el balance del 14-nov).
- n.º 90 combinada de 4 ($8.500, cuota ≈4,62): cayeron Tenerife–Ceuta tarjetas Más 4.5 (4 pts) y Letonia Más 0.5 goles (0-0).
- n.º 91 combinada de 4 BB ($6.500, ≈24): cayeron Finlandia -5.5 córners (ganó por 4), Eldense Más 3.5 córners (1) y Eibar–Cádiz Más 7.5 córners (6).
- n.º 92 combinada de 4 BB ($7.500, ≈21,1): 9 de 11 patas; cayeron Tonali 1+ remates (0) y Červ 1+ remates (0).
- n.º 93 BB España–Inglaterra ($35.000 @5,80): cayó solo Remates totales Menos 29.5 (hubo 32).
- n.º 94 BB Bélgica–Italia ($15.000 @5,40): cayó solo De Ketelaere 1+ a puerta (0).
- Patas: 22 de 31 (71 %); equipo 14 de 20, jugador 8 de 11.

## Mis sugerencias del día (151 en total: 85 se dieron, 55 fallaron, 11 pendientes por Panamá–Curazao)
| Entrega | Resultado | ROI plano |
|---|---|---|
| Informe de la jornada, protección (< 1,50) | 27 de 32 | +7 % |
| Informe, sencillas 1,50–1,99 | 5 de 10 | −20 % |
| Informe, combinadas de 2 patas / lotería | 2 de 3 / 1 de 1 | +3 % / +95 % |
| Tu estrategia (01:45), sencillas | 39 de 54 | +17 % |
| Tu estrategia, combinadas | 0 de 7 (3 pendientes) | −100 % |
| Sugerencias 11:45 (partidos de las 12:00 y 12:30) | 3 de 5 | −11 % |
| Bet Builders 14:00 | 1 de 4 | −33 % |
| **En vivo 16:00 (2.º tiempo)** | **7 de 24** | **−49 %** |

**En vivo:** en las 20 líneas de equipo mi probabilidad media era 78 % y ocurrió el 25 %; la de Betano era 50 % (Brier: mío 0,47; Betano 0,24; mezcla 0,34). Las 9 de España–Inglaterra cayeron juntas (España iba 0-1 y en el 2T hizo 19 remates, 7 a puerta y 4 córners). Jugadores en vivo: Güler 4+ remates y Porro 4+ faltas sí; Bellingham 3+ a puerta y Calhanoglu 2+ remates no.

## Criterios (líneas de equipo, 12 partidos terminados)
- Todas con cuota: 817 de 1.652 (49 %), ROI plano −10 %.
- Tu filtro (cuota 1,40–2,20, cumple ≥ 7 de 10, colchón > 0): 33 de 48 (69 %) contra 60 % del modelo, ROI plano +10 %. «No cumple» (misma cuota): 206 de 400 (52 %), −10 %.
- Por mercado (mismo filtro): tarjetas Menos 5/5, goles Menos 8/9, remates Menos 0/5. Por partido: España–Inglaterra 1 de 6; Croacia y Francia 8 de 10.
- Modelo pre-partido bien calibrado (1.434 líneas): 11 % → 9 %, 50 % → 50 %, 89 % → 90 %.
- Corrección técnica: el casador de nombres no reconocía la «ı» turca (Bardakcı, Yılmaz, Kadıoğlu); arreglado en `recoleccion/calificar_jugadores.py`.

Detalle interactivo: `1735_balance-15nov.html` (filtros por partido, mercado, lado, cuota, resultado; pestañas Resumen, Líneas, Tus apuestas, Pendientes, Conclusiones). Balance del 14-nov actualizado con los boletos 88–89: `1735_balance-14nov-actualizado.html`.
