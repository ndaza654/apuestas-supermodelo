"""Líneas de jugador (remates, tiros al arco) ajustadas por el rival de hoy. Informativo, SIN validar; el modelo de jugador viene inflado 17–19 pts según los balances.
Uso: python3 recoleccion/jugadores_ajustados.py jornadas/AAAA-MM-DD <clave> <datos_ligas/liga_fecha.json>  → jornadas/.../ajustado/jugadores_<clave>.json"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import ajuste_rival as AR

STAT = {'jugador:remates': ('remates', 'sh'), 'jugador:al_arco': ('al_arco', 'sot')}


def correr(jornada, clave, ratings, min_min=30):
    eq = AR.cargar(ratings)
    ent = json.load(open(f'{jornada}/entradas/{clave}.json', encoding='utf8'))
    fs = json.load(open(f'{jornada}/flashscore/{clave}.json', encoding='utf8'))
    L, V = fs['local'], fs['visitante']
    rival_de = {'local': {p['mid']: p['rival'] for p in fs['forma']['local']}, 'visitante': {p['mid']: p['rival'] for p in fs['forma']['visitante']}}
    hist = ent['ficha']['jugadores_hist']; tit = {j['nombre']: j for j in ent['jugadores']}
    dia = os.path.basename(jornada.rstrip('/'))
    filas = [r for r in csv.DictReader(open('registro/lineas.csv', encoding='utf-8-sig'), delimiter=';') if r['jornada'] == dia and r['mercado'] in STAT and r['partido'].lower().startswith(L.lower()[:5])]
    out = []
    for r in filas:
        campo, m = STAT[r['mercado']]; nom = r['jugador']; lado = r['ambito']
        h = hist.get(nom); 
        if not h: continue
        opp = V if lado == 'local' else L
        rh = AR.rating(eq, opp, m); lin = float(r['linea'])
        vals, adj = [], []
        for pt in h['partidos']:
            if (pt.get('min') or 0) < min_min: continue
            v = pt.get(campo) or 0; vals.append(v)
            rv = rival_de[lado].get(pt['mid']); rr = AR.rating(eq, rv, m) if rv else None
            if rh and rr and AR.primera_division(eq.get(rv, [])) and rr[1] > 0:
                adj.append(v * AR._clip(rh[1] / rr[1]))
        cr = sum(1 for v in vals if v >= lin); ca = sum(1 for v in adj if v >= lin)
        mins = [pt['min'] for pt in h['partidos'] if (pt.get('min') or 0) > 0]
        out.append({'jugador': nom, 'lado': lado, 'pos': h.get('pos'), 'titular': (tit.get(nom) or {}).get('titular'), 'fuera': bool((tit.get(nom) or {}).get('fuera')),
                    'mercado': r['mercado'], 'linea': lin, 'cuota': float(r['cuota']), 'p_modelo': r['p_modelo'], 'reg': r['reg_local'] or r['reg_visitante'],
                    'crudo': f'{cr} de {len(vals)}', 'ajustado': f'{ca} de {len(adj)}', 'media_cruda': round(sum(vals) / len(vals), 2) if vals else None,
                    'media_ajustada': round(sum(adj) / len(adj), 2) if adj else None, 'min_medios': round(sum(mins) / len(mins)) if mins else None, 'factor_rival': round(rh[1] / ((AR.media_liga(eq, m)[0]) or 1), 2) if rh else None})
    os.makedirs(f'{jornada}/ajustado', exist_ok=True)
    json.dump({'clave': clave, 'nota': 'Ajuste por rival SIN validar; solo remates y tiros al arco; partidos con ≥30 min.', 'filas': out}, open(f'{jornada}/ajustado/jugadores_{clave}.json', 'w', encoding='utf8'), ensure_ascii=False)
    return out


if __name__ == '__main__':
    o = correr(sys.argv[1], sys.argv[2], sys.argv[3]); print(len(o), 'líneas de jugador ajustadas')
