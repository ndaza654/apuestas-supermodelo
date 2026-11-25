# Estrategias por mercado (qué se lee para analizar cada mercado de un partido)

Una ficha por mercado. **Cada vez que se analiza un mercado de un partido, el agente de ese mercado (`.claude/agents/`) lee primero su ficha de aquí** y escribe, en `jornadas/AAAA-MM-DD/agentes/<partido>_<mercado>.md`, la sección «Lectura de <mercado>» con cada punto de la lista (dato leído → a favor / en contra / sin dato) y una predicción comprobable que entra al `guion` de la nota (`recoleccion/calificar_guion.py`).

| Mercado | Ficha | Agente |
|---|---|---|
| Córners (total, equipo, 1T/2T) | `corners.md` | `corners` |
| Tarjetas y faltas | `tarjetas_faltas.md` | `tarjetas` (tarjetas) · `partido` (faltas) |
| Goles, resultado, ambos marcan | `goles_resultado.md` | `goles-resultado` |
| Remates y tiros al arco (equipo) | `remates_tiros_arco.md` | `partido` |
| Saques de meta, saques de banda, fueras de juego | `saques_fueras.md` | `partido` |
| Jugadores | `jugadores.md` | `jugadores` |

## Cómo leer estas fichas (honestidad)
- Cada punto trae su **origen**: *usuario* (lo que dijiste), *tipster* (criterio general de tipsters y medios, **sin resultados verificados**), *lección* (lo que nos pasó en tus boletos o en el registro) o *medición* (cifra del repo).
- Un punto no es una regla de exclusión: **no se excluye ninguna línea de Betano** por estas fichas; solo ordenan la lectura (a favor / en contra) y dan la predicción del guion.
- «Dato en el repo» dice si el punto se puede leer hoy de lo recolectado; «falta» = hay que añadirlo a la recolección o leerlo a mano de la previa.
- Las estrategias en video que el usuario envió **no quedaron guardadas** en el repo: cuando las reenvíe se convierten en puntos de estas fichas (con la fuente del video).
- Si una ficha y la medición se contradicen, manda la medición y se dice.
