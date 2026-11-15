import json, math, sys
from math import exp, factorial
J='/home/claude/apuestas-supermodelo/jornadas/2026-11-15/jugadores/'
def pois_pmf(l,n): return exp(-l)*l**n/factorial(n)
def p_ge(l,n):  # P(X>=n)
    if n<=0: return 1.0
    return 1-sum(pois_pmf(l,i) for i in range(n))
def p_le(l,n):
    if n<0: return 0.0
    return sum(pois_pmf(l,i) for i in range(n+1))
K=2.0
def lam2(E,x1,f=1.0,k=K):  # esperado del partido E (equipo), observado 1T x1 -> lambda 2T
    return f*(k*E/2+x1)/(k+1)
# ---- partidos ----
P={
'ESP-ING':dict(h='España',a='Inglaterra',g=(0,1),xg=(0.21,1.70),
  E=dict(c=(5.3,3.8),sh=(14.55,11.2),sot=(5.3,4.15),tj=(1.22,2.57),f=(12.25,11.2),off=(2.15,1.6),g=(1.85,1.8)),
  o=dict(c=(0,3),sh=(4,6),sot=(0,3),tj=(0,1),off=(1,2)),st=(1.10,0.92)),
'BEL-ITA':dict(h='Bélgica',a='Italia',g=(3,1),xg=(1.86,0.58),
  E=dict(c=(4.5,4.95),sh=(15.4,15.65),sot=(5.4,5.65),tj=(2.25,1.95),g=(1.65,1.6)),
  o=dict(c=(2,2),sh=(13,4),sot=(8,3),tj=(0,1)),st=(0.88,1.12)),
'CRO-CZE':dict(h='Croacia',a='Rep. Checa',g=(1,0),xg=(1.05,0.34),
  E=dict(c=(4.5,4.6),sh=(14.0,10.85),sot=(4.9,3.4),tj=(1.64,1.56),g=(1.8,1.75)),
  o=dict(c=(3,0),sh=(10,4),sot=(3,0),tj=(0,0)),st=(0.95,1.05)),
'FRA-TUR':dict(h='Francia',a='Turquía',g=(0,0),xg=(1.22,0.67),
  E=dict(c=(4.8,4.5),sh=(15.05,13.7),sot=(5.9,3.9),tj=(1.79,2.26),g=(1.8,1.05)),
  o=dict(c=(3,2),sh=(11,7),sot=(5,1),tj=(0,0)),st=(1.0,1.0)),
}
F2={'c':1.0,'sh':1.0,'sot':1.0,'tj':1.12,'f':1.05,'off':1.0,'g':1.0}
def team_lams(m,stat):
    d=P[m];E=d['E'][stat];o=d['o'].get(stat,(0,0));f=F2[stat]
    st=d['st'] if stat in('c','sh','sot') else (1,1)
    if stat=='g':
        return tuple(lam2(E[i],d['xg'][i],f) for i in (0,1))
    return tuple(lam2(E[i],o[i],f*st[i]) for i in (0,1))
rows=[]   # (partido, mercado, lado/linea, cuota, p, nota)
def add(m,mk,lbl,c,p): rows.append((m,mk,lbl,c,p))
def ou_total(m,stat,mk,lines,now,which='t'):
    la,lb=team_lams(m,stat)
    l={'t':la+lb,'h':la,'a':lb}[which]
    for L,co,cu in lines:
        need=int(math.floor(L))+1-now   # 'Más' needs remaining>=need
        pov=p_ge(l,need)
        add(m,mk,f'Más {L}',co,pov);add(m,mk,f'Menos {L}',cu,1-pov)
