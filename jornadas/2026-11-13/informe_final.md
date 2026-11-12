# Informe final · jornada 2026-11-13 (Betano.co) — versión con los 7 agentes

Cuotas leídas el 12-nov ~12:32 Bogotá; alineaciones probables (Flashscore) ~13:00; historial por jugador ~14:30. Informe regenerado el 12-nov ~16:00 Bogotá con los agentes `corners`, `partido`, `jugadores`, `goles-resultado`, `tarjetas` y `combinadas`. Horas en Bogotá. Las tablas por línea salen directo de `fichas/ficha_<partido>.json`; el detalle completo de cada agente (todas las líneas, también las que no cumplen) está en `agentes/<partido>_<agente>.md`. Ningún dato se rellenó con supuestos. **Cuotas con casi un día de antigüedad: relee antes de apostar.**

## Enfoque de mercados

**Qué pesa en esta jornada y por qué**

- **Córners son el mercado central:** Betano los ofrece en los 11 partidos y la muestra 7+7 está completa. 26 líneas cumplen (cuota ≥ 1.20) en 9 de los 10 partidos aptos; Andorra–Gibraltar no tiene ninguna.
- **Goles:** Betano los ofrece en los 11. Cumplen líneas en 8 de 10; no cumple ninguna en Liechtenstein–Azerbaiyán ni en Andorra–Gibraltar. Son lecturas de regularidad (≥ 5 de 7), no de valor: el modelo toma sus goles esperados de las cuotas de Betano, así que su probabilidad no es una segunda opinión.
- **Tarjetas:** hay líneas que cumplen en 7 de 10 partidos; Liechtenstein–Azerbaiyán, Luxemburgo–Estonia y Moldavia–Kazajistán no tienen ninguna con cuota ≥ 1.20. Límite fuerte: Betano cuenta en puntos y la fuente solo trae amarillas.
- **Estadísticas de partido** (faltas, fueras de juego, saques, remates, tiros al arco): Betano solo las ofrece en **Países Bajos–Grecia, Serbia–Alemania y Escocia–Macedonia**. En los otros 8 no existen, así que no se analizan.
- **Jugadores:** solo cuentan los **4 partidos con alineación probable** (Países Bajos–Grecia, Serbia–Alemania, Escocia–Macedonia, Eslovenia–Suiza). Cumplen 6 líneas en total y ninguna pareja. Los otros 7 partidos no tienen alineación: sin mercados de jugadores (regla 1).
- **Enfoque del modelo por contexto** (informes): Países Bajos–Grecia y Serbia–Alemania favorecen goles, remates/tiros al arco del favorito y córners del favorito; Escocia–Macedonia favorece goles y remates de Escocia; Luxemburgo–Estonia y Moldavia–Kazajistán (parejos y cerrados) apuntan a pocos goles y 1T; Bulgaria–Islandia y Eslovenia–Suiza: «ningún mercado destaca por contexto». Es orientación, no cambia la regularidad.
- **Internacional de Bogotá–Santa Fe: no apto** (situación 12: Santa Fe ya clasificado, Inter fuera de los ocho). No se analiza.

**Advertencias que aplican a todo el informe**

1. **Alertas del modelo (corregido respecto a la versión anterior).** Cada informe trae 2–9 alertas «la simulación sin contexto se aleja 15–53 pts del mercado». Revisadas línea por línea, caen en líneas de córners, tarjetas, «ambos con N tarjetas», saques de banda y «más … que»; **ninguna línea de goles, resultado o ambos marcan lleva alerta** (en esas 610 líneas la simulación se aleja del mercado 4 pts como máximo). Por eso las probabilidades del modelo de tarjetas y córners no son fiables, y las de goles/resultado coinciden con el mercado porque salen de él: no aportan señal independiente. Las líneas de este informe se miden por regularidad histórica.
2. **Entradas.** Betano ofrece el total; Flashscore solo «entradas ganadas». El historial queda a la baja (Tsimikas, Nmecha).
3. **Tarjetas.** Betano cuenta en puntos (amarilla 1, roja 2); Flashscore solo trae amarillas. La serie queda por debajo si hubo rojas, sobre todo en líneas ajustadas y en los «Menos» altos.
4. **«Cumple»** = ≥ 5 de 7 en **ambos** equipos (n mínimo 5; jugadores ≥ 5 de ≤ 7 jugados). El colchón es solo informativo y ninguna línea se excluye por él. La regularidad no es una probabilidad calibrada: 6 de 7 no equivale a ~86 %. Las líneas de goles asiáticas (.25/.75) cuentan solo la victoria completa.
5. **Directos** (H2H): 1 a 3 por partido, nunca llegan a n ≥ 5; informan, no deciden.
6. **Muestra de rivales muy desiguales** (selecciones grandes contra pequeñas): varios «Menos» del equipo fuerte cumplen por cuota baja y esperado bajo, no por valor. En **Serbia–Alemania** el esperado de goles de la ficha (2.43) queda muy por debajo del que implica Betano (3.51): los «Menos» de goles cumplen por historial mientras el mercado espera más goles; las dos lecturas cuentan historias distintas.

