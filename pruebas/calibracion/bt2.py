import sys, datetime as dt, pickle
import numpy as np, pandas as pd
sys.path.insert(0,'/home/claude/papers')
from bt import fit, est_rho, matrix, markets
d=pd.read_csv('data/Matches.csv',low_memory=False)
d['MatchDate']=pd.to_datetime(d['MatchDate']).dt.date
LIGAS=['E0','SP1','I1','D1','F1']
def devig3(o):
    p=1/np.array(o,float); return p/p.sum()
def run(div,hl,rg,rg_g,T0=dt.date(2022,8,1),win=1100,step=14):
    x=d[(d.Division==div)].dropna(subset=['FTHome','FTAway']).sort_values('MatchDate')
    ms=[(r.MatchDate,r.HomeTeam,r.AwayTeam,int(r.FTHome),int(r.FTAway)) for r in x.itertuples()]
    rows=[]; start=T0; last=ms[-1][0]
    while start<=last:
        end=start+dt.timedelta(days=step)
        chunk=x[(x.MatchDate>=start)&(x.MatchDate<end)]
        tr=[m for m in ms if start-dt.timedelta(days=win)<=m[0]<start]
        if len(chunk) and len(tr)>150:
            teams=sorted({m[1] for m in tr}|{m[2] for m in tr})
            Fa=fit(tr,teams,start,hl,rg); Fb=fit(tr,teams,start,hl,rg_g)
            for r in chunk.itertuples():
                if r.HomeTeam not in Fa['idx'] or r.AwayTeam not in Fa['idx']: continue
                outs=[]
                for F in (Fa,Fb):
                    th=F['th'];N=F['N'];h=F['idx'][r.HomeTeam];a=F['idx'][r.AwayTeam]
                    lh=np.exp(th[2*N+1]+th[2*N]+th[h]-th[N+a]); la=np.exp(th[2*N+1]+th[a]-th[N+h])
                    outs.append(markets(matrix(lh,la,0.0)))
                p=outs[0][0]; ov=outs[1][1]; bt=outs[1][2]
                rows.append(dict(div=div,date=r.MatchDate,h=r.HomeTeam,a=r.AwayTeam,gh=int(r.FTHome),ga=int(r.FTAway),
                  pH=p[0],pD=p[1],pA=p[2],pOv=ov,pBt=bt,oH=r.OddHome,oD=r.OddDraw,oA=r.OddAway,oOv=r.Over25,oUn=r.Under25))
        start=end
    return pd.DataFrame(rows)
if __name__=='__main__':
    hl=float(sys.argv[1]); rg=float(sys.argv[2]); rgg=float(sys.argv[3])
    df=pd.concat([run(l,hl,rg,rgg) for l in LIGAS]); df.to_pickle(f'bt2_{int(hl)}_{rg}_{rgg}.pkl'); print(len(df))
