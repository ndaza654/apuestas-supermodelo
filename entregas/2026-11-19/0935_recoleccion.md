# Recolección del 19-nov-2026 (solo datos, sin análisis)

Fecha y hora: jueves 19-nov-2026, 09:35 Bogotá. Cuotas de Betano leídas ≈08:10 Bogotá. Límites: ver abajo y `jornadas/2026-11-19/ESTADO.md` (copia íntegra del estado).

Recolección hecha entre ≈08:00 y 09:30 Bogotá (cuotas de Betano leídas ≈08:10; los partidos empiezan 12:45). **No se entregó análisis ni sugerencias**: `correr_jornada.py` corrió para comprobar que todo cuadra (fichas, contexto, registro e informe quedan en el repo), pero las sugerencias no se han enviado ni agregado a `registro/sugerencias.csv`. 10 partidos.

## Qué se recogió y dónde
| Dato | Carpeta | Cobertura |
|---|---|---|
| Betano: líneas, jugadores, parejas, mercados únicos (1X2, doble oportunidad, ambos marcan…) | `betano/`, `raw/bet_*.txt` | 10 partidos |
| Flashscore: últimos 10 de cada equipo con estadísticas de equipo, directos (hasta 6), árbitro anunciado | `flashscore/<clave>.json` | 10 partidos. Austria F: 4 de 10 con estadísticas; Servette F: 5 de 10; sin directos en los 5 femeninos |
| **Árbitro (nuevo, regla fija)** | `arbitros/<clave>.json` → `ficha.arbitro` | 10 de 10 (ValueStats). Muestra de 20 partidos en 7; **5 en Barcelona F–Servette F y 5 en Paris FC F–Køge F** (muestra corta); 19 en Benfica F–Roma F |
| **Goleadores/goleadoras (nuevo)**: goles, penales, asistencias y tarjetas por jugador de los últimos 10 partidos de cada equipo | `goleadores/<clave>.md/.json`, `flashscore/goles_crudo.json` | 20 equipos × 10 partidos (incidentes de Flashscore). Cruce con las líneas «anota» de Betano por nombre |
| Flashscore: tabla, qué se juega, ánimo, bajas | `notas/<clave>.json` | 10 |
| Flashscore: alineaciones probables + bajas | `alineaciones/`, `raw/lu_*.txt` | 5 de Brasil/MLS. **Los 5 femeninos no tienen pestaña de alineaciones todavía** |
| Flashscore: historial por jugador (todas las columnas) | `jugadores/<partido>.json`, `jugadores/LEEME.md` | Ver tabla de cobertura abajo |
| Contexto por partido y mercado | `contexto/` | 10 |

## Betano por partido
| Partido | Líneas de equipo | Líneas de jugador | de estadística |
|---|---|---|---|
| Austria Viena F – Bayern F | 43 | 41 (solo anota) | 0 |
| Paris FC F – Køge F | 54 | 45 (solo anota) | 0 |
| Arsenal F – Lyon F | 55 | 38 (solo anota) | 0 |
| Barcelona F – Servette F | 48 | 47 (solo anota) | 0 |
| Benfica F – Roma F | 54 | 40 (solo anota) | 0 |
| Vasco – Internacional | 190 | 346 | 213 |
| Vitória – Bragantino | 192 | 394 | 242 |
| São Paulo – Fluminense | 189 | 371 | 229 |
| Orlando City – Cincinnati | 143 | 238 | 117 |
| Seattle Sounders – Real Salt Lake | 142 | 235 | 114 |

Los femeninos solo traen goleadora (`anota`): no necesitan historial de estadística; se les trajo el historial de goles (goleadoras) porque el usuario lo pidió. MLS trae remates, tiros al arco y asistencias (sin entradas ni faltas de jugador).

## Cobertura del historial por jugador (partidos de 10 con tabla de jugadores)
| Partido | Local | Visitante |
|---|---|---|
| Vasco – Internacional | 10 | 10 |
| Vitória – Bragantino | 9 | 8 |
| São Paulo – Fluminense | 9 | 9 |
| Orlando City – Cincinnati | **7** | **4** |
| Seattle – Real Salt Lake | **4** | 9 |
| Femeninos (5 partidos) | 0–2 de 10 | 0–4 de 10 |

- **Brasil**: suficiente; los 1–2 partidos faltantes por equipo no tienen tabla en Flashscore.
- **MLS**: **parcial**. Cincinnati 4/10 y Seattle 4/10 son muestra corta: los mercados de jugador (remates, al arco, asistencias) de esos dos equipos **no se recomiendan sin declarar n**; Orlando 7/10 y RSL 9/10 aceptables.
- **Femeninos**: Flashscore casi no publica tablas de jugadoras. El historial disponible es el de **goles y asistencias** (incidentes), sin minutos ni remates. «Sin gol» no prueba que la jugadora jugó.

## Qué no se pudo leer
- Alineaciones de los 5 femeninos (no publicadas); releer ≈1 h antes con `raw/lu_<clave>.txt` oficial.
- Faltas por partido y penales por partido del árbitro: requieren cuenta de ValueStats (solo la muestra de 20: amarillas, rojas, penales y % sobre 3,5/4,5/5,5 tarjetas).
- Directos (H2H) de los 5 femeninos; estadísticas de equipo de partidos viejos de Austria F y Servette F.
- MLS Playoffs: cuadro/prórroga y tanda de penales no leídos.
- Goleadores: sin minutos ni titularidad, sin tiros por jugadora en femeninos.

## Límites que se declaran siempre
Flashscore no trae «faltas recibidas»; «entradas» de Flashscore son ganadas/intentadas, no las «entradas totales» de Betano; los criterios de tipsters no tienen resultados verificados. Los datos de jugadores pasaron por el navegador y se descargaron como archivo con hash verificado.

## Cambios de método de hoy
Árbitro obligatorio en todos los partidos (`CLAUDE.md`, `armar_entrada.arbitro_de`, `contexto_mercado.texto_arbitro`); goleadores desde incidentes (`recoleccion/goleadores.py`, ahora dentro de `correr_jornada.py`); orden alfabético de slugs en URLs de Flashscore. Ver `recoleccion/README.md`.
