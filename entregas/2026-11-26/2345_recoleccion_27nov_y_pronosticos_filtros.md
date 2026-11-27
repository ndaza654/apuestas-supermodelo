# Recolección completa del 27-nov + página «Pronósticos Flashscore» con filtros

Fecha y hora: 2026-11-26 ~23:45 Bogotá. Cuotas de Betano leídas 26-nov 22:20–22:22 (una sola lectura, sin relectura). Sofascore, ValueStats y Flashscore leídos entre 22:20 y 23:30. Límites al final.

## Qué quedó en el repo (`jornadas/2026-11-27/`)
- 19 partidos con Betano, Sofascore (10 + 10 partidos, directos, once probable, ≈41–76 jugadores por partido), árbitro (ValueStats), notas de contexto + guion, fichas, contexto por mercado, `informe.html`, `analisis.json`, `ranking.md`, `ESTADO.md`, `enfoque.md`.
- 11 previas de Flashscore (6 con apuesta de una persona, 5 generadas con IA solo con probabilidades) y 1 noticia de pronósticos (Premier J12, 6 picks) con su contraste.
- 827 líneas de equipo con «cumple»; 205 sugerencias registradas como pendientes.

## Página «Pronósticos Flashscore» (dashboard)
Filtros funcionales (jornada, tipo previa/noticia, estado pendiente/resuelto/se dio/falló/sin apuesta, origen persona/IA/noticia, mercado, cuota, búsqueda) más «Limpiar filtros»; balance de lo filtrado y «dónde acierta cada fuente»; cada pronóstico con sus argumentos, cuota si la trae y bajas; las previas de IA muestran las probabilidades implícitas; los partidos con y sin Preview quedan en un desplegable por jornada. Probada con Playwright (17 pronósticos; filtros por tipo, estado, origen, mercado y búsqueda responden; 0 errores de consola).

## Estado de la recolección — 27-nov-2026 (leída la noche del 26-nov, Bogotá)

**Una sola lectura de cuotas** (Betano 22:20–22:22 del 26-nov). Sin relectura 1 h antes (el computador del usuario no queda disponible siempre): las cuotas pueden moverse y los onces son «probables».

## Qué se recolectó (19 partidos)
- **Betano:** 19 partidos con todos sus mercados (`betano/`). No se recolectó Azam – Al Ahli Tripoli (Betano trae solo 44 mercados, partido fuera del foco).
- **Sofascore (principal):** forma de los últimos 10 partidos oficiales de cada equipo con estadísticas (todos 10 de 10 salvo Alanyaspor 9 de 10 del local y Rizespor/Kasımpaşa 9 de 10 del visitante: partidos de copa sin estadísticas), hasta 6 directos (Ittihad–Neom 2, Leganés–Sabadell 4), once probable y ausentes. Historial por jugador (≈41–76 jugadores por partido) en `jugadores_sofascore/` para todos los partidos con mercado de jugador de estadística. Macarthur–Melbourne City: Sofascore aún no publica once ni ausentes.
- **Árbitro (ValueStats):** leído con historial en 12 partidos (Madley, Fischer, Mendoza, Delgado, Zwayer, Colombo, Martens, Buquet, Harrington, Sesma, Villalobos, King). **Sin historial en ValueStats:** Sen A. (Alanyaspor–Konyaspor) y Taskinsoy A. B. (Rizespor–Kasımpaşa), árbitros turcos que la página no tiene. **Árbitro no anunciado todavía:** Millonarios–América, Dep. Cali–Bucaramanga, Al-Ittihad–Neom, Al-Kholood–Al-Khaleej, Al-Qadsiah–Al-Fayha. Esos partidos se analizan sin factor de árbitro y se declara.
- **Contexto (notas + guion):** tabla y situación leídas en Flashscore para los 19 (`notas/`). Brest–Paris FC, Rizespor–Kasımpaşa y Macarthur–Melbourne City quedan en «reserva» en el ranking porque no hay factor que pese (situación normal, sin urgencia), no porque no se leyera.
- **Previas de Flashscore:** 11 con Preview. Las escritas por una persona (Premier, Bundesliga, Ligue 1, Serie A, LaLiga, Primera A: 6) traen apuesta; las generadas con IA (Süper Lig, Eredivisie, LaLiga2, Championship: 5) solo probabilidades implícitas. Sin Preview no se recolecta.
- **Noticias de pronósticos:** 1 (Premier League, fecha 12, Apuestas CO: 6 picks). Contraste con ficha y previa en `noticias/`.

## Límites
- Sofascore/Flashscore no traen «faltas recibidas»; las entradas no son idénticas a las de Betano.
- Onces: probables de Sofascore (sin oficial). Revisar 1 h antes si el usuario está conectado.
- Fueras de juego, tarjetas y demás cuentan como los define Betano (Opta); aquí son las de Sofascore.
- `registro/lineas.csv` pasa de 50 MB (GitHub avisa; sigue funcionando).
- Pendientes de calificar: noche del 26-nov (Pachuca–Chivas, León–Cruz Azul).

## Enfoque de mercados — viernes 27-nov (19 partidos, una sola lectura de cuotas)

Los mercados que pesan hoy salen del contexto de cada partido, no solo de la regularidad:

- **Tarjetas altas por urgencia o árbitro:** Dep. Cali–Bucaramanga (7,0 esperadas; ambos con 1 punto en el cuadrangular), Millonarios–América (6,5; América con 24 amarillas en sus últimos 3 de visitante), Leganés–Sabadell (7,0; Villalobos 5,9 amarillas por partido) y Alanyaspor–Konyaspor (4,5; duelo de zona baja, árbitro sin historial).
- **Goles altos:** Groningen–Willem II (4,4 esperados; Willem II recibe 3,2 por partido), Columbus–Inter Miami (3,9; Miami debe ganar), Werder–Gladbach (3,65; Gladbach con 10 bajas) y Al-Kholood–Al-Khaleej (3,7). Goles bajos: Dep. Cali–Bucaramanga (2,25) y Alanyaspor–Konyaspor (2,4).
- **Córners:** Fluminense–Cruzeiro (10,8) y RSL–Vancouver (10,95) arriba; Millonarios–América (8,3), Brest–Paris FC (8,2) y Dep. Cali–Bucaramanga (7,95) abajo. Se tratan como cualquier mercado, sin exigir cuota alta.
- **Remates y tiros al arco:** el local domina en Groningen, Werder y Qadsiah; Middlesbrough y Bologna dominan de visitante. Remates Menos solo con once oficial.
- **Resultado / ambos marcan:** Venezia–Bologna (ambos no: Venezia no marcó en 4 de sus últimos 5), Werder y ambos (previa), Millonarios–América (ambos sí, 12 de 16 de Millonarios).
- **Contexto que contradice los números:** Forest–Chelsea: la previa de Flashscore pide «ambos marcan: No» y la noticia «Más de 2,5»; no son la misma lectura.

Límites: una sola lectura de cuotas, onces probables, 5 árbitros sin anunciar y 2 sin historial. Los criterios de tipsters y medios no tienen resultados verificados.
