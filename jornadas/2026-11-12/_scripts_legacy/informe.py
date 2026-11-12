# -*- coding: utf-8 -*-
"""Escribe el bloque «informe» de un partido con las líneas elegidas (cifras exactas del resultado del modelo), vuelve a correr el
modelo y deja el HTML en informes/<clave>.html. Uso: python3 informe.py <clave>   (lee elegidas/<clave>.json)"""
import json, sys, os, subprocess, html as H
B = '/home/claude/nov12'
U = {'goles': 'goles', 'corners': 'córners', 'tarjetas': 'puntos de tarjeta', 'remates': 'remates', 'al_arco': 'tiros al arco', 'faltas': 'faltas', 'fueras': 'fueras de lugar',
     'saques_meta': 'saques de meta', 'saques_banda': 'saques de banda'}
def frase(A, r, loc, vis):
    s = r['sel']; m, a = s.get('mercado'), s.get('ambito')
    idx = {(x['mercado'], x['ambito']): x for x in A['medias']}
    t = ''
    if (m, a) in idx:
        x = idx[(m, a)]
        donde = {'total': 'en el partido', 'local': f'de {loc}', 'visitante': f'de {vis}', '1T': 'en el 1.er tiempo', '2T': 'en el 2.º tiempo'}[a]
        t = f" El modelo calculó <b>{x['modelo']:.1f} {U[m]}</b> {donde}" + (f"; Betano espera <b>{x['betano']:.1f}</b>" if x.get('betano') is not None else '; Betano no da escalera para comparar') + f" (rango habitual {x['p10']:g}–{x['p90']:g})."
    pm = f"mercado {r['p_mercado'] * 100:.0f} %" if r.get('p_mercado') else 'sin referencia de mercado'
    sc = r.get('p_sin_contexto')
    ctx = f"; sin el ajuste de contexto {sc * 100:.0f} %" if sc is not None and abs(sc - r['p']) >= 0.02 else ''
    return t + f" Probabilidad {r['p'] * 100:.0f} % ({pm}{ctx}), EV {r['ev'] * 100:+.1f} %, <b>cuota mínima {r['cuota_minima']:.2f}</b>."
def main(k):
    E_ = json.load(open(f'{B}/corridas/{k}/entrada.json', encoding='utf8'))
    A = json.load(open(f'{B}/corridas/{k}/entrada_resultado.json', encoding='utf8'))
    X = json.load(open(f'{B}/elegidas/{k}.json', encoding='utf8'))
    loc, vis = E_['local'], E_['visitante']
    por = {r['seleccion']: r for r in A['lineas']}
    lect, picks = [], []
    for tipo, tit in (('alta', 'Alta probabilidad'), ('valor', 'Línea de valor (cuota 1.50–1.70)'), ('extra', 'Extra')):
        for sel, why in X.get(tipo, []):
            r = por[sel]
            lect.append(f"<b>{tit} · {H.escape(sel)} a {r['cuota']:.2f}.</b> {why}" + frase(A, r, loc, vis))
            picks.append(dict(tipo=tipo, seleccion=sel, cuota=r['cuota'], p=r['p'], p_mercado=r.get('p_mercado'), p_sin_contexto=r.get('p_sin_contexto'), ev=r['ev'], cuota_minima=r['cuota_minima'], porque=why))
    inf = E_.setdefault('informe', {})
    import re
    idx = {(x['mercado'], x['ambito']): x for x in A['medias']}
    def rell(t):
        def f(m):
            tp, a1, a2 = m.group(1), m.group(2), m.group(3)
            if tp == 'm': return f"{idx[(a1, a2)]['modelo']:.1f}".replace('.', ',')
            if tp == 'b': return f"{idx[(a1, a2)]['betano']:.1f}".replace('.', ',') if idx[(a1, a2)].get('betano') is not None else 'sin dato'
            if tp == 'p': return f"{A['p_resultado'][a1] * 100:.0f} %"
        return re.sub(r'\{(m|b|p):([a-z_0-9A-Z]+):?([a-zA-Z0-9]*)\}', f, t)
    X = json.loads(rell(json.dumps(X, ensure_ascii=False)))
    inf['lectura'] = lect + X.get('lectura', [])
    for c in ('veredicto', 'accion', 'chips', 'limites', 'checklist', 'evitar', 'acento'):
        if c in X: inf[c] = X[c]
    json.dump(E_, open(f'{B}/corridas/{k}/entrada.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    r = subprocess.run(['python3', '-m', 'supermodelo', f'{B}/corridas/{k}/entrada.json'], cwd='/home/claude/supermodelo', capture_output=True, text=True)
    if r.returncode: print(r.stderr[-800:]); return
    os.makedirs(f'{B}/informes', exist_ok=True)
    nom = X.get('archivo', k)
    open(f'{B}/informes/{nom}.html', 'w', encoding='utf8').write(open(f'{B}/corridas/{k}/entrada_informe.html', encoding='utf8').read())
    P = json.load(open(f'{B}/picks.json')) if os.path.exists(f'{B}/picks.json') else {}
    P[k] = dict(partido=f'{loc} – {vis}', hora=E_['fecha'][-5:], liga=E_['liga'], picks=picks, veredicto=X.get('veredicto', ''))
    json.dump(P, open(f'{B}/picks.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('ok', nom, os.path.getsize(f'{B}/informes/{nom}.html'), 'bytes;', len(picks), 'líneas')
if __name__ == '__main__':
    main(sys.argv[1])
