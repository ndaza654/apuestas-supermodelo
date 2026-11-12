# Mapa de origen: de dónde salió cada pieza del supermodelo SM-1 (10-nov-2026)

Estados: **Adoptado** (cambia números) · **Registrado** (no cambia números; queda en el registro para medirlo con tus
datos) · **Sombra** (se sigue sin apostar) · **Descartado** (con el motivo). Nada de esto es una regla de apuesta.

## 1. Lo que ya teníamos (v1 → v2 → 9-nov)
| Pieza | Origen | Estado en SM-1 |
|---|---|---|
| Precio de Betano sin margen como base | Backtest 5-nov (17 partidos, 450 líneas): mercado 0,2328 contra v1 0,2399 | Adoptado. Confirmado con 7.128 partidos de 5 ligas: el mercado le gana al modelo de promedios de goles en todas (log loss 0,969 contra 0,988); las "apuestas con valor" del modelo de promedios rinden −14 % a −17 % |
| Simulador minuto a minuto, guiones, robustez, builders | Modelo v2 | Adoptado y recalibrado (ver 2) |
| Ficha de contexto con "frescos" y FUERZA_CONTEXTO | v2 + balance 4–8 nov | Adoptado y ampliado (bajas con detalle, información tardía, calendario) |
| Dominio del día | Balance 4–8 nov (72 partidos) | Rehecho: con 62.164 partidos la correlación real goles–remates es 0,14, no 0,34; se separó en territorio + dominio |
| Calibración del 9-nov (DOMINIO q 0,15; FORMA_RITMO 40; FORMA_EQUIPO c 24) | Partidos del 9-nov | Superada por la calibración con datos (FORMA_RITMO 150, etc.). El paquete modelo_v3_apuestas.zip no la tenía; SM-1 sí la incorpora y la reemplaza |
| Residuo "Ambos Sí 3–5 pts bajo el mercado" (9-nov) | Calibración 9-nov | **Resuelto**: era un sesgo del modelo. El Poisson del precio subestima Ambos Marcan en 2,25 pts y el empate en 1,9 (76.096 partidos, 12 errores estándar); SM-1 lo reproduce |
| "Más 1.5 tarjetas 1T" 5–10 pts sobre el precio (9-nov) | Calibración 9-nov | **Resuelto**: el simulador ponía el 41–43 % de las tarjetas en el 1T; ahora 34 % (amarillas sin falta que crecen con el minuto, StatsBomb) |
| Convención sim./ajust. de los combos (joint3.py) | 9-nov | Adoptado dentro de `combos.py`, con stress por pata, margen acumulado, estado y corrección de dependencia |
| Memoria propia (avisos del historial 4–8 nov) | Balance de 151 líneas | Adoptado; también avisa en builders y combos |
| Perfil de córners (centros, territorio) | Ingeniero Analista + 70 partidos propios | Adoptado (40 % de fuerza) |
| Columna "Combinada" 50/50 de los informes | 9-nov | Reemplazada por la probabilidad de decisión: W_MERCADO = 0,5 (backtest 5-nov: así el modelo queda igual al mercado en log loss) |

## 2. Calibración con datos reales (10-nov, `docs/CALIBRACION_10NOV.md`)
| Pieza | Evidencia | Estado |
|---|---|---|
| Quitar margen con método de potencia | 160.256 partidos 1X2: −0,00055 ± 0,00008 de log loss contra proporcional; O/U 2.5 −0,00013 ± 0,00005; igual con margen ≥8 % | Adoptado (`config.METODO_SIN_MARGEN`) |
| Sesgo favorito–longshot | No favorito con <35 % gana 2–3 pts menos que su cuota; favorito >65 % gana 3–4 pts más | Adoptado vía método de potencia |
| Dispersión real de cada estadística | 62.164 partidos, condicionado a equipo y precio | Adoptado en el simulador y en la lectura de escaleras (`R_EQUIPO`, `R_TOTAL`) |
| Córners que nacen de remates (Binomial 0,09) | corr remates–córners 0,28 sin dispersión extra | Adoptado |
| Volumen contra calidad (0,30) | corr goles–remates real 0,23 | Adoptado |
| Amarillas sin falta (30 %) | StatsBomb (59 % del partido; "otras razones" hasta la mitad al final) + corr faltas–tarjetas real 0,29 | Adoptado |
| Roja directa = 2 puntos (regla Betano) | El v2 contaba 1 | Corregido |
| Efecto marcador en goles | El que pierde al HT marca +13 % en el 2T | Adoptado (sim +9 %) |
| Corrección de dependencia entre patas | Lift real contra simulado (p. ej. gana favorito + córners del favorito Más: 0,88 contra 0,93) | Adoptado en builders y combos |
| Prior de liga (38 ligas, ago-2022 → nov-2026) | `datos/prior_liga.csv` | Adoptado: media de tarjetas para el árbitro, base del informe, valores por defecto |
| Dixon-Coles | ρ ≈ −0,005; sin mejora en 4 ligas | Descartado |
| Decaimiento temporal (vida media 180–365 d) | −0,017 de log loss con historia de varias temporadas | Registrado: aplica al modelo de perfiles, que sigue apagado (W_MODELO_MEDIA = 0) porque pierde contra el mercado |
| Poisson bivariada (λ₃) | Mejora pequeña en log loss pero no reproduce Ambos/empate | Descartado (el efecto marcador lo explica mejor) |

