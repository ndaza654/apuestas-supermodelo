# Supermodelo SM-1.2 — lectura de partidos para Betano (11-nov-2026)

Un solo paquete (`supermodelo`) que reemplaza a `modelo_v2` y a `modelo_v3_apuestas.zip`. Une el modelo v2, la
calibración del 9-nov, los combos del 9-nov (joint3) y todo lo investigado: JekeDeportivas, Ingeniero Analista,
Sharpods, StatArea, fuentes por mercado, papers y, sobre todo, una calibración con **238.858 partidos reales**
(football-data.co.uk, copia pública en GitHub) que antes no teníamos.

La idea no cambia: el precio de Betano sin margen es la base; la ventaja posible sale del contexto que el precio no
tiene (hechos frescos), de elegir la línea que aguanta los guiones probables, del precio del cupón y de combinar patas
que se ayudan. No hay reglas ni mercados vetados: el registro mide qué funciona con tus datos.

## Qué trae de nuevo (con su evidencia)
| Pieza | Qué cambia | Evidencia |
|---|---|---|
| Quitar margen con método de potencia | El favorito y el lado probable quedan algo más probables que con el reparto proporcional | 160.256 partidos: mejor log loss (7 errores estándar), igual con márgenes de 8 % o más |
| Simulador recalibrado con 62.164 partidos | Dispersión real de córners, remates, al arco, faltas y tarjetas; dependencias reales | Córners totales var/media: real 1,11, SM-1 1,16, v2 1,47; faltas: real 1,06, SM-1 1,02, v2 3,2 |
| Ambos Marcan y empate bien estructurados | El efecto marcador (el que pierde se vuelca) da más empates y Ambos Sí que el Poisson | Real: +2,25 pts Ambos y +1,9 empate sobre el Poisson del precio; SM-1 +2,3 y +1,7 |
| Tarjetas por tiempo y roja directa = 2 | 34 % de tarjetas en el 1T (v2 41–43 %); amarillas sin falta que crecen con el minuto | StatsBomb + corr faltas–tarjetas real 0,29 |
| Dependencia entre patas corregida | Combos como «gana el favorito + sus córners Más» o «Más 2.5 + córners Más» ya no salen inflados | Lift real contra simulado en 62.000 partidos |
| Prior de liga (38 ligas) | Media de tarjetas para el árbitro, base de cada liga en el informe, valores por defecto | ago-2022 → nov-2026 |
| Alertas de discrepancia | Avisa si la simulación se aleja ≥15 pts del precio, o si el contexto mueve ≥10 pts, sin hecho fresco | Ingeniero Analista: sus "valores" acertaron 2 de 7 contra 5,2 esperados |
| Ficha ampliada | Bajas una por una (posición, peso, reemplazo, horas), información tardía, calendario, consenso, rachas, H2H | Ingeniero Analista #296, Sharpods, Jeke |
| Combos con la cuota del cupón | Prob. sim. y ajustada, stress por pata, margen acumulado, estado, cartera (boletos que dependen de la misma idea) | Lecciones del 9-nov |
| En vivo | Simula desde el minuto y el estado actuales; lo observado actualiza el ritmo; compara con el plan previo | Validado con 400 partidos reales desde el descanso |
| Registro que se cierra solo | `--cerrar` califica todas las líneas con las estadísticas reales, anota cierre y CLV, y guarda el partido en la base propia | — |
| Sistemas de tipsters auditados | Etiqueta los filtros que el partido cumple, con su historial real con cuotas | Ninguno de 20 supera el margen en 160.000+ partidos |
| Seguimiento en sombra | StatArea, Forebet, app Sharpods, picks de TikTok: Brier contra el mercado y ROI con cuota Betano | ≥300 picks antes de decidir |
| Balance semanal | Las 5 preguntas (operativa más rentable, mercado a evitar, consistencia, patrón de pérdida, 3 mejoras) + CLV + n | Ingeniero Analista #397 |
| **HT/FT, resultado por tiempos y parejas de jugadores** (SM-1.2) | Los nueve HT/FT, «resultado medio tiempo o tiempo completo», resultado del 1.er y 2.º tiempo y «cualquiera de los jugadores» (asiste, anota, anota o asiste, tarjeta) salen de la misma simulación; las parejas con una baja confirmada se marcan «no apostar» | Petición del 11-nov (Turquía–Bélgica) |
| **Jugadores con alineación probable** (SM-1.2) | Los mercados de jugador se analizan SIEMPRE con la alineación confirmada o, si no, la probable (titularidad 0.8 / 0.5 / 0.2); solo se omiten si no hay nada | Regla del usuario, 11-nov |
| **Media esperada en cada mercado** (SM-1.1) | Cada bloque del informe (goles, córners, tarjetas, remates, faltas, saques…) abre con la media esperada del modelo, lo que espera Betano, la media sin ficha y el rango del 80 %; cada línea dice si cae «sobre la línea» o «lejos» | Hoja de partido Toulouse–Estrasburgo del 11-nov |
| **Informe con la hoja de partido completa** (SM-1.1) | Veredicto en 4 cajas, proyección por equipo contra Betano, Más y Menos lado a lado, mejores líneas de jugador, líderes y tarjetas de jugador | Misma hoja |

