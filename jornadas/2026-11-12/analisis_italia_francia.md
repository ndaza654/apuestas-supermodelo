# Italia – Francia · análisis de todos los mercados
UEFA Liga de Naciones A, Grupo 1, jornada 5 · jueves 12-nov-2026, **14:45 Bogotá** · San Siro (Milán) · árbitro Istvan Kovacs.

> **Antes de usar nada de esto.** (1) No se recolectó información nueva: esta sesión no tiene navegador, así que el análisis usa la recolección de las 00:05–00:35 del 12-nov. (2) **Las cuotas tienen ~14 h**: releerlas en Betano antes de apostar. (3) **Las alineaciones no están confirmadas** (fuentes de las 00:15–00:20). (4) Las cifras salen de `fichas/ficha_italia-francia.*`, la entrada `pub/entradas/italia-francia.json`, el contexto y el informe del modelo de esta carpeta; los tres agentes (córners, partido, jugadores) las recalcularon sin diferencias. Lo marcado «provisional» es un cálculo a mano que **no** viene de la ficha.

## Enfoque de mercados
- **Qué ofrece Betano:** 587 mercados. Córners (total, local, visitante, 1T, 2T, «más córners que»), tarjetas (14 líneas, por equipo, «más tarjetas que», «ambos con N tarjetas»), faltas, fueras de juego, saques de banda y de meta, remates, tiros al arco, goles/resultado/hándicap/ambos marcan/descanso-final, 49 jugadores con línea y 56 parejas «cualquiera de los jugadores…». No existe hándicap de córners.
- **Qué pesa en este partido:**
  - **Córners y tiros al arco**: son los mercados con más líneas que cumplen la regularidad con muestra de 7+7.
  - **Tarjetas**: el contexto las empuja (Italia necesita no perder antes de visitar a Bélgica, árbitro con más tarjetas que la media, lluvia), pero **la ficha no genera tarjetas** (hueco del pipeline), así que solo hay un cálculo provisional.
  - **Goles/resultado**: la lectura del modelo es Francia 48 %, empate 27 %, Italia 25 %, con 2.8 goles frente a 3.0 de Betano. **No lo uso como señal**: es el partido donde el contexto más separa al modelo de Betano, y Francia llega sin Mbappé, Dembélé, Koundé, Saliba ni Tchouaméni (la muestra de Francia incluye partidos con ellos). No verifiqué las alertas del informe para este partido.
  - **Jugadores y parejas**: solo escaleras bajas de jugadores que casi seguro juegan; anotadores y parejas son lotería (ninguna con EV positivo en el informe).
- **Criterio:** cumple = ≥5 de 7 en ambos equipos (n mínimo 5); colchón informativo, no excluye nada; en líneas de equipo «L» = lo propio del local y «V» = lo que concede el rival (y al revés para el visitante); en totales, los totales de los partidos de cada equipo. Directos: n = 0.

## Cobertura de datos
- Muestra: 7 oficiales de Italia (sin los amistosos con Grecia y Luxemburgo) y 7 de Francia (6 en tarjetas y fueras). **Directos útiles: ninguno**; los 6 H2H del archivo son de 1938–2006 y sin estadísticas.
- El **1-1 del 2-oct-2026** entre ambos está en las dos muestras (como partido de forma, no como directo), con Italia al 35 % de posesión y una roja a Upamecano. Sin ese partido varias líneas dejan de cumplir (ver córners).
- Estadística por tiempo: la ficha no la usa, así que **no hay ficha de 1T/2T** para ningún mercado. Existe córners/amarillas de 1T en el contexto, pero no se convirtió en ficha.

## 1. Córners (esperado Italia 4.14 · Francia 5.93 · total 10.07)
Cumplen con cuota ≥ 1.20:

| Línea | Cuota | Colchón | L | V | Nota |
|---|---|---|---|---|---|
| Total Más 7.5 | 1.30 | +2.57 | 7 de 7 | 6 de 7 | Aguanta sin el 2-oct (6/6 y 5/6). El menor total de la muestra es 7. |
| Italia Menos 5.5 | 1.24 | +1.36 | 5 de 7 | 7 de 7 | Media de Italia inflada por un 12 ante Irlanda del Norte (mediana 4). Sin el 2-oct: 4/6. |
| Francia Más 3.5 | 1.22 | +2.43 | 5 de 7 | 5 de 7 | Justo en el mínimo; sin el 2-oct: 4/6 y 4/6. |
| Francia Más 4.5 | 1.50 | +1.43 | 5 de 7 | 5 de 7 | Igual de ajustada. |
| Italia Menos 4.5 | 1.52 | +0.36 | 5 de 7 | 5 de 7 | Colchón mínimo. |

Otras 12 cumplen con cuota 1.03–1.19 (total Más 4.5/5.5/6.5, total Menos 12.5/13.5/14.5, Italia Más 1.5, Menos 6.5/7.5, Francia Más 2.5, Menos 8.5/9.5): regularidad alta, sin valor práctico.
**No cumplen:** todo el centro del mercado (totales 8.5–11.5 en ambos lados; Italia 2.5–3.5; Francia 5.5–7.5). Casi: Francia Menos 7.5 @1.21 (4/6), Italia Más 3.5 (5/4), Francia Más 5.5 (5/4).
**«Más córners que»:** Italia 3.20, empate 6.60, Francia 1.50. Sin criterio de cumple; informativo (Francia ganó la batalla en 4 de 7, Italia en 2 de 7, rivales distintos).
**1T/2T** (Más/Menos 1.5 a 8.5): sin ficha. Dato sospechoso en el contexto: Italia–Bélgica con 1T 1–8 sobre un total 4–8.

## 2. Estadísticas de partido
Cumplen (todas con n = 7 y cuota ≥ 1.20):

| Mercado | Línea | Cuota | Esperado | Colchón | L | V |
|---|---|---|---|---|---|---|
| Tiros al arco | Total Más 8.5 | 1.45 | 10.57 | +2.07 | 7 de 7 | 5 de 7 |
| Tiros al arco | Francia Más 4.5 | 1.40 | 6.29 | +1.79 | 5 de 7 | 5 de 7 |
| Faltas | Total Menos 23.5 | 1.95 | 22.36 | +1.14 | 5 de 7 | 6 de 7 |
| Faltas | Francia Menos 11.5 | 1.82 | 10.50 | +1.00 | 5 de 7 | 5 de 7 |
| Faltas | Italia Menos 12.5 | 1.78 | 11.86 | +0.64 | 5 de 7 | 5 de 7 |
| Saques de meta | Italia Más 7.5 | 1.75 | 9.43 | +1.93 | 5 de 7 | 5 de 7 |

Cuidado: las tres de faltas son una sola apuesta en tres formas; las dos de tiros al arco están correlacionadas (Francia aporta casi todos); el saque de meta de Italia depende de un 20 ante Bosnia (sin él, 4 de 6 y no cumple). Los esperados de Francia vienen de datos con Mbappé y Dembélé.
**No cumplen:** fueras de juego (n = 6, ninguna), saques de banda (ninguna; no usar el 1T por el defecto conocido del modelo), remates (las 9 líneas; Italia Más 11.5 6/4), el resto de tiros al arco (total Más 9.5 5/3, Italia Más 3.5 5/1), el resto de saques de meta (total Más 13.5 @1.82 con colchón +2.64 pero 7/4), faltas Más (todas 1–2 de 7).

### Tarjetas (puntos: amarilla 1, roja 2) — PROVISIONAL, no es de la ficha
Calculado a mano con la tabla del contexto (Italia 7 partidos, Francia 6; roja en blanco = 0, supuesto). Esperado Italia 2.46, Francia 2.19, **total 4.65** (Betano 4.2; el modelo 4.6).

| Línea | Cuota | Colchón | L | V | Cumple |
|---|---|---|---|---|---|
| Total Más 2.5 | 1.29 | +2.15 | 6 de 7 | 5 de 6 | sí (provisional) |
| Total Más 3.5 | 1.65 | +1.15 | 5 de 7 | 2 de 6 | no |
| Total Menos 4.5 / Más 4.5 | 1.60 / 2.25 | ∓0.15 | 3/4 · 4/2 | | no |
| Total Menos 5.5 | 1.31 | +0.85 | 4 de 7 | 4 de 6 | no |
| Francia Menos 3.5 | 1.15 | +1.31 | 5 de 7 | 5 de 6 | sí, pero cuota < 1.20 |

