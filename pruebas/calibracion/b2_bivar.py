# B2. Poisson bivariada: X=A+C, Y=B+C con C~Poisson(l3). Ajuste (a,b) por partido al 1X2+O/U con l3 global; elegir l3.
import numpy as np, pandas as pd
from scipy.stats import poisson
x=pd.read_pickle('val/b_lam.pkl')
from scipy.optimize import brentq
def pw(o):
    k=brentq(lambda k:(o**k).sum()-1,0.5,3.0); return o**k
P3=np.array([pw(o) for o in 1/x[['OddHome','OddDraw','OddAway']].values]); P2=np.array([pw(o) for o in 1/x[['Over25','Under25']].values])[:,0]
T=np.column_stack([P3,P2]); K=np.arange(0,13); L=np.arange(0.05,4.01,0.025)
gh=x.FTHome.values.astype(int); ga=x.FTAway.values.astype(int)
res={}
for l3 in [0.0,0.05,0.10,0.15,0.20,0.30]:
    pm=poisson.pmf(K[None,:],L[:,None]); pc=poisson.pmf(K,l3)
    # joint P(X=i,Y=j)=sum_k pA(i-k) pB(j-k) pC(k)
    M=np.zeros((len(L),len(L),13,13))
    for k in range(0,6):
        if pc[k]<1e-9: continue
        sh=np.zeros((len(L),13)); sh[:,k:]=pm[:,:13-k]
        M+=pc[k]*sh[:,None,:,None]*sh[None,:,None,:]
    tri=np.tril(np.ones((13,13)),-1); tru=np.triu(np.ones((13,13)),1); eye=np.eye(13); tot=K[:,None]+K[None,:]
    G=np.stack([(M*tri).sum((2,3)).ravel(),(M*eye).sum((2,3)).ravel(),(M*tru).sum((2,3)).ravel(),(M*(tot>=3)).sum((2,3)).ravel()],1)
    idx=np.empty(len(x),int)
    for i in range(0,len(x),400):
        idx[i:i+400]=((T[i:i+400,None,:]-G[None,:,:])**2).sum(2).argmin(1)
    ia,ib=np.unravel_index(idx,(len(L),len(L)))
    Mf=M.reshape(len(L)*len(L),13,13)[idx]
    ll=-np.log(np.clip(Mf[np.arange(len(x)),np.minimum(gh,12),np.minimum(ga,12)],1e-12,1))
    pB=Mf[:,1:,1:].sum((1,2)); pX=np.trace(Mf,axis1=1,axis2=2); p00=Mf[:,0,0]; pH0=Mf[:,0,:].sum(1); pA0=Mf[:,:,0].sum(1)
    fit=np.sqrt(((T-G[idx])**2).sum(1)).mean()
    yB=(gh>0)&(ga>0); yX=gh==ga
    res[l3]=ll
    print(f'l3={l3:.2f} LL marcador {ll.mean():.5f} | ajuste al mercado {fit:.4f} | BTTS {pB.mean():.4f} (real {yB.mean():.4f}) X {pX.mean():.4f} (real {yX.mean():.4f}) 0-0 {p00.mean():.4f} ({((gh==0)&(ga==0)).mean():.4f}) H0 {pH0.mean():.4f} ({(gh==0).mean():.4f}) A0 {pA0.mean():.4f} ({(ga==0).mean():.4f})')
b=res[0.0]
for k,v in res.items():
    d=v-b; print(f'  l3={k:.2f} dLL vs independiente {d.mean():+.5f} ± {d.std(ddof=1)/len(d)**.5:.5f}')
