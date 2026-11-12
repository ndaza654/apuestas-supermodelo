# Informe final · jornada 2026-11-13 (Betano.co)

Cuotas leídas el 12-nov ~12:32 Bogotá; alineaciones probables (Flashscore) ~13:00; historial por jugador ~14:30. Horas en Bogotá. Todas las cifras salen de `fichas/ficha_<partido>.md/.json`, `informes/` y `ranking.md` de esta carpeta; ningún dato se rellenó con supuestos.

## Enfoque de mercados

**Qué pesa en esta jornada y por qué**

- **Córners son el mercado central.** Es el único que Betano ofrece en los 11 partidos con líneas suficientes y con muestra de 7+7 completa. En 8 de los 11 partidos es lo único analizable por regularidad (más goles/resultado, que no se usan como señal; ver advertencia).
- **Estadísticas de partido** (faltas, fueras de juego, saques, remates, tiros al arco): Betano solo las ofrece en **Países Bajos–Grecia, Serbia–Alemania y Escocia–Macedonia**. En los otros 8 no existen, así que no se analizan.
- **Jugadores:** solo cuentan los **4 partidos con alineación probable** (Países Bajos–Grecia, Serbia–Alemania, Escocia–Macedonia, Eslovenia–Suiza). Binks (Escocia) es baja. En Eslovenia–Suiza Betano solo ofrece anota/asiste/anota_o_asiste/tarjeta (sin escaleras de remates ni entradas).
- **Enfoque del modelo por contexto** (informes): Países Bajos–Grecia y Serbia–Alemania favorecen goles, remates/tiros al arco del favorito y córners del favorito; Escocia–Macedonia favorece goles y remates de Escocia; Luxemburgo–Estonia y Moldavia–Kazajistán (parejos y cerrados) apuntan a pocos goles y 1T; Bulgaria–Islandia y Eslovenia–Suiza: «ningún mercado destaca por contexto». Esto es orientación, no cambia la regularidad.
- **Internacional de Bogotá–Santa Fe: no apto** (situación 12: Santa Fe ya clasificado, Inter fuera de los ocho). Sin informe del modelo, no se analiza.

**Advertencias que aplican a todo el informe**

1. **Alertas del modelo.** Todos los informes traen alertas «la simulación sin contexto se aleja 17–48 pts del mercado» (8–35 por partido; las más numerosas: Eslovenia–Suiza 35, Liechtenstein–Azerbaiyán 17, Serbia–Alemania 15). Aparecen en favoritos claros (Escocia, Serbia–Alemania, Liechtenstein, Eslovaquia) y también en partidos parejos o de favorito leve (Eslovenia–Suiza). **No se usa ninguna línea de goles ni de resultado de ningún partido como señal.** Las líneas de este informe son de córners, estadísticas y jugadores, medidas por regularidad histórica, no por la simulación.
2. **Entradas.** Betano ofrece el **total de entradas**; Flashscore da **«entradas ganadas»**. El historial puede quedar **por debajo** de la cifra real, así que las líneas de entradas (Tsimikas, Nmecha) son lecturas con sesgo a la baja en el historial.
3. **«Cumple»** = ≥5 de 7 en **ambos** equipos (n mínimo 5). El colchón es solo informativo; ninguna línea se excluye por él. La regularidad no es una probabilidad calibrada: 6 de 7 con 7 partidos no equivale a ~86 %.
4. **Directos** (H2H): entre 1 y 3 por partido, nunca llegan a n≥5; informan, no deciden.
5. **Cuotas con casi un día de antigüedad.** Relee antes de apostar, sobre todo Moldavia–Kazajistán (12:00 Bogotá).

Notación: L/V = local/visitante (a favor del equipo; en el tramo V de una línea de local es lo que el visitante concede); D = directos; col = colchón (esperado − línea para Más, línea − esperado para Menos).

---

## Partidos con estadísticas de partido y jugadores

### 1. Países Bajos – Grecia · 14:45 · árbitro Saggi R. (sin estadística de árbitro)
Esperado córners: PB 5.79 / GRE 4.64 / total 10.43.

**Córners que cumplen con cuota ≥ 1.20**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 6.5 | 1.20 | 10.43 | +3.9 | 7 de 7 | 6 de 7 | 3 de 3 |
| total | Más 7.5 | 1.38 | 10.43 | +2.9 | 5 de 7 | 6 de 7 | 3 de 3 |
| visitante (GRE) | Más 2.5 | 1.45 | 4.64 | +2.1 | 6 de 7 | 5 de 7 | 2 de 3 |
| visitante (GRE) | Más 3.5 | 2.07 | 4.64 | +1.1 | 5 de 7 | 5 de 7 | 1 de 3 |

