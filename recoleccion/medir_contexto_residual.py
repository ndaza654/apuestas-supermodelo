#!/usr/bin/env python3
# Real menos esperado por equipo según las banderas de la nota (necesita ganar, le sirve el empate, rota). Uso: python3 recoleccion/medir_contexto_residual.py
import sys,csv,re,json,os,glob,random,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import contexto_mercado as C
random.seed(2)
R='.'
rows=list(csv.DictReader(open('registro/lineas.csv',encoding='utf-8-sig'),delimiter=';'))
def f(x):
    try:return float(str(x).replace(',','.'))
    except:return None
vistos={}
for r in rows:
    if r['mercado'] not in ('corners','goles','remates','al_arco','fueras') or r['ambito'] not in('local','visitante'): continue
    m=re.search(r'valor real ([0-9]+(?:[.,][0-9]+)?)',r['nota'] or '')
    e=f(r['esperado'])
    if not m or e is None: continue
    k=(r['jornada'],r['partido'],r['mercado'],r['ambito'])
    vistos[k]=(f(m.group(1)),e)
print('equipo-mercado únicos con valor real y esperado:',len(vistos))
# notas
mapa={}
def nota(j,p):
    key=(j,p)
    if key in mapa: return mapa[key]
    base='jornadas/'+j
    N=None
    for fp in glob.glob(base+'/fichas/ficha_*.json'):
        pass
    mapa[key]=None
    return None
# mapa partido->clave por jornada
cl={}
for j in set(k[0] for k in vistos):
    for fp in glob.glob('jornadas/%s/fichas/ficha_*.json'%j):
        F=json.load(open(fp,encoding='utf8'))
        cl[(j,F.get('encuentro'))]=fp.split('ficha_')[1][:-5]
grupos=collections.defaultdict(list)
for (j,p,m,a),(real,esp) in vistos.items():
    c=cl.get((j,p))
    if not c: continue
    np_=os.path.join('jornadas',j,'notas',c+'.json')
    if not os.path.exists(np_): continue
    N=json.load(open(np_,encoding='utf8'))
    s=N.get(a) or {}
    rival=N.get('visitante' if a=='local' else 'local') or {}
    if not any(N.get(k2,{}).get(x) for k2 in('local','visitante') for x in('necesita_ganar','le_sirve_empate','rotacion')) and not N.get('decisivo'):
        g='sin banderas en el partido'
    else:
        flags=[]
        if s.get('necesita_ganar'): flags.append('necesita ganar')
        if s.get('le_sirve_empate'): flags.append('le sirve el empate')
        if s.get('rotacion'): flags.append('rota')
        if rival.get('necesita_ganar') and not flags: flags.append('(solo el rival necesita ganar)')
        g=' + '.join(flags) or 'partido con banderas, este equipo sin bandera'
    for gg in (g,'TODOS'):
        grupos[(m if False else 'todos',gg)].append((j,c,m,real,esp))
        grupos[(m,gg)].append((j,c,m,real,esp))
def est(S):
    d=collections.defaultdict(list)
    for j,c,m,r,e in S: d[(j,c)].append(r-e)
    ks=list(d); allv=[v for k in ks for v in d[k]]
    med=sum(allv)/len(allv)
    rs=[]
    for _ in range(1500):
        t=[v for k in random.choices(ks,k=len(ks)) for v in d[k]]
        rs.append(sum(t)/len(t))
    rs.sort()
    esp=sum(e for *_,e in S)/len(S)
    return len(ks),len(S),med,rs[37],rs[1462],esp
print('mercado | grupo | partidos | n | real−esperado | IC95 | esperado medio')
for (m,g),S in sorted(grupos.items()):
    if m!='todos' or g=='TODOS' and False: pass
    if len(S)<15: continue
    if m=='todos':
        a=est(S); print('%-8s %-50s %3d %4d %+.2f [%+.2f,%+.2f] esp %.2f'%((m,g)+a))
