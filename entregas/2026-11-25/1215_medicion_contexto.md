# ¿El contexto que leo ayuda a que una línea se dé? Medición 12–25 nov

**Fecha y hora:** 25-nov-2026, ≈ 12:15 Bogotá. **Datos:** `registro/lineas.csv` (35.611 líneas calificadas, cumplió/falló, sin nulas), `jornadas/*/notas/` y `fichas/`. **Cuotas:** las de cada jornada (sin relectura). **Scripts:** `recoleccion/medir_contexto.py`, `medir_contexto_partidos.py`, `medir_contexto_residual.py`; tabla completa en `registro/medicion_contexto.md`.

## Pregunta
El usuario siente que el contexto (qué se juega, quién necesita ganar) es lo que hace que una línea se dé. Medida: acierto real frente a la probabilidad del precio (`p_mercado`, sin margen), con intervalos de confianza **por partido** (las líneas de un mismo partido caen juntas; contar líneas daba errores 5 veces más chicos).

## Resultado 1: ¿la línea que el contexto apoya acierta más que el precio?
| Grupo | partidos | diferencia real − precio | IC 95 % |
|---|---|---|---|
| Total del partido, situación a favor (casi todo «necesita ganar» → Más) | 67 | −6,7 pts | −13,3 a −0,4 |
| Total del partido, datos a favor (esperado vs línea, rachas, directos) | 222 | +1,6 pts | −1,4 a +4,4 |
| Línea de un equipo, situación a favor | 54 | +0,9 pts | −5,4 a +7,2 |
| Línea de un equipo, datos a favor | 213 | +0,9 pts | −1,1 a +2,9 |
| Total, situación a favor Y «cumple» a cuota ≥ 1,50 | 29 líneas | −13,2 pts | muestra mínima |

## Resultado 2: ¿el equipo que «necesita ganar» produce más de lo que decían sus datos? (real − esperado, remates/tiros al arco/córners/goles/fueras de un equipo)
| Bandera en la nota | partidos | real − esperado | IC 95 % |
|---|---|---|---|
| necesita ganar | 52 | −0,04 | −0,58 a +0,50 |
| solo el rival necesita ganar | 30 | −0,24 | −1,12 a +0,51 |
| le sirve el empate | 9 | +0,67 | −1,16 a +3,11 |
| sin banderas en el partido | 149 | +0,20 | −0,02 a +0,41 |
El esperado medio es ≈ 5; un equipo que necesita ganar hizo lo mismo que ya decían sus datos.

## Lectura honesta
- **No se confirma que el contexto estructurado mejore la línea.** En totales apunta incluso al lado contrario (−6,7 pts, intervalo apenas fuera de cero; con tantas comparaciones puede ser azar). En líneas de equipo no hay efecto medible.
- **No se descarta tampoco.** Solo 54–69 partidos tienen banderas de situación; el intervalo es de ± 6 pts. En las jornadas grandes (20–23 nov, ≈ 120 partidos) mis notas fueron narrativas (tabla, ánimo, bajas) **sin banderas**, así que casi no entran en la medición: lo que el contexto cuenta en texto no quedó medido.
- Las banderas son binarias y crudas («necesita ganar» sí/no). No capturan lo que el usuario describe (Barça con todo en juego, contra un rival cerrado, línea de tiros al arco a 1,70).
- Los factores de «datos» (esperado frente a la línea) ayudan poco: +1,6 pts, dentro del ruido; es lo mismo que el colchón.
- Un caso atípico (roja temprana) no se puede predecir ni medir con estos datos; en este análisis cae como fallo.

## Regla del usuario (25-nov 11:55)
No se busca ganarle a la casa de apuestas. Se busca que las líneas (sencillas y combinadas) que se analicen, escojan y apuesten estén **apoyadas por un buen contexto**; un partido atípico (roja, lesión temprana) no invalida el contexto. Quedó en `CLAUDE.md` («Contexto manda; no se busca ganarle a la casa»).

## Propuesta (pendiente de aprobación del usuario)
Para que el contexto se pueda medir de verdad: en cada partido analizado escribir en la nota, **antes del partido**, un `guion` concreto y comprobable (quién domina, ritmo abierto/cerrado, qué equipo tiene más remates/córners) y las líneas que ese guion apoya. En la calificación se mide si el guion se cumplió (reparto de remates, córners, goles) y si las líneas apoyadas se dieron. Así se juzga la lectura, no el precio.

## Límites
Contexto recalculado con el código actual sobre fichas y notas guardadas; jornadas 12–14 nov sin notas o sin banderas; reglas de situación de tipsters sin verificar; 25-nov solo con partidos ya terminados; 26-nov sin resultados.
