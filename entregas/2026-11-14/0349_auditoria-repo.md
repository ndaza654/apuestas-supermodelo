# Auditoría del repo apuestas-supermodelo

- **Fecha y hora:** sábado 14-nov-2026, 03:49 (Bogotá).
- **Commit auditado:** `11ce7af` (rama `recoleccion/2026-11-14`).
- **Alcance:** Se leyó: CLAUDE.md, recoleccion/README.md, BITACORA, ESTADO e INDICE; registro/ completo (lineas.csv, sugerencias.csv, historial, libro); el código de supermodelo/ y recoleccion/; agentes, skills y documentos de la raíz; el inventario de archivos versionados. No se leyó: los JSON crudos de flashscore/ y betano/, el historial de git anterior al 12-nov ni las páginas de Betano y Flashscore.
- **Reproducir las cifras:** scripts y salidas en `jornadas/2026-11-14/auditoria/`.

## Conclusión en 10 líneas

1. El repo está bien construido como herramienta de registro y de análisis honesto, pero **hoy no demuestra ventaja sobre Betano**.
2. Lo medido son 12 partidos: apostar las líneas del sistema pierde 6,5 %, lo mismo que el margen; las que «cumplen», 7,5 %.
3. El modelo copia el precio (47 % mercado, 53 % simulación) y, donde se aparta, acierta el precio.
4. «Cumple X de N» no añade información una vez se mira la cuota.
5. El «recorte de p» que añadí anoche empeora la predicción fuera de muestra: hay que retirarlo.
6. Tus 71 boletos reales están en −$1.925 gracias a dos aciertos; sin ellos serían −$345.316, y del 9 al 13-nov el ROI fue −23 %.
7. Tu libro fija un máximo de 7.500 por boleto y 17 de los últimos 23 lo superan.
8. Lo más frágil del flujo es que los datos se transcriben por el chat, y que volver a correr una jornada borra sus resultados.
9. Hay que reconstruir tres cosas: la recolección, el registro (con cuota de cierre) y el papel del modelo. No hay que tocar el simulador, las pruebas, el registro de sugerencias ni el libro.
10. Recomendación: seguir solo como experimento medido, a 1 u y con sencillas, y decidir con el CLV tras 100 partidos.

## Semáforo por área

| Área | Estado | Lectura |
|---|---|---|
| A · Método y estadística | rojo | No hay ventaja demostrada: 12 partidos calificados, el modelo no mejora al precio y los filtros no separan. |
| B · Modelo (supermodelo/) | ámbar | Simulador serio y bien calibrado, pero por diseño copia el precio; arrastra unas 940 líneas sin uso y un registro con CLV que nadie corre. |
| C · Recolección (recoleccion/) | rojo | Funciona, pero los datos viajan transcritos por el modelo de lenguaje (unos 280 KB por jornada) y volver a correr una jornada borra sus resultados. |
| D · Datos y registro | ámbar | Sin duplicados ni filas rotas, pero el registro y el repo crecen unos 20 MB por jornada y tres columnas clave están vacías. |
| E · Flujo y organización | ámbar | Reglas repartidas en siete sitios que se contradicen; los agentes repiten lo que ya calcula el pipeline. |
| F · Ingeniería y seguridad | verde | Sin credenciales, repo privado, 200 comprobaciones que pasan. Faltan pruebas de los extractores y versiones fijas. |
| G · Riesgos al apostar | rojo | Las reglas de stake existen en tu libro y no se cumplen: 17 de 23 boletos del 9 al 13-nov superan el máximo. |
| H · Lo que está bien | verde | Honestidad con los datos, registro previo de sugerencias, calibración con 238.858 partidos y pruebas automáticas. |

## Hallazgos (48: 4 críticos, 13 altos, 15 medios, 7 bajos, 9 cosas que están bien)

### Lo malo (críticos y altos)

#### A1 · No hay ventaja demostrada con los datos del repo

- **Severidad:** crítico · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** Con todo lo calificado, apostar las líneas del sistema pierde lo mismo que el margen de Betano. Tus boletos reales quedan en cero gracias a dos aciertos grandes.
- **Evidencia:** registro/lineas.csv: 1.460 líneas de equipo calificadas en solo 12 partidos. Apostar todas a 1 u: ROI −6,5 % (IC 95 % por partidos −11 % a −1 %). Solo las que «cumplen» (213): ROI −7,5 % (IC −21 % a +5 %). Libro: 71 boletos con dinero real, apostado $1.282.982, neto −$1.925; del 4 al 8-nov +$74.625, del 9 al 13-nov −$76.550 (ROI −23 %); sin los 2 mejores boletos el neto sería −$345.316.
- **Por qué importa:** Todo lo demás (informes, filtros, combinadas) se apoya en que el método encuentre líneas mejores que el precio. Hoy no hay ninguna medición que lo muestre.
- **Qué hacer:** Tratar el sistema como un experimento: stake fijo de 1 u, sin combinadas, y medir cuota de cierre y calibración hasta tener al menos 100 partidos antes de decidir si sigue.

#### A2 · El modelo no le agrega información al precio de Betano