«Ambos con 1+ tarjeta» (Sí @1.24): Italia 6/7, Francia 4/6, no cumple. «Más tarjetas que»: sin criterio.
**Árbitro Kovacs (hipótesis, no hecho de la muestra):** 5.23 amarillas + 0.23 rojas = ~5.69 puntos por partido en 31 partidos, contra una referencia de 4.69; en sus 10 partidos de Liga de Naciones, 4.3 amarillas. Empuja a «Más» pero no entra en el cumple. El modelo marca «Tarjetas Más 3.5 @1.65» con EV +6.7 % **por esa hipótesis**; la regularidad provisional no la respalda (Francia 2 de 6).

## 3. Jugadores
Fuentes del XI: Sofascore (probable, 00:15) y Sports Mole (00:20); **sin confirmar**. Titular 0.85 si sale en ambas, 0.60 si en una. Excluidos: Mbappé (molestias), Dembélé, Koundé, Saliba, Tchouaméni, M. Thuram, Mancini, Di Lorenzo, Raspadori, Kean. Dudas: arquero de Francia (Maignan vs Restes), Rabiot vs Camavinga, centrales de Italia (Scalvini/Ghilardi), mediocampo (Doumbia/Romano), extremo (Cissè/Cambiaghi).

| Jugador (titular) | Línea | Cuota | Esperado | Colchón | X de n |
|---|---|---|---|---|---|
| Tonali (0.85) | Remates 1+ | 1.32 | 1.76 | +1.26 | 6 de 6 |
| P. Esposito (0.85) | Tiros al arco 1+ | 1.25 | 1.83 | +1.33 | 6 de 7 |
| P. Esposito | Remates 2+ | 1.25 | 2.93 | +1.43 | 5 de 7 |
| Calafiori (0.85) | Entradas 1+ | 1.14 | 1.93 | +1.43 | 5 de 5 |
| Doué (0.85) | Tiros al arco 1+ | 1.26 | 1.77 | +1.27 | 6 de 7 |
| Olise (0.85) | Remates 2+ | 1.28 | 2.83 | +1.33 | 5 de 7 |
| Olise | Anota o asiste Sí | 1.67 | n/a | n/a | 5 de 7 |
| Rabiot (0.60) | Remates 1+ | 1.26 | 1.65 | +1.15 | 6 de 7 |
| Rabiot (0.60) | Entradas 1+ | 1.14 | 1.81 | +1.31 | 5 de 7 |
| Upamecano (0.60) | Entradas 1+ | 1.11 | 2.18 | +1.68 | 5 de 6 |
| Upamecano (0.60) | Faltas 1+ | 1.50 | 1.00 | +0.50 | 5 de 6 |

Avisos que cambian la lectura:
- **Minutos:** la ficha da ~82′ a todos, pero el historial muestra suplentes y cameos (promedios: Barcola 44′, Cherki 40′, Doué 50′, Pio Esposito 59′, Olise 69′). El esperado y el colchón de la ficha son optimistas; el informe del modelo da menos (Pio al arco 1.2, Doué al arco 1.2, Tonali remates 1.1, Rabiot remates 0.9).
- **Pio Esposito:** al arco 1+ y remates 2+ a la misma cuota son el mismo guion, no dos apuestas.
- **Olise anota o asiste** se apoya en el 4-1 a Bélgica con 30′ jugados; con 60′+ son 3 de 6.
- **Entradas:** Betano da total y el historial puede ser entradas ganadas (la fuente no lo aclara) → conservador.
- **Casi (4 de n):** Pio Esposito remates 3+, al arco 2+, anota, anota o asiste; Olise remates 3+; Barcola al arco 1+; Donnarumma atajadas 3+ (4 de 7; el esperado 4.09 lo inflan un 10 y un 7; mediana 3) y 4+; Bastoni faltas 1+ (4 de 5).
- **No cumplen:** anota, asiste y tarjeta de todos los demás (Bastoni tarjeta 3 de 5, Olise asiste 3 de 7, Olise anota 3 de 7); Maignan atajadas (3 de 7). Con n < 5 (no pueden cumplir): Da Cunha, Diouf, Jacquet, Truffert, Yoro, Camavinga, Gusto, S. Esposito, Kayode, Scalvini, Romano, Doumbia; sin historial: Cissè, Ghilardi.
- **Parejas «cualquiera de los jugadores…»** (56: anota 20, anota o asiste 12, asiste 12, tarjeta 12): ninguna con EV positivo en el informe. Mejores en probabilidad: Olise o Doué anota o asiste @1.35 (63 %, EV −14 %), Olise o Cherki @1.42 (61 %, −13 %); tarjeta Tonali o Barella @1.95 (47 %, −8 %). 13 incluyen a Vergara (titular 0.12) y quedan fuera. Hay dependencia por equipo: no sumar probabilidades.

