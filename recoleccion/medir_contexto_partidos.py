#!/usr/bin/env python3
# Mide el contexto con intervalos agrupados por PARTIDO (bootstrap): las líneas de un mismo partido no son independientes. Uso: python3 recoleccion/medir_contexto_partidos.py
import sys,os,random,collections,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import medir_contexto as M
L,cob=M.cargar()
random.seed(1)
def por_partido(S):
    d=collections.defaultdict(list)
    for x in S: d[(x['jornada'],x['clave'])].append(x)
    return d
def boot(S,B=2000):
    d=por_partido(S); ks=list(d)
    if len(ks)<3: return None
    base=sum(x['hit']-x['pm'] for x in S)/len(S)
    r=[]
    for _ in range(B):
        t=[x for k in random.choices(ks,k=len(ks)) for x in d[k]]
        r.append(sum(x['hit']-x['pm'] for x in t)/len(t))
    r.sort()
    return len(ks),len(S),base*100,r[int(.025*B)]*100,r[int(.975*B)]*100
for nombre,f in (('TOTAL',lambda x:x['ambito']=='total'),('EQUIPO',lambda x:x['ambito']!='total')):
    S=[x for x in L if f(x)]
    print('==',nombre)
    for campo in('sit','dat'):
        for k,e in((1,'a favor'),(-1,'en contra')):
            for lado in ('Más','Menos',None):
                T=[x for x in S if x[campo]==k and (lado is None or x['lado']==lado)]
                b=boot(T)
                if b: print(campo,e,lado or 'ambos','partidos %d líneas %d dif %+.1f IC95 [%+.1f, %+.1f]'%b)
    # por mercado, sit a favor
    for m in M.MERC:
        T=[x for x in S if x['sit']==1 and x['mercado']==m]
        b=boot(T) if len(T)>20 else None
        if b: print('  sit a favor',m,'partidos %d líneas %d dif %+.1f IC95 [%+.1f, %+.1f]'%b)
