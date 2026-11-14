import os
import csv, collections, numpy as np
import os
RAIZ=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R=list(csv.DictReader(open(RAIZ+'/registro/lineas.csv',encoding='utf-8-sig'),delimiter=';'))
def f(x):
    try: return float(x)
    except: return None
E=[r for r in R if r['resultado'] in('cumplió','falló') and not r['mercado'].startswith('jugador') and f(r['p_modelo']) is not None and f(r['p_mercado']) is not None]
for r in E: r['y']=1.0 if r['resultado']=='cumplió' else 0.0; r['d']=f(r['p_modelo'])-f(r['p_mercado']); r['c']=f(r['cuota']); r['pm']=f(r['p_mercado']); r['p']=f(r['p_modelo']); r['ps']=f(r['p_simulacion'])
print('== dónde se aparta el modelo del mercado (|d|>=0.03) por mercado/ámbito')
for k,v in sorted(collections.Counter((r['mercado'],r['ambito']) for r in E if abs(r['d'])>=.03).items(), key=lambda kv:-kv[1])[:14]:
    tot=sum(1 for r in E if (r['mercado'],r['ambito'])==k); print('  ',k,v,'de',tot)
print('== por mercado: cuando el modelo está >=3 pts por ENCIMA del mercado')
for m in sorted({r['mercado'] for r in E}):
    s=[r for r in E if r['mercado']==m and r['d']>=.03]
    if s: print(f"   {m:13s} n={len(s):3d} partidos={len({(r['jornada'],r['partido']) for r in s}):2d} real={np.mean([r['y'] for r in s]):.1%} p_merc={np.mean([r['pm'] for r in s]):.1%} p_mod={np.mean([r['p'] for r in s]):.1%} ROI={np.mean([(r['c']-1) if r['y'] else -1 for r in s]):+.1%}")
print('== por partido: real − p_mercado en las líneas donde el modelo está >=3 pts por encima')
for k in sorted({(r['jornada'],r['partido']) for r in E}):
    s=[r for r in E if (r['jornada'],r['partido'])==k and r['d']>=.03]
    if s: print(f"   {k[1][:40]:40s} n={len(s):3d} real={np.mean([r['y'] for r in s]):.0%} p_merc={np.mean([r['pm'] for r in s]):.0%} p_mod={np.mean([r['p'] for r in s]):.0%} lados={dict(collections.Counter(r['lado'] for r in s))} mercados={dict(collections.Counter(r['mercado'] for r in s))}")
print('== p_modelo vs p_simulacion vs mercado: ¿qué es p_modelo?')
a=np.array([[r['p'],r['pm'],r['ps']] for r in E if r['ps'] is not None])
# regresión p = a*pm + b*ps
X=np.c_[a[:,1],a[:,2]]; w,res,_,_=np.linalg.lstsq(X,a[:,0],rcond=None); print('   p_modelo ≈ %.3f·p_mercado + %.3f·p_simulación  (residuo medio abs %.4f)'%(w[0],w[1],np.abs(X@w-a[:,0]).mean()))
print('   |p_sim − p_merc| media %.4f · p90 %.4f · >=0.10: %d (%.1f%%) · >=0.15: %d'%(np.abs(a[:,2]-a[:,1]).mean(),np.percentile(np.abs(a[:,2]-a[:,1]),90),(np.abs(a[:,2]-a[:,1])>=.10).sum(),100*(np.abs(a[:,2]-a[:,1])>=.10).mean(),(np.abs(a[:,2]-a[:,1])>=.15).sum()))
# Simulación vs mercado como predictor: regresión logística simple y = b0 + b1*logit(pm) + b2*(ps-pm)
from scipy.optimize import minimize
y=np.array([r['y'] for r in E if r['ps'] is not None]); lg=lambda q: np.log(np.clip(q,1e-4,1-1e-4)/(1-np.clip(q,1e-4,1-1e-4)))
def nll(b,X): z=X@b; return np.sum(np.log1p(np.exp(-z))*y+np.log1p(np.exp(z))*(1-y))
X1=np.c_[np.ones(len(y)),lg(a[:,1])]; X2=np.c_[X1,a[:,2]-a[:,1]]; X3=np.c_[X1,a[:,0]-a[:,1]]
r1=minimize(nll,np.zeros(2),args=(X1,)); r2=minimize(nll,np.zeros(3),args=(X2,)); r3=minimize(nll,np.zeros(3),args=(X3,))
print('   logit(y) ~ logit(p_merc): b=%s nll=%.2f'%(np.round(r1.x,3),r1.fun)); print('   + (p_sim − p_merc): b=%s nll=%.2f  (coef. negativo = la simulación empuja en la dirección equivocada)'%(np.round(r2.x,3),r2.fun)); print('   + (p_mod − p_merc): b=%s nll=%.2f'%(np.round(r3.x,3),r3.fun))
print('== sesgo favorito-improbable del mercado: real − p_merc por tramo de p_merc (todas las líneas de equipo)')
for lo in np.arange(0,1,.1):
    s=[r for r in E if lo<=r['pm']<lo+.1]
    if s: print(f"   p_merc {lo:.1f}–{lo+.1:.1f}: n={len(s):4d} real={np.mean([r['y'] for r in s]):.1%} p_merc={np.mean([r['pm'] for r in s]):.1%} ROI={np.mean([(r['c']-1) if r['y'] else -1 for r in s]):+.1%}")
