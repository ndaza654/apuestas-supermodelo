# Plan del dashboard y de la automatización (propuesta del 14-nov-2026 — HISTÓRICO)

Estado (23-nov-2026): **ya construido y en línea** como dashboard v2 «Mando» (https://ndaza654.github.io/apuestas-supermodelo/, `dashboard/`, reconstruido por GitHub Actions en cada push a `main`). Este texto se conserva como registro de la propuesta; lo vigente está en `CLAUDE.md`. Reglas que no cambian: el usuario decide y apuesta; Claude no coloca apuestas ni entra a Betano con credenciales; no se toca nada de GitHub fuera de este repo; los datos que faltan se dicen, no se inventan.

## 1. Qué se vio en los tres videos (plantillas de Excel de Etsy)
- **Modelo de valor esperado:** cuota → probabilidad implícita, quita del margen (vig), «% de banca» por Kelly con factor ajustable, EV por línea. Hojas aparte para arbitraje y parlay (p de cada pata, p conjunta, cuota justa, tamaño de apuesta).
- **Tracker con tablero:** KPIs (ganancia total, ROI, # apuestas, % acierto), segmentadores (liga, deporte, casa, tipo de apuesta, año, mes, «últimos 30 días»), ganancia por casa, **por banda de cuota**, % acierto por banda de cuota, ganancia mensual, % de apuestas por deporte.
- **Tracker diario:** curva de banca acumulada, ganancia por día, por deporte, por tipo de apuesta; filas con color de ganada/perdida.
- Lo que se toma: segmentadores globales, banda de cuota, curva de banca, parlay con p conjunta, Kelly. Lo que no: arbitraje (Betano es una sola casa) y cifras fijas de hoja de cálculo; aquí todo sale de la base y se recalcula.

## 2. Qué hacen repos y herramientas parecidos (búsqueda del 14-nov)
- **mlb-sharp** (Scottguts): GitHub Actions con cron diario que ejecuta el pipeline y hace commit de los resultados; `bet_tracker.py` (anexar, liquidar, reporte por categoría y CLV); `closing_snapshot.py` guarda la cuota de cierre cada hora durante los partidos; `bankroll_sim.py` repite el historial con apuesta plana, escalera y Kelly; avisos por Telegram/Slack/correo.
- **wild-tracker** (osmond): endpoint de calibración (pares probabilidad-resultado), «apuesta de 1 $ plana a la cuota de cierre» con ganancia acumulada, columnas de contexto (días de descanso).
- **rust-bet-tracker** (WalrusQuant): tres bloques: dónde estás (actual vs máximo, exposición abierta, últimos 30 días), ¿eres afilado? (ganancia esperada, tasa de superar el cierre, curva de banca) y de dónde sale la ganancia (por casa, liga, tipo).
- **kelly-js** (ianalloway): fórmulas de CLV y EV con pruebas.
- **betting-oracle y similares:** actualización nocturna por GitHub Actions, herramienta de banca y notificaciones.
- **Evidence.dev** (SQL + Markdown, sitio estático, DuckDB en el navegador) y **Observable Framework** (Markdown + JS, cargadores de datos en Python, se despliega estático). Un blog de 2026 sobre Evidence advierte que su diseño es «desktop-first» en móvil.

## 3. Arquitectura recomendada
```
 TU PC (Claude desktop + navegador integrado)         NUBE (sin tu PC)
 ┌──────────────────────────────────────────┐         ┌───────────────────────────────────────────┐
 │ Recolección: Betano (cuotas, jugadores,  │ commit  │ GitHub Actions: correr_jornada, calificar,│
 │ Mis apuestas), Flashscore, alineaciones  ├────────►│ sugerencias, pruebas, construir base,     │
 │ (tareas programadas de escritorio)       │ al repo │ desplegar tablero, avisos                 │
 └──────────────────────────────────────────┘         │ Rutina de Claude (nube): enfoque, lectura,│
                                                       │ sugerencias, balance → rama + PR           │
 CELULAR / PC ◄──── Tablero (sitio estático + DuckDB) ◄┘ Hosting privado con acceso por correo      │
```
- **Fuente de verdad:** los archivos del repo (CSV, JSON, MD). **La base no se edita a mano**: `dashboard/construir.py` la regenera (DuckDB/Parquet por jornada).
- **Frontend:** Observable Framework (o Vite + Svelte) + DuckDB-WASM + ECharts/Plot. PWA instalable en el celular. Una sola base de componentes, diseño móvil primero.
- **Backend:** ninguno obligatorio. Para registrar tus apuestas desde el celular: formulario que guarda en el teléfono y envía un archivo a `registro/entrada_apuestas/` con una **llave de GitHub limitada a este repo** (decisión tuya) o, alternativa sin llave, exporta un texto que pegas en el chat.
- **Hosting:** Cloudflare Pages + Cloudflare Access (inicio de sesión por correo, gratis) para que sea privado en PC y celular. GitHub Pages es público: no.
- **Dónde vive el código:** carpeta `dashboard/` de este mismo repo; no hace falta otro repositorio.

### Tablas de la base
`partidos`, `equipos`, `lineas` (una fila por línea y lectura de cuota), `cuotas_historial` (snapshots), `series_equipo` (stats por partido y tiempo), `directos`, `jugadores`, `jugador_partidos`, `alineaciones`, `arbitros`, `clima`, `clasificacion`, `fichas` (esperado, regularidad), `modelo` (p, EV, alertas), `resultados`, `boletos`, `patas`, `sugerencias`, `informes` (MD con etiquetas), `entregas`, `metodos`, `recolecciones` (fuente, hora, hash, estado), `decisiones` (pendientes tuyos).
Tamaño: hoy `lineas.csv` tiene ~15.500 filas y crece ~6.000 por jornada (≈2 millones al año): por eso Parquet por jornada y consultas en el navegador solo de lo que se mira.

## 4. Páginas, en orden de construcción
1. **Hoy** (centro de mando): partidos por hora con estado en vivo, líneas que cumplen, tus apuestas, semáforo de datos (alineación, árbitro, historial de jugadores, edad de las cuotas).
2. **Explorador de líneas:** todos los filtros actuales + «X de N» (N hasta 10, K libre, equipos), filtros guardados con nombre y comparación de dos filtros (líneas, aciertos, 1 u plana).
3. **Ficha de partido:** cuotas y su movimiento, series y directos con gráficos contra la línea, plantilla, bajas, árbitro, clima, tabla, lectura del modelo, mapa de calor de líneas.
4. **Mis apuestas:** boletos por pata, en vivo, ROI por tipo, banda de cuota, mercado y día; vista «mías / tuyas / mezcladas».
5. **Mis sugerencias:** cada una con p dicha, cuota, resultado y distancia entre lo prometido y lo ocurrido.
6. **Jugadores:** ficha por jugador, tasa por 90, historial, líneas del día, comparador.
7. **Resultados y calificación:** qué se dio y qué no, por criterio.
8. **Calibración y honestidad** (ver §6).
9. **Laboratorio de criterios:** simulador de un criterio sobre todo el historial (líneas, aciertos, 1 u plana, intervalo).
10. **Banca y riesgo:** curva en COP y unidades, apuesta plana/escalera/Kelly fraccionado simulada, rachas, exposición por partido, correlación en cupones.
11. **Cupón:** constructor con p conjunta, cuota justa, condición de Bet Builder, guardado y comparación con lo apostado.
12. **Biblioteca de informes:** buscable, por jornada y etiqueta.
13. **Recolección y salud:** qué se recogió, fuente, hora, hash, fallos y qué falta.
14. **Bitácora y libro; decisiones pendientes.**
Transversal: **búsqueda global** (líneas, jugadores, partidos, informes; atajo en PC, botón en celular), filtros globales fijos (fecha, liga, mercado), modo claro/oscuro, exportar a CSV/Excel.

## 5. Automatización: qué se puede y qué no
| Paso | Dónde corre | ¿Necesita tu PC? | Disparador |
|---|---|---|---|
| Plan del día (partidos, horas, qué recolectar) | nube | no | cron 05:00 |
| Cuotas Betano, jugadores, Mis apuestas | **navegador de tu PC** | **sí, encendido y con Claude abierto** | tarea programada de escritorio |
| Flashscore (resultados, series, alineaciones) | PC; probar si GitHub Actions lo lee sin evadir bloqueos | según prueba | por horario del partido |
| Análisis offline, calificación, sugerencias, pruebas | GitHub Actions | no | al llegar datos nuevos |
| Enfoque, lectura, balance escrito | Rutina de Claude en la nube | no | tras el pipeline |
| Construir base y desplegar tablero | GitHub Actions | no | al terminar |
| Avisos (cupón listo, alineación cambió, balance) | Telegram o notificación del celular | no | eventos |
Línea de tiempo por partido: −24 h cuotas de apertura · −90 min alineación + cuotas · −5 min **cuota de cierre** (para CLV) · +120 min resultado y calificación · 23:30 balance del día.
Límites honestos: Betano exige tu navegador (sesión, geografía), así que sin PC encendido ese paso no corre y el tablero lo marca en rojo; si Betano o Flashscore cambian su página el recolector falla y se avisa. Nada se rellena con supuestos.

## 6. Panel de honestidad
- Calibración: p del modelo contra frecuencia real por tramo, con intervalo de Wilson; Brier y log-loss contra la p del mercado.
- CLV: cuota tomada contra cuota de cierre y % de veces que se superó el cierre.
- ROI con intervalo (bootstrap) y tamaño de muestra. Cuenta de referencia: con cuotas ~2,0 el error típico del ROI es ≈ 1/√n; para distinguir un +5 % de cero hacen falta del orden de 1.600 apuestas independientes.
- Separación de «líneas del pipeline» (muchas, correlacionadas) y «apuestas reales».
- Marca visible de «1 jornada / muestra pequeña» en cada conclusión.
- **Criterios de graduación (propuesta a ajustar):** p calibrada dentro del intervalo, CLV positivo sostenido y límite inferior del ROI > 0 con una muestra mínima acordada, antes de pasar a «semiautomático».

## 7. Camino hacia «dale el mando»
Solo hay dos niveles posibles: 1) **actual:** tú apuestas con lo que el tablero y yo preparamos; 2) **semiautomático:** yo dejo el cupón armado y una notificación; tú lo confirmas en Betano. **Claude no ingresa credenciales ni confirma apuestas con dinero**: eso queda fuera de lo que puedo hacer aunque lo autorices.

