# Estado de la recolección — 27-nov-2026 (leída la noche del 26-nov, Bogotá)

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