Notación: L/V = veces que se cumplió la línea en los últimos 7 del local/visitante (en una línea de equipo, V es lo que el visitante concede; el equipo a favor y el rival en contra); D = directos; col = colchón (esperado − línea para Más, línea − esperado para Menos); EV omitido: la ficha no trae una probabilidad calibrada.

---

## Partidos (10 aptos)

### 1. Países Bajos – Grecia · 14:45 · árbitro Saggi R. (sin estadística de árbitro)
Esperado córners: Países Bajos 5.79 / Grecia 4.64 / total 10.43. Directos con estadística: 3.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 6.5 | 1.20 | 10.43 | +3.9 | 7 de 7 | 6 de 7 | 3 de 3 |
| total | Más 7.5 | 1.38 | 10.43 | +2.9 | 5 de 7 | 6 de 7 | 3 de 3 |
| Grecia | Más 2.5 | 1.45 | 4.64 | +2.1 | 6 de 7 | 5 de 7 | 2 de 3 |
| Grecia | Más 3.5 | 2.07 | 4.64 | +1.1 | 5 de 7 | 5 de 7 | 1 de 3 |

_Faltas: ninguna línea cumple con cuota ≥ 1.20._

**Fueras de juego que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Países Bajos | Más 1.5 | 1.70 | 2.21 | +0.7 | 5 de 7 | 5 de 7 | 1 de 3 |

**Saques de banda que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 32.5 | 1.91 | 35.43 | +2.9 | 5 de 7 | 5 de 7 | 1 de 1 |
| Grecia | Más 14.5 | 1.75 | 17.0 | +2.5 | 5 de 7 | 5 de 7 | 1 de 1 |

_Saques de meta: ninguna línea cumple con cuota ≥ 1.20._

_Remates: ninguna línea cumple con cuota ≥ 1.20._

**Tiros al arco que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Países Bajos | Menos 7.5 | 1.42 | 5.64 | +1.9 | 5 de 7 | 6 de 7 | 3 de 3 |
| Grecia | Más 1.5 | 1.24 | 4.71 | +3.2 | 7 de 7 | 6 de 7 | 2 de 3 |
| Grecia | Más 2.5 | 1.72 | 4.71 | +2.2 | 6 de 7 | 5 de 7 | 1 de 3 |

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Países Bajos | Menos 2.5 | 1.45 | 1.71 | +0.8 | 5 de 7 | 6 de 7 | 2 de 3 |
| total | Menos 4.5 | 1.22 | 3.0 | +1.5 | 6 de 7 | 6 de 7 | 3 de 3 |
| Grecia | Más 0.5 | 1.50 | 1.29 | +0.8 | 7 de 7 | 5 de 7 | 1 de 3 |

**Tarjetas que cumplen (cuota ≥ 1.20; serie de amarillas, Betano cuenta puntos)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Países Bajos | Menos 2.5 | 1.37 | 1.2 | +1.3 | 5 de 6 | 5 de 7 | 3 de 3 |
| total | Menos 5.5 | 1.45 | 3.49 | +2.0 | 6 de 6 | 5 de 7 | 1 de 3 |
| total | Menos 6.5 | 1.24 | 3.49 | +3.0 | 6 de 6 | 6 de 7 | 3 de 3 |
| Grecia | Menos 3.5 | 1.39 | 2.29 | +1.2 | 5 de 6 | 5 de 7 | 1 de 3 |
| Grecia | Más 0.5 | 1.50 | 2.29 | +1.8 | 6 de 6 | 7 de 7 | 3 de 3 |

**1X2 modelo vs mercado** (local / empate / visitante, %): 62 / 22 / 16 — Betano sin margen 62 / 22 / 16. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores** (XI probable de Flashscore, leído ~13:00 del 12-nov; titular 0.9, 80 min esperados). Cumplen 4 líneas, todas del escalón 1+:

| Jugador | Mercado | Línea | Esperado | Col | X de n |
|---|---|---|---|---|---|
| Konstantinos Mavropanos (GRE) | Remates | 1+ @1.40 | 1.46 | +1.0 | 5 de 5 |
| Denzel Dumfries (PB) | Remates | 1+ @1.27 | 1.11 | +0.6 | 5 de 7 |
| Konstantinos Karetsas (GRE) | Remates | 1+ @1.20 | 1.59 | +1.1 | 5 de 7 |
| Konstantinos Tsimikas (GRE) | Entradas | 1+ @1.12 | 1.40 | +0.9 | 6 de 7 |

