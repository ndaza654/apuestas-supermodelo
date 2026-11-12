# -*- coding: utf-8 -*-
import json, sys
def L(r):
    al = ' ⚠' if r.get('alerta') else ''
    return f"  {r['seleccion'][:52]:52s} @{r['cuota']:<5g} p={r['p']*100:4.0f}% mk={(r['p_mercado'] or 0)*100:4.0f}% sc={r['p_sin_contexto']*100:4.0f}% EV={r['ev']*100:+5.1f}% min={r['cuota_minima']:<5g} rob={r['robustez']*100:3.0f} {r.get('enfoque') or ''}{al}"
def main(k, full=False):
    A = json.load(open(f'/home/claude/nov12/corridas/{k}/entrada_resultado.json'))
    print('#', A['partido'], '|', A['tipo'], '| fav', A['favorito'], '|', A.get('p_resultado'))
    print('ENFOQUE:', A.get('enfoque_resumen'))
    for x in A.get('enfoque', []): print('  -', x['mercado'], '→', x['estado'], '·', x['porque'])
    print('CONTEXTO:'); [print('  ·', n[:140]) for n in A.get('contexto', [])[:-1] if 'Calendario' not in n and 'centros por partido' not in n]
    print('MEDIAS modelo (Betano) [sin ficha]:')
    idx = {(r['mercado'], r['ambito']): r for r in A['medias']}
    for m in ('goles', 'corners', 'tarjetas', 'remates', 'al_arco', 'faltas'):
        c = []
        for a in ('total', 'local', 'visitante', '1T', '2T'):
            r = idx.get((m, a))
            if r and (r.get('betano') is not None or m in ('goles', 'corners', 'tarjetas')): c.append(f"{a} {r['modelo']:.2f} ({r['betano'] if r.get('betano') is not None else '—'}) [{r['sin_contexto']:.2f}]")
        if c: print(f'  {m}: ' + ' | '.join(c))
    ls = A['lineas']; eq = [r for r in ls if r['familia'] not in ('jugador', 'pareja')]
    print(f"ALERTAS: {len(A.get('alertas', []))} tipos; líneas con alerta: {sum(1 for r in ls if r.get('alerta'))} de {len(ls)}")
    print('A) ALTA PROB (cuota 1.28–1.48, p≥66 %):'); [print(L(r)) for r in sorted([r for r in eq if 1.28 <= r['cuota'] <= 1.48 and r['p'] >= 0.66], key=lambda r: -r['ev'])[:6]]
    print('B) VALOR (cuota 1.50–1.75):'); [print(L(r)) for r in sorted([r for r in eq if 1.50 <= r['cuota'] <= 1.75], key=lambda r: -r['ev'])[:7]]
    print('C) EV más alto (equipo, cuota ≤ 3.2):'); [print(L(r)) for r in sorted([r for r in eq if r['cuota'] <= 3.2], key=lambda r: -r['ev'])[:5]]
    ht = [r for r in eq if r['sel']['mercado'] in ('htft', 'htft_o', 'resultado_1t', 'resultado_2t')]
    print('D) DESCANSO/FINAL (mejor EV):'); [print(L(r)) for r in sorted(ht, key=lambda r: -r['ev'])[:3]]
    jg = [r for r in ls if r['familia'] == 'jugador' and not r.get('alerta')]
    if jg:
        print('E) JUGADORES (cuota 1.3–2.6, mejor EV):'); [print(L(r)) for r in sorted([r for r in jg if 1.3 <= r['cuota'] <= 2.6], key=lambda r: -r['ev'])[:6]]
    pj = [r for r in ls if r['familia'] == 'pareja']
    if pj:
        print('F) PAREJAS (mejor EV):'); [print(L(r)) for r in sorted(pj, key=lambda r: -r['ev'])[:3]]
    if A.get('builders'):
        print('G) BUILDERS:'); [print(f"  {' + '.join(b['patas'])} | p={b['p']*100:.0f}% justa={b['cuota_justa']} min={b['cuota_minima']} prod={b['producto_cuotas']} corr={b['correlacion']}") for b in A['builders'][:2]]
if __name__ == '__main__':
    main(sys.argv[1])