Lo que se probó y **no** entró: Dixon-Coles (ρ ≈ 0), Poisson bivariada, decaimiento temporal en el modelo de perfiles
(ayuda, pero el modelo de perfiles sigue perdiendo contra el mercado), todos los sistemas de filtros de tipsters como
reglas. Detalle en `docs/MAPA_DE_ORIGEN.md` y `docs/CALIBRACION_10NOV.md`.

## Instalación
Python 3.10+ con numpy y scipy (`pip install numpy scipy`).

## Uso
```bash
# 1. Analizar un partido → _informe.md, _informe.html y _resultado.json junto a la entrada
python3 -m supermodelo ejemplos/ejemplo_supermodelo.json

# 2. Igual, guardando todas las líneas en el registro y marcando lo que jugaste
python3 -m supermodelo partido.json --registro registro.csv --apostadas "Gana Junior;Córners Más 9.5"

# 3. Combos con la cuota real del cupón (también se pueden poner en la entrada como "combos")
python3 -m supermodelo --combos partido.json combos.json

# 4. En vivo, desde el estado actual del partido (trae la media final esperada: lo que ya pasó + lo que falta)
python3 -m supermodelo --vivo partido.json ejemplos/ejemplo_vivo.json

# 5. Al terminar: califica todas las líneas solas con las estadísticas reales (+ cuotas de cierre si las tienes).
#    El partido se agrega a datos/partidos.csv (base propia de la liga). Con el ejemplo, manda la base a otro lado:
python3 -m supermodelo --cerrar registro.csv "Local - Visitante" real.json cierres.json [--referencia pinnacle.json]
python3 -m supermodelo --cerrar ejemplos/registro_ejemplo.csv "Local FC - Visitante SC" ejemplos/ejemplo_real.json ejemplos/ejemplo_cierres.json --partidos /tmp/partidos_ejemplo.csv

# 6. Aprendizaje y balance
python3 -m supermodelo --informe registro.csv
python3 -m supermodelo --balance registro.csv --desde 2026-11-09
python3 -m supermodelo --sombra sombra.csv

# Pruebas
python3 pruebas/test_modelo.py        # 93 pruebas
python3 pruebas/backtest_5nov.py      # v1 contra SM-1 contra mercado en 17 partidos reales
```

## Entrada (`partido.json`)
Igual que en v2 (ver `ejemplos/ejemplo_supermodelo.json`):
- `local`, `visitante`, `liga` (texto libre: "Inglaterra · Premier League", "España LaLiga"...; el prior se busca solo) y `fecha`.
- `betano`: `unicos` (resultado, ambos, mas_que, ambos_n_tarjetas, handicap), `lineas` (goles, corners, tarjetas, faltas,
  remates, al_arco, fueras, saques_meta, saques_banda; ámbitos total, local, visitante, 1T y 2T) y `jugadores`.