Tsimikas va con cuota < 1.20 y con entradas ganadas (no totales): el historial queda a la baja. Mavropanos tiene n = 5. Casi (4 de n, no cumplen): Reijnders tiros al arco 1+ @1.42 (4 de 6), Tzolis remates 1+ @1.22 (4 de 6), Dumfries faltas 1+ @1.24 (4 de 7).
**Parejas «cualquiera de…» (56 en Betano):** ninguna cumple. Las de equipos distintos van solo como información (independencia, sin corregir dependencia): Gakpo/Tzolis anota @1.72 da unión 0.80 con 3/5 y 3/6 frente a 0.58 implícita; Reijnders/Tzolis anota o asiste @1.67, 0.75 con 3/6 y 3/6 frente a 0.60. Los individuales tienen n 5–6 y no cumplen: **sin confianza**. Summerville/Reijnders asiste @2.47 (mismo equipo): 4 de 7 conjunto, no cumple. Las parejas de tarjeta quedan todas por debajo de su cuota implícita.


### 2. Serbia – Alemania · 14:45 · árbitro Alberola J. (sin estadística de árbitro)
Esperado córners: Serbia 4.79 / Alemania 6.21 / total 11.0. Directos con estadística: 1.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Serbia | Más 1.5 | 1.20 | 4.79 | +3.3 | 6 de 7 | 6 de 7 | 0 de 1 |
| total | Más 7.5 | 1.34 | 11.0 | +3.5 | 6 de 7 | 5 de 7 | 1 de 1 |
| total | Más 8.5 | 1.60 | 11.0 | +2.5 | 5 de 7 | 5 de 7 | 1 de 1 |
| total | Más 9.5 | 2.02 | 11.0 | +1.5 | 5 de 7 | 5 de 7 | 1 de 1 |

**Faltas que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Serbia | Menos 11.5 | 2.05 | 10.57 | +0.9 | 5 de 7 | 5 de 7 | 1 de 1 |

_Fueras de juego: ninguna línea cumple con cuota ≥ 1.20._

_Saques de banda: ninguna línea cumple con cuota ≥ 1.20._

_Saques de meta: ninguna línea cumple con cuota ≥ 1.20._

**Remates que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Serbia | Más 6.5 | 1.40 | 10.07 | +3.6 | 6 de 7 | 5 de 7 | 0 de 1 |

**Tiros al arco que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Serbia | Más 1.5 | 1.30 | 3.5 | +2.0 | 5 de 7 | 5 de 7 | 0 de 1 |
| total | Menos 11.5 | 1.53 | 9.14 | +2.4 | 5 de 7 | 6 de 7 | 1 de 1 |
| Alemania | Menos 8.5 | 1.60 | 5.64 | +2.9 | 6 de 7 | 7 de 7 | 1 de 1 |

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Serbia | Menos 1.5 | 1.23 | 1.07 | +0.4 | 5 de 7 | 5 de 7 | 1 de 1 |
| Serbia | Más 0.5 | 1.65 | 1.07 | +0.6 | 5 de 7 | 5 de 7 | 0 de 1 |
| total | Menos 3.5 | 1.78 | 2.43 | +1.1 | 6 de 7 | 7 de 7 | 1 de 1 |
| total | Menos 3.75 | 1.65 | 2.43 | +1.3 | 6 de 7 | 7 de 7 | 1 de 1 |
| total | Menos 4.0 | 1.47 | 2.43 | +1.6 | 6 de 7 | 7 de 7 | 1 de 1 |
| total | Menos 4.5 | 1.34 | 2.43 | +2.1 | 7 de 7 | 7 de 7 | 1 de 1 |
| Alemania | Menos 2.5 | 1.85 | 1.36 | +1.1 | 7 de 7 | 7 de 7 | 1 de 1 |
| Alemania | Menos 3.5 | 1.32 | 1.36 | +2.1 | 7 de 7 | 7 de 7 | 1 de 1 |

**Tarjetas que cumplen (cuota ≥ 1.20; serie de amarillas, Betano cuenta puntos)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Serbia | Más 0.5 | 1.75 | 2.2 | +1.7 | 6 de 7 | 6 de 6 | 1 de 1 |
| Alemania | Menos 2.5 | 1.20 | 1.31 | +1.2 | 6 de 7 | 5 de 6 | 1 de 1 |
| Alemania | Más 0.5 | 1.25 | 1.31 | +0.8 | 5 de 7 | 5 de 6 | 0 de 1 |