## 3. JekeDeportivas (114 videos)
| Idea | Estado |
|---|---|
| EV = cuota/justa − 1 | Ya estaba (misma cuenta que p·cuota − 1) |
| Poisson ataque × defensa con media de liga ("Jeknica") | Probado con 2.280 + 999 partidos: pierde contra el mercado. Queda solo como alerta (historial contra mercado) |
| "Controles de ajuste" hacia el precio | Ya estaba (ancla al mercado) y ahora reforzado (alerta de discrepancia) |
| Decaimiento temporal / esperar ~50 % de temporada | Probado: sirve para pesar historia vieja, no dentro de una temporada. Registrado (ver 2) |
| Normalización ELO por confederación para torneos | No aplica mientras el ancla sea el mercado; queda como referencia |
| Referencia afilada (Pinnacle) para el CLV | Adoptado: columna `cuota_referencia` en el registro |
| Confirmar el once ("baja + reemplazo") | Adoptado: bajas con `reemplazo` y `confirmada` |
| Clima por liga | Registrado (hechos lluvia/viento/calor≥30) |
| Sesgo contra el último de la tabla | Probado con 10.656 partidos: −5,4 % y −4,7 % de ROI, sin ventaja. Registrado como sistema JEKE_ULT |
| Regresión del xG | Registrado: `xg_menos_goles` en la ficha |
| xG solo-distancia, broker, Polymarket, "fijas" | Descartado |