# ---- goles (score-state aware) ----
def goals_block(m,tot,hg,ag,btts,res2t,ft):
    d=P[m];gh,ga=d['g'];lh,la=team_lams(m,'g')
    # total
    for L,co,cu in tot:
        need=int(math.floor(L))+1-(gh+ga);pov=p_ge(lh+la,need);add(m,'goles total',f'Más {L}',co,pov);add(m,'goles total',f'Menos {L}',cu,1-pov)
    for nm,lst,l,now in (('local',hg,lh,gh),('visitante',ag,la,ga)):
        for L,co,cu in lst:
            need=int(math.floor(L))+1-now;pov=p_ge(l,need);add(m,f'goles {nm}',f'Más {L}',co,pov);add(m,f'goles {nm}',f'Menos {L}',cu,1-pov)
    # BTTS final
    ph=1-pois_pmf(lh,0) if gh==0 else 1.0; pa=1-pois_pmf(la,0) if ga==0 else 1.0
    if btts: add(m,'ambos anotan','Sí',btts[0],ph*pa);add(m,'ambos anotan','No',btts[1],1-ph*pa)
    # ambos 2T
    b2=(1-pois_pmf(lh,0))*(1-pois_pmf(la,0))
    if res2t: add(m,'ambos anotan 2T','Sí',res2t[0],b2);add(m,'ambos anotan 2T','No',res2t[1],1-b2)
    # resultado 2T
    pw=pd=pl=0
    for i in range(12):
        for j in range(12):
            pr=pois_pmf(lh,i)*pois_pmf(la,j)
            if i>j:pw+=pr
            elif i==j:pd+=pr
            else:pl+=pr
    if ft: 
        for nm,c,p in zip(('local','empate','visitante'),ft,(pw,pd,pl)): add(m,'resultado 2T (resto)',nm,c,p)
    return lh,la
