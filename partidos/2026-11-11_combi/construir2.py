# -*- coding: utf-8 -*-
"""Londrina–Náutico, Independiente Petrolero–Always Ready, Quindío–Tigres. Cuotas leídas del JSON de Betano (15:3x Bogotá)."""
import json, os
aqui=os.path.dirname(os.path.abspath(__file__))
def parse(s):
    out=[]
    for it in s.split(';'):
        m,a,h,mas,menos=[x.strip() for x in it.split(',')]
        out.append(dict(mercado=m,ambito=a,linea=float(h),mas=float(mas) if mas else None,menos=float(menos) if menos else None))
    return out
def ops(s): return {k.strip():float(v) for k,v in (x.split('=') for x in s.split('|'))}
def htft(names, vals):
    return dict(zip(names, vals))
K=['1/1','1/X','1/2','X/1','X/X','X/2','2/1','2/X','2/2']
P={}
# ---------------- Londrina – Náutico ----------------
lad=("goles,total,0.5,1.05,7.3;goles,total,1.5,1.26,3.4;goles,total,2.5,1.78,1.91;goles,total,3.5,2.82,1.36;goles,total,4.5,4.75,1.14;goles,total,2.75,1.98,1.75;"
     "goles,1T,0.5,1.35,2.65;goles,1T,1.5,2.45,1.4;goles,1T,2.5,4.75,1.1;goles,1T,1,1.75,1.93;goles,1T,1.25,2.15,1.6;goles,2T,1.5,1.93,1.75;"
     "goles,local,1.5,1.75,1.98;goles,visitante,0.5,1.5,2.4;corners,total,10.5,1.7,2.07;corners,1T,5.5,2.05,1.72;corners,local,5.5,1.72,;corners,visitante,5.5,2.2,")
un=[dict(mercado='resultado',opciones={'1':1.72,'X':3.8,'2':4.5}),dict(mercado='resultado',opciones={'1X':1.19,'X2':2.1,'12':1.24}),
    dict(mercado='ambos',opciones={'si':1.75,'no':1.93}),dict(mercado='resultado_1t',opciones={'1':2.25,'X':2.2,'2':4.6}),
    dict(mercado='resultado_2t',opciones={'1':2.02,'X':2.6,'2':4.2}),
    dict(mercado='htft',opciones=htft(K,[2.57,14.5,45,4.35,5.5,9.25,23,15,7.2])),
    dict(mercado='handicap',h=-1,opciones={'local':2.82,'empate':3.55,'visitante':2.1}),
    dict(mercado='mas_que',stat='corners',opciones={'local':1.7,'empate':6.6,'visitante':2.42})]
PL="Igor Bahia;L;1.87;.9|Pablo Dyego;L;2.2;.3|William Pottker;L;2.27;.3|Cachoeira;L;2.57;.3|João Vitor Coni de Andrade;L;2.95;.8|Herbert Mateus Almeida de Oliveira;L;3.1;.85|Vitinho;L;3.3;.3|Geovane Meurer;L;3.9;.85|Guilherme Portuga;L;4.2;.3|Derek;V;4.5;0|Luiz Claudio;V;4.65;.75|Luiz Felipe;V;5.0;.4|Benjamin Borasi;V;5.8;.2|Luiz Paulo;V;15.5;.75"
jug=[];info=[]
for r in PL.split('|'):
    n,l,c,t=r.split(';'); lado='local' if l=='L' else 'visitante'
    if n=='Luiz Paulo': continue   # solo tiene línea de 2+ goles
    jug.append(dict(jugador=n,lado=lado,stat='anota',cuota=float(c)))
    d=dict(nombre=n,lado=lado,titular=float(t),minutos=80)
    if n=='Derek': d.update(fuera=True,minutos=0)
    info.append(d)
P['londrina_nautico']=dict(local='Londrina-PR',visitante='Náutico PE',liga='Brasil · Série B (38.ª y última fecha)',fecha='2026-11-11 17:00',
  betano=dict(lineas=parse(lad),unicos=un,jugadores=jug,parejas=[]),jugadores=info,
  ficha=dict(derbi=False,importancia='baja',arbitro={'nombre':'Andreza Helena de Siqueira (MG)'},clima={'lluvia':'no','viento_fuerte':False},
    info_tardia=[dict(tipo='rotacion',hecho='Náutico (15.º, 46 pts, ya salvado): 9 titulares con vacaciones adelantadas, 4 suspendidos (Reginaldo, Ryan, Samuel, Kauã Maranhão), Derek dejó el club; saldrán ~14 juveniles/reservas',horas=20),
                 dict(tipo='motivacion',hecho='Londrina (18.º, 32 pts) ya descendido a Serie C, 3 derrotas seguidas, plantel liberado y con juveniles, juega a puertas cerradas; solo un empate le asegura no caer al 19.º',horas=20)],
    local=dict(rotacion=True,motivacion='baja'),visitante=dict(rotacion=True,motivacion='baja'),
    frescos=['rotacion','motivacion'],
    fuentes=['Diario de Pernambuco (38.ª fecha, escalaciones y desfalques)','MixVale (probables)','TV Sim Brasil (puertas cerradas, tabla)'],
    dudas=['Alineaciones probables de Náutico difieren entre fuentes (Derek ya no está; Kauã Maranhão suspendido en un caso aparece titular)','Nada confirmado a la hora de leer']),
  estadio='Vitorino Gonçalves Dias (Londrina) · puertas cerradas · 19:00 Brasilia',cuotas_leidas='Cuotas de Betano leídas ~15:30 (Bogotá) del JSON del partido')
