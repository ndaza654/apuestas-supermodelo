# Dónde están el supermodelo y lo de los tipsters, y para qué sirven junto a tu estrategia

**Entrega:** dom 15-nov-2026, 19:45 Bogotá. **Fuentes:** el repo (`MODELO_README.md`, `docs/MAPA_DE_ORIGEN.md`, `docs/CALIBRACION_10NOV.md`, `supermodelo/`, `datos/sistemas_historial.json`, `entregas/2026-11-14/0349_auditoria-repo.md`) y `registro/lineas.csv` (5.875 líneas de equipo calificadas, 12-nov noche a 15-nov). **Límites:** los archivos `criterios_por_mercado_12nov.md` e `idea_chats_por_mercado.md` están en el proyecto «Apuestas» de Claude, no en el repo; no se leyeron. `sombra.csv` no existe (el seguimiento en sombra nunca se usó). La comparación modelo–mercado cubre 4 jornadas.

## Dónde está
- **Supermodelo SM-1.2:** paquete `supermodelo/` (5.032 líneas), con `MODELO_README.md`. Sigue en el repo y corre en cada jornada desde `correr_jornada.py`; sus pruebas pasan (106).
- **Calibración con 238.858 partidos reales:** `docs/CALIBRACION_10NOV.md`; resultados en `datos/` (prior de 38 ligas, dependencia entre patas, memoria propia).
- **Tipsters que mandaste a analizar** (JekeDeportivas 114 videos, Ingeniero Analista 530, Sharpods 720, StatArea): qué se tomó y qué se descartó en `docs/MAPA_DE_ORIGEN.md`; sus filtros en `supermodelo/sistemas.py` con el historial de 160.000+ partidos en `datos/sistemas_historial.json`; seguimiento externo en `supermodelo/sombra.py` (sin datos aún).
- **Criterios por mercado de los tipsters** (regularidad, colchón): aplicados en `recoleccion/ficha.py`; los documentos de origen quedaron en el proyecto «Apuestas», fuera del repo.

## Cómo funciona
1. Parte del precio de Betano sin margen (método de potencia, mejor log loss en 160.256 partidos).
2. Simula el partido minuto a minuto (goles, córners, remates, faltas, tarjetas) con dispersión y dependencias medidas en 62.164 partidos; aplica contexto (bajas, árbitro, clima).
3. Entrega p del modelo (≈ 47 % precio + 53 % simulación), p del mercado, EV y alertas; etiqueta los sistemas de tipsters que el partido cumple (sin filtrar).
4. Combinadas: probabilidad conjunta con corrección de dependencia, stress por pata y margen acumulado. En vivo: re-simula desde el minuto y el marcador.

## Qué dicen los datos sobre su aporte
- **Sistemas de tipsters:** ninguno de ~20 supera el margen en 160.000+ partidos con cuota (por eso son solo etiquetas).
- **Modelo contra precio** (5.875 líneas de equipo): Brier mercado 0,1922; modelo 0,1932; simulación 0,1936. El modelo no mejora al precio.
- **Cuando el modelo discrepa del precio** (cuota 1,40–2,20): modelo ≥ 3 pts por encima → se dieron 41,6 % contra 56,4 % que decía la cuota (ROI −25,6 %, 166 líneas, 28 partidos); modelo ≈ precio → 54,7 % (−5,6 %); modelo ≥ 3 pts por debajo → 64,5 % (+13,2 %, 203 líneas, 33 partidos).
- **Dentro de tu filtro:** modelo ≈ precio 175 líneas 69,7 % (+13,6 %); modelo sobre el precio 17 líneas 35,3 % (−37,6 %, 10 partidos); modelo bajo 10 líneas.

## Para qué serviría junto a la estrategia
1. **Probabilidad de partida:** la p del mercado sin margen, no la del modelo, como probabilidad de cada línea.
2. **Alarma, no empuje:** si el modelo está ≥ 3 pts por encima del precio en una línea de tu filtro, desconfiar. Es una pista (17 líneas), no una regla.
3. **Combinadas del mismo partido:** única parte donde la simulación aporta (probabilidad conjunta con dependencia).
4. **Calibración y CLV:** medir si la cuota que tomas supera la de cierre.
5. **En vivo:** sus probabilidades fueron muy altas contra lo real (65–78 % contra 25–44 %); no usarlo en vivo hasta recalibrarlo.
6. **Tipsters:** como etiquetas y sombra, sin apostar; nada de lo medido los respalda como regla.
