# Jornada 2026-11-13 · estado de la recolección (etapa 1) — completa a las ~14:00 Bogotá del 12-nov

**Etapa 1 COMPLETA** para los 11 partidos (hash de cada archivo verificado contra el navegador). La etapa 2 ya se corrió una vez como prueba (`python3 recoleccion/correr_jornada.py jornadas/2026-11-13`); puede correrse de nuevo sin navegador.

| Dato | Estado |
|---|---|
| Betano (cuotas leídas 12-nov ~12:32 Bogotá, 11 partidos) | En el repo: `raw/` y `betano/`. |
| Flashscore (7+7 últimos, directos ≤ 5 años, árbitro) | En el repo: `flashscore/` (11 partidos). |
| Alineaciones probables + bajas (Flashscore, leídas ~13:00 Bogotá) | Solo 4 partidos: Países Bajos–Grecia, Serbia–Alemania, Escocia–Macedonia, Eslovenia–Suiza. Los otros 7 no tenían alineación publicada → sin mercados de jugadores filtrados. |
| Binks (Escocia) | Flashscore lo trae en el XI probable y en bajas a la vez; se toma como baja y queda anotado en `dudas`. |
| Estadísticas del árbitro (BeSoccer) | No disponibles (404). Solo el nombre (Flashscore). |
| Historial por jugador | No disponible. Los mercados de jugadores salen «no apto» por datos. |
| Lectura de la situación (`notas/`) | Hecha: tablas de la Liga de Naciones calculadas con los resultados de Flashscore (las de Wikipedia estaban desactualizadas); Colombia con la tabla de Publimetro del 9-nov. |
| Descanso, clima, estilo, tabla del descenso colombiano | Sin leer (anotado en las notas del partido de Colombia). |

## Resultado de la prueba de etapa 2 (ver `ranking.md`)
- 10 partidos «apto» y 1 «no apto» (Inter de Bogotá–Santa Fe: Santa Fe ya clasificado, Inter eliminado de los ocho; situación 12).
- Betano ofrece estadísticas de partido y de jugadores solo en Países Bajos–Grecia, Serbia–Alemania y Escocia–Macedonia; en los otros 8 solo córners y goles/resultado.
- Todo se calculó con lo que hay en el repo; lo que falta está dicho arriba y en cada ficha.