Tarjetas, mercados de «ambos» y «más tarjetas que» (calculados por el agente con las series de la ficha; dependencia entre equipos no modelada): Ambos ≥1 tarjetas Sí @1.38 (L 6 de 7, V 5 de 6).

**1X2 modelo vs mercado** (local / empate / visitante, %): 8 / 13 / 79 — Betano 9 / 15 / 76. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** cumple **Felix Nmecha (ALE) entradas 1+ @1.19** (cuota < 1.20): esperado 2.07, col +1.6, **5 de 5**, titular 0.9. Esperado inflado por un partido de 5 entradas (20-jun) y entradas ganadas vs total (límite de la fuente). Casi (4 de 5): Tah entradas 1+ @1.31, Tah faltas 1+ @1.72, Nmecha faltas 1+ @1.52. Las 5 bajas (Lukić, Maksimović, S. Pavlović, Stanković, Anton) se filtraron con titular 0.0. Muchos del XI con n < 5 (Havertz 4, Karl 1): las parejas con ellos no son evaluables; ninguna pareja cumple.


### 3. Escocia – Macedonia del Norte · 14:45 · árbitro Ocenas M. (sin estadística de árbitro)
Esperado córners: Escocia 5.57 / Macedonia del Norte 3.57 / total 9.14. Directos con estadística: 1.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 11.5 | 1.28 | 9.14 | +2.4 | 6 de 7 | 5 de 7 | 1 de 1 |

_Faltas: ninguna línea cumple con cuota ≥ 1.20._

**Fueras de juego que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Escocia | Menos 1.5 | 1.90 | 0.93 | +0.6 | 6 de 7 | 6 de 7 | 1 de 1 |
| total | Menos 2.5 | 2.07 | 1.86 | +0.6 | 5 de 7 | 6 de 7 | 1 de 1 |
| Macedonia del Norte | Menos 1.5 | 1.45 | 0.93 | +0.6 | 5 de 7 | 6 de 7 | 1 de 1 |

**Remates que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Escocia | Menos 20.5 | 1.82 | 15.79 | +4.7 | 6 de 7 | 5 de 7 | 0 de 1 |
| Escocia | Menos 21.5 | 1.57 | 15.79 | +5.7 | 6 de 7 | 5 de 7 | 0 de 1 |
| total | Menos 25.5 | 2.50 | 26.21 | −0.7 | 5 de 7 | 5 de 7 | 0 de 1 |
| total | Menos 27.5 | 1.83 | 26.21 | +1.3 | 5 de 7 | 5 de 7 | 0 de 1 |
| total | Menos 29.5 | 1.45 | 26.21 | +3.3 | 5 de 7 | 5 de 7 | 0 de 1 |

_Tiros al arco: ninguna línea cumple con cuota ≥ 1.20._

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Escocia | Menos 3.5 | 1.27 | 1.86 | +1.6 | 7 de 7 | 5 de 7 | 1 de 1 |
| total | Menos 3.5 | 1.45 | 2.64 | +0.9 | 7 de 7 | 5 de 7 | 1 de 1 |

**Tarjetas que cumplen (cuota ≥ 1.20; serie de amarillas, Betano cuenta puntos)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 4.5 | 1.88 | 4.07 | +0.4 | 5 de 7 | 5 de 7 | 0 de 1 |

Tarjetas, mercados de «ambos» y «más tarjetas que» (calculados por el agente con las series de la ficha; dependencia entre equipos no modelada): Ambos ≥1 tarjetas Sí @1.23 (L 7 de 7, V 7 de 7).

**1X2 modelo vs mercado** (local / empate / visitante, %): 85 / 11 / 4 — Betano 81 / 14 / 5. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** ninguna línea cumple (lo más cercano: Bardhi remates 1+ @1.15, 4 de 7). Betano no ofrece entradas, faltas ni atajadas de jugador y no hay parejas. Binks se tomó como baja (Flashscore lo trae también en el XI; conflicto anotado en dudas); Gannon-Doak no casó con Betano (sin historial, sin análisis). 10 jugadores con n < 5 (McTominay 3, Tierney 2).


### 4. Eslovenia – Suiza · 14:45 · árbitro Vergoote J. (sin estadística de árbitro)
Esperado córners: Eslovenia 4.07 / Suiza 4.36 / total 8.43. Directos con estadística: 3.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 10.5 | 1.29 | 8.43 | +2.1 | 5 de 7 | 6 de 7 | 3 de 3 |
| total | Más 6.5 | 1.26 | 8.43 | +1.9 | 6 de 7 | 5 de 7 | 3 de 3 |
| Suiza | Más 3.5 | 1.26 | 4.36 | +0.9 | 5 de 7 | 5 de 7 | 3 de 3 |

