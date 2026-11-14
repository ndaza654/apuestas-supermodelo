# Lectura de tu boleto abierto · Combinada de 3 Bet Builder (Japón–Brasil, Valladolid–Castellón, Kosovo–Israel)

- **Entrega:** viernes 13-nov-2026, 23:24 (Bogotá).
- **Boleto (captura tuya de Betano, «Abiertas (1)»):** combinada de 3 Bet Builder, apuesta $13.450 (3,6 u), cuota 7,60, ganancia potencial $102.251.
- **Fuente de las probabilidades:** fichas y modelo de la jornada del 14-nov (`registro/lineas.csv`), con cuotas de Betano leídas el 13-nov entre las 19:01 y las 19:15; la conjunta de cada partido sale de la simulación del modelo (`supermodelo/combos.py`).
- **Límites:** cuotas sin releer; muestra de 7 partidos por equipo («cumple» = 5 de 7); sin estadísticas de árbitro (y árbitro sin publicar en Japón–Brasil); alineaciones solo probables; Betano cuenta tarjetas en puntos y la serie solo trae amarillas.

## Veredicto
El boleto se da más o menos 1 de cada 9 veces según el modelo (11 %), y Betano lo paga como si fuera 1 de cada 7,6 (13 %): **EV de −13 %**. Con el recorte de la auditoría (cada Bet Builder ×0,80) la probabilidad baja a cerca de 6 %. Por tus propias reglas es una **lotería** (6 patas en total), y 3,6 u no es stake mínimo.

## Los tres Bet Builder

| Partido (hora) | Patas | Cuota Betano | p conjunta (simulación) | Cuota justa | Pata más frágil |
|---|---|---|---|---|---|
| Japón–Brasil (05:15) | Tarjetas Brasil Más 0.5 + Córners Más 7.5 | 2,02 | 45 % | 2,20 | Córners Más 7.5 |
| Valladolid–Castellón (08:00) | Tarjetas Más 5.5 + Goles Más 1.5 | 1,95 | 49 % | 2,06 | Tarjetas Más 5.5 |
| Kosovo–Israel (09:00) | Córners Menos 9.5 + Goles Israel Menos 1.5 | 1,93 | 52 % | 1,93 | Córners Menos 9.5 |

Conjunta de los tres (partidos independientes): 45 % × 49 % × 52 % = **11,4 %** (cuota justa 8,74; para no perder a 7,60 haría falta 13,2 %). Con cada pata 5 puntos peor: 9,0 %. Con el recorte de la auditoría (×0,80 por Bet Builder): 5,9 %.

## Pata por pata

| Pata | Cuota suelta | p modelo | Local | Visitante | Directos | Real hasta hoy (con «cumple») |
|---|---|---|---|---|---|---|
| Tarjetas Brasil Más 0.5 | 1,42 | 68 % | 6 de 6 | 7 de 7 | 1 de 1 | tarjetas Más 7 de 7 (muestra muy chica) |
| Córners Más 7.5 (Japón–Brasil) | 1,42 | 67 % | 6 de 7 | 6 de 7 | 1 de 1 | córners Más 24 de 39 (62 % contra 76 % dicho) |
| Tarjetas Más 5.5 (Valladolid–Castellón) | 1,57 | 60 % | 7 de 7 | 5 de 7 | 1 de 2 | tarjetas Más 7 de 7 (muestra muy chica) |
| Goles Más 1.5 (Valladolid–Castellón) | 1,24 | 79 % | 6 de 7 | 6 de 7 | 1 de 2 | goles Más 21 de 30 (70 % contra 76 %) |
| Córners Menos 9.5 (Kosovo–Israel) | 1,44 | 69 % | 6 de 7 | 6 de 7 | 3 de 3 | córners Menos 17 de 20 (85 % contra 82 %) |
| Goles Israel Menos 1.5 | 1,31 | 75 % | 5 de 7 | 6 de 7 | 3 de 3 | goles Menos 46 de 59 (78 % contra 87 %) |

## Lo bueno
- Las 6 patas cumplen 5 de 7 en ambos equipos; ninguna tiene alerta del modelo.
- Kosovo–Israel es el mejor de los tres: Betano paga 1,93, igual a la cuota justa, y sus dos patas son del tipo que mejor se ha dado (córners Menos y goles Menos), con directos 3 de 3 y 3,4 °C de pronóstico.
- Brasil ha visto al menos una amarilla en 7 de 7 y los rivales de Japón en 6 de 6.

## Lo que pesa en contra
- Solo 2 de las 6 patas llegan a 70 % por sí solas (Goles Más 1.5 y Goles Israel Menos 1.5). La regla de la auditoría pide 70 % en cada pata.
- Dos patas son de tarjetas, el mercado peor calibrado y sin dato de árbitro. En Japón–Brasil el árbitro ni siquiera está publicado y es amistoso (rotación y tensión impredecibles).
- Córners Más 7.5 es el lado de córners que menos se ha dado frente a lo que dice la p.
- Tarjetas Más 5.5 (60 %) es la pata más débil del boleto: Betano cuenta puntos, pero la serie de respaldo solo trae amarillas y el directo es 1 de 2.
- Hasta hoy mis combinadas de 3 patas se dieron 5 de 21 y las de 4 o más, 0 de 3.

## Qué mirar
- Japón–Brasil (05:15) decide primero y es el Bet Builder más flojo (45 %). Si pasa, el boleto sube a cerca de 25 % con dos partidos por delante.
- La decisión de dejarlo correr o usar Cash Out es tuya; yo no entro a Betano ni toco la apuesta.