## 8. Fases
- **F0 (1 sesión):** carpeta `dashboard/`, base DuckDB desde el repo, esquema, pruebas de integridad.
- **F1:** Hoy, Explorador, Ficha de partido, Mis apuestas, búsqueda global, móvil + PWA, hosting privado.
- **F2:** Automatización en la nube (Actions + rutina) y avisos; cuota de cierre y snapshots.
- **F3:** Sugerencias, Jugadores, Resultados, Biblioteca, Recolección/salud.
- **F4:** Calibración, Laboratorio, Banca y riesgo, Cupón avanzado.
- **F5:** semiautomático (cupón + aviso), si se cumplen los criterios de graduación.

## 9. Decisiones tuyas
1. Hosting privado con Cloudflare Access (cuenta tuya) o solo local en el PC.
2. Cómo entran tus apuestas desde el celular: llave limitada a este repo, o texto exportado.
3. Si tu PC puede quedar encendido con Claude abierto en las horas de partido.
4. Aviso por Telegram (bot nuevo) o notificación del celular.
5. Aprobar `dashboard/` y los flujos de GitHub Actions dentro de este repo.
6. Pendientes anteriores: regla de banca, retirar «recorte de p»/«valor»/EV, tarea de las 4:00 en `main`, unidad 3.700 vs 3.750.

Fuentes: repos mlb-sharp (Scottguts), wild-tracker (osmond), rust-bet-tracker (WalrusQuant), kelly-js (ianalloway); documentación y artículos de Evidence.dev, Observable Framework y de las rutinas de Claude Code (abril 2026).