- **Severidad:** crítico · **Área:** A (Método y estadística) · **Veredicto:** RECONSTRUIR · **Esfuerzo:** M
- **Qué pasa:** La probabilidad del modelo es, en la práctica, 47 % precio sin margen + 53 % simulación. Donde se aparta del precio, el que acierta es el precio.
- **Evidencia:** Regresión sobre las 1.460 líneas: p_modelo ≈ 0,470·p_mercado + 0,530·p_simulación. Brier: mercado 0,2020, modelo 0,2047, simulación sola 0,2079 (diferencia modelo − mercado +0,0028, IC −0,0018 a +0,0072). Líneas donde el modelo está 3 puntos o más por encima del mercado (162): se dieron 35 % contra 44 % del mercado y 50 % del modelo, ROI −27 %. Líneas con «EV del modelo > 0» (141): 43 % real contra 60 % dicho, ROI −20 %.
- **Por qué importa:** Las etiquetas «valor», «EV positivo» y el orden por p del modelo llevan hacia las líneas donde el modelo se equivoca, no hacia donde hay ventaja.
- **Qué hacer:** Usar la probabilidad del mercado sin margen como probabilidad de la línea. Dejar la simulación solo para probabilidades conjuntas. Quitar «valor» y «EV del modelo» de informes y fichas hasta que una muestra nueva diga otra cosa.

#### C1 · Los datos viajan del navegador al repo transcritos por el modelo de lenguaje

- **Severidad:** crítico · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** RECONSTRUIR · **Esfuerzo:** L
- **Qué pasa:** Cada archivo recolectado pasa por el contexto del chat y se vuelve a escribir a mano con un heredoc; se compara con una suma de 32 bits.
- **Evidencia:** jornadas/2026-11-14: raw 134 KB, flashscore 120 KB, alineaciones 26 KB: unos 280 KB de texto por jornada, leídos y reescritos. registro/BITACORA.md (14-nov): «hubo 2 desajustes por mi transcripción, corregidos». recoleccion/verificar_hash.py y PROMPT_NUEVA_SESION.md lo describen como el procedimiento.
- **Por qué importa:** Es la parte más cara, lenta y frágil del flujo, y limita cuántos partidos se pueden recoger.
- **Qué hacer:** Recolectar con un script en tu computador (Node o Playwright) que guarde los archivos y haga push, sin pasar por el chat. El análisis en la nube queda igual.

#### G1 · Las reglas de stake de tu libro no se están cumpliendo

- **Severidad:** crítico · **Área:** G (Riesgos al apostar) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** El 8-nov quedaron escritas reglas de banca. Desde el 9-nov la mayoría de los boletos las rompe.
- **Evidencia:** Hoja «Reglas» del libro: máximo 7.500 por boleto, máximo 3 selecciones, exposición diaria máxima 60.000, tope de pérdida diaria 30.000. Boletos del 9 al 13-nov: 17 de 23 por encima de 7.500 (mediana 12.500, máximo 32.000); exposición de 143.000 el 12-nov y 111.375 el 13-nov; el 9-nov se perdieron 37.500. El boleto abierto del 14-nov es de 13.450 con 6 patas. Ni CLAUDE.md ni los informes mencionan estas reglas.
- **Por qué importa:** Sin ventaja demostrada, el tamaño de la apuesta es lo único que controla cuánto se pierde.
- **Qué hacer:** Decidir tú la regla de banca (unidad, máximo por boleto, tope diario y semanal) y escribirla en CLAUDE.md. Cada lectura de un boleto debe decir si la cumple.

#### A3 · «Cumple X de N» no separa nada una vez se mira el precio

- **Severidad:** alto · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** Las líneas que cumplen se dan más porque son más baratas, no porque el criterio vea algo que el precio no vea.
- **Evidencia:** Real menos probabilidad de mercado: «cumple» −4,1 puntos (IC −13,7 a +4,0, 213 líneas); «no cumple» +1,6 puntos (791 líneas). Por regularidad mínima de los dos equipos: 5 de 7 → −3,4 puntos; 6 de 7 → −4,3; 7 de 7 → −5,9 (ROI −7 % a −9 %). En la banda de mercado 70–80 %: «cumple» 60,5 % (n=43) contra «no cumple» 83,8 % (n=37).
- **Por qué importa:** Es el filtro central de fichas, ranking e informe. Viene de tipsters sin resultados verificados (lo dice CLAUDE.md) y la primera medición propia no lo respalda.
- **Qué hacer:** Mantener «X de N» como dato descriptivo. No usarlo como semáforo de sugerencia ni para ordenar hasta validarlo con una muestra nueva de al menos 50 partidos.

#### A4 · El «recorte de p» que añadí anoche no pasa la validación fuera de muestra

- **Severidad:** alto · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** El recorte de analisis_jornada.py empeora la probabilidad cuando se prueba en partidos que no usó para calcular los factores.
- **Evidencia:** Dejando un partido fuera cada vez (213 líneas con «cumple», 12 partidos): Brier con p cruda 0,1808, con p recortada 0,1964 (diferencia +0,0156, IC −0,0033 a +0,0309). Real 73,2 %, p cruda 77,5 %, p recortada 69,3 %: recorta de más. El sesgo por partido va de −38 a +25 puntos, y por jornada cambia de signo (12-nov noche +2 puntos; 13-nov −7).
- **Por qué importa:** El informe de anoche presenta la «p recortada» como la cifra prudente. Es un parche calculado con 12 partidos y aplicado dos veces (mercado-lado y banda de cuota).
- **Qué hacer:** Mostrar el «real hasta hoy» al lado de la p sin cambiar la p. Si se quiere un ajuste, un solo factor global con su intervalo, y solo cuando haya 50 partidos o más.

#### A5 · La muestra es mínima y las líneas del mismo partido no son independientes

