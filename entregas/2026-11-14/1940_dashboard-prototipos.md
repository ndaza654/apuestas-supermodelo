# Dashboard: tres prototipos completos (14-nov-2026, 19:40 Bogotá)

**Datos:** los del repo hasta hoy — `registro/lineas.csv` (15.475 líneas: 4.731 de equipo, 10.744 de jugador, 35 partidos), boletos de Betano leídos el 14-nov ~19:00 (36 boletos), 439 sugerencias, 323 líneas históricas, 31 documentos, historial de jugadores solo de Portugal–Dinamarca. Cuotas de Betano de cada jornada (hora en cada ficha). Nada se leyó de nuevo para este prototipo.
**Qué son:** tres versiones del mismo dashboard (mismas 16 páginas, mismos filtros, mismos datos, ~2,6 MB cada una, abren con doble clic, sin internet). Cambia la navegación, la densidad y la pantalla de inicio, para que compares la experiencia.

## Las 16 páginas (en los tres)
Hoy · Líneas (tabla, tarjetas o pivote; ~15 filtros; «X de N» ajustable con conteo por K) · Partido (líneas, series, jugadores, datos) · Jugadores (líneas, resultados, cobertura) · Buscar (global) · Mis apuestas · Sugerencias · Cupón (arma, califica con lo que ya pasó, guarda) · Resultados · Honestidad (¿hay ventaja real? Brier, ROI con intervalo) · Laboratorio (prueba un criterio y compáralo) · Banca (simulación de stress) · Informes · Salud de datos · Automatización · Decisiones pendientes.

## Diferencias
| | A «Mando» | B «Móvil» | C «Laboratorio» |
|---|---|---|---|
| Aspecto | oscuro, denso | claro, grande, táctil | claro, números monoespaciados |
| Navegación | barra lateral | barra inferior + «Más» | barra superior de dos filas |
| Inicio | Hoy (partidos y KPIs) | Hoy en línea de tiempo | Laboratorio |
| Líneas | tabla; filtros abiertos | tarjetas; filtros plegados | pivote; filtros abiertos |
| Detalle | panel fijo a la derecha | hoja desde abajo | panel deslizante |

**A — pros:** más información a la vez, ideal en PC; detalle sin perder la tabla. **Contras:** en celular queda apretado; el tema oscuro cansa menos de noche pero no es de todos.
**B — pros:** el mejor para apostar desde el celular (pulgar, tarjetas, filtros plegados). **Contras:** en PC desperdicia espacio; comparar muchas filas es más lento.
**C — pros:** pensado para probar criterios (pivote, Laboratorio, Honestidad al frente). **Contras:** menos «operativo»: para ver los partidos de hoy hay que dar un clic más.

## Qué le falta a cada uno (y a los tres)
- A: vista de celular pulida (hoy funciona, no es su fuerte); atajos de teclado más completos.
- B: tablas anchas con desplazamiento lateral; pivote y Laboratorio son incómodos en pantalla chica.
- C: una pantalla «de operación» para el día del partido; es la más exigente de leer.
- **Los tres:** (1) leen una foto del repo, no se actualizan solos; (2) las apuestas y las notas que anotes en el prototipo solo viven en tu navegador (localStorage); (3) el historial de jugadores existe solo para Portugal–Dinamarca (51 de 10.744 líneas); (4) los boletos se enlazan a partidos por nombre, algunos sin partido claro; (5) banca inicial de $200.000 supuesta; (6) la versión real usaría base de datos en el navegador (DuckDB-WASM) y actualización automática; (7) nadie coloca apuestas: el dashboard solo lee y calcula.

## Lo que muestran los datos (honesto)
Líneas de equipo calificadas: 3.131 en 29 partidos; se dieron 42 % (intervalo 40–44 %) y el mercado decía 41 %; 1 u plana −7 %. Con «cumple 5 de 7»: 71 líneas, 58 % real contra 62 % del mercado, −11 %. Boletos: 36 liquidados, 6 ganados, neto −$175.000. Sugerencias: 65 % real contra 68 % dicho. Aún no hay ventaja demostrada en ningún filtro.

## Límites
Probado con Playwright (1440 y 390 px): 16 páginas × 3 diseños sin errores de consola ni desbordes; filtros, K de N, detalle, cupón, guardar filtros, Laboratorio, Banca, búsqueda e informes respondieron. No se probó en un celular real. Código: `dashboard/` (`construir_prototipos.py`).