# ---------------- Independiente Petrolero – Always Ready ----------------
lad=("goles,total,1.5,1.16,4.45;goles,total,2.5,1.5,2.37;goles,total,3.5,2.15,1.6;goles,total,4.5,3.45,1.25;goles,total,5.5,5.6,1.1;goles,total,3,1.75,1.95;goles,total,3.25,1.98,1.75;"
     "goles,1T,0.5,1.26,3.05;goles,1T,1.5,2.2,1.57;goles,1T,2.5,4,1.15;goles,1T,1.25,1.85,1.82;goles,2T,1.5,1.67,2.05;goles,local,1.5,2.55,1.45;goles,visitante,1.5,1.55,2.3;"
     "corners,total,9.5,1.93,1.82;corners,1T,4.5,1.93,1.8")
un=[dict(mercado='resultado',opciones={'1':4.05,'X':3.95,'2':1.7}),dict(mercado='resultado',opciones={'1X':2.1,'X2':1.21,'12':1.22}),
    dict(mercado='ambos',opciones={'si':1.5,'no':2.35}),dict(mercado='resultado_1t',opciones={'1':4.1,'X':2.37,'2':2.2}),
    dict(mercado='resultado_2t',opciones={'1':3.85,'X':2.85,'2':1.95}),
    dict(mercado='htft',opciones=htft(K,[6.7,13.5,18,9,6.4,4.6,35,14,2.57])),
    dict(mercado='handicap',h=1,opciones={'local':2.1,'empate':3.75,'visitante':2.72})]
P['petrolero_always']=dict(local='Independiente Petrolero',visitante='Always Ready',liga='Bolivia · Copa Bolivia (semifinal, ida)',fecha='2026-11-11 17:00',
  betano=dict(lineas=parse(lad),unicos=un,jugadores=[],parejas=[]),jugadores=[],
  ficha=dict(derbi=False,importancia='alta',clima={'lluvia':'no','viento_fuerte':False},
    info_tardia=[dict(tipo='bajas',hecho='Independiente sin Richet Gómez ni Jesús Maraude (lesionados); Always Ready: un artículo dice que no tiene bajas, otro nombra a Maraude (posible confusión de club)',horas=6)],
    local=dict(estilo=['balon_parado']),
    fuentes=['Vision360 (11-nov)','El Diario (11-nov)','Diez.bo','Scores24 (forma y H2H)'],
    dudas=['Sin alineaciones ni árbitro; las dos fuentes difieren en la lista de bajas','Sede Sucre (~2.800 m): no está en el modelo; ya está en el precio']),
  estadio='Olímpico Patria (Sucre) · 18:00 hora de Bolivia',cuotas_leidas='Cuotas de Betano leídas ~15:30 (Bogotá) del JSON del partido')
# ---------------- Quindío – Tigres ----------------
lad=("goles,total,0.5,1.12,5.1;goles,total,1.5,1.53,2.27;goles,total,2.5,2.55,1.44;goles,total,3.5,4.6,1.15;goles,total,4.5,7.6,1.04;goles,total,1.75,1.7,2.02;goles,total,2,1.98,1.75;"
     "goles,1T,0.5,1.55,2.27;goles,1T,1.5,3.1,1.25;goles,1T,2.5,5.9,1.05;goles,1T,0.75,1.78,1.91;goles,2T,0.5,1.4,2.65;goles,local,1.5,2.35,1.53;goles,visitante,0.5,1.75,1.95;"
     "corners,total,8.5,1.75,2;corners,1T,4.5,2.12,1.67")
un=[dict(mercado='resultado',opciones={'1':1.88,'X':3.05,'2':4.3}),dict(mercado='resultado',opciones={'1X':1.19,'X2':1.87,'12':1.32}),
    dict(mercado='ambos',opciones={'si':2.25,'no':1.55}),dict(mercado='resultado_1t',opciones={'1':2.52,'X':1.93,'2':4.9}),
    dict(mercado='resultado_2t',opciones={'1':2.35,'X':2.12,'2':4.5}),
    dict(mercado='htft',opciones=htft(K,[2.9,15,60,4.4,3.95,8.75,35,16.5,7.1])),
    dict(mercado='handicap',h=-1,opciones={'local':3.7,'empate':3.3,'visitante':1.87})]
P['quindio_tigres']=dict(local='Deportes Quindío',visitante='Tigres FC',liga='Colombia · Primera B (cuadrangular Clausura 2026, fecha 4)',fecha='2026-11-11 20:10',
  betano=dict(lineas=parse(lad),unicos=un,jugadores=[],parejas=[]),jugadores=[],
  ficha=dict(derbi=False,importancia='alta',arbitro={'nombre':'José Bautista'},clima={'lluvia':'no','viento_fuerte':False},
    local=dict(motivacion='alta'),
    fuentes=['Win Sports (ficha del partido: Estadio Centenario, árbitro José Bautista)','gioscore (forma: Quindío 6V-1E-3D últimos 10, Tigres 2V-7E-1D; Quindío 3 victorias en los últimos 5 H2H)'],
    dudas=['Sin alineaciones ni bajas; el partido de ida (Tigres 2–0 Quindío) parece ser del 7-nov pero la fuente no es limpia','Tabla actual del cuadrangular no verificada (la tabla que vi era del cuadrangular de mayo)']),
  estadio='Centenario (Armenia) · 20:10',cuotas_leidas='Cuotas de Betano leídas ~15:30 (Bogotá) del JSON del partido')
for k,v in P.items():
    json.dump(v,open(os.path.join(aqui,k+'.json'),'w'),ensure_ascii=False,indent=1)
    print(k,len(v['betano']['lineas']),len(v['betano']['unicos']),len(v['betano']['jugadores']))