Otras 10 líneas de córners cumplen pero con cuota 1.03–1.15 (p. ej. total Más 4.5 @1.04, local Menos 8.5 @1.13): regularidad alta, pero sin valor práctico; están en la ficha.

**Estadísticas de partido que cumplen**

| Mercado | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Fueras de juego | PB Más 1.5 | 1.70 | 2.21 | +0.7 | 5 de 7 | 5 de 7 | 1 de 3 |
| Saques de banda | total Más 32.5 | 1.91 | 35.43 | +2.9 | 5 de 7 | 5 de 7 | 1 de 1 |
| Saques de banda | GRE Más 14.5 | 1.75 | 17.0 | +2.5 | 5 de 7 | 5 de 7 | 1 de 1 |
| Tiros al arco | PB Menos 7.5 | 1.42 | 5.64 | +1.9 | 5 de 7 | 6 de 7 | 3 de 3 |
| Tiros al arco | GRE Más 1.5 | 1.24 | 4.71 | +3.2 | 7 de 7 | 6 de 7 | 2 de 3 |
| Tiros al arco | GRE Más 2.5 | 1.72 | 4.71 | +2.2 | 6 de 7 | 5 de 7 | 1 de 3 |

**Jugadores** (XI probable, titular p 0.90, 80 min esperados)

| Jugador | Mercado | Línea | Esperado | Col | X de n |
|---|---|---|---|---|---|
| Konstantinos Mavropanos (GRE) | Remates | 1+ @1.40 | 1.46 | +1.0 | 5 de 5 |
| Denzel Dumfries (PB) | Remates | 1+ @1.27 | 1.11 | +0.6 | 5 de 7 |
| Konstantinos Karetsas (GRE) | Remates | 1+ @1.20 | 1.59 | +1.1 | 5 de 7 |
| Konstantinos Tsimikas (GRE) | Entradas | 1+ @1.12 | 1.40 | +0.9 | 6 de 7 |

Ningún escalón 2+ cumple (Tsimikas entradas 2+ 4 de 7). Tsimikas: cuota baja y entradas ganadas (ver advertencia 2). Mavropanos solo tiene n = 5 y parte de su historial es de oct-2025.

**No cumple (resumen):** faltas (3 líneas), los 9 de remates, fueras de juego total 3.5 y GRE Más 1.5, saques de banda local 17.5, tiros al arco total Más 8.5, local Más 5.5 / Menos 6.5, GRE Más 3.5; córners total Más 8.5/9.5 (5 y 4) y Menos 11.5/12.5 (4 y 4). Saques de meta: n = 4, sin ficha. Goles anota/asiste/tarjeta de jugadores: ninguna cumple (Gakpo anota 3 de 5).

### 2. Serbia – Alemania · 14:45 · árbitro Alberola J.
Esperado córners: SRB 4.79 / ALE 6.21 / total 11.0. Directos: 1.

**Córners que cumplen con cuota ≥ 1.20**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 7.5 | 1.34 | 11.0 | +3.5 | 6 de 7 | 5 de 7 | 1 de 1 |
| total | Más 8.5 | 1.60 | 11.0 | +2.5 | 5 de 7 | 5 de 7 | 1 de 1 |
| total | Más 9.5 | 2.02 | 11.0 | +1.5 | 5 de 7 | 5 de 7 | 1 de 1 |
| local (SRB) | Más 1.5 | 1.20 | 4.79 | +3.3 | 6 de 7 | 6 de 7 | 0 de 1 |

Otras 12 con cuota 1.03–1.19 (p. ej. total Más 4.5 @1.03). Total Menos 11.5/12.5 no cumple (5 y 4).

**Estadísticas de partido que cumplen**

| Mercado | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Faltas | SRB Menos 11.5 | 2.05 | 10.57 | +0.9 | 5 de 7 | 5 de 7 | 1 de 1 |
| Remates | SRB Más 6.5 | 1.40 | 10.07 | +3.6 | 6 de 7 | 5 de 7 | 0 de 1 |
| Tiros al arco | SRB Más 1.5 | 1.30 | 3.5 | +2.0 | 5 de 7 | 5 de 7 | 0 de 1 |
| Tiros al arco | total Menos 11.5 | 1.53 | 9.14 | +2.4 | 5 de 7 | 6 de 7 | 1 de 1 |
| Tiros al arco | ALE Menos 8.5 | 1.60 | 5.64 | +2.9 | 6 de 7 | 7 de 7 | 1 de 1 |

