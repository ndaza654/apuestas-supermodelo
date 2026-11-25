# Qué datos necesita cada mercado (catálogo para aprobar) — 25-nov-2026

Cómo leerlo: **Dato** = lo que haría falta para analizar bien el mercado; **Hoy** = si ya lo recolectamos; **Evidencia** = correlación entre el dato y la estadística del mercado en **171–176 partidos terminados** (352 equipo-partido; Flashscore, 12–25 nov), *del mismo partido*, es decir descriptiva: dice qué se mueve junto, no que sirva para predecir. **Propuesta** = agregar / no agregar. El usuario aprueba o rechaza dato por dato.
Marca ✅ = ya se recolecta desde el 25-nov (extractor ampliado; los partidos recogidos antes no lo traen) · 🟡 = Flashscore lo trae pero hay que construir algo · ❌ = Flashscore no lo trae.

## Hallazgo que corrige una idea: las entradas NO miden agresividad
Entradas (tackles) contra faltas del mismo equipo r = −0,01; contra tarjetas r = +0,04; entradas totales del partido contra faltas totales r = −0,11. Lo que sí se mueve con las faltas: **los duelos que gana el rival** (r = +0,44: si el rival gana los duelos, tú cometes faltas) y las faltas ↔ amarillas del partido (r = +0,51; ≈ 0,165 amarillas por falta). Las **faltas recibidas** ya están: el «Tiros libres» de Flashscore es casi exactamente las faltas del rival (r = 0,99). Aun así, entradas y duelos quedan guardados por si el usuario los quiere ver.

## Córners (total, equipo, 1T/2T)
| Dato | Hoy | Evidencia (r con córners propios) | Propuesta |
|---|---|---|---|
| Centros intentados / acertados | ✅ `cr`, `crw` | 0,66 (el más fuerte) | agregar |
| Toques en el área rival | ✅ `box` | 0,58 | agregar |
| Remates dentro del área / bloqueados | ✅ `shi`, `blk` | 0,53 / 0,52 | agregar |
| Posesión % | ✅ `pos` | 0,46 (menos que el «dónde») | agregar |
| Pases en el último tercio | ✅ `pf3` | 0,47 | agregar |
| xA (asistencias esperadas) | ✅ `xa` | 0,52 | agregar |
| Despejes del RIVAL | ✅ `cl` | 0,55 (el rival que despeja mucho = tú atacas) | agregar |
| Alineación: laterales y extremos titulares | 🟡 alineaciones | sin medir | ya existe; leer en la lectura |
| Marcador al descanso / minuto del primer gol (para «favorito perdiendo empuja») | 🟡 incidentes `df_su` | sin medir | agregar al guion |
| Posesión y centros POR TIEMPO (1T) | ✅ (el extractor ya guarda `stats_1t`) | sin medir | agregar |

## Tarjetas y faltas
| Dato | Hoy | Evidencia | Propuesta |
|---|---|---|---|
| Faltas cometidas / recibidas | ✅ `f` / `fk` (recibidas = tiros libres) | amarillas ↔ faltas 0,42 (equipo) y 0,51 (partido) | agregar |
| Duelos ganados (propios y del rival) | ✅ `du` | rival gana duelos → mis faltas +0,44; rojas ↔ amarillas +0,31 | agregar |
| Entradas (intentos / ganadas) | ✅ `tk`, `tkw` | ≈ 0 con faltas y tarjetas | guardar, **no usar como señal** |
| Árbitro: tarjetas y faltas por partido, penales | 🟡 `arbitros/` (ValueStats; cuenta de faltas solo con cuenta) | la señal más directa de tarjetas; **no medida aún** | seguir recolectando en todos los partidos |
| Qué se juegan / derbi / necesita ganar | ✅ notas | sin medir | ya existe |
| Rojas del equipo (últimos 10) | ✅ `r` | rojas ↔ faltas +0,15 | agregar |
| Faltas por jugador (para tarjeta de jugador) | ✅ historial de jugadores | modelo de jugador inflado 17–19 pts | ya existe |

## Remates y tiros al arco
| Dato | Hoy | Evidencia | Propuesta |
|---|---|---|---|
| xG, xGOT, ocasiones claras | ✅ `xg`, `xgot`, `big` | xG ↔ remates 0,70; xGOT ↔ al arco 0,81; ocasiones ↔ al arco 0,65 | agregar |
| Remates dentro/fuera del área | ✅ `shi`, `sho` | dentro ↔ remates 0,88 | agregar |
| Toques en el área rival | ✅ `box` | 0,80 con remates | agregar |
| Lo que concede el rival (remates, bloqueos, xGOT concedido) | ✅ (el extractor guarda «en contra») | rival que tira poco → tú tiras más (−0,31 con sus remates) | agregar |
| Posesión | ✅ `pos` | 0,54 | agregar |
| Atajadas rivales / calidad del portero (goles evitados `gp`) | ✅ `gp`, `xgotf` | atajadas ↔ xGOT concedido 0,57 | agregar |

