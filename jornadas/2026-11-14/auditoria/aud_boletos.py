# Auditoría · boletos reales del usuario (libro_apuestas.xlsx). Solo lectura.
import openpyxl, collections, datetime, sys, json
import os
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
wb = openpyxl.load_workbook(RAIZ + '/registro/libro_apuestas.xlsx')
U = 3700


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).strip().lstrip('=')
    try:
        return float(s)
    except ValueError:
        return None


B = []
ws = wb['Boletos']
for r in ws.iter_rows(min_row=5, values_only=True):
    if r[0] is None or num(r[0]) is None:
        continue
    B.append(dict(n=int(num(r[0])), fecha=str(r[2])[:10], hora=str(r[3] or ''), tipo=r[6], npart=num(r[7]), nsel=num(r[8]), cuota=num(r[11]), stake=num(r[12]) or 0,
                  gratis=(r[13] == 'Sí'), vivo=(r[15] == 'Sí'), res=r[16], cobrado=num(r[17]) or 0, etiqueta=r[28]))
ws = wb['Boletos 9-12']
for r in ws.iter_rows(min_row=5, values_only=True):
    if r[0] is None or num(r[0]) is None:
        continue
    patas = str(r[16] or '')
    B.append(dict(n=int(num(r[0])), fecha=str(r[2])[:10], hora=str(r[3] or ''), tipo=r[4], npart=num(r[5]), nsel=patas.count('·') + 1 if patas else None, cuota=num(r[6]), stake=num(r[7]) or 0,
                  gratis=(r[8] == 'Sí'), vivo=None, res=r[10], cobrado=num(r[11]) or 0, etiqueta=None, patas=patas))
print('boletos', len(B), 'numeración', B[0]['n'], '→', B[-1]['n'])
print('resultados', collections.Counter(b['res'] for b in B))
real = [b for b in B if not b['gratis'] and b['res'] in ('Ganada', 'Perdida', 'Cash out', 'Cashout', 'Anulada', 'Reembolso', 'Devuelta') or (not b['gratis'] and b['res'] not in (None, 'Pendiente'))]


def resumen(t, bs):
    st = sum(b['stake'] for b in bs)
    co = sum(b['cobrado'] for b in bs)
    g = sum(1 for b in bs if b['cobrado'] > b['stake'])
    print(f"{t:42s} n={len(bs):3d} ganados={g:3d} ({g / len(bs) if bs else 0:5.1%}) apostado=${st:>10,.0f} cobrado=${co:>10,.0f} neto=${co - st:>+10,.0f} ROI={((co - st) / st if st else 0):+6.1%}")


resumen('TODOS (dinero real)', real)
resumen('  4–8 nov', [b for b in real if b['fecha'] <= '2026-11-08'])
resumen('  9–13 nov', [b for b in real if b['fecha'] >= '2026-11-09'])
print('-- por día')
for d in sorted({b['fecha'] for b in real}):
    resumen('  ' + d, [b for b in real if b['fecha'] == d])
print('-- por cuota')
for a, z, t in ((0, 2, '<2,00'), (2, 3, '2,00–2,99'), (3, 5, '3,00–4,99'), (5, 10, '5,00–9,99'), (10, 1e9, '≥10')):
    resumen('  cuota ' + t, [b for b in real if b['cuota'] and a <= b['cuota'] < z])
print('-- por stake')
for a, z, t in ((0, 3751, '≤ 1 u (3.750)'), (3751, 7501, '1–2 u'), (7501, 15001, '2–4 u'), (15001, 30001, '4–8 u'), (30001, 1e9, '> 8 u')):
    resumen('  stake ' + t, [b for b in real if a <= b['stake'] < z])
print('-- por nº de selecciones (donde se sabe)')
for k in (1, 2, 3, 4, 5, 6):
    bs = [b for b in real if b['nsel'] and (b['nsel'] == k if k < 6 else b['nsel'] >= 6)]
    if bs:
        resumen(f'  {k}{"+" if k == 6 else ""} selecciones', bs)
print('-- en vivo (solo 4–8 nov trae la marca)')
resumen('  en vivo', [b for b in real if b['vivo'] is True])
resumen('  prepartido', [b for b in real if b['vivo'] is False])
# cumplimiento de las reglas del propio libro (hoja Reglas, escritas tras el 8-nov) en los boletos del 9-nov en adelante
post = [b for b in real if b['fecha'] >= '2026-11-09']
print('\n== Reglas del libro (stake máx 7.500; máx 3 selecciones; exposición diaria máx 60.000; tope de pérdida diaria 30.000; no 0:00–7:00) en boletos del 9-nov en adelante')
print('  boletos con stake > 7.500:', sum(1 for b in post if b['stake'] > 7500), 'de', len(post), '· stake mediano', sorted(b['stake'] for b in post)[len(post) // 2], '· máximo', max(b['stake'] for b in post))
print('  boletos con > 3 selecciones:', sum(1 for b in post if (b['nsel'] or 0) > 3), 'de', sum(1 for b in post if b['nsel']))
for d in sorted({b['fecha'] for b in post}):
    bs = [b for b in post if b['fecha'] == d]
    st = sum(b['stake'] for b in bs)
    net = sum(b['cobrado'] - b['stake'] for b in bs)
    print(f"  {d}: {len(bs)} boletos, exposición ${st:,.0f} ({'SUPERA' if st > 60000 else 'dentro de'} 60.000), neto ${net:+,.0f} ({'SUPERA el tope de pérdida' if net < -30000 else 'ok'})")
mad = [b for b in post if b['hora'][:2].isdigit() and int(b['hora'][:2]) < 7]
print('  boletos entre 0:00 y 7:00:', len(mad), '(solo los que traen hora:', sum(1 for b in post if b['hora'][:2].isdigit()), ')')
# gratis
g = [b for b in B if b['gratis']]
print('\napuestas gratis:', len(g), 'cobrado', sum(b['cobrado'] for b in g))
# racha y concentración
real.sort(key=lambda b: b['n'])
acc = 0; peor = 0; pico = 0
for b in real:
    acc += b['cobrado'] - b['stake']; pico = max(pico, acc); peor = min(peor, acc - pico)
print(f'neto acumulado ${acc:+,.0f} · mayor caída desde un pico ${peor:,.0f} · mejor boleto ${max(b["cobrado"] - b["stake"] for b in real):+,.0f} · neto sin los 2 mejores ${acc - sum(sorted((b["cobrado"] - b["stake"] for b in real), reverse=True)[:2]):+,.0f}')
# banca
ws = wb['Banca']
dep = sum(num(r[4]) or 0 for r in ws.iter_rows(min_row=5, values_only=True) if r[1] == 'Depósito')
ndep = sum(1 for r in ws.iter_rows(min_row=5, values_only=True) if r[1] == 'Depósito')
ult = [r for r in ws.iter_rows(min_row=5, values_only=True) if r[0] is not None][-1]
print(f'Banca (hoja, solo 4–8 nov): {ndep} depósitos por ${dep:,.0f}; último movimiento {ult[0]} saldo {ult[5]}')
print('tipos de movimiento', collections.Counter(r[1] for r in ws.iter_rows(min_row=5, values_only=True) if r[1]))
json.dump(B, open(sys.argv[1], 'w'), ensure_ascii=False, default=str) if len(sys.argv) > 1 else None
