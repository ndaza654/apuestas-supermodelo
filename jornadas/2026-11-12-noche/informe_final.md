# Informe final · jornada 2026-11-12 noche (Betano.co)

Partidos (hora Bogotá): **Estudiantes – Independiente Rivadavia 18:00**, **Curazao – Panamá 19:30**, **Atl. Morelia – Leones Negros 21:00**. Cuotas leídas ~17:29; recolección completa ~17:35. Cifras de `fichas/`, `informes/` y `agentes/` de esta carpeta; las principales se contrastaron con la ficha. El detalle de cada agente está en `agentes/<partido>_<agente>.md`.

## Enfoque de mercados

- **Estudiantes–Rivadavia (final de la Supercopa Argentina, cancha neutra en Córdoba):** es el único partido con mercados de estadísticas. Pesan **córners, remates y tiros al arco** (con regularidad en ambos equipos y 3 directos), **tarjetas** (final de importancia alta) y **goles**. Estudiantes prepara la final de la Libertadores ante Palmeiras: si rota, bajan sus remates y tiros, y suben los «Menos» de Estudiantes.
- **Curazao–Panamá (ida de cuartos de la Nations League):** Betano solo ofrece goles, córners, tarjetas y resultado (sin tiros ni faltas; jugadores solo «anota»). Pesan **córners** (una sola línea cumple), tarjetas y goles. Hay 39 días sin partido oficial para ambos.
- **Morelia–Leones Negros (ida de semifinal de la Liguilla de Expansión):** 37 mercados: goles, resultado, descanso/final, hándicap y 2 líneas de córners. Sin tarjetas, tiros ni jugadores. Pesan **goles y resultado**; los córners no tienen ninguna línea que cumpla.
- **Jugadores: no se analizan** en ningún partido. A las 17:35 no había alineaciones publicadas (regla 1), no hay historial por jugador y no hay estadísticas del árbitro.

## Advertencias que aplican a todo el informe
1. **Liquidación de la final no verificada.** No se pudo comprobar si Betano liquida el resultado, la doble oportunidad, el hándicap y el descanso/final de Estudiantes–Rivadavia a 90 minutos o con prórroga y penales (los archivos `raw/` solo traen códigos y cuotas). **No se recomienda nada del mercado de resultado de esa final** hasta leerlo en la página del mercado.
2. **El modelo no es segunda opinión en goles ni resultado.** Sus goles salen de las cuotas de Betano (`fuente_objetivos.g = mercado`), así que su probabilidad queda a ≤2 pts del mercado por construcción; el EV de todas las líneas de goles que cumplen sale negativo (−1 % a −11 %). Las alertas «la simulación se aleja N pts del mercado» (10 en Estudiantes, 5 en Curazao–Panamá, ninguna en Morelia) caen en **tarjetas** y córners, no en goles. Los EV positivos de tarjetas vienen de esa brecha, no de la serie.
3. **Cuotas de tarjetas incoherentes (sin verificar).** En Estudiantes y en Curazao–Panamá las líneas «Más 0.5 tarjetas» por equipo implican menos probabilidad (~45–70 %) que «Ambos con 1+ tarjeta» (~66–92 %), lo cual no puede ser. Puede ser una etiqueta o una unidad distinta; no se pudo comprobar. **No se usan esas líneas** hasta revisarlas en Betano.
4. **Tarjetas en puntos** (amarilla 1, roja 2) en Betano; Flashscore solo trae amarillas, así que la serie queda por debajo si hubo rojas (perjudica sobre todo a los «Menos» ajustados).
5. **Cuotas de las 17:29**: releer antes de apostar. Colchón informativo, no excluye ninguna línea. «Cumple» = ≥5 de 7 en ambos equipos (n mínimo 5); no es una probabilidad.
6. **Escalones = una sola apuesta.** Varias líneas del mismo mercado y ámbito (p. ej. remates de Estudiantes Menos 15.5 y 16.5) fallan juntas.

