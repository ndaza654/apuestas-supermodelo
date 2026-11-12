# E. Auditoría de sistemas de tipsters con cuotas reales: 38 ligas, ago-2012 → 2026. ROI a cuota media del archivo y a la máxima.
import numpy as np, pandas as pd, json
from scipy.optimize import brentq
d=pd.read_csv('data/Matches.csv',low_memory=False); d['MatchDate']=pd.to_datetime(d.MatchDate)
d=d[d.MatchDate>='2012-08-01'].dropna(subset=['FTHome','FTAway','OddHome','OddDraw','OddAway']).sort_values('MatchDate').reset_index(drop=True)
d=d[(d.OddHome>1)&(d.OddDraw>1)&(d.OddAway>1)]
d['G']=d.FTHome+d.FTAway; d['res']=np.where(d.FTHome>d.FTAway,'H',np.where(d.FTHome==d.FTAway,'D','A'))
d['ss']=np.where(d.MatchDate.dt.month>=7,d.MatchDate.dt.year,d.MatchDate.dt.year-1)
# rachas e historial (por liga): BTTS seguidos del local, victorias seguidas, empates en H2H, posición en la tabla
d['btts']=(d.FTHome>0)&(d.FTAway>0)
last_btts={}; streak_w={}; h2h={}; pts={}; played={}
f_btts2=[]; f_w2h=[]; f_w2a=[]; f_h2hX=[]; f_ultimo_h=[]; f_ultimo_a=[]
for r in d.itertuples():
    kh=(r.Division,r.HomeTeam); ka=(r.Division,r.AwayTeam)
    f_btts2.append(last_btts.get(kh,[])[-2:]==[True,True])
    f_w2h.append(streak_w.get(kh,0)>=2); f_w2a.append(streak_w.get(ka,0)>=2)
    pair=tuple(sorted([r.HomeTeam,r.AwayTeam])); hh=h2h.get(pair,[])[-5:]; f_h2hX.append(sum(hh)>=2 if len(hh)>=3 else None)
    ks=(r.Division,r.ss)
    tab=pts.get(ks,{}); pl=played.get(ks,{})
    if tab and min(pl.get(t,0) for t in tab)>=8 and kh[1] in tab and ka[1] in tab:
        ult=min(tab,key=lambda t:(tab[t],)); f_ultimo_h.append(r.HomeTeam==ult); f_ultimo_a.append(r.AwayTeam==ult)
    else: f_ultimo_h.append(False); f_ultimo_a.append(False)
    # actualizar
    last_btts.setdefault(kh,[]).append(bool(r.btts))
    for k,won in ((kh,r.res=='H'),(ka,r.res=='A')): streak_w[k]=streak_w.get(k,0)+1 if won else 0
    h2h.setdefault(pair,[]).append(r.res=='D')
    tab=pts.setdefault(ks,{}); pl=played.setdefault(ks,{})
    for t,p in ((r.HomeTeam,3 if r.res=='H' else 1 if r.res=='D' else 0),(r.AwayTeam,3 if r.res=='A' else 1 if r.res=='D' else 0)):
        tab[t]=tab.get(t,0)+p; pl[t]=pl.get(t,0)+1
d['btts2_local']=f_btts2; d['w2_local']=f_w2h; d['w2_visita']=f_w2a; d['h2h_2X']=f_h2hX; d['ultimo_local']=f_ultimo_h; d['ultimo_visita']=f_ultimo_a
def pw(o):
    o=np.asarray(o); 
    if o.sum()<=1: return o/o.sum()
    k=brentq(lambda k:(o**k).sum()-1,1,3); return o**k
