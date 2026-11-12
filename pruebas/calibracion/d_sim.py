# D. Medir el simulador con los mismos momentos que los datos reales. Uso: python3 val/d_sim.py [json con overrides de config]
import sys, json, numpy as np, pandas as pd
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import importlib
pk = 'supermodelo'
C = importlib.import_module(pk+'.config'); SIM = importlib.import_module(pk+'.simulador')
ov = json.loads(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1] not in ('', '-') else {}
for k,v in ov.items():
    if isinstance(v,dict): getattr(C,k).update(v)
    else: setattr(C,k,v)
from scipy.stats import poisson
rng=np.random.default_rng(3)
x=pd.read_pickle('val/b_lam.pkl')
s=x.dropna(subset=['HomeCorners','AwayCorners','HomeShots','AwayShots','HomeTarget','AwayTarget','HomeFouls','AwayFouls','HomeYellow','AwayYellow']).copy()
s['bt']=pd.cut(s.lh+s.la,[0,2.2,2.5,2.8,3.1,3.5,9]); s['bd']=pd.cut(s.lh-s.la,[-9,-0.8,-0.3,0.3,0.8,1.3,9])
cols={'c':('HomeCorners','AwayCorners'),'sh':('HomeShots','AwayShots'),'sot':('HomeTarget','AwayTarget'),'f':('HomeFouls','AwayFouls'),'y':('HomeYellow','AwayYellow')}
for k,(h,a) in cols.items():
    s[k+'_h']=s.groupby(['bt','bd'],observed=True)[h].transform('mean'); s[k+'_a']=s.groupby(['bt','bd'],observed=True)[a].transform('mean')
muestra=s.sample(24,random_state=5)
N=int(ov.get('_n',8000))
acc=dict(dB=[],dX=[],dH0=[],dA0=[],d00=[],g1=[],corrSH=[],corrSOT=[],corrC=[],vC=[],vCt=[],vSH=[],vSOT=[],vF=[],vT=[],vY=[],vG=[],vYt=[],vFt=[],
         rSHC=[],rFT=[],rFC=[],rGC=[],rCC=[],T0=[],T1=[],T2=[],T3=[],rojas=[],y1=[],tr2=[],ld2=[])
