---
name: registrar-resultados
description: Registra los picks y califica los resultados reales de una jornada (aciertos, calibración, CLV) para aprender qué mercados y criterios funcionan.
---
# Registrar y calificar

1. Guardar los picks de la jornada en `registro/` con `supermodelo/registro.py` (CSV con `;`): línea, cuota, probabilidad del modelo, qué criterios cumplía y si el usuario la apostó.
2. Al terminar el partido, traer las estadísticas reales (Sofascore) y llamar a `cerrar()` de `registro.py`: califica TODAS las líneas analizadas, no solo las apostadas.
3. Medir por mercado y por criterio: ¿las líneas que cumplían «≥5 de 7» acertaron más que las que no? ¿el colchón informó algo? Con n pequeño, decirlo; no concluir con pocos datos.
4. Resumir en `registro/resumen_AAAA-MM-DD.md`: aciertos, calibración, qué ajustar en `criterios/`.