## 4. Ingeniero Analista (530 videos)
| Idea | Estado |
|---|---|
| Encoger hacia el mercado cuando el modelo discrepa (sus 7 "valores": 2 aciertos contra 5,2 esperados) | Adoptado: `ALERTA_DISCREPANCIA` 15 pts sin hecho fresco; `ALERTA_CONTEXTO` 10 pts |
| Línea de apertura y cierre (CLV) | Adoptado: `cuota` (apertura), `cuota_cierre`, `clv`; el informe mide si el mercado se mueve hacia el modelo |
| Tasas base por liga | Adoptado con datos propios verificados (prior de liga), no con sus porcentajes |
| Centros, % en campo rival, favorito empatando/perdiendo | Ya estaba (perfil de córners, estado del partido) |
| Variables en vivo (xG, tiros a puerta y ataques peligrosos al HT) | Adoptado como modo en vivo (`vivo.py`): lo observado actualiza el ritmo; validado con partidos reales |
| Cuota del empate y de la local como señal de goles | Probado: empate ≥3,60 → Más 2.5 rinde −4,0 % (42.643 partidos). Registrado (etiqueta precio:empate>=3.60 y sistema IA14) |
| Bajas: peso por posición, reemplazo, ventana de 24 h | Adoptado: `bajas` con detalle; <24 h = fresca |
| Balance con 5 preguntas | Adoptado: `balance.py` |
| IA sin adulación, fuentes, 3 razones para estar equivocado | Adoptado en el Lector de contexto |
| Fecha FIFA: descanso, viajes | Registrado (sin efecto en números) |
| Sistemas de filtros (#400, #453, #14, #5, #26, #45, #420, #429, #16, #313, #415, #456) | Probados los que se pueden con cuotas (160.000+ partidos): ninguno supera el margen. Registrado como etiquetas de sistema con su historial (`sistemas.py`) |
| Stop tras 3 pérdidas, stake 0,1–3 % | Referencia (disciplina tuya); el balance muestra racha y stake |
| Par/impar, rachas sin rival, "racha brutal" | Descartado |

## 5. Sharpods (720 videos)
| Idea | Estado |
|---|---|
| FootyStats / StatsHub como fuentes de datos | Adoptado en el Lector (fuentes de la ficha) |
| Forebet, StatArea, app de Sharpods como segunda opinión | Sombra: `sombra.py` (Brier contra el mercado, ROI con cuota Betano, 300 picks antes de decidir) |
| Consenso de la app como campo "popular" | Registrado: `consenso_publico` en la ficha |
| Información tardía | Adoptado: `info_tardia` en la ficha (marca frescos) |
| Unders por sesgo del público (90/10) | Probado: Más 2.5 −5,8 % contra Menos −6,2 % (107.273 partidos): no hay sesgo aprovechable. Registrado |
| Combinadas de patas 1,1–1,3 | El informe muestra el margen acumulado por combo |
| Banca 0,5–2 % | Referencia; `mercado.kelly` (¼ Kelly) como dato informativo |
| Récords "X de las últimas Y" | Descartado como evidencia; el balance da n e intervalo |
| Action Labs, Outlier, OddsShopper | Descartado (NBA/MLB, de pago) |

## 6. StatArea y fuentes por mercado
| Idea | Estado |
|---|---|
| StatArea: porcentajes 1X2 bien calibrados; Más 1.5 y Ambos peor que la base; tip X 7/40 | Sombra (snapshot y `sombra.py`); no usar tip X, Más 1.5 ni Ambos |
| `compare` de StatArea como contexto | Adoptado como fuente de la ficha |
| Ningún tipster de córners/tarjetas/jugadores con historial verificado | Sombra para cualquiera que se quiera seguir (≥300 picks por mercado) |
| football-data.co.uk para córners/tarjetas | Adoptado: copia pública en GitHub → prior de liga y toda la calibración |
| Wheatcroft (tiros y córners → Más/Menos, +0,8 %) | No replicable sin cuotas de córners; queda como referencia |

## 7. Balances propios
| Lección | Estado |
|---|---|
| 4–8 nov: el volumen de un equipo es una apuesta sobre quién domina | Ahora calibrado con datos: la relación existe pero es más débil (0,14 con remates; 0,50 con al arco) |
| 4–8 nov: en vivo 3 de 13 boletos | El modo en vivo muestra si la línea estaba en el plan previo |
| 9-nov: combos de misión dependían de lo mismo | `combos.cartera`: boletos que dependen de la misma idea cuentan como una apuesta |
| 9-nov: stress de una sola pata | `combos.evaluar`: stress de cada pata (−5 pts) |
| 9-nov: aviso de fuga en córners Más | Los avisos de memoria se heredan en builders y combos |
| 9-nov: leer el cupón, no la tarjeta | Los combos se evalúan con la cuota del cupón |
| 9-nov: guardar xG y córners reales por liga | `registro.cerrar` → `datos/partidos.csv` (base propia de Colombia, Ecuador, etc.) |
| 9-nov: medias de liga de tarjetas para el árbitro | Prior de liga |

## 8. Revisión independiente (10-nov, otro agente que no vio la construcción)
Probó los comandos, casos borde y el código. Todo lo que encontró está corregido y tiene su prueba en `pruebas/test_modelo.py`:
- **Graves:**
  - la ficha con campos en null tumbaba el análisis;
  - un mercado de una sola opción o la doble oportunidad daban un falso «Valor»;
  - un hecho fresco apagaba la alerta de una línea mal copiada;
  - el hándicap de 3 opciones evaluaba mal el empate y nombraba mal al visitante.
- **Medios:**
  - ligas mal reconocidas (Austria → Alemania, Rusia → Inglaterra, Escocia) y el aviso de Italia en Brasil y Ecuador;
  - la base propia no agrupaba por liga (jornadas) y cerrar dos veces duplicaba partidos;
  - registro viejo con columnas corridas y «--apostadas» que fallaba en silencio;
  - líneas enteras y de cuarto sin devolución, y faltaban 1T/2T de fueras y saques;
  - línea solo con «menos», goles sin anclar cuando faltaba el 1X2 o la línea de goles;
  - convención de rojas en vivo, aviso de vivo sin datos del 1T, combos en el registro y rutas fijas del backtest.

## Añadido el 11-nov (SM-1.1): hoja de partido con la media esperada
| Pieza | De dónde sale |
|---|---|
| Media esperada en cada bloque de mercado, con «Betano» y rango del 80 % | Pedido del usuario al ver la hoja Toulouse–Estrasburgo; la media sale de la simulación (`proyeccion.medias`) y la de Betano de `analizar.media_mercado` |
| Proyección del partido (modelo contra Betano; a favor / en contra con `forma`) | Hoja Toulouse–Estrasburgo (tabla «Proyección del partido») |
| Más y Menos lado a lado, «veces que salió Más», lectura por línea | Hoja Toulouse–Estrasburgo (tablas de mercado); la regla de lectura usa la probabilidad de decisión |
| Veredicto en cajas, mejores líneas de jugador, líderes y tarjetas de jugador | Hoja Toulouse–Estrasburgo; el EV, la cuota mínima y la robustez siguen siendo los del SM-1 |
| Media final esperada en vivo | `vivo.py`: lo ya jugado más lo que falta |

