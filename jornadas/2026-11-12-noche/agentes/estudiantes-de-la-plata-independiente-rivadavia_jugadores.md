# Jugadores · Estudiantes de La Plata – Independiente Rivadavia (Supercopa Argentina, final, 18:00 Bogotá)

Revisión a las ~17:35 Bogotá del 12-nov. Fuente: `fichas/ficha_estudiantes-de-la-plata-independiente-rivadavia.json` (clave `jugadores`) y `notas/`.

## Enfoque de mercados
Betano ofrece mercados de jugadores amplios. Pero NO hay alineación publicada, ni historial por jugador, ni árbitro con estadísticas. Por la regla 1 de CLAUDE.md **no se analiza ningún mercado de jugadores**. Ninguna línea es «cumple».

## Qué ofrece Betano (según la ficha)
- 67 jugadores con línea (36 de Estudiantes, 31 de Rivadavia), 364 filas jugador-mercado.
- Mercados: tarjeta 67; anota 61; anota o asiste 61; tiros al arco 60 (escaleras); remates 57 (escaleras); asiste 56; atajadas 2 (Muslera, Bolcato; escaleras 2-6 y 3-7).
- No hay entradas ni faltas de jugador. No hay parejas «cualquiera de los jugadores…» en los datos de la ficha (no aparecen).

## Estado de la ficha para jugadores
- `titular`: null en las 364 filas. `minutos_esperados`: null. `fuentes_xi`: sin fuente.
- `sin_historial`: true en las 364 filas; `partidos_muestra` 0; `por_90`: null en todas; regularidad «0 de 0»; cumple: 0.
- No hay tasas por 90 que reportar como referencia: la ficha no trae ninguna. No se rellena nada.

## Qué falta para poder analizarlos
1. Alineación probable o confirmada con fuente y hora: Flashscore la anuncia ~1 h antes del inicio (hacia las 17:00 Bogotá para las 18:00; a las 17:35 la pestaña seguía sin publicar). Leer con `recoleccion/flashscore_alineaciones.js` (`leerLineups(doc)` en `…/resumen/alineaciones/?mid=<mid>`) y guardar en `jugadores/<clave>.json` (la carpeta `jugadores/` no existe aún).
2. Historial por jugador, últimos ≤7 partidos jugados (remates, tiros al arco, atajadas, goles, asistencias, tarjetas, minutos). No se recolectó; sin él no hay tasa por 90, esperado, colchón ni «X de n».
3. Árbitro con estadísticas (B-Soccer), para tarjetas: solo se sabe el nombre, Pérez Y.
4. Verificar a cuántos minutos se liquida el mercado de la final (90 min o con prórroga).

## Bajas conocidas que Betano aún lista con línea
Fuente: previa de Flashscore del 12-nov, sin hora de la noticia (`notas/`). No excluidos por mí de la ficha; solo marcados.
| Jugador | Equipo | anota | tarjeta | remates (escalones 1+ con cuota) | al arco |
|---|---|---|---|---|---|
| Joaquín Correa | Estudiantes | 5.50 | 3.65 | 1:1.07 · 2:1.42 · 3:2.20 · 4:3.90 · 5:7.20 · 6:12.5 · 7:18.5 | 1:1.52 · 2:2.90 · 3:7.90 · 4:16 · 5:22 |
| Alexis Castro | Estudiantes | 4.90 | 2.85 | 1:1.28 · 2:2.18 · 3:3.65 · 4:10 · 5:17.5 | 1:2.07 · 2:6.40 · 3:16 · 4:23 |
| Alex Arce | Rivadavia (con la selección de Paraguay) | 3.40 | 2.15 | 2:1.19 · 3:1.60 · 4:2.32 · 5:4.10 · 6:7.20 · 7:12 · 8:17.5 | 1:1.35 · 2:2.40 · 3:5.60 · 4:11.75 · 5:19.5 |
Si de verdad son baja, esas líneas no tienen sentido y conviene no tocarlas. También tienen líneas de asiste y anota o asiste.

## Otros límites
- Estudiantes prepara la final de la Libertadores ante Palmeiras: posible rotación sin confirmar. Esto pesa en titularidad y minutos.
- Final en cancha neutra: «local» solo por orden de Betano.

## Plan cuando salgan las alineaciones
Titulares con fuente y hora; solo esos entran. Para cada uno: tasa por 90 × minutos/90 = esperado; colchón = esperado − (k − 0.5); regularidad en los últimos ≤7 (cumple ≥ 5); anota/asiste/tarjeta con regularidad y cuota.
