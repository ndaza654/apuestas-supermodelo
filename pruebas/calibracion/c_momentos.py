# C. Momentos reales para calibrar el simulador: dispersión y correlaciones condicionadas a la fuerza/goles del mercado.
import numpy as np, pandas as pd, json
x=pd.read_pickle('val/b_lam.pkl')
s=x.dropna(subset=['HomeCorners','AwayCorners','HomeShots','AwayShots','HomeTarget','AwayTarget','HomeFouls','AwayFouls','HomeYellow','AwayYellow','HomeRed','AwayRed']).copy()
s['C']=s.HomeCorners+s.AwayCorners; s['SH']=s.HomeShots+s.AwayShots; s['SOT']=s.HomeTarget+s.AwayTarget; s['F']=s.HomeFouls+s.AwayFouls
s['T']=s.HomeYellow+s.AwayYellow+2*(s.HomeRed+s.AwayRed); s['G']=s.FTHome+s.FTAway; s['GD']=s.FTHome-s.FTAway
s['CD']=s.HomeCorners-s.AwayCorners; s['SD']=s.HomeShots-s.AwayShots; s['TD']=s.HomeTarget-s.AwayTarget
s['G1']=s.HTHome+s.HTAway
print('n con estadísticas',len(s), 'ligas', s.Division.nunique())
# bins por mercado: total esperado y diferencia
s['bt']=pd.cut(s.lh+s.la,[0,2.2,2.5,2.8,3.1,3.5,9]); s['bd']=pd.cut(s.lh-s.la,[-9,-0.8,-0.3,0.3,0.8,1.3,9])
s['bl']=s.Division
grp=['bl','bt','bd']
for v in ['C','SH','SOT','F','T','G','HomeCorners','AwayCorners','HomeYellow','AwayYellow']:
    s[v+'_m']=s.groupby(grp,observed=True)[v].transform('mean')
    s[v+'_r']=s[v]-s[v+'_m']
s=s[s.groupby(grp,observed=True)['C'].transform('size')>=40]
out={}
for v in ['C','SH','SOT','F','T','G','HomeCorners','AwayCorners']:
    vr=(s[v+'_r']**2).mean()*len(s)/(len(s)-s.groupby(grp,observed=True).ngroups); m=s[v].mean()
    out[v]=dict(media=round(m,2),var_sobre_media=round(vr/m,3),sd=round(vr**.5,2))
print('dispersión residual (dentro de liga × goles esperados × diferencia; cota SUPERIOR de la condicional):'); [print(' ',k,v) for k,v in out.items()]
cr=lambda a,b: round(float(np.corrcoef(s[a],s[b])[0,1]),3)
cors={'remates-corners (tot, resid)':cr('SH_r','C_r'),'faltas-tarjetas (tot, resid)':cr('F_r','T_r'),'goles-corners (tot, resid)':cr('G_r','C_r'),
      'goles-tarjetas (tot, resid)':cr('G_r','T_r'),'corners-tarjetas':cr('C_r','T_r'),'faltas-corners':cr('F_r','C_r')}
# diferencias (dominio): residualizar las diferencias también
for v in ['GD','CD','SD','TD']:
    s[v+'_r']=s[v]-s.groupby(grp,observed=True)[v].transform('mean')
cors.update({'dif goles - dif remates':cr('GD_r','SD_r'),'dif goles - dif al arco':cr('GD_r','TD_r'),'dif goles - dif corners':cr('GD_r','CD_r'),
             'corners local - corners visita (resid)':cr('HomeCorners_r','AwayCorners_r')})
print('correlaciones:'); [print(' ',k,v) for k,v in cors.items()]
# tarjetas según margen final
s['ad']=s.GD.abs()
print('tarjetas (y+2r) por |dif final|:',s.groupby(s.ad.clip(upper=3))['T'].mean().round(2).to_dict(), ' corners:',s.groupby(s.ad.clip(upper=3))['C'].mean().round(2).to_dict())
# rojas
print('rojas por equipo y partido %.4f'%((s.HomeRed+s.AwayRed).mean()/2), ' amarillas por equipo %.3f'%((s.HomeYellow+s.AwayYellow).mean()/2))
# goles 1T
print('goles en 1T: %.3f del total'%(s.G1.sum()/s.G.sum()))
xx=x.copy(); xx['G']=xx.FTHome+xx.FTAway; xx['G1']=xx.HTHome+xx.HTAway
print('goles en 1T (todos con HT, n=%d): %.3f'%(len(xx),xx.G1.sum()/xx.G.sum()))
# 2T según el marcador al descanso: goles 2T del que gana/pierde al HT, relativo a su lambda
xx['g2h']=xx.FTHome-xx.HTHome; xx['g2a']=xx.FTAway-xx.HTAway; xx['dht']=xx.HTHome-xx.HTAway
rows=[]
for dv in [-2,-1,0,1,2]:
    m=(xx.dht.clip(-2,2)==dv)
    rows.append((dv,m.sum(),(xx.g2h[m]/xx.lh[m]).mean(),(xx.g2a[m]/xx.la[m]).mean()))
print('goles 2T / lambda del partido, según dif al HT (local):'); [print('  dHT=%+d n=%d local %.3f visita %.3f'%r) for r in rows]
json.dump(dict(dispersion=out,correlaciones=cors),open('val/c_momentos.json','w'),ensure_ascii=False,indent=1)