for _,m in muestra.iterrows():
    obj=[dict(g=m.lh,sh=m.sh_h,sot=m.sot_h,c=m.c_h,f=m.f_h,y=m.y_h),dict(g=m.la,sh=m.sh_a,sot=m.sot_a,c=m.c_a,f=m.f_a,y=m.y_a)]
    P=SIM.Partido(obj,n=N,seed=int(rng.integers(1e6))); R=P.res
    gh,ga=R[0]['g'],R[1]['g']; lh,la=gh.mean(),ga.mean()
    K=np.arange(13); M=np.outer(poisson.pmf(K,lh),poisson.pmf(K,la))
    acc['dB'].append(((gh>0)&(ga>0)).mean()-(1-np.exp(-lh))*(1-np.exp(-la))); acc['dX'].append((gh==ga).mean()-np.trace(M))
    acc['dH0'].append((gh==0).mean()-np.exp(-lh)); acc['dA0'].append((ga==0).mean()-np.exp(-la)); acc['d00'].append(((gh==0)&(ga==0)).mean()-np.exp(-lh-la))
    G=gh+ga; acc['g1'].append((R[0]['g1']+R[1]['g1']).sum()/max(G.sum(),1))
    cc=lambda a,b: np.corrcoef(a,b)[0,1]
    acc['corrSH'].append(cc(gh-ga,R[0]['sh']-R[1]['sh'])); acc['corrSOT'].append(cc(gh-ga,R[0]['sot']-R[1]['sot'])); acc['corrC'].append(cc(gh-ga,R[0]['c']-R[1]['c']))
    Ct=R[0]['c']+R[1]['c']; SH=R[0]['sh']+R[1]['sh']; SOT=R[0]['sot']+R[1]['sot']; F=R[0]['f']+R[1]['f']; T=R[0]['tarjetas']+R[1]['tarjetas']; Y=R[0]['y']+R[1]['y']
    vm=lambda z: z.var()/z.mean()
    acc['vCt'].append(vm(Ct)); acc['vC'].append((vm(R[0]['c'])+vm(R[1]['c']))/2); acc['vSH'].append(vm(SH)); acc['vSOT'].append(vm(SOT)); acc['vF'].append(vm(F)); acc['vT'].append(vm(T)); acc['vY'].append(vm(Y)); acc['vG'].append(vm(G))
    acc['vYt'].append((vm(R[0]['y'])+vm(R[1]['y']))/2); acc['vFt'].append((vm(R[0]['f'])+vm(R[1]['f']))/2)
    acc['rSHC'].append(cc(SH,Ct)); acc['rFT'].append(cc(F,T)); acc['rFC'].append(cc(F,Ct)); acc['rGC'].append(cc(G,Ct)); acc['rCC'].append(cc(R[0]['c'],R[1]['c']))
    ad=np.abs(gh-ga)
    for k in range(4): acc[f'T{k}'].append(T[np.minimum(ad,3)==k].mean()/T.mean())
    acc.setdefault('rGS',[]).append(cc(G,SH)); acc.setdefault('rGSOT',[]).append(cc(G,SOT)); acc.setdefault('rgsh',[]).append((cc(gh,R[0]['sh'])+cc(ga,R[1]['sh']))/2); acc.setdefault('rgc',[]).append((cc(gh,R[0]['c'])+cc(ga,R[1]['c']))/2); acc.setdefault('rshc',[]).append((cc(R[0]['sh'],R[0]['c'])+cc(R[1]['sh'],R[1]['c']))/2); acc.setdefault('rgl_shv',[]).append((cc(gh,R[1]['sh'])+cc(ga,R[0]['sh']))/2)
    acc.setdefault('C0',[]).append(Ct[ad==0].mean()/Ct.mean()); acc.setdefault('C3',[]).append(Ct[ad>=3].mean()/Ct.mean())
    acc['rojas'].append((R[0]['r']+R[1]['r']).mean()/2); acc['y1'].append((R[0]['y1']+R[1]['y1']).sum()/max(Y.sum(),1))
    # 2T según el marcador al descanso (local), relativo a la media de goles 2T del local en empate
    d1=R[0]['g1']-R[1]['g1']; g2h=gh-R[0]['g1']; g2a=ga-R[1]['g1']
    lvl=g2h[d1==0].mean(); lvla=g2a[d1==0].mean()
    acc['tr2'].append((g2h[d1==-1].mean()/lvl + g2a[d1==1].mean()/lvla)/2); acc['ld2'].append((g2h[d1==1].mean()/lvl + g2a[d1==-1].mean()/lvla)/2)
REAL=dict(dB=0.0225,dX=0.0194,dH0=-0.0104,dA0=-0.0113,d00=0.0008,g1=0.443,corrSH=0.138,corrSOT=0.502,corrC=-0.116,vCt=1.107,vC=1.34,vSH=1.176,vSOT=1.052,vF=1.063,vT=1.229,vY=0.977,vG=0.948,
          vYt=0.853,vFt=0.966,rSHC=0.282,rFT=0.287,rFC=-0.129,rGC=-0.042,rCC=-0.175,T0=4.57/4.44,T1=4.67/4.44,T2=4.22/4.44,T3=3.66/4.44,rojas=0.099,y1=0.35,C0=10.01/9.86,C3=9.52/9.86,rGS=0.228,rGSOT=0.517,rgsh=0.183,rgc=-0.075,rshc=0.413,rgl_shv=0.031,tr2=1.13,ld2=0.98)
print(f"{'momento':8s} {'sim':>8s} {'real':>8s}")
err=0
for k,v in acc.items():
    sv=float(np.nanmean(v)); rv=REAL[k]; print(f'{k:8s} {sv:8.3f} {rv:8.3f} {"  <--" if abs(sv-rv)>max(0.15*abs(rv),0.01) else ""}')
