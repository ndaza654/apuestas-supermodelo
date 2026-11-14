# Goles y resultado · sábado 14-nov-2026 (21 partidos)

Generado por el agente goles-resultado. Muestra de 7 por equipo (cumple = 5 de 7 en ambos, n mín. 5), directos hasta 6. Fuentes: `registro/lineas.csv` (mercado goles), `informes/<slug>_resultado.json` (modelo SM-1.2), `fichas/ficha_<slug>.json`. Horas Bogotá. Cuotas de Betano leídas el 14-nov ~00:06 UTC (13-nov ~19:06 Bogotá; ver `cuotas_leidas` en cada fila).

**Ajuste de calibración aplicado:** `p ajustada = p_modelo − 7 pts` (punto medio del recorte de 6–8 pts por la calibración del 12 y 13-nov: goles Menos 78 % real vs 87 % modelo, Más 70 % vs 76 %). Se marca **PROTECCIÓN** lo que paga < 1,50. EV = p·cuota − 1 (informativo); se da con la p cruda y con la ajustada.

**Alertas:** en los 21 informes no hay ninguna alerta sobre líneas de goles, resultado ni ambos marcan; las alertas (7 de 21 partidos: Noruega, Almería, Portugal, Suecia, Atl. Nacional, Millonarios, Chapecoense; 1–4 por partido) están solo en córners, «Más córners» (especial) y saques de banda. Los 1X2 del modelo coinciden con el mercado sin margen (ver tablas). La columna `alerta_modelo` del CSV está vacía en las 1.192 filas de goles.


---

## 05:15 · Japón - Brasil (Internacional Amistosos)

Competición/contexto: importancia «normal»; tabla: sin dato; bajas: ninguna anotada; clima: 15.1 °C al inicio, humedad 71 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 4.1 km/h (código OMM al inicio 2) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Japón | 3.9 | 23 % | 24 % | -0.7 | -0.10 |
| Empate | 3.8 | 25 % | 25 % | +0.2 | -0.06 |
| Gana Brasil | 1.88 | 52 % | 52 % | +0.6 | -0.02 |

