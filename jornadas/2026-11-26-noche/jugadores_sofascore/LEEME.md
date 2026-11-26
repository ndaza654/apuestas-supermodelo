# Historial por jugador · cobertura real (Sofascore, últimos 10 partidos oficiales de cada equipo)

Fuente: Sofascore `/api/v1` (estadísticas del jugador en cada partido; una fila por jugador que sumó minutos), leído 2026-11-26 ~15:55 Bogotá. Columnas por partido: id, fecha, minutos, remates, a puerta, goles, asistencias, tarjetas, entradas (totales/ganadas), faltas cometidas/recibidas, centros, xA, rating (ver `recoleccion/sofascore_decod.py`). Partidos con mercado de jugador en Betano: São Paulo–Remo, Pachuca–Chivas, León–Cruz Azul (Montevideo City–Nacional no tiene mercados de jugador: historial no necesario, queda de referencia).

**Límites declarados:** Sofascore sí trae faltas recibidas (Flashscore no); «entradas» son totales y ganadas de Sofascore (Betano cuenta totales, no son idénticas); lo recogido pasa transcrito por el chat y se verificó con hash (sha256 943267c8…); onces solo probables (Sofascore, sin oficial a las 15:55): reconfirmar con los oficiales ~1 h antes.

## cf-pachuca-guadalajara-chivas
- Pachuca: **10 de 10** partidos con estadísticas por jugador, 24 jugadores (17 con ≥5 apariciones).
- Chivas: **10 de 10** partidos con estadísticas por jugador, 26 jugadores (18 con ≥5 apariciones).
## club-leon-cruz-azul
- León: **10 de 10** partidos con estadísticas por jugador, 25 jugadores (17 con ≥5 apariciones).
- Cruz Azul: **10 de 10** partidos con estadísticas por jugador, 24 jugadores (20 con ≥5 apariciones).
## montevideo-city-torque-nacional-montevideo
- Montevideo City Torque: **7 de 10** partidos con estadísticas por jugador, 21 jugadores (14 con ≥5 apariciones).
- Nacional: **7 de 10** partidos con estadísticas por jugador, 25 jugadores (14 con ≥5 apariciones).
## sao-paulo-sp-remo-pa
- São Paulo: **10 de 10** partidos con estadísticas por jugador, 30 jugadores (18 con ≥5 apariciones).
- Remo: **10 de 10** partidos con estadísticas por jugador, 27 jugadores (18 con ≥5 apariciones).
