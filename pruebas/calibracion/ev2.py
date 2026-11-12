import numpy as np, pandas as pd, sys
df=pd.read_pickle(sys.argv[1]).dropna(subset=['oH','oD','oA']).copy()
o=1/df[['oH','oD','oA']].values; mk=o/o.sum(1,keepdims=True); marg=o.sum(1)-1
df['mH'],df['mD'],df['mA']=mk.T
res=np.where(df.gh>df.ga,0,np.where(df.gh==df.ga,1,2)); Y=np.eye(3)[res]
M=mk; P=df[['pH','pD','pA']].values
def ll(p): return -np.log(p[np.arange(len(p)),res])
def br(p): return ((p-Y)**2).sum(1)
print('n',len(df),'margen medio %.3f'%marg.mean())
print('1X2   modelo LL %.4f Br %.4f | mercado(sin margen) LL %.4f Br %.4f'%(ll(P).mean(),br(P).mean(),ll(M).mean(),br(M).mean()))
for w in [0,.1,.2,.3,.5,.7,1]:
    B=(1-w)*M+w*P; d=ll(B)-ll(M); print(f' mezcla w_modelo={w:.1f}: LL {ll(B).mean():.4f} Br {br(B).mean():.4f}  dLL vs mercado {d.mean():+.4f} ± {d.std(ddof=1)/len(d)**.5:.4f}')
print('por liga (modelo vs mercado LL):')
for l,g in df.groupby('div'):
    i=g.index; ii=np.where(df['div'].values==l)[0]
    print(' ',l,len(g),'%.4f vs %.4f'%(ll(P)[ii].mean(),ll(M)[ii].mean()))
# value: apostar donde modelo > mercado por >= edge (EV con la cuota ofrecida)
odds=df[['oH','oD','oA']].values
print('ROI plano apostando donde EV_modelo >= umbral (cuota Bet365/promedio del archivo):')
for th in [0,.03,.06,.10]:
    pn=0;st=0
    for k in range(3):
        ev=P[:,k]*odds[:,k]-1; m=ev>=th
        pn+=((Y[:,k]*odds[:,k]-1)[m]).sum(); st+=m.sum()
    print(f'  EV>={th:.2f}: apuestas {st} ROI {pn/max(st,1):+.3%}')
print('referencia: apostar a todo 1X2 sin criterio ROI %.3f%%'%(100*np.mean([ (Y[:,k]*odds[:,k]-1).mean() for k in range(3)])))
# totales
g=df.dropna(subset=['oOv','oUn']).copy()
oo=1/g[['oOv','oUn']].values; mo=oo[:,0]/oo.sum(1); y=((g.gh+g.ga)>=3).astype(float).values
b=lambda p:(p-y)**2; l2=lambda p:-np.log(np.where(y==1,p,1-p))
pm=g.pOv.values
print('\nO/U 2.5 n',len(g),'  Brier modelo %.4f mercado %.4f naive(base) %.4f'%(b(pm).mean(),b(mo).mean(),b(np.full(len(y),y.mean())).mean()))
for w in [0,.1,.2,.3,.5]:
    B=(1-w)*mo+w*pm; dd=l2(B)-l2(mo); print(f' mezcla w={w:.1f}: Br {b(B).mean():.4f} dLL vs mercado {dd.mean():+.4f} ± {dd.std(ddof=1)/len(dd)**.5:.4f}')