El directo de remates fue 1 a 32 (extremo) y el de tiros al arco 1 a 8; las dos líneas de Serbia Más fallan en ese directo. Total Menos 11.5 y ALE Menos 8.5 están correlacionadas (mismo guion).

**Jugadores:** solo **Felix Nmecha (ALE) entradas 1+ @1.19**, esperado 2.07, col +1.6, **5 de 5**. Su esperado está inflado por un partido de 5 entradas (20-jun); en los otros cuatro hizo 1, y en tres jugó 45–64 min. Entradas ganadas vs total (advertencia 2). Alemania: 14 de 22 del XI con n < 5.

**No cumple (resumen):** fueras de juego (ninguna), saques de banda (ninguna), remates total y visitante, el resto de tiros al arco, faltas total/visitante. Saques de meta n = 4.

### 3. Escocia – Macedonia del Norte · 14:45 · árbitro Ocenas M.
Esperado córners: ESC 5.57 / MKD 3.57 / total 9.14. Directos: 1. Binks: baja (Flashscore lo trae en XI y en bajas; se tomó como baja). Welsh, McKenna y Shankland también aparecen en bajas.

**Córners:** total Menos 11.5 @1.28, esperado 9.14, col +2.4, L 6 de 7, V 5 de 7, D 1 de 1.

**Estadísticas de partido que cumplen**

| Mercado | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Fueras de juego | ESC Menos 1.5 | 1.90 | 0.93 | +0.6 | 6 de 7 | 6 de 7 | 1 de 1 |
| Fueras de juego | MKD Menos 1.5 | 1.45 | 0.93 | +0.6 | 5 de 7 | 6 de 7 | 1 de 1 |
| Fueras de juego | total Menos 2.5 | 2.07 | 1.86 | +0.6 | 5 de 7 | 6 de 7 | 1 de 1 |
| Remates | ESC Menos 20.5 | 1.82 | 15.79 | +4.7 | 6 de 7 | 5 de 7 | 0 de 1 |
| Remates | ESC Menos 21.5 | 1.57 | 15.79 | +5.7 | 6 de 7 | 5 de 7 | 0 de 1 |
| Remates | total Menos 25.5 | 2.50 | 26.21 | **−0.7** | 5 de 7 | 5 de 7 | 0 de 1 |
| Remates | total Menos 27.5 | 1.83 | 26.21 | +1.3 | 5 de 7 | 5 de 7 | 0 de 1 |
| Remates | total Menos 29.5 | 1.45 | 26.21 | +3.3 | 5 de 7 | 5 de 7 | 0 de 1 |

El directo de remates fue 25 a 9 (34 en total), y falla todas las líneas Menos de remates. El colchón −0.7 de Menos 25.5 se informa; no excluye la línea (regularidad 5 y 5, esperado por encima de la línea).

**Jugadores:** ninguna línea cumple (Bardhi remates 1+ @1.15, 4 de 7, es lo más cercano). Betano no ofrece entradas ni faltas de jugador ni parejas. Gannon-Doak no casó con Betano. 10 jugadores con n < 5 (McTominay 3, Tierney 2).

**No cumple (resumen):** faltas (ninguna), fueras Más, tiros al arco (ninguna), remates Más. Saques de banda y de meta: Betano no ofrece líneas.

---

## Partidos con solo córners (más jugadores en Eslovenia–Suiza)

### 4. Moldavia – Kazajistán · **12:00** · D 3
Esperado: MOL 5.93 / KAZ 6.36 / total 12.29.

| Línea | Cuota | Col | L | V | D |
|---|---|---|---|---|---|
| total Más 6.5 | 1.24 | +5.8 | 7 de 7 | 7 de 7 | 2 de 3 |
| total Más 7.5 | 1.45 | +4.8 | 6 de 7 | 7 de 7 | 2 de 3 |
| total Más 8.5 | 1.82 | +3.8 | 6 de 7 | 7 de 7 | 2 de 3 |
| total Más 9.5 | 2.35 | +2.8 | 5 de 7 | 6 de 7 | 2 de 3 |

No cumple: Más 10.5 (4 y 6), todas las Menos, líneas por equipo.

### 5. Eslovenia – Suiza · 14:45 · D 3
Esperado: ESL 4.07 / SUI 4.36 / total 8.43.

| Línea | Cuota | Col | L | V | D |
|---|---|---|---|---|---|
| total Más 6.5 | 1.26 | +1.9 | 6 de 7 | 5 de 7 | 3 de 3 |
| total Menos 10.5 | 1.29 | +2.1 | 5 de 7 | 6 de 7 | 3 de 3 |
| visitante (SUI) Más 3.5 | 1.26 | +0.9 | 5 de 7 | 5 de 7 | 3 de 3 |