_Estadísticas de partido: Betano no las ofrece en este partido._

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 3.5 | 1.26 | 2.21 | +1.3 | 7 de 7 | 6 de 7 | 3 de 3 |
| total | Más 1.5 | 1.40 | 2.21 | +0.7 | 5 de 7 | 6 de 7 | 2 de 3 |

**Tarjetas que cumplen (cuota ≥ 1.20; serie de amarillas, Betano cuenta puntos)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Eslovenia | Más 0.5 | 1.67 | 2.86 | +2.4 | 7 de 7 | 7 de 7 | 3 de 3 |

Tarjetas, mercados de «ambos» y «más tarjetas que» (calculados por el agente con las series de la ficha; dependencia entre equipos no modelada): Más tarjetas que: 1 (local más) @1.82 (L 5 de 7, V 5 de 7).

**1X2 modelo vs mercado** (local / empate / visitante, %): 17 / 25 / 58 — Betano 17 / 26 / 57. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** Betano solo ofrece anota/asiste/anota_o_asiste/tarjeta (sin escaleras, sin parejas). Cumple **Dan Ndoye (SUI) anota o asiste «Sí» @1.98: 5 de 7** (titular 0.9; sin esperado ni colchón porque no es escalera). Ndoye anota @3.00: 4 de 7, no cumple. Embolo n = 3, Matko y Athekame n = 4: no pueden cumplir. Urbancic está en el XI con línea pero sin partidos en la ventana; Gnezda Cerin no casó con Betano.


### 5. Moldavia – Kazajistán · 12:00 · árbitro Colombo A. (sin estadística de árbitro)
Esperado córners: Moldavia 5.93 / Kazajistán 6.36 / total 12.29. Directos con estadística: 3.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 6.5 | 1.24 | 12.29 | +5.8 | 7 de 7 | 7 de 7 | 2 de 3 |
| total | Más 7.5 | 1.45 | 12.29 | +4.8 | 6 de 7 | 7 de 7 | 2 de 3 |
| total | Más 8.5 | 1.82 | 12.29 | +3.8 | 6 de 7 | 7 de 7 | 2 de 3 |
| total | Más 9.5 | 2.35 | 12.29 | +2.8 | 5 de 7 | 6 de 7 | 2 de 3 |

_Estadísticas de partido: Betano no las ofrece en este partido._

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 1.5 | 1.47 | 2.64 | +1.1 | 7 de 7 | 6 de 7 | 3 de 3 |
| Kazajistán | Más 0.5 | 1.45 | 1.71 | +1.2 | 7 de 7 | 7 de 7 | 3 de 3 |

_Tarjetas: ninguna línea cumple con cuota ≥ 1.20._

**1X2 modelo vs mercado** (local / empate / visitante, %): 37 / 29 / 35 — Betano 36 / 31 / 33. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** sin alineación publicada en Flashscore al leer (~13:00 del 12-nov): no se analizan (regla 1).


### 6. Bulgaria – Islandia · 14:45 · árbitro Badstubner F. (sin estadística de árbitro)
Esperado córners: Bulgaria 4.07 / Islandia 5.5 / total 9.57. Directos con estadística: 1.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 6.5 | 1.22 | 9.57 | +3.1 | 6 de 7 | 6 de 7 | 1 de 1 |
| total | Más 7.5 | 1.42 | 9.57 | +2.1 | 6 de 7 | 6 de 7 | 1 de 1 |
| total | Más 8.5 | 1.75 | 9.57 | +1.1 | 6 de 7 | 6 de 7 | 1 de 1 |

_Estadísticas de partido: Betano no las ofrece en este partido._

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 3.5 | 1.27 | 2.86 | +0.6 | 6 de 7 | 6 de 7 | 1 de 1 |
| total | Más 1.5 | 1.36 | 2.86 | +1.4 | 5 de 7 | 6 de 7 | 1 de 1 |
| Islandia | Menos 2.5 | 1.22 | 1.36 | +1.1 | 6 de 7 | 5 de 7 | 0 de 1 |

**Tarjetas que cumplen (cuota ≥ 1.20; serie de amarillas, Betano cuenta puntos)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Islandia | Menos 2.5 | 1.85 | 1.64 | +0.9 | 7 de 7 | 6 de 7 | 1 de 1 |

**1X2 modelo vs mercado** (local / empate / visitante, %): 21 / 27 / 52 — Betano 22 / 26 / 52. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** sin alineación publicada en Flashscore al leer (~13:00 del 12-nov): no se analizan (regla 1).