## 4. Descanso/final, goles y resultado
- **Descanso/final** (informe del modelo): Empate/Empate @5.80, 15 %, EV −10 %; Francia/Francia @3.00, 29 %, −14 %; «descanso o final Empate» @1.75, 54 %, −6 % (necesitaría 1.94). Sin valor.
- **Goles/resultado/hándicap/ambos marcan:** sin ficha de regularidad. Lectura del modelo, **no usada como señal**: Francia 48 / empate 27 / Italia 25, 2.8 goles (Betano 3.0). La línea «Goles Menos 3.75 @1.38 (74 %)» del resumen del 12-nov nace de esa simulación con contexto; sin Mbappé y con el partido de ida 1-1 puede tener sentido, pero no hay regularidad que la respalde aquí.

## Las líneas más sólidas (regularidad, no valor)
1. **Córners total Más 7.5 @1.30**: 7 de 7 y 6 de 7, colchón +2.57, aguanta sin el 2-oct.
2. **Tiros al arco total Más 8.5 @1.45**: 7 de 7 y 5 de 7, colchón +2.07 (el visitante está justo en el mínimo; depende de Francia sin Mbappé).
3. **Faltas total Menos 23.5 @1.95**: 5 de 7 y 6 de 7, colchón +1.14 (comparte apuesta con Menos 11.5 Francia y Menos 12.5 Italia).
4. **Tonali remates 1+ @1.32**: 6 de 6, 5 de 5 en ≥45′, titular en ambas fuentes (EV del informe −13 %).
5. **Pio Esposito tiros al arco 1+ @1.25**: 6 de 7, titular 0.85 (minutos medios 59′; EV del informe −14 %).
Ninguna de las cinco tiene EV positivo según el informe del modelo para jugadores; el EV positivo de tarjetas depende de la hipótesis del árbitro.

## Límites y fallas
- **Sin recolección nueva** (no hay navegador en la nube): cuotas de las 00:05, alineaciones sin confirmar, sin bajas de última hora. Antes de apostar: releer cuotas en Betano y el XI oficial (se publica ~1 h antes).
- **Tarjetas fuera de la ficha** (`recoleccion/ficha.py` solo genera córners y seis estadísticas de partido) y **`stats` sin rojas**: lo de tarjetas es provisional.
- **Directos:** la ficha dice 0; el 1-1 del 2-oct está en la muestra de ambos equipos (doble conteo) y `h2h_empates_ult5 = 0` contradice ese resultado.
- **1T/2T sin ficha** aunque el contexto trae córners/goles/amarillas por tiempo.
- **Bajas:** `ficha.contexto.bajas` lista 3; `bajas_todas` trae 10. Francia: `necesita_ganar` en falso para ambos pese a que Francia asegura el primer puesto si gana.
- **Titularidad:** pares excluyentes que suman > 1 (Maignan 0.6 + Restes 0.6); minutos de 82′ para todos.
- **Esperado de Francia** (remates, tiros al arco, córners) calculado con partidos en que jugaban Mbappé y Dembélé: puede ser optimista.
- **Colchón** redondeado distinto entre .md y .json (usé el JSON). Entradas: Betano total vs historial posiblemente «ganadas».
- Clima: lluvia moderada (1.4 mm/h), 96 % humedad, 11.8 °C; no hay dato de su efecto en córners y no se inventa.
