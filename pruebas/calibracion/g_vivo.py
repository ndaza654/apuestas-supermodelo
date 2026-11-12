# G. Validación del modo en vivo: desde el marcador real al descanso, ¿acierta el final? (300 partidos reales)
import sys, numpy as np, pandas as pd, json
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from supermodelo.simulador import Partido
x=pd.read_pickle('val/b_lam.pkl')
s=x.dropna(subset=['HomeCorners','AwayCorners','HomeShots','AwayShots','HomeTarget','AwayTarget','HomeFouls','AwayFouls','HomeYellow','AwayYellow']).copy()
s['bt']=pd.cut(s.lh+s.la,[0,2.2,2.5,2.8,3.1,3.5,9]); s['bd']=pd.cut(s.lh-s.la,[-9,-0.8,-0.3,0.3,0.8,1.3,9])
cols={'c':('HomeCorners','AwayCorners'),'sh':('HomeShots','AwayShots'),'sot':('HomeTarget','AwayTarget'),'f':('HomeFouls','AwayFouls'),'y':('HomeYellow','AwayYellow')}
for k,(h,a) in cols.items():
    s[k+'_h']=s.groupby(['bt','bd'],observed=True)[h].transform('mean'); s[k+'_a']=s.groupby(['bt','bd'],observed=True)[a].transform('mean')
m=s.sample(int(sys.argv[1]),random_state=11)
from supermodelo import config as C
if len(sys.argv)>2: C.VIVO_FORMA_GOLES=float(sys.argv[2])
rows=[]
for i,(_,r) in enumerate(m.iterrows()):
    obj=[dict(g=r.lh,sh=r.sh_h,sot=r.sot_h,c=r.c_h,f=r.f_h,y=r.y_h),dict(g=r.la,sh=r.sh_a,sot=r.sot_a,c=r.c_a,f=r.f_a,y=r.y_a)]
    est={'mitad':2,'minuto':45,'goles':[int(r.HTHome),int(r.HTAway)],'goles_1t':[int(r.HTHome),int(r.HTAway)]}
    R=Partido(obj,n=1500,seed=i,estado=est).res
    gh,ga=R[0]['g'],R[1]['g']
    rows.append(dict(ht=f'{int(r.HTHome)}-{int(r.HTAway)}',pO=((gh+ga)>=3).mean(),pB=((gh>0)&(ga>0)).mean(),p1=(gh>ga).mean(),pX=(gh==ga).mean(),
                     g2=(gh+ga).mean()-r.HTHome-r.HTAway,yO=int(r.FTHome+r.FTAway>=3),yB=int(r.FTHome>0 and r.FTAway>0),y1=int(r.FTHome>r.FTAway),yX=int(r.FTHome==r.FTAway),
                     y2=r.FTHome+r.FTAway-r.HTHome-r.HTAway))
d=pd.DataFrame(rows); d.to_pickle('val/g_vivo_%s.pkl'%(sys.argv[2] if len(sys.argv)>2 else 'def'))
print('n',len(d))
for p,y in [('pO','yO'),('pB','yB'),('p1','y1'),('pX','yX'),('g2','y2')]:
    print(f'{p}: predicho {d[p].mean():.3f} real {d[y].mean():.3f}  ± {d[y].std()/len(d)**.5:.3f}' + ('' if p=='g2' else f'  Brier {((d[p]-d[y])**2).mean():.4f} vs base {((d[y].mean()-d[y])**2).mean():.4f}'))
d['grp']=d.ht.map(lambda s: s if s in ('0-0','1-0','0-1','1-1') else 'otro')
print(d.groupby('grp').agg(n=('yO','size'),g2=('g2','mean'),y2=('y2','mean'),pO=('pO','mean'),yO=('yO','mean'),p1=('p1','mean'),y1=('y1','mean')).round(3))
