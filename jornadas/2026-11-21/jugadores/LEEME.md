# Historial por jugador · 21-nov · estado de la recolección (21-nov 01:10 Bogotá)

**INCOMPLETO y SIN DECODIFICAR.** Esta carpeta solo guarda el crudo de Flashscore leído hasta que se cayó la conexión con el computador.

- Partidos pasados leídos: 251 de 465 (8 más no tienen tabla de jugadores en Flashscore; ~206 faltan por leer).
- **Problema de columnas:** en esta lectura los encabezados de Flashscore salieron duplicados («RatingRating») y con un encabezado «ALL» de más, y las celdas quedaron corridas respecto a los encabezados (p. ej. la columna «Rating» trae los minutos, «Minutes played» trae los goles, «Assists» trae las amarillas, «xG on target» trae los tiros al arco). Verificado contra los totales de equipo de las fichas (coincidencias exactas de la suma por equipo con la ficha: 282 para tiros al arco, 246 para amarillas, 259 para faltas), pero NO está verificado columna por columna, así que **no se generaron los `jugadores/<partido>.json` y no se recomienda ningún mercado de jugador de estadística** de esta jornada con estos datos.
- `recoleccion/flashscore_jugadores_en_par.js` ya guarda desde ahora las celdas crudas (`rows[pid].raw`) y los encabezados (`th`) para decodificar fuera de línea y verificar contra los totales del partido.
- Para retomar: volver a leer los partidos faltantes (y, mejor, todos con el extractor corregido), decodificar con alineación verificada y correr `jugadores_en_decod.py`.

## Cobertura por partido (partidos pasados leídos / total de los últimos 10 del equipo)

- 1-fc-union-berlin-rb-leipzig: local 10 de 10, visitante 10 de 10
- afc-bournemouth-nottingham-forest: local 10 de 10, visitante 10 de 10
- as-monaco-aj-auxerre: local 1 de 10, visitante 1 de 10
- aston-villa-sunderland: local 9 de 10, visitante 9 de 10
- bayer-04-leverkusen-sc-paderborn-07: local 10 de 10, visitante 10 de 10
- borussia-monchengladbach-borussia-dortmund: local 10 de 10, visitante 10 de 10
- chapecoense-sc-cruzeiro: local 0 de 10, visitante 0 de 10
- chelsea-fc-leeds-united: local 10 de 10, visitante 9 de 10
- como-1907-cagliari-calcio: local 10 de 10, visitante 10 de 10
- coventry-city-crystal-palace-fc: local 10 de 10, visitante 10 de 10
- deportivo-alaves-deportivo-de-a-coruna: local 9 de 10, visitante 9 de 10
- ec-bahia-ba-coritiba-pr: local 0 de 10, visitante 0 de 10
- eintracht-frankfurt-tsg-1899-hoffenheim: local 10 de 10, visitante 10 de 10
- fc-schalke-04-vfb-stuttgart: local 5 de 10, visitante 5 de 10
- lille-osc-olympique-lyonnais: local 0 de 10, visitante 4 de 10
- manchester-city-fulham: local 10 de 10, visitante 10 de 10
- newcastle-united-arsenal-fc: local 5 de 10, visitante 1 de 10
- ogc-niza-paris-saint-germain: local 6 de 10, visitante 7 de 10
- palmeiras-sp-flamengo-rj: local 0 de 10, visitante 0 de 10
- parma-calcio-1913-as-roma: local 1 de 10, visitante 3 de 10
- rayo-vallecano-valencia-cf: local 6 de 10, visitante 5 de 10
- rc-lens-toulouse-fc: local 1 de 10, visitante 0 de 10
- rc-strasbourg-stade-brestois-29: local 0 de 10, visitante 2 de 10
- real-madrid-rc-celta-de-vigo: local 2 de 10, visitante 2 de 10
- sevilla-fc-real-betis-balompie: local 4 de 10, visitante 2 de 10
- ss-lazio-us-lecce: local 10 de 10, visitante 10 de 10
- ssc-napoli-torino-fc: local 1 de 10, visitante 2 de 10
- sv-elversberg-sc-friburgo: local 10 de 10, visitante 10 de 10
- tottenham-hotspur-ipswich-town: local 10 de 10, visitante 10 de 10
