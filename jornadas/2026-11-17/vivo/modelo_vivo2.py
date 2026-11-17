"""Valoración en vivo 2º tiempo (17-nov-2026 ~16:05 Bogotá). Ritmo = mezcla del esperado de la ficha (por minuto) y el ritmo en vivo; peso del vivo = min/(min+60)."""
import math
import sys,os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from modelo_vivo import p_ge
LATE={'corners':1.07,'cards':1.12,'goals':1.0}
DISP={'corners':1.35,'cards':1.35,'goals':1.0}
def mu(kind,E_full,obs,minute,xg=None):
    prior=E_full/93; live=(xg if (kind=='goals' and xg is not None) else obs)/max(minute,1)
    w=minute/(minute+60); rate=(1-w)*prior+w*live
    return rate*max(93-minute,0)*LATE[kind]
def ev(nombre,kind,E_full,have,obs,minute,lines,xg=None,mult=1.0):
    m=mu(kind,E_full,obs,minute,xg)*mult;d=DISP[kind];out=[]
    for side,L,odds in lines:
        need=math.floor(L)+1-have; pm=p_ge(need,m,d); p=pm if side=='Más' else 1-pm
        out.append((nombre,side,L,odds,round(p,3),round(p*odds-1,3),round(m,2)))
    return out
R=[]
def add(*a,**k): R.extend(ev(*a,**k))
# DIN-NOR min 60: corners 1-7, cards 2, goles 3 xG 3.66
add('DIN-NOR corners total','corners',10.6,8,8,60,[('Más',10.5,1.22),('Más',11.5,1.57),('Menos',11.5,2.25),('Más',12.5,2.25),('Menos',12.5,1.57)])
add('DIN-NOR corners Noruega','corners',4.7,7,7,60,[('Más',8.5,1.21),('Más',9.5,1.65),('Menos',9.5,2.07),('Más',10.5,2.55),('Menos',10.5,1.44)])
add('DIN-NOR corners Dinamarca','corners',5.9,1,1,60,[('Más',1.5,1.35),('Más',2.5,2.55),('Menos',2.5,1.44),('Más',3.5,5.10)])
add('DIN-NOR tarjetas total','cards',3.9,2,2,60,[('Más',3.5,1.55),('Menos',3.5,2.35),('Más',4.5,2.40),('Menos',4.5,1.53)])
add('DIN-NOR goles total','goals',3.95,3,3,60,[('Más',3.5,1.27),('Más',4.5,2.30),('Menos',4.5,1.57),('Más',5.5,5.20)],xg=3.66)
# IRL-KOS min 60: Kosovo 10 hombres; corners 7 (6-1); cards 5; goles 2 xG 3.83
add('IRL-KOS corners total','corners',8.45,7,7,60,[('Más',8.5,1.20),('Más',9.5,1.60),('Menos',9.5,2.20),('Más',10.5,2.50),('Menos',10.5,1.47)])
add('IRL-KOS corners Irlanda','corners',4.3,6,6,60,[('Más',7.5,1.50)])
add('IRL-KOS tarjetas total','cards',4.46,5,5,60,[('Más',6.5,1.60),('Menos',6.5,2.25)],mult=1.1)
add('IRL-KOS goles total','goals',2.25,2,2,60,[('Más',2.5,1.30),('Más',3.5,2.40),('Menos',3.5,1.52),('Más',4.5,5.40)],xg=3.83)
# WAL-POR min 61: corners 2-1; cards 2; goles 4 xG 2.35
add('WAL-POR corners total','corners',9.75,3,3,61,[('Más',5.5,1.42),('Menos',5.5,2.65),('Más',6.5,2.05),('Menos',6.5,1.70),('Más',7.5,3.25),('Menos',7.5,1.30)])
add('WAL-POR corners Gales','corners',4.85,2,2,61,[('Más',2.5,1.31),('Más',3.5,2.35),('Menos',3.5,1.50)])
add('WAL-POR corners Portugal','corners',4.9,1,1,61,[('Más',2.5,1.47),('Menos',2.5,2.45),('Más',3.5,2.35),('Menos',3.5,1.50)])
add('WAL-POR tarjetas total','cards',3.4,2,2,61,[('Más',3.5,1.55),('Menos',3.5,2.35),('Más',4.5,2.40),('Menos',4.5,1.53)])
add('WAL-POR goles total','goals',2.95,4,4,61,[('Más',4.5,1.22),('Menos',4.5,3.95),('Más',5.5,2.00),('Menos',5.5,1.75)],xg=2.35)
# UKR-GEO min 62: corners 1-9; cards 2; goles 1 xG 1.13
add('UKR-GEO corners total','corners',8.65,10,10,62,[('Más',12.5,1.50),('Menos',12.5,2.42),('Más',13.5,2.18),('Menos',13.5,1.62),('Más',14.5,3.55)])
add('UKR-GEO corners Georgia','corners',4.45,9,9,62,[('Más',11.5,2.37)])
add('UKR-GEO corners Ucrania','corners',4.2,1,1,62,[('Más',1.5,1.44)])
add('UKR-GEO tarjetas total','cards',3.95,2,2,62,[('Más',4.5,2.32),('Menos',4.5,1.57)])
add('UKR-GEO goles total','goals',2.5,1,1,62,[('Más',1.5,1.55),('Menos',1.5,2.32),('Más',2.5,3.60),('Menos',2.5,1.25)],xg=1.13)
# ISR-AUT min 62 1-1: corners 1-6; cards 0; goles 2 xG 1.88
add('ISR-AUT corners total','corners',7.65,7,7,62,[('Más',9.5,1.45),('Menos',9.5,2.57),('Más',10.5,2.12),('Menos',10.5,1.65),('Más',11.5,3.40)])
add('ISR-AUT corners Austria','corners',4.1,6,6,62,[('Más',8.5,1.95)])
add('ISR-AUT corners Israel','corners',3.55,1,1,62,[('Más',1.5,1.70)])
add('ISR-AUT tarjetas total','cards',3.9,0,0,62,[('Más',1.5,1.85),('Menos',1.5,1.88)],mult=1.0)
add('ISR-AUT goles total','goals',3.35,2,2,62,[('Más',2.5,1.32),('Más',3.5,2.45),('Menos',3.5,1.50),('Más',4.5,5.60)],xg=1.88)
# POL-SWE min 62 1-1: corners 0-5; cards 1; goles 2 xG 2.0
add('POL-SWE corners total','corners',8.5,5,5,62,[('Más',7.5,1.52),('Menos',7.5,2.37),('Más',8.5,2.25),('Menos',8.5,1.57),('Más',9.5,3.70)])
add('POL-SWE corners Polonia','corners',5.35,0,0,62,[('Más',1.5,1.93)])
add('POL-SWE corners Suecia','corners',3.15,5,5,62,[('Más',6.5,1.93)])
add('POL-SWE tarjetas total','cards',4.4,1,1,62,[('Más',2.5,1.72),('Menos',2.5,2.05)])
add('POL-SWE goles total','goals',3.4,2,2,62,[('Más',2.5,1.37),('Más',3.5,2.67),('Menos',3.5,1.42),('Más',4.5,6.40)],xg=2.0)
if __name__=='__main__':
    for r in sorted(R,key=lambda r:-r[5]):
        if r[3]>=1.45 and r[5]>0.03: print(r)
