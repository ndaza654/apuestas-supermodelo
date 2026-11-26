# Recolección de datos · 4 partidos de la noche del 26-nov

Fecha y hora: 26-nov-2026 ~16:50 Bogotá. Fuente y hora de las cuotas: Betano, leídas 15:54 Bogotá (una sola lectura). Contenido: copia íntegra de `jornadas/2026-11-26-noche/ESTADO.md` (datos en esa carpeta).


Recolección de etapa 1 pedida por el usuario el 26-nov 15:52 (Bogotá) para los 4 partidos de la noche. Una sola lectura de cuotas (Betano 15:54 Bogotá); sin relectura 1 h antes.

| Partido | Hora (Bogotá) | Fase | Betano: mercados | Sofascore | Árbitro | Notas / guion |
|---|---|---|---|---|---|---|
| São Paulo – Remo | 18:00 | Brasileirão, fecha 37 | goles, córners, tarjetas, remates, tiros al arco, resultado, ambos, hándicap + 54 jugadores (an/aoa/tj/as/sh/sot) | 10/10 + 10/10, directos 1 (Remo recién ascendido), once probable | Bruno Arleu de Araujo (ValueStats leído) | sí |
| Pachuca – Chivas | 20:00 | Liguilla, cuartos, ida | idem + 61 jugadores | 10/10 + 10/10, directos 6, once probable | Fernando Hernández Gómez (ValueStats leído; solo 26 partidos) | sí |
| Montevideo City Torque – Nacional | 19:30 | Copa AUF Uruguay, semifinal a partido único (Durazno) | solo goles, córners, resultado, ambos, hándicap, descanso/final: **sin tarjetas, remates ni jugadores** | 10/10 + 10/10 (7 de 10 con estadísticas por jugador), directos 6, **sin once** | Bruno Sacarelo (anunciado; **sin estadísticas leídas**) | sí |
| León – Cruz Azul | 22:10 | Liguilla, cuartos, ida | idem + 67 jugadores | 10/10 + 10/10, directos 6, once probable | César Arturo Ramos Palazuelos (ValueStats leído) | sí |

## Historial de jugadores (regla de recolección)
Hecho para los 3 partidos con mercado de jugador de estadística (São Paulo–Remo, Pachuca–Chivas, León–Cruz Azul) con **Sofascore** (fuente principal desde el 25-nov): 10 de 10 partidos por equipo, 24–30 jugadores por equipo, todas las columnas del feed (minutos, remates, a puerta, goles, asistencias, tarjetas, entradas, faltas cometidas y recibidas, centros, xA, rating). Cobertura en `jugadores_sofascore/LEEME.md`. Montevideo City–Nacional no ofrece mercados de jugador: no lo necesita (queda el historial de referencia, 7 de 10).

## Límites declarados
- Una sola lectura de cuotas (15:54); sin relectura cercana al partido ni onces oficiales (solo probables de Sofascore). Reconfirmar onces ~1 h antes (Bobadilla de São Paulo figura en el once probable aunque noticias previas lo daban con su selección).
- Montevideo City–Nacional: Betano no ofrece tarjetas, remates ni jugadores; Sofascore no publicó once; árbitro sin historial; sede neutral (Durazno): el «local» de Betano no juega en su estadio. Los mercados son de 90 minutos.
- Árbitros: penales y porcentajes de +3,5/+4,5/+5,5 de la muestra de 20 no se leyeron (texto colapsado en ValueStats). Fernando Hernández: solo 26 partidos registrados.
- Tabla de Remo sin confirmar (Terra: 19.º, descendido; ArqTricolor la daba 17.º con 32 pts): no se usa como dato duro. Fecha de São Paulo–Remo confirmada para hoy (Betano, ValueStats, Terra, O Tempo, Lance); un portal listaba el 28-nov (dato viejo).
- Flashscore no se usó en esta recolección (Sofascore principal); el contraste Sofascore–Flashscore no se hizo. «Entradas» de Sofascore no equivalen a las de Betano. Los datos pasaron transcritos por el chat (Sofascore verificado con hash sha256 943267c8…; los textos de Betano sin hash).
- Notas de contexto y guion escritos con tabla/bajas leídas en medios (hora en cada nota) y datos de las fichas; los criterios de mercado son de tipsters sin verificar. No se pidió análisis: `analisis.json`/`informe.html` salieron del pipeline automático, sin «Enfoque de mercados» ni sugerencias enviadas (no se tocó `registro/sugerencias.csv`).
- Liga MX: Betano trae mercados de jugador solo en parte de los partidos: aquí sí (54–67 jugadores, escaleras válidas, sin avisos).
