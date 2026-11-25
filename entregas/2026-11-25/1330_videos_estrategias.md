# Videos de estrategias de @ingenieroanalista10 (cuenta nueva): qué dicen y cómo les fue

Fecha: 25-nov-2026, ≈13:30 Bogotá. Fuente: 4 mp4 que envió el usuario, transcritos con Whisper small (pueden fallar cifras y nombres; no se guarda la transcripción completa, es contenido ajeno). Medición con datos del repo (`pruebas/backtest/datos.json`, `registro/lineas.csv`, `jornadas/*/resultados/`) y, para la final, la API pública de ESPN. Cuotas: las del registro (lecturas de Betano de cada jornada). Límites: criterios de tipsters sin resultados verificados; muestras pequeñas; no se verificaron los datos de bajas/rachas que cita.

## 1. «Más 2,5 goles» (63 s)
Filtros: local ≤ ≈ 1,50 y línea 1T Más 1,5 ≤ 2,15; dice 500/670 (75 %). Medición: base 49,8 %; local ≤ 1,50 → 59,7 % (n 7.986, 6 ligas); mis líneas con filtro completo → 62,5 % (n 24, cuota media Más 2,5 ≈ 1,35). **No reproduce el 75 %; y 75 % a esa cuota es el equilibrio.** Detalle en `estrategias/goles_resultado.md`.

## 2. Córners: 4 filtros (168 s)
Centros > 20 por partido; dominio territorial > 55 % en campo rival; favorito ofensivo; proyección 9–10 córners; extra en vivo (favorito empatando/perdiendo). Medición descriptiva (165 partidos): centros ↔ córners r = 0,66; toques en área 0,58; posesión 0,46; equipos > 20 centros: 7,1 córners contra 4,0. Lógico y coherente con los datos, **pero no probado como predictor** (faltan centros de los últimos 10 en la recolección). Detalle en `estrategias/corners.md`.

## 3. Previa Palmeiras–Cruzeiro (18-nov, Brasileirão) — sin pick
Tesis: ambas defensas diezmadas (Palmeiras sin tres titulares y con Flamengo en 3 días; Cruzeiro con bajas) → ambos marcan y goles Más. **Resultado 2–1:** ambos marcan Sí ✓ (cuota 1,55), Más 2,5 ✓ (1,67), Más 3,5 ✗. Una sola muestra y tesis fácil de cumplir en un partido con 3 goles; a favor: la lectura de «rotación» del favorito sí pesó.

## 4. Previa Atlético-MG–Boca (final Sudamericana, sáb. 21-nov) — sin pick
Tesis: cruce cerrado (últimos cruces 2-2, 0-0, 0-0 según el video), presión en los dos, porteros de penales → toca goles Menos y penales. **Resultado (ESPN, API oficial, leído 25-nov 13:40): Boca 2–0 Atlético-MG en los 90 min, sin prórroga ni penales** (ESPN: remates 16–9, tiros al arco 7–2, amarillas 1–3). La insinuación de penales **falló**; goles Menos 2,5 habría cumplido (2 goles) pero Menos 1,5 no. *Corrección: la primera versión de esta entrega decía 0–0 y penales 3–1; era un partido distinto (otra página de ESPN), y se retiró.* El partido no estaba en mi registro (sin líneas que calificar). Hechos verificados en la web: Mineiro perdió la final de Libertadores 2024 y la de Sudamericana 2025 en penales.

## Veredicto
- Lo útil: los **tipos de factores** (bajas defensivas + calendario, partido decisivo, dominio territorial, centros) son lógicos y ya están en nuestras fichas; el de córners se puede medir si se recolectan centros.
- Lo no probado: los porcentajes que da (75 % de 670) no se reproducen con nuestros datos y se miden contra el precio.
- Las previas: Palmeiras–Cruzeiro acertó (ambos marcan, goles Más); la final **no** (penales/partido cerrado: ganó Boca 2–0 en 90 min). 1 de 2, sin pick ni cuota; con n = 2 no dicen nada de su exactitud en general.
