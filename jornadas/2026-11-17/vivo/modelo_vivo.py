"""Valoración de líneas EN VIVO al descanso (17-nov-2026 ~15:40 Bogotá).
Modelo: restante ~ Binomial negativa / Poisson con media = mezcla de lo esperado por la ficha (parte de la 2ª parte) y el ritmo del 1T.
No es apuesta: solo p y EV frente a la cuota de Betano en vivo."""
import math,json,sys
def pmf_nb(k,mu,disp):
    if disp<=1.0001: return math.exp(-mu+k*math.log(mu)-math.lgamma(k+1)) if mu>0 else (1.0 if k==0 else 0.0)
    r=mu/(disp-1); p=r/(r+mu)
    return math.exp(math.lgamma(k+r)-math.lgamma(r)-math.lgamma(k+1)+r*math.log(p)+k*math.log(1-p))
def p_ge(n,mu,disp):  # P(X>=n)
    if n<=0: return 1.0
    return 1-sum(pmf_nb(k,mu,disp) for k in range(n))
SH={'corners':(0.54,0.30,1.35),'cards':(0.58,0.20,1.35),'goals':(0.54,0.40,1.0)}
def lam(kind,E_full,obs1h,xg1h=None):
    sh,w,d=SH[kind]
    live=obs1h*1.05 if kind!='goals' else (xg1h if xg1h is not None else obs1h)*1.1
    return (1-w)*E_full*sh+w*live,d
def evalua(nombre,kind,E_full,have,obs1h,lines,xg=None,mult=1.0):
    mu,d=lam(kind,E_full,obs1h,xg);mu*=mult;out=[]
    for side,L,odds in lines:
        need=math.floor(L)+1-have   # Más: total final >= floor(L)+1
        pm=p_ge(need,mu,d); p=pm if side=='Más' else 1-pm
        out.append((nombre,side,L,odds,round(p,3),round(p*odds-1,3),round(mu,2)))
    return out