# ---- datos Betano (descanso ~15:44-15:49) ----
m='ESP-ING';d=P[m]
goals_block(m,[(1.5,1.11,6.0),(2.5,1.60,2.27),(3.5,2.80,1.42),(4.5,5.70,1.13)],[(0.5,1.37,2.95),(1.5,2.72,1.42),(2.5,6.60,1.09)],[(1.5,1.67,2.12),(2.5,4.30,1.19),(3.5,10.0,1.03)],(1.37,2.95),(2.32,1.57),(2.07,3.00,3.55))
ou_total(m,'c','córners total',[(6.5,1.23,3.80),(7.5,1.52,2.37),(8.5,2.05,1.70),(9.5,2.95,1.35),(10.5,4.5,1.17)],3)
ou_total(m,'c','córners España',[(2.5,1.38,2.75),(3.5,1.93,1.75),(4.5,2.95,1.33)],0,'h')
ou_total(m,'c','córners Inglaterra',[(3.5,1.16,4.45),(4.5,1.72,1.95),(5.5,3.00,1.32)],3,'a')
ou_total(m,'tj','tarjetas total',[(2.5,1.42,2.77),(3.5,2.05,1.72),(4.5,3.30,1.30)],1)
ou_total(m,'tj','tarjetas España',[(0.5,1.45,2.60)],0,'h')
ou_total(m,'tj','tarjetas Inglaterra',[(2.5,2.15,1.65)],1,'a')
ou_total(m,'sh','remates total',[(26.5,1.95,1.75)],10)
ou_total(m,'sh','remates España',[(14.5,1.67,2.07)],4,'h')
ou_total(m,'sh','remates Inglaterra',[(11.5,2.15,1.62)],6,'a')
ou_total(m,'sot','tiros al arco total',[(8.5,1.93,1.78)],3)
ou_total(m,'sot','tiros al arco España',[(3.5,1.87,1.83)],0,'h')
ou_total(m,'sot','tiros al arco Inglaterra',[(4.5,1.65,2.10)],3,'a')
ou_total(m,'off','fueras de juego total',[(4.5,1.62,2.15)],3)
m='BEL-ITA'
goals_block(m,[(4.5,1.15,5.00),(5.5,1.75,2.02),(6.5,3.30,1.30),(7.5,7.0,1.08)],[(3.5,1.47,2.55),(4.5,3.25,1.31),(5.5,8.0,1.06)],[(1.5,1.75,2.02),(2.5,4.60,1.17),(3.5,10.25,1.03)],None,(2.62,1.45),(2.27,2.80,3.30))
ou_total(m,'c','córners total',[(7.5,1.33,3.05),(8.5,1.75,1.98),(9.5,2.50,1.47),(10.5,3.80,1.22)],4)
ou_total(m,'c','córners Bélgica',[(3.5,1.55,2.27),(4.5,2.57,1.42),(5.5,4.70,1.14)],2,'h')
ou_total(m,'c','córners Italia',[(3.5,1.24,3.50),(4.5,1.72,1.95),(5.5,2.77,1.37)],2,'a')
ou_total(m,'tj','tarjetas total',[(2.5,1.36,3.00),(3.5,1.93,1.82),(4.5,3.00,1.36)],1)
ou_total(m,'tj','tarjetas Bélgica',[(1.5,2.07,1.70)],0,'h')
ou_total(m,'tj','tarjetas Italia',[(2.5,2.70,1.42)],1,'a')
m='CRO-CZE'
goals_block(m,[(1.5,1.18,4.40),(2.5,1.88,1.83),(3.5,3.70,1.24),(4.5,7.9,1.06)],[(1.5,1.38,2.90),(2.5,2.77,1.40),(3.5,6.8,1.08)],[(0.5,2.37,1.55),(1.5,8.0,1.06)],(2.37,1.55),(3.30,1.30),(1.78,2.82,5.40))
ou_total(m,'c','córners total',[(5.5,1.21,3.90),(6.5,1.55,2.30),(7.5,2.18,1.62),(8.5,3.35,1.28),(9.5,5.40,1.12)],3)
ou_total(m,'c','córners Croacia',[(4.5,1.47,2.47),(5.5,2.35,1.50),(6.5,4.20,1.18)],3,'h')
ou_total(m,'c','córners Rep. Checa',[(1.5,1.57,2.22),(2.5,2.60,1.42),(3.5,4.75,1.14)],0,'a')
ou_total(m,'tj','tarjetas total',[(1.5,1.45,2.60),(2.5,2.15,1.65),(3.5,3.55,1.27)],0)
ou_total(m,'tj','tarjetas Croacia',[(0.5,1.47,2.55)],0,'h')
ou_total(m,'tj','tarjetas Rep. Checa',[(1.5,2.30,1.57)],0,'a')
m='FRA-TUR'
goals_block(m,[(0.5,1.07,7.60),(1.5,1.40,2.82),(2.5,2.20,1.62),(3.5,4.05,1.21),(4.5,7.9,1.06)],[(0.5,1.12,5.60),(1.5,1.65,2.18),(2.5,2.95,1.37),(3.5,6.10,1.10)],[(0.5,2.60,1.45),(1.5,9.0,1.04)],(2.95,1.36),None,None)
ou_total(m,'c','córners total',[(8.5,1.23,3.75),(9.5,1.52,2.37),(10.5,2.07,1.67),(11.5,3.00,1.34),(12.5,4.50,1.17)],5)
ou_total(m,'c','córners Francia',[(5.5,1.31,3.05),(6.5,1.75,1.93),(7.5,2.62,1.42)],3,'h')
ou_total(m,'c','córners Turquía',[(2.5,1.22,3.70),(3.5,1.98,1.72),(4.5,3.80,1.21)],2,'a')
ou_total(m,'tj','tarjetas total',[(1.5,1.50,2.50),(2.5,2.30,1.57),(3.5,3.85,1.24)],0)
ou_total(m,'tj','tarjetas Francia',[(0.5,1.67,2.12)],0,'h')
ou_total(m,'tj','tarjetas Turquía',[(1.5,2.12,1.67)],0,'a')
# ---- jugadores ----
IDX={'sh':3,'sot':4,'f':9,'tk':12,'sv':11}
NAMEKEY={'ESP-ING':'espana-inglaterra','BEL-ITA':'belgica-italia','CRO-CZE':'croacia-republica-checa','FRA-TUR':'francia-turquia'}
import unicodedata
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
def hist(m,last):
    j=json.load(open(J+NAMEKEY[m]+'.json'));last=norm(last)
    c=[(k,v) for k,v in j.items() if last in norm(k).split(' #')[0].replace('.','').split() or norm(k).startswith(last)]
    if not c: c=[(k,v) for k,v in j.items() if last in norm(k)]
    return c
