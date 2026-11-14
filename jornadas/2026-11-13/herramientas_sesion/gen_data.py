import sys, json, re, math, difflib
sys.path.insert(0,'recoleccion')
import informe_completo as I
J='jornadas/2026-11-13'
SP='/tmp/claude-0/-home-claude/c53d9b89-4877-57c7-835a-ec0c5b00a54b/scratchpad/'
CL=['paises-bajos-grecia','escocia-macedonia-del-norte','eslovenia-suiza']
XI={
'paises-bajos-grecia':("Bart Verbruggen|Denzel Dumfries|Jan Paul van Hecke|Micky van de Ven|Jurriën Timber|Joey Veerman|Tijjani Reijnders|Frenkie de Jong|Crysencio Summerville|Donyell Malen|Cody Gakpo","Konstantinos Tzolakis|Lazaros Rota|Konstantinos Mavropanos|Panagiotis Retsos|Kostas Tsimikas|Konstantinos Karetsas|Dimitris Kourbelis|Athanasios Androutsos|Christos Tzolis|Vangelis Pavlidis|Fotis Ioannidis","4-3-3","4-4-2"),
'escocia-macedonia-del-norte':("Angus Gunn|Ryan Porteous|Luke Graham|Kieran Tierney|Ben Gannon-Doak|Lewis Ferguson|Billy Gilmour|Andy Robertson|John McGinn|Scott McTominay|Che Adams","Stole Dimitrievski|Bojan Ilievski|Mario Mladenovski|Visar Musliu|Ezgjan Alioski|Enis Bardhi|Matej Gaštarov|Eljif Elmas|Darko Churlinov|Elmin Rastoder|Ljupche Doriev","3-4-1-2","4-3-3"),
'eslovenia-suiza':("Jan Oblak|Žan Zaletel|Vanja Drkušić|Jaka Bijol|Srđan Kuzmić|Žan Karničnik|Adam Gnezda Čerin|Mark Zabukovnik|Danijel Šturm|Aljoša Matko|Žan Vipotnik","Gregor Kobel|Zachary Athekame|Nico Elvedi|Manuel Akanji|Sascha Britschgi|Michel Aebischer|Denis Zakaria|Remo Freuler|Fabian Rieder|Breel Embolo|Dan Ndoye","4-4-2","4-3-3")}
def md2html(t):
    out=[];ul=False
    for ln in t.strip().split('\n'):
        ln=ln.rstrip()
        if not ln: 
            if ul: out.append('</ul>');ul=False
            continue
        ln=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',ln)
        m=re.match(r'^(\d+)\.\s+(.*)',ln)
        if m:
            if not ul: out.append('<ul>');ul=True
            out.append('<li>'+m.group(2)+'</li>')
        else:
            if ul: out.append('</ul>');ul=False
            out.append('<p>'+ln+'</p>')
    if ul: out.append('</ul>')
    return ''.join(out)