- **Severidad:** alto · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** Las cifras que parecen grandes («17 de 20», «18 de 20») salen de muy pocos partidos.
- **Evidencia:** 1.460 líneas de equipo, pero 12 partidos; de 32 a 240 líneas por partido. Tiros al arco con «cumple»: 20 líneas de 3 partidos. Córners con «cumple»: 59 líneas de 10 partidos. Para distinguir un ROI real de +3 % de cero hacen falta unas 1.200 apuestas independientes a cuota 1,30 o unas 3.800 a cuota 1,90.
- **Por qué importa:** Casi todas las reglas vigentes se sacaron de esta muestra.
- **Qué hacer:** Reportar siempre el número de partidos, no solo el de líneas, y los intervalos por partido. No crear reglas nuevas con menos de 30 partidos.

#### A6 · No se mide la cuota de cierre (CLV)

- **Severidad:** alto · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** La columna existe y nunca se ha llenado. Tampoco «apostada» ni «stake».
- **Evidencia:** registro/lineas.csv: cuota_cierre, apostada y stake vacías en las 18.097 filas. El modelo ya trae el mecanismo (`python3 -m supermodelo --cerrar … cierres.json`, probado en test_modelo.py) y no se usa.
- **Por qué importa:** Ganarle a la cuota de cierre es la única señal de ventaja que se puede ver en semanas; el ROI necesita miles de apuestas.
- **Qué hacer:** Releer la cuota de cada línea sugerida o apostada unos 10 minutos antes del partido y guardarla. Reportar el CLV medio por partido en cada balance.

#### A9 · Mercados de jugador: muy negativos en lo poco medido

- **Severidad:** alto · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** En los 4 partidos con estadística por jugador, las líneas se dieron la mitad de lo que decían modelo y precio.
- **Evidencia:** 1.875 líneas calificadas: 11,4 % real contra 23,0 % del modelo; ROI −71 % (IC por partidos −80 % a −66 %). Solo jugadores con 60 minutos o más (1.230): ROI −58 %. Titulares probables con cuota menor a 1,50 (104): 61 % real contra 79 % implícito. Remates 1+ de titulares: 49 % contra 68 %. La suma de remates por jugador coincide con el total del equipo en los 4 partidos, así que la calificación es correcta. El modelo supone un margen de 12 % (VIG_JUGADOR) y, sin dato, titular 0,85 y 82 minutos.
- **Por qué importa:** Varias patas de jugador tumbaron boletos tuyos; el modelo copia la cuota y no descuenta el margen real de estas escaleras.
- **Qué hacer:** No sugerir líneas de jugador hasta tener historial por jugador y unos 20 partidos medidos. Medir el margen real por escalón y corregir el supuesto de titular por defecto.

#### B1 · Por diseño, el modelo es un espejo del precio

- **Severidad:** alto · **Área:** B (Modelo (supermodelo/)) · **Veredicto:** MANTENER · **Esfuerzo:** S
- **Qué pasa:** Las medias de cada estadística se leen de la escalera de Betano y la probabilidad final se mezcla 50/50 con el precio. Solo el contexto puede moverla, y el contexto está sin leer.
- **Evidencia:** supermodelo/config.py: W_MODELO_MEDIA = 0.0 y W_MERCADO = 0,50 por familia. supermodelo/analizar.py: construir_objetivos() toma media_mercado(). Jornada del 14-nov: situación «sin leer» en 21 de 21 partidos.
- **Por qué importa:** Es una decisión honesta y documentada (el mercado calibra mejor que los promedios), pero convierte al modelo en una herramienta de coherencia, no de valor. Los informes lo siguen presentando como fuente de valor.
- **Qué hacer:** Conservar el simulador para conjuntas, guiones y en vivo. Dejar de reportar EV, «valor» y cuota mínima por línea.

#### C2 · Volver a correr una jornada borra sus resultados

- **Severidad:** alto · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** El registro reemplaza todas las filas de la jornada por filas nuevas con resultado vacío.
- **Evidencia:** recoleccion/registrar_jornada.py, registrar(): conserva solo las filas de otras jornadas y escribe las nuevas sin resultado, apostada ni cuota de cierre. correr_jornada.py lo llama siempre.
- **Por qué importa:** Una corrida después de calificar deja la jornada sin resultados y obliga a calificar otra vez.
- **Qué hacer:** Unir por clave de línea y conservar resultado, apostada, stake y cuota de cierre. Añadir una prueba.

#### C3 · Extractores atados a interfaces internas de Betano y Flashscore

- **Severidad:** alto · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** Leen direcciones internas de las páginas y clasifican los mercados por su nombre en español.
- **Evidencia:** recoleccion/betano_extraer.js: `/api/cuotas-de-partido/…?bt=12` con cambio de pestaña según el partido y una lista de exclusiones por expresión regular; ya se colaron dos mercados (córners por equipo y tiempo, tarjetas 1T). recoleccion/flashscore_extraer.js: cabecera `x-fsign` fija. Sofascore respondió 403. No hay ninguna prueba sobre los dos extractores.
- **Por qué importa:** Un cambio de nombre o de pestaña mete líneas equivocadas sin avisar; un bloqueo deja la jornada sin datos. Además conviene revisar los términos de uso de cada sitio.
- **Qué hacer:** Guardar una respuesta real de cada sitio como muestra de prueba, validar cada escalera (cuotas monótonas, línea única por ámbito) y abortar con un mensaje claro si el esquema cambia.

#### D1 · El registro de líneas no escala