Notación: L/V = local/visitante (en una línea de equipo, lo propio del equipo y lo que concede el rival); D = directos.

---

## 1. Estudiantes de La Plata – Independiente Rivadavia · 18:00
Final única, cancha neutra: «local» es solo el orden de Betano. Muestra 7+7, 3 directos. Bajas según la previa de Flashscore (sin hora): Correa y Castro (Estudiantes), Arce (Rivadavia); Betano aún lista líneas de esos tres. Árbitro Pérez Y. (sin estadística). Rotación posible de Estudiantes, sin confirmar.

### Córners (esperado Estudiantes 5.5 · Rivadavia 4.36 · total 9.86)
| Línea | Cuota | Colchón | L | V | D |
|---|---|---|---|---|---|
| Total Más 6.5 | 1.24 | +3.4 | 7 de 7 | 6 de 7 | 3 de 3 |
| Total Más 7.5 | 1.47 | +2.4 | 6 de 7 | 6 de 7 | 2 de 3 |
| Total Más 8.5 | 1.82 | +1.4 | 5 de 7 | 5 de 7 | 1 de 3 |
| Estudiantes Más 3.5 | 1.35 | +2.0 | 6 de 7 | 5 de 7 | 2 de 3 |
| Rivadavia Más 2.5 | 1.29 | +1.9 | 5 de 7 | 6 de 7 | 2 de 3 |

Cumplen con cuota < 1.20 (sin valor práctico): total Más 4.5 @1.05 y 5.5 @1.11, total Menos 12.5 @1.10 y 13.5 @1.05, Estudiantes Más 2.5 @1.14, Rivadavia Más 1.5 @1.09. No cumple: total Más 9.5 y superiores, total Menos 4.5–10.5 (Menos 10.5 @1.31: 4 y 4), Estudiantes Más 4.5 (6/4), Rivadavia Más 3.5 (5/4). 1T/2T: Betano las ofrece pero no hay estadística por tiempo (sin ficha).

### Remates y tiros al arco (esperado remates 13.64 + 12.57 = 26.21; tiros al arco 4.5 + 4.36 = 8.86)
Cumplen 26 líneas, 14 con cuota ≥ 1.20 (coincide con el ranking). Las más destacadas:

| Mercado | Línea | Cuota | Colchón | L | V | D |
|---|---|---|---|---|---|---|
| Remates | Estudiantes Menos 16.5 | 1.25 | +2.9 | 6 de 7 | 5 de 7 | 3 de 3 |
| Remates | Estudiantes Más 10.5 | 1.20 | +3.1 | 6 de 7 | 5 de 7 | 3 de 3 |
| Remates | Total Menos 29.5 | 1.27 | +3.3 | 6 de 7 | 5 de 7 | 2 de 3 |
| Remates | Rivadavia Menos 14.5 | 1.29 | n/d | 5 de 7 | 6 de 7 | 2 de 3 |
| Tiros al arco | Total Menos 10.5 | 1.27 | +1.6 | 5 de 7 | 6 de 7 | 3 de 3 |
| Tiros al arco | Total Más 6.5 | 1.30 | +2.4 | 5 de 7 | 5 de 7 | 2 de 3 |
| Tiros al arco | Rivadavia Más 2.5 | 1.27 | +1.9 | 6 de 7 | 5 de 7 | 3 de 3 |

Cuidado: «Estudiantes Más 10.5» y «Estudiantes Menos 16.5» forman una banda del mismo equipo; los «Más» de Estudiantes y «Tiros al arco total Más 6.5» sufren si Estudiantes rota, y los «Menos» salen favorecidos. No cumple: la más cercana, remates total Menos 26.5 @1.70 (5/4, colchón +0.3). Las 12 con cuota < 1.20 (p. ej. tiros al arco total Más 4.5 @1.06) no aportan. Faltas, fueras, saques de banda y de meta: Betano no ofrece línea (la ficha solo trae el esperado: faltas 23.5, fueras 3.36, saques de banda 43.93, saques de meta 16.57).

