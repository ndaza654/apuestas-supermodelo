# Mantenimiento: cuotas de jugador inventadas (25-nov-2026, 15:10 Bogotá)
Fuente: repo y Betano (lectura del 25-nov ~15:00); sin cuotas nuevas para apostar. Límite: las cuotas de 22–25-nov ya jugadas no se pueden releer.

**Qué viste:** «Julián Álvarez · Remates 1+ @3,20 · 28 %», «Carlos Forbs · Remates 1+ @2,25». Esas líneas no existen en Betano (Álvarez empieza en 5+ a 1,45; tiros al arco, tarjeta 1T @1,53 sí es real).
**Por qué pasó:** desde ~22-nov Betano entrega los mercados de jugador como UNA tabla por mercado con todos los jugadores; el extractor la leía como la escalera del primer jugador y juntaba ~39 escaleras en una; al decodificar, la última cuota de cada línea ganaba. Resultado: líneas «1+» con cuotas de otros jugadores.
**Qué se arregló:** extractor (una escalera por fila de la tabla), decodificador (descarta escaleras con líneas repetidas o precio que baja, y lo avisa), pruebas con respuesta real simulada (17 de test_betano), y verificado en vivo (Atlético–Viking: 46 jugadores, 0 avisos).
**Datos limpiados:** 22–25-nov: 414 escaleras / 1.623 filas quitadas de `registro/lineas.csv` (copia en `registro/lineas_invalidas.csv`; una estaba apostada —David Soria, atajadas 3—, se conserva con nota). 26-nov: 36 partidos releídos, 0 escaleras inválidas; 22.554 líneas de jugador.
**Qué cambia para ti:** no hay sugerencias ni boletos tuyos afectados salvo esa pata; las calibraciones de jugador de balances anteriores usaban líneas contaminadas: se vuelven a medir. Los combos BB de PSG–Roma usaron precio real de Betano (`mc-leg`): no afectados.
