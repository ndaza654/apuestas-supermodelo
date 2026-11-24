# Calificación de líneas de jugador pendientes (12-nov noche a 23-nov) — hecha el 24-nov-2026 ~08:45 Bogotá

Qué es: las líneas de jugador de `registro/lineas.csv` que habían quedado «sin resultado» porque no se había leído la tabla Player stats de Flashscore.
Cómo: tablas de 63 de 65 partidos con el iframe de Flashscore (`flashscore_jugadores_en_par.js`, lotes `pj_24nov_a..d.json`, hash verificado), goles y tarjetas por los feeds `df_su_1_`, y `python3 recoleccion/calificar_jugadores_pendientes.py jornadas/2026-11-24/calificacion_jugadores --calificar`.

Verificación: la suma por jugador de remates, tiros al arco, faltas y goles de cada tabla se comparó con el total del partido (feed `df_st`): cuadra en 58 de 62 partidos revisados.
Excepciones declaradas:
- CFR Cluj–FC Otelul (21-nov): la tabla no trae remates (0 de 30): sus líneas de remates y tiros al arco (174) vuelven a «sin calificar».
- Tractor Sazi–Al Wasl (23-nov): la tabla no trae faltas (0 de 15): sus líneas de faltas no se califican.
- Estudiantes–Independiente Rivadavia (12-nov noche) y Gimnasia LP–Newell's (23-nov): la tabla incluye prórroga (Betano liquida a 90′): los «cumplió» de remates, tiros al arco, faltas y entradas llevan aviso en `nota`; los «falló» siguen valiendo.
- Sin tabla en Flashscore: América de Cali–Inter de Bogotá y Atl. Nacional–Once Caldas (17-nov): 57 líneas de goleador siguen sin resultado.

Reglas de calificación (las de siempre): «N» = N o más; quien no figura con minutos = «nula» (Betano anula); atajadas, rojas y faltas recibidas no se leen; «entradas» = intentadas de Flashscore (Betano cuenta entradas totales: no son idénticas).
Cambio en `recoleccion/calificar_jugadores.py`: casa variantes de escritura del apellido (Abdullazade/Abdullazada, Khaybulayev/Khaybulaev) y limpia la nota «no jugó» al recalificar.

Archivos: `objetivos.json` (partido → mid), `mid_info.json`, `feeds_24nov.json` (df_st/df_su), `pj_24nov_a..d.json` (tablas), `lote_unido.json`; por jornada, en `jornadas/<día>/resultados/`: `resultados_jug.json`, `incidentes_jug.json`, `mapa_jug.json`, `mids_jug.json`, `jugadores_resultado_pendientes.txt`.
