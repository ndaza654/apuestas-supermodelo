# Alineaciones y bajas · 14-nov-2026

- **Fuente:** Flashscore.co, pestaña «Alineaciones» de cada partido (`…/resumen/alineaciones/?mid=<mid>`), leída con `recoleccion/flashscore_alineaciones.js` (`leerLineups`).
- **Hora de lectura:** vie 13-nov-2026, ~19:15–19:45 Bogotá (UTC−5). Todos los archivos se leyeron en esa ventana (los Colombianos y Banfield–Boca se confirmaron como «sin pestaña» en la misma lectura).
- **Estado:** todas son **«Alineaciones probables»**, no oficiales. Flashscore publica las oficiales ~1 h antes del inicio; si se quiere apostar a jugadores, hay que releer ese día (regla fija 1).
- **Orientación:** `L` = primer equipo del `titulo` = local; `V` = visitante. (El orden del enlace de Flashscore NO sirve para esto; el título sí.)
- **Formato:** `probables.L/V` = `[nombre, dorsal, id_jugador_flashscore, 1 si arquero]`; `bajas.L/V` = `[nombre, id, motivo]` (lesión, selección nacional, tarjetas amarillas = suspendido, inactivo…).
- `kick` = hora que muestra Flashscore en el navegador (Bogotá). En Jamaica–México el título dice 15/11 (UTC) pero el kick es 14-nov 20:00 Bogotá.

## Sin datos (declarado, no se rellena)
Flashscore **no tiene pestaña de alineaciones** para estos 5 partidos (`sin_pestana: true`): Banfield–Boca, Millonarios–Alianza, Atl. Nacional–Once Caldas, Dep. Cali–Tolima, Águilas Doradas–Ind. Medellín. Para ellos no hay alineación ni bajas con fuente; los mercados de jugadores quedan sin análisis hasta tener otra fuente (Sofascore/medios) o las oficiales.

Hash verificado archivo por archivo contra el navegador (`verificar_hash.py`).
