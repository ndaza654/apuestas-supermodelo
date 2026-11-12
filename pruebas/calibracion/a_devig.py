# A. Métodos para quitar margen: proporcional, potencia (k que hace sumar 1), Shin, exponente fijo; 1X2 y O/U 2.5
import numpy as np, pandas as pd
from scipy.optimize import brentq
d=pd.read_csv('data/Matches.csv',low_memory=False); d['MatchDate']=pd.to_datetime(d.MatchDate)
d=d[d.MatchDate>='2012-08-01']
def prop(O): return O/O.sum(1,keepdims=True)
def power(O):
    out=np.empty_like(O)
    for i,o in enumerate(O):
        k=brentq(lambda k:(o**k).sum()-1,0.5,3.0); out[i]=o**k
    return out
def shin(O):
    out=np.empty_like(O)
    for i,o in enumerate(O):
        S=o.sum(); n=len(o)
        def pz(z): return (np.sqrt(z**2+4*(1-z)*o**2/S)-z)/(2*(1-z))
        z=brentq(lambda z:pz(z).sum()-1,0,0.4) if S>1 else 0
        out[i]=pz(z)
    return out
def ll(P,y): return -np.log(np.clip(P[np.arange(len(P)),y],1e-9,1))
x=d.dropna(subset=['OddHome','OddDraw','OddAway','FTResult']); x=x[(x.OddHome>1)&(x.OddDraw>1)&(x.OddAway>1)]
O=1/x[['OddHome','OddDraw','OddAway']].values; O=O[O.sum(1)>1.0]; x=x[(1/x[['OddHome','OddDraw','OddAway']].values).sum(1)>1.0]
y=x.FTResult.map({'H':0,'D':1,'A':2}).values
print('1X2 n',len(x),'margen medio %.3f'%(O.sum(1).mean()-1))
P={'proporcional':prop(O),'potencia':power(O),'shin':shin(O)}
pw=O**1.085; P['exp_fijo_1.085']=pw/pw.sum(1,keepdims=True)
base=ll(P['proporcional'],y)
for k,v in P.items():
    dd=ll(v,y)-base; print(f'  {k:16s} LL {ll(v,y).mean():.5f}  vs prop {dd.mean():+.5f} ± {dd.std(ddof=1)/len(dd)**.5:.5f}')
# por margen (Betano suele tener más margen)
m=O.sum(1)-1
for lo,hi in [(0,.04),(.04,.06),(.06,.08),(.08,.2)]:
    s=(m>=lo)&(m<hi)
    if s.sum()<500: continue
    print(f'  margen {lo:.2f}-{hi:.2f} n={s.sum()}: '+' '.join(f"{k} {(ll(v[s],y[s])-base[s]).mean():+.5f}" for k,v in P.items() if k!='proporcional'))
# O/U 2.5
g=d.dropna(subset=['Over25','Under25','FTHome','FTAway']); g=g[(g.Over25>1)&(g.Under25>1)]
O2=1/g[['Over25','Under25']].values; s=O2.sum(1)>1.0; g=g[s]; O2=O2[s]; y2=((g.FTHome+g.FTAway)>=3).astype(int).map({1:0,0:1}).values
P2={'proporcional':prop(O2),'potencia':power(O2),'shin':shin(O2)}
b2=ll(P2['proporcional'],y2); print('O/U2.5 n',len(g),'margen %.3f'%(O2.sum(1).mean()-1))
for k,v in P2.items():
    dd=ll(v,y2)-b2; print(f'  {k:16s} LL {ll(v,y2).mean():.5f} vs prop {dd.mean():+.5f} ± {dd.std(ddof=1)/len(dd)**.5:.5f}')
# calibración de lado Over por tramo (proporcional)
po=P2['proporcional'][:,0]; yo=(y2==0)
t=pd.DataFrame({'b':pd.cut(po,[0,.35,.45,.5,.55,.6,.65,.75,1]),'p':po,'y':yo}).groupby('b',observed=True).agg(n=('y','size'),prob=('p','mean'),real=('y','mean'))
t['dif']=t.real-t.prob; print(t.round(3))