### 7. Luxemburgo – Estonia · 14:45 · árbitro Barbara I. (sin estadística de árbitro)
Esperado córners: Luxemburgo 3.86 / Estonia 4.43 / total 8.29. Directos con estadística: 1.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 10.5 | 1.35 | 8.29 | +2.2 | 7 de 7 | 6 de 7 | 1 de 1 |
| total | Más 6.5 | 1.22 | 8.29 | +1.8 | 5 de 7 | 7 de 7 | 1 de 1 |
| Estonia | Más 3.5 | 1.60 | 4.43 | +0.9 | 5 de 7 | 5 de 7 | 1 de 1 |

_Estadísticas de partido: Betano no las ofrece en este partido._

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Estonia | Menos 1.5 | 1.30 | 0.86 | +0.6 | 5 de 7 | 7 de 7 | 1 de 1 |

_Tarjetas: ninguna línea cumple con cuota ≥ 1.20._

**1X2 modelo vs mercado** (local / empate / visitante, %): 40 / 30 / 29 — Betano 40 / 30 / 30. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** sin alineación publicada en Flashscore al leer (~13:00 del 12-nov): no se analizan (regla 1).


### 8. Eslovaquia – Islas Feroé · 14:45 · árbitro Al-Emara M. (sin estadística de árbitro)
Esperado córners: Eslovaquia 6.36 / Islas Feroé 3.71 / total 10.07. Directos con estadística: 1.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Más 7.5 | 1.30 | 10.07 | +2.6 | 6 de 7 | 5 de 7 | 1 de 1 |
| total | Más 8.5 | 1.55 | 10.07 | +1.6 | 6 de 7 | 5 de 7 | 1 de 1 |

_Estadísticas de partido: Betano no las ofrece en este partido._

**Goles que cumplen (cuota ≥ 1.20; las líneas asiáticas cuentan solo la victoria completa)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| Eslovaquia | Menos 2.5 | 1.47 | 1.57 | +0.9 | 5 de 7 | 6 de 7 | 1 de 1 |
| total | Más 1.5 | 1.27 | 2.93 | +1.4 | 6 de 7 | 5 de 7 | 1 de 1 |

_Tarjetas: ninguna línea cumple con cuota ≥ 1.20._

Tarjetas, mercados de «ambos» y «más tarjetas que» (calculados por el agente con las series de la ficha; dependencia entre equipos no modelada): Más tarjetas que: 2 (visitante más) @1.57 (L 5 de 7, V 6 de 7).

**1X2 modelo vs mercado** (local / empate / visitante, %): 72 / 19 / 9 — Betano 71 / 19 / 10. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** sin alineación publicada en Flashscore al leer (~13:00 del 12-nov): no se analizan (regla 1).


### 9. Liechtenstein – Azerbaiyán · 14:45 · árbitro Tohver K. (sin estadística de árbitro)
Esperado córners: Liechtenstein 2.21 / Azerbaiyán 6.07 / total 8.29. Directos con estadística: 1.

**Córners que cumplen (cuota ≥ 1.20)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 9.5 | 1.67 | 8.29 | +1.2 | 5 de 7 | 5 de 7 | 1 de 1 |
| total | Menos 10.5 | 1.39 | 8.29 | +2.2 | 6 de 7 | 6 de 7 | 1 de 1 |

_Estadísticas de partido: Betano no las ofrece en este partido._

_Goles: ninguna línea cumple con cuota ≥ 1.20._

_Tarjetas: ninguna línea cumple con cuota ≥ 1.20._

**1X2 modelo vs mercado** (local / empate / visitante, %): 6 / 18 / 76 — Betano 7 / 18 / 76. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** sin alineación publicada en Flashscore al leer (~13:00 del 12-nov): no se analizan (regla 1).


### 10. Andorra – Gibraltar · 14:45 · árbitro Hennessy R. (sin estadística de árbitro)
Esperado córners: Andorra 5.71 / Gibraltar 3.5 / total 9.21. Directos con estadística: 1.

_Córners: ninguna línea cumple con cuota ≥ 1.20._

_Estadísticas de partido: Betano no las ofrece en este partido._

_Goles: ninguna línea cumple con cuota ≥ 1.20._

**Tarjetas que cumplen (cuota ≥ 1.20; serie de amarillas, Betano cuenta puntos)**

| Ámbito | Línea | Cuota | Esperado | Col | L | V | D |
|---|---|---|---|---|---|---|---|
| total | Menos 5.5 | 2.00 | 4.5 | +1.0 | 5 de 7 | 5 de 6 | 1 de 1 |
| Gibraltar | Menos 2.5 | 2.27 | 1.87 | +0.6 | 7 de 7 | 5 de 6 | 1 de 1 |

