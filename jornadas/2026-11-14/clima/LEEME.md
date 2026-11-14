# Clima por partido · 14-nov-2026

- **Fuente:** Open-Meteo (`api.open-meteo.com/v1/forecast`, modelo por defecto), consultado desde el navegador el vie 13-nov-2026 ~20:00 Bogotá. Es **pronóstico a ~1 día**, no observación: puede cambiar y conviene releerlo el día del partido.
- **Ubicación:** coordenadas de la **ciudad del estadio** (no del estadio exacto). Banfield–Boca = Mendoza (Estadio Malvinas Argentinas, sede neutral de la semifinal de Copa Argentina); Águilas Doradas = Rionegro; Portugal–Dinamarca = Braga; Suecia–Bosnia = Solna (Estocolmo).
- **Formato** (`clima.json`): por partido, `kick_bogota` y 3 horas en **UTC** (hora de inicio, +1 h, +2 h): `[hora_utc, temp °C, humedad %, prob. lluvia %, lluvia mm, viento km/h, código meteorológico WMO]`. Código: 0–3 despejado/nublado, 51 llovizna, 61 lluvia, 80 chubascos, 95 tormenta.
- Hora UTC = hora Bogotá + 5.
- Hash de `clima.json` verificado contra el navegador (3167637587 / 4089).
