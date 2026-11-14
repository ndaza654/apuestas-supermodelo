# Evidencia de la auditoría del repo (14-nov-2026)

Scripts de solo lectura con los que se calcularon las cifras del informe `entregas/2026-11-14/*_auditoria-repo.html`.
Se corren desde cualquier carpeta: `python3 jornadas/2026-11-14/auditoria/aud_lineas.py`.

| Archivo | Qué mide | Salida guardada |
|---|---|---|
| `aud_boletos.py` | Boletos reales del libro: neto, ROI por día, cuota, stake y número de selecciones; cumplimiento de las reglas de la hoja «Reglas» | `aud_boletos.txt` |
| `aud_lineas.py` | Líneas de equipo calificadas: ROI e intervalos por partido, modelo contra mercado, «cumple», calibración, margen de Betano, validación del recorte dejando un partido fuera, jugadores, potencia | `aud_lineas.txt` |
| `aud_lineas2.py` | Dónde se aparta el modelo del mercado y si eso predice algo | `aud_lineas2.txt` |
| `aud_jug.py` | Líneas de jugador por banda de cuota, titularidad y minutos | `aud_jug.txt` |
| `aud_hallazgos.py` | Los 48 hallazgos, el semáforo, el plan y los límites (datos del informe) | — |
| `aud_informe.py` | Genera el HTML y el Markdown del informe a partir de `aud_hallazgos.py` | — |
| `aud_probar.js` | Prueba del HTML con Playwright (filtros, consola, ancho móvil) | — |

Las cifras corresponden al commit `11ce7af`. Si `registro/lineas.csv` o el libro cambian, los números cambian.