**1X2 modelo vs mercado** (local / empate / visitante, %): 55 / 29 / 16 — Betano 54 / 30 / 16. Solo información: el modelo toma sus goles esperados de las cuotas, así que coincidir no confirma nada.

**Jugadores:** sin alineación publicada en Flashscore al leer (~13:00 del 12-nov): no se analizan (regla 1).

---

## Combinadas del mismo partido (agente `combinadas`)

Solo con patas que ya cumplen (cuota ≥ 1.20) y que Betano ofrece; ninguna lleva patas de jugador (bajan la probabilidad y las alineaciones son probables). **No tengo el precio del cupón de Betano:** «cuota producto» es el producto de las cuotas individuales, un techo; con el precio real hay que recalcular. Con p·producto − 1 el EV sale negativo (entre −2 % y −6 % en las mejores). `p` es la probabilidad de decisión del modelo (mezcla simulación y mercado); «stress» es esa `p` con la pata más frágil 5 pts peor.

| Combinada | Cuota producto | p | Stress | Justa / mín. | Pata más frágil |
|---|---|---|---|---|---|
| Países Bajos–Grecia: córners Más 6.5 @1.20 (7/7 y 6/7) + goles Menos 4.5 @1.22 (6/7 y 6/7) | 1.46 | 0.662 | 0.622 | 1.51 / 1.55 | córners Más 6.5 (en el piso de 1.20) |
| Bulgaria–Islandia: córners Más 6.5 @1.22 (6/7 y 6/7) + goles Menos 3.5 @1.27 (6/7 y 6/7) | 1.55 | 0.657 | 0.614 | 1.52 / 1.57 | goles Menos 3.5 |
| Eslovenia–Suiza: córners Más 6.5 @1.26 (6/7 y 5/7) + goles Menos 3.5 @1.26 (7/7 y 6/7) | 1.59 | 0.650 | 0.608 | 1.54 / 1.59 | córners Más 6.5 (V 5 de 7) |
| Serbia–Alemania: córners Serbia Más 1.5 @1.20 (6/7 y 6/7) + tarjetas Alemania Más 0.5 @1.25 (5/7 y 5/6) | 1.50 | 0.642 | 0.601 | 1.56 / 1.61 | tarjetas Alemania Más 0.5 |
| Escocia–Macedonia: goles Escocia Menos 3.5 @1.27 (7/7 y 5/7) + ambos con 1+ tarjetas Sí @1.23 | 1.56 | 0.626 | 0.586 | 1.60 / 1.64 | goles Escocia Menos 3.5 (V 5 de 7) |

Otras (p menor): Luxemburgo–Estonia 0.600; Países Bajos–Grecia tiros al arco Grecia Más 1.5 + tarjetas Menos 6.5 0.593; Serbia–Alemania tiros al arco Serbia Más 1.5 + goles Alemania Menos 3.5 0.549; Eslovaquia–Feroe 0.532; Moldavia–Kazajistán 0.523; Eslovenia–Suiza córners Menos 10.5 + goles Más 1.5 0.512; Escocia–Macedonia córners Menos 11.5 + remates Menos 29.5 0.509. **Sin combinada defendible:** Andorra–Gibraltar (las dos patas son de tarjetas y del mismo guion, correlación 1.95) y Liechtenstein–Azerbaiyán (córners Menos 9.5 y 10.5 son la misma línea).

**Límites de las combinadas**
- Las patas de córners y tarjetas comparten familia con las alertas del modelo (las que usé no tienen alerta propia, pero su `p` es una mezcla no verificada). Su `p` de goles sale de las cuotas de Betano y no confirma nada por separado.
- **Dependencia entre partidos:** seis boletos dependen de «muchos córners» (Países Bajos–Grecia, Eslovenia–Suiza, Bulgaria, Luxemburgo, Moldavia, Eslovaquia) y seis de «pocos goles»: cuentan como una apuesta repetida, no como independientes.
- Dentro de un partido, las dos patas de Serbia–Alemania se tratan como una sola apuesta (guion «Serbia compite») y las de Eslovenia–Suiza forman una banda de córners.
- Se descartó «ambos con 1+ tarjetas Sí» + «tarjetas Alemania Más 0.5» (p 0.719): la primera implica la segunda. Goles Menos 4.0 tiene devolución en 4 goles y no se usó.
- **Hándicap:** ningún agente lo marcó como «cumple», así que no entra en las combinadas. En los archivos del agente hay una tabla derivada de la diferencia de goles de `goles.series` (solo victoria completa, **no es criterio validado**): Serbia +2.5 y +3 (7/7 y 7/7), Grecia +3 (7/7 y 6/7), Islas Feroe +1.5 a +3, Kazajistán +0.5 y +1, Gibraltar +2. Muestra de rivales muy desiguales.

