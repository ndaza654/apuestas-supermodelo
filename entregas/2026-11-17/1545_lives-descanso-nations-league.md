# Lives al descanso · 8 partidos de las 14:45 (Nations League)
**Fecha/hora:** mar 17-nov-2026, ~15:40 Bogotá (min 45–47 de cada partido).
**Fuentes:** cuotas en vivo de Betano (páginas /live/ de cada partido, leídas 15:33–15:42); estadísticas en vivo de Flashscore (feed df_st, 15:37); esperados de la ficha de 10 partidos de cada equipo; árbitros de ValueStats (`arbitros/valuestats_arbitros_1400.json`, últimos 20 partidos). Modelo: `jornadas/2026-11-17/vivo/modelo_vivo.py` (restante = mezcla de lo esperado por la ficha para la 2ª parte y el ritmo del 1T; binomial negativa para córners y tarjetas, Poisson para goles).
**Límites:** cuotas del descanso, se mueven al reanudar; el modelo en vivo no está calibrado con resultados (los rangos de p reflejan cuánto peso se da al ritmo del 1T); tarjetas en puntos Betano (amarilla 1, roja 2); sin faltas por jugador; Flashscore y Betano pueden diferir en 1 córner por retraso.

## Enfoque de mercados
Con todos los partidos en el descanso pesan tres mercados: tarjetas (muchos partidos con 0 tarjetas y pocas faltas frente a árbitros de 3,5–3,7 puntos), córners (Georgia 8–0, Gales–Portugal 2 en total) y goles (Dinamarca–Noruega abierto). Se descartan líneas con cuota < 1,50 y las que Betano ya ajustó al marcador de córners.

## Estado al descanso
| Partido | Marcador | Córners | Tarjetas (pts) | Remates | Árbitro (pts/partido) |
|---|---|---|---|---|---|
| Dinamarca–Noruega | 2–1 | 1–6 | 0–1 | 4–10 | Meler |
| Irlanda–Kosovo | 1–0 (Kosovo con 10) | 4–1 | 2–3 | 11–4 | Malcevs 5,7 |
| Bosnia–Rumanía | 1–1 | 2–2 | 0–0 | 5–7 | Sánchez 5,0 |
| Gales–Portugal | 2–2 | 2–0 | 0–0 | 10–6 | Jablonski 3,5 |
| Hungría–Irlanda del Norte | 1–0 | 2–2 | 0–0 | 4–2 | Guida 3,7 |
| Israel–Austria | 1–0 | 1–4 | 0–0 | 3–10 | Massa 4,7 |
| Ucrania–Georgia | 1–0 | 0–8 | 0–0 | 5–6 | Matosa 4,5 |
| Polonia–Suecia | 1–1 | 0–5 | 0–0 | 4–6 | Zwayer 5,0 |

## Líneas sugeridas (cuota ≥ 1,50)
1. Gales–Portugal · Menos 2,5 tarjetas @1,88 · p ≈ 70–78 %.
2. Hungría–Irlanda del Norte · Menos 2,5 tarjetas @2,05 · p ≈ 62–65 %.
3. Irlanda–Kosovo · Más 7,5 tarjetas @1,85 · p ≈ 60–62 %.
4. Ucrania–Georgia · Georgia Más 11,5 córners @2,20 (p ≈ 50–57 %) / total Más 12,5 @1,72 (p ≈ 55–65 %).
5. Gales–Portugal · Gales Más 3,5 córners @1,70 · p ≈ 66 %.
6. Dinamarca–Noruega · Más 4,5 goles @1,57 · p 62–74 %.

No valen: Gales–Portugal Más córners totales (Betano ya lo descontó), Israel–Austria Más córners (p ≈ 45 %), todo lo de cuota < 1,50.