### Tarjetas (puntos; esperado Estudiantes 3.64 · Rivadavia 2.36 · total 6.00)
| Línea | Cuota | Colchón | L | V | p modelo · EV |
|---|---|---|---|---|---|
| Total Menos 8.5 | 1.24 | +2.5 | 6 de 7 | 5 de 7 | 84 % · +4 % |
| Total Menos 7.5 | 1.42 | +1.5 | 5 de 7 | 5 de 7 | 75 % · +7 % |
| Rivadavia Menos 4.5 | 1.27 | n/d | 6 de 7 | 6 de 7 | 81 % · +3 % |

También cumplen Rivadavia Menos 3.5 @1.62, Estudiantes Más 1.5 @2.87 y «Ambos con 2+ Sí» @1.37 (5 y 6 de 7). Ver advertencias 3 y 4: no se usan «Más 0.5» de equipo ni «Ambos 1+». El total cae entre 5.5 y 6.5 (esperado 6.00), por eso no hay regularidad ahí. «Más tarjetas que»: no cumple ningún lado; la serie espera más tarjetas para Estudiantes pero la cuota es menor para Rivadavia. Las alertas del modelo (16–40 pts) están en tarjetas: los EV altos (Rivadavia Más 1.5 +56 %, Estudiantes Más 1.5 +44 %) vienen de esa brecha. Sin 1T.

### Goles y resultado (modelo copia el mercado; ver advertencia 2; liquidación sin verificar)
Mercado 1X2 sin margen 39/34/27 %; modelo 40/34/25 %. Cumplen con cuota ≥ 1.20 (ninguna con EV positivo, −2 %): Más 1.0 goles @1.28 (5 de 7 y 5 de 7, D 3/3, esperado 2.79), Estudiantes Menos 1.5 goles @1.33 (D 1/3, colchón +0.07), y las de resultado/hándicap (Estudiantes o empate @1.31, hándicap Estudiantes +1 @1.31, Rivadavia +0.75 @1.40) **que dependen de cómo liquide Betano la final**. No cumplen: el 1X2, ambos marcan, Más 2.5, hándicap −1.

---

## 2. Curazao – Panamá · 19:30
Muestra 7+7 (Curazao n = 6 en tarjetas), **1 directo** (4-4, 13-oct-2023). La muestra mezcla Mundial, Nations League y la Kirin Cup (amistosa que Flashscore marca como oficial). Árbitro Penso M. (sin estadística).

### Córners (esperado Curazao–Panamá total 8.07)
Solo cumple **Total Menos 10.5 @1.30** (L 6 de 7, V 6 de 7, D 1 de 1, colchón +2.4; p modelo 72 %, y el informe marca la cuota «por debajo de la justa»). No cumplen: total Más 6.5/7.5/8.5 (Curazao 5/7 pero Panamá 4/7; cuotas 1.26, 1.50, 1.87), Menos 9.5 @1.52 (4 y 5), líneas de equipo Más 2.5/3.5. 1T/2T: sin ficha.

### Tarjetas (esperado Curazao 1.60 · Panamá 2.00 · total 3.60)
Betano ofrece pocas líneas (total solo 2.5; equipos 0.5 y 1.5; 1T 0.5). Cumplen solo «Ambos con 1+ Sí» @1.45 (Curazao 5/6, Panamá 7/7; modelo p 58 %, EV −16 %; **afectado por la advertencia 3**), Panamá Más 0.5 @2.12 (6/6 y 7/7) y Curazao Más 0.5 @2.07 (5/6 y 5/7), también bajo la advertencia 3. No cumplen: total Más 2.5 @1.60 (6/6 y 4/7), las de 1.5 por equipo, «Ambos 2+», «Más tarjetas que», 1T. «Ambos 2+ No» @1.33 contradice la serie (por independencia ~52 % frente a 75 % implícito).