P=np.array([pw(1/np.array(x)) for x in d[['OddHome','OddDraw','OddAway']].values]); d['pH'],d['pD'],d['pA']=P.T
ou=d.Over25.notna()&d.Under25.notna()&(d.Over25>1)&(d.Under25>1)
PO=np.full(len(d),np.nan); PO[ou.values]=[pw(1/np.array(x))[0] for x in d.loc[ou,['Over25','Under25']].values]; d['pO']=PO
d.to_pickle('val/e_base.pkl')
def roi(m, gana, cuota, cuota_max=None, p_impl=None, nombre=''):
    g=d[m]; 
    if len(g)<30: return None
    y=gana(g).astype(float); o=cuota(g); pr=y*o-1
    out=dict(sistema=nombre,n=int(len(g)),acierto=round(y.mean(),4),implicita=round(float(p_impl(g).mean()),4) if p_impl else None,
             roi=round(pr.mean(),4),ic95=round(1.96*pr.std(ddof=1)/len(g)**.5,4))
    if cuota_max is not None:
        om=cuota_max(g); pm=(y*om-1); out['roi_cuota_max']=round(pm[np.isfinite(pm)].mean(),4)
    g2=g[g.MatchDate>='2019-08-01']
    if len(g2)>=30:
        y2=gana(g2).astype(float); out['roi_desde_2019']=round((y2*cuota(g2)-1).mean(),4); out['n_desde_2019']=int(len(g2))
    return out
OV=lambda g:(g.G>=3); UN=lambda g:(g.G<=2); X=lambda g:g.res=='D'
cO=lambda g:g.Over25; cU=lambda g:g.Under25; cX=lambda g:g.OddDraw
mO=lambda g:g.MaxOver25; mU=lambda g:g.MaxUnder25; mX=lambda g:g.MaxDraw
S=[]
S.append(roi(ou,OV,cO,mO,lambda g:g.pO,'Referencia: Más 2.5 en todos'))
S.append(roi(ou,UN,cU,mU,lambda g:1-g.pO,'Referencia: Menos 2.5 en todos (¿sesgo del público al Más? Sharpods)'))
S.append(roi(ou&(d.OddHome<=1.50),OV,cO,mO,lambda g:g.pO,'IA #400: local ≤1,50 → Más 2.5 (sin el filtro 1T, no está en datos)'))
S.append(roi(ou&(d.OddHome<=1.50)&(d.OddDraw>=4.10),OV,cO,mO,lambda g:g.pO,'IA #453: local ≤1,50 y empate ≥4,10 → Más 2.5'))
S.append(roi(ou&(d.OddDraw>=3.60),OV,cO,mO,lambda g:g.pO,'IA #5/#14: empate ≥3,60 → Más 2.5'))
S.append(roi(ou&(d.OddDraw>=2.90)&(d.OddDraw<=3.20),UN,cU,mU,lambda g:1-g.pO,'IA #5: empate 2,90–3,20 → Menos 2.5'))
S.append(roi(ou&(d.OddHome>=2.0)&(d.OddAway>=2.0),UN,cU,mU,lambda g:1-g.pO,'IA #26: ambos ≥2,00 (parejo) → Menos 2.5'))
S.append(roi((d.Division=='D1')&(d.OddDraw>=3.60)&(d.OddDraw<=4.33)&(d.OddHome>=2.0)&(d.OddAway>=2.0),X,cX,mX,lambda g:g.pD,'IA #45: Bundesliga, empate 3,60–4,33, ambos ≥2,00 → Empate'))
S.append(roi((d.Division=='D1')&(d.OddDraw>=3.60)&(d.OddDraw<=4.33)&(d.OddHome>=2.0)&(d.OddAway>=2.0)&(d.h2h_2X==True),X,cX,mX,lambda g:g.pD,'IA #45 completo: + ≥2 empates en los últimos 5 H2H → Empate'))
S.append(roi((d.OddDraw<=3.40)&(d.OddHome>=2.0)&(d.OddAway>=2.0)&(~d.w2_local)&(~d.w2_visita),X,cX,mX,lambda g:g.pD,'IA #420: empate ≤3,40, ambos ≥2,00, nadie con 2 victorias seguidas → Empate (todas las ligas)'))
S.append(roi(d.Division.isin(['ARG','BRA'])&(d.OddDraw<=3.40)&(d.OddHome>=2.0)&(d.OddAway>=2.0)&(~d.w2_local)&(~d.w2_visita),X,cX,mX,lambda g:g.pD,'IA #420 en Argentina/Brasil → Empate'))
S.append(roi(pd.Series(True,index=d.index),X,cX,mX,lambda g:g.pD,'Referencia: Empate en todos'))
fav_h=d.OddHome<d.OddAway
S.append(roi(fav_h,lambda g:g.res=='H',lambda g:g.OddHome,lambda g:g.MaxHome,lambda g:g.pH,'IA #414: favorito local siempre'))
S.append(roi(~fav_h,lambda g:g.res=='A',lambda g:g.OddAway,lambda g:g.MaxAway,lambda g:g.pA,'IA #414: favorito visitante siempre'))
for lo,hi in [(1.0,1.30),(1.30,1.60),(1.60,2.0)]:
    S.append(roi(fav_h&(d.OddHome>lo)&(d.OddHome<=hi),lambda g:g.res=='H',lambda g:g.OddHome,lambda g:g.MaxHome,lambda g:g.pH,f'Favorito local {lo:.2f}–{hi:.2f}'))