## Lo que no cumple, resumido

- **Córners:** Andorra–Gibraltar sin ninguna línea; en el resto, las líneas Menos de partidos de muchos córners esperados (Moldavia, Eslovaquia, Serbia–Alemania) y las Más de partidos de pocos (Liechtenstein) no llegan a 5 de 7 en ambos equipos. Las líneas por equipo casi nunca cumplen (solo Países Bajos–Grecia, Serbia–Alemania, Eslovenia–Suiza y Luxemburgo–Estonia).
- **Estadísticas de partido:** faltas y remates casi no cumplen salvo las listadas; fueras de juego solo en Países Bajos–Grecia y Escocia–Macedonia; saques de meta nunca (n = 4 por equipo).
- **Jugadores:** 6 líneas cumplen en los 4 partidos con alineación; las parejas ninguna. Muchos titulares tienen n < 5 en la ventana de su selección y no pueden cumplir.
- **Goles/tarjetas:** Liechtenstein–Azerbaiyán y Andorra–Gibraltar sin líneas de goles que cumplan; Liechtenstein, Luxemburgo y Moldavia sin tarjetas con cuota ≥ 1.20 que cumplan.
- Las líneas que cumplen pero con cuota < 1.20 (p. ej. córners total Más 4.5 @1.04) no están en las tablas; sí en cada `agentes/<partido>_<agente>.md`. 1X2, doble oportunidad, descanso/final y hándicap no tienen regularidad en la ficha: solo modelo y mercado, y no se presentan como «cumple».

## Límites y fallas

**Datos que faltaron**
- Estadística de árbitro: BeSoccer devuelve 404; solo el nombre. Las faltas y tarjetas no se apoyan en el árbitro.
- Alineaciones: solo 4 de 11 partidos las tenían publicadas. Son **probables** (una fuente, Flashscore, ~13:00 del 12-nov), no confirmadas.
- 1T/2T: Betano ofrece líneas por tiempo, pero no hay estadística por tiempo en la muestra: no hay ficha de 1T/2T.
- Saques de meta: n = 4 por equipo, bajo el mínimo de 5. Escocia–Macedonia: Betano no ofrece saques de banda ni de meta.
- Directos: 1 a 3 por partido; no se comprobó que estén orientados local/visitante (afectaría a las líneas por equipo, no a los totales).
- Descanso, clima, estilo y tabla del descenso colombiano: sin leer.
- Jugadores sin casar o sin historial: Gannon-Doak (Escocia) y Gnezda Cerin (Eslovenia) sin casar con Betano; Urbancic sin partidos en la ventana. El historial de algunos (Karetsas, Mavropanos, Tsimikas) incluye partidos de 2025, por lo que no es estrictamente «últimos 7 de la selección».
- Tarjetas: la fuente no trae rojas (ver advertencia 3).

**Arreglado desde la versión anterior**
- `puntuar.py` ya cuenta todas las líneas de jugadores (anota/asiste/tarjeta, entradas, faltas, atajadas): Eslovenia–Suiza deja de salir «no lo ofrece» y Nmecha/Tsimikas cuentan (commit 2c1966a).
- Líneas de goles asiáticas (.25/.75): la ficha cuenta solo la victoria completa.
- La corrección de las alertas del modelo (advertencia 1): no es una falla general del modelo; está en córners, tarjetas, saques y «más … que».

**Pendiente (sin corregir)**
- `ficha.bajas` sigue vacío en las 4 fichas con alineación (las bajas de Serbia–Alemania se filtran porque aparecen con titular 0.0).
- Contexto con valores inconsistentes en las notas (p. ej. Países Bajos–Grecia con `necesita_ganar: False` en ambos pese a ser choque directo por la cima; Eslovaquia–Feroe). Afecta al puntaje de situación, no a las estadísticas.
- Las alertas de córners/tarjetas del modelo (15–53 pts) no se investigaron a fondo: sus probabilidades en esos mercados no se usaron.
- Colchón negativo: Escocia–Macedonia remates total Menos 25.5 (−0.7): se informa, no se excluye.
- Dos agentes ejecutaron por error el `gen.py` de otro en el scratchpad compartido; no tocaron archivos del repo.

**Pruebas (12-nov, tras los cambios de hoy):** `test_modelo` 106 superadas · `test_ficha` 18 · `test_betano` 11 · `test_recoleccion` 17. Las tablas por línea se generaron directo de las fichas (sin transcribir); los textos de jugadores, 1X2 y combinadas se copiaron de los informes de los agentes (`agentes/`), cuyas cifras principales se contrastaron con los archivos de detalle.
