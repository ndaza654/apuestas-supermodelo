# Cambios en los mercados de Betano.co — sábado 21-nov-2026, 09:52 (Bogotá)

**Fecha/hora de lectura:** 21-nov-2026 09:52 (14:52Z). **Fuente:** API de Betano.co leída desde el navegador integrado (`/api/sports/upcoming/calendar/FOOT/` para el calendario y `/api/cuotas-de-partido/<partido>/?bt=2..13` para las familias). Comparado con las fotos de anoche (`calendario_betano_2250.json`, 22:46 del 20-nov; `mercados_top40_2300.json`, 23:05). Archivos de hoy: `jornadas/2026-11-21/calendario_betano_0950.json`, `mercados_top40_0950.json`. No hay fotos intermedias.

## Límites (léelos primero)
- **El calendario de hoy solo trae los partidos que aún no empiezan** (588; anoche eran 1.116). Los 581 que ya iniciaron o terminaron antes de las 09:52 salen del listado, no «desaparecieron»: no se pueden comparar. Comparación válida = los **535 partidos presentes en ambas fotos**.
- De los **40 del top de anoche, 9 ya no están en el calendario (ya empezaron/terminaron) y no se releyeron**: Man City–Fulham, Alavés–Dep. La Coruña, Como–Cagliari, Lazio–Lecce, Leverkusen–Paderborn, Frankfurt–Hoffenheim, Union Berlin–Leipzig, Gladbach–Dortmund, Elversberg–Friburgo. Se compararon **31**.
- «Leídos» = mercados distintos que entrega la API (puede variar unos pocos por cambios de alineación/jugadores). La columna `resultado` valía 0 anoche en todos: era un artefacto del clasificador de anoche, **no** es una familia nueva (hoy 26–28 en todos); se ignora.
- 53 partidos del calendario de hoy no estaban anoche (sin url/slug guardado): ver abajo. 17 partidos de anoche con hora ≥10:00 ya no aparecen (p. ej. Sheffield Utd–Watford, Dunfermline–Morton, Teuta–Laci): quitados del listado o ya en juego; no se sabe cuál.
- Solo análisis de datos; ninguna apuesta.

## Resumen
| | Partidos | Mercados |
|---|---|---|
| Presentes en ambas fotos | 535 | 76.159 → 76.477 (+318 netos) |
| **Subieron** | **64** | **+735** |
| Bajaron | 39 | −417 |
| Sin cambio | 432 | — |
| Partidos con ≥500 mercados | 58 → 58 | ninguno cruzó 500 |
| Nuevos en el calendario (no estaban anoche) | 53 | 1.668 mercados (22–44 c/u) |

## Partidos que más subieron (top 15)
| # | Partido | Liga | Anoche | Hoy | Δ |
|---|---|---|---|---|---|
| 1 | AFC Bournemouth – Nottingham Forest | Premier League | 855 | 911 | +56 |
| 2 | Coventry City – Crystal Palace | Premier League | 861 | 915 | +54 |
| 3 | Newcastle – Arsenal | Premier League | 908 | 959 | +51 |
| 4 | Tottenham – Ipswich | Premier League | 956 | 1.005 | +49 |
| 5 | Aston Villa – Sunderland | Premier League | 1.006 | 1.052 | +46 |
| 6 | Chelsea – Leeds | Premier League | 920 | 960 | +40 |
| 7 | Kalamata – AEK Atenas | Super League 1 (Grecia) | 721 | 760 | +39 |
| 8 | Tigres UANL – Club América | Liga MX | 580 | 616 | +36 |
| 9 | Wellington Phoenix – Macarthur | A-League | 508 | 540 | +32 |
| 10 | OGC Niza – PSG | Ligue 1 | 921 | 952 | +31 |
| 11 | Parma – Roma | Serie A | 833 | 855 | +22 |
| 12 | Sevilla – Betis | LaLiga | 806 | 828 | +22 |
| 13 | Schalke 04 – Stuttgart | Bundesliga | 809 | 830 | +21 |
| 14 | Rayo Vallecano – Valencia | LaLiga | 819 | 839 | +20 |
| 15 | Real Madrid – Celta | LaLiga | 826 | 846 | +20 |

(Δ de los 6 partidos de Premier: +296 mercados, el 40 % de todo el aumento.)

## Ligas con más aumento (suma de Δ, partidos que subieron)
| Liga | Partidos que subieron | Δ mercados |
|---|---|---|
| Premier League | 6 | +296 |
| LaLiga | 3 | +62 |
| Liga MX | 4 | +57 |
| Championship | 5 | +53 |
| Super League 1 (Grecia) | 1 | +39 |
| Ligue 1 | 5 | +38 |
| A-League | 1 | +32 |
| Serie A | 2 | +25 |
| Bundesliga | 1 | +21 |
| 1A Pro League (Bélgica) | 3 | +17 |