- **Severidad:** alto · **Área:** D (Datos y registro) · **Veredicto:** RECONSTRUIR · **Esfuerzo:** M
- **Qué pasa:** Un solo CSV recibe todas las líneas de cada jornada y se reescribe completo.
- **Evidencia:** registro/lineas.csv: 4,75 MB y 18.097 filas con 3 jornadas; la del 14-nov aporta 12.232, de las cuales 9.139 (75 %) son de jugador sin historial y 946 de 1T/2T sin ficha. Cada corrida cambia hasta 36.196 líneas en git.
- **Por qué importa:** A una jornada diaria son unas 370.000 filas y 100 MB en un mes; los diffs dejan de servir.
- **Qué hacer:** Un archivo por jornada, registrar solo las líneas con ficha (o guardar las de jugador aparte) y mantener un índice chico de lo sugerido y apostado.

#### D2 · El repo crece unos 20 MB por jornada con archivos que se pueden regenerar

- **Severidad:** alto · **Área:** D (Datos y registro) · **Veredicto:** ELIMINAR · **Esfuerzo:** S
- **Qué pasa:** Se versionan los resultados completos del modelo y copias de HTML con todos los datos dentro.
- **Evidencia:** jornadas/2026-11-14/informes: 63 archivos, 18,2 MB (hasta 1,48 MB por partido). entregas/: 7,2 MB en 15 archivos, tres de ellos de 1,4 a 2,1 MB. Total versionado: 44,9 MB en jornadas tras 5 días.
- **Por qué importa:** En dos meses el repo pasa de 1 GB y cada clon y cada sesión se vuelven lentos.
- **Qué hacer:** Sacar del versionado los *_resultado.json y los informes por partido (se regeneran con la entrada). En entregas, guardar el HTML sin los datos embebidos o comprimido.

#### E1 · Las reglas están en siete sitios y se contradicen

- **Severidad:** alto · **Área:** E (Flujo y organización) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** Cada documento cuenta una versión distinta del criterio.
- **Evidencia:** .claude/agents (6 archivos) dicen «≥ 7 de 10» fijo aunque la jornada sea de 7; corners.md y jugadores.md apuntan a `pub/entradas/`, que no existe. criterios/README.md dice «5 de 7». README.md habla de Sofascore y de 3 agentes. GUIA_RAPIDA.md y MODELO_README.md describen `--registro` y `--cerrar`, que ya no se usan. Las 13 reglas del libro y las 6 de la auditoría no están en CLAUDE.md.
- **Por qué importa:** Cada sesión nueva puede seguir una regla distinta; anoche hubo que explicarle a cada agente que la muestra era de 7.
- **Qué hacer:** Un solo archivo de reglas numeradas y fechadas, citado desde CLAUDE.md, agentes y skills. Borrar o actualizar el resto.

#### G2 · El resultado depende de dos boletos; los patrones que más pierden siguen activos

- **Severidad:** alto · **Área:** G (Riesgos al apostar) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** El balance en cero esconde caídas grandes.
- **Evidencia:** Caída máxima desde un pico: −$326.399. Cuota de 5,00 a 9,99: 24 boletos, 3 ganados, −$337.693 (ROI −62 %). Stake de más de 8 u: 0 de 7, −$298.095. En vivo (4–8 nov): 3 de 13, −$95.370 (ROI −41 %). Boletos de 3 selecciones: 3 de 16, −$137.054.
- **Por qué importa:** Son los mismos tipos de boleto del ticket abierto (cuota 7,60, combinada).
- **Qué hacer:** Mientras dure la medición: solo sencillas, cuota menor a 3, 1 u.

#### G3 · El informe ofrece volumen aunque diga que no hay valor

- **Severidad:** alto · **Área:** G (Riesgos al apostar) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** Anoche el informe decía que ninguna sugerencia tenía EV positivo y aun así listaba 58, con cupón y «lotería».
- **Evidencia:** entregas/2026-11-13/2310_informe-jornada-14nov.html: 12.232 líneas, 446 que cumplen, 38 protecciones, 15 sencillas, 4 combinadas y 1 lotería; mejor EV −8 %.
- **Por qué importa:** Una lista larga de líneas «probables» empuja a apostar más, no mejor.
- **Qué hacer:** Cuando no hay ventaja, el informe debe abrir con «hoy no hay apuesta con valor» y mostrar como mucho cinco líneas de lectura, sin cupón ni lotería.

### Lo que se puede mejorar (medios y bajos)

#### A10 · El margen de Betano es la valla que hay que saltar

- **Severidad:** medio · **Área:** A (Método y estadística) · **Veredicto:** MANTENER · **Esfuerzo:** S
- **Qué pasa:** Cada línea de dos lados trae alrededor de 7 % de margen; en goles, 5,7 %.
- **Evidencia:** Jornada del 14-nov, pares Más/Menos: córners 7,0 % (423 pares), tarjetas 7,0 %, tiros al arco 7,0 %, remates 7,0 %, goles 5,7 % (596 pares).
- **Por qué importa:** Para no perder hay que acertar unos 3,5 puntos más de lo que dice el precio en cada pata; en una combinada de dos patas, el margen ronda 13 %.
- **Qué hacer:** Poner el margen de cada mercado a la vista en el informe y descartar por defecto las combinadas.

#### A7 · Reglas sacadas y aplicadas sobre los mismos datos

- **Severidad:** medio · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** Hay 13 reglas en el libro (8-nov), 6 de la auditoría (13-nov) y el recorte (14-nov), todas derivadas del periodo 4–13 nov y sin periodo de prueba posterior.
- **Evidencia:** registro/libro_apuestas.xlsx hoja «Reglas»; CLAUDE.md sección «Análisis»; recoleccion/analisis_jornada.py. Ejemplo: «base de combinada: tarjetas Menos 5/5» (regla 9 del libro) contra tarjetas Menos con «cumple» 7 de 15 una semana después.
- **Por qué importa:** Con muestras tan chicas, la regla que mejor se ve hacia atrás suele ser ruido.
- **Qué hacer:** Congelar las reglas hoy, numerarlas en un solo lugar y evaluarlas solo con partidos posteriores a la fecha en que se escribieron.