R=[]
def add(*a,**k): R.extend(evalua(*a,**k))
# ===== DIN-NOR 2-1 (corners 1-6, cards pts 0-1, goles 3, xG 3.06)
add('DIN-NOR corners total','corners',10.6,7,6,[('Más',11.5,1.45),('Menos',11.5,2.55),('Más',12.5,1.93),('Menos',12.5,1.78),('Más',13.5,2.75),('Menos',13.5,1.40)])
add('DIN-NOR corners Noruega','corners',4.7,6,6,[('Más',8.5,1.42),('Menos',8.5,2.62),('Más',9.5,2.0),('Menos',9.5,1.70),('Más',10.5,3.15)])
add('DIN-NOR corners Dinamarca','corners',5.9,1,1,[('Más',2.5,1.52),('Menos',2.5,2.32),('Más',3.5,2.5),('Menos',3.5,1.45)])
add('DIN-NOR goles total','goals',3.95,3,3,[('Más',3.5,1.11),('Más',4.5,1.57),('Menos',4.5,2.30),('Más',5.5,2.72),('Menos',5.5,1.42)],xg=3.06)
add('DIN-NOR tarjetas total','cards',3.9,1,1,[('Más',2.5,1.35),('Menos',2.5,3.05),('Más',3.5,1.88),('Menos',3.5,1.85),('Más',4.5,2.87),('Menos',4.5,1.38)])
# ===== IRL-KOS 1-0 (Kosovo 10 hombres; corners 4-1; cards pts: IRL 2, KOS 1+2=3 → 5; goles 1; xG 1.90)
add('IRL-KOS corners total','corners',8.45,5,5,[('Más',8.5,1.38),('Menos',8.5,2.82),('Más',9.5,1.85),('Menos',9.5,1.85),('Más',10.5,2.72),('Menos',10.5,1.40)])
add('IRL-KOS tarjetas total','cards',4.46,5,5,[('Más',7.5,1.85),('Menos',7.5,1.88)],mult=1.1)
add('IRL-KOS goles total','goals',2.25,1,1,[('Más',1.5,1.15),('Menos',1.5,4.85),('Más',2.5,1.78),('Menos',2.5,1.95),('Más',3.5,3.35),('Menos',3.5,1.29)],xg=1.90)
# ===== BIH-ROU 1-1 (corners 2-2; cards 0; xG .86)
add('BIH-ROU corners total','corners',8.3,4,4,[('Más',7.5,1.42),('Menos',7.5,2.65),('Más',8.5,1.93),('Menos',8.5,1.78),('Más',9.5,2.87),('Menos',9.5,1.37)])
add('BIH-ROU tarjetas total','cards',4.87,0,0,[('Más',3.5,2.22),('Menos',3.5,1.62)])
add('BIH-ROU goles total','goals',3.35,2,2,[('Más',2.5,1.22),('Menos',2.5,3.90),('Más',3.5,2.00),('Menos',3.5,1.75),('Más',4.5,4.10),('Menos',4.5,1.20)],xg=0.86)
# ===== WAL-POR 2-2 (corners 2-0; cards 0; xG 1.80 (0.75+1.05) )
add('WAL-POR corners total','corners',9.75,2,2,[('Más',5.5,1.33),('Menos',5.5,3.05),('Más',6.5,1.72),('Menos',6.5,2.00),('Más',7.5,2.50),('Menos',7.5,1.47)])
add('WAL-POR corners Portugal','corners',4.9,0,0,[('Más',2.5,1.60),('Menos',2.5,2.15),('Más',3.5,2.42),('Menos',3.5,1.47),('Más',4.5,3.95),('Menos',4.5,1.20)])
add('WAL-POR corners Gales','corners',4.85,2,2,[('Más',2.5,1.15),('Más',3.5,1.70),('Menos',3.5,1.98),('Más',4.5,3.0),('Menos',4.5,1.32)])
add('WAL-POR tarjetas total','cards',3.4,0,0,[('Más',1.5,1.33),('Menos',1.5,3.15),('Más',2.5,1.85),('Menos',2.5,1.88),('Más',3.5,2.85),('Menos',3.5,1.39)])
add('WAL-POR goles total','goals',2.95,4,4,[('Más',4.5,1.10),('Más',5.5,1.53),('Menos',5.5,2.40),('Más',6.5,2.62),('Menos',6.5,1.45)],xg=1.8)
# ===== HUN-NIR 1-0 (corners 2-2; cards 0; fouls 2-3)
add('HUN-NIR corners total','corners',8.95,4,4,[('Más',7.5,1.42),('Menos',7.5,2.65),('Más',8.5,1.93),('Menos',8.5,1.78),('Más',9.5,2.87),('Menos',9.5,1.37)])
add('HUN-NIR tarjetas total','cards',4.55,0,0,[('Más',2.5,1.72),('Menos',2.5,2.05)])
add('HUN-NIR goles total','goals',1.8,1,1,[('Más',1.5,1.32),('Menos',1.5,3.15),('Más',2.5,2.50),('Menos',2.5,1.47),('Más',3.5,5.70),('Menos',3.5,1.11)],xg=0.88)
# ===== ISR-AUT 1-0 (corners 1-4; cards 0; shots 3-10; xG 1.71)
add('ISR-AUT corners total','corners',7.65,5,5,[('Más',8.5,1.26),('Menos',8.5,3.50),('Más',9.5,1.60),('Menos',9.5,2.20),('Más',10.5,2.20),('Menos',10.5,1.60)])
add('ISR-AUT corners Austria','corners',4.1,4,4,[('Más',7.5,1.83)])
add('ISR-AUT tarjetas total','cards',3.9,0,0,[('Más',2.5,2.37),('Menos',2.5,1.55)])
add('ISR-AUT goles total','goals',3.35,1,1,[('Más',1.5,1.12),('Más',2.5,1.65),('Menos',2.5,2.15),('Más',3.5,2.95),('Menos',3.5,1.36)],xg=1.71)
add('ISR-AUT goles Austria','goals',1.9,0,0,[('Más',0.5,1.27),('Menos',0.5,3.55),('Más',1.5,2.32),('Menos',1.5,1.57),('Más',2.5,5.30)],xg=1.24)
# ===== UKR-GEO 1-0 (corners 0-8; cards 0; xG .96)
add('UKR-GEO corners total','corners',8.65,8,8,[('Más',11.5,1.32),('Menos',11.5,3.15),('Más',12.5,1.72),('Menos',12.5,2.02),('Más',13.5,2.42),('Menos',13.5,1.50)])
add('UKR-GEO corners Ucrania','corners',4.2,0,0,[('Más',1.5,1.87)])
add('UKR-GEO corners Georgia','corners',4.45,8,8,[('Más',11.5,2.20)])
add('UKR-GEO tarjetas total','cards',3.95,0,0,[('Más',2.5,1.62),('Menos',2.5,2.22)])
add('UKR-GEO goles total','goals',2.5,1,1,[('Más',1.5,1.27),('Menos',1.5,3.45),('Más',2.5,2.32),('Menos',2.5,1.55),('Más',3.5,5.10)],xg=0.96)
# ===== POL-SWE 1-1 (corners 0-5; cards 0; xG 1.58)
add('POL-SWE corners total','corners',8.5,5,5,[('Más',8.5,1.29),('Menos',8.5,3.25),('Más',9.5,1.65),('Menos',9.5,2.12),('Más',10.5,2.32),('Menos',10.5,1.53)])
add('POL-SWE corners Polonia','corners',5.35,0,0,[('Más',2.5,2.00)])
add('POL-SWE tarjetas total','cards',4.4,0,0,[('Más',2.5,1.98),('Menos',2.5,1.78)])
add('POL-SWE goles total','goals',3.4,2,2,[('Más',2.5,1.15),('Menos',2.5,4.80),('Más',3.5,1.75),('Menos',3.5,1.98),('Más',4.5,3.30),('Menos',4.5,1.30)],xg=1.58)
if __name__=='__main__':
    for r in sorted(R,key=lambda r:-r[5]):
        if r[3]>=1.30: print(r)
