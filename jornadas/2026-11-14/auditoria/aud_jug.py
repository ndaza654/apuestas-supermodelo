import os
import csv, collections, numpy as np
R=list(csv.DictReader(open(os.path.join(__import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','..')),'registro','lineas.csv'),encoding='utf-8-sig'),delimiter=';'))
def f(x):
    try: return float(x)
    except: return None
J=[r for r in R if r['mercado'].startswith('jugador') and r['resultado'] in('cumplió','falló') and f(r['cuota'])]
print('jugador calificadas',len(J),'partidos',sorted({r['partido'] for r in J}))
print('titular (campo):',collections.Counter(('titular>=0.5' if (f(r['titular']) or 0)>=.5 else 'suplente/sin dato') for r in J))
def tab(t,key,rows):
    G=collections.defaultdict(list)
    for r in rows:
        k=key(r)
        if k is not None: G[k].append(r)
    print('==',t)
    for k in sorted(G):
        g=G[k]; y=np.mean([r['resultado']=='cumplió' for r in g]); inv=np.mean([1/f(r['cuota']) for r in g]); pm=np.mean([f(r['p_mercado']) for r in g if f(r['p_mercado']) is not None] or [np.nan]); p=np.mean([f(r['p_modelo']) for r in g if f(r['p_modelo']) is not None] or [np.nan])
        roi=np.mean([(f(r['cuota'])-1) if r['resultado']=='cumplió' else -1 for r in g])
        print(f"   {str(k):26s} n={len(g):4d} real={y:5.1%} 1/cuota={inv:5.1%} p_merc={pm:5.1%} p_mod={p:5.1%} ROI={roi:+.0%}")
band=lambda r: ('1 <1.5' if f(r['cuota'])<1.5 else '2 1.5-2' if f(r['cuota'])<2 else '3 2-3' if f(r['cuota'])<3 else '4 3-6' if f(r['cuota'])<6 else '5 6-15' if f(r['cuota'])<15 else '6 >=15')
tab('por banda de cuota (todos)',band,J)
T=[r for r in J if (f(r['titular']) or 0)>=.5]
tab('por banda de cuota (titulares probables)',band,T)
tab('por escalón (linea) titulares',lambda r:(r['mercado'][8:],r['linea']) if r['mercado'][8:] in('remates','al_arco') else None,T)
tab('minutos jugados (de la nota) – todos',lambda r:(lambda m: None if m is None else ('1 <30' if m<30 else '2 30-59' if m<60 else '3 60+'))(int(r['nota'].split(', ')[-1].split('′')[0]) if '′' in r['nota'] else None),J)
