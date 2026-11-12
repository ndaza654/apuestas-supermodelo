# B. λ local/visitante desde 1X2 + Más/Menos 2.5 (como analizar.lambdas_mercado) → ¿acierta BTTS, empate, 0-0, marca cada uno?
import numpy as np, pandas as pd, pickle
from scipy.stats import poisson
from scipy.optimize import brentq
d=pd.read_csv('data/Matches.csv',low_memory=False); d['MatchDate']=pd.to_datetime(d.MatchDate)
x=d[(d.MatchDate>='2016-08-01')].dropna(subset=['OddHome','OddDraw','OddAway','Over25','Under25','FTHome','FTAway','HTHome','HTAway'])
x=x[(x.OddHome>1)&(x.OddDraw>1)&(x.OddAway>1)&(x.Over25>1)&(x.Under25>1)]
def pw(o):
    k=brentq(lambda k:(o**k).sum()-1,0.5,3.0); return o**k
O3=1/x[['OddHome','OddDraw','OddAway']].values; O2=1/x[['Over25','Under25']].values
ok=(O3.sum(1)>1)&(O2.sum(1)>1); x=x[ok]; O3=O3[ok]; O2=O2[ok]
P3=np.array([pw(o) for o in O3]); P2=np.array([pw(o) for o in O2])[:,0]
# rejilla
L=np.arange(0.15,4.01,0.025); K=np.arange(0,13)
pm=poisson.pmf(K[None,:],L[:,None])           # (nL,13)
M=pm[:,None,:,None]*pm[None,:,None,:]          # (nL,nL,13,13)
tri=np.tril(np.ones((13,13)),-1); tru=np.triu(np.ones((13,13)),1); eye=np.eye(13)
G1=(M*tri).sum((2,3)); GX=(M*eye).sum((2,3)); G2=(M*tru).sum((2,3))
tot=K[:,None]+K[None,:]; GO=(M*(tot>=3)).sum((2,3))
GB=(1-pm[:,0])[:,None]*(1-pm[:,0])[None,:]; G00=pm[:,0][:,None]*pm[:,0][None,:]
f=lambda A:A.reshape(-1)
G=np.stack([f(G1),f(GX),f(G2),f(GO)],1)
idx=np.empty(len(x),int)
T=np.column_stack([P3,P2])
for i in range(0,len(x),400):
    e=((T[i:i+400,None,:]-G[None,:,:])**2).sum(2); idx[i:i+400]=e.argmin(1)
ih,ia=np.unravel_index(idx,G1.shape); lh,la=L[ih],L[ia]
x=x.assign(lh=lh,la=la,pBTTS=f(GB)[idx],p00=f(G00)[idx],pX=f(GX)[idx],pH0=pm[ih,0],pA0=pm[ia,0],
           yB=((x.FTHome>0)&(x.FTAway>0)).values,y00=((x.FTHome==0)&(x.FTAway==0)).values,yX=(x.FTHome==x.FTAway).values,
           yH0=(x.FTHome==0).values,yA0=(x.FTAway==0).values,mX=P3[:,1],mO=P2)
x.to_pickle('val/b_lam.pkl')
print('n',len(x))
for k,yk in [('pBTTS','yB'),('p00','y00'),('pX','yX'),('pH0','yH0'),('pA0','yA0')]:
    dif=x[yk].mean()-x[k].mean(); se=x[yk].std()/len(x)**.5
    print(f'{k:6s} predicho {x[k].mean():.4f} real {x[yk].mean():.4f} dif {dif*100:+.2f} pts ± {se*100:.2f}')
print('ajuste: empate del mercado %.4f vs Poisson %.4f'%(x.mX.mean(),x.pX.mean()))
t=x.assign(b=pd.cut(x.pBTTS,[0,.4,.45,.5,.55,.6,.65,1])).groupby('b',observed=True).agg(n=('yB','size'),pred=('pBTTS','mean'),real=('yB','mean'))
t['dif']=t.real-t.pred; print(t.round(3))
# por liga (top)
for dv,g in x.groupby('Division'):
    if len(g)<2500: continue
    print(dv,len(g),'BTTS dif %+.1f'%((g.yB.mean()-g.pBTTS.mean())*100),'X dif %+.1f'%((g.yX.mean()-g.pX.mean())*100),'00 dif %+.1f'%((g.y00.mean()-g.p00.mean())*100))