PL=[]
def pj(m,stat,name,team,cnt,lines):PL.append((m,stat,name,team,cnt,lines))
def L(s): return [(int(a.split(':')[0]),float(a.split(':')[1])) for a in s.split(',')]
# ESP-ING
for args in [
('sh','Yamal','L',1,'3:1.21,4:1.62,5:2.52'),('sh','Kane','V',2,'3:1.32,4:2.35,5:5.30'),('sh','Bellingham','V',2,'3:1.37,4:2.55,5:6.10'),('sh','Porro','L',2,'3:1.75,4:4.60'),
('sh','Merino','L',1,'2:1.14,3:1.65,4:2.90'),('sh','Oyarzabal','L',0,'2:1.27,3:1.78,4:2.77'),('sh','Gordon','V',1,'2:1.60,3:3.65'),('sh','Rogers','V',1,'2:1.75,3:4.50'),
('sh','Baena','L',0,'1:1.08,2:1.47,3:2.30'),('sh','Ruiz','L',0,'1:1.39,2:2.60'),('sh','Zubimendi','L',0,'1:1.67,2:4.15'),
('sot','Bellingham','V',2,'3:2.10,4:6.60'),('sot','Kane','V',1,'2:1.67,3:4.20'),('sot','Oyarzabal','L',0,'1:1.47,2:3.10'),('sot','Yamal','L',0,'1:1.50,2:3.15'),('sot','Baena','L',0,'1:1.70'),('sot','Merino','L',0,'1:1.78'),('sot','Gordon','V',0,'1:2.37'),
('f','Porro','L',3,'4:1.37,5:2.55'),('f','Anderson','V',2,'3:1.67,4:4.15'),('f','Rogers','V',2,'3:1.91'),('f','Merino','L',1,'2:1.27,3:2.18'),('f','Oyarzabal','L',1,'2:1.39'),('f','Hall','V',1,'2:1.39'),('f','Baena','L',1,'2:1.40'),('f','Cucurella','L',1,'2:1.45'),('f','Yamal','L',0,'1:1.50'),
('sv','Simón','L',2,'3:1.47,4:3.05,5:7.70'),('sv','Trafford','V',0,'2:1.35,3:2.02,4:3.40'),
]:
    s,n,lado,c,ls=args; pj('ESP-ING',s,n,lado,c,L(ls))
for s,n,lado,c,ls in [
('sh','Bruyne','L',3,'4:1.10,5:1.50,6:2.37,7:4.55'),('sh','Moreira','L',2,'3:1.33,4:2.37,5:5.40'),('sh','Doku','L',2,'3:1.37,4:2.52,5:6.00'),('sh','Pisilli','V',2,'3:1.62,4:3.80'),('sh','Ngoy','L',2,'3:2.65,4:9.75'),
('sh','Esposito','V',1,'2:1.13,3:1.67,4:2.85,5:6.00'),('sh','Ketelaere','L',1,'2:1.36,3:2.50'),('sh','Cuyper','L',1,'2:1.65,3:4.00'),('sh','Fagioli','V',1,'2:1.83'),('sh','Lavia','L',1,'2:1.95'),
('sh','Koleosho','V',0,'1:1.33,2:2.42'),('sh','Tielemans','L',0,'1:1.36,2:2.50'),('sh','Tonali','V',0,'1:1.75'),('sh','Barella','V',0,'1:1.83'),
('sot','Bruyne','L',2,'3:1.78,4:4.80'),('sot','Doku','L',2,'3:2.72,4:10.25'),('sot','Esposito','V',1,'2:1.60,3:3.60'),('sot','Cuyper','L',1,'2:2.90'),('sot','Koleosho','V',0,'1:2.57'),('sot','Moreira','L',0,'1:2.72'),('sot','Tielemans','L',0,'1:2.77')]:
    pj('BEL-ITA',s,n,lado,c,L(ls))
