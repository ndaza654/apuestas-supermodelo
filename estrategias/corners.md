# Córners (total del partido, por equipo, 1T/2T)

**Regla del usuario (25-nov-2026):** los córners entran a cualquier cuota (1,35, 1,40, 1,50…), Más o Menos, total o de equipo, sin exigir 8–9 de 10. Se analizan por **cómo se va a jugar el partido**, no solo por promedios.

## Lectura obligatoria por partido (en este orden)
| # | Pregunta | Para Más de un equipo / total | Para Menos | Dato en el repo | Origen |
|---|---|---|---|---|---|
| 1 | **¿Quién tendrá la pelota y quién defenderá?** (dominio esperado: cuotas 1X2, xG y remates esperados, diferencia de nivel) | el dominador acumula córners | el que defiende y contragolpea saca pocos | xG, remates y tiros al arco en la ficha; cuota 1X2 en `betano/`; **posesión: falta** (el feed de estadísticas la trae, no se recolecta) | tipster + lección 4-nov |
| 2 | **Estilo de ataque:** bandas y centros contra bloque bajo, extremos y laterales que llegan al fondo | equipo de centros contra rival encerrado | equipo de juego interior/combinativo o de contragolpe directo | **centros: falta** (feed `Crosses`); leer en la previa/crónicas | tipster |
| 3 | **El rival, ¿concede córners a favoritos o se cierra bien?** (córners concedidos por el rival, ajustados por el nivel de los rivales que enfrentó) | rival que concede mucho | rival que concede poco | `ficha.promedios.*_en_contra`; `recoleccion/ficha_ajustada.py` (ajuste por rival, sin validar) | tipster |
| 4 | **Marcador esperado y gol temprano:** el favorito que se adelanta baja el ritmo; el que va perdiendo empuja y saca córners; partidos de marcador muy abierto dan menos córners que los trabados con presión | equipo que necesita remontar / partido parejo | favorito con gol temprano / partido que se rompe | cuotas de goles y resultado; notas de contexto | tipster |
| 5 | **Partido muy desigual:** no suponer total alto; **sumar el esperado de cada equipo**. Más córners TOTALES con un dominador claro suele fallar; los córners DEL dominador sí tienen sentido | córners del dominador | total | esperado por equipo en la ficha | lección 4-nov (Leipzig–City, Dortmund–Betis 8 y 6–7 córners con xG alto) |
| 6 | **Alineación:** laterales, extremos y rematadores titulares; cobradores de balón parado; bajas del once | titulares ofensivos de banda | bajas de extremos/laterales o rotación | `alineaciones/<clave>.json` (probables/oficiales) | tipster |
| 7 | **Qué se juegan:** necesita ganar (+), le sirve el empate (−), rotación (−), derbi | necesita ganar | le sirve el empate / rota | `notas/<clave>.json` (banderas) | usuario + tipster |
| 8 | **Clima y cancha** (lluvia, viento, césped pesado) | — | lluvia fuerte y cancha pesada | falta (leer a mano si hay dato) | tipster |
| 9 | **Liga y nivel:** los promedios de una liga débil no viajan a Champions/Europa; equipo fuerte de liga débil sale inflado | — | — | `registro/mercados_betano_por_liga.*`, comp en la ficha | lección 8-nov |
| 10 | **Regularidad y directos** (X de 10 L/V, directos) | cumple ≥ 7 de 10 en ambos | igual | ficha | usuario |
| 11 | **Línea y cuota** | informar p, EV | informar p, EV | `lineas.csv` | — |

## Salida por partido (en `agentes/<partido>_corners.md`)
1. «Lectura de córners»: los 11 puntos con su dato y el signo (+ / − / sin dato).
2. **Predicción comprobable** (va al `guion` de la nota, ej. `{"tipo":"mas_corners","equipo":"local"}` y/o `{"tipo":"corners_mas","linea":9.5}`): se califica después con el resultado.
3. Las líneas de Betano, todas, con cuota, X de 10, esperado y colchón; sin excluir ninguna.

## Lo que sabemos (medición, para no engañarnos)
- Córners: 51 % de acierto en tus boletos (Más 48 %); el modelo no le gana al precio (Brier 0,1683 contra 0,1678 en 16.845 líneas).
- Los puntos 1–9 son **criterios de tipsters sin verificar**; el guion de córners por partido sirve para medir si mi lectura acierta (equipo con más córners, total).

## Pendiente de recolección (para que los puntos 1 y 2 tengan dato)
Añadir al extractor de Flashscore **posesión** y **centros** (y xG por equipo si no está) de los últimos 10 partidos de cada equipo.

## Estrategia del video @ingenieroanalista10 (cuenta nueva; recibido 25-nov-2026) — «4 filtros para partidos con muchos córners»
Origen: video del usuario, transcrito con Whisper small (puede haber errores en cifras). **Tipster sin resultados verificados.** Sus 4 filtros:
1. **Centros al área:** equipos que promedian > 20 centros por partido; mejor si ambos > 25 (cita estudios de Mundiales con relación «moderada y significativa» entre centros y córners; no verificado).
2. **Dominio territorial:** no importa la posesión sino dónde se tiene: > ≈ 55 % de las acciones en campo rival → más centros, remates bloqueados y córners.
3. **Favorito con intención ofensiva** (necesita ganar); evitar partidos intrascendentes.
4. **Proyección de 9–10 córners** (promedio habitual del fútbol profesional).
Extra en vivo: favorito empatando o perdiendo → empuja, más centros y córners. Ligas que favorecen los córners suman.
**Cómo encaja con la lectura de arriba:** filtro 1 = punto 2; filtro 2 = punto 1 (dominio); filtro 3 = puntos 4 y 7; filtro 4 = línea del punto 11.
**Medición con el repo (165 partidos con estadísticas de Flashscore, 330 equipo-partido; descriptiva, no predictiva):** centros ↔ córners propios r = 0,66; toques en el área rival r = 0,58; remates r = 0,60; posesión r = 0,46 (la posesión sirve menos que el dónde, como dice el video). Equipos con > 20 centros sacaron 7,1 córners contra 4,0 los de ≤ 20; partidos con ambos > 20 centros: 11,9 córners (n 7) contra 9,8 el resto. **Qué NO prueba:** son los centros *del mismo partido* (no se conocen antes) y el equipo que centra mucho suele ser el fuerte; falta medir si el promedio de centros de los últimos 10 predice los córners del siguiente. Dato que falta en la recolección: centros y toques en el área de los últimos 10 (el feed `df_st` los trae: `Crosses`, `Touches in opposition box`, `Ball possession`).
