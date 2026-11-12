# Jornada 2026-11-13 · estado de la recolección (etapa 1) — completa a las ~14:00 Bogotá del 12-nov

**Etapa 1 COMPLETA** para los 11 partidos (hash de cada archivo verificado contra el navegador). La etapa 2 ya se corrió una vez como prueba (`python3 recoleccion/correr_jornada.py jornadas/2026-11-13`); puede correrse de nuevo sin navegador.

| Dato | Estado |
|---|---|
| Betano (cuotas leídas 12-nov ~12:32 Bogotá, 11 partidos) | En el repo: `raw/` y `betano/`. |
| Flashscore (7+7 últimos, directos ≤ 5 años, árbitro) | En el repo: `flashscore/` (11 partidos). |
| Alineaciones probables + bajas (Flashscore, leídas ~13:00 Bogotá) | Solo 4 partidos: Países Bajos–Grecia, Serbia–Alemania, Escocia–Macedonia, Eslovenia–Suiza. Los otros 7 no tenían alineación publicada → sin mercados de jugadores filtrados. |
| Binks (Escocia) | Flashscore lo trae en el XI probable y en bajas a la vez; se toma como baja y queda anotado en `dudas`. |
| Estadísticas del árbitro (BeSoccer) | No disponibles (404). Solo el nombre (Flashscore). |
| Historial por jugador | **Recolectado el 12-nov ~14:30 Bogotá** (Flashscore, pestaña «Estadísticas de jugadores» de 40 partidos pasados) para los jugadores de la alineación probable de los 4 partidos con alineación; está en `jugadores/<clave>.json` (hash verificado). Trae minutos, remates, tiros al arco, goles, asistencias, tarjetas, faltas y entradas ganadas; ventana = últimos 7 partidos oficiales de cada selección. Los otros 7 partidos no tienen alineación, así que no tienen historial. Sin casar con Betano: Gannon-Doak (Escocia) y Gnezda Cerin (Eslovenia); Urbancic (Eslovenia) no jugó en esa ventana. |
| Lectura de la situación (`notas/`) | Hecha: tablas de la Liga de Naciones calculadas con los resultados de Flashscore (las de Wikipedia estaban desactualizadas); Colombia con la tabla de Publimetro del 9-nov. |
| Descanso, clima, estilo, tabla del descenso colombiano | Sin leer (anotado en las notas del partido de Colombia). |

## Resultado de la prueba de etapa 2 (ver `ranking.md`)
- 10 partidos «apto» y 1 «no apto» (Inter de Bogotá–Santa Fe: Santa Fe ya clasificado, Inter eliminado de los ocho; situación 12).
- Betano ofrece estadísticas de partido y de jugadores solo en Países Bajos–Grecia, Serbia–Alemania y Escocia–Macedonia; en los otros 8 solo córners y goles/resultado.
- Con el historial, los mercados de jugadores de Países Bajos–Grecia, Serbia–Alemania y Escocia–Macedonia pasaron a «apto» (datos 85/70/73). En el puntaje de jugadores solo cuentan los del XI probable (regla 1).
- Límite: Betano «entradas» es total de entradas; Flashscore da «entradas ganadas». El historial de entradas puede quedar por debajo. Tómalo con cuidado.
- Todo se calculó con lo que hay en el repo; lo que falta está dicho arriba y en cada ficha.

## Actualización 12-nov ~16:30 Bogotá
- `informe_final.md` regenerado con los 7 agentes (córners, partido, jugadores, goles-resultado, tarjetas, combinadas); detalle de cada agente en `agentes/`.
- `puntuar.py` corregido (jugadores cuentan todas las líneas). La ficha trae goles y tarjetas (no entran al ranking).
- Las alertas del modelo caen en córners/tarjetas/saques/«más … que», no en goles ni resultado.