#### A8 · La muestra de la ficha mezcla competiciones y fechas viejas

- **Severidad:** medio · **Área:** A (Método y estadística) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** Los 7 partidos por equipo no se ajustan por rival, sede ni competición.
- **Evidencia:** Entradas del 14-nov: 294 partidos de muestra; 61 son del Mundial y 56 de Nations League; antigüedad mediana 40 días, máxima 499; 38 tienen más de 180 días. El esperado es (a favor + en contra del rival)/2 sin ponderar.
- **Por qué importa:** En selecciones, 7 partidos oficiales cubren más de un año y rivales muy distintos.
- **Qué hacer:** Declarar en la ficha el rango de fechas y la competición de la muestra; ponderar por antigüedad o, al menos, marcar la muestra con más de 180 días.

#### B2 · La alerta «la simulación se aleja del mercado» dice otra cosa de la que parece

- **Severidad:** medio · **Área:** B (Modelo (supermodelo/)) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** El texto sugiere una línea mal copiada. En realidad salta donde la forma del simulador no coincide con Betano.
- **Evidencia:** analizar.py: alerta si |p sin contexto − mercado| ≥ 0,15. El 14-nov saltó en 7 de 21 partidos, siempre en «más córners que», córners y saques de banda. En lo calificado, los desvíos de 3 puntos o más se concentran en córners 2T (68 de 96 líneas), tarjetas total (32 de 46) y remates total (24 de 36).
- **Por qué importa:** Genera ruido y se interpreta como error de datos; el problema es el reparto por tiempos y por equipo del simulador.
- **Qué hacer:** Cambiar el mensaje a «el simulador no reproduce este mercado» y recalibrar el reparto por tiempos de córners y tarjetas, o sacar esas familias del cálculo.

#### B3 · Los «builders» muestran un EV que Betano no paga

- **Severidad:** medio · **Área:** B (Modelo (supermodelo/)) · **Veredicto:** ELIMINAR · **Esfuerzo:** S
- **Qué pasa:** El campo ev_si_paga_producto sale positivo porque supone que el cupón paga el producto de las cuotas.
- **Evidencia:** analizar.py armar_builders(): ejemplo Portugal–Dinamarca, +6,3 % y +13,9 %. Auditoría de sugerencias: combinadas del mismo partido 9 de 29 (31 % contra 47 % dicho).
- **Por qué importa:** Es una invitación a combinar con un precio que no existe.
- **Qué hacer:** Quitar el campo de los informes, o mostrarlo solo cuando se dé la cuota real del cupón.

#### B4 · Hay un segundo registro con CLV dentro del modelo que no se usa

- **Severidad:** medio · **Área:** B (Modelo (supermodelo/)) · **Veredicto:** RECONSTRUIR · **Esfuerzo:** M
- **Qué pasa:** El paquete trae su propio registro, balance y medición en sombra; el flujo actual los reinventó en recoleccion/.
- **Evidencia:** supermodelo/registro.py (437 líneas), balance.py (174), sombra.py (114), perfiles.py (150, peso 0) y lectores.py (69, nadie lo importa): 944 de 5.032 líneas. datos/partidos.csv, la base propia que alimenta ligas.prior(), no existe. GUIA_RAPIDA.md y MODELO_README.md siguen describiendo ese flujo.
- **Por qué importa:** Dos sistemas de registro confunden y el que sabe medir el cierre está apagado.
- **Qué hacer:** Decidir uno: o se adopta `--cerrar` (con cuota de cierre) como forma de calificar, o se archiva y se lleva esa función a recoleccion/.

#### C4 · Un jugador que no casa por nombre se califica como «no jugó»

- **Severidad:** medio · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** El calificador marca «nula» cuando no encuentra el nombre, igual que si el jugador no hubiera jugado.
- **Evidencia:** recoleccion/calificar_jugadores.py: casar() exige parecido ≥ 0,8; si no, resultado = «nula» y nota «no jugó». 862 líneas nulas en el registro.
- **Por qué importa:** Un nombre mal emparejado desaparece de la medición sin dejar rastro.
- **Qué hacer:** Separar «sin casar» de «no jugó» y listar los nombres sin casar al final.

#### C5 · Resultados y estadísticas por jugador se recogen a mano

- **Severidad:** medio · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** No hay script en el repo para traer el resultado final ni la estadística por jugador.
- **Evidencia:** jornadas/2026-11-13/balance/jugadores_resultado.txt y resultados_completos.json se armaron en la sesión; la búsqueda de los campos de Sofascore en el repo no devuelve nada.
- **Por qué importa:** La calificación depende de repetir a mano el mismo trabajo cada día.
- **Qué hacer:** Añadir el extractor de resultados y de jugadores al mismo script local de recolección.

#### C6 · Cuotas viejas y alineaciones sin releer

- **Severidad:** medio · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** El análisis usa cuotas leídas la tarde anterior y alineaciones probables.
- **Evidencia:** Jornada del 14-nov: cuotas leídas el 13-nov de 19:01 a 19:15 para partidos hasta las 20:00 del 14; alineaciones probables en 16 de 21; sin árbitro en 3; sin estadísticas de árbitro en ninguno.
- **Por qué importa:** La regla de releer una hora antes existe y no tiene automatización.
- **Qué hacer:** Una segunda lectura corta por partido (cuota y XI oficial), que además sirve para registrar el cierre.

#### D3 · Datos repartidos en formatos que no cuadran entre sí