for lo,hi in [(3.0,5.0),(5.0,8.0),(8.0,50)]:
    S.append(roi((d.OddAway>lo)&(d.OddAway<=hi),lambda g:g.res=='A',lambda g:g.OddAway,lambda g:g.MaxAway,lambda g:g.pA,f'No favorito visitante {lo:.1f}–{hi:.1f}'))
S.append(roi(d.ultimo_visita,lambda g:g.res=='H',lambda g:g.OddHome,lambda g:g.MaxHome,lambda g:g.pH,'Jeke: contra el último (último de visita → gana el local)'))
S.append(roi(d.ultimo_local,lambda g:g.res=='A',lambda g:g.OddAway,lambda g:g.MaxAway,lambda g:g.pA,'Jeke: contra el último (último de local → gana el visitante)'))
S.append(roi(d.ultimo_local,lambda g:g.res=='H',lambda g:g.OddHome,lambda g:g.MaxHome,lambda g:g.pH,'A favor del último de local'))
S=[s for s in S if s]
# BTTS (no hay cuota de ambos en el archivo): acierto contra la estimación corregida (Poisson del precio + 2,25 pts)
b=pd.read_pickle('val/b_lam.pkl')[['Division','MatchDate','HomeTeam','AwayTeam','pBTTS']]
e=d.merge(b,on=['Division','MatchDate','HomeTeam','AwayTeam'],how='inner')
def btts(m,nombre):
    g=e[m(e)]
    if len(g)<30: return None
    y=g.btts.astype(float); p=g.pBTTS+0.0225
    return dict(sistema=nombre,n=int(len(g)),acierto=round(y.mean(),4),estimada_mercado=round(p.mean(),4),dif_pts=round((y.mean()-p.mean())*100,2),ic95_pts=round(196*y.std()/len(g)**.5,2))
B=[btts(lambda g:(g.OddDraw>=3.90)&(g.OddAway<=2.00)&g.btts2_local,'IA #429: empate ≥3,90, visitante ≤2,00, local con 2 BTTS seguidos → Ambos Sí'),
   btts(lambda g:(g.OddDraw>=3.90)&(g.OddAway<=2.00),'IA #429 sin la racha'),
   btts(lambda g:g.btts2_local,'Local con 2 Ambos Sí seguidos (racha sola)'),
   btts(lambda g:(g.Over25<=1.80),'IA #16 (parcial): Más 2.5 ≤1,80 → Ambos Sí')]
B=[x for x in B if x]
json.dump(dict(sistemas=S,ambos=B),open('val/e_sistemas.json','w'),ensure_ascii=False,indent=1)
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',80)
print(pd.DataFrame(S).to_string()); print(pd.DataFrame(B).to_string())
