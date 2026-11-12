# -*- coding: utf-8 -*-
"""Entradas del supermodelo para la combi del 11-nov-2026. Cuotas = capturas de Betano del usuario (13:17–13:20 Bogotá).
Solo se cargan las líneas que se VEN en las capturas; los mercados plegados no se inventan."""
import json, os
aqui = os.path.dirname(os.path.abspath(__file__))
def L(m,a,l,mas,menos): return dict(mercado=m,ambito=a,linea=l,mas=mas,menos=menos)
def lad(m,a,txt):
    out=[]
    for it in txt.split():
        h,v=it.split(':'); mas,menos=v.split('/'); out.append(L(m,a,float(h),float(mas),float(menos)))
    return out

P={}
# ---------- Barnsley – Oldham (EFL Trophy, 14:00 Bogotá) ----------
l=[]
l+=lad('goles','local',"1.5:1.32/3.2 2.5:1.95/1.8 3.5:3.3/1.31")
l+=lad('goles','visitante',"0.5:1.23/3.85 1.5:2.05/1.72 2.5:4.05/1.22")
l+=lad('corners','1T',"5.5:1.98/1.75")
u=[dict(mercado='resultado',opciones={'1':1.60,'X':4.80,'2':4.05}),
   dict(mercado='resultado',opciones={'1X':1.24,'X2':2.32,'12':1.17}),
   dict(mercado='ambos',opciones={'si':1.32,'no':3.10}),
   dict(mercado='handicap',h=-1,opciones={'local':2.32,'empate':4.35,'visitante':2.32}),
   dict(mercado='handicap',h=-2,opciones={'local':3.85,'empate':4.90,'visitante':1.60}),
   dict(mercado='handicap',h=-3,opciones={'local':7.00,'empate':6.70,'visitante':1.25})]
P['barnsley_oldham']=dict(objetivos={'local':{'g':2.59},'visitante':{'g':1.54}},local='Barnsley',visitante='Oldham',liga='Inglaterra · EFL Trophy',fecha='2026-11-11 14:00',betano=dict(lineas=l,unicos=u,jugadores=[],parejas=[]),jugadores=[])
# ---------- Sheffield Wednesday – Accrington (EFL Trophy, 14:00) ----------
l=[]
l+=lad('goles','total',"2.5:1.42/2.67 3.5:2.02/1.72 4.5:3.15/1.31")
l+=lad('goles','local',"0.5:1.19/4.4 1.5:1.85/1.88 2.5:3.55/1.27")
l+=lad('goles','visitante',"0.5:1.17/4.65 1.5:1.78/1.98 2.5:3.3/1.31")
l+=lad('corners','total',"9.5:1.65/2.12 10.5:2.07/1.67 11.5:2.72/1.4")
l+=lad('corners','1T',"4.5:1.75/1.98")
u=[dict(mercado='resultado',opciones={'1':2.55,'X':3.85,'2':2.35}),
   dict(mercado='resultado',opciones={'1X':1.60,'X2':1.50,'12':1.24}),
   dict(mercado='ambos',opciones={'si':1.39,'no':2.77})]
l+=[dict(mercado='corners',ambito='local',linea=5.5,mas=1.82,menos=None),dict(mercado='corners',ambito='visitante',linea=4.5,mas=2.0,menos=None)]
P['sheffwed_accrington']=dict(objetivos={'local':{'c':5.5},'visitante':{'c':4.7}},local='Sheffield Wednesday',visitante='Accrington Stanley',liga='Inglaterra · EFL Trophy',fecha='2026-11-11 14:00',betano=dict(lineas=l,unicos=u,jugadores=[],parejas=[]),jugadores=[])
# ---------- Juventus W – Lyon W (Champions League F, 15:00) ----------
l=[]
l+=lad('goles','total',"2.5:1.25/3.7 3.5:1.62/2.2 4.5:2.35/1.55")
l+=lad('goles','local',"0.5:1.93/1.82 1.5:5.2/1.14 2.5:11.25/1.02")
l+=lad('goles','visitante',"2.5:1.44/2.67 3.5:2.07/1.7 4.5:3.3/1.31")
l+=lad('corners','total',"8.5:1.36/3.0 9.5:1.62/2.22 10.5:2.02/1.75 11.5:2.6/1.45")
l+=lad('corners','1T',"3.5:1.31/3.25 4.5:1.7/2.07 5.5:2.4/1.53")
l+=lad('tarjetas','total',"2.5:1.7/2.07")
l+=lad('tarjetas','1T',"0.5:1.53/2.42")
u=[dict(mercado='resultado',opciones={'1':17.0,'X':8.75,'2':1.12}),
   dict(mercado='resultado',opciones={'1X':7.0,'X2':1.02,'12':1.06}),
   dict(mercado='ambos',opciones={'si':1.95,'no':1.75}),
   dict(mercado='ambos_n_tarjetas',n=1,opciones={'si':1.67,'no':2.12}),
   dict(mercado='ambos_n_tarjetas',n=2,opciones={'si':4.25,'no':1.20}),
   dict(mercado='mas_que',stat='tarjetas',opciones={'local':1.55,'empate':3.85,'visitante':5.80}),
   dict(mercado='mas_que',stat='corners',opciones={'local':9.75,'empate':10.75,'visitante':1.05}),
   dict(mercado='handicap',h=1,opciones={'local':7.00,'empate':5.60,'visitante':1.34}),
   dict(mercado='handicap',h=2,opciones={'local':3.40,'empate':4.55,'visitante':1.80}),
   dict(mercado='handicap',h=3,opciones={'local':2.02,'empate':4.65,'visitante':2.77})]
l+=[dict(mercado='corners',ambito='local',linea=2.5,mas=1.98,menos=None),dict(mercado='corners',ambito='visitante',linea=7.5,mas=1.82,menos=None)]
P['juventus_lyon_f']=dict(objetivos={'local':{'c':2.7,'y':1.9},'visitante':{'c':7.7,'y':1.05}},local='Juventus W',visitante='Lyon W',liga='UEFA Champions League (F)',fecha='2026-11-11 15:00',betano=dict(lineas=l,unicos=u,jugadores=[],parejas=[]),jugadores=[])

FICHA={
 'barnsley_oldham':dict(derbi=False,importancia='normal',fuentes=['footballpredictions.ai (forma y tabla del grupo)','starting11.com (once probable sin nombres)'],
   dudas=['Alineaciones no publicadas aún; EFL Trophy suele traer rotación','Sin árbitro ni clima verificados']),
 'sheffwed_accrington':dict(derbi=False,importancia='normal',fuentes=['capturas Betano del usuario'],dudas=['Sin alineaciones, árbitro ni clima verificados; EFL Trophy suele traer rotación']),
 'juventus_lyon_f':dict(derbi=False,importancia='normal',fuentes=['futboltotal.futbol (fecha, sede, forma: Lyon 5 victorias, Juventus 3V-2D)','UEFA informe del 19-nov-2025 (mismo cruce: Lyon 13 córners)'],dudas=['Sin alineaciones, árbitro ni clima verificados']),
}
for k,v in P.items():
    v['ficha']=FICHA[k]; v['estadio']=''; v['cuotas_leidas']='Capturas de Betano del usuario 13:17–13:20 (Bogotá); solo mercados visibles'
    json.dump(v,open(os.path.join(aqui,k+'.json'),'w'),ensure_ascii=False,indent=1)
    print(k,len(v['betano']['lineas']),'líneas',len(v['betano']['unicos']),'únicos')
