# Jornada dom 22-nov-2026 · estado de la recolección (22-nov ~11:00 Bogotá)

Selección: los 29 partidos de «Favoritos» de Flashscore del usuario (el 30.º del contador no se veía en las capturas; Chicago Fire–Charlotte y Nashville–Cincinnati existen en Betano pero no estaban en las capturas: no se recogieron). Solo recolección: no se entrega análisis.

## Hecho
- **Betano (29/29):** lectura completa uniendo todas las pestañas de mercados (la pestaña «Todo» recorta y no trae los de jugador): hasta ~690 mercados por partido (`raw/`, `betano/`). Mercados extra de jugador leídos y guardados crudos en `betano_extra/<partido>.json` (faltas ganadas = recibidas, fueras de juego, pases, remates y tiros al arco de 1T, «2+ goles»; hash verificado). Cuotas leídas 22-nov ~02:30–09:00.
- **Flashscore forma 10+10 y directos (hasta 6) (29/29)**, `flashscore/`.
- **Historial por jugador:** 387 de 394 partidos pasados leídos (`jugadores/LEEME.md`, 22 partidos con mercado de jugador de estadística; 10 de 10 en la mayoría). Faltan: Copa del Rey ×5, EFL Cup (Liverpool–Brighton) y Angers–Nice del 8-nov (Flashscore no tiene tabla de jugadores de ese partido; releído 22-nov). Los partidos solo con goleador/tarjeta (Chile ×3, Córdoba–Oviedo, Gijón, Vancouver, Querétaro) no necesitan historial y no se trajo.
- **Árbitro: 26/29** con historial en ValueStats. Sin dato: Hernández A., Mera C. D., Pérez S. (sin página); Badstubner con 1 solo partido.
- **Alineaciones probables y bajas: 26/29** (los 3 de Chile no las publican aún). Oficiales: relectura ≈ 1 h antes de cada partido.
- **Tabla y qué se juega: 25/29** (los 4 de playoffs/copas no tienen tabla). Previa de Flashscore solo en Liverpool–Man United y unos pocos más; el resto trae únicamente forma.
- Pipeline corrido (`correr_jornada.py`): fichas, modelo, contexto, `informe.html`, `registro/lineas.csv`.

## Límites (declarados)
- **Betano no ofrece mercados de partido (faltas, fueras, remates, tiros al arco…) en 7 partidos:** Córdoba–Oviedo, Gijón–Las Palmas, Chile ×3, Vancouver–Salt Lake, Querétaro–Necaxa (158–196 mercados; solo goles/córners/tarjetas, y de jugador solo goleador). Rosario–Gimnasia, River–Lanús e Instituto–Huracán: estadística de jugador de un solo jugador. Bragantino, Fluminense y Guadalajara sin entradas/faltas de jugador. Puede ampliarse cerca del partido: se vuelve a leer.
- Faltas recibidas, fueras de juego, pases y 1T de jugador están recogidos (cuotas) pero **el pipeline todavía no los analiza** (el historial por jugador trae faltas recibidas, pero no está cableado a ficha, calificación ni dashboard): no se recomiendan hasta cablearlos.
- Flashscore no trae «faltas recibidas» exactas; «entradas» = ganadas/intentadas de Flashscore, Betano cuenta entradas totales; atajadas de la pestaña de portero: 51 % exactas, 70 % ±1 frente a tiros al arco rival − goles.
- Lo recogido pasa transcrito por el chat y se verifica con hash.
- Situación: hechos leídos en `notas/` (tabla, forma, bajas); sin juicio de importancia/motivación todavía, por eso el ranking sale «reserva».
- Criterios de tipsters sin resultados verificados.

## Falta
- Relectura de cuotas y onces oficiales ≈ 1 h antes de cada partido (con `cambios_cuotas.json`); análisis cuando el usuario lo pida.
