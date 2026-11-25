# Goles, resultado y ambos marcan

## Lectura obligatoria por partido
1. **Esperado de goles por equipo:** (a favor propio + concedido por el rival)/2; en partidos muy desiguales, sumar el esperado de cada uno (*tipster*).
2. **Qué se juega y ritmo:** necesita ganar → el partido se abre en el 2T si no va por delante; **partido decisivo → los primeros tiempos suelen ser más cerrados** de lo que dicen los promedios (*tipster*); nada en juego baja la intensidad.
3. **Bajas y once:** delantero titular, portero, línea defensiva; rotación por otra competición.
4. **Alertas del modelo:** si la simulación se aleja del mercado, no usar el modelo como argumento; decirlo.
5. **Ambos marcan:** regularidad «marcaron los dos» en ambos equipos + directos; equipo que no deja el arco en cero.
6. **Resultado/doble oportunidad:** regularidad de «ganó/no perdió»; ver el precio y la probabilidad sin margen.
7. **Descanso/final y 1T/2T:** solo modelo y mercado (sin goles por tiempo en la ficha).
8. Hándicap de Betano = europeo (3 resultados); líneas asiáticas con media ganancia/pérdida.

## Medición
Goles Más 71 % en tus boletos (n 77) y 5 de 5 en los BB Boost; goles del modelo ≈ precio (Brier 0,1755 / 0,1751). En goles 2,5 la cuota ya descuenta lo que ve el filtro.

## Estrategias de los videos de @ingenieroanalista10 (cuenta nueva; 25-nov-2026; tipster sin verificar)
**A. «Más 2,5 goles» con 2 filtros** (video de 63 s): (1) local pagado como máximo ≈ 1,50 (transcripción: «unos 50»; probablemente 1,50); (2) línea **1T Más 1,5 goles** pagada como máximo 2,15. Dice 500 aciertos de 670 partidos (75 %) con una lista de ligas (la lista sale en pantalla, no en el audio).
- **Medición propia:** 50.408 partidos de 6 ligas (backtest, solo filtro 1): Más 2,5 sale 49,8 % en general, **59,7 %** con local ≤ 1,50 (n 7.986; 65,9 % con ≤ 1,25; 62,5 % en los últimos 6.000 partidos). En mis líneas de Betano (237 partidos): con 1T Más 1,5 ≤ 2,15 → 64,8 % (n 54); filtro completo → **62,5 % (n 24)**, cuota media de Más 2,5 ≈ 1,35 (equilibrio ≈ 74 %).
- **Lectura:** el filtro sí sube el acierto frente a la base, pero **no reproduce el 75 %** y, al precio que paga Más 2,5 en esos partidos, el 75 % del video sería el equilibrio, no una ventaja. El filtro 2 es un precio: la casa ya espera muchos goles en el 1T. n 24 no concluye. Falta la cuota 1T en el backtest (no está en football-data).
**B. Previa por bajas** (video Palmeiras–Cruzeiro): si ambos llegan sin titulares defensivos y el favorito tiene calendario cargado (rotación), ambos marcan y goles Más pesan más que el escudo. Se alinea con el punto 3 y la bandera `rotacion`.
**C. Final a partido único** (video Atlético-MG–Boca): historial reciente de cruces cerrados (2-2, 0-0, 0-0), finalistas con presión y porteros de penales → goles Menos / definición en penales. Se alinea con el punto 2 (partido decisivo = más cerrado).
Calificación de B y C con resultados reales: `entregas/2026-11-25/1330_videos_estrategias.md`.