- **Severidad:** medio · **Área:** D (Datos y registro) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** La misma información vive en varios sitios con convenciones distintas.
- **Evidencia:** Unidad: 3.700 COP en CLAUDE.md e informe_html.py; 3.750 en el libro y en sus reglas de stake. Hoja «Banca» del libro: solo hasta el 8-nov. Tres registros de líneas (historial_lineas.csv, lineas.csv, sugerencias.csv). Tu boleto del 14 está en un JSON aparte. Dos partidos del 13-nov siguen sin ninguna línea calificada.
- **Por qué importa:** Cada balance obliga a reconciliar a mano.
- **Qué hacer:** Fijar la unidad, llevar los boletos en un solo archivo de texto por jornada y regenerar el libro desde ahí.

#### E2 · Los agentes por mercado repiten lo que ya calcula el pipeline

- **Severidad:** medio · **Área:** E (Flujo y organización) · **Veredicto:** RECONSTRUIR · **Esfuerzo:** S
- **Qué pasa:** Devuelven tablas que ya están en el registro; aportan cuando revisan, no cuando listan.
- **Evidencia:** Anoche: 5 agentes, unos 223.000 tokens. Córners, partido, goles y tarjetas entregaron las líneas que cumplen (ya en lineas.csv). Lo útil fue la revisión de Mirassol–Atlético-MG y la de combinadas. El agente «jugadores» no puede trabajar sin historial.
- **Por qué importa:** Coste y tiempo sin información nueva.
- **Qué hacer:** Dejar un agente revisor que busque errores y un agente de combinadas. Suspender «jugadores» hasta tener historial.

#### E3 · El ranking apto / reserva no filtra nada

- **Severidad:** medio · **Área:** E (Flujo y organización) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** Sin la lectura de situación, ningún partido llega a «apto».
- **Evidencia:** jornadas/2026-11-14/ranking.md: 21 de 21 en «reserva» con situación «sin leer»; recoleccion/puntuar.py (195 líneas) calcula un puntaje que no cambia ninguna decisión.
- **Por qué importa:** Se mantiene código y un paso del flujo que no decide.
- **Qué hacer:** O se escriben las notas de situación antes del análisis, o se simplifica el ranking a «datos completos sí/no».

#### F2 · Las pruebas cubren la mecánica, no lo que más falla

- **Severidad:** medio · **Área:** F (Ingeniería y seguridad) · **Veredicto:** ARREGLAR · **Esfuerzo:** M
- **Qué pasa:** Pasan 200 comprobaciones, pero ninguna toca los extractores ni la calificación de punta a punta.
- **Evidencia:** test_modelo.py 106 (52 s), test_ficha.py 27, test_betano.py 11, test_recoleccion.py 56. Cero pruebas sobre betano_extraer.js y flashscore_extraer.js. test_recoleccion.py lee jornadas/2026-11-13 y registro/sugerencias.csv reales: si esos datos cambian, la prueba cambia. No hay integración continua (.github no existe).
- **Por qué importa:** Los dos errores de lectura de mercados se descubrieron en producción.
- **Qué hacer:** Muestras fijas para los extractores, una prueba de «recolectar → registrar → calificar» con datos de juguete y correr las pruebas en cada push.

#### G4 · Combinadas y Bet Builder: se paga el margen varias veces

- **Severidad:** medio · **Área:** G (Riesgos al apostar) · **Veredicto:** ELIMINAR · **Esfuerzo:** S
- **Qué pasa:** El precio real del cupón no se conoce y el historial es malo.
- **Evidencia:** Margen por pata cercano a 7 %: cerca de 13 % en dos patas y de 18 % en tres. Sugerencias auditadas: combinadas del mismo partido 9 de 29; de 2 patas 7 de 21; de 3 patas 5 de 21.
- **Por qué importa:** Es el formato que más usas y el que peor rinde.
- **Qué hacer:** Sacarlas del informe por defecto; evaluarlas solo si das la cuota real del cupón.

#### G5 · No hay control de banca desde el 9-nov

- **Severidad:** medio · **Área:** G (Riesgos al apostar) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** No se sabe cuánto se ha depositado ni el saldo desde esa fecha.
- **Evidencia:** Hoja «Banca»: 2 depósitos por $100.000 y movimientos solo del 4 al 8-nov. Unidad sin fijar (3.700 o 3.750).
- **Por qué importa:** Sin banca no se puede fijar un stake ni un tope de pérdida con sentido.
- **Qué hacer:** Anotar depósitos, retiros y saldo en cada balance. Betano permite fijar límites de depósito y de pérdida en la cuenta; es una herramienta útil si la quieres usar.

#### B5 · Multiplicadores de contexto sin medir

- **Severidad:** bajo · **Área:** B (Modelo (supermodelo/)) · **Veredicto:** MANTENER · **Esfuerzo:** S
- **Qué pasa:** Derbi, importancia, clima, bajas y rotación mueven las medias con valores de partida.
- **Evidencia:** config.py: FUERZA_CONTEXTO, CALIDAD_REEMPLAZO, clima ×0,96 por frío; el propio archivo dice «puntos de partida sin medir». Tope de ±10 %.
- **Por qué importa:** El efecto está acotado y documentado; el riesgo es darlo por cierto.
- **Qué hacer:** Mantener con el tope y medir cada hecho cuando haya muestra.

#### C7 · Scripts de una sola sesión dentro del repo

