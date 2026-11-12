# Turquía – Bélgica (Liga de Naciones A, jue 12-nov-2026 12:00 Bogotá) — análisis SM-1.2

Cuotas de Betano leídas el 11-nov ~12:00 (Bogotá), 599 mercados (JSON de la página). 1.319 selecciones evaluadas.

**Veredicto: sin valor verificable.** El modelo reproduce el precio de Betano (1X2 52/24/24 % contra 53/23/24 %; 1.er tiempo, 2.º tiempo y los nueve HT/FT a ±1 pt).
Línea más cerca de justa: Goles Menos 4.5 a 1.28 (EV 0 %). Lo más probable (EV −1 % a −3 %): Goles Más 1.5 (83 %), Bélgica Más 0.5 goles (86 %), Ambos reciben 1+ tarjeta (82 %).

## Hechos que importan (fuentes en la ficha)
- **Lukaku fuera** (cadera; federación belga, 11-nov). Betano sigue con sus líneas y 10 parejas que lo incluyen → «no apostar».
- Turquía: **técnico nuevo** (Sergen Yalçın, debut), 0 puntos, 0-3 en Lieja el 2-oct. Bajas: Bardakcı (suspendido), Kenan Yıldız, Demirbağ; duda Şimşir.
- Bélgica: Lavia (suspendido según una fuente), Debast y Openda fuera de la lista; Courtois descansa.
- Grupo 1: Francia 10, Italia 7, Bélgica 6, Turquía 0. Árbitro Sandro Schärer (4,23 amarillas/partido en su carrera; 3,9 en Liga de Naciones).

## Mercados que pidió el usuario
- **Parejas «cualquiera de los jugadores…»** (58): la mejor sin Lukaku es Güler o Tielemans (asistencia) a 2.70, EV −10 % (necesitaría 3.19). Las de «anota o asiste», «anota» y «tarjeta» quedan entre −11 % y −23 %.
- **HT/FT y «resultado medio tiempo o tiempo completo»**: EV −12 % a −30 % (la mejor, Bélgica/Bélgica 2.75 → −12 %); «Descanso o final: Bélgica» 1.53 → −8 %.
- Jugadores (alineación PROBABLE, no confirmada): ninguna escalera con valor; la más cercana a justa es Demiral «anota o asiste» a 7.70 (EV −2 %, prob. 13 %); el resto de jugadores queda entre −6 % y −10 % o peor.

## Alerta de modelo
- Saques de banda 1.er tiempo Menos 17.5 (2.05) sale +16 % solo porque el simulador reparte los saques de banda por tiempos distinto a Betano (diferencia de 23 pts): NO es valor; pendiente revisar el reparto por tiempos de saques de banda con datos reales.

## Para revisar antes de jugar
- Builders (solo si el cupón llega a la cuota mínima): Goles Menos 4.5 + Tiros al arco Menos 11.5 (mín. 1.75; p 59 %); Goles Bélgica Menos 3.5 + Ambos 1+ tarjetas Sí + Tarjetas 1.er tiempo Más 0.5 (mín. 1.75; p 59 %).
- Con las alineaciones oficiales (≈1 h antes): cambiar `titular` en `partidos/2026-11-12_turquia_belgica/construir.py` (lista J) y volver a correr.
