import numpy as np, datetime as dt, itertools, sys, json
from scipy.optimize import minimize, minimize_scalar
from scipy.stats import poisson
from parse import parse
G=10
def load(files):
    ms=[]
    for f in files: ms+=parse(f)
    ms.sort(key=lambda x:x[0]); return ms
def fit(ms, teams, tnow, hl, ridge):
    idx={t:i for i,t in enumerate(teams)}; N=len(teams)
    hi=np.array([idx[m[1]] for m in ms]); ai=np.array([idx[m[2]] for m in ms])
    gh=np.array([m[3] for m in ms],float); ga=np.array([m[4] for m in ms],float)
    age=np.array([(tnow-m[0]).days for m in ms],float)
    w=np.ones(len(ms)) if hl is None else 0.5**(age/hl)
    def f(th):
        a=th[:N]; d=th[N:2*N]; h=th[2*N]; c=th[2*N+1]
        lh=c+h+a[hi]-d[ai]; la=c+a[ai]-d[hi]
        eh=np.exp(lh); ea=np.exp(la)
        nll=np.sum(w*(eh-gh*lh+ea-ga*la))+ridge*(a@a+d@d)
        r1=w*(eh-gh); r2=w*(ea-ga)
        g=np.zeros_like(th)
        np.add.at(g,hi,r1); np.add.at(g,ai,r2)           # attack
        np.add.at(g[N:2*N],ai,-r1); np.add.at(g[N:2*N],hi,-r2)  # defence
        g[:N]+=2*ridge*a; g[N:2*N]+=2*ridge*d
        g[2*N]=r1.sum(); g[2*N+1]=r1.sum()+r2.sum()
        return nll,g
    th0=np.zeros(2*N+2); th0[2*N+1]=0.2
    r=minimize(f,th0,jac=True,method='L-BFGS-B')
    th=r.x
    lh=th[2*N+1]+th[2*N]+th[:N][hi]-th[N:2*N][ai]; la=th[2*N+1]+th[:N][ai]-th[N:2*N][hi]
    return dict(idx=idx,N=N,th=th,lh=lh,la=la,gh=gh,ga=ga,w=w)
def tau(x,y,l,m,rho):
    t=np.ones_like(l)
    t=np.where((x==0)&(y==0),1-l*m*rho,t); t=np.where((x==0)&(y==1),1+l*rho,t)
    t=np.where((x==1)&(y==0),1+m*rho,t); t=np.where((x==1)&(y==1),1-rho,t); return t
def est_rho(F):
    l=np.exp(F['lh']); m=np.exp(F['la']); x=F['gh']; y=F['ga']; w=F['w']
    def nl(r):
        t=tau(x,y,l,m,r)
        if np.any(t<=0): return 1e9
        return -np.sum(w*np.log(t))
    return minimize_scalar(nl,bounds=(-0.3,0.1),method='bounded').x
def matrix(l,m,rho=0.0):
    k=np.arange(G+1)
    P=np.outer(poisson.pmf(k,l),poisson.pmf(k,m))
    if rho!=0:
        P[0,0]*=1-l*m*rho; P[0,1]*=1+l*rho; P[1,0]*=1+m*rho; P[1,1]*=1-rho
    return P/P.sum()
def markets(P):
    H=np.tril(P,-1).sum(); D=np.trace(P); A=np.triu(P,1).sum()
    k=np.arange(G+1); tot=k[:,None]+k[None,:]
    ov=P[tot>=3].sum(); bt=P[1:,1:].sum()
    return np.array([H,D,A]),ov,bt
def walk(ms, test_from, hl, ridge, dc, step=14, minTrain=100, season_only=None):
    teams=sorted({m[1] for m in ms}|{m[2] for m in ms})
    tests=[m for m in ms if m[0]>=test_from]
    out=[]; i=0
    ds=sorted({m[0] for m in tests}); start=ds[0]
    while start<=ds[-1]:
        end=start+dt.timedelta(days=step)
        chunk=[m for m in tests if start<=m[0]<end]
        tr=[m for m in ms if m[0]<start]
        if season_only: tr=[m for m in tr if m[0]>=season_only]
        if chunk and len(tr)>=minTrain:
            F=fit(tr,teams,start,hl,ridge); rho=est_rho(F) if dc else 0.0
            th=F['th']; N=F['N']; idx=F['idx']
            for m in chunk:
                h=idx[m[1]]; a=idx[m[2]]
                lh=np.exp(th[2*N+1]+th[2*N]+th[h]-th[N+a]); la=np.exp(th[2*N+1]+th[a]-th[N+h])
                p,ov,bt=markets(matrix(lh,la,rho))
                out.append((m,p,ov,bt,rho))
        start=end
    return out
def score(out):
    ll=[];br=[];bo=[];bb=[];llo=[];llb=[]
    for m,p,ov,bt,rho in out:
        x,y=m[3],m[4]; r=0 if x>y else 1 if x==y else 2
        o=np.zeros(3); o[r]=1
        ll.append(-np.log(p[r])); br.append(((p-o)**2).sum())
        yo=1.0 if x+y>=3 else 0.0; yb=1.0 if x>0 and y>0 else 0.0
        bo.append((ov-yo)**2); bb.append((bt-yb)**2)
        llo.append(-np.log(ov if yo else 1-ov)); llb.append(-np.log(bt if yb else 1-bt))
    return dict(n=len(out),ll=np.array(ll),br=np.array(br),bo=np.array(bo),bb=np.array(bb),llo=np.array(llo),llb=np.array(llb))
def baseline(ms,test_from):
    out=[]
    for m in ms:
        if m[0]<test_from: continue
        tr=[t for t in ms if t[0]<m[0]]
        if len(tr)<100: continue
        x=np.array([t[3] for t in tr]);y=np.array([t[4] for t in tr])
        p,ov,bt=markets(matrix(x.mean(),y.mean(),0))
        out.append((m,p,ov,bt,0))
    return out