### Goles y resultado (modelo copia el mercado)
1X2: modelo 24/29/48 % (Panamá favorito leve) contra 24/29/47 % del mercado. Cumplen con cuota ≥ 1.20 (4 líneas, EV negativo): Hándicap Curazao +2 @1.26 (5/6, D 1/1), No hay empate @1.33 (5/7), Más 1.5 goles @1.39 (5/5, esperado 3.21, colchón +1.71), Curazao Más 0.5 goles @1.50 (5/6). **Sesgo de la muestra:** el esperado de la ficha (3.21 goles) está muy por encima de lo que cobra Betano (~2.45); un 6-1 y un 1-7 de Curazao inflan el promedio, así que los colchones de «Más» no miden probabilidad. Solo 1 directo; 39 días sin partido oficial.

---

## 3. Atl. Morelia – Leones Negros · 21:00
Ida de semifinal de la Liguilla de Expansión. Muestra 7+7, **7 directos** (abarcan 5 años), mezcla fase regular y liguilla; la liga base del modelo es Liga MX, no Expansión. Árbitro Sánchez M. E. L. (sin estadística). Sin alertas del modelo.

- **Córners:** ninguna línea cumple. Total Más 10.5 @2.02 (4 y 2, D 3/7, colchón −0.4); Menos 10.5 @1.75 (3 y 5, D 4/7, colchón +0.4). 1T 4.5: sin ficha.
- **Tarjetas, remates, tiros al arco, jugadores:** Betano no los ofrece.
- **Goles y resultado** (1X2 modelo 57/26/18 % contra 56/26/19 %; ninguna con EV positivo): Menos 3.5 goles @1.30 (6 y 5, D 6/7, esperado 3.14, colchón +0.36), No hay empate @1.25 (5 y 6, D 7/7), Más 1.5 goles @1.31 (7 y 6, D 7/7), Leones Más 0.5 goles @1.57 (7 y 6, D 5/7), Ambos marcan Sí @1.85 (7 y 5; D 2/7 y EV −11 %: cumple por regularidad pero los directos y la probabilidad no lo respaldan).

---

## Combinadas del mismo partido (agente `combinadas`)
Patas que cumplen (≥5 de 7 en ambos), de mercados distintos, evaluadas con `python3 -m supermodelo --combos`. **La «cuota total» es el producto de las individuales y es un techo**, no la cuota real del cupón de Betano; la «cuota mínima» (1.03/p) es la referencia del modelo, no una exigencia de Betano. No se verificó que el builder de Betano admita estas combinaciones. En goles y resultado el modelo copia el mercado (no es segunda opinión). Se excluyeron las tarjetas con aviso, «Más 0.5 de equipo» y «Ambos 1+», y no hay patas de jugadores. Los builders del informe del modelo se descartaron porque todos llevan alguna pata que no cumple.

| Partido | Combinada | Cuota techo | p | Cuota mínima | EV al techo | Stress (−5 pts/pata) |
|---|---|---|---|---|---|---|
| Estudiantes (E1) | Córners total Más 6.5 @1.24 + tiros al arco total Más 6.5 @1.30 + tarjetas total Menos 8.5 @1.24 | 2.00 | 50 % | 2.07 | −0.4 % | 46 % |
| Estudiantes (E6) | Córners total Más 6.5 + tiros al arco total Menos 10.5 @1.27 | 1.57 | 59 % | 1.75 | −7.7 % | 55 % |
| Estudiantes (E11) | Córners Rivadavia Más 2.5 @1.29 + Estudiantes o empate @1.31 | 1.69 | 57 % | 1.80 | −3.0 % | n/d |
| Curazao–Panamá (C8) | Córners total Menos 10.5 @1.30 + hándicap Curazao +2 @1.26 | 1.64 | 56 % | 1.84 | −8.4 % | 52 % |
| Morelia–Leones (M2) | Menos 3.5 goles @1.30 + No hay empate @1.25 | 1.62 | 56 % | 1.84 | −9.1 % | 52 % |

