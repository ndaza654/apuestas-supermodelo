# F. Dependencia entre patas: lift = P(A y B) / (P(A)·P(B)) en datos reales (dentro de liga × goles esperados × diferencia)
#    y en el simulador (configuración final). Línea de cada estadística = media esperada redondeada a x.5.
import sys, numpy as np, pandas as pd, json
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from supermodelo.simulador import Partido
x=pd.read_pickle('val/b_lam.pkl')
s=x.dropna(subset=['HomeCorners','AwayCorners','HomeShots','AwayShots','HomeTarget','AwayTarget','HomeYellow','AwayYellow','HomeRed','AwayRed']).copy()
s['bt']=pd.cut(s.lh+s.la,[0,2.2,2.5,2.8,3.1,3.5,9]); s['bd']=pd.cut(s.lh-s.la,[-9,-0.8,-0.3,0.3,0.8,1.3,9])
grp=['Division','bt','bd']
s['fav']=np.where(s.lh>=s.la,0,1)
def side(df,h,a,who): return np.where(who==0,df[h],df[a])
def ev_real(g):
    fav=g.fav.values; G=(g.FTHome+g.FTAway).values; C=(g.HomeCorners+g.AwayCorners).values
    T=(g.HomeYellow+g.AwayYellow+2*(g.HomeRed+g.AwayRed)).values; SH=(g.HomeShots+g.AwayShots).values
    cf=side(g,'HomeCorners','AwayCorners',fav); cn=side(g,'HomeCorners','AwayCorners',1-fav)
    shf=side(g,'HomeShots','AwayShots',fav); sotf=side(g,'HomeTarget','AwayTarget',fav)
    gf=side(g,'FTHome','FTAway',fav); gn=side(g,'FTHome','FTAway',1-fav)
    return dict(fav_gana=gf>gn, o25=G>=3, u25=G<=2, btts=(gf>0)&(gn>0), c_mas=C, c_fav=cf, c_nofav=cn, sh_fav=shf, sot_fav=sotf, t_mas=T, sh_mas=SH)
PARES=[('fav_gana','c_fav'),('fav_gana','sh_fav'),('fav_gana','sot_fav'),('fav_gana','o25'),('fav_gana','c_nofav'),('fav_gana','t_mas'),
       ('o25','c_mas'),('btts','c_mas'),('o25','t_mas'),('c_mas','t_mas'),('o25','sh_mas'),('btts','o25'),('u25','c_mas_menos'),('fav_gana','btts')]
def binarize(E, means):
    out={}
    for k,v in E.items():
        if v.dtype==bool: out[k]=v
        else:
            L=np.floor(means[k])+0.5; out[k]=v>L
            if k=='c_mas': out['c_mas_menos']=v<L
    return out
def lifts(groups):
    acc={p:[0.0,0.0] for p in PARES}
    for E,w in groups:
        for a,b in PARES:
            pa,pb,pab=E[a].mean(),E[b].mean(),(E[a]&E[b]).mean()
            if pa>0 and pb>0: acc[(a,b)][0]+=w*pab/(pa*pb); acc[(a,b)][1]+=w
    return {f'{a} & {b}':round(v[0]/v[1],4) for (a,b),v in acc.items()}
G=[]
for _,g in s.groupby(grp,observed=True):
    if len(g)<60: continue
    E=ev_real(g); means={k:v.mean() for k,v in E.items() if v.dtype!=bool}
    G.append((binarize(E,means),len(g)))
real=lifts(G)
# simulador
cols={'c':('HomeCorners','AwayCorners'),'sh':('HomeShots','AwayShots'),'sot':('HomeTarget','AwayTarget'),'f':('HomeFouls','AwayFouls'),'y':('HomeYellow','AwayYellow')}
s2=s.dropna(subset=['HomeFouls','AwayFouls']).copy()
for k,(h,a) in cols.items():
    s2[k+'_h']=s2.groupby(['bt','bd'],observed=True)[h].transform('mean'); s2[k+'_a']=s2.groupby(['bt','bd'],observed=True)[a].transform('mean')
m=s2.sample(int(sys.argv[1]) if len(sys.argv)>1 else 24,random_state=5)
GS=[]; rng=np.random.default_rng(9)
for _,r in m.iterrows():
    obj=[dict(g=r.lh,sh=r.sh_h,sot=r.sot_h,c=r.c_h,f=r.f_h,y=r.y_h),dict(g=r.la,sh=r.sh_a,sot=r.sot_a,c=r.c_a,f=r.f_a,y=r.y_a)]
    R=Partido(obj,n=int(sys.argv[2]) if len(sys.argv)>2 else 6000,seed=int(rng.integers(1e6))).res
    fav=0 if r.lh>=r.la else 1; nf=1-fav
    G_=R[0]['g']+R[1]['g']
    E=dict(fav_gana=R[fav]['g']>R[nf]['g'],o25=G_>=3,u25=G_<=2,btts=(R[0]['g']>0)&(R[1]['g']>0),c_mas=R[0]['c']+R[1]['c'],c_fav=R[fav]['c'],c_nofav=R[nf]['c'],
           sh_fav=R[fav]['sh'],sot_fav=R[fav]['sot'],t_mas=R[0]['tarjetas']+R[1]['tarjetas'],sh_mas=R[0]['sh']+R[1]['sh'])
    means={k:v.mean() for k,v in E.items() if v.dtype!=bool}
    GS.append((binarize(E,means),1))
sim=lifts(GS)
out={k:dict(real=real[k],sim=sim[k],ajuste=round(real[k]/sim[k],4)) for k in real}
json.dump(out,open('val/f_lifts.json','w'),ensure_ascii=False,indent=1)
print(f"{'par':28s} {'real':>7s} {'sim':>7s} {'real/sim':>8s}")
for k,v in out.items(): print(f"{k:28s} {v['real']:7.3f} {v['sim']:7.3f} {v['ajuste']:8.3f}")
