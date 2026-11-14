import sys, itertools, math, json
sys.path.insert(0,'recoleccion')
import informe_completo as I
J='jornadas/2026-11-13'
XI={
'paises-bajos-grecia':"Bart Verbruggen|Denzel Dumfries|Jan Paul van Hecke|Micky van de Ven|Jurriën Timber|Joey Veerman|Tijjani Reijnders|Frenkie de Jong|Crysencio Summerville|Donyell Malen|Cody Gakpo|Konstantinos Tzolakis|Lazaros Rota|Konstantinos Mavropanos|Panagiotis Retsos|Kostas Tsimikas|Konstantinos Karetsas|Dimitris Kourbelis|Athanasios Androutsos|Christos Tzolis|Vangelis Pavlidis|Fotis Ioannidis",
'escocia-macedonia-del-norte':"Angus Gunn|Ryan Porteous|Luke Graham|Kieran Tierney|Ben Gannon-Doak|Lewis Ferguson|Billy Gilmour|Andy Robertson|John McGinn|Scott McTominay|Che Adams|Stole Dimitrievski|Bojan Ilievski|Mario Mladenovski|Visar Musliu|Ezgjan Alioski|Enis Bardhi|Matej Gaštarov|Eljif Elmas|Darko Churlinov|Elmin Rastoder|Ljupche Doriev",
'eslovenia-suiza':"Jan Oblak|Žan Zaletel|Vanja Drkušić|Jaka Bijol|Srđan Kuzmić|Žan Karničnik|Adam Gnezda Čerin|Mark Zabukovnik|Danijel Šturm|Aljoša Matko|Žan Vipotnik|Gregor Kobel|Zachary Athekame|Nico Elvedi|Manuel Akanji|Sascha Britschgi|Michel Aebischer|Denis Zakaria|Remo Freuler|Fabian Rieder|Breel Embolo|Dan Ndoye"}
def sin(s): return I.norm(s)
pool={}
for c,xi in XI.items():
    d=I.cargar(J,c); xs={sin(x) for x in xi.split('|')}
    loc,vis=d['loc'],d['vis']
    tc=I.tarjetas_sofa(d)
    L=[]
    for r in d['reg']:
        if r['mercado'].startswith('jugador') or not r['p_modelo'] or not r['cuota']: continue
        cu=I.f2(r['cuota']); p=I.f2(r['p_modelo']); pm=I.f2(r['p_mercado']) or 1/cu
        if r['mercado']=='tarjetas' and r['ambito'] in('total','local','visitante'):
            lam={'total':tc['tot'],'local':tc['exp_h'],'visitante':tc['exp_a']}[r['ambito']]
            k=math.floor(I.f2(r['linea']))+1; ps=I.pois_ge(lam,k); ps=ps if r['lado']=='Más' else 1-ps
            p=(p+ps)/2
        amb={'total':'total','local':loc,'visitante':vis,'1T':'1T','2T':'2T'}.get(r['ambito'],r['ambito'])
        L.append(dict(m=c,n=f"{I.NOM_MERC.get(r['mercado'],r['mercado'])} {amb} {r['lado']} {r['linea']}",c=cu,p=min(p,pm+0.06),pm=pm,t='eq'))
    for l in d['modelo']['lineas']:
        if l['familia'] in('resultado','ambos') and not l['seleccion'].startswith('Descanso/final'):
            L.append(dict(m=c,n=l['seleccion'],c=l['cuota'],p=min(l['p'],l['p_mercado']+0.06),pm=l['p_mercado'],t='res'))
    for r in I.jugadores(d):
        if sin(r['sn']) in xs and r['st']!='tarjeta':
            pu=(r['pe']+r['mk'])/2
            L.append(dict(m=c,n=f"{r['sn']} {I.NOMBRE[r['st']]} {r['k']}+",c=r['c'],p=pu,pm=r['mk'],t='jug'))
        elif sin(r['sn']) in xs:
            L.append(dict(m=c,n=f"{r['sn']} Tarjeta 1+",c=r['c'],p=(r['pe']+r['mk'])/2,pm=r['mk'],t='jug'))
    # quitar duplicados por nombre
    seen={}
    for x in L: seen[(x['n'])]=x
    pool[c]=list(seen.values())
    print(c,len(pool[c]))
import pickle; pickle.dump(pool,open('/tmp/claude-0/-home-claude/c53d9b89-4877-57c7-835a-ec0c5b00a54b/scratchpad/pool.pkl','wb'))
def best(lo,hi,top=5,minc=1.25,maxc=8):
    P=[[x for x in pool[c] if minc<=x['c']<=maxc and x['p']>=0.15] for c in pool]
    P=[sorted(p,key=lambda x:-x['p'])[:70] for p in P]
    out=[]
    for a in P[0]:
        for b in P[1]:
            ab=a['c']*b['c']
            for c_ in P[2]:
                pr=ab*c_['c']
                if lo<=pr<=hi: out.append((a['p']*b['p']*c_['p'],pr,a,b,c_))
    out.sort(key=lambda t:-t[0]); return out[:top]
for lo,hi in((17,24),(8.5,11.5)):
    print('=== cuota',lo,hi)
    for p,pr,*ls in best(lo,hi,6):
        print(f"{pr:.1f}  p={p*100:.1f}%  fair={1/p:.1f} | "+' + '.join(f"{x['n']} @{x['c']} ({x['p']*100:.0f}%)" for x in ls))