## Goles, ambos marcan, resultado
| Dato | Hoy | Evidencia | Propuesta |
|---|---|---|---|
| xG a favor y en contra (últimos 10) | ✅ `xg` | xG ↔ remates 0,70 | agregar (mide mejor que los goles reales) |
| Ocasiones claras, xGOT, goles evitados del portero | ✅ | — | agregar |
| Errores que terminan en remate / gol | ✅ `es`, `eg` | errores ↔ tarjetas +0,13 | agregar |
| Goles de cabeza (juego aéreo y córners) | ✅ `hg` | 0,19 con córners | agregar |
| Goles por tiempo (1T/2T) y minuto del primer gol | 🟡 incidentes | sin medir | agregar para 1T/2T y para el filtro de video 1 |
| Cuota 1T Más 1,5 (filtro del video) | ✅ Betano | 62,5 % con el filtro completo (n 24) | ya existe |
| Bajas defensivas / delanteros | 🟡 alineaciones y bajas | sin medir | ya existe |

## Fueras de juego
Las estadísticas de equipo **no explican** los fueras de juego: la mejor correlación es 0,07. Falta (❌ o 🟡): altura de la línea defensiva (no está en Flashscore), estilo de pase en profundidad (`tp` pases en profundidad: r = 0,01), árbitro y los fueras de juego que concede/provoca cada equipo en sus 10 partidos (ya está). **Propuesta:** no agregar más; usar solo las dos medias y declarar que no hay dato de contexto que lo anticipe.

## Saques de banda
| Dato | Hoy | Evidencia | Propuesta |
|---|---|---|---|
| Centros / despejes del rival / posesión | ✅ | centros 0,31; despejes del rival 0,38; posesión 0,29 | agregar |
| Duelos y entradas del rival | ✅ | entradas del rival 0,28; duelos 0,24 | agregar |
Sin estrategia de tipster todavía.

## Saques de meta
| Dato | Hoy | Evidencia | Propuesta |
|---|---|---|---|
| Remates y toques en el área del RIVAL | ✅ | remates del rival 0,68; toques en el área del rival 0,55 | agregar |
| Pases largos propios (portero que juega largo) | ✅ `lp` | 0,33 | agregar |
| Posesión propia | ✅ | −0,50 | agregar |

## Jugadores (remates, tiros al arco, entradas, faltas, atajadas, asistencias, goleador)
Hoy: historial por jugador de los últimos 10 (minutos, goles, asistencias, remates, a puerta, entradas, faltas cometidas, atajadas, rating) + alineación probable/oficial.
| Dato | Hoy | Propuesta |
|---|---|---|
| xG y xA por jugador (últimos 10) | 🟡 la última columna de la tabla parece ser xG (por confirmar contra Flashscore); xA no confirmado | revisar y agregar |
| Rol y posición en el once (delantero, extremo, lateral, volante) y si cobra penales/tiros libres/córners | 🟡 la posición sí está (`pos`); los cobradores no | agregar cobradores desde la previa |
| Faltas recibidas por jugador | ❌ Flashscore no las trae | no se puede; declarar |
| Calidad del portero rival y de la defensa (goles evitados, xGOT concedido) | ✅ por equipo | agregar |
| Minutos esperados (titular/suplente, rotación) | ✅ alineaciones | ya existe |

## Todos los mercados (comunes)
| Dato | Hoy | Propuesta |
|---|---|---|
| Árbitro (tarjetas, penales; faltas solo con cuenta) | 🟡 | seguir en todos los partidos |
| Tabla y qué se juega | ✅ notas | ya existe |
| Segunda lectura de cuotas | ❌ depende de que el PC del usuario esté disponible | solo cuando esté conectado |
| Clima | ❌ no está | proponer fuente (previa de Flashscore o servicio de clima) si el usuario lo quiere |
| Guion comprobable por partido | ✅ regla del 25-nov | ya existe |

## Qué se hizo hoy
- Extractor `recoleccion/flashscore_extraer.js` ampliado (25 estadísticas nuevas por partido, incluida la de 1T; probado con un partido real).
- `recoleccion/ficha.py`: sección «Estilo de juego» con la media de cada dato «a favor» y «en contra» (se muestra cuando hay ≥ 5 partidos con el dato; las jornadas anteriores salen «sin datos»).
- Pendiente de aprobación del usuario: qué datos se usan en cada mercado y cuáles se descartan; luego se convierten en reglas de `contexto_mercado.py` y en la «Lectura» de cada ficha.
- **Límite:** las correlaciones son del mismo partido; para saber si sirven antes del partido hay que juntar los 10 partidos previos de cada equipo (se obtendrán en la próxima recolección) y medir si predicen.