## Familias de mercado en los 31 releídos del top 40
**Los 11 que anoche no tenían mercados de jugador (rank 1, 29–34, 37–40):**
| Partido | Anoche (remates / al arco / asist.) | Hoy | ¿Ya tiene? |
|---|---|---|---|
| Celtic – St Mirren | 4 / 5 / 1 | 74 / 74 / 36 | **Sí, apareció** |
| Falkirk – St Johnstone | 4 / 5 / 1 | 84 / 85 / 41 | **Sí, apareció** |
| CFR Cluj – Otelul Galati | 4 / 5 / 1 | 80 / 81 / 33 | **Sí, apareció** |
| Hibernian – Dundee United | 4 / 5 / 1 | 80 / 81 / 39 | **Sí, apareció** |
| Atlético MG – Boca Juniors | 4 / 5 / 1 | 4 / 5 / 1 | No |
| Defensa y Justicia – Barracas Central | 4 / 5 / 1 | 4 / 5 / 1 | No |
| Kalamata – AEK Atenas | 4 / 5 / 1 | 4 / 5 / 1 | No (sube +39 en otras familias) |
| Motherwell – Rangers | 4 / 5 / 1 | 4 / 5 / 1 | No |
| Argentinos – Independiente | 4 / 5 / 1 | 4 / 5 / 1 | No |
| Dundee – Hearts | 4 / 5 / 1 | 4 / 5 / 1 | No |
| Dinamo Bucarest – Petrolul | 4 / 5 / 1 | 4 / 5 / 1 | No |

→ **4 de 11 ya tienen mercados de jugador de estadística; 7 siguen sin ellos** (los 4–5 que aparecen son mercados de equipo/primer jugador, no estadística por jugador).
Además, en esos 4 partidos subieron goleador (+3 c/u), tarjetas (+1 en 3 de ellos) y goles (+1). **Ojo:** el total anunciado en el calendario de esos 4 (y Kilmarnock–Aberdeen) **bajó** (p. ej. Celtic 688 → 545) aunque se añadieron ~190 mercados de jugador: Betano cambió lo que cuenta en `totalMarketsAvailable`; para ellos el «m» del calendario no sirve como señal de «subió/bajó».

**Otros cambios de familia en el top (con mercados de jugador ya presentes):**
- Real Madrid – Celta: +16 en h2h (10→16), +2 a +1 por jugador en remates/arco/entradas/faltas/asist./pases/fuera.
- Newcastle – Arsenal: +4 remates, +4 al arco, +2 entradas, +2 asist. (más jugadores listados).
- Niza – PSG: +2 remates/al arco/faltas, +1 entradas/asist./pases/fuera.
- Palmeiras – Flamengo: córners 25 → 27.
- Sevilla – Betis: entradas 36 → 38.
- Bajaron un poco (−1 a −4 por familia de jugador, probable salida de algún jugador de la lista): Aston Villa–Sunderland, Tottenham–Ipswich, Chelsea–Leeds, Coventry–Palace, Rayo–Valencia, Bahía–Coritiba.
- Sin cambio de familias: Napoli–Torino, Lille–Lyon, Lens–Toulouse, Mónaco–Auxerre, Estrasburgo–Brest, Chapecoense–Cruzeiro y los 7 sin jugadores.

## ¿Entró alguien al top 40 o cruzó 500?
- Ningún partido pasó de <500 a ≥500; los partidos con ≥500 siguen siendo 58.
- Nadie con más de 652 mercados (corte anoche) quedó fuera del top; el corte de hoy sería ~637 porque 9 del top ya empezaron. Siguientes en la fila: Bohemians 1905–Viktoria Plzen 637, Telstar–Zwolle 634, Pumas–Monterrey 628, Kocaelispor–Fenerbahçe 624, Pachuca–Toluca 619, Genk–La Louvière 618.

## Ligas con partidos nuevos en el calendario (53)
| País / liga | Partidos nuevos |
|---|---|
| España — Tercera RFEF | 11 |
| Inglaterra — Isthmian Div. 1 Norte / Southern / Northern | 8 |
| Suiza — 1. Liga Classic / Promotion League | 7 |
| Polonia — III Liga | 5 |
| Bélgica — Tweede Afdeling | 5 |
| España — Divisiones Regionales / Honor Juvenil | 3 |
| Senegal — Ligue 1 / Ligue 2 | 2 |
| El Salvador — Reserva | 2 |
| México — Liga Premier | 2 |
| Nueva Zelanda — National League (F) | 2 |
| Portugal, Países Bajos Sub-21, Brasil Sub-20, Austria (F), Puerto Rico | 1 c/u |

Todos son ligas menores con 22–44 mercados anunciados (sin mercados de jugador): no cambian el análisis.
