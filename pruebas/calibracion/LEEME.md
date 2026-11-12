# Scripts de la calibración del 10-nov (reproducibles)

Datos (no van en el paquete, 45 MB):
```bash
mkdir -p data && curl -L -o data/Matches.csv https://raw.githubusercontent.com/xgabora/Club-Football-Match-Data-2000-2025/main/data/Matches.csv
```
Correr desde una carpeta que tenga `data/` y `val/` (los scripts esperan `val/` para sus salidas).

| Script | Qué mide | Resultado (docs/CALIBRACION_10NOV.md) |
|---|---|---|
| a_devig.py | Métodos para quitar margen (1X2 y O/U 2.5) | Potencia gana (sección 1) |
| b_lambdas.py / b2_bivar.py | Ambos, empate, 0-0 desde el precio; Poisson bivariada | Sección 2 |
| c_momentos.py / c2_condicional.py | Dispersión y correlaciones reales condicionadas | Sección 3 |
| d_sim.py | Los mismos momentos en el simulador (acepta overrides de config en JSON) | Sección 3 |
| e_sistemas.py | Sistemas de tipsters con cuotas | Sección 5 → datos/sistemas_historial.json |
| f_lifts.py | Dependencia entre patas (real contra simulador) | Sección 4 → datos/dependencia_pares.json |
| g_vivo.py | En vivo desde el descanso | Sección 8 |
| h_9nov.py | Los 6 partidos del 9-nov | Sección 7 |
| parse.py, bt.py, bt2.py, ev2.py | Dixon-Coles, decaimiento, modelo de promedios contra el mercado | Sección 6 |

Nota: `bt2.py` y `h_9nov.py` son de la sesión del 10-nov y leen carpetas de trabajo propias (`/home/claude/papers` y `/home/claude/hoy`);
cambia esas rutas por las tuyas para repetirlos. El resto usa rutas relativas al paquete.
