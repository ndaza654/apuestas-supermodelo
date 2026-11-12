import sys, json, numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from supermodelo.analizar import analizar
G=json.load(open('/home/claude/hoy/bal/lineas_graded.json'))
res={}
for m in ['mushuc','kris','sab','las','tec','junior']:
    e=json.load(open(f'/home/claude/hoy/{m}.json'))
    A=analizar(e,n=20000,builders=False)
    res[m]={r['seleccion']:r for r in A['lineas']}
rows=[]
for g in G:
    r=res[g['m']].get(g['sel'])
    if r is None or g['y'] is None: continue
    rows.append((g['y'],g['pm'],g['pk'],g['pc'],r['p'],r['p_mercado'],r['p_simulacion'],g['m'],g['mk']))
y=np.array([r[0] for r in rows],float)
def B(i): p=np.array([r[i] if r[i] is not None else np.nan for r in rows],float); m=~np.isnan(p); return ((p[m]-y[m])**2).mean(), m.sum()
print('n',len(rows))
for nom,i in [('mercado proporcional (9-nov)',1),('modelo v2 9-nov',2),('combinada 9-nov',3),('SM-1 decisión',4),('mercado potencia (SM-1)',5),('SM-1 simulación sola',6)]:
    b,n=B(i); print(f'{nom:30s} Brier {b:.4f}  (n={n})')
d=np.array([(r[4]-r[0])**2-(r[5]-r[0])**2 for r in rows if r[5] is not None])
print('SM-1 decisión − mercado: %+.4f ± %.4f'%(d.mean(),d.std(ddof=1)/len(d)**.5))
d=np.array([(r[4]-r[0])**2-(r[2]-r[0])**2 for r in rows])
print('SM-1 decisión − v2 9-nov: %+.4f ± %.4f'%(d.mean(),d.std(ddof=1)/len(d)**.5))
for fam in sorted({r[8] for r in rows}):
    X=[r for r in rows if r[8]==fam]
    if len(X)<10: continue
    yy=np.array([r[0] for r in X]); f=lambda i: np.mean([(r[i]-r[0])**2 for r in X if r[i] is not None])
    print(f'  {fam:10s} n={len(X):3d}  mercado {f(1):.4f}  v2 {f(2):.4f}  SM-1 {f(4):.4f}')