def sim(a,b): return difflib.SequenceMatcher(None,a,b).ratio()
STATL={'anota':'anota','anota_o_asiste':'anota o asiste','tarjeta':'recibe tarjeta','asiste':'da una asistencia'}
DATA={'matches':[]}
for mi,c in enumerate(CL):
    d=I.cargar(J,c); loc,vis=d['loc'],d['vis']; M=d['modelo']; S=d['sofa']
    tc=I.tarjetas_sofa(d)
    xs_h,xs_a,f_h,f_a=XI[c]; xi_h=xs_h.split('|'); xi_a=xs_a.split('|')
    xiset={I.norm(x) for x in xi_h+xi_a}
    def es_tit(name):
        n=I.norm(name)
        if n in xiset: return True
        ap=n.split()[-1]
        return any(I.norm(x).split()[-1]==ap and I.norm(x).split()[0][:1]==n.split()[0][:1] for x in xi_h+xi_a)
    ob=M['objetivos']; ol,ov=ob['local'],ob['visitante']
    # filas de equipo
    R=[]
    tj={}
    for r in d['reg']:
        if r['mercado'].startswith('jugador') or not r['p_modelo']: continue
        ps=None
        if r['mercado']=='tarjetas' and r['ambito'] in('total','local','visitante'):
            lam={'total':tc['tot'],'local':tc['exp_h'],'visitante':tc['exp_a']}[r['ambito']]
            k=math.floor(I.f2(r['linea']))+1; x=I.pois_ge(lam,k); ps=round(x if r['lado']=='Más' else 1-x,3)
        R.append([r['mercado'],r['ambito'],r['lado'],I.f2(r['linea']),I.f2(r['cuota']),I.f2(r['p_modelo']),I.f2(r['p_mercado']),I.f2(r['esperado']),I.f2(r['colchon']),r['reg_local'],r['reg_visitante'],r['directos'],r['cumple_ficha'],ps])
    # resultados
    RES=[]
    for l in M['lineas']:
        if l['familia'] in('resultado','ambos','especial'):
            RES.append([l['familia'],l['seleccion'],l['cuota'],round(l['p'],3),round(l['p_mercado'],3)])
    # jugadores
    jug=I.jugadores(d); P=[]; seen=set()
    for r in jug:
        P.append([r['sn'],r['lado'],r['st'],r['k'],r['c'],round(r['pe'],3),round(r['mk'],3),r['fr'],r['n'],1 if es_tit(r['sn']) else 0,1 if (r['n']>=5 and r['fr']>=5) else 0,r['nota'] or '',round(r['pois'],3)])
        seen.add((r['j'],r['st'],r['k']))
    mp=I.emparejar(d)
    for x in d['bet']['betano']['jugadores']:
        ks=[(1,x['cuota'])] if 'cuota' in x else [(int(a),cc) for a,cc in x['escalera'].items()]
        for k,cc in ks:
            if (x['jugador'],x['stat'],k) in seen: continue
            if x['stat'] not in I.NOMBRE: continue
            P.append([x['jugador'],'L' if x['lado']=='local' else 'V',x['stat'],k,cc,None,round(1/cc,3),None,None,1 if es_tit(x['jugador']) else 0,0,'sin historial recogido (solo mercado)',None])
    # parejas
    pm_model={}
    for l in M['lineas']:
        if l['familia']=='pareja': pm_model[l['seleccion']]=l['p']
    pe1={(r['j'],r['st']):r['pe'] for r in jug if r['k']==1}
    Q=[]
    for q in d['bet']['betano'].get('parejas') or []:
        a,b=q['jugadores']; key=f"{a} o {b} ({STATL.get(q['stat'],q['stat'])})"
        pmod=pm_model.get(key)
        mine=None
        if (a,q['stat']) in pe1 and (b,q['stat']) in pe1: mine=round(1-(1-pe1[(a,q['stat'])])*(1-pe1[(b,q['stat'])]),3)
        Q.append([a,b,q['stat'],q['cuota'],round(pmod,3) if pmod else None,mine,1 if (es_tit(a) and es_tit(b)) else 0])
    # series para gráficos
    T=S['T']
    def ser(rows,i): return [r[i] for r in rows]
    ser_d={'h':{'rival':ser(T['h'],1),'gf':ser(T['h'],3),'gc':ser(T['h'],4),'yf':ser(T['h'],5),'yc':ser(T['h'],6),'cf':ser(T['h'],11),'cc':ser(T['h'],12)},
           'a':{'rival':ser(T['a'],1),'gf':ser(T['a'],3),'gc':ser(T['a'],4),'yf':ser(T['a'],5),'yc':ser(T['a'],6),'cf':ser(T['a'],11),'cc':ser(T['a'],12)}}
    notas=md2html(d['enfoque'])
    DATA['matches'].append(dict(id=mi,clave=c,loc=loc,vis=vis,liga=d['ficha'].get('liga'),estadio=S['ev']['venue'],arbitro=S['ev']['ref'],
        pres=[M['p_resultado']['local'],M['p_resultado']['empate'],M['p_resultado']['visitante']],
        obj=dict(gl=ol['g'],gv=ov['g'],cl=ol['c'],cv=ov['c'],yl=tc['exp_h'],yv=tc['exp_a'],ytot=tc['tot'],shl=ol['sh'],shv=ov['sh'],sotl=ol['sot'],sotv=ov['sot'],fl=ol['f'],fv=ov['f']),
        xi=dict(h=xi_h,a=xi_a,fh=f_h,fa=f_a,mh=S['L']['h']['miss'],ma=S['L']['a']['miss']),
        ref=dict(serie=tc['ref_serie'],media=tc['ref_mean']),series=ser_d,enfoque=notas,
        R=R,RES=RES,P=P,Q=Q))
    print(c,len(R),len(RES),len(P),len(Q))
json.dump(DATA,open(SP+'data.json','w'),ensure_ascii=False,separators=(',',':'))
import os; print(os.path.getsize(SP+'data.json')//1024,'KB')