- **Ninguna tiene EV positivo.** E1 es la única que roza el techo de precio (cuota justa 2.01 contra techo 2.00) y comparte la pata «córners Más 6.5» con E6 (no son combinadas independientes). Su pata más frágil es tiros al arco Más 6.5.
- **Rotación de Estudiantes:** es un escenario del agente (−10 pts en las patas que dependen del once), no una estimación del modelo. E1 bajaría a ~38 % (cuota justa ~2.67 frente a techo 2.00), E6 a ~51 % y E11 a ~50 %.
- **E11 contiene una pata no verificada** («Estudiantes o empate»): depende de si Betano liquida a 90 minutos o con prórroga y penales.
- **C8 y M2** tienen correlación ~1.0 entre patas y margen acumulado de 6 % y 11 %. El colchón de Menos 3.5 en Morelia es solo +0.36.
- **Morelia M6** (Más 1.5 goles + Leones marcan, cuota 2.06, EV +6.2 %) tiene patas casi redundantes (si Leones marca, hay 2 o más goles en ~89 % de los casos): ese EV es un artefacto del producto y no se recomienda.
- Curazao–Panamá no tiene tarjetas utilizables (las que cumplen están excluidas por la advertencia 3); alternativas del agente: córners Menos 10.5 + Más 1.5 goles @1.39 (cuota 1.81, p 52 %).

## Lo que no cumple, resumido
- **Córners:** nada en Morelia; en Curazao–Panamá todo salvo el total Menos 10.5; en Estudiantes, el centro del mercado y los «Más» altos.
- **Remates/tiros al arco (solo Estudiantes):** las líneas de dos o más escalones de Rivadavia/Estudiantes fuera de las listadas; cualquier línea por debajo de 5 de 7 en un equipo.
- **Tarjetas:** el total de Estudiantes en 5.5–6.5, casi todas las líneas por equipo, «Más tarjetas que» en ambos partidos, y todo el 1T.
- **Goles/resultado:** el 1X2 de Estudiantes (gana 1/7 y 2/7), ambos marcan y Más 2.5 en Estudiantes, Más 2.5 y Menos en varias líneas de Curazao–Panamá.

## Límites y fallas
- **Sin alineaciones, historial por jugador ni estadísticas de árbitro.** Mercados de jugadores no analizados. Bajas en Estudiantes (Correa, Castro) y Rivadavia (Arce) vienen de la previa de Flashscore, sin hora; Betano aún lista líneas de los tres (anota, tarjeta, remates, tiros al arco): **no usar esas líneas si la baja se confirma**. Si Flashscore publica alineaciones antes del partido, hay que recolectarlas con `recoleccion/flashscore_alineaciones.js` y guardar `jugadores/<clave>.json`.
- **Liquidación de la final** sin verificar (advertencia 1).
- **Cuotas de tarjetas incoherentes** sin resolver (advertencia 3).
- **Sin estadística por tiempo**: ninguna ficha de 1T/2T en ningún partido, aunque Betano ofrece las líneas.
- **Muestras pequeñas** (5 de 7); solo 3, 1 y 7 directos; Curazao con n = 6 en tarjetas; muestra de Curazao–Panamá mezcla Mundial, Nations League y Kirin Cup; la de Morelia mezcla fase regular y liguilla.
- **Contexto:** las notas de situación se escribieron desde la previa de Flashscore; las tablas de las ligas no se leyeron. La ficha de Estudiantes marca `rotacion=False`, pero la rotación por la final de la Libertadores figura en las dudas.
- **Criterios** vienen de tipsters y medios sin resultados verificados. El EV se informa y no manda.