(Local Más 1.5 @1.15, 7 y 6 de 7, queda fuera por cuota < 1.20.) No cumple: total Más 7.5 (4 y 4), Menos 9.5 (5 y 4), SUI Más 4.5.

**Jugadores:** Betano solo ofrece anota/asiste/anota_o_asiste/tarjeta. Cumple **Dan Ndoye (SUI) anota o asiste «Sí» @1.98: 5 de 7** (titular 0.90). Sin esperado ni colchón (no es escalera). Ndoye anota @3.00: 4 de 7 (no cumple). Embolo n = 3, Matko y Athekame n = 4: no pueden cumplir. Urbancic no jugó en la ventana; Gnezda Cerin no casó con Betano.

### 6. Bulgaria – Islandia · 14:45 · D 1
Esperado: BUL 4.07 / ISL 5.5 / total 9.57.

| Línea | Cuota | Col | L | V | D |
|---|---|---|---|---|---|
| total Más 6.5 | 1.22 | +3.1 | 6 de 7 | 6 de 7 | 1 de 1 |
| total Más 7.5 | 1.42 | +2.1 | 6 de 7 | 6 de 7 | 1 de 1 |
| total Más 8.5 | 1.75 | +1.1 | 6 de 7 | 6 de 7 | 1 de 1 |

No cumple: Más 9.5 (4 y 5), Menos 10.5 (4 y 5), líneas por equipo.

### 7. Luxemburgo – Estonia · 14:45 · D 1
Esperado: LUX 3.86 / EST 4.43 / total 8.29.

| Línea | Cuota | Col | L | V | D |
|---|---|---|---|---|---|
| total Más 6.5 | 1.22 | +1.8 | 5 de 7 | 7 de 7 | 1 de 1 |
| total Menos 10.5 | 1.35 | +2.2 | 7 de 7 | 6 de 7 | 1 de 1 |
| visitante (EST) Más 3.5 | 1.60 | +0.9 | 5 de 7 | 5 de 7 | 1 de 1 |

No cumple: total Más 7.5 (4 y 5), Menos 9.5 (6 y 3), LUX Más 4.5.

### 8. Eslovaquia – Islas Feroe · 14:45 · D 1
Esperado: SVK 6.36 / FAR 3.71 / total 10.07.

| Línea | Cuota | Col | L | V | D |
|---|---|---|---|---|---|
| total Más 7.5 | 1.30 | +2.6 | 6 de 7 | 5 de 7 | 1 de 1 |
| total Más 8.5 | 1.55 | +1.6 | 6 de 7 | 5 de 7 | 1 de 1 |

No cumple: Más 9.5 (5 y 4), Menos 11.5 (6 y 3), líneas por equipo.

### 9. Liechtenstein – Azerbaiyán · 14:45 · D 1
Esperado: LIE 2.21 / AZE 6.07 / total 8.29.

| Línea | Cuota | Col | L | V | D |
|---|---|---|---|---|---|
| total Menos 9.5 | 1.67 | +1.2 | 5 de 7 | 5 de 7 | 1 de 1 |
| total Menos 10.5 | 1.39 | +2.2 | 6 de 7 | 6 de 7 | 1 de 1 |

No cumple: Menos 8.5 (4 y 4), todas las Más, líneas por equipo.

### 10. Andorra – Gibraltar · 14:45 · D 1
Esperado: AND 5.71 / GIB 3.5 / total 9.21. **Ninguna línea cumple.** Lo más cercano: Menos 10.5 (6 y 4), Menos 9.5 (5 y 3), Más 6.5 (4 y 7), Gibraltar Más 2.5 (6 y 2). Figura «apto» en el ranking por calidad de datos, no porque haya líneas que cumplan.

### 11. Internacional de Bogotá – Santa Fe · 20:30 · **no apto**
Situación 12 (Santa Fe ya clasificado, posible rotación sin confirmar; Inter fuera de los ocho; descanso ≤ 3 días). Betano ofrece 3 líneas de córners; ninguna cumple. No se analiza más. No se leyó la tabla del descenso, que podría darle motivo a Inter.

---

## Lo que no cumple, resumido