Favorito del modelo: **visitante** (53 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 4 de 7, no perdió 6 de 7, perdió 1 de 7; visitante ganó 4 de 7, no perdió 5 de 7, perdió 2 de 7. Directos (n=1) con ambos marcan: 1 de 1. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 4 de 7 · V perdió 2 de 7 → no
- Gana visitante: V ganó 4 de 7 · L perdió 1 de 7 → no
- Local o empate: L no perdió 6 de 7 · V no ganó 3 de 7 → no
- Visitante o empate: V no perdió 5 de 7 · L no ganó 3 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Japón o empate | 1.95 | 48 % | 48 % | -0.07 |
| Brasil o empate | 1.28 | 77 % | 76 % | -0.02 |
| No hay empate | 1.26 | 75 % | 75 % | -0.05 |

**Ambos marcan** (L ambos marcan 4 de 7, V 3 de 7, directos 1 de 1):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.6 | 60 % | 59 % | -0.05 | L 4 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 2.25 | 40 % | 41 % | -0.09 | L 3 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Japón | 4.25 | 20 % | 21 % | -0.14 |
| 1.er tiempo: Empate | 2.27 | 41 % | 41 % | -0.07 |
| 1.er tiempo: Brasil | 2.42 | 39 % | 38 % | -0.06 |
| 2.º tiempo: Japón | 3.7 | 23 % | 24 % | -0.14 |
| 2.º tiempo: Empate | 2.7 | 34 % | 34 % | -0.07 |
| 2.º tiempo: Brasil | 2.18 | 42 % | 43 % | -0.08 |
| Descanso o final: Japón | 2.65 | 33 % | 35 % | -0.13 |
| Descanso o final: Empate | 1.75 | 52 % | 53 % | -0.08 |
| Descanso o final: Brasil | 1.57 | 60 % | 60 % | -0.06 |
| Descanso/final: Japón / Japón | 6.5 | 12 % | 13 % | -0.21 |
| Descanso/final: Japón / Empate | 15.0 | 5 % | 5 % | -0.25 |
| Descanso/final: Japón / Brasil | 24.0 | 3 % | 3 % | -0.26 |
| Descanso/final: Empate / Japón | 8.75 | 9 % | 9 % | -0.21 |
| Descanso/final: Empate / Empate | 5.8 | 14 % | 14 % | -0.17 |
| Descanso/final: Empate / Brasil | 4.8 | 18 % | 18 % | -0.16 |
| Descanso/final: Brasil / Japón | 37.0 | 2 % | 2 % | -0.30 |
| Descanso/final: Brasil / Empate | 13.5 | 6 % | 6 % | -0.24 |
| Descanso/final: Brasil / Brasil | 2.92 | 31 % | 31 % | -0.08 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.36 | 72 % | 71 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 3.1 | 28 % | 29 % | -0.14 |
| Goles 1.er tiempo Más 0.75 | 1.47 | 67 % | 66 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.67 | 34 % | 35 % | -0.09 |
| Goles 1.er tiempo Más 1.0 | 1.72 | 58 % | 57 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.15 | 44 % | 45 % | -0.05 |
| Goles 1.er tiempo Más 1.25 | 2.15 | 45 % | 44 % | -0.02 |
| Goles 1.er tiempo Menos 1.25 | 1.72 | 55 % | 56 % | -0.05 |
| Goles 1.er tiempo Más 1.5 | 2.5 | 38 % | 37 % | -0.06 |
| Goles 1.er tiempo Menos 1.5 | 1.52 | 62 % | 63 % | -0.05 |
| Goles 1.er tiempo Más 2.5 | 5.6 | 14 % | 14 % | -0.19 |
| Goles 1.er tiempo Menos 2.5 | 1.14 | 86 % | 86 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 11.0 | 4 % | 4 % | -0.53 |
| Goles 1.er tiempo Menos 3.5 | 1.03 | 96 % | 96 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.19 | 81 % | 82 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 4.55 | 19 % | 18 % | -0.15 |
| Goles 2.º tiempo Más 1.5 | 1.85 | 50 % | 51 % | -0.08 |
| Goles 2.º tiempo Menos 1.5 | 1.93 | 50 % | 49 % | -0.03 |
| Goles 2.º tiempo Más 2.5 | 3.5 | 24 % | 25 % | -0.17 |
| Goles 2.º tiempo Menos 2.5 | 1.29 | 76 % | 75 % | -0.01 |

**Goles, esperado ficha:** local 1.21, visitante 1.36, total 2.57 (modelo: λ local 1.17, visitante 1.80). Muestra local 7, visitante 7, directos 1.

**Líneas de goles que cumplen 5 de 7 en ambos (8):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.1 | 1.21 | 1.29 | 6 de 7 | 7 de 7 | 1 de 1 | 89 % | 82 % | 89 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Más 0.5 | 1.05 | 2.57 | 2.07 | 7 de 7 | 7 de 7 | 1 de 1 | 95 % | 88 % | 94 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 1.5 | 1.23 | 2.57 | 1.07 | 5 de 7 | 6 de 7 | 1 de 1 | 80 % | 73 % | 80 % | -0.02 | -0.11 | PROTECCIÓN |
| total | Menos 3.5 | 1.5 | 2.57 | 0.93 | 5 de 7 | 7 de 7 | 1 de 1 | 65 % | 58 % | 65 % | -0.02 | -0.13 |  |
| total | Menos 3.75 | 1.38 | 2.57 | 1.18 | 5 de 7 | 7 de 7 | 1 de 1 | 71 % | 64 % | 71 % | -0.01 | -0.11 | PROTECCIÓN |
| total | Menos 4.5 | 1.2 | 2.57 | 1.93 | 7 de 7 | 7 de 7 | 1 de 1 | 82 % | 75 % | 82 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.08 | 2.57 | 2.93 | 7 de 7 | 7 de 7 | 1 de 1 | 92 % | 85 % | 91 % | -0.01 | -0.09 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.1 | 1.36 | 2.14 | 7 de 7 | 7 de 7 | 1 de 1 | 90 % | 83 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (53 %) en línea con el mercado; total esperado ficha 2.57 vs modelo 2.97. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 3.75 @1.38 (p 71 %, aj. 64 %).


---

## 08:00 · Real Valladolid - CD Castellón (España Segunda División)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 12, 'equipo': 'Real Valladolid', 'pj': 13, 'g': 5, 'e': 3, 'p': 5, 'gf_gc': '22:20', 'dg': 2, 'pts': 18, 'grupo': ''}, 'visitante': {'pos': 2, 'equipo': 'Castellón', 'pj': 12, 'g': 8, 'e': 3, 'p': 1, 'gf_gc': '23:5', 'dg': 18, 'pts': 27, 'grupo': ''}}; bajas: ninguna anotada; clima: 13.7 °C al inicio, humedad 79 %, prob. de lluvia máx. 80 %, lluvia máx. 0.3 mm/h, viento máx. 16.9 km/h (código OMM al inicio 80) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Real Valladolid | 3.05 | 31 % | 31 % | -0.4 | -0.06 |
| Empate | 3.6 | 27 % | 26 % | +0.4 | -0.04 |
| Gana CD Castellón | 2.25 | 43 % | 43 % | +0.0 | -0.04 |

Favorito del modelo: **visitante** (43 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 4 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 4 de 7, no perdió 6 de 7, perdió 1 de 7. Directos (n=2) con ambos marcan: 0 de 2. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 4 de 7 · V perdió 1 de 7 → no
- Gana visitante: V ganó 4 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 3 de 7 → no
- Visitante o empate: V no perdió 6 de 7 · L no ganó 3 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Real Valladolid o empate | 1.67 | 57 % | 57 % | -0.04 |
| CD Castellón o empate | 1.4 | 69 % | 69 % | -0.03 |
| No hay empate | 1.28 | 73 % | 74 % | -0.06 |

**Ambos marcan** (L ambos marcan 5 de 7, V 2 de 7, directos 0 de 2):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.6 | 60 % | 60 % | -0.04 | L 5 de 7 · V 2 de 7 → no |
| Ambos marcan: No | 2.27 | 40 % | 40 % | -0.09 | L 2 de 7 · V 5 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Real Valladolid | 3.5 | 25 % | 26 % | -0.11 |
| 1.er tiempo: Empate | 2.22 | 42 % | 42 % | -0.08 |
| 1.er tiempo: CD Castellón | 2.82 | 33 % | 32 % | -0.07 |
| 2.º tiempo: Real Valladolid | 3.15 | 28 % | 28 % | -0.12 |
| 2.º tiempo: Empate | 2.62 | 36 % | 35 % | -0.07 |
| 2.º tiempo: CD Castellón | 2.5 | 36 % | 37 % | -0.09 |
| Descanso o final: Real Valladolid | 2.2 | 41 % | 42 % | -0.11 |
| Descanso o final: Empate | 1.7 | 54 % | 55 % | -0.08 |
| Descanso o final: CD Castellón | 1.8 | 52 % | 52 % | -0.07 |
| Descanso/final: Real Valladolid / Real Valladolid | 5.0 | 17 % | 17 % | -0.16 |
| Descanso/final: Real Valladolid / Empate | 14.0 | 6 % | 6 % | -0.21 |
| Descanso/final: Real Valladolid / CD Castellón | 25.0 | 3 % | 3 % | -0.28 |
| Descanso/final: Empate / Real Valladolid | 7.0 | 12 % | 12 % | -0.19 |
| Descanso/final: Empate / Empate | 5.6 | 15 % | 15 % | -0.16 |
| Descanso/final: Empate / CD Castellón | 5.5 | 15 % | 15 % | -0.17 |
| Descanso/final: CD Castellón / Real Valladolid | 32.0 | 2 % | 2 % | -0.25 |
| Descanso/final: CD Castellón / Empate | 14.0 | 6 % | 6 % | -0.18 |
| Descanso/final: CD Castellón / CD Castellón | 3.6 | 25 % | 24 % | -0.11 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.37 | 72 % | 71 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 3.05 | 28 % | 29 % | -0.13 |
| Goles 1.er tiempo Más 0.75 | 1.5 | 66 % | 65 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.6 | 35 % | 36 % | -0.08 |
| Goles 1.er tiempo Más 1.0 | 1.75 | 56 % | 56 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.1 | 45 % | 46 % | -0.05 |
| Goles 1.er tiempo Más 1.25 | 2.18 | 44 % | 44 % | -0.03 |
| Goles 1.er tiempo Menos 1.25 | 1.7 | 57 % | 57 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 2.57 | 36 % | 36 % | -0.07 |
| Goles 1.er tiempo Menos 1.5 | 1.5 | 64 % | 64 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 5.8 | 14 % | 13 % | -0.21 |
| Goles 1.er tiempo Menos 2.5 | 1.13 | 86 % | 87 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 11.25 | 4 % | 4 % | -0.54 |
| Goles 1.er tiempo Menos 3.5 | 1.03 | 96 % | 96 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.2 | 80 % | 81 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 4.4 | 20 % | 19 % | -0.14 |
| Goles 2.º tiempo Más 1.5 | 1.9 | 48 % | 50 % | -0.08 |
| Goles 2.º tiempo Menos 1.5 | 1.88 | 52 % | 50 % | -0.03 |
| Goles 2.º tiempo Más 2.5 | 3.65 | 22 % | 23 % | -0.18 |
| Goles 2.º tiempo Menos 2.5 | 1.27 | 78 % | 77 % | -0.01 |

**Goles, esperado ficha:** local 1.43, visitante 1.79, total 3.21 (modelo: λ local 1.32, visitante 1.58). Muestra local 7, visitante 7, directos 2.

**Líneas de goles que cumplen 5 de 7 en ambos (7):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.14 | 1.43 | 1.07 | 5 de 7 | 7 de 7 | 2 de 2 | 86 % | 79 % | 86 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 3.5 | 1.03 | 1.43 | 2.07 | 5 de 7 | 7 de 7 | 2 de 2 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.05 | 3.21 | 2.71 | 7 de 7 | 7 de 7 | 2 de 2 | 94 % | 87 % | 94 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 1.5 | 1.24 | 3.21 | 1.71 | 6 de 7 | 6 de 7 | 1 de 2 | 79 % | 72 % | 79 % | -0.03 | -0.11 | PROTECCIÓN |
| total | Menos 5.5 | 1.07 | 3.21 | 2.29 | 6 de 7 | 7 de 7 | 2 de 2 | 93 % | 86 % | 92 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.21 | 1.79 | 1.29 | 5 de 7 | 6 de 7 | 1 de 2 | 80 % | 73 % | 80 % | -0.03 | -0.11 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.06 | 1.79 | 1.71 | 7 de 7 | 6 de 7 | 1 de 2 | 93 % | 86 % | 93 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (43 %) en línea con el mercado; total esperado ficha 3.21 vs modelo 2.90. No hay línea que cumpla con cuota ≥ 1,30 (solo protecciones o ninguna).


---

## 09:00 · Kosovo - Israel (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 2, 'equipo': 'Kosovo', 'pj': 4, 'g': 1, 'e': 2, 'p': 1, 'gf_gc': '3:4', 'dg': -1, 'pts': 5, 'grupo': 'GRUPO 3'}, 'visitante': {'pos': 4, 'equipo': 'Israel', 'pj': 4, 'g': 0, 'e': 2, 'p': 2, 'gf_gc': '2:7', 'dg': -5, 'pts': 2, 'grupo': 'GRUPO 3'}}; bajas: ninguna anotada; clima: 3.4 °C al inicio, humedad 84 %, prob. de lluvia máx. 40 %, lluvia máx. 0.5 mm/h, viento máx. 13.6 km/h (código OMM al inicio 61) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Kosovo | 1.82 | 54 % | 53 % | +0.5 | -0.02 |
| Empate | 3.65 | 26 % | 26 % | +0.0 | -0.06 |
| Gana Israel | 4.4 | 21 % | 21 % | -0.5 | -0.09 |

Favorito del modelo: **local** (54 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 2 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 1 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=3) con ambos marcan: 1 de 3. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 2 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 1 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 6 de 7 → sí
- Visitante o empate: V no perdió 3 de 7 · L no ganó 5 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Kosovo o empate | 1.23 | 79 % | 79 % | -0.02 |
| Israel o empate | 2.02 | 46 % | 47 % | -0.07 |
| No hay empate | 1.27 | 74 % | 74 % | -0.06 |

**Ambos marcan** (L ambos marcan 4 de 7, V 3 de 7, directos 1 de 3):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.8 | 51 % | 52 % | -0.08 | L 4 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 1.95 | 49 % | 48 % | -0.05 | L 3 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Kosovo | 2.42 | 39 % | 38 % | -0.06 |
| 1.er tiempo: Empate | 2.18 | 43 % | 43 % | -0.06 |
| 1.er tiempo: Israel | 4.6 | 18 % | 19 % | -0.16 |
| 2.º tiempo: Kosovo | 2.12 | 43 % | 44 % | -0.08 |
| 2.º tiempo: Empate | 2.55 | 37 % | 36 % | -0.07 |
| 2.º tiempo: Israel | 4.2 | 20 % | 21 % | -0.15 |
| Descanso o final: Kosovo | 1.55 | 60 % | 60 % | -0.06 |
| Descanso o final: Empate | 1.72 | 53 % | 54 % | -0.08 |
| Descanso o final: Israel | 2.87 | 30 % | 33 % | -0.14 |
| Descanso/final: Kosovo / Kosovo | 2.82 | 32 % | 32 % | -0.09 |
| Descanso/final: Kosovo / Empate | 15.5 | 5 % | 5 % | -0.26 |
| Descanso/final: Kosovo / Israel | 50.0 | 2 % | 1 % | -0.25 |
| Descanso/final: Empate / Kosovo | 4.6 | 18 % | 18 % | -0.15 |
| Descanso/final: Empate / Empate | 5.3 | 16 % | 16 % | -0.15 |
| Descanso/final: Empate / Israel | 9.0 | 9 % | 9 % | -0.22 |
| Descanso/final: Israel / Kosovo | 24.0 | 3 % | 3 % | -0.31 |
| Descanso/final: Israel / Empate | 15.0 | 5 % | 5 % | -0.27 |
| Descanso/final: Israel / Israel | 7.4 | 10 % | 11 % | -0.23 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.42 | 68 % | 68 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.85 | 32 % | 32 % | -0.10 |
| Goles 1.er tiempo Más 0.75 | 1.57 | 62 % | 62 % | -0.03 |
| Goles 1.er tiempo Menos 0.75 | 2.42 | 39 % | 39 % | -0.05 |
| Goles 1.er tiempo Más 1.0 | 1.87 | 52 % | 52 % | -0.04 |
| Goles 1.er tiempo Menos 1.0 | 1.93 | 50 % | 50 % | -0.03 |
| Goles 1.er tiempo Más 1.25 | 2.35 | 40 % | 40 % | -0.06 |
| Goles 1.er tiempo Menos 1.25 | 1.6 | 61 % | 61 % | -0.02 |
| Goles 1.er tiempo Más 1.5 | 2.77 | 32 % | 33 % | -0.11 |
| Goles 1.er tiempo Menos 1.5 | 1.44 | 68 % | 67 % | -0.02 |
| Goles 1.er tiempo Más 2.5 | 6.4 | 11 % | 11 % | -0.27 |
| Goles 1.er tiempo Menos 2.5 | 1.11 | 89 % | 89 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.25 | 77 % | 78 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 3.9 | 23 % | 22 % | -0.09 |
| Goles 2.º tiempo Más 1.5 | 2.07 | 43 % | 45 % | -0.11 |
| Goles 2.º tiempo Menos 1.5 | 1.72 | 57 % | 55 % | -0.02 |
| Goles 2.º tiempo Más 2.5 | 4.25 | 18 % | 19 % | -0.22 |
| Goles 2.º tiempo Menos 2.5 | 1.21 | 82 % | 81 % | -0.01 |

**Goles, esperado ficha:** local 1.71, visitante 1.07, total 2.79 (modelo: λ local 1.69, visitante 0.99). Muestra local 7, visitante 7, directos 3.

**Líneas de goles que cumplen 5 de 7 en ambos (7):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.18 | 1.71 | 1.21 | 5 de 7 | 6 de 7 | 2 de 3 | 82 % | 75 % | 82 % | -0.03 | -0.12 | PROTECCIÓN |
| local | Menos 3.5 | 1.07 | 1.71 | 1.79 | 6 de 7 | 6 de 7 | 3 de 3 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 0.5 | 1.06 | 2.79 | 2.29 | 6 de 7 | 6 de 7 | 2 de 3 | 92 % | 85 % | 93 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 4.5 | 1.13 | 2.79 | 1.71 | 6 de 7 | 5 de 7 | 3 de 3 | 88 % | 81 % | 87 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 5.5 | 1.05 | 2.79 | 2.71 | 6 de 7 | 7 de 7 | 3 de 3 | 95 % | 88 % | 94 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Menos 1.5 | 1.31 | 1.07 | 0.43 | 5 de 7 | 6 de 7 | 3 de 3 | 75 % | 68 % | 74 % | -0.02 | -0.12 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.07 | 1.07 | 1.43 | 5 de 7 | 6 de 7 | 3 de 3 | 93 % | 86 % | 92 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (54 %) en línea con el mercado; total esperado ficha 2.79 vs modelo 2.67. Mejor línea con cuota ≥ 1,30 que cumple: visitante Menos 1.5 @1.31 (p 75 %, aj. 68 %).


---

## 10:15 · Real Sociedad II - Sporting de Gijón (España Segunda División)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 18, 'equipo': 'Real Sociedad B', 'pj': 13, 'g': 3, 'e': 3, 'p': 7, 'gf_gc': '15:22', 'dg': -7, 'pts': 12, 'grupo': ''}, 'visitante': {'pos': 7, 'equipo': 'Real Sporting', 'pj': 13, 'g': 7, 'e': 1, 'p': 5, 'gf_gc': '14:15', 'dg': -1, 'pts': 22, 'grupo': ''}}; bajas: ninguna anotada; clima: 16.9 °C al inicio, humedad 76 %, prob. de lluvia máx. 78 %, lluvia máx. 0.3 mm/h, viento máx. 9.4 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Real Sociedad II | 2.47 | 39 % | 39 % | -0.2 | -0.05 |
| Empate | 3.3 | 29 % | 29 % | +0.1 | -0.05 |
| Gana Sporting de Gijón | 2.92 | 33 % | 33 % | +0.1 | -0.05 |

Favorito del modelo: **local** (38 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 2 de 7, no perdió 3 de 7, perdió 4 de 7; visitante ganó 5 de 7, no perdió 5 de 7, perdió 2 de 7. Directos (n=3) con ambos marcan: 1 de 3. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 2 de 7 · V perdió 2 de 7 → no
- Gana visitante: V ganó 5 de 7 · L perdió 4 de 7 → no
- Local o empate: L no perdió 3 de 7 · V no ganó 2 de 7 → no
- Visitante o empate: V no perdió 5 de 7 · L no ganó 5 de 7 → sí

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Real Sociedad II o empate | 1.42 | 67 % | 67 % | -0.04 |
| Sporting de Gijón o empate | 1.57 | 61 % | 61 % | -0.04 |
| No hay empate | 1.32 | 71 % | 71 % | -0.06 |

**Ambos marcan** (L ambos marcan 3 de 7, V 4 de 7, directos 1 de 3):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.75 | 54 % | 54 % | -0.06 | L 3 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 2.02 | 46 % | 46 % | -0.07 | L 4 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Real Sociedad II | 3.1 | 29 % | 29 % | -0.09 |
| 1.er tiempo: Empate | 2.07 | 45 % | 45 % | -0.07 |
| 1.er tiempo: Sporting de Gijón | 3.55 | 26 % | 25 % | -0.08 |
| 2.º tiempo: Real Sociedad II | 2.72 | 33 % | 33 % | -0.10 |
| 2.º tiempo: Empate | 2.45 | 38 % | 38 % | -0.06 |
| 2.º tiempo: Sporting de Gijón | 3.1 | 29 % | 29 % | -0.11 |
| Descanso o final: Real Sociedad II | 1.91 | 47 % | 49 % | -0.09 |
| Descanso o final: Empate | 1.62 | 57 % | 58 % | -0.08 |
| Descanso o final: Sporting de Gijón | 2.18 | 42 % | 43 % | -0.09 |
| Descanso/final: Real Sociedad II / Real Sociedad II | 4.05 | 22 % | 22 % | -0.12 |
| Descanso/final: Real Sociedad II / Empate | 14.0 | 5 % | 6 % | -0.25 |
| Descanso/final: Real Sociedad II / Sporting de Gijón | 35.0 | 2 % | 2 % | -0.26 |
| Descanso/final: Empate / Real Sociedad II | 5.6 | 15 % | 15 % | -0.18 |
| Descanso/final: Empate / Empate | 4.8 | 18 % | 18 % | -0.14 |
| Descanso/final: Empate / Sporting de Gijón | 6.4 | 13 % | 13 % | -0.19 |
| Descanso/final: Sporting de Gijón / Real Sociedad II | 30.0 | 2 % | 2 % | -0.29 |
| Descanso/final: Sporting de Gijón / Empate | 14.5 | 5 % | 5 % | -0.21 |
| Descanso/final: Sporting de Gijón / Sporting de Gijón | 4.9 | 18 % | 17 % | -0.13 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.45 | 67 % | 66 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.67 | 33 % | 34 % | -0.12 |
| Goles 1.er tiempo Más 0.75 | 1.65 | 60 % | 59 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.27 | 41 % | 42 % | -0.07 |
| Goles 1.er tiempo Más 1.0 | 2.0 | 49 % | 48 % | -0.02 |
| Goles 1.er tiempo Menos 1.0 | 1.82 | 53 % | 53 % | -0.04 |
| Goles 1.er tiempo Más 1.25 | 2.52 | 38 % | 37 % | -0.04 |
| Goles 1.er tiempo Menos 1.25 | 1.53 | 63 % | 64 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 2.95 | 31 % | 30 % | -0.09 |
| Goles 1.er tiempo Menos 1.5 | 1.39 | 69 % | 70 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 6.9 | 10 % | 10 % | -0.30 |
| Goles 1.er tiempo Menos 2.5 | 1.09 | 90 % | 90 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.26 | 76 % | 77 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 3.75 | 24 % | 23 % | -0.11 |
| Goles 2.º tiempo Más 1.5 | 2.12 | 43 % | 44 % | -0.10 |
| Goles 2.º tiempo Menos 1.5 | 1.7 | 57 % | 56 % | -0.02 |
| Goles 2.º tiempo Más 2.5 | 4.4 | 18 % | 19 % | -0.22 |
| Goles 2.º tiempo Menos 2.5 | 1.2 | 82 % | 81 % | -0.01 |

**Goles, esperado ficha:** local 1.43, visitante 1.71, total 3.14 (modelo: λ local 1.35, visitante 1.22). Muestra local 7, visitante 7, directos 3.

**Líneas de goles que cumplen 5 de 7 en ambos (5):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.29 | 1.43 | 0.93 | 5 de 7 | 5 de 7 | 1 de 3 | 75 % | 68 % | 75 % | -0.04 | -0.13 | PROTECCIÓN |
| local | Menos 2.5 | 1.15 | 1.43 | 1.07 | 6 de 7 | 6 de 7 | 3 de 3 | 85 % | 78 % | 85 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 3.5 | 1.04 | 1.43 | 2.07 | 6 de 7 | 6 de 7 | 3 de 3 | 96 % | 89 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.07 | 3.14 | 2.64 | 6 de 7 | 7 de 7 | 3 de 3 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 5.5 | 1.04 | 3.14 | 2.36 | 6 de 7 | 7 de 7 | 3 de 3 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (38 %) en línea con el mercado; total esperado ficha 3.14 vs modelo 2.57. No hay línea que cumpla con cuota ≥ 1,30 (solo protecciones o ninguna).


---

## 12:00 · Georgia - Hungría (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 4, 'equipo': 'Georgia', 'pj': 4, 'g': 0, 'e': 2, 'p': 2, 'gf_gc': '0:2', 'dg': -2, 'pts': 2, 'grupo': 'GRUPO 2'}, 'visitante': {'pos': 2, 'equipo': 'Hungría', 'pj': 4, 'g': 2, 'e': 1, 'p': 1, 'gf_gc': '3:2', 'dg': 1, 'pts': 7, 'grupo': 'GRUPO 2'}}; bajas: ninguna anotada; clima: 16.3 °C al inicio, humedad 54 %, prob. de lluvia máx. 38 %, lluvia máx. 0.1 mm/h, viento máx. 21.3 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Georgia | 3.05 | 31 % | 31 % | -0.3 | -0.06 |
| Empate | 3.1 | 31 % | 31 % | +0.4 | -0.04 |
| Gana Hungría | 2.5 | 38 % | 38 % | -0.1 | -0.05 |

Favorito del modelo: **visitante** (38 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 0 de 7, no perdió 2 de 7, perdió 5 de 7; visitante ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7. Directos (n=1) con ambos marcan: 0 de 1. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 0 de 7 · V perdió 2 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 5 de 7 → no
- Local o empate: L no perdió 2 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 5 de 7 · L no ganó 7 de 7 → sí

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Georgia o empate | 1.57 | 62 % | 62 % | -0.03 |
| Hungría o empate | 1.4 | 69 % | 69 % | -0.03 |
| No hay empate | 1.35 | 69 % | 69 % | -0.07 |

**Ambos marcan** (L ambos marcan 2 de 7, V 3 de 7, directos 0 de 1):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 2.05 | 45 % | 45 % | -0.07 | L 2 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 1.72 | 55 % | 55 % | -0.06 | L 5 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Georgia | 3.7 | 24 % | 24 % | -0.11 |
| 1.er tiempo: Empate | 2.0 | 48 % | 47 % | -0.04 |
| 1.er tiempo: Hungría | 3.15 | 28 % | 29 % | -0.11 |
| 2.º tiempo: Georgia | 3.4 | 26 % | 26 % | -0.12 |
| 2.º tiempo: Empate | 2.2 | 43 % | 42 % | -0.06 |
| 2.º tiempo: Hungría | 2.87 | 31 % | 32 % | -0.11 |
| Descanso o final: Georgia | 2.3 | 39 % | 41 % | -0.10 |
| Descanso o final: Empate | 1.6 | 59 % | 58 % | -0.06 |
| Descanso o final: Hungría | 1.98 | 46 % | 47 % | -0.09 |
| Descanso/final: Georgia / Georgia | 4.9 | 17 % | 17 % | -0.16 |
| Descanso/final: Georgia / Empate | 15.0 | 5 % | 5 % | -0.25 |
| Descanso/final: Georgia / Hungría | 37.0 | 2 % | 2 % | -0.31 |
| Descanso/final: Empate / Georgia | 6.7 | 12 % | 12 % | -0.18 |
| Descanso/final: Empate / Empate | 4.25 | 21 % | 20 % | -0.12 |
| Descanso/final: Empate / Hungría | 5.7 | 15 % | 15 % | -0.15 |
| Descanso/final: Hungría / Georgia | 45.0 | 2 % | 2 % | -0.32 |
| Descanso/final: Hungría / Empate | 15.5 | 5 % | 5 % | -0.23 |
| Descanso/final: Hungría / Hungría | 3.9 | 22 % | 22 % | -0.15 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.53 | 62 % | 63 % | -0.05 |
| Goles 1.er tiempo Menos 0.5 | 2.47 | 38 % | 37 % | -0.06 |
| Goles 1.er tiempo Más 0.75 | 1.75 | 54 % | 55 % | -0.05 |
| Goles 1.er tiempo Menos 0.75 | 2.1 | 46 % | 46 % | -0.02 |
| Goles 1.er tiempo Más 1.0 | 2.25 | 42 % | 43 % | -0.06 |
| Goles 1.er tiempo Menos 1.0 | 1.65 | 60 % | 59 % | -0.01 |
| Goles 1.er tiempo Más 1.25 | 2.82 | 32 % | 33 % | -0.09 |
| Goles 1.er tiempo Menos 1.25 | 1.44 | 69 % | 68 % | -0.01 |
| Goles 1.er tiempo Más 1.5 | 3.3 | 26 % | 27 % | -0.15 |
| Goles 1.er tiempo Menos 1.5 | 1.32 | 74 % | 73 % | -0.02 |
| Goles 1.er tiempo Más 2.5 | 7.9 | 8 % | 8 % | -0.39 |
| Goles 1.er tiempo Menos 2.5 | 1.07 | 92 % | 92 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.39 | 69 % | 70 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 2.95 | 31 % | 30 % | -0.09 |
| Goles 2.º tiempo Más 1.5 | 2.7 | 33 % | 34 % | -0.10 |
| Goles 2.º tiempo Menos 1.5 | 1.45 | 67 % | 66 % | -0.03 |
| Goles 2.º tiempo Más 2.5 | 6.1 | 12 % | 12 % | -0.29 |
| Goles 2.º tiempo Menos 2.5 | 1.11 | 88 % | 88 % | -0.02 |

**Goles, esperado ficha:** local 0.64, visitante 1.43, total 2.07 (modelo: λ local 1.02, visitante 1.16). Muestra local 7, visitante 7, directos 1.

**Líneas de goles que cumplen 5 de 7 en ambos (7):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 1.5 | 1.33 | 0.64 | 0.86 | 7 de 7 | 5 de 7 | 1 de 1 | 73 % | 66 % | 73 % | -0.03 | -0.12 | PROTECCIÓN |
| local | Menos 2.5 | 1.07 | 0.64 | 1.86 | 7 de 7 | 6 de 7 | 1 de 1 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 0.5 | 1.11 | 2.07 | 1.57 | 5 de 7 | 6 de 7 | 1 de 1 | 88 % | 81 % | 89 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 3.5 | 1.2 | 2.07 | 1.43 | 5 de 7 | 5 de 7 | 1 de 1 | 82 % | 75 % | 82 % | -0.01 | -0.10 | PROTECCIÓN |
| total | Menos 4.5 | 1.06 | 2.07 | 2.43 | 6 de 7 | 6 de 7 | 1 de 1 | 93 % | 86 % | 93 % | -0.01 | -0.09 | PROTECCIÓN |
| visitante | Más 0.5 | 1.38 | 1.43 | 0.93 | 5 de 7 | 5 de 7 | 1 de 1 | 69 % | 62 % | 70 % | -0.04 | -0.14 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.1 | 1.43 | 1.07 | 5 de 7 | 7 de 7 | 1 de 1 | 89 % | 82 % | 89 % | -0.02 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (38 %) en línea con el mercado; total esperado ficha 2.07 vs modelo 2.19. Mejor línea con cuota ≥ 1,30 que cumple: local Menos 1.5 @1.33 (p 73 %, aj. 66 %).


---

## 12:00 · Noruega - Gales (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 4, 'equipo': 'Noruega', 'pj': 4, 'g': 1, 'e': 0, 'p': 3, 'gf_gc': '6:8', 'dg': -2, 'pts': 3, 'grupo': 'GRUPO 4'}, 'visitante': {'pos': 3, 'equipo': 'Gales', 'pj': 4, 'g': 1, 'e': 0, 'p': 3, 'gf_gc': '2:5', 'dg': -3, 'pts': 3, 'grupo': 'GRUPO 4'}}; bajas: ninguna anotada; clima: 4.1 °C al inicio, humedad 91 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 12.6 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Noruega | 1.23 | 80 % | 80 % | -0.5 | -0.02 |
| Empate | 6.6 | 14 % | 13 % | +0.8 | -0.09 |
| Gana Gales | 11.75 | 7 % | 7 % | -0.4 | -0.22 |

Favorito del modelo: **local** (81 %). Alertas: Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 3 de 7, perdió 4 de 7; visitante ganó 3 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=1) con ambos marcan: 1 de 1. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 4 de 7 → no
- Local o empate: L no perdió 3 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 3 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Noruega o empate | 1.06 | 93 % | 93 % | -0.01 |
| Gales o empate | 4.4 | 20 % | 20 % | -0.10 |
| No hay empate | 1.11 | 86 % | 87 % | -0.04 |

**Ambos marcan** (L ambos marcan 7 de 7, V 3 de 7, directos 1 de 1):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.88 | 50 % | 50 % | -0.06 | L 7 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 1.87 | 50 % | 50 % | -0.07 | L 0 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Noruega | 1.57 | 61 % | 61 % | -0.04 |
| 1.er tiempo: Empate | 2.95 | 30 % | 30 % | -0.12 |
| 1.er tiempo: Gales | 8.5 | 9 % | 9 % | -0.26 |
| 2.º tiempo: Noruega | 1.45 | 63 % | 66 % | -0.08 |
| 2.º tiempo: Empate | 3.5 | 26 % | 24 % | -0.08 |
| 2.º tiempo: Gales | 7.9 | 10 % | 10 % | -0.18 |
| Descanso o final: Noruega | 1.17 | 82 % | 80 % | -0.05 |
| Descanso o final: Empate | 2.4 | 38 % | 39 % | -0.10 |
| Descanso o final: Gales | 5.7 | 14 % | 16 % | -0.21 |
| Descanso/final: Noruega / Noruega | 1.65 | 57 % | 57 % | -0.06 |
| Descanso/final: Noruega / Empate | 23.0 | 3 % | 3 % | -0.26 |
| Descanso/final: Noruega / Gales | 90.0 | 1 % | 1 % | -0.47 |
| Descanso/final: Empate / Noruega | 4.1 | 19 % | 20 % | -0.20 |
| Descanso/final: Empate / Empate | 9.75 | 8 % | 7 % | -0.23 |
| Descanso/final: Empate / Gales | 23.0 | 3 % | 3 % | -0.35 |
| Descanso/final: Gales / Noruega | 20.0 | 3 % | 3 % | -0.43 |
| Descanso/final: Gales / Empate | 23.0 | 3 % | 3 % | -0.36 |
| Descanso/final: Gales / Gales | 18.5 | 3 % | 4 % | -0.40 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.23 | 80 % | 79 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 4.1 | 20 % | 21 % | -0.17 |
| Goles 1.er tiempo Más 1.0 | 1.4 | 71 % | 70 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 3.0 | 31 % | 31 % | -0.07 |
| Goles 1.er tiempo Más 1.25 | 1.72 | 57 % | 56 % | -0.02 |
| Goles 1.er tiempo Menos 1.25 | 2.15 | 44 % | 44 % | -0.06 |
| Goles 1.er tiempo Más 1.5 | 2.0 | 47 % | 47 % | -0.05 |
| Goles 1.er tiempo Menos 1.5 | 1.78 | 53 % | 53 % | -0.07 |
| Goles 1.er tiempo Más 1.75 | 2.37 | 40 % | 40 % | -0.05 |
| Goles 1.er tiempo Menos 1.75 | 1.6 | 61 % | 61 % | -0.03 |
| Goles 1.er tiempo Más 2.0 | 3.15 | 29 % | 29 % | -0.08 |
| Goles 1.er tiempo Menos 2.0 | 1.36 | 72 % | 72 % | -0.02 |
| Goles 1.er tiempo Más 2.5 | 4.0 | 21 % | 21 % | -0.17 |
| Goles 1.er tiempo Menos 2.5 | 1.24 | 79 % | 79 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 8.25 | 7 % | 8 % | -0.40 |
| Goles 1.er tiempo Menos 3.5 | 1.07 | 93 % | 92 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.13 | 85 % | 87 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 5.6 | 15 % | 13 % | -0.16 |
| Goles 2.º tiempo Más 1.5 | 1.62 | 56 % | 59 % | -0.09 |
| Goles 2.º tiempo Menos 1.5 | 2.27 | 44 % | 41 % | -0.01 |
| Goles 2.º tiempo Más 2.5 | 2.82 | 29 % | 32 % | -0.17 |
| Goles 2.º tiempo Menos 2.5 | 1.42 | 71 % | 68 % | +0.00 |

**Goles, esperado ficha:** local 1.36, visitante 1.64, total 3.0 (modelo: λ local 2.81, visitante 0.74). Muestra local 7, visitante 7, directos 1.

**Líneas de goles que cumplen 5 de 7 en ambos (13):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.05 | 1.36 | 0.86 | 7 de 7 | 6 de 7 | 1 de 1 | 94 % | 87 % | 94 % | -0.01 | -0.09 | PROTECCIÓN |
| local | Menos 2.5 | 1.98 | 1.36 | 1.14 | 6 de 7 | 7 de 7 | 1 de 1 | 49 % | 42 % | 47 % | -0.04 | -0.17 |  |
| local | Menos 3.5 | 1.39 | 1.36 | 2.14 | 7 de 7 | 7 de 7 | 1 de 1 | 72 % | 65 % | 69 % | -0.00 | -0.10 | PROTECCIÓN |
| local | Menos 4.5 | 1.15 | 1.36 | 3.14 | 7 de 7 | 7 de 7 | 1 de 1 | 87 % | 80 % | 85 % | -0.00 | -0.08 | PROTECCIÓN |
| local | Menos 5.5 | 1.05 | 1.36 | 4.14 | 7 de 7 | 7 de 7 | 1 de 1 | 95 % | 88 % | 94 % | -0.00 | -0.08 | PROTECCIÓN |
| total | Menos 3.5 | 1.82 | 3.0 | 0.5 | 6 de 7 | 6 de 7 | 1 de 1 | 55 % | 48 % | 53 % | -0.00 | -0.13 |  |
| total | Menos 3.75 | 1.67 | 3.0 | 0.75 | 6 de 7 | 6 de 7 | 1 de 1 | 60 % | 53 % | 58 % | +0.01 | -0.11 |  |
| total | Menos 4.0 | 1.5 | 3.0 | 1.0 | 6 de 7 | 6 de 7 | 1 de 1 | 67 % | 60 % | 65 % | +0.01 | -0.10 |  |
| total | Menos 4.25 | 1.42 | 3.0 | 1.25 | 6 de 7 | 6 de 7 | 1 de 1 | 71 % | 64 % | 69 % | +0.00 | -0.09 | PROTECCIÓN |
| total | Menos 4.5 | 1.36 | 3.0 | 1.5 | 6 de 7 | 6 de 7 | 1 de 1 | 74 % | 67 % | 72 % | +0.00 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.15 | 3.0 | 2.5 | 7 de 7 | 6 de 7 | 1 de 1 | 87 % | 80 % | 85 % | -0.00 | -0.08 | PROTECCIÓN |
| total | Menos 6.5 | 1.06 | 3.0 | 3.5 | 7 de 7 | 6 de 7 | 1 de 1 | 94 % | 87 % | 93 % | -0.00 | -0.08 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.03 | 1.64 | 0.86 | 7 de 7 | 6 de 7 | 1 de 1 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (81 %) en línea con el mercado; total esperado ficha 3.0 vs modelo 3.55. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 4.5 @1.36 (p 74 %, aj. 67 %).


---

## 12:30 · RCD Mallorca - Cordoba CF (España Segunda División)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 6, 'equipo': 'Mallorca', 'pj': 12, 'g': 6, 'e': 4, 'p': 2, 'gf_gc': '15:7', 'dg': 8, 'pts': 22, 'grupo': ''}, 'visitante': {'pos': 11, 'equipo': 'Córdoba', 'pj': 13, 'g': 6, 'e': 1, 'p': 6, 'gf_gc': '22:22', 'dg': 0, 'pts': 19, 'grupo': ''}}; bajas: ninguna anotada; clima: 19.3 °C al inicio, humedad 74 %, prob. de lluvia máx. 0 %, lluvia máx. 0.3 mm/h, viento máx. 9.2 km/h (código OMM al inicio 1) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana RCD Mallorca | 1.98 | 49 % | 49 % | +0.3 | -0.03 |
| Empate | 3.85 | 25 % | 24 % | +0.5 | -0.05 |
| Gana Cordoba CF | 3.5 | 26 % | 27 % | -0.8 | -0.09 |

Favorito del modelo: **local** (49 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 6 de 7, perdió 1 de 7; visitante ganó 4 de 7, no perdió 5 de 7, perdió 2 de 7. Directos (n=0) con ambos marcan: 0 de 0. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 2 de 7 → no
- Gana visitante: V ganó 4 de 7 · L perdió 1 de 7 → no
- Local o empate: L no perdió 6 de 7 · V no ganó 3 de 7 → no
- Visitante o empate: V no perdió 5 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| RCD Mallorca o empate | 1.33 | 74 % | 73 % | -0.02 |
| Cordoba CF o empate | 1.85 | 51 % | 51 % | -0.06 |
| No hay empate | 1.26 | 75 % | 76 % | -0.05 |

**Ambos marcan** (L ambos marcan 4 de 7, V 4 de 7, directos 0 de 0):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.52 | 63 % | 63 % | -0.04 | L 4 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 2.42 | 37 % | 37 % | -0.10 | L 3 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: RCD Mallorca | 2.52 | 37 % | 37 % | -0.06 |
| 1.er tiempo: Empate | 2.32 | 40 % | 40 % | -0.07 |
| 1.er tiempo: Cordoba CF | 3.85 | 23 % | 23 % | -0.13 |
| 2.º tiempo: RCD Mallorca | 2.25 | 41 % | 41 % | -0.08 |
| 2.º tiempo: Empate | 2.77 | 33 % | 33 % | -0.08 |
| 2.º tiempo: Cordoba CF | 3.45 | 26 % | 26 % | -0.11 |
| Descanso o final: RCD Mallorca | 1.62 | 58 % | 58 % | -0.06 |
| Descanso o final: Empate | 1.78 | 52 % | 52 % | -0.07 |
| Descanso o final: Cordoba CF | 2.42 | 36 % | 39 % | -0.12 |
| Descanso/final: RCD Mallorca / RCD Mallorca | 3.1 | 29 % | 29 % | -0.10 |
| Descanso/final: RCD Mallorca / Empate | 14.0 | 6 % | 5 % | -0.18 |
| Descanso/final: RCD Mallorca / Cordoba CF | 32.0 | 2 % | 2 % | -0.28 |
| Descanso/final: Empate / RCD Mallorca | 5.1 | 17 % | 17 % | -0.16 |
| Descanso/final: Empate / Empate | 6.1 | 14 % | 14 % | -0.17 |
| Descanso/final: Empate / Cordoba CF | 8.0 | 10 % | 10 % | -0.20 |
| Descanso/final: Cordoba CF / RCD Mallorca | 22.0 | 3 % | 3 % | -0.26 |
| Descanso/final: Cordoba CF / Empate | 14.0 | 5 % | 5 % | -0.23 |
| Descanso/final: Cordoba CF / Cordoba CF | 5.8 | 14 % | 14 % | -0.20 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.32 | 74 % | 73 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 3.3 | 26 % | 27 % | -0.15 |
| Goles 1.er tiempo Más 0.75 | 1.42 | 69 % | 69 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.87 | 32 % | 32 % | -0.09 |
| Goles 1.er tiempo Más 1.0 | 1.62 | 61 % | 60 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.32 | 41 % | 41 % | -0.06 |
| Goles 1.er tiempo Más 1.25 | 2.02 | 48 % | 47 % | -0.03 |
| Goles 1.er tiempo Menos 1.25 | 1.8 | 53 % | 54 % | -0.05 |
| Goles 1.er tiempo Más 1.5 | 2.37 | 40 % | 39 % | -0.06 |
| Goles 1.er tiempo Menos 1.5 | 1.57 | 60 % | 61 % | -0.06 |
| Goles 1.er tiempo Más 1.75 | 2.95 | 32 % | 31 % | -0.06 |
| Goles 1.er tiempo Menos 1.75 | 1.4 | 69 % | 70 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 5.1 | 16 % | 16 % | -0.18 |
| Goles 1.er tiempo Menos 2.5 | 1.16 | 84 % | 84 % | -0.03 |
| Goles 1.er tiempo Más 3.5 | 10.25 | 5 % | 5 % | -0.47 |
| Goles 1.er tiempo Menos 3.5 | 1.04 | 95 % | 95 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.17 | 83 % | 84 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 4.85 | 17 % | 16 % | -0.17 |
| Goles 2.º tiempo Más 1.5 | 1.75 | 53 % | 54 % | -0.08 |
| Goles 2.º tiempo Menos 1.5 | 2.05 | 47 % | 46 % | -0.03 |
| Goles 2.º tiempo Más 2.5 | 3.25 | 26 % | 27 % | -0.17 |
| Goles 2.º tiempo Menos 2.5 | 1.33 | 74 % | 73 % | -0.01 |

**Goles, esperado ficha:** local 1.21, visitante 1.29, total 2.5 (modelo: λ local 1.82, visitante 1.31). Muestra local 7, visitante 7, directos 0.

**Líneas de goles que cumplen 5 de 7 en ambos (9):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.33 | 1.21 | 1.29 | 6 de 7 | 6 de 7 |  | 73 % | 66 % | 73 % | -0.03 | -0.12 | PROTECCIÓN |
| local | Menos 3.5 | 1.1 | 1.21 | 2.29 | 7 de 7 | 7 de 7 |  | 90 % | 83 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 0.5 | 1.04 | 2.5 | 2.0 | 6 de 7 | 7 de 7 |  | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Menos 4.5 | 1.24 | 2.5 | 2.0 | 7 de 7 | 6 de 7 |  | 79 % | 72 % | 79 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.09 | 2.5 | 3.0 | 7 de 7 | 7 de 7 |  | 90 % | 84 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 6.5 | 1.03 | 2.5 | 4.0 | 7 de 7 | 7 de 7 |  | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.31 | 1.29 | 0.79 | 5 de 7 | 7 de 7 |  | 74 % | 67 % | 74 % | -0.04 | -0.13 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.14 | 1.29 | 1.21 | 7 de 7 | 5 de 7 |  | 86 % | 79 % | 86 % | -0.02 | -0.10 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.03 | 1.29 | 2.21 | 7 de 7 | 7 de 7 |  | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (49 %) en línea con el mercado; total esperado ficha 2.5 vs modelo 3.13. Mejor línea con cuota ≥ 1,30 que cumple: visitante Más 0.5 @1.31 (p 74 %, aj. 67 %).


---

## 12:30 · UD Almeria - FC Andorra (España Segunda División)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 1, 'equipo': 'Almería', 'pj': 13, 'g': 9, 'e': 2, 'p': 2, 'gf_gc': '24:10', 'dg': 14, 'pts': 29, 'grupo': ''}, 'visitante': {'pos': 19, 'equipo': 'Andorra', 'pj': 12, 'g': 3, 'e': 2, 'p': 7, 'gf_gc': '17:22', 'dg': -5, 'pts': 11, 'grupo': ''}}; bajas: ninguna anotada; clima: 20.2 °C al inicio, humedad 72 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 10.5 km/h (código OMM al inicio 0) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana UD Almeria | 1.67 | 59 % | 58 % | +1.0 | -0.02 |
| Empate | 3.85 | 23 % | 24 % | -0.2 | -0.10 |
| Gana FC Andorra | 4.75 | 18 % | 19 % | -0.8 | -0.14 |

Favorito del modelo: **local** (60 %). Alertas: Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 5 de 7, no perdió 7 de 7, perdió 0 de 7; visitante ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7. Directos (n=2) con ambos marcan: 2 de 2. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 5 de 7 · V perdió 2 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 0 de 7 → no
- Local o empate: L no perdió 7 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 5 de 7 · L no ganó 2 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| UD Almeria o empate | 1.2 | 82 % | 81 % | -0.02 |
| FC Andorra o empate | 2.22 | 41 % | 42 % | -0.08 |
| No hay empate | 1.24 | 77 % | 76 % | -0.05 |

**Ambos marcan** (L ambos marcan 5 de 7, V 3 de 7, directos 2 de 2):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.57 | 60 % | 60 % | -0.06 | L 5 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 2.3 | 40 % | 40 % | -0.07 | L 2 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: UD Almeria | 2.22 | 43 % | 42 % | -0.04 |
| 1.er tiempo: Empate | 2.35 | 39 % | 39 % | -0.08 |
| 1.er tiempo: FC Andorra | 4.7 | 18 % | 19 % | -0.16 |
| 2.º tiempo: UD Almeria | 1.95 | 48 % | 48 % | -0.07 |
| 2.º tiempo: Empate | 2.8 | 33 % | 32 % | -0.08 |
| 2.º tiempo: FC Andorra | 4.35 | 20 % | 20 % | -0.15 |
| Descanso o final: UD Almeria | 1.47 | 65 % | 64 % | -0.04 |
| Descanso o final: Empate | 1.82 | 50 % | 51 % | -0.09 |
| Descanso o final: FC Andorra | 3.0 | 28 % | 31 % | -0.15 |
| Descanso/final: UD Almeria / UD Almeria | 2.55 | 36 % | 35 % | -0.07 |
| Descanso/final: UD Almeria / Empate | 15.0 | 5 % | 5 % | -0.23 |
| Descanso/final: UD Almeria / FC Andorra | 45.0 | 2 % | 1 % | -0.32 |
| Descanso/final: Empate / UD Almeria | 4.55 | 19 % | 19 % | -0.15 |
| Descanso/final: Empate / Empate | 6.2 | 13 % | 13 % | -0.19 |
| Descanso/final: Empate / FC Andorra | 10.25 | 7 % | 8 % | -0.25 |
| Descanso/final: FC Andorra / UD Almeria | 20.0 | 4 % | 4 % | -0.30 |
| Descanso/final: FC Andorra / Empate | 14.5 | 5 % | 5 % | -0.27 |
| Descanso/final: FC Andorra / FC Andorra | 8.25 | 9 % | 10 % | -0.24 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.31 | 74 % | 74 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 3.35 | 26 % | 26 % | -0.14 |
| Goles 1.er tiempo Más 0.75 | 1.42 | 69 % | 69 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.92 | 31 % | 32 % | -0.08 |
| Goles 1.er tiempo Más 1.0 | 1.6 | 62 % | 61 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.37 | 40 % | 40 % | -0.05 |
| Goles 1.er tiempo Más 1.25 | 1.98 | 49 % | 49 % | -0.03 |
| Goles 1.er tiempo Menos 1.25 | 1.85 | 52 % | 52 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 2.3 | 41 % | 40 % | -0.07 |
| Goles 1.er tiempo Menos 1.5 | 1.6 | 59 % | 60 % | -0.05 |
| Goles 1.er tiempo Más 1.75 | 2.87 | 33 % | 32 % | -0.06 |
| Goles 1.er tiempo Menos 1.75 | 1.42 | 68 % | 69 % | -0.03 |
| Goles 1.er tiempo Más 2.5 | 5.0 | 16 % | 16 % | -0.19 |
| Goles 1.er tiempo Menos 2.5 | 1.16 | 84 % | 84 % | -0.03 |
| Goles 1.er tiempo Más 3.5 | 10.0 | 5 % | 5 % | -0.49 |
| Goles 1.er tiempo Menos 3.5 | 1.04 | 95 % | 95 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.18 | 82 % | 83 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 4.75 | 18 % | 17 % | -0.16 |
| Goles 2.º tiempo Más 1.5 | 1.78 | 52 % | 53 % | -0.08 |
| Goles 2.º tiempo Menos 1.5 | 2.0 | 48 % | 47 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 3.3 | 26 % | 27 % | -0.16 |
| Goles 2.º tiempo Menos 2.5 | 1.32 | 74 % | 73 % | -0.02 |

**Goles, esperado ficha:** local 1.71, visitante 1.29, total 3.0 (modelo: λ local 2.02, visitante 1.11). Muestra local 7, visitante 7, directos 2.

**Líneas de goles que cumplen 5 de 7 en ambos (10):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.42 | 1.71 | 0.79 | 5 de 7 | 6 de 7 | 1 de 2 | 67 % | 60 % | 68 % | -0.04 | -0.14 | PROTECCIÓN |
| local | Menos 3.5 | 1.13 | 1.71 | 1.79 | 6 de 7 | 7 de 7 | 2 de 2 | 86 % | 79 % | 86 % | -0.03 | -0.10 | PROTECCIÓN |
| local | Menos 4.5 | 1.04 | 1.71 | 2.79 | 7 de 7 | 7 de 7 | 2 de 2 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.04 | 3.0 | 2.5 | 7 de 7 | 6 de 7 | 2 de 2 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 1.5 | 1.19 | 3.0 | 1.5 | 6 de 7 | 5 de 7 | 2 de 2 | 82 % | 75 % | 82 % | -0.03 | -0.11 | PROTECCIÓN |
| total | Menos 4.5 | 1.24 | 3.0 | 1.5 | 6 de 7 | 5 de 7 | 1 de 2 | 79 % | 72 % | 79 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.09 | 3.0 | 2.5 | 6 de 7 | 7 de 7 | 2 de 2 | 90 % | 83 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 6.5 | 1.03 | 3.0 | 3.5 | 7 de 7 | 7 de 7 | 2 de 2 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.42 | 1.29 | 0.79 | 5 de 7 | 5 de 7 | 2 de 2 | 67 % | 60 % | 67 % | -0.05 | -0.15 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.09 | 1.29 | 1.21 | 7 de 7 | 5 de 7 | 2 de 2 | 90 % | 83 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (60 %) en línea con el mercado; total esperado ficha 3.0 vs modelo 3.13. Mejor línea con cuota ≥ 1,30 que cumple: local Menos 2.5 @1.42 (p 67 %, aj. 60 %).


---

## 14:45 · Irlanda del Norte - Ucrania (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 1, 'equipo': 'Irlanda del Norte', 'pj': 4, 'g': 2, 'e': 2, 'p': 0, 'gf_gc': '4:0', 'dg': 4, 'pts': 8, 'grupo': 'GRUPO 2'}, 'visitante': {'pos': 3, 'equipo': 'Ucrania', 'pj': 4, 'g': 1, 'e': 1, 'p': 2, 'gf_gc': '2:5', 'dg': -3, 'pts': 4, 'grupo': 'GRUPO 2'}}; bajas: ninguna anotada; clima: 9.8 °C al inicio, humedad 71 %, prob. de lluvia máx. 14 %, lluvia máx. 0.3 mm/h, viento máx. 19.1 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Irlanda del Norte | 2.55 | 38 % | 38 % | +0.2 | -0.04 |
| Empate | 3.0 | 32 % | 32 % | -0.1 | -0.05 |
| Gana Ucrania | 3.1 | 31 % | 31 % | -0.1 | -0.05 |

Favorito del modelo: **local** (38 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 2 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=1) con ambos marcan: 0 de 1. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 2 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 5 de 7 → sí
- Visitante o empate: V no perdió 3 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Irlanda del Norte o empate | 1.4 | 69 % | 69 % | -0.03 |
| Ucrania o empate | 1.53 | 62 % | 62 % | -0.05 |
| No hay empate | 1.37 | 68 % | 68 % | -0.06 |

**Ambos marcan** (L ambos marcan 0 de 7, V 2 de 7, directos 0 de 1):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 2.05 | 45 % | 45 % | -0.07 | L 0 de 7 · V 2 de 7 → no |
| Ambos marcan: No | 1.72 | 55 % | 55 % | -0.06 | L 7 de 7 · V 5 de 7 → sí |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Irlanda del Norte | 3.25 | 28 % | 28 % | -0.09 |
| 1.er tiempo: Empate | 1.95 | 48 % | 48 % | -0.05 |
| 1.er tiempo: Ucrania | 3.75 | 24 % | 24 % | -0.12 |
| 2.º tiempo: Irlanda del Norte | 2.92 | 31 % | 31 % | -0.10 |
| 2.º tiempo: Empate | 2.15 | 43 % | 43 % | -0.07 |
| 2.º tiempo: Ucrania | 3.4 | 26 % | 26 % | -0.11 |
| Descanso o final: Irlanda del Norte | 2.02 | 45 % | 46 % | -0.08 |
| Descanso o final: Empate | 1.57 | 59 % | 60 % | -0.07 |
| Descanso o final: Ucrania | 2.3 | 39 % | 41 % | -0.10 |
| Descanso/final: Irlanda del Norte / Irlanda del Norte | 4.1 | 21 % | 21 % | -0.13 |
| Descanso/final: Irlanda del Norte / Empate | 15.0 | 5 % | 5 % | -0.23 |
| Descanso/final: Irlanda del Norte / Ucrania | 45.0 | 1 % | 2 % | -0.34 |
| Descanso/final: Empate / Irlanda del Norte | 5.7 | 15 % | 15 % | -0.17 |
| Descanso/final: Empate / Empate | 4.05 | 21 % | 21 % | -0.14 |
| Descanso/final: Empate / Ucrania | 6.6 | 13 % | 12 % | -0.17 |
| Descanso/final: Ucrania / Irlanda del Norte | 40.0 | 2 % | 2 % | -0.28 |
| Descanso/final: Ucrania / Empate | 14.5 | 5 % | 5 % | -0.25 |
| Descanso/final: Ucrania / Ucrania | 5.0 | 17 % | 17 % | -0.17 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.55 | 62 % | 62 % | -0.04 |
| Goles 1.er tiempo Menos 0.5 | 2.42 | 38 % | 38 % | -0.07 |
| Goles 1.er tiempo Más 0.75 | 1.78 | 54 % | 54 % | -0.04 |
| Goles 1.er tiempo Menos 0.75 | 2.05 | 47 % | 47 % | -0.03 |
| Goles 1.er tiempo Más 1.0 | 2.3 | 41 % | 42 % | -0.05 |
| Goles 1.er tiempo Menos 1.0 | 1.62 | 61 % | 60 % | -0.02 |
| Goles 1.er tiempo Más 1.25 | 2.87 | 32 % | 32 % | -0.09 |
| Goles 1.er tiempo Menos 1.25 | 1.42 | 69 % | 69 % | -0.02 |
| Goles 1.er tiempo Más 1.5 | 3.35 | 25 % | 26 % | -0.15 |
| Goles 1.er tiempo Menos 1.5 | 1.31 | 75 % | 74 % | -0.02 |
| Goles 1.er tiempo Más 2.5 | 8.0 | 8 % | 8 % | -0.39 |
| Goles 1.er tiempo Menos 2.5 | 1.07 | 92 % | 92 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.39 | 69 % | 69 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 2.92 | 31 % | 31 % | -0.11 |
| Goles 2.º tiempo Más 1.5 | 2.72 | 33 % | 33 % | -0.10 |
| Goles 2.º tiempo Menos 1.5 | 1.44 | 67 % | 67 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 6.2 | 12 % | 12 % | -0.28 |
| Goles 2.º tiempo Menos 2.5 | 1.11 | 88 % | 88 % | -0.02 |

**Goles, esperado ficha:** local 1.21, visitante 0.57, total 1.79 (modelo: λ local 1.14, visitante 1.01). Muestra local 7, visitante 7, directos 1.

**Líneas de goles que cumplen 5 de 7 en ambos (5):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| total | Más 0.5 | 1.12 | 1.79 | 1.29 | 5 de 7 | 6 de 7 | 1 de 1 | 88 % | 81 % | 88 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 3.5 | 1.19 | 1.79 | 1.71 | 7 de 7 | 5 de 7 | 1 de 1 | 83 % | 76 % | 82 % | -0.01 | -0.10 | PROTECCIÓN |
| total | Menos 4.5 | 1.06 | 1.79 | 2.71 | 7 de 7 | 7 de 7 | 1 de 1 | 93 % | 86 % | 93 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Menos 1.5 | 1.32 | 0.57 | 0.93 | 6 de 7 | 6 de 7 | 1 de 1 | 73 % | 66 % | 73 % | -0.03 | -0.12 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.07 | 0.57 | 1.93 | 7 de 7 | 7 de 7 | 1 de 1 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (38 %) en línea con el mercado; total esperado ficha 1.79 vs modelo 2.15. Mejor línea con cuota ≥ 1,30 que cumple: visitante Menos 1.5 @1.32 (p 73 %, aj. 66 %).


---

## 14:45 · Portugal - Dinamarca (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 1, 'equipo': 'Portugal', 'pj': 4, 'g': 4, 'e': 0, 'p': 0, 'gf_gc': '9:4', 'dg': 5, 'pts': 12, 'grupo': 'GRUPO 4'}, 'visitante': {'pos': 2, 'equipo': 'Dinamarca', 'pj': 4, 'g': 2, 'e': 0, 'p': 2, 'gf_gc': '7:7', 'dg': 0, 'pts': 6, 'grupo': 'GRUPO 4'}}; bajas: ninguna anotada; clima: 13.8 °C al inicio, humedad 93 %, prob. de lluvia máx. 73 %, lluvia máx. 0.2 mm/h, viento máx. 5.1 km/h (código OMM al inicio 80) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Portugal | 1.52 | 64 % | 64 % | -0.1 | -0.02 |
| Empate | 4.6 | 20 % | 20 % | +0.5 | -0.06 |
| Gana Dinamarca | 5.8 | 15 % | 16 % | -0.4 | -0.11 |

Favorito del modelo: **local** (64 %). Alertas: Revisar: la simulación sin contexto se aleja 22 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 5 de 7, no perdió 6 de 7, perdió 1 de 7; visitante ganó 3 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=3) con ambos marcan: 2 de 3. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 5 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 1 de 7 → no
- Local o empate: L no perdió 6 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 3 de 7 · L no ganó 2 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Portugal o empate | 1.16 | 85 % | 84 % | -0.02 |
| Dinamarca o empate | 2.62 | 36 % | 36 % | -0.06 |
| No hay empate | 1.19 | 80 % | 80 % | -0.05 |

**Ambos marcan** (L ambos marcan 4 de 7, V 4 de 7, directos 2 de 3):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.62 | 59 % | 59 % | -0.04 | L 4 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 2.22 | 41 % | 41 % | -0.10 | L 3 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Portugal | 1.98 | 48 % | 47 % | -0.05 |
| 1.er tiempo: Empate | 2.5 | 36 % | 37 % | -0.09 |
| 1.er tiempo: Dinamarca | 5.4 | 15 % | 16 % | -0.16 |
| 2.º tiempo: Portugal | 1.78 | 52 % | 53 % | -0.08 |
| 2.º tiempo: Empate | 3.0 | 31 % | 30 % | -0.08 |
| 2.º tiempo: Dinamarca | 4.9 | 18 % | 17 % | -0.13 |
| Descanso o final: Portugal | 1.35 | 70 % | 69 % | -0.05 |
| Descanso o final: Empate | 1.95 | 47 % | 48 % | -0.09 |
| Descanso o final: Dinamarca | 3.45 | 25 % | 27 % | -0.14 |
| Descanso/final: Portugal / Portugal | 2.22 | 42 % | 41 % | -0.07 |
| Descanso/final: Portugal / Empate | 15.5 | 5 % | 5 % | -0.23 |
| Descanso/final: Portugal / Dinamarca | 50.0 | 1 % | 1 % | -0.30 |
| Descanso/final: Empate / Portugal | 4.3 | 19 % | 20 % | -0.18 |
| Descanso/final: Empate / Empate | 7.2 | 11 % | 11 % | -0.19 |
| Descanso/final: Empate / Dinamarca | 12.5 | 6 % | 6 % | -0.25 |
| Descanso/final: Dinamarca / Portugal | 20.0 | 4 % | 4 % | -0.29 |
| Descanso/final: Dinamarca / Empate | 17.0 | 4 % | 4 % | -0.27 |
| Descanso/final: Dinamarca / Dinamarca | 9.5 | 8 % | 8 % | -0.26 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.29 | 76 % | 75 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 3.5 | 24 % | 25 % | -0.17 |
| Goles 1.er tiempo Más 0.75 | 1.38 | 72 % | 71 % | -0.01 |
| Goles 1.er tiempo Menos 0.75 | 3.05 | 29 % | 30 % | -0.11 |
| Goles 1.er tiempo Más 1.0 | 1.55 | 64 % | 63 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.5 | 37 % | 38 % | -0.07 |
| Goles 1.er tiempo Más 1.25 | 1.91 | 51 % | 50 % | -0.02 |
| Goles 1.er tiempo Menos 1.25 | 1.9 | 50 % | 51 % | -0.06 |
| Goles 1.er tiempo Más 1.5 | 2.25 | 42 % | 41 % | -0.05 |
| Goles 1.er tiempo Menos 1.5 | 1.62 | 58 % | 59 % | -0.07 |
| Goles 1.er tiempo Más 1.75 | 2.77 | 34 % | 34 % | -0.04 |
| Goles 1.er tiempo Menos 1.75 | 1.45 | 66 % | 67 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 4.75 | 18 % | 17 % | -0.16 |
| Goles 1.er tiempo Menos 2.5 | 1.18 | 82 % | 83 % | -0.03 |
| Goles 1.er tiempo Más 3.5 | 9.5 | 6 % | 6 % | -0.44 |
| Goles 1.er tiempo Menos 3.5 | 1.05 | 94 % | 94 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.16 | 84 % | 84 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 5.1 | 16 % | 16 % | -0.18 |
| Goles 2.º tiempo Más 1.5 | 1.7 | 55 % | 56 % | -0.07 |
| Goles 2.º tiempo Menos 1.5 | 2.12 | 45 % | 44 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 3.05 | 28 % | 29 % | -0.16 |
| Goles 2.º tiempo Menos 2.5 | 1.36 | 72 % | 71 % | -0.02 |

**Goles, esperado ficha:** local 1.79, visitante 1.5, total 3.29 (modelo: λ local 2.24, visitante 1.04). Muestra local 7, visitante 7, directos 3.

**Líneas de goles que cumplen 5 de 7 en ambos (7):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 3.5 | 1.2 | 1.79 | 1.71 | 6 de 7 | 5 de 7 | 1 de 3 | 82 % | 75 % | 81 % | -0.01 | -0.10 | PROTECCIÓN |
| local | Menos 4.5 | 1.07 | 1.79 | 2.71 | 7 de 7 | 7 de 7 | 2 de 3 | 93 % | 86 % | 92 % | -0.00 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.03 | 3.29 | 2.79 | 6 de 7 | 7 de 7 | 3 de 3 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Menos 5.5 | 1.11 | 3.29 | 2.21 | 6 de 7 | 5 de 7 | 1 de 3 | 89 % | 82 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 6.5 | 1.04 | 3.29 | 3.21 | 7 de 7 | 7 de 7 | 2 de 3 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.47 | 1.5 | 1.0 | 5 de 7 | 7 de 7 | 3 de 3 | 66 % | 59 % | 65 % | -0.04 | -0.14 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.07 | 1.5 | 1.0 | 7 de 7 | 6 de 7 | 3 de 3 | 91 % | 84 % | 92 % | -0.02 | -0.10 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (64 %) en línea con el mercado; total esperado ficha 3.29 vs modelo 3.28. Mejor línea con cuota ≥ 1,30 que cumple: visitante Más 0.5 @1.47 (p 66 %, aj. 59 %).


---

## 14:45 · Rumanía - Polonia (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 4, 'equipo': 'Rumanía', 'pj': 4, 'g': 0, 'e': 0, 'p': 4, 'gf_gc': '3:13', 'dg': -10, 'pts': 0, 'grupo': 'GRUPO 4'}, 'visitante': {'pos': 3, 'equipo': 'Polonia', 'pj': 4, 'g': 1, 'e': 1, 'p': 2, 'gf_gc': '7:4', 'dg': 3, 'pts': 4, 'grupo': 'GRUPO 4'}}; bajas: ninguna anotada; clima: 3.5 °C al inicio, humedad 93 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 3.3 km/h (código OMM al inicio 1) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Rumanía | 3.85 | 23 % | 24 % | -1.0 | -0.11 |
| Empate | 3.95 | 26 % | 24 % | +2.2 | +0.02 |
| Gana Polonia | 1.85 | 51 % | 52 % | -1.2 | -0.05 |

Favorito del modelo: **visitante** (52 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 1 de 7, no perdió 1 de 7, perdió 6 de 7; visitante ganó 3 de 7, no perdió 4 de 7, perdió 3 de 7. Directos (n=1) con ambos marcan: 0 de 1. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 1 de 7 · V perdió 3 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 6 de 7 → no
- Local o empate: L no perdió 1 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 4 de 7 · L no ganó 6 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Rumanía o empate | 1.98 | 49 % | 48 % | -0.03 |
| Polonia o empate | 1.28 | 77 % | 76 % | -0.02 |
| No hay empate | 1.25 | 74 % | 76 % | -0.07 |

**Ambos marcan** (L ambos marcan 4 de 7, V 4 de 7, directos 0 de 1):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.7 | 56 % | 55 % | -0.05 | L 4 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 2.07 | 44 % | 45 % | -0.08 | L 3 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Rumanía | 4.15 | 20 % | 21 % | -0.15 |
| 1.er tiempo: Empate | 2.32 | 41 % | 40 % | -0.05 |
| 1.er tiempo: Polonia | 2.4 | 39 % | 39 % | -0.08 |
| 2.º tiempo: Rumanía | 3.85 | 23 % | 23 % | -0.12 |
| 2.º tiempo: Empate | 2.65 | 36 % | 34 % | -0.05 |
| 2.º tiempo: Polonia | 2.15 | 41 % | 43 % | -0.11 |
| Descanso o final: Rumanía | 2.65 | 33 % | 35 % | -0.13 |
| Descanso o final: Empate | 1.8 | 53 % | 52 % | -0.05 |
| Descanso o final: Polonia | 1.57 | 59 % | 60 % | -0.08 |
| Descanso/final: Rumanía / Rumanía | 6.2 | 12 % | 13 % | -0.25 |
| Descanso/final: Rumanía / Empate | 15.0 | 5 % | 5 % | -0.19 |
| Descanso/final: Rumanía / Polonia | 24.0 | 3 % | 3 % | -0.30 |
| Descanso/final: Empate / Rumanía | 8.75 | 9 % | 9 % | -0.20 |
| Descanso/final: Empate / Empate | 6.0 | 15 % | 14 % | -0.11 |
| Descanso/final: Empate / Polonia | 4.9 | 17 % | 17 % | -0.16 |
| Descanso/final: Polonia / Rumanía | 40.0 | 2 % | 2 % | -0.26 |
| Descanso/final: Polonia / Empate | 15.0 | 6 % | 5 % | -0.16 |
| Descanso/final: Polonia / Polonia | 2.8 | 31 % | 32 % | -0.13 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.35 | 71 % | 72 % | -0.04 |
| Goles 1.er tiempo Menos 0.5 | 3.15 | 29 % | 28 % | -0.09 |
| Goles 1.er tiempo Más 0.75 | 1.47 | 65 % | 66 % | -0.04 |
| Goles 1.er tiempo Menos 0.75 | 2.7 | 36 % | 35 % | -0.04 |
| Goles 1.er tiempo Más 1.0 | 1.7 | 56 % | 57 % | -0.04 |
| Goles 1.er tiempo Menos 1.0 | 2.15 | 46 % | 45 % | -0.02 |
| Goles 1.er tiempo Más 1.25 | 2.15 | 44 % | 44 % | -0.06 |
| Goles 1.er tiempo Menos 1.25 | 1.72 | 57 % | 56 % | -0.01 |
| Goles 1.er tiempo Más 1.5 | 2.52 | 35 % | 36 % | -0.12 |
| Goles 1.er tiempo Menos 1.5 | 1.5 | 65 % | 64 % | -0.03 |
| Goles 1.er tiempo Más 2.5 | 5.7 | 13 % | 13 % | -0.24 |
| Goles 1.er tiempo Menos 2.5 | 1.13 | 87 % | 87 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 11.25 | 4 % | 4 % | -0.56 |
| Goles 1.er tiempo Menos 3.5 | 1.03 | 96 % | 96 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.22 | 78 % | 80 % | -0.05 |
| Goles 2.º tiempo Menos 0.5 | 4.2 | 22 % | 20 % | -0.08 |
| Goles 2.º tiempo Más 1.5 | 1.95 | 46 % | 48 % | -0.11 |
| Goles 2.º tiempo Menos 1.5 | 1.82 | 54 % | 52 % | -0.01 |
| Goles 2.º tiempo Más 2.5 | 3.9 | 20 % | 22 % | -0.22 |
| Goles 2.º tiempo Menos 2.5 | 1.24 | 80 % | 78 % | -0.01 |

**Goles, esperado ficha:** local 1.5, visitante 2.29, total 3.79 (modelo: λ local 1.11, visitante 1.75). Muestra local 7, visitante 7, directos 1.

**Líneas de goles que cumplen 5 de 7 en ambos (8):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.09 | 1.5 | 1.0 | 6 de 7 | 5 de 7 | 1 de 1 | 91 % | 84 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 0.5 | 1.05 | 3.79 | 3.29 | 7 de 7 | 6 de 7 | 1 de 1 | 93 % | 86 % | 94 % | -0.02 | -0.09 | PROTECCIÓN |
| total | Más 1.5 | 1.25 | 3.79 | 2.29 | 5 de 7 | 5 de 7 | 1 de 1 | 77 % | 70 % | 78 % | -0.04 | -0.13 | PROTECCIÓN |
| total | Más 2.0 | 1.37 | 3.79 | 1.79 | 5 de 7 | 5 de 7 | 1 de 1 | 70 % | 63 % | 72 % | -0.04 | -0.14 | PROTECCIÓN |
| total | Más 2.25 | 1.57 | 3.79 | 1.54 | 5 de 7 | 5 de 7 | 1 de 1 | 60 % | 53 % | 62 % | -0.06 | -0.17 |  |
| total | Más 2.5 | 1.75 | 3.79 | 1.29 | 5 de 7 | 5 de 7 | 1 de 1 | 52 % | 45 % | 55 % | -0.09 | -0.21 |  |
| visitante | Más 0.5 | 1.18 | 2.29 | 1.79 | 7 de 7 | 5 de 7 | 1 de 1 | 82 % | 75 % | 83 % | -0.03 | -0.12 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.09 | 2.29 | 1.21 | 5 de 7 | 6 de 7 | 0 de 1 | 91 % | 84 % | 90 % | -0.00 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (52 %) en línea con el mercado; total esperado ficha 3.79 vs modelo 2.87. Mejor línea con cuota ≥ 1,30 que cumple: total Más 2.0 @1.37 (p 70 %, aj. 63 %).


---

## 14:45 · Suecia - Bosnia y Herzegovina (UEFA Liga de Naciones)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 1, 'equipo': 'Suecia', 'pj': 4, 'g': 3, 'e': 1, 'p': 0, 'gf_gc': '7:3', 'dg': 4, 'pts': 10, 'grupo': 'GRUPO 4'}, 'visitante': {'pos': 2, 'equipo': 'Bosnia-Herzegovina', 'pj': 4, 'g': 2, 'e': 2, 'p': 0, 'gf_gc': '6:3', 'dg': 3, 'pts': 8, 'grupo': 'GRUPO 4'}}; bajas: ninguna anotada; clima: 3.4 °C al inicio, humedad 89 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 17.3 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Suecia | 1.55 | 63 % | 63 % | +0.1 | -0.02 |
| Empate | 4.35 | 22 % | 21 % | +0.7 | -0.05 |
| Gana Bosnia y Herzegovina | 5.8 | 15 % | 16 % | -0.8 | -0.13 |

Favorito del modelo: **local** (64 %). Alertas: Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 17 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 18 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 24 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7. Directos (n=1) con ambos marcan: 1 de 1. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 2 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 5 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Suecia o empate | 1.16 | 85 % | 84 % | -0.01 |
| Bosnia y Herzegovina o empate | 2.52 | 37 % | 37 % | -0.07 |
| No hay empate | 1.21 | 78 % | 79 % | -0.06 |

**Ambos marcan** (L ambos marcan 5 de 7, V 4 de 7, directos 1 de 1):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.67 | 56 % | 56 % | -0.07 | L 5 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 2.1 | 44 % | 44 % | -0.07 | L 2 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Suecia | 2.02 | 46 % | 46 % | -0.06 |
| 1.er tiempo: Empate | 2.42 | 38 % | 38 % | -0.07 |
| 1.er tiempo: Bosnia y Herzegovina | 5.4 | 15 % | 16 % | -0.18 |
| 2.º tiempo: Suecia | 1.83 | 50 % | 51 % | -0.08 |
| 2.º tiempo: Empate | 2.87 | 33 % | 31 % | -0.05 |
| 2.º tiempo: Bosnia y Herzegovina | 4.9 | 17 % | 17 % | -0.19 |
| Descanso o final: Suecia | 1.37 | 69 % | 68 % | -0.06 |
| Descanso o final: Empate | 1.91 | 48 % | 49 % | -0.08 |
| Descanso o final: Bosnia y Herzegovina | 3.45 | 24 % | 27 % | -0.16 |
| Descanso/final: Suecia / Suecia | 2.27 | 40 % | 40 % | -0.08 |
| Descanso/final: Suecia / Empate | 15.5 | 5 % | 5 % | -0.27 |
| Descanso/final: Suecia / Bosnia y Herzegovina | 50.0 | 1 % | 1 % | -0.40 |
| Descanso/final: Empate / Suecia | 4.3 | 20 % | 20 % | -0.16 |
| Descanso/final: Empate / Empate | 6.6 | 13 % | 12 % | -0.15 |
| Descanso/final: Empate / Bosnia y Herzegovina | 12.0 | 6 % | 6 % | -0.29 |
| Descanso/final: Bosnia y Herzegovina / Suecia | 22.0 | 3 % | 3 % | -0.32 |
| Descanso/final: Bosnia y Herzegovina / Empate | 17.0 | 4 % | 4 % | -0.27 |
| Descanso/final: Bosnia y Herzegovina / Bosnia y Herzegovina | 9.5 | 8 % | 8 % | -0.26 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.31 | 74 % | 74 % | -0.04 |
| Goles 1.er tiempo Menos 0.5 | 3.35 | 26 % | 26 % | -0.11 |
| Goles 1.er tiempo Más 0.75 | 1.42 | 68 % | 69 % | -0.03 |
| Goles 1.er tiempo Menos 0.75 | 2.9 | 33 % | 32 % | -0.06 |
| Goles 1.er tiempo Más 1.0 | 1.6 | 60 % | 61 % | -0.03 |
| Goles 1.er tiempo Menos 1.0 | 2.35 | 41 % | 41 % | -0.03 |
| Goles 1.er tiempo Más 1.25 | 2.0 | 47 % | 48 % | -0.05 |
| Goles 1.er tiempo Menos 1.25 | 1.82 | 53 % | 53 % | -0.03 |
| Goles 1.er tiempo Más 1.5 | 2.35 | 39 % | 39 % | -0.09 |
| Goles 1.er tiempo Menos 1.5 | 1.57 | 61 % | 61 % | -0.04 |
| Goles 1.er tiempo Más 1.75 | 2.92 | 31 % | 32 % | -0.09 |
| Goles 1.er tiempo Menos 1.75 | 1.42 | 69 % | 69 % | -0.02 |
| Goles 1.er tiempo Más 2.5 | 5.1 | 16 % | 16 % | -0.21 |
| Goles 1.er tiempo Menos 2.5 | 1.16 | 84 % | 84 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 10.25 | 5 % | 5 % | -0.49 |
| Goles 1.er tiempo Menos 3.5 | 1.04 | 95 % | 95 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.18 | 81 % | 83 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 4.7 | 19 % | 17 % | -0.12 |
| Goles 2.º tiempo Más 1.5 | 1.8 | 50 % | 53 % | -0.10 |
| Goles 2.º tiempo Menos 1.5 | 1.98 | 50 % | 47 % | -0.01 |
| Goles 2.º tiempo Más 2.5 | 3.4 | 23 % | 26 % | -0.21 |
| Goles 2.º tiempo Menos 2.5 | 1.31 | 77 % | 74 % | +0.00 |

**Goles, esperado ficha:** local 1.36, visitante 1.57, total 2.93 (modelo: λ local 2.11, visitante 0.98). Muestra local 7, visitante 7, directos 1.

**Líneas de goles que cumplen 5 de 7 en ambos (12):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.11 | 1.36 | 0.86 | 6 de 7 | 5 de 7 | 1 de 1 | 88 % | 81 % | 88 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 2.5 | 1.47 | 1.36 | 1.14 | 6 de 7 | 6 de 7 | 1 de 1 | 66 % | 59 % | 65 % | -0.02 | -0.13 | PROTECCIÓN |
| local | Menos 3.5 | 1.17 | 1.36 | 2.14 | 7 de 7 | 6 de 7 | 1 de 1 | 86 % | 79 % | 83 % | +0.00 | -0.08 | PROTECCIÓN |
| local | Menos 4.5 | 1.05 | 1.36 | 3.14 | 7 de 7 | 7 de 7 | 1 de 1 | 95 % | 88 % | 94 % | -0.00 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.04 | 2.93 | 2.43 | 7 de 7 | 6 de 7 | 1 de 1 | 95 % | 88 % | 95 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 1.5 | 1.2 | 2.93 | 1.43 | 6 de 7 | 5 de 7 | 1 de 1 | 80 % | 73 % | 82 % | -0.03 | -0.12 | PROTECCIÓN |
| total | Menos 4.5 | 1.23 | 2.93 | 1.57 | 6 de 7 | 5 de 7 | 1 de 1 | 82 % | 75 % | 80 % | +0.00 | -0.08 | PROTECCIÓN |
| total | Menos 5.5 | 1.09 | 2.93 | 2.57 | 6 de 7 | 6 de 7 | 1 de 1 | 92 % | 85 % | 90 % | +0.00 | -0.08 | PROTECCIÓN |
| total | Menos 6.5 | 1.03 | 2.93 | 3.57 | 7 de 7 | 7 de 7 | 1 de 1 | 97 % | 90 % | 96 % | -0.00 | -0.07 | PROTECCIÓN |
| visitante | Más 0.5 | 1.5 | 1.57 | 1.07 | 6 de 7 | 5 de 7 | 1 de 1 | 62 % | 55 % | 64 % | -0.07 | -0.17 |  |
| visitante | Menos 1.5 | 1.3 | 1.57 | -0.07 | 5 de 7 | 5 de 7 | 1 de 1 | 75 % | 68 % | 74 % | -0.02 | -0.11 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.06 | 1.57 | 0.93 | 5 de 7 | 5 de 7 | 1 de 1 | 93 % | 86 % | 93 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (64 %) en línea con el mercado; total esperado ficha 2.93 vs modelo 3.10. Mejor línea con cuota ≥ 1,30 que cumple: visitante Menos 1.5 @1.3 (p 75 %, aj. 68 %).


---

## 15:30 · Aguilas Doradas - Independiente Medellín (Colombia Categoría Primera A)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 10, 'equipo': 'Águilas Doradas', 'pj': 18, 'g': 6, 'e': 7, 'p': 5, 'gf_gc': '22:21', 'dg': 1, 'pts': 25, 'grupo': ''}, 'visitante': {'pos': 6, 'equipo': 'Ind. Medellín', 'pj': 18, 'g': 9, 'e': 2, 'p': 7, 'gf_gc': '28:25', 'dg': 3, 'pts': 29, 'grupo': ''}}; bajas: ninguna anotada; clima: 23.5 °C al inicio, humedad 48 %, prob. de lluvia máx. 94 %, lluvia máx. 0.3 mm/h, viento máx. 14.2 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Aguilas Doradas | 2.47 | 39 % | 39 % | +0.1 | -0.04 |
| Empate | 3.3 | 28 % | 29 % | -0.2 | -0.06 |
| Gana Independiente Medellín | 2.92 | 33 % | 33 % | +0.1 | -0.05 |

Favorito del modelo: **local** (39 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 3 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=6) con ambos marcan: 4 de 6. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 3 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 4 de 7 → no
- Visitante o empate: V no perdió 3 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Aguilas Doradas o empate | 1.44 | 67 % | 67 % | -0.03 |
| Independiente Medellín o empate | 1.57 | 61 % | 61 % | -0.04 |
| No hay empate | 1.33 | 72 % | 71 % | -0.05 |

**Ambos marcan** (L ambos marcan 3 de 7, V 5 de 7, directos 4 de 6):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.67 | 56 % | 56 % | -0.06 | L 3 de 7 · V 5 de 7 → no |
| Ambos marcan: No | 2.07 | 44 % | 44 % | -0.09 | L 4 de 7 · V 2 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Aguilas Doradas | 3.0 | 30 % | 30 % | -0.11 |
| 1.er tiempo: Empate | 2.05 | 44 % | 45 % | -0.09 |
| 1.er tiempo: Independiente Medellín | 3.45 | 26 % | 25 % | -0.11 |
| 2.º tiempo: Aguilas Doradas | 2.75 | 33 % | 33 % | -0.09 |
| 2.º tiempo: Empate | 2.47 | 38 % | 37 % | -0.07 |
| 2.º tiempo: Independiente Medellín | 3.05 | 29 % | 30 % | -0.10 |
| Descanso o final: Aguilas Doradas | 1.91 | 48 % | 49 % | -0.08 |
| Descanso o final: Empate | 1.62 | 56 % | 58 % | -0.09 |
| Descanso o final: Independiente Medellín | 2.18 | 42 % | 43 % | -0.09 |
| Descanso/final: Aguilas Doradas / Aguilas Doradas | 4.1 | 21 % | 21 % | -0.12 |
| Descanso/final: Aguilas Doradas / Empate | 13.0 | 6 % | 6 % | -0.22 |
| Descanso/final: Aguilas Doradas / Independiente Medellín | 32.0 | 2 % | 2 % | -0.28 |
| Descanso/final: Empate / Aguilas Doradas | 5.6 | 15 % | 15 % | -0.17 |
| Descanso/final: Empate / Empate | 4.8 | 17 % | 18 % | -0.17 |
| Descanso/final: Empate / Independiente Medellín | 6.5 | 12 % | 13 % | -0.19 |
| Descanso/final: Independiente Medellín / Aguilas Doradas | 30.0 | 2 % | 2 % | -0.26 |
| Descanso/final: Independiente Medellín / Empate | 14.5 | 5 % | 5 % | -0.22 |
| Descanso/final: Independiente Medellín / Independiente Medellín | 4.9 | 18 % | 17 % | -0.13 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.44 | 68 % | 67 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 2.67 | 32 % | 33 % | -0.14 |
| Goles 1.er tiempo Más 0.75 | 1.6 | 61 % | 60 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.3 | 40 % | 41 % | -0.08 |
| Goles 1.er tiempo Más 1.0 | 1.95 | 50 % | 49 % | -0.02 |
| Goles 1.er tiempo Menos 1.0 | 1.83 | 52 % | 53 % | -0.05 |
| Goles 1.er tiempo Más 1.25 | 2.42 | 39 % | 39 % | -0.05 |
| Goles 1.er tiempo Menos 1.25 | 1.55 | 62 % | 62 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 2.82 | 32 % | 31 % | -0.10 |
| Goles 1.er tiempo Menos 1.5 | 1.4 | 68 % | 69 % | -0.05 |
| Goles 1.er tiempo Más 2.5 | 6.4 | 11 % | 11 % | -0.28 |
| Goles 1.er tiempo Menos 2.5 | 1.1 | 89 % | 89 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.25 | 77 % | 78 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 3.85 | 23 % | 22 % | -0.12 |
| Goles 2.º tiempo Más 1.5 | 2.07 | 44 % | 45 % | -0.09 |
| Goles 2.º tiempo Menos 1.5 | 1.72 | 56 % | 55 % | -0.03 |
| Goles 2.º tiempo Más 2.5 | 4.25 | 19 % | 19 % | -0.21 |
| Goles 2.º tiempo Menos 2.5 | 1.21 | 81 % | 81 % | -0.02 |

**Goles, esperado ficha:** local 1.43, visitante 1.21, total 2.64 (modelo: λ local 1.37, visitante 1.24). Muestra local 7, visitante 7, directos 6.

**Líneas de goles que cumplen 5 de 7 en ambos (9):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.29 | 1.43 | 0.93 | 5 de 7 | 6 de 7 | 4 de 6 | 75 % | 68 % | 75 % | -0.03 | -0.12 | PROTECCIÓN |
| local | Menos 2.5 | 1.16 | 1.43 | 1.07 | 7 de 7 | 5 de 7 | 6 de 6 | 85 % | 78 % | 84 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 3.5 | 1.04 | 1.43 | 2.07 | 7 de 7 | 7 de 7 | 6 de 6 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.07 | 2.64 | 2.14 | 7 de 7 | 7 de 7 | 5 de 6 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 3.5 | 1.33 | 2.64 | 0.86 | 6 de 7 | 5 de 7 | 6 de 6 | 73 % | 66 % | 73 % | -0.03 | -0.12 | PROTECCIÓN |
| total | Menos 4.5 | 1.12 | 2.64 | 1.86 | 7 de 7 | 6 de 7 | 6 de 6 | 87 % | 80 % | 87 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.04 | 2.64 | 2.86 | 7 de 7 | 7 de 7 | 6 de 6 | 95 % | 88 % | 95 % | -0.01 | -0.09 | PROTECCIÓN |
| visitante | Más 0.5 | 1.33 | 1.21 | 0.71 | 5 de 7 | 6 de 7 | 5 de 6 | 73 % | 66 % | 73 % | -0.03 | -0.13 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.12 | 1.21 | 1.29 | 7 de 7 | 6 de 7 | 6 de 6 | 87 % | 80 % | 87 % | -0.02 | -0.10 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (39 %) en línea con el mercado; total esperado ficha 2.64 vs modelo 2.62. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 3.5 @1.33 (p 73 %, aj. 66 %).


---

## 15:30 · Atletico Nacional - Once Caldas (Colombia Categoría Primera A)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 1, 'equipo': 'Atl. Nacional', 'pj': 18, 'g': 12, 'e': 3, 'p': 3, 'gf_gc': '37:17', 'dg': 20, 'pts': 39, 'grupo': ''}, 'visitante': {'pos': 8, 'equipo': 'Once Caldas', 'pj': 18, 'g': 7, 'e': 6, 'p': 5, 'gf_gc': '22:18', 'dg': 4, 'pts': 27, 'grupo': ''}}; bajas: ninguna anotada; clima: 23.5 °C al inicio, humedad 79 %, prob. de lluvia máx. 93 %, lluvia máx. 0.3 mm/h, viento máx. 5.2 km/h (código OMM al inicio 51) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Atletico Nacional | 2.6 | 37 % | 37 % | +0.3 | -0.03 |
| Empate | 3.4 | 28 % | 28 % | +0.0 | -0.05 |
| Gana Once Caldas | 2.72 | 35 % | 35 % | -0.3 | -0.05 |

Favorito del modelo: **local** (37 %). Alertas: Revisar: la simulación sin contexto se aleja 15 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 16 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 4 de 7, no perdió 6 de 7, perdió 1 de 7; visitante ganó 4 de 7, no perdió 7 de 7, perdió 0 de 7. Directos (n=6) con ambos marcan: 3 de 6. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 4 de 7 · V perdió 0 de 7 → no
- Gana visitante: V ganó 4 de 7 · L perdió 1 de 7 → no
- Local o empate: L no perdió 6 de 7 · V no ganó 3 de 7 → no
- Visitante o empate: V no perdió 7 de 7 · L no ganó 3 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Atletico Nacional o empate | 1.5 | 65 % | 65 % | -0.02 |
| Once Caldas o empate | 1.53 | 63 % | 63 % | -0.04 |
| No hay empate | 1.31 | 72 % | 72 % | -0.06 |

**Ambos marcan** (L ambos marcan 4 de 7, V 3 de 7, directos 3 de 6):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.57 | 60 % | 60 % | -0.06 | L 4 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 2.25 | 40 % | 40 % | -0.10 | L 3 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Atletico Nacional | 3.0 | 30 % | 30 % | -0.11 |
| 1.er tiempo: Empate | 2.15 | 43 % | 43 % | -0.08 |
| 1.er tiempo: Once Caldas | 3.2 | 28 % | 28 % | -0.11 |
| 2.º tiempo: Atletico Nacional | 2.82 | 32 % | 32 % | -0.09 |
| 2.º tiempo: Empate | 2.52 | 36 % | 36 % | -0.08 |
| 2.º tiempo: Once Caldas | 2.85 | 31 % | 32 % | -0.11 |
| Descanso o final: Atletico Nacional | 1.95 | 47 % | 48 % | -0.09 |
| Descanso o final: Empate | 1.67 | 55 % | 56 % | -0.08 |
| Descanso o final: Once Caldas | 2.07 | 44 % | 45 % | -0.09 |
| Descanso/final: Atletico Nacional / Atletico Nacional | 4.15 | 21 % | 21 % | -0.13 |
| Descanso/final: Atletico Nacional / Empate | 12.5 | 6 % | 6 % | -0.25 |
| Descanso/final: Atletico Nacional / Once Caldas | 28.0 | 3 % | 3 % | -0.28 |
| Descanso/final: Empate / Atletico Nacional | 6.0 | 14 % | 14 % | -0.18 |
| Descanso/final: Empate / Empate | 5.2 | 16 % | 16 % | -0.15 |
| Descanso/final: Empate / Once Caldas | 6.4 | 13 % | 13 % | -0.17 |
| Descanso/final: Once Caldas / Atletico Nacional | 30.0 | 3 % | 2 % | -0.21 |
| Descanso/final: Once Caldas / Empate | 14.0 | 6 % | 5 % | -0.22 |
| Descanso/final: Once Caldas / Once Caldas | 4.4 | 19 % | 20 % | -0.15 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.37 | 71 % | 70 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.95 | 29 % | 30 % | -0.14 |
| Goles 1.er tiempo Más 0.75 | 1.5 | 65 % | 65 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.55 | 36 % | 36 % | -0.08 |
| Goles 1.er tiempo Más 1.0 | 1.75 | 56 % | 55 % | -0.02 |
| Goles 1.er tiempo Menos 1.0 | 2.05 | 46 % | 47 % | -0.05 |
| Goles 1.er tiempo Más 1.25 | 2.15 | 44 % | 44 % | -0.06 |
| Goles 1.er tiempo Menos 1.25 | 1.67 | 57 % | 57 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 2.55 | 35 % | 35 % | -0.10 |
| Goles 1.er tiempo Menos 1.5 | 1.47 | 65 % | 65 % | -0.05 |
| Goles 1.er tiempo Más 2.5 | 5.5 | 13 % | 13 % | -0.26 |
| Goles 1.er tiempo Menos 2.5 | 1.13 | 87 % | 87 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 10.25 | 4 % | 4 % | -0.58 |
| Goles 1.er tiempo Menos 3.5 | 1.03 | 96 % | 96 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.22 | 80 % | 80 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 4.1 | 20 % | 20 % | -0.17 |
| Goles 2.º tiempo Más 1.5 | 1.98 | 47 % | 47 % | -0.06 |
| Goles 2.º tiempo Menos 1.5 | 1.8 | 53 % | 53 % | -0.05 |
| Goles 2.º tiempo Más 2.5 | 3.9 | 21 % | 22 % | -0.16 |
| Goles 2.º tiempo Menos 2.5 | 1.24 | 79 % | 78 % | -0.03 |

**Goles, esperado ficha:** local 1.14, visitante 1.14, total 2.29 (modelo: λ local 1.43, visitante 1.39). Muestra local 7, visitante 7, directos 6.

**Líneas de goles que cumplen 5 de 7 en ambos (11):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.18 | 1.14 | 1.36 | 5 de 7 | 7 de 7 | 5 de 6 | 83 % | 76 % | 82 % | -0.02 | -0.11 | PROTECCIÓN |
| local | Menos 3.5 | 1.05 | 1.14 | 2.36 | 6 de 7 | 7 de 7 | 6 de 6 | 94 % | 87 % | 94 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.05 | 2.29 | 1.79 | 7 de 7 | 7 de 7 | 6 de 6 | 94 % | 87 % | 94 % | -0.02 | -0.09 | PROTECCIÓN |
| total | Más 1.5 | 1.25 | 2.29 | 0.79 | 6 de 7 | 5 de 7 | 4 de 6 | 78 % | 71 % | 78 % | -0.03 | -0.12 | PROTECCIÓN |
| total | Menos 3.5 | 1.4 | 2.29 | 1.21 | 6 de 7 | 7 de 7 | 5 de 6 | 68 % | 61 % | 69 % | -0.04 | -0.14 | PROTECCIÓN |
| total | Menos 4.5 | 1.16 | 2.29 | 2.21 | 6 de 7 | 7 de 7 | 6 de 6 | 84 % | 77 % | 84 % | -0.03 | -0.11 | PROTECCIÓN |
| total | Menos 5.5 | 1.06 | 2.29 | 3.21 | 6 de 7 | 7 de 7 | 6 de 6 | 93 % | 86 % | 93 % | -0.01 | -0.09 | PROTECCIÓN |
| visitante | Más 0.5 | 1.26 | 1.14 | 0.64 | 5 de 7 | 7 de 7 | 4 de 6 | 77 % | 70 % | 77 % | -0.04 | -0.12 | PROTECCIÓN |
| visitante | Menos 1.5 | 1.6 | 1.14 | 0.36 | 6 de 7 | 5 de 7 | 6 de 6 | 59 % | 52 % | 59 % | -0.05 | -0.17 |  |
| visitante | Menos 2.5 | 1.16 | 1.14 | 1.36 | 6 de 7 | 7 de 7 | 6 de 6 | 84 % | 77 % | 84 % | -0.03 | -0.11 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.04 | 1.14 | 2.36 | 7 de 7 | 7 de 7 | 6 de 6 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (37 %) en línea con el mercado; total esperado ficha 2.29 vs modelo 2.82. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 3.5 @1.4 (p 68 %, aj. 61 %).


---

## 15:30 · Deportivo Cali - Deportes Tolima (Colombia Categoría Primera A)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 2, 'equipo': 'Deportivo Cali', 'pj': 18, 'g': 9, 'e': 7, 'p': 2, 'gf_gc': '26:10', 'dg': 16, 'pts': 34, 'grupo': ''}, 'visitante': {'pos': 9, 'equipo': 'Tolima', 'pj': 18, 'g': 7, 'e': 5, 'p': 6, 'gf_gc': '23:21', 'dg': 2, 'pts': 26, 'grupo': ''}}; bajas: ninguna anotada; clima: 25.3 °C al inicio, humedad 78 %, prob. de lluvia máx. 100 %, lluvia máx. 0.1 mm/h, viento máx. 5.8 km/h (código OMM al inicio 51) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Deportivo Cali | 2.32 | 41 % | 42 % | -0.3 | -0.04 |
| Empate | 3.25 | 30 % | 29 % | +0.4 | -0.04 |
| Gana Deportes Tolima | 3.25 | 29 % | 29 % | -0.1 | -0.05 |

Favorito del modelo: **local** (41 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 7 de 7, perdió 0 de 7; visitante ganó 2 de 7, no perdió 4 de 7, perdió 3 de 7. Directos (n=6) con ambos marcan: 5 de 6. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 3 de 7 → no
- Gana visitante: V ganó 2 de 7 · L perdió 0 de 7 → no
- Local o empate: L no perdió 7 de 7 · V no ganó 5 de 7 → sí
- Visitante o empate: V no perdió 4 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Deportivo Cali o empate | 1.38 | 71 % | 71 % | -0.02 |
| Deportes Tolima o empate | 1.65 | 59 % | 58 % | -0.03 |
| No hay empate | 1.33 | 70 % | 71 % | -0.06 |

**Ambos marcan** (L ambos marcan 2 de 7, V 4 de 7, directos 5 de 6):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.88 | 49 % | 49 % | -0.07 | L 2 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 1.82 | 51 % | 51 % | -0.08 | L 5 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Deportivo Cali | 2.95 | 30 % | 30 % | -0.10 |
| 1.er tiempo: Empate | 1.98 | 47 % | 47 % | -0.08 |
| 1.er tiempo: Deportes Tolima | 3.8 | 23 % | 23 % | -0.12 |
| 2.º tiempo: Deportivo Cali | 2.65 | 34 % | 34 % | -0.10 |
| 2.º tiempo: Empate | 2.35 | 40 % | 39 % | -0.06 |
| 2.º tiempo: Deportes Tolima | 3.4 | 26 % | 26 % | -0.11 |
| Descanso o final: Deportivo Cali | 1.85 | 49 % | 51 % | -0.09 |
| Descanso o final: Empate | 1.6 | 58 % | 58 % | -0.08 |
| Descanso o final: Deportes Tolima | 2.37 | 38 % | 39 % | -0.10 |
| Descanso/final: Deportivo Cali / Deportivo Cali | 3.8 | 23 % | 23 % | -0.12 |
| Descanso/final: Deportivo Cali / Empate | 14.0 | 6 % | 5 % | -0.22 |
| Descanso/final: Deportivo Cali / Deportes Tolima | 40.0 | 2 % | 2 % | -0.31 |
| Descanso/final: Empate / Deportivo Cali | 5.2 | 16 % | 16 % | -0.17 |
| Descanso/final: Empate / Empate | 4.5 | 19 % | 19 % | -0.14 |
| Descanso/final: Empate / Deportes Tolima | 6.8 | 12 % | 12 % | -0.20 |
| Descanso/final: Deportes Tolima / Deportivo Cali | 35.0 | 2 % | 2 % | -0.27 |
| Descanso/final: Deportes Tolima / Empate | 15.5 | 5 % | 5 % | -0.22 |
| Descanso/final: Deportes Tolima / Deportes Tolima | 5.4 | 16 % | 16 % | -0.15 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.52 | 64 % | 63 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.45 | 36 % | 37 % | -0.12 |
| Goles 1.er tiempo Más 0.75 | 1.72 | 56 % | 56 % | -0.03 |
| Goles 1.er tiempo Menos 0.75 | 2.07 | 45 % | 46 % | -0.07 |
| Goles 1.er tiempo Más 1.0 | 2.2 | 44 % | 43 % | -0.03 |
| Goles 1.er tiempo Menos 1.0 | 1.65 | 58 % | 59 % | -0.04 |
| Goles 1.er tiempo Más 1.25 | 2.75 | 34 % | 34 % | -0.06 |
| Goles 1.er tiempo Menos 1.25 | 1.44 | 67 % | 67 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 3.2 | 28 % | 27 % | -0.12 |
| Goles 1.er tiempo Menos 1.5 | 1.32 | 72 % | 73 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 7.3 | 9 % | 8 % | -0.37 |
| Goles 1.er tiempo Menos 2.5 | 1.07 | 91 % | 92 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.31 | 73 % | 74 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 3.4 | 27 % | 26 % | -0.09 |
| Goles 2.º tiempo Más 1.5 | 2.35 | 38 % | 39 % | -0.11 |
| Goles 2.º tiempo Menos 1.5 | 1.57 | 62 % | 61 % | -0.02 |
| Goles 2.º tiempo Más 2.5 | 5.0 | 15 % | 16 % | -0.25 |
| Goles 2.º tiempo Menos 2.5 | 1.16 | 85 % | 84 % | -0.01 |

**Goles, esperado ficha:** local 1.21, visitante 0.71, total 1.93 (modelo: λ local 1.30, visitante 1.05). Muestra local 7, visitante 7, directos 6.

**Líneas de goles que cumplen 5 de 7 en ambos (5):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.14 | 1.21 | 1.29 | 5 de 7 | 6 de 7 | 6 de 6 | 86 % | 79 % | 86 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 3.5 | 1.03 | 1.21 | 2.29 | 7 de 7 | 7 de 7 | 6 de 6 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Menos 3.5 | 1.24 | 1.93 | 1.57 | 6 de 7 | 5 de 7 | 6 de 6 | 79 % | 72 % | 78 % | -0.02 | -0.11 | PROTECCIÓN |
| total | Menos 4.5 | 1.08 | 1.93 | 2.57 | 7 de 7 | 6 de 7 | 6 de 6 | 91 % | 84 % | 91 % | -0.02 | -0.09 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.08 | 0.71 | 1.79 | 7 de 7 | 6 de 7 | 6 de 6 | 91 % | 84 % | 91 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (41 %) en línea con el mercado; total esperado ficha 1.93 vs modelo 2.35. No hay línea que cumpla con cuota ≥ 1,30 (solo protecciones o ninguna).


---

## 15:30 · Millonarios FC - Alianza FC (Colombia Categoría Primera A)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 7, 'equipo': 'Millonarios', 'pj': 18, 'g': 6, 'e': 9, 'p': 3, 'gf_gc': '25:16', 'dg': 9, 'pts': 27, 'grupo': ''}, 'visitante': {'pos': 16, 'equipo': 'Alianza', 'pj': 18, 'g': 5, 'e': 3, 'p': 10, 'gf_gc': '18:31', 'dg': -13, 'pts': 18, 'grupo': ''}}; bajas: ninguna anotada; clima: 21.2 °C al inicio, humedad 41 %, prob. de lluvia máx. 95 %, lluvia máx. 0.2 mm/h, viento máx. 6.2 km/h (código OMM al inicio 51) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Millonarios FC | 1.33 | 75 % | 74 % | +0.8 | -0.01 |
| Empate | 5.2 | 17 % | 17 % | +0.1 | -0.10 |
| Gana Alianza FC | 9.5 | 8 % | 9 % | -0.9 | -0.22 |

Favorito del modelo: **local** (75 %). Alertas: Revisar: la simulación sin contexto se aleja 29 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 38 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 42 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 1 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 2 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=6) con ambos marcan: 4 de 6. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 1 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 2 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 5 de 7 → sí
- Visitante o empate: V no perdió 3 de 7 · L no ganó 6 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Millonarios FC o empate | 1.08 | 92 % | 91 % | -0.01 |
| Alianza FC o empate | 3.45 | 25 % | 26 % | -0.12 |
| No hay empate | 1.16 | 83 % | 83 % | -0.04 |

**Ambos marcan** (L ambos marcan 6 de 7, V 4 de 7, directos 4 de 6):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 2.1 | 44 % | 43 % | -0.07 | L 6 de 7 · V 4 de 7 → no |
| Ambos marcan: No | 1.65 | 56 % | 57 % | -0.08 | L 1 de 7 · V 3 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Millonarios FC | 1.78 | 54 % | 52 % | -0.04 |
| 1.er tiempo: Empate | 2.4 | 36 % | 37 % | -0.13 |
| 1.er tiempo: Alianza FC | 7.5 | 10 % | 10 % | -0.27 |
| 2.º tiempo: Millonarios FC | 1.6 | 58 % | 59 % | -0.07 |
| 2.º tiempo: Empate | 3.0 | 30 % | 30 % | -0.09 |
| 2.º tiempo: Alianza FC | 7.3 | 11 % | 11 % | -0.18 |
| Descanso o final: Millonarios FC | 1.25 | 77 % | 75 % | -0.03 |
| Descanso o final: Empate | 2.02 | 44 % | 46 % | -0.11 |
| Descanso o final: Alianza FC | 5.1 | 16 % | 18 % | -0.21 |
| Descanso/final: Millonarios FC / Millonarios FC | 1.9 | 50 % | 48 % | -0.05 |
| Descanso/final: Millonarios FC / Empate | 21.0 | 4 % | 3 % | -0.25 |
| Descanso/final: Millonarios FC / Alianza FC | 90.0 | 1 % | 1 % | -0.43 |
| Descanso/final: Empate / Millonarios FC | 3.75 | 22 % | 22 % | -0.18 |
| Descanso/final: Empate / Empate | 7.1 | 11 % | 11 % | -0.24 |
| Descanso/final: Empate / Alianza FC | 17.5 | 4 % | 4 % | -0.38 |
| Descanso/final: Alianza FC / Millonarios FC | 24.0 | 3 % | 3 % | -0.35 |
| Descanso/final: Alianza FC / Empate | 22.0 | 3 % | 3 % | -0.36 |
| Descanso/final: Alianza FC / Alianza FC | 15.5 | 4 % | 5 % | -0.38 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.35 | 73 % | 71 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 3.0 | 27 % | 29 % | -0.18 |
| Goles 1.er tiempo Más 0.75 | 1.47 | 67 % | 66 % | -0.01 |
| Goles 1.er tiempo Menos 0.75 | 2.6 | 34 % | 35 % | -0.12 |
| Goles 1.er tiempo Más 1.0 | 1.72 | 58 % | 56 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.07 | 44 % | 46 % | -0.08 |
| Goles 1.er tiempo Más 1.25 | 2.15 | 45 % | 44 % | -0.02 |
| Goles 1.er tiempo Menos 1.25 | 1.67 | 56 % | 57 % | -0.07 |
| Goles 1.er tiempo Más 1.5 | 2.55 | 37 % | 35 % | -0.06 |
| Goles 1.er tiempo Menos 1.5 | 1.47 | 63 % | 65 % | -0.07 |
| Goles 1.er tiempo Más 2.5 | 5.5 | 14 % | 13 % | -0.24 |
| Goles 1.er tiempo Menos 2.5 | 1.12 | 86 % | 87 % | -0.04 |
| Goles 1.er tiempo Más 3.5 | 10.25 | 4 % | 4 % | -0.56 |
| Goles 1.er tiempo Menos 3.5 | 1.03 | 96 % | 96 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.2 | 80 % | 81 % | -0.04 |
| Goles 2.º tiempo Menos 0.5 | 4.35 | 20 % | 19 % | -0.14 |
| Goles 2.º tiempo Más 1.5 | 1.9 | 48 % | 50 % | -0.09 |
| Goles 2.º tiempo Menos 1.5 | 1.87 | 52 % | 50 % | -0.03 |
| Goles 2.º tiempo Más 2.5 | 3.7 | 22 % | 23 % | -0.19 |
| Goles 2.º tiempo Menos 2.5 | 1.27 | 78 % | 77 % | -0.01 |

**Goles, esperado ficha:** local 1.43, visitante 1.14, total 2.57 (modelo: λ local 2.25, visitante 0.65). Muestra local 7, visitante 7, directos 6.

**Líneas de goles que cumplen 5 de 7 en ambos (9):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.1 | 1.43 | 0.93 | 6 de 7 | 5 de 7 | 5 de 6 | 90 % | 83 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |
| local | Menos 2.5 | 1.55 | 1.43 | 1.07 | 6 de 7 | 6 de 7 | 6 de 6 | 61 % | 54 % | 61 % | -0.05 | -0.16 |  |
| local | Menos 3.5 | 1.2 | 1.43 | 2.07 | 6 de 7 | 7 de 7 | 6 de 6 | 82 % | 75 % | 81 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 4.5 | 1.06 | 1.43 | 3.07 | 7 de 7 | 7 de 7 | 6 de 6 | 93 % | 86 % | 93 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 0.5 | 1.04 | 2.57 | 2.07 | 6 de 7 | 7 de 7 | 6 de 6 | 95 % | 88 % | 95 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 3.5 | 1.44 | 2.57 | 0.93 | 5 de 7 | 5 de 7 | 5 de 6 | 67 % | 60 % | 67 % | -0.04 | -0.14 | PROTECCIÓN |
| total | Menos 4.5 | 1.17 | 2.57 | 1.93 | 6 de 7 | 7 de 7 | 6 de 6 | 84 % | 76 % | 83 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.06 | 2.57 | 2.93 | 7 de 7 | 7 de 7 | 6 de 6 | 93 % | 86 % | 93 % | -0.02 | -0.09 | PROTECCIÓN |
| visitante | Más 0.5 | 1.93 | 1.14 | 0.64 | 6 de 7 | 6 de 7 | 5 de 6 | 49 % | 42 % | 48 % | -0.06 | -0.20 |  |

**Lectura:** el modelo da local favorito (75 %) en línea con el mercado; total esperado ficha 2.57 vs modelo 2.91. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 3.5 @1.44 (p 67 %, aj. 60 %).


---

## 16:30 · Mirassol SP - Clube Atletico MG (Brasil Brasileirao - Serie A)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 14, 'equipo': 'Mirassol', 'pj': 34, 'g': 10, 'e': 10, 'p': 14, 'gf_gc': '39:48', 'dg': -9, 'pts': 40, 'grupo': ''}, 'visitante': {'pos': 7, 'equipo': 'Atlético-MG', 'pj': 34, 'g': 14, 'e': 8, 'p': 12, 'gf_gc': '44:40', 'dg': 4, 'pts': 50, 'grupo': ''}}; bajas: ninguna anotada; clima: 31.6 °C al inicio, humedad 42 %, prob. de lluvia máx. 41 %, lluvia máx. 0 mm/h, viento máx. 9.9 km/h (código OMM al inicio 1) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Mirassol SP | 1.98 | 49 % | 49 % | -0.1 | -0.03 |
| Empate | 3.6 | 27 % | 26 % | +0.4 | -0.05 |
| Gana Clube Atletico MG | 3.75 | 25 % | 25 % | -0.3 | -0.07 |

Favorito del modelo: **local** (49 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 1 de 7, no perdió 2 de 7, perdió 5 de 7. Directos (n=3) con ambos marcan: 2 de 3. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 5 de 7 → no
- Gana visitante: V ganó 1 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 6 de 7 → sí
- Visitante o empate: V no perdió 2 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Mirassol SP o empate | 1.29 | 75 % | 75 % | -0.03 |
| Clube Atletico MG o empate | 1.87 | 51 % | 51 % | -0.04 |
| No hay empate | 1.28 | 73 % | 74 % | -0.06 |

**Ambos marcan** (L ambos marcan 3 de 7, V 2 de 7, directos 2 de 3):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.7 | 56 % | 55 % | -0.04 | L 3 de 7 · V 2 de 7 → no |
| Ambos marcan: No | 2.07 | 44 % | 45 % | -0.09 | L 4 de 7 · V 5 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Mirassol SP | 2.52 | 36 % | 36 % | -0.08 |
| 1.er tiempo: Empate | 2.2 | 42 % | 42 % | -0.07 |
| 1.er tiempo: Clube Atletico MG | 4.15 | 21 % | 21 % | -0.12 |
| 2.º tiempo: Mirassol SP | 2.3 | 40 % | 40 % | -0.08 |
| 2.º tiempo: Empate | 2.55 | 36 % | 36 % | -0.07 |
| 2.º tiempo: Clube Atletico MG | 3.7 | 23 % | 24 % | -0.13 |
| Descanso o final: Mirassol SP | 1.65 | 56 % | 57 % | -0.07 |
| Descanso o final: Empate | 1.72 | 54 % | 54 % | -0.07 |
| Descanso o final: Clube Atletico MG | 2.6 | 34 % | 36 % | -0.11 |
| Descanso/final: Mirassol SP / Mirassol SP | 3.05 | 29 % | 29 % | -0.11 |
| Descanso/final: Mirassol SP / Empate | 14.0 | 6 % | 5 % | -0.23 |
| Descanso/final: Mirassol SP / Clube Atletico MG | 40.0 | 2 % | 2 % | -0.29 |
| Descanso/final: Empate / Mirassol SP | 5.0 | 17 % | 17 % | -0.15 |
| Descanso/final: Empate / Empate | 5.4 | 16 % | 16 % | -0.15 |
| Descanso/final: Empate / Clube Atletico MG | 8.25 | 10 % | 10 % | -0.21 |
| Descanso/final: Clube Atletico MG / Mirassol SP | 26.0 | 3 % | 3 % | -0.27 |
| Descanso/final: Clube Atletico MG / Empate | 15.0 | 5 % | 5 % | -0.21 |
| Descanso/final: Clube Atletico MG / Clube Atletico MG | 6.1 | 13 % | 14 % | -0.19 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.38 | 70 % | 70 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.95 | 30 % | 30 % | -0.12 |
| Goles 1.er tiempo Más 0.75 | 1.53 | 64 % | 64 % | -0.02 |
| Goles 1.er tiempo Menos 0.75 | 2.52 | 37 % | 37 % | -0.07 |
| Goles 1.er tiempo Más 1.0 | 1.8 | 54 % | 54 % | -0.02 |
| Goles 1.er tiempo Menos 1.0 | 2.02 | 47 % | 48 % | -0.04 |
| Goles 1.er tiempo Más 1.25 | 2.25 | 43 % | 42 % | -0.04 |
| Goles 1.er tiempo Menos 1.25 | 1.65 | 58 % | 59 % | -0.04 |
| Goles 1.er tiempo Más 1.5 | 2.65 | 35 % | 34 % | -0.08 |
| Goles 1.er tiempo Menos 1.5 | 1.47 | 65 % | 66 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 6.0 | 13 % | 12 % | -0.25 |
| Goles 1.er tiempo Menos 2.5 | 1.12 | 87 % | 88 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.24 | 78 % | 79 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 3.95 | 22 % | 21 % | -0.14 |
| Goles 2.º tiempo Más 1.5 | 2.05 | 45 % | 46 % | -0.07 |
| Goles 2.º tiempo Menos 1.5 | 1.75 | 55 % | 54 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 4.15 | 20 % | 20 % | -0.17 |
| Goles 2.º tiempo Menos 2.5 | 1.22 | 80 % | 80 % | -0.02 |

**Goles, esperado ficha:** local 1.29, visitante 0.71, total 2.0 (modelo: λ local 1.63, visitante 1.11). Muestra local 7, visitante 7, directos 3.

**Líneas de goles que cumplen 5 de 7 en ambos (13):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.21 | 1.29 | 0.79 | 5 de 7 | 6 de 7 | 2 de 3 | 81 % | 74 % | 80 % | -0.02 | -0.10 | PROTECCIÓN |
| local | Menos 2.5 | 1.25 | 1.29 | 1.21 | 7 de 7 | 6 de 7 | 3 de 3 | 78 % | 71 % | 78 % | -0.03 | -0.11 | PROTECCIÓN |
| local | Menos 3.5 | 1.07 | 1.29 | 2.21 | 7 de 7 | 7 de 7 | 3 de 3 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Más 0.5 | 1.06 | 2.0 | 1.5 | 7 de 7 | 7 de 7 | 3 de 3 | 93 % | 86 % | 93 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 2.5 | 1.98 | 2.0 | 0.5 | 6 de 7 | 6 de 7 | 1 de 3 | 48 % | 41 % | 48 % | -0.05 | -0.19 |  |
| total | Menos 2.75 | 1.78 | 2.0 | 0.75 | 6 de 7 | 6 de 7 | 1 de 3 | 54 % | 47 % | 55 % | -0.03 | -0.16 |  |
| total | Menos 3.0 | 1.57 | 2.0 | 1.0 | 6 de 7 | 6 de 7 | 1 de 3 | 62 % | 55 % | 62 % | -0.02 | -0.13 |  |
| total | Menos 3.25 | 1.47 | 2.0 | 1.25 | 6 de 7 | 6 de 7 | 1 de 3 | 67 % | 60 % | 67 % | -0.02 | -0.12 | PROTECCIÓN |
| total | Menos 3.5 | 1.38 | 2.0 | 1.5 | 7 de 7 | 6 de 7 | 1 de 3 | 70 % | 63 % | 70 % | -0.03 | -0.12 | PROTECCIÓN |
| total | Menos 4.5 | 1.15 | 2.0 | 2.5 | 7 de 7 | 6 de 7 | 3 de 3 | 86 % | 79 % | 86 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 5.5 | 1.05 | 2.0 | 3.5 | 7 de 7 | 7 de 7 | 3 de 3 | 94 % | 87 % | 94 % | -0.01 | -0.09 | PROTECCIÓN |
| visitante | Menos 1.5 | 1.38 | 0.71 | 0.79 | 6 de 7 | 6 de 7 | 1 de 3 | 69 % | 62 % | 70 % | -0.04 | -0.14 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.09 | 0.71 | 1.79 | 7 de 7 | 7 de 7 | 2 de 3 | 90 % | 83 % | 90 % | -0.02 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da local favorito (49 %) en línea con el mercado; total esperado ficha 2.0 vs modelo 2.74. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 3.5 @1.38 (p 70 %, aj. 63 %).


---

## 17:00 · CA Banfield - Boca Juniors (Argentina Copa Argentina)

Competición/contexto: importancia «normal»; tabla: sin dato; bajas: ninguna anotada; clima: 26.4 °C al inicio, humedad 24 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 6.3 km/h (código OMM al inicio 1) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana CA Banfield | 7.1 | 12 % | 13 % | -0.0 | -0.11 |
| Empate | 3.75 | 24 % | 25 % | -0.3 | -0.09 |
| Gana Boca Juniors | 1.55 | 63 % | 63 % | +0.4 | -0.02 |

Favorito del modelo: **visitante** (64 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 1 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 5 de 7, no perdió 6 de 7, perdió 1 de 7. Directos (n=5) con ambos marcan: 0 de 5. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 1 de 7 · V perdió 1 de 7 → no
- Gana visitante: V ganó 5 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 2 de 7 → no
- Visitante o empate: V no perdió 6 de 7 · L no ganó 6 de 7 → sí

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| CA Banfield o empate | 2.5 | 37 % | 37 % | -0.08 |
| Boca Juniors o empate | 1.12 | 88 % | 87 % | -0.02 |
| No hay empate | 1.25 | 76 % | 75 % | -0.05 |

**Ambos marcan** (L ambos marcan 6 de 7, V 3 de 7, directos 0 de 5):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 2.2 | 42 % | 42 % | -0.08 | L 6 de 7 · V 3 de 7 → no |
| Ambos marcan: No | 1.62 | 58 % | 58 % | -0.06 | L 1 de 7 · V 4 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: CA Banfield | 6.9 | 12 % | 12 % | -0.17 |
| 1.er tiempo: Empate | 2.15 | 43 % | 43 % | -0.07 |
| 1.er tiempo: Boca Juniors | 2.1 | 45 % | 44 % | -0.06 |
| 2.º tiempo: CA Banfield | 5.9 | 14 % | 14 % | -0.17 |
| 2.º tiempo: Empate | 2.42 | 38 % | 38 % | -0.09 |
| 2.º tiempo: Boca Juniors | 1.93 | 48 % | 48 % | -0.07 |
| Descanso o final: CA Banfield | 4.3 | 20 % | 22 % | -0.14 |
| Descanso o final: Empate | 1.78 | 52 % | 52 % | -0.08 |
| Descanso o final: Boca Juniors | 1.39 | 68 % | 67 % | -0.06 |
| Descanso/final: CA Banfield / CA Banfield | 11.75 | 6 % | 6 % | -0.28 |
| Descanso/final: CA Banfield / Empate | 20.0 | 4 % | 4 % | -0.29 |
| Descanso/final: CA Banfield / Boca Juniors | 32.0 | 2 % | 2 % | -0.30 |
| Descanso/final: Empate / CA Banfield | 13.5 | 6 % | 5 % | -0.26 |
| Descanso/final: Empate / Empate | 4.9 | 17 % | 17 % | -0.19 |
| Descanso/final: Empate / Boca Juniors | 4.0 | 21 % | 21 % | -0.15 |
| Descanso/final: Boca Juniors / CA Banfield | 80.0 | 1 % | 1 % | -0.34 |
| Descanso/final: Boca Juniors / Empate | 16.5 | 4 % | 4 % | -0.31 |
| Descanso/final: Boca Juniors / Boca Juniors | 2.3 | 40 % | 39 % | -0.09 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.47 | 66 % | 66 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.65 | 34 % | 34 % | -0.09 |
| Goles 1.er tiempo Más 0.75 | 1.65 | 59 % | 59 % | -0.03 |
| Goles 1.er tiempo Menos 0.75 | 2.25 | 42 % | 42 % | -0.05 |
| Goles 1.er tiempo Más 1.0 | 2.02 | 48 % | 48 % | -0.03 |
| Goles 1.er tiempo Menos 1.0 | 1.8 | 54 % | 54 % | -0.03 |
| Goles 1.er tiempo Más 1.25 | 2.55 | 37 % | 37 % | -0.06 |
| Goles 1.er tiempo Menos 1.25 | 1.52 | 64 % | 64 % | -0.03 |
| Goles 1.er tiempo Más 1.5 | 3.0 | 30 % | 30 % | -0.10 |
| Goles 1.er tiempo Menos 1.5 | 1.38 | 70 % | 70 % | -0.03 |
| Goles 1.er tiempo Más 2.5 | 7.0 | 10 % | 10 % | -0.33 |
| Goles 1.er tiempo Menos 2.5 | 1.09 | 90 % | 90 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.33 | 73 % | 73 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 3.25 | 27 % | 27 % | -0.12 |
| Goles 2.º tiempo Más 1.5 | 2.42 | 38 % | 38 % | -0.08 |
| Goles 2.º tiempo Menos 1.5 | 1.55 | 62 % | 62 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 5.3 | 15 % | 15 % | -0.23 |
| Goles 2.º tiempo Menos 2.5 | 1.15 | 85 % | 85 % | -0.02 |

**Goles, esperado ficha:** local 1.0, visitante 1.5, total 2.5 (modelo: λ local 0.66, visitante 1.72). Muestra local 7, visitante 7, directos 5.

**Líneas de goles que cumplen 5 de 7 en ambos (6):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| total | Más 0.5 | 1.09 | 2.5 | 2.0 | 7 de 7 | 7 de 7 | 5 de 5 | 91 % | 84 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 4.5 | 1.09 | 2.5 | 2.0 | 7 de 7 | 7 de 7 | 5 de 5 | 91 % | 84 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 5.5 | 1.03 | 2.5 | 3.0 | 7 de 7 | 7 de 7 | 5 de 5 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.18 | 1.5 | 1.0 | 7 de 7 | 6 de 7 | 3 de 5 | 83 % | 76 % | 82 % | -0.02 | -0.10 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.29 | 1.5 | 1.0 | 6 de 7 | 6 de 7 | 4 de 5 | 75 % | 68 % | 75 % | -0.03 | -0.12 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.09 | 1.5 | 2.0 | 7 de 7 | 7 de 7 | 5 de 5 | 91 % | 84 % | 90 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (64 %) en línea con el mercado; total esperado ficha 2.5 vs modelo 2.38. No hay línea que cumpla con cuota ≥ 1,30 (solo protecciones o ninguna).


---

## 18:00 · Queretaro FC - CF Monterrey (México Liga MX)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 12, 'equipo': 'Querétaro', 'pj': 15, 'g': 6, 'e': 2, 'p': 7, 'gf_gc': '18:23', 'dg': -5, 'pts': 20, 'grupo': ''}, 'visitante': {'pos': 10, 'equipo': 'Monterrey', 'pj': 15, 'g': 6, 'e': 3, 'p': 6, 'gf_gc': '26:25', 'dg': 1, 'pts': 21, 'grupo': ''}}; bajas: ninguna anotada; clima: 21.3 °C al inicio, humedad 40 %, prob. de lluvia máx. 0 %, lluvia máx. 0 mm/h, viento máx. 7.9 km/h (código OMM al inicio 0) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Queretaro FC | 3.45 | 26 % | 27 % | -0.6 | -0.09 |
| Empate | 3.75 | 25 % | 25 % | +0.3 | -0.06 |
| Gana CF Monterrey | 2.0 | 48 % | 48 % | +0.3 | -0.03 |

Favorito del modelo: **visitante** (49 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 2 de 7, no perdió 2 de 7, perdió 5 de 7; visitante ganó 2 de 7, no perdió 4 de 7, perdió 3 de 7. Directos (n=6) con ambos marcan: 3 de 6. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 2 de 7 · V perdió 3 de 7 → no
- Gana visitante: V ganó 2 de 7 · L perdió 5 de 7 → no
- Local o empate: L no perdió 2 de 7 · V no ganó 5 de 7 → no
- Visitante o empate: V no perdió 4 de 7 · L no ganó 5 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Queretaro FC o empate | 1.83 | 52 % | 52 % | -0.06 |
| CF Monterrey o empate | 1.33 | 74 % | 73 % | -0.02 |
| No hay empate | 1.26 | 75 % | 75 % | -0.06 |

**Ambos marcan** (L ambos marcan 3 de 7, V 5 de 7, directos 3 de 6):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.52 | 64 % | 63 % | -0.03 | L 3 de 7 · V 5 de 7 → no |
| Ambos marcan: No | 2.42 | 36 % | 37 % | -0.12 | L 4 de 7 · V 2 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Queretaro FC | 3.8 | 23 % | 24 % | -0.12 |
| 1.er tiempo: Empate | 2.32 | 40 % | 40 % | -0.08 |
| 1.er tiempo: CF Monterrey | 2.55 | 37 % | 36 % | -0.06 |
| 2.º tiempo: Queretaro FC | 3.4 | 26 % | 26 % | -0.12 |
| 2.º tiempo: Empate | 2.75 | 34 % | 33 % | -0.08 |
| 2.º tiempo: CF Monterrey | 2.25 | 41 % | 41 % | -0.09 |
| Descanso o final: Queretaro FC | 2.4 | 37 % | 39 % | -0.11 |
| Descanso o final: Empate | 1.78 | 52 % | 52 % | -0.08 |
| Descanso o final: CF Monterrey | 1.65 | 57 % | 57 % | -0.07 |
| Descanso/final: Queretaro FC / Queretaro FC | 5.7 | 14 % | 15 % | -0.18 |
| Descanso/final: Queretaro FC / Empate | 14.0 | 6 % | 6 % | -0.21 |
| Descanso/final: Queretaro FC / CF Monterrey | 22.0 | 3 % | 3 % | -0.27 |
| Descanso/final: Empate / Queretaro FC | 7.9 | 10 % | 10 % | -0.21 |
| Descanso/final: Empate / Empate | 6.1 | 14 % | 14 % | -0.16 |
| Descanso/final: Empate / CF Monterrey | 5.2 | 16 % | 16 % | -0.17 |
| Descanso/final: CF Monterrey / Queretaro FC | 32.0 | 2 % | 2 % | -0.29 |
| Descanso/final: CF Monterrey / Empate | 14.0 | 6 % | 6 % | -0.21 |
| Descanso/final: CF Monterrey / CF Monterrey | 3.15 | 29 % | 28 % | -0.09 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.32 | 74 % | 73 % | -0.02 |
| Goles 1.er tiempo Menos 0.5 | 3.3 | 26 % | 27 % | -0.15 |
| Goles 1.er tiempo Más 0.75 | 1.44 | 69 % | 68 % | -0.01 |
| Goles 1.er tiempo Menos 0.75 | 2.85 | 32 % | 33 % | -0.09 |
| Goles 1.er tiempo Más 1.0 | 1.62 | 61 % | 60 % | -0.01 |
| Goles 1.er tiempo Menos 1.0 | 2.3 | 41 % | 42 % | -0.07 |
| Goles 1.er tiempo Más 1.25 | 2.02 | 48 % | 47 % | -0.02 |
| Goles 1.er tiempo Menos 1.25 | 1.8 | 52 % | 54 % | -0.06 |
| Goles 1.er tiempo Más 1.5 | 2.37 | 40 % | 39 % | -0.05 |
| Goles 1.er tiempo Menos 1.5 | 1.57 | 60 % | 61 % | -0.06 |
| Goles 1.er tiempo Más 1.75 | 3.0 | 32 % | 31 % | -0.04 |
| Goles 1.er tiempo Menos 1.75 | 1.4 | 69 % | 70 % | -0.04 |
| Goles 1.er tiempo Más 2.5 | 5.2 | 16 % | 15 % | -0.16 |
| Goles 1.er tiempo Menos 2.5 | 1.15 | 84 % | 85 % | -0.04 |
| Goles 1.er tiempo Más 3.5 | 10.25 | 5 % | 5 % | -0.45 |
| Goles 1.er tiempo Menos 3.5 | 1.04 | 95 % | 95 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.17 | 83 % | 84 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 4.85 | 17 % | 16 % | -0.18 |
| Goles 2.º tiempo Más 1.5 | 1.78 | 53 % | 53 % | -0.06 |
| Goles 2.º tiempo Menos 1.5 | 2.02 | 47 % | 47 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 3.25 | 26 % | 27 % | -0.15 |
| Goles 2.º tiempo Menos 2.5 | 1.33 | 74 % | 73 % | -0.02 |

**Goles, esperado ficha:** local 1.57, visitante 1.93, total 3.5 (modelo: λ local 1.32, visitante 1.80). Muestra local 7, visitante 7, directos 6.

**Líneas de goles que cumplen 5 de 7 en ambos (8):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Más 0.5 | 1.31 | 1.57 | 1.07 | 5 de 7 | 7 de 7 | 3 de 6 | 74 % | 67 % | 74 % | -0.02 | -0.12 | PROTECCIÓN |
| local | Menos 3.5 | 1.03 | 1.57 | 1.93 | 7 de 7 | 5 de 7 | 6 de 6 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.04 | 3.5 | 3.0 | 7 de 7 | 7 de 7 | 5 de 6 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 1.5 | 1.2 | 3.5 | 2.0 | 7 de 7 | 6 de 7 | 4 de 6 | 82 % | 75 % | 82 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.09 | 3.5 | 2.0 | 7 de 7 | 5 de 7 | 5 de 6 | 90 % | 83 % | 90 % | -0.02 | -0.09 | PROTECCIÓN |
| total | Menos 6.5 | 1.03 | 3.5 | 3.0 | 7 de 7 | 7 de 7 | 6 de 6 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.16 | 1.93 | 1.43 | 5 de 7 | 5 de 7 | 5 de 6 | 85 % | 78 % | 84 % | -0.02 | -0.10 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.1 | 1.93 | 1.57 | 6 de 7 | 6 de 7 | 4 de 6 | 89 % | 82 % | 89 % | -0.02 | -0.10 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (49 %) en línea con el mercado; total esperado ficha 3.5 vs modelo 3.11. Mejor línea con cuota ≥ 1,30 que cumple: local Más 0.5 @1.31 (p 74 %, aj. 67 %).


---

## 18:30 · Chapecoense SC - Vasco da Gama RJ (Brasil Brasileirao - Serie A)

Competición/contexto: importancia «normal»; tabla: {'local': {'pos': 20, 'equipo': 'Chapecoense', 'pj': 33, 'g': 4, 'e': 9, 'p': 20, 'gf_gc': '33:68', 'dg': -35, 'pts': 21, 'grupo': ''}, 'visitante': {'pos': 13, 'equipo': 'Vasco', 'pj': 33, 'g': 11, 'e': 8, 'p': 14, 'gf_gc': '43:50', 'dg': -7, 'pts': 41, 'grupo': ''}}; bajas: ninguna anotada; clima: 19.5 °C al inicio, humedad 99 %, prob. de lluvia máx. 45 %, lluvia máx. 2.3 mm/h, viento máx. 13.5 km/h (código OMM al inicio 95) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Chapecoense SC | 6.9 | 12 % | 13 % | -0.9 | -0.17 |
| Empate | 4.8 | 19 % | 19 % | +0.3 | -0.07 |
| Gana Vasco da Gama RJ | 1.44 | 69 % | 68 % | +0.7 | -0.01 |

Favorito del modelo: **visitante** (69 %). Alertas: Revisar: la simulación sin contexto se aleja 20 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?); Revisar: la simulación sin contexto se aleja 21 pts del mercado (¿línea mal copiada, equipo cambiado o dato viejo?). Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 1 de 7, no perdió 2 de 7, perdió 5 de 7; visitante ganó 2 de 7, no perdió 3 de 7, perdió 4 de 7. Directos (n=3) con ambos marcan: 1 de 3. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 1 de 7 · V perdió 4 de 7 → no
- Gana visitante: V ganó 2 de 7 · L perdió 5 de 7 → no
- Local o empate: L no perdió 2 de 7 · V no ganó 5 de 7 → no
- Visitante o empate: V no perdió 3 de 7 · L no ganó 6 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Chapecoense SC o empate | 2.87 | 31 % | 32 % | -0.10 |
| Vasco da Gama RJ o empate | 1.13 | 88 % | 87 % | -0.01 |
| No hay empate | 1.18 | 81 % | 81 % | -0.05 |

**Ambos marcan** (L ambos marcan 4 de 7, V 5 de 7, directos 1 de 3):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 1.8 | 52 % | 52 % | -0.06 | L 4 de 7 · V 5 de 7 → no |
| Ambos marcan: No | 1.93 | 48 % | 48 % | -0.08 | L 3 de 7 · V 2 de 7 → no |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Chapecoense SC | 6.0 | 13 % | 14 % | -0.21 |
| 1.er tiempo: Empate | 2.6 | 35 % | 35 % | -0.08 |
| 1.er tiempo: Vasco da Gama RJ | 1.85 | 52 % | 51 % | -0.05 |
| 2.º tiempo: Chapecoense SC | 5.7 | 15 % | 15 % | -0.16 |
| 2.º tiempo: Empate | 2.87 | 32 % | 31 % | -0.09 |
| 2.º tiempo: Vasco da Gama RJ | 1.75 | 54 % | 54 % | -0.06 |
| Descanso o final: Chapecoense SC | 3.95 | 21 % | 24 % | -0.18 |
| Descanso o final: Empate | 2.05 | 45 % | 46 % | -0.08 |
| Descanso o final: Vasco da Gama RJ | 1.31 | 73 % | 71 % | -0.04 |
| Descanso/final: Chapecoense SC / Chapecoense SC | 10.75 | 6 % | 7 % | -0.33 |
| Descanso/final: Chapecoense SC / Empate | 18.0 | 4 % | 4 % | -0.30 |
| Descanso/final: Chapecoense SC / Vasco da Gama RJ | 22.0 | 3 % | 3 % | -0.32 |
| Descanso/final: Empate / Chapecoense SC | 14.5 | 5 % | 5 % | -0.30 |
| Descanso/final: Empate / Empate | 7.1 | 11 % | 11 % | -0.21 |
| Descanso/final: Empate / Vasco da Gama RJ | 4.4 | 19 % | 19 % | -0.15 |
| Descanso/final: Vasco da Gama RJ / Chapecoense SC | 65.0 | 1 % | 1 % | -0.38 |
| Descanso/final: Vasco da Gama RJ / Empate | 18.0 | 4 % | 4 % | -0.23 |
| Descanso/final: Vasco da Gama RJ / Vasco da Gama RJ | 2.02 | 46 % | 46 % | -0.07 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.28 | 76 % | 76 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 3.6 | 24 % | 24 % | -0.12 |
| Goles 1.er tiempo Más 0.75 | 1.37 | 71 % | 71 % | -0.03 |
| Goles 1.er tiempo Menos 0.75 | 3.15 | 30 % | 29 % | -0.06 |
| Goles 1.er tiempo Más 1.0 | 1.52 | 64 % | 64 % | -0.03 |
| Goles 1.er tiempo Menos 1.0 | 2.55 | 38 % | 37 % | -0.03 |
| Goles 1.er tiempo Más 1.25 | 1.88 | 50 % | 51 % | -0.05 |
| Goles 1.er tiempo Menos 1.25 | 1.93 | 50 % | 50 % | -0.03 |
| Goles 1.er tiempo Más 1.5 | 2.22 | 41 % | 42 % | -0.08 |
| Goles 1.er tiempo Menos 1.5 | 1.65 | 59 % | 58 % | -0.03 |
| Goles 1.er tiempo Más 1.75 | 2.72 | 34 % | 34 % | -0.09 |
| Goles 1.er tiempo Menos 1.75 | 1.47 | 67 % | 66 % | -0.02 |
| Goles 1.er tiempo Más 2.5 | 4.65 | 17 % | 17 % | -0.22 |
| Goles 1.er tiempo Menos 2.5 | 1.18 | 83 % | 83 % | -0.02 |
| Goles 1.er tiempo Más 3.5 | 9.5 | 6 % | 6 % | -0.48 |
| Goles 1.er tiempo Menos 3.5 | 1.05 | 94 % | 94 % | -0.01 |
| Goles 2.º tiempo Más 0.5 | 1.2 | 81 % | 81 % | -0.03 |
| Goles 2.º tiempo Menos 0.5 | 4.35 | 19 % | 19 % | -0.18 |
| Goles 2.º tiempo Más 1.5 | 1.91 | 49 % | 49 % | -0.06 |
| Goles 2.º tiempo Menos 1.5 | 1.87 | 51 % | 51 % | -0.05 |
| Goles 2.º tiempo Más 2.5 | 3.7 | 23 % | 23 % | -0.15 |
| Goles 2.º tiempo Menos 2.5 | 1.27 | 77 % | 77 % | -0.02 |

**Goles, esperado ficha:** local 1.36, visitante 1.86, total 3.21 (modelo: λ local 0.87, visitante 2.22). Muestra local 7, visitante 7, directos 3.

**Líneas de goles que cumplen 5 de 7 en ambos (11):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 2.5 | 1.05 | 1.36 | 1.14 | 7 de 7 | 5 de 7 | 3 de 3 | 94 % | 87 % | 94 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.04 | 3.21 | 2.71 | 7 de 7 | 7 de 7 | 1 de 3 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 1.5 | 1.2 | 3.21 | 1.71 | 6 de 7 | 5 de 7 | 1 de 3 | 82 % | 75 % | 82 % | -0.02 | -0.11 | PROTECCIÓN |
| total | Más 2.25 | 1.45 | 3.21 | 0.96 | 5 de 7 | 5 de 7 | 0 de 3 | 67 % | 60 % | 67 % | -0.03 | -0.13 | PROTECCIÓN |
| total | Más 2.5 | 1.62 | 3.21 | 0.71 | 5 de 7 | 5 de 7 | 0 de 3 | 59 % | 52 % | 60 % | -0.04 | -0.16 |  |
| total | Menos 4.5 | 1.22 | 3.21 | 1.29 | 6 de 7 | 5 de 7 | 3 de 3 | 81 % | 74 % | 80 % | -0.02 | -0.10 | PROTECCIÓN |
| total | Menos 5.5 | 1.09 | 3.21 | 2.29 | 7 de 7 | 7 de 7 | 3 de 3 | 91 % | 84 % | 91 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Menos 6.5 | 1.03 | 3.21 | 3.29 | 7 de 7 | 7 de 7 | 3 de 3 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Más 0.5 | 1.1 | 1.86 | 1.36 | 7 de 7 | 5 de 7 | 1 de 3 | 90 % | 83 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.19 | 1.86 | 1.64 | 5 de 7 | 7 de 7 | 3 de 3 | 83 % | 76 % | 82 % | -0.02 | -0.10 | PROTECCIÓN |
| visitante | Menos 4.5 | 1.06 | 1.86 | 2.64 | 7 de 7 | 7 de 7 | 3 de 3 | 93 % | 86 % | 93 % | -0.01 | -0.08 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (69 %) en línea con el mercado; total esperado ficha 3.21 vs modelo 3.08. Mejor línea con cuota ≥ 1,30 que cumple: total Más 2.25 @1.45 (p 67 %, aj. 60 %).


---

## 20:00 · Jamaica - México (CONCACAF Nations League Play-offs)

Competición/contexto: importancia «normal»; tabla: sin dato; bajas: ninguna anotada; clima: 25.4 °C al inicio, humedad 94 %, prob. de lluvia máx. 11 %, lluvia máx. 0.1 mm/h, viento máx. 2.3 km/h (código OMM al inicio 3) · Open-Meteo, pronóstico del 13-nov, ciudad del estadio.

**1X2** (modelo vs mercado sin margen; EV = p·cuota − 1):

| Selección | Cuota | p modelo | p mercado | dif (pts) | EV |
|---|---|---|---|---|---|
| Gana Jamaica | 6.2 | 14 % | 15 % | -0.5 | -0.13 |
| Empate | 4.0 | 23 % | 23 % | +0.1 | -0.07 |
| Gana México | 1.57 | 63 % | 62 % | +0.4 | -0.02 |

Favorito del modelo: **visitante** (63 %). Alertas: ninguna. Alertas en goles/resultado/ambos: no.

Regularidad «ganó / no perdió / ambos marcan» (últimos 7 y 7, cualquier sede): local ganó 3 de 7, no perdió 5 de 7, perdió 2 de 7; visitante ganó 6 de 7, no perdió 6 de 7, perdió 1 de 7. Directos (n=5) con ambos marcan: 3 de 5. _Esta regularidad la calculé yo desde `series.g` de la ficha (la ficha no la trae hecha)._

Cumple (definición mía, no está en la ficha): Gana local = local ganó ≥5 y visitante perdió ≥5; 1X = local no perdió ≥5 y visitante perdió ≥5 de 7 [no ganó]; análogo para visitante.

- Gana local: L ganó 3 de 7 · V perdió 1 de 7 → no
- Gana visitante: V ganó 6 de 7 · L perdió 2 de 7 → no
- Local o empate: L no perdió 5 de 7 · V no ganó 1 de 7 → no
- Visitante o empate: V no perdió 6 de 7 · L no ganó 4 de 7 → no

**Doble oportunidad / no hay empate:**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Jamaica o empate | 2.47 | 37 % | 38 % | -0.08 |
| México o empate | 1.15 | 86 % | 85 % | -0.01 |
| No hay empate | 1.23 | 77 % | 77 % | -0.06 |

**Ambos marcan** (L ambos marcan 2 de 7, V 2 de 7, directos 3 de 5):

| Selección | Cuota | p modelo | p mercado | EV | regularidad |
|---|---|---|---|---|---|
| Ambos marcan: Sí | 2.07 | 46 % | 45 % | -0.06 | L 2 de 7 · V 2 de 7 → no |
| Ambos marcan: No | 1.7 | 54 % | 55 % | -0.08 | L 5 de 7 · V 5 de 7 → sí |

**Descanso/final y 1T/2T (solo modelo y mercado, sin regularidad: no hay goles por tiempo en la muestra):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| 1.er tiempo: Jamaica | 6.0 | 14 % | 14 % | -0.18 |
| 1.er tiempo: Empate | 2.27 | 41 % | 41 % | -0.07 |
| 1.er tiempo: México | 2.07 | 45 % | 45 % | -0.06 |
| 2.º tiempo: Jamaica | 5.5 | 15 % | 15 % | -0.16 |
| 2.º tiempo: Empate | 2.5 | 36 % | 36 % | -0.09 |
| 2.º tiempo: México | 1.93 | 48 % | 48 % | -0.07 |
| Descanso o final: Jamaica | 3.8 | 22 % | 25 % | -0.15 |
| Descanso o final: Empate | 1.85 | 50 % | 51 % | -0.08 |
| Descanso o final: México | 1.4 | 68 % | 67 % | -0.05 |
| Descanso/final: Jamaica / Jamaica | 10.0 | 7 % | 8 % | -0.28 |
| Descanso/final: Jamaica / Empate | 18.5 | 4 % | 4 % | -0.28 |
| Descanso/final: Jamaica / México | 28.0 | 3 % | 2 % | -0.29 |
| Descanso/final: Empate / Jamaica | 12.5 | 6 % | 6 % | -0.26 |
| Descanso/final: Empate / Empate | 5.5 | 15 % | 15 % | -0.18 |
| Descanso/final: Empate / México | 4.3 | 20 % | 20 % | -0.14 |
| Descanso/final: México / Jamaica | 70.0 | 1 % | 1 % | -0.36 |
| Descanso/final: México / Empate | 17.5 | 4 % | 4 % | -0.23 |
| Descanso/final: México / México | 2.27 | 40 % | 40 % | -0.09 |

**Goles 1T/2T (solo modelo y mercado):**

| Selección | Cuota | p modelo | p mercado | EV |
|---|---|---|---|---|
| Goles 1.er tiempo Más 0.5 | 1.4 | 69 % | 69 % | -0.03 |
| Goles 1.er tiempo Menos 0.5 | 2.92 | 31 % | 31 % | -0.10 |
| Goles 1.er tiempo Más 0.75 | 1.55 | 63 % | 63 % | -0.03 |
| Goles 1.er tiempo Menos 0.75 | 2.47 | 38 % | 38 % | -0.05 |
| Goles 1.er tiempo Más 1.0 | 1.83 | 53 % | 53 % | -0.04 |
| Goles 1.er tiempo Menos 1.0 | 1.98 | 49 % | 49 % | -0.03 |
| Goles 1.er tiempo Más 1.25 | 2.32 | 41 % | 41 % | -0.06 |
| Goles 1.er tiempo Menos 1.25 | 1.62 | 60 % | 60 % | -0.02 |
| Goles 1.er tiempo Más 1.5 | 2.72 | 33 % | 33 % | -0.11 |
| Goles 1.er tiempo Menos 1.5 | 1.44 | 67 % | 67 % | -0.03 |
| Goles 1.er tiempo Más 2.5 | 6.2 | 11 % | 12 % | -0.29 |
| Goles 1.er tiempo Menos 2.5 | 1.11 | 89 % | 88 % | -0.02 |
| Goles 2.º tiempo Más 0.5 | 1.3 | 75 % | 75 % | -0.02 |
| Goles 2.º tiempo Menos 0.5 | 3.45 | 25 % | 25 % | -0.14 |
| Goles 2.º tiempo Más 1.5 | 2.3 | 40 % | 40 % | -0.07 |
| Goles 2.º tiempo Menos 1.5 | 1.6 | 60 % | 60 % | -0.04 |
| Goles 2.º tiempo Más 2.5 | 4.9 | 16 % | 16 % | -0.20 |
| Goles 2.º tiempo Menos 2.5 | 1.17 | 84 % | 84 % | -0.02 |

**Goles, esperado ficha:** local 0.79, visitante 1.29, total 2.07 (modelo: λ local 0.75, visitante 1.80). Muestra local 7, visitante 7, directos 5.

**Líneas de goles que cumplen 5 de 7 en ambos (8):** p aj. = p − 7 pts; PROT = cuota < 1,50.

| Ámbito | Línea | Cuota | Esperado | Colchón | L | V | Directos | p modelo | p aj. | p mercado | EV | EV aj. | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local | Menos 1.5 | 1.18 | 0.79 | 0.71 | 5 de 7 | 6 de 7 | 4 de 5 | 83 % | 76 % | 83 % | -0.03 | -0.11 | PROTECCIÓN |
| local | Menos 2.5 | 1.03 | 0.79 | 1.71 | 6 de 7 | 6 de 7 | 5 de 5 | 96 % | 89 % | 96 % | -0.01 | -0.08 | PROTECCIÓN |
| total | Más 0.5 | 1.07 | 2.07 | 1.57 | 6 de 7 | 7 de 7 | 5 de 5 | 92 % | 85 % | 92 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 3.5 | 1.31 | 2.07 | 1.43 | 6 de 7 | 6 de 7 | 4 de 5 | 75 % | 68 % | 74 % | -0.02 | -0.11 | PROTECCIÓN |
| total | Menos 4.5 | 1.11 | 2.07 | 2.43 | 6 de 7 | 6 de 7 | 5 de 5 | 89 % | 82 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |
| total | Menos 5.5 | 1.04 | 2.07 | 3.43 | 7 de 7 | 7 de 7 | 5 de 5 | 95 % | 88 % | 95 % | -0.01 | -0.08 | PROTECCIÓN |
| visitante | Menos 2.5 | 1.32 | 1.29 | 1.21 | 7 de 7 | 6 de 7 | 4 de 5 | 74 % | 66 % | 73 % | -0.03 | -0.12 | PROTECCIÓN |
| visitante | Menos 3.5 | 1.1 | 1.29 | 2.21 | 7 de 7 | 7 de 7 | 5 de 5 | 90 % | 83 % | 89 % | -0.01 | -0.09 | PROTECCIÓN |

**Lectura:** el modelo da visitante favorito (63 %) en línea con el mercado; total esperado ficha 2.07 vs modelo 2.55. Mejor línea con cuota ≥ 1,30 que cumple: total Menos 3.5 @1.31 (p 75 %, aj. 68 %).


---

## Resumen de la jornada

| Hora | Partido | Local | Empate | Visitante | Alertas (n) | En goles/resultado |
|---|---|---|---|---|---|---|
| 05:15 | Japón - Brasil | 22 % | 25 % | 53 % | 0 | no |
| 08:00 | Real Valladolid - CD Castellón | 30 % | 27 % | 43 % | 0 | no |
| 09:00 | Kosovo - Israel | 54 % | 26 % | 20 % | 0 | no |
| 10:15 | Real Sociedad II - Sporting de Gijón | 38 % | 29 % | 33 % | 0 | no |
| 12:00 | Georgia - Hungría | 31 % | 31 % | 38 % | 0 | no |
| 12:00 | Noruega - Gales | 81 % | 13 % | 6 % | 1 | no |
| 12:30 | RCD Mallorca - Cordoba CF | 49 % | 25 % | 25 % | 0 | no |
| 12:30 | UD Almeria - FC Andorra | 60 % | 23 % | 17 % | 1 | no |
| 14:45 | Irlanda del Norte - Ucrania | 38 % | 32 % | 30 % | 0 | no |
| 14:45 | Portugal - Dinamarca | 64 % | 21 % | 15 % | 1 | no |
| 14:45 | Rumanía - Polonia | 22 % | 26 % | 52 % | 0 | no |
| 14:45 | Suecia - Bosnia y Herzegovina | 64 % | 22 % | 14 % | 4 | no |
| 15:30 | Aguilas Doradas - Independiente Medellín | 39 % | 28 % | 33 % | 0 | no |
| 15:30 | Atletico Nacional - Once Caldas | 37 % | 28 % | 35 % | 2 | no |
| 15:30 | Deportivo Cali - Deportes Tolima | 41 % | 30 % | 29 % | 0 | no |
| 15:30 | Millonarios FC - Alianza FC | 75 % | 17 % | 7 % | 3 | no |
| 16:30 | Mirassol SP - Clube Atletico MG | 49 % | 27 % | 24 % | 0 | no |
| 17:00 | CA Banfield - Boca Juniors | 12 % | 24 % | 64 % | 0 | no |
| 18:00 | Queretaro FC - CF Monterrey | 26 % | 25 % | 49 % | 0 | no |
| 18:30 | Chapecoense SC - Vasco da Gama RJ | 11 % | 20 % | 69 % | 2 | no |
| 20:00 | Jamaica - México | 14 % | 23 % | 63 % | 0 | no |

### 10 mejores líneas de goles (cumplen 5 de 7 en ambos, cuota ≥ 1,30) por p_modelo

| # | Partido | Hora | Línea | Cuota | p modelo | p aj. | L | V | Directos |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Suecia - Bosnia y Herzegovina | 14:45 | visitante Menos 1.5 | 1.3 | 75 % | 68 % | 5 de 7 | 5 de 7 | 1 de 1 |
| 2 | Jamaica - México | 20:00 | total Menos 3.5 | 1.31 | 75 % | 68 % | 6 de 7 | 6 de 7 | 4 de 5 |
| 3 | Kosovo - Israel | 09:00 | visitante Menos 1.5 | 1.31 | 75 % | 68 % | 5 de 7 | 6 de 7 | 3 de 3 |
| 4 | Queretaro FC - CF Monterrey | 18:00 | local Más 0.5 | 1.31 | 74 % | 67 % | 5 de 7 | 7 de 7 | 3 de 6 |
| 5 | RCD Mallorca - Cordoba CF | 12:30 | visitante Más 0.5 | 1.31 | 74 % | 67 % | 5 de 7 | 7 de 7 |  |
| 6 | Noruega - Gales | 12:00 | total Menos 4.5 | 1.36 | 74 % | 67 % | 6 de 7 | 6 de 7 | 1 de 1 |
| 7 | Jamaica - México | 20:00 | visitante Menos 2.5 | 1.32 | 74 % | 66 % | 7 de 7 | 6 de 7 | 4 de 5 |
| 8 | Irlanda del Norte - Ucrania | 14:45 | visitante Menos 1.5 | 1.32 | 73 % | 66 % | 6 de 7 | 6 de 7 | 1 de 1 |
| 9 | Georgia - Hungría | 12:00 | local Menos 1.5 | 1.33 | 73 % | 66 % | 7 de 7 | 5 de 7 | 1 de 1 |
| 10 | Aguilas Doradas - Independiente Medellín | 15:30 | total Menos 3.5 | 1.33 | 73 % | 66 % | 6 de 7 | 5 de 7 | 6 de 6 |

## Límites
- Muestra de 7 por equipo (no 10) y directos de 0 a 6; con n tan chico, 5 de 7 es una señal débil y las líneas del mismo partido (Menos 3.5/4.5/5.5, por equipo y total) están muy correlacionadas entre sí.
- La p_modelo está anclada al mercado (p_modelo ≈ p_mercado en casi todas las filas), así que EV ≈ −margen; el modelo no aporta una opinión independiente en goles. Calibración real del 12 y 13-nov: sobreestima 6–8 pts (por eso la columna p aj.).
- Ninguna alerta del modelo cae sobre goles, resultado o ambos marcan; las alertas son de córners/saques de banda. La columna `alerta_modelo` del CSV está vacía incluso donde el informe trae alertas.
- 1T/2T y descanso/final: solo modelo y mercado; sin goles por tiempo en la muestra no hay regularidad.
- «Cumple» de 1X2, doble oportunidad y ambos marcan: la ficha no trae esa regularidad; la calculé desde `series.g` (goles a favor/en contra de los 7 partidos de cada equipo) con una definición propia (ver arriba). Es lectura, no criterio validado.
- No leí JSON crudos de flashscore/ ni betano/. Alineaciones probables (no oficiales); clima = pronóstico del 13-nov. Sin alineación de 5 partidos (Banfield–Boca y los 4 de Colombia) ni tabla en Japón–Brasil, Banfield–Boca, Jamaica–México.
- Competición: Japón–Brasil amistoso (rotación y motivación impredecibles); Banfield–Boca semifinal de Copa Argentina en sede neutral (si hay empate a los 90 min, puede haber prórroga/penales: «resultado» a 90 min); Jamaica–México cuartos de Concacaf NL (ida/vuelta sin verificar, afecta el incentivo).
- Los directos que dice el CSV vienen de la ficha (`h2h`) con su n; con n=1 o 2 no pesan.
