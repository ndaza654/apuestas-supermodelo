"""Agrega a las líneas de EQUIPO de un partido la lectura ajustada por rival (recoleccion/ajuste_rival.py). Informativa, sin validar.
Uso: python3 recoleccion/ficha_ajustada.py jornadas/AAAA-MM-DD <clave> <datos_ligas/liga_fecha.json>  → jornadas/.../ajustado/<clave>.json"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import ajuste_rival as AR

MAP = {'corners': 'c', 'goles': 'g', 'tarjetas': 'y', 'al_arco': 'sot', 'remates': 'sh', 'faltas': 'f', 'fueras': 'off', 'saques_banda': 'ti', 'saques_meta': 'gk'}


def media(sr):
    v = [a for a, c, r, ok in sr if ok]
    return sum(v) / len(v) if v else None


def correr(jornada, clave, ratings):
    eq = AR.cargar(ratings)
    fs = json.load(open(f'{jornada}/flashscore/{clave}.json', encoding='utf8'))
    L, V = fs['local'], fs['visitante']; fl, fv = fs['forma']['local'], fs['forma']['visitante']
    dia = os.path.basename(jornada.rstrip('/'))
    filas = [r for r in csv.DictReader(open('registro/lineas.csv', encoding='utf-8-sig'), delimiter=';') if r['jornada'] == dia and r['mercado'] in MAP and r['ambito'] in ('local', 'visitante', 'total') and r['partido'].lower().startswith(L.lower()[:5])]
    cache, out = {}, []
    def S(m, equipo, tipo):
        k = (m, equipo, tipo)
        if k not in cache:
            cache[k] = AR.serie(eq, fl if equipo == 'L' else fv, V if equipo == 'L' else L, m, tipo)
        return cache[k]
    for r in filas:
        m = MAP[r['mercado']]; amb = r['ambito']; lin = float(r['linea']); lado = r['lado']
        if amb == 'local':   sL, sV = S(m, 'L', 'prop'), S(m, 'V', 'conc')
        elif amb == 'visitante': sL, sV = S(m, 'L', 'conc'), S(m, 'V', 'prop')
        else:                sL, sV = S(m, 'L', 'total'), S(m, 'V', 'total')
        (aL, nL), _ = AR.conteo(sL, lin, lado); (aV, nV), _ = AR.conteo(sV, lin, lado)
        eL, eV = media(sL), media(sV)
        esp_aj = None if eL is None or eV is None else ((eL + eV) if amb == 'total' and False else (eL + eV) / 2)
        if amb == 'total' and eL is not None and eV is not None:
            # total de partido: cada equipo ya trae el total ajustado de sus partidos; el esperado es el promedio de ambas medias
            esp_aj = (eL + eV) / 2
        ok = nL >= 6 and nV >= 6
        cumple_aj = ok and aL / nL >= 0.7 and aV / nV >= 0.7
        out.append({'mercado': r['mercado'], 'ambito': amb, 'linea': lin, 'lado': lado, 'cuota': float(r['cuota']), 'p_modelo': r['p_modelo'], 'p_mercado': r['p_mercado'], 'colchon': r['colchon'], 'ev': r['ev_modelo'], 'alerta': r['alerta_modelo'], 'reg_local': r['reg_local'], 'reg_visitante': r['reg_visitante'], 'directos': r['directos'],
                    'cumple_ficha': r['cumple_ficha'], 'esperado': r['esperado'], 'esperado_aj': None if esp_aj is None else round(esp_aj, 2), 'aj_local': f'{aL} de {nL}', 'aj_visitante': f'{aV} de {nV}', 'cumple_aj': bool(cumple_aj)})
    os.makedirs(f'{jornada}/ajustado', exist_ok=True)
    json.dump({'clave': clave, 'ratings': os.path.basename(ratings), 'nota': 'Ajuste por rival SIN validar; excluye rivales de otra división (n menor); informativo.', 'filas': out}, open(f'{jornada}/ajustado/{clave}.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
    return out


if __name__ == '__main__':
    o = correr(sys.argv[1], sys.argv[2], sys.argv[3]); print(len(o), 'líneas; cumple ficha', sum(1 for x in o if x['cumple_ficha'] == 'sí'), '· cumple ajustado', sum(1 for x in o if x['cumple_aj']), '· ambos', sum(1 for x in o if x['cumple_aj'] and x['cumple_ficha'] == 'sí'))