for s,n,lado,c,ls in [
('sh','Beljo','L',2,'3:1.14,4:1.65,5:2.87'),('sh','Hlozek','V',2,'3:1.36,4:2.50,5:5.90'),('sh','Hopi','V',2,'3:1.52,4:3.05'),('sh','Caleta','L',2,'3:2.22,4:7.30'),('sh','Kovacic','L',1,'2:1.44,3:2.77'),('sh','Vuskovic','L',1,'2:2.05'),
('sh','Kabongo','V',0,'1:1.32,2:2.40'),('sh','Baturina','L',0,'1:1.38,2:2.57'),('sh','Sadilek','V',0,'1:1.65'),('sh','Modric','L',0,'1:1.72'),('sh','Cerv','V',0,'1:1.85'),
('sot','Beljo','L',1,'2:1.75,3:4.55'),('sot','Perisic','L',1,'2:2.07,3:6.40'),('sot','Hlozek','V',0,'1:2.40'),('sot','Kabongo','V',0,'1:2.55'),('sot','Baturina','L',0,'1:2.60')]:
    pj('CRO-CZE',s,n,lado,c,L(ls))
for s,n,lado,c,ls in [
('sh','Mbappé','L',2,'5:1.23,6:1.60,7:2.30'),('sh','Olise','L',2,'3:1.12,4:1.62,5:2.85'),('sh','Barcola','L',2,'3:1.14,4:1.72,5:3.10'),('sh','Güler','V',2,'3:1.24,4:2.05,5:4.20'),('sh','Rabiot','L',3,'4:1.39,5:2.60'),
('sh','Cherki','L',1,'2:1.25,3:2.12,4:4.45'),('sh','Diouf','L',1,'2:1.50,3:3.20'),('sh','Yilmaz','V',1,'2:1.87'),('sh','Calhanoglu','V',0,'1:1.50,2:3.00'),('sh','Da Cunha','L',0,'1:1.50,2:3.20'),('sh','Uzun','V',0,'1:1.62'),
('sot','Mbappé','L',2,'3:1.12,4:1.65,5:2.92'),('sot','Olise','L',1,'2:1.85,3:5.10'),('sot','Barcola','L',1,'2:1.91'),('sot','Güler','V',0,'1:1.82'),('sot','Cherki','L',0,'1:2.18')]:
    pj('FRA-TUR',s,n,lado,c,L(ls))
out=[]
for m,stat,name,lado,cnt,lines in PL:
    c=hist(m,name)
    c=[x for x in c if x[1]['lado']==lado]
    if not c: out.append((m,stat,name,'SIN HISTORIAL',cnt,None));continue
    k,v=c[0]
    games=[h for h in v['p'] if h[2]>0]
    if not games: out.append((m,stat,k,'SIN MIN',cnt,None));continue
    mins=sum(h[2] for h in games);tot=sum(h[IDX[stat]] for h in games);n=len(games)
    avg=mins/n;rate90=tot/mins*90
    m2=max(15,min(45,avg-45+8)) if stat!='sv' else 45   # minutos esperados 2T
    d=P[m];stt=d['st'][0 if lado=='L' else 1] if stat in('sh','sot') else 1.0
    prior=rate90*m2/90*stt
    # actualiza con 1T: peso 0.25 del ritmo observado
    obs=cnt/45*m2*stt
    lam=0.75*prior+0.25*obs
    for ln,co in lines:
        need=ln-cnt
        p=p_ge(lam,need)
        out.append((m,stat,k,lado,cnt,(ln,co,p,lam,rate90,avg,n,tot)))
json.dump({'rows':rows,'pl':[o for o in out]},open('res.json','w'))
print(len(rows),len(out))