- **Córners:** Andorra–Gibraltar sin ninguna línea; en el resto, las líneas Menos de partidos de muchos córners esperados (Moldavia, Eslovaquia, Serbia–Alemania) y las Más de partidos de pocos (Liechtenstein) no llegan a 5 de 7 en ambos equipos. Las líneas por equipo casi nunca cumplen (solo PB/GRE, SRB y SUI).
- **Estadísticas de partido:** faltas y remates casi no cumplen salvo las listadas; fueras de juego solo en Países Bajos–Grecia y Escocia–Macedonia; saques de meta nunca (n = 4 por equipo).
- **Jugadores:** de unas 1.185 líneas del XI en los 4 partidos solo 6 cumplen, todas en el escalón 1+; 2+ y 3+ fallan. Anota, asiste y tarjeta no cumplen (salvo Ndoye anota_o_asiste). Muchos jugadores tienen n < 5 (p. ej. 14 de 22 en Alemania).
- **Parejas «cualquiera de los jugadores…»:** no las trae la ficha (están en `betano/` y en las tablas del informe del modelo). Las que muestra el informe del modelo tienen EV entre −6 % y −16 % y están marcadas «No». No se analizaron como ficha.

## Límites y fallas

**Datos que faltaron**
- Estadística de árbitro: BeSoccer devuelve 404; solo se tiene el nombre. El mercado de faltas y tarjetas no se apoya en el árbitro.
- Alineaciones: solo 4 de 11 partidos tenían alineación publicada. En los otros 7 no hay mercados de jugadores filtrados. Las alineaciones son **probables** (una fuente, Flashscore), no confirmadas, y se leyeron ~28 min después que las cuotas.
- 1T/2T: Betano ofrece líneas de córners y de otras estadísticas por tiempo, pero no hay estadística por tiempo en la muestra, así que no hay ficha de 1T/2T.
- Saques de meta: n = 4 por equipo, bajo el mínimo de 5.
- Escocia–Macedonia: Betano no ofrece líneas de saques de banda ni de meta.
- Directos (H2H): 1 a 3 por partido; en la ficha de córners no están etiquetados con fecha ni rival, y no se comprobó partido a partido que estén orientados local/visitante (afectaría a las líneas por equipo, no a los totales).
- Descanso, clima, estilo y tabla del descenso colombiano: sin leer. `estilo`, `perfil_corners` y `clima` están vacíos en las fichas.
- Jugadores sin casar o sin historial: Gannon-Doak (Escocia) y Gnezda Cerin (Eslovenia) sin casar con Betano; Urbancic sin partidos en la ventana. Historial de algunos jugadores incluye partidos de 2025 (Karetsas, Mavropanos, Tsimikas), por lo que no coincide estrictamente con «últimos 7 de la selección».

**Fallas e incoherencias detectadas en el repo (sin corregir)**
- `ranking.md` / `ranking.json` cuenta «jugadores que cumplen» solo con escaleras de remates y tiros al arco (`recoleccion/puntuar.py`, ~línea 137). Por eso muestra Serbia–Alemania 0 (la ficha trae Nmecha entradas), Eslovenia–Suiza «no lo ofrece» (la ficha trae Ndoye; Betano sí ofrece anota/asiste/tarjeta) y Países Bajos–Grecia 3 (la ficha trae 4: omite Tsimikas).
- `ficha.bajas` está vacío en las 4 fichas con alineación aunque Flashscore trae bajas con nombre; el contexto dice «Bajas: ninguna anotada». En Serbia–Alemania, Stanković, Maksimović, Lukić, S. Pavlović y Anton aparecen en el JSON con titular 0.0 y `sin_historial`: hay que filtrarlos.
- El «Resumen» de cada ficha omite las líneas con cuota < 1.20 (lo declara su encabezado), y se titula «líneas de equipo» aunque mezcla totales.
- Contexto con valores inconsistentes en las notas: Países Bajos–Grecia con `necesita_ganar: False` en ambos pese a ser «choque directo por la cima» (8 pts cada uno); Eslovaquia–Feroe con local motivación alta y sin necesidad de ganar y visitante al revés; Macedonia «motivación baja». Afecta al puntaje de situación, no a las estadísticas.
- ESTADO.md dice que en 8 partidos Betano ofrece solo córners y goles/resultado; el informe de jugadores indica que en Eslovenia–Suiza hay además mercados de jugador (anota, asiste, anota_o_asiste, tarjeta).
- Alertas del modelo de 17–48 pts en todos los informes (ver advertencia 1): no se investigó su causa.
- Colchón negativo: Escocia–Macedonia remates total Menos 25.5 (−0.7); se informa y no se excluye.

**Pruebas (13-nov):** `test_modelo` 106 superadas · `test_ficha` 14 · `test_betano` 11 · `test_recoleccion` 15. Las cifras del informe se contrastaron con las fichas (Serbia–Alemania tiros al arco, Escocia–Macedonia remates y fueras de juego, Moldavia córners, Ndoye, Tsimikas y Mavropanos); el resto lo recalcularon los agentes desde `series` del JSON sin diferencias.
