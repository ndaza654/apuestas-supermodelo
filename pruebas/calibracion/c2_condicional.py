# C2. Varianza condicional a los equipos (lo que sabe la casa): OLS por liga-temporada con efecto local-equipo + visitante-equipo.
import numpy as np, pandas as pd
x=pd.read_pickle('val/b_lam.pkl')
s=x.dropna(subset=['HomeCorners','AwayCorners','HomeShots','AwayShots','HomeTarget','AwayTarget','HomeFouls','AwayFouls','HomeYellow','AwayYellow','HomeRed','AwayRed']).copy()
s['C']=s.HomeCorners+s.AwayCorners; s['SH']=s.HomeShots+s.AwayShots; s['SOT']=s.HomeTarget+s.AwayTarget; s['F']=s.HomeFouls+s.AwayFouls
s['T']=s.HomeYellow+s.AwayYellow+2*(s.HomeRed+s.AwayRed); s['G']=s.FTHome+s.FTAway; s['Y']=s.HomeYellow+s.AwayYellow
s['ss']=np.where(s.MatchDate.dt.month>=7,s.MatchDate.dt.year,s.MatchDate.dt.year-1)
vars_=['C','SH','SOT','F','T','Y','G','HomeCorners','AwayCorners','HomeShots','HomeTarget','HomeFouls','HomeYellow']
acc={v:[0.0,0.0,0.0] for v in vars_}  # suma residuo^2, dof, suma media
R={v:[] for v in vars_}
for (dv,ss),g in s.groupby(['Division','ss']):
    if len(g)<200: continue
    H=pd.get_dummies(g.HomeTeam).values.astype(float); A=pd.get_dummies(g.AwayTeam).values.astype(float)
    X=np.column_stack([np.ones(len(g)),H[:,1:],A[:,1:], (g.lh+g.la).values, (g.lh-g.la).values])
    for v in vars_:
        yv=g[v].values.astype(float)
        b,*_=np.linalg.lstsq(X,yv,rcond=None); r=yv-X@b
        rk=np.linalg.matrix_rank(X)
        acc[v][0]+=(r**2).sum(); acc[v][1]+=len(g)-rk; acc[v][2]+=yv.sum()
        R[v].append(pd.Series(r,index=g.index))
n=len(pd.concat(R['C']))
print('partidos usados',n)
for v in vars_:
    var=acc[v][0]/acc[v][1]; m=acc[v][2]/n
    print(f'  {v:12s} media {m:6.2f}  var condicional {var:6.2f}  var/media {var/m:.3f}  sd {var**.5:.2f}')
RR={v:pd.concat(R[v]) for v in vars_}
c=lambda a,b: np.corrcoef(RR[a],RR[b])[0,1]
print('corr condicional remates-corners %.3f  faltas-tarjetas %.3f  faltas-corners %.3f  goles-corners %.3f  corners local-visita %.3f'%(
    c('SH','C'),c('F','T'),c('F','C'),c('G','C'), np.corrcoef(RR['HomeCorners'],RR['AwayCorners'])[0,1]))