- **Severidad:** bajo · **Área:** C (Recolección (recoleccion/)) · **Veredicto:** ELIMINAR · **Esfuerzo:** S
- **Qué pasa:** Hay generadores que solo usó una entrega.
- **Evidencia:** recoleccion/informe_completo.py (465 líneas) solo lo importan jornadas/2026-11-13/herramientas_sesion/*.py; jornadas/2026-11-12/_scripts_legacy (11 archivos con rutas viejas).
- **Por qué importa:** Ocupan y confunden a la siguiente sesión.
- **Qué hacer:** Moverlos a una carpeta de archivo o borrarlos.

#### D4 · Restos de sesiones viejas

- **Severidad:** bajo · **Área:** D (Datos y registro) · **Veredicto:** ELIMINAR · **Esfuerzo:** S
- **Qué pasa:** Quedan paquetes y carpetas de prueba.
- **Evidencia:** jornadas/2026-11-12/pub/sm_paquete.b64.txt (286 KB, un paquete comprimido en base64), jornadas/2026-11-12/ranking_prueba, jornadas/2026-11-13/herramientas_sesion, partidos/ (2,6 MB del 11 y 12-nov), ejemplos/9nov.
- **Por qué importa:** Ruido para quien abre el repo.
- **Qué hacer:** Borrar o mover a una carpeta de archivo.

#### E4 · Entregas guardadas por fecha de entrega, no por jornada

- **Severidad:** bajo · **Área:** E (Flujo y organización) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** El informe de la jornada del 14 quedó en la carpeta del 13.
- **Evidencia:** entregas/2026-11-13/2310_informe-jornada-14nov.html; la tarea programada anterior lo buscaba en entregas/2026-11-14/.
- **Por qué importa:** Es fácil no encontrarlo o duplicarlo.
- **Qué hacer:** Añadir la jornada al nombre de la carpeta o una columna «jornada» en INDICE.md.

#### F1 · Sin credenciales en el repo; hay datos de tus apuestas

- **Severidad:** bajo · **Área:** F (Ingeniería y seguridad) · **Veredicto:** MANTENER · **Esfuerzo:** S
- **Qué pasa:** No aparecen claves, tokens ni cookies. Sí están los códigos de tus boletos y los montos.
- **Evidencia:** Búsqueda de patrones de clave y token en los archivos versionados: sin resultados reales (un paquete en base64 y la palabra «tokens» en un comentario). Repo privado. Códigos de boleto de 11 dígitos en 5 archivos; montos y stakes en el libro y en los balances. Sin imágenes ni capturas versionadas.
- **Por qué importa:** En privado es aceptable; no conviene hacer público el repo tal como está.
- **Qué hacer:** Mantenerlo privado. Si algún día se comparte, quitar antes registro/ y entregas/.

#### F3 · Dependencias sin versión y calibración no reproducible desde el repo

- **Severidad:** bajo · **Área:** F (Ingeniería y seguridad) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** requirements.txt no fija versiones y los datos de la calibración no están.
- **Evidencia:** requirements.txt: «numpy» y «scipy». openpyxl y pandas se usan sin declararse. pruebas/calibracion: Matches.csv se descarga aparte y dos scripts leen /home/claude/…
- **Por qué importa:** Un cambio de versión puede mover probabilidades; las cifras de config.py no se pueden volver a comprobar.
- **Qué hacer:** Fijar versiones, declarar openpyxl y dejar un script que descargue los datos y repita las tablas de docs/CALIBRACION_10NOV.md.

#### F4 · Errores que se tragan en silencio

- **Severidad:** bajo · **Área:** F (Ingeniería y seguridad) · **Veredicto:** ARREGLAR · **Esfuerzo:** S
- **Qué pasa:** Algunos bloques capturan cualquier error y siguen.
- **Evidencia:** recoleccion/informe_html.py:46, supermodelo/registro.py:262 y 279, recoleccion/informe_completo.py:129, 212 y 338.
- **Por qué importa:** Un archivo roto se convierte en un dato vacío sin aviso.
- **Qué hacer:** Registrar el error con el nombre del archivo.

### Lo que está bien

#### H1 · No se inventan datos y los límites se declaran

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** Lo que falta se dice en la ficha, el estado y el informe.
- **Evidencia:** ESTADO.md de cada jornada; «sin estadística por tiempo», «sin alineación», «árbitro sin publicar»; armar_entrada.py deja vacío lo que no hay.
- **Por qué importa:** Es la base para poder confiar en cualquier medición posterior.
- **Qué hacer:** No tocar.

#### H2 · Las sugerencias se registran antes del partido y se califican pata por pata

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** Hay 394 sugerencias con su probabilidad dicha y su resultado.
- **Evidencia:** registro/sugerencias.csv; recoleccion/sugerencias.py; las 58 del 14-nov quedaron «pendiente» y se califican solas.
- **Por qué importa:** Gracias a esto se pudo ver que las combinadas se daban 31 % y no 47 %.
- **Qué hacer:** No tocar; ampliarlo con la cuota de cierre.

#### H3 · El libro de apuestas con tus 77 boletos reales

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** Cada boleto con stake, cuota, resultado y diagnóstico.
- **Evidencia:** registro/libro_apuestas.xlsx: hojas Boletos, Selecciones, Banca, Lecciones y Reglas.
- **Por qué importa:** Es el único dato de dinero real y permitió esta auditoría.
- **Qué hacer:** Mantenerlo al día; es más importante que cualquier informe de jornada.

#### H4 · La calibración con 238.858 partidos y la decisión de anclar al mercado

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** El modelo se contrastó con datos públicos y se aceptó que el precio calibra mejor que los promedios.
- **Evidencia:** docs/CALIBRACION_10NOV.md; config.py con la fuente de cada constante; los sistemas de tipsters probados con cuotas reales dieron casi todos un ROI de −3 % a −7 %.
- **Por qué importa:** Evita creer en ventajas que no existen. El propio repo ya decía lo que confirma esta auditoría.
- **Qué hacer:** No tocar.

#### H5 · Pruebas automáticas y resultados reproducibles

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** 200 comprobaciones pasan en cerca de un minuto y la simulación usa semilla fija.
- **Evidencia:** pruebas/test_*.py; SEED = 7 y N_SIM = 20.000 en config.py.
- **Por qué importa:** Permite cambiar código sin romper lo anterior.
- **Qué hacer:** No tocar; ampliarlas (ver F2).

#### H6 · Dos etapas y un pipeline corto

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** Recolección con navegador y análisis sin red, en 3,5 minutos para 21 partidos.
- **Evidencia:** recoleccion/correr_jornada.py; «si falta, lo dice y no inventa».
- **Por qué importa:** El análisis se puede repetir y programar.
- **Qué hacer:** No tocar la separación.

#### H7 · El simulador da probabilidades conjuntas con dependencia medida

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** Sirve para ver cuánto vale de verdad una combinada.
- **Evidencia:** supermodelo/simulador.py, combos.py y dependencia.py; correlaciones contrastadas con 62.164 partidos.
- **Por qué importa:** Es justo lo que mostró que las combinadas no pagan lo que arriesgan.
- **Qué hacer:** No tocar.

#### H8 · Informe interactivo autónomo y trazabilidad de entregas

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** Un HTML sin red con filtros, más índice y bitácora de todo lo entregado.
- **Evidencia:** recoleccion/informe_html.py; entregas/INDICE.md; registro/BITACORA.md.
- **Por qué importa:** Se puede reconstruir qué se dijo cada día y con qué datos.
- **Qué hacer:** No tocar la base; adelgazar el contenido (ver G3 y D2).

#### H9 · Claude no apuesta ni entra a Betano

- **Severidad:** bien · **Área:** H (Lo que está bien) · **Veredicto:** MANTENER · **Esfuerzo:** —
- **Qué pasa:** La separación entre analizar y apostar se respeta.
- **Evidencia:** CLAUDE.md; la sesión de Betano caducada no se reabrió; el boleto del 14 se leyó de una captura tuya.
- **Por qué importa:** Mantiene el control y la responsabilidad donde deben estar.
- **Qué hacer:** No tocar.

## Plan priorizado

### Antes de la próxima jornada

1. Decidir y escribir en CLAUDE.md la regla de banca: unidad, máximo por boleto, tope diario y semanal (G1, G5).
2. Arreglar el registro para que volver a correr una jornada no borre resultados (C2).
3. Quitar «valor», «EV del modelo» y la «p recortada» de los informes; usar la probabilidad del mercado sin margen y mostrar el «real hasta hoy» al lado (A2, A4, B3).
4. Releer y guardar la cuota unos 10 minutos antes del partido para lo sugerido y lo apostado (A6, C6).
5. Informe corto: si no hay ventaja, decirlo arriba; como mucho cinco líneas de lectura, sin jugadores, sin combinadas, sin lotería (G3, G4, A9).

### Qué reconstruir, en este orden

1. Recolección local por script, sin transcripción por el chat (C1, C5).
2. Registro por jornada con cuota de cierre, y un solo sistema de calificación (D1, A6, B4).
3. Repo liviano: fuera los resultados completos del modelo y los HTML con datos embebidos (D2, D4).
4. Una sola fuente de reglas, numeradas y fechadas (E1, A7).
5. Agentes: un revisor y uno de combinadas; el resto se suspende (E2, E3).

### Qué no tocar

1. El simulador, config.py y la calibración con datos públicos.
2. Las pruebas automáticas.
3. El registro previo de sugerencias y su calificación pata por pata.
4. El libro de apuestas y la regla de no inventar datos.

### Qué medir en las próximas 2 o 3 semanas

1. Antes de empezar, dejar por escrito qué se va a apostar: de 3 a 5 sencillas por día, 1 u fija, sin combinadas ni en vivo.
2. Medida principal: CLV medio (cuota tomada contra cuota de cierre), con intervalo por partido. Con unas 100 a 300 apuestas en 100 partidos ya se puede leer.
3. Medida secundaria: calibración por tramos contando partidos, no líneas.
4. El ROI se anota pero no decide: harían falta entre 1.200 y 3.800 apuestas independientes.
5. Condición de parada: si tras 100 partidos el CLV medio no es mayor que cero, el método no tiene ventaja y lo razonable es parar o dejarlo como entretenimiento con un tope fijo.

## Límites de esta auditoría

- El clon es superficial (58 commits desde el 12-nov); no se revisó el historial anterior ni las otras ramas.
- No se abrieron los JSON crudos de flashscore/ ni betano/ (solo su esquema y tamaños), como pide CLAUDE.md.
- No se ejecutaron los extractores contra Betano ni Flashscore: esta sesión no tiene navegador. Se leyó su código.
- Las cifras de rendimiento salen de 12 partidos de equipo y 4 de jugador: sirven para decir que no hay evidencia de ventaja, no para probar que no existe.
- El libro se leyó con sus fórmulas sin calcular; los totales se recalcularon desde las filas (coinciden con la bitácora: 71 boletos, −$1.925).
- La hoja «Banca» solo llega al 8-nov; no se conocen depósitos ni saldo posteriores.
- De supermodelo/ se leyeron completos config, simulador, analizar, mercado, jugadores, combos y ejecutar; del resto, la estructura, los usos y las pruebas.
- No se revisaron los términos de uso de Betano ni de Flashscore; solo se señala que conviene hacerlo.
