# Jornada 2026-11-15 · estado de la recolección (etapa 1) — completa a las ~21:05 Bogotá del 14-nov

**Etapa 1 COMPLETA** para los 13 partidos que el usuario marcó como favoritos en Flashscore (13 de ~21 que muestran sus capturas; los demás no se recolectaron). Hash de cada archivo verificado contra el navegador.

| Dato | Estado |
|---|---|
| Betano (cuotas leídas 14-nov 19:55 Bogotá, 13 partidos) | En el repo: `raw/` y `betano/`. 5 partidos con mercado de jugador de estadística (Bélgica–Italia, Croacia–Rep. Checa, España–Inglaterra, Francia–Turquía, Chipre–Montenegro); los otros 8 solo goles/córners/tarjeta o goleador. |
| Flashscore (10+10 últimos, directos ≤ 6) | En el repo: `flashscore/` (13 partidos). |
| Alineaciones probables + bajas (Flashscore, ~20:16–20:18) | 4 partidos: Bélgica–Italia, Croacia–Rep. Checa, España–Inglaterra, Francia–Turquía. **Chipre–Montenegro: sin pestaña de alineaciones** → sus mercados de jugador no se recomiendan. |
| **Historial por jugador** (regla obligatoria) | **Completo para los 5 partidos con mercado de jugador:** últimos 10 partidos oficiales de cada equipo, 10 de 10 en los 10 equipos (`jugadores/`, `LEEME.md`). 75 partidos pasados leídos; 9 fallaron una vez y se reintentaron. Los 8 partidos sin mercado de jugador de estadística no lo necesitan. |
| Estadísticas del árbitro | Solo el nombre (Flashscore). |
| Lectura de la situación (tabla, descanso, clima) | Sin leer. |

## Límites declarados
- Flashscore no trae «faltas recibidas»: ese mercado no se recomienda.
- «Entradas» = ganadas; Betano cuenta entradas totales.
- Cruce de nombres Flashscore↔Betano: 6 jugadores ambiguos o abreviados se resolvieron por id de Flashscore verificado en su perfil (`recoleccion/alias_jugadores.json`); los que ningún partido de los últimos 10 jugaron quedan sin historial.
- Sin cruzar a propósito: Giannis Kosti (Chipre; Flashscore «Kosti I.»), sin alias verificado.
- Los datos pasaron transcritos por el chat y se verificaron con hash (3 erratas de transcripción halladas y corregidas por hash de línea).

## Relectura del 15-nov 13:36 (Bogotá)
- Betano releído para España–Inglaterra y Bélgica–Italia (hash verificado); lectura de anoche en `betano_previo/`. Los otros 11 partidos siguen con cuotas del 14-nov 19:55.
- Onces **oficiales** (Flashscore 13:40) para esos dos partidos. Italia cambió 4 titulares; Koleosho y Pisilli sin historial.
- Tabla leída (Flashscore 13:50) y notas de situación para los 4 partidos de Liga de Naciones A; el resto, situación sin leer.