- `ficha`: la llena el Lector de contexto (`prompts/lector_de_contexto.md`).
- `combos` (opcional): `[{"nombre", "patas": ["Gana X", "Goles Más 2.5"], "cuota": 3.40, "apostado": true, "stake": 1}]`.
  Las patas son los nombres que salen en el informe (sin importar tildes, mayúsculas ni coma decimal). Con `"apostado": true`
  y `--registro`, el combo se guarda como una fila propia y se califica solo al cerrar.
- Hándicap: `{"mercado": "handicap", "h": -1, "opciones": {"local": 4.2, "empate": 3.9, "visitante": 1.55}}`; `h` es siempre
  el hándicap del LOCAL. Con 3 opciones es el europeo; con 2 (`local`/`visitante`) y `h` entero o de cuarto es asiático.
- Líneas enteras (2.0) y de cuarto (2.25, 2.75) se evalúan con devolución y medias (EV correcto, columna «devuelve»).
- Un mercado único con una sola opción, o la doble oportunidad (1X/X2/12), no se normaliza como si fueran todas las
  opciones: la doble oportunidad se deriva del 1X2 y una opción sola usa un margen típico de un lado.
- Tarjetas (en vivo y al cerrar): `amarillas` = amarillas mostradas, incluida la 2.ª de una expulsión; `rojas` = todas;
  `rojas_directas` = las directas (si falta, se suponen directas). Puntos de Betano: amarilla 1, roja 2 (doble amarilla 3).
  Lo más seguro al cerrar es dar `tarjetas_betano` y `tarjetas_betano_1t` ya en puntos.
- `forma` (opcional, también dentro de la ficha): historial reciente de cada equipo, mismo formato que `perfiles.py`:
  `{"local": [{"v": "H", "stats": {"g": [2, 1], "c": [6, 3], "sh": [14, 9], "sot": [5, 3], "f": [12, 11], "y": [2, 1], "off": [2, 1], "ti": [15, 17], "gk": [7, 9], "xg": [1.8, 0.9]}}], "visitante": [...]}`
  (`[a favor, en contra]`, `v` = H si jugó en casa, A si fuera). Con él, el informe suma «a favor / en contra» en la proyección y
  «veces que salió Más» en cada línea (solo en la condición de hoy: local en casa, visitante fuera).
- `jugadores_hist` (opcional, también dentro de la ficha): `{"Nombre": {"pos": "Delantero", "partidos": [{"min": 90, "remates": 3, "al_arco": 1, "entradas": 0, "faltas": 1, "goles": 1, "asist": 0, "tarjeta": 0, "atajadas": null}]}}`.
  Con él, el informe suma /90, el histórico de 60′ o más y las barras en la sección de jugadores. El nombre puede ser distinto al de Betano
  («Hidalgo S.» y «Savanier Hidalgo» coinciden).
- **Mercados nuevos (SM-1.2)**, en `betano.unicos`: `{"mercado": "htft", "opciones": {"1/1": 6.2, "1/X": 14.5, … "2/2": 2.75}}` (descanso/final, 9 opciones),
  `{"mercado": "htft_o", "opciones": {"1": 2.6, "X": 1.87, "2": 1.53}}` («Resultado medio tiempo o tiempo completo»: ese resultado en el descanso O al
  final), `resultado_1t` y `resultado_2t` (`1`, `X`, `2`). En `betano.jugadores`: `stat` `asiste` (escalera 1+, 2+…). En `betano.parejas`:
  `[{"stat": "asiste|anota|anota_o_asiste|tarjeta", "jugadores": ["A", "B"], "cuota": 2.7}]` («cualquiera de los jugadores…»; gana si cualquiera cumple).
  En `jugadores` (ficha): `{"nombre", "lado", "titular", "minutos", "fuera": true}`; `fuera` = baja confirmada, juega 0 y sus parejas se calculan solo con la simulación.
- `estadio`, `cuotas_leidas` (texto con la hora a la que se copiaron las cuotas): salen en la franja de datos del partido.
- Sin `forma` ni `jugadores_hist` el informe sale igual, sin esas columnas, y avisa en «Límites».
- `informe` (opcional): textos escritos a mano para el HTML (veredicto, accion, chips, lectura, boletos, tabla, formas, h2h, datos, evitar,
  límites, checklist, `notas` {"Selección": "texto"} para escribir la lectura de una línea, `alineaciones`, `jugadores_notas`, `acento` [color, color suave],
  `como`). Si falta, el HTML se arma solo.

## Estructura
| Archivo | Qué hace |
|---|---|
| `config.py` | Todos los parámetros con su fuente y la cifra real con la que se calibró |
| `mercado.py` | Quitar margen (potencia), media de una escalera, EV, cuota justa y mínima, Kelly |
| `simulador.py` | Monte Carlo minuto a minuto; factores de territorio y dominio; córners desde remates; amarillas sin falta; modo en vivo (`estado`) |
| `contexto.py` | Ficha → multiplicadores; bajas con detalle; información tardía; calendario (solo nota); árbitro con media de la liga |
| `analizar.py` | Orquesta: precio → contexto → simulación → líneas → builders; alertas; base de la liga; sistemas |
| `mercados.py`, `escenarios.py`, `jugadores.py` | Eventos de cada mercado, guiones y robustez, mercados de jugador |
| `dependencia.py` | Corrección de la dependencia entre patas medida con datos |
| `combos.py` | Combos con cuota del cupón, stress, margen, estado, cartera |
| `vivo.py` | En vivo desde el estado actual |
| `ligas.py` | Prior de 38 ligas + mezcla con la base propia (`datos/partidos.csv`) |
| `sistemas.py` | Sistemas de tipsters que el partido cumple, con su historial real |
| `registro.py` | Registro, cierre automático, CLV, informe de aprendizaje |
| `balance.py` | Balance con las 5 preguntas |
| `sombra.py` | Seguimiento en sombra de fuentes externas |
| `memoria.py` | Avisos del historial propio (4–8 nov) |
| `proyeccion.py` | Media esperada por mercado y ámbito, esperado de cada jugador, historial de equipos y jugadores |
| `reporte.py`, `reporte_html.py` | Informe en Markdown y en HTML (hoja de partido con la media esperada en cada bloque) |
| `datos/` | prior_liga.csv, sistemas_historial.json, dependencia_pares.json, memoria propia, datos del 5-nov |
| `docs/` | MAPA_DE_ORIGEN.md (de dónde salió cada pieza) y CALIBRACION_10NOV.md (todas las cifras) |

## Límites honestos
- La calibración con datos reales usa ligas europeas (y algunas de América sin córners ni tarjetas). Colombia y Ecuador no
  están: su base saldrá de tu registro (`datos/partidos.csv`).
- Las cuotas de la fuente son de casas europeas, no de Betano.co: sirven para medir contra "un mercado", no para
  calcular la ganancia en Betano.
- No hay cuotas históricas públicas de córners, tarjetas ni jugadores: en esos mercados no se pudo medir si el modelo
  le gana a la casa; sí se calibró la forma (dispersión, dependencias, tiempos) con los resultados reales.
- En tus 6 partidos del 9-nov, SM-1, el v2 y el mercado quedan empatados (Brier ≈ 0,20; diferencias dentro del ruido).
- Una revisión independiente (otro agente que no vio la construcción) probó casos borde y encontró 5 errores graves y 15
  medios; están corregidos y cada uno tiene su prueba (las «G…» y «M…» de `pruebas/test_modelo.py`).
- Ningún modelo garantiza resultados. Lo que puede hacer este es equivocarse menos de forma sistemática, decir cuándo
  una apuesta depende de un solo guion y medir con tus datos qué funciona.
