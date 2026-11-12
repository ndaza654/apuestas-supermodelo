# -*- coding: utf-8 -*-
"""Arma entrada.json (formato del supermodelo) con las cuotas de Betano leídas el 11-nov-2026 ~12:00 (hora Bogotá).
Turquía (local) – Bélgica (visitante), Liga de Naciones A, jueves 12-nov 12:00 Bogotá (20:00 İzmir).
Fuente de las cuotas: API de la página del partido en betano.co (todas las pestañas, 599 mercados)."""
import json, re, os

def L(m, a, linea, mas, menos): return dict(mercado=m, ambito=a, linea=linea, mas=mas, menos=menos)
def lad(m, a, txt):
    out = []
    for it in txt.split():
        h, v = it.split(':'); mas, menos = v.split('/')
        out.append(L(m, a, float(h), float(mas), float(menos)))
    return out

lineas = []
lineas += lad('goles', 'total', "1.5:1.17/5.2 2.5:1.52/2.57 3.5:2.25/1.65 4.5:3.75/1.28 5.5:6.5/1.11")
lineas += lad('goles', 'local', "0.5:1.32/3.2 1.5:2.42/1.52 2.5:5.2/1.14")
lineas += lad('goles', 'visitante', "0.5:1.13/5.5 1.5:1.6/2.25 2.5:2.77/1.42 3.5:5.3/1.14")
lineas += lad('goles', '1T', "0.5:1.28/3.6 1.5:2.2/1.65 2.5:4.6/1.19")
lineas += lad('goles', '2T', "0.5:1.16/5.1 1.5:1.7/2.1 2.5:3.1/1.36")
lineas += lad('corners', 'total', "7.5:1.35/3.05 8.5:1.62/2.2 9.5:2.07/1.7 10.5:2.75/1.42 11.5:3.75/1.24 12.5:5.2/1.14")
lineas += lad('corners', 'local', "2.5:1.21/4.15 3.5:1.52/2.45 4.5:2.07/1.7 5.5:3.15/1.33 6.5:4.85/1.16")
lineas += lad('corners', 'visitante', "3.5:1.34/3.1 4.5:1.75/2.02 5.5:2.45/1.52 6.5:3.7/1.25 7.5:5.5/1.12")
lineas += lad('corners', '1T', "3.5:1.47/2.57 4.5:2.05/1.72 5.5:3.1/1.34 6.5:4.9/1.15")
lineas += lad('corners', '2T', "3.5:1.34/3.1 4.5:1.75/2 5.5:2.5/1.5 6.5:3.9/1.23")
lineas += lad('tarjetas', 'total', "2.5:1.25/3.7 3.5:1.55/2.35 4.5:2.07/1.7 5.5:2.95/1.36 6.5:4.35/1.19")
lineas += lad('tarjetas', 'local', "1.5:1.45/2.62 2.5:2.32/1.57 3.5:4.2/1.2")
lineas += lad('tarjetas', 'visitante', "1.5:1.5/2.45 2.5:2.47/1.5 3.5:4.55/1.17")
lineas += lad('tarjetas', '1T', "0.5:1.3/3.35 1.5:2.05/1.72")
lineas += lad('remates', 'total', "28.5:1.6/2.27 29.5:1.8/1.95 30.5:2.05/1.72")
lineas += lad('remates', 'local', "12.5:1.52/2.42 13.5:1.8/1.93 14.5:2.22/1.62")
lineas += lad('remates', 'visitante', "15.5:1.72/2.05 16.5:2.05/1.72 17.5:2.55/1.47")
lineas += lad('al_arco', 'total', "9.5:1.62/2.22 10.5:2/1.75 11.5:2.57/1.47")
lineas += lad('al_arco', 'local', "3.5:1.39/2.87 4.5:1.83/1.9 5.5:2.67/1.44")
lineas += lad('al_arco', 'visitante', "4.5:1.44/2.67 5.5:1.88/1.85 6.5:2.65/1.45")
lineas += lad('al_arco', '1T', "4.5:1.8/1.95")
lineas += lad('faltas', 'total', "22.5:1.95/1.78")
lineas += lad('faltas', 'local', "10.5:1.95/1.78")
lineas += lad('faltas', 'visitante', "11.5:1.78/1.98")
lineas += lad('fueras', 'total', "3.5:1.93/1.82")
lineas += lad('fueras', 'local', "1.5:1.87/1.87")
lineas += lad('fueras', 'visitante', "1.5:1.65/2.15")
lineas += lad('fueras', '1T', "1.5:1.7/2.07")
lineas += lad('saques_meta', 'total', "14.5:1.82/1.91")
lineas += lad('saques_meta', 'local', "7.5:1.75/2")
lineas += lad('saques_meta', 'visitante', "6.5:1.75/2")
lineas += lad('saques_meta', '1T', "6.5:1.78/1.95")
lineas += lad('saques_banda', 'total', "34.5:1.91/1.83")
lineas += lad('saques_banda', 'local', "16.5:1.91/1.83")
lineas += lad('saques_banda', 'visitante', "17.5:1.78/1.95")
lineas += lad('saques_banda', '1T', "17.5:1.72/2.05")
# asiáticas enteras / de cuarto de la casa
lineas += lad('corners', 'total', "9:1.85/1.98")
lineas += lad('tarjetas', 'total', "4:1.78/2")
lineas += lad('goles', 'total', "3:1.8/2.07 2.75:1.62/2.35 3.25:2.02/1.83")

unicos = [
    dict(mercado='resultado', opciones={'1': 3.85, 'X': 4.1, '2': 1.82}),
    dict(mercado='ambos', opciones={'si': 1.5, 'no': 2.47}),
    dict(mercado='mas_que', stat='corners', opciones={'local': 2.37, 'empate': 6.2, 'visitante': 1.83}),
    dict(mercado='mas_que', stat='tarjetas', opciones={'local': 2.27, 'empate': 3.85, 'visitante': 2.5}),
    dict(mercado='ambos_n_tarjetas', n=1, opciones={'si': 1.21, 'no': 4.1}),
    dict(mercado='ambos_n_tarjetas', n=2, opciones={'si': 2.02, 'no': 1.75}),
    dict(mercado='resultado_1t', opciones={'1': 4.0, 'X': 2.45, '2': 2.3}),
    dict(mercado='resultado_2t', opciones={'1': 3.65, 'X': 2.87, '2': 2.1}),
    dict(mercado='htft_o', opciones={'1': 2.6, 'X': 1.87, '2': 1.53}),
    dict(mercado='htft', opciones={'1/1': 6.2, '1/X': 14.5, '1/2': 20, 'X/1': 9, 'X/X': 6.7, 'X/2': 5, '2/1': 35, '2/X': 14, '2/2': 2.75}),
    dict(mercado='handicap', h=0.25, opciones={'local': 2.37, 'visitante': 1.62}),
    dict(mercado='handicap', h=0.75, opciones={'local': 1.83, 'visitante': 2.02}),
]

# ---- jugadores: nombre;lado;anota;anota_o_asiste;asiste1+;remates;al_arco;entradas;faltas_cometidas;tarjeta;titular
J = """
Hugo Cuypers;V;2.25;1.91;5.4 21;4:1.27,5:1.62,6:2.27,7:3.4,8:5.4,9:8.75,10:13,11:18,12:22;1:1.35,2:2.52,3:5.9,4:13,5:21;1:1.7,2:4.2,3:11,4:19.5;1:1.37,2:2.67,3:6.5,4:14,5:21;6.5;0.40
Charles De Ketelaere;V;2.52;1.87;3.6 15 24;3:1.28,4:1.72,5:2.55,6:4.25,7:7.2,8:12,9:17.5,10:21;1:1.27,2:2.2,3:4.75,4:10.5,5:18.5;1:1.16,2:1.78,3:3.35,4:6.9,5:13;1:1.5,2:3.25,3:8.25,4:17,5:23;6.5;0.80
Kevin De Bruyne;V;2.75;2.1;4.55 18.5;3:1.5,4:2.25,5:3.8,6:5.9,7:11.5,8:17.5,9:22;1:1.5,2:3.1,3:8,4:16.5,5:23;1:1.25,2:2.12,3:4.5,4:9.75,5:17;1:1.45,2:3.05,3:7.5,4:15.5,5:22;5;0.92
Leandro Trossard;V;2.75;2.18;5.1 20;2:1.31,3:1.95,4:3.4,5:6.4,6:11.75,7:18,8:22;1:1.7,2:4.3,3:11.25,4:20;1:1.29,2:2.3,3:5.1,4:11,5:18.5;1:1.45,2:3.05,3:7.5,4:16,5:22;6.2;0.60
Mika Godts;V;3.05;2.35;5.1 20;3:1.42,4:2,5:3.1,6:5.6,7:9.75,8:15,9:20;1:1.36,2:2.57,3:6.1,4:13.5,5:21;1:1.26,2:2.15,3:4.55,4:9.75,5:17.5;1:1.38,2:2.7,3:6.6,4:14.5,5:21;5;0.55
Dodi Lukébakio;V;3.25;2.32;4.55 18.5;2:1.21,3:1.7,4:2.65,5:4.8,6:8.75,7:14.5,8:20,9:23;1:1.23,2:2.1,3:4.45,4:9.75,5:17.5;1:1.25,2:2.15,3:4.55,4:9.75,5:17.5;1:1.4,2:2.77,3:6.8,4:14.5,5:22;3.75;0.45
Hans Vanaken;V;3.25;2.07;3.5 14 23;1:1.09,2:1.52,3:2.52,4:4.85,5:9.5,6:16.5,7:22;1:1.75,2:4.55,3:12,4:21;1:1.25,2:2.12,3:4.5,4:9.75,5:17;1:1.5,2:3.25,3:8.25,4:17,5:23;4.65;0.50
Jérémy Doku;V;3.4;2.5;5.1 20;3:1.5,4:2.25,5:3.6,6:6.7,7:11.5,8:17.5,9:22;1:1.5,2:3.1,3:8,4:16.5,5:23;1:1.29,2:2.3,3:5.1,4:11,5:18.5;1:1.45,2:3.05,3:7.5,4:16,5:22;5.8;0.65
Diego Moreira;V;3.4;2.5;5.1 20;2:1.45,3:2.35,4:4.45,5:8.75,6:15,7:21;1:1.7,2:4.3,3:11.25,4:20;1:1.29,2:2.3,3:5.1,4:11,5:18.5;1:1.3,2:2.37,3:5.4,4:12,5:19.5,6:24;3;0.10
Youri Tielemans;V;3.7;2.5;4.55 18.5;1:1.09,2:1.52,3:2.52,4:4.85,5:9.5,6:16.5,7:22;1:1.75,2:4.55,3:12,4:21;1:1.09,2:1.52,3:2.5,4:4.75,5:9.25;1:1.23,2:2.1,3:4.5,4:9.75,5:17.5,6:23;4.65;0.92
Maxim De Cuyper;V;4.7;3.35;6.2 22;1:1.23,2:2.07,3:4.4,4:9.75,5:17.5,6:23;1:1.78,2:4.8,3:12.5,4:21;1:1.18,2:1.85,3:3.55,4:7.4,5:14;1:1.44,2:2.9,3:7.3,4:15.5,5:22;3.9;0.70
Nicolas Raskin;V;5.5;3.2;5 19.5;1:1.45,2:3.1,3:7.7,4:16,5:22;1:2.42,2:8.75,3:19.5,4:24;2:1.35,3:2.02,4:3.6,5:6.7,6:12;2:1.37,3:2.12,4:3.85,5:7.4,6:13,7:19.5,8:23;3.2;0.50
Brandon Mechele;V;6.6;5.5;9.75;1:1.82,2:4.9,3:13,4:22;1:4.55,2:18.5,3:24;1:1.16,2:1.78,3:3.3,4:6.8,5:13;1:1.47,2:3.2,3:8,4:16.5,5:23;5;0.75
Kyriani Sabbe;V;7.9;4.8;6.8 23;1:1.67,2:4.2,3:11,4:20;1:3.75,2:15.5,3:24;1:1.16,2:1.78,3:3.35,4:6.9,5:13;1:1.5,2:3.3,3:8.25,4:17,5:23;6.2;0.08
Joaquin Seys;V;7.6;4.35;6.2 22;1:1.72,2:4.45,3:11.75,4:21;1:4,2:16.5,3:24;2:1.3,3:1.91,4:3.25,5:5.9,6:10.75;1:1.5,2:3.25,3:8.25,4:17,5:23;5;0.20
Arthur Theate;V;7.9;6.4;9.75;1:1.87,2:5.2,3:14,4:22;1:4.55,2:18.5,3:24;1:1.3,2:2.3,3:5.1,4:11,5:18.5;1:1.57,2:3.65,3:9.5,4:18.5,5:24;3.5;0.30
Romeo Lavia;V;9.25;4.35;5.5 21;1:1.5,2:3.25,3:8.25,4:17,5:23;1:3.3,2:13.5,3:23;2:1.29,3:1.87,4:3.15,5:5.7,6:10.25;1:1.15,2:1.78,3:3.35,4:7.1,5:13.5,6:20;3.15;0.15
Josue Kongolo;V;9.25;7.2;9.75;1:1.98,2:5.9,3:15,4:23;1:4.55,2:18.5,3:24;1:1.3,2:2.3,3:5.1,4:11,5:18.5;1:1.57,2:3.65,3:9.5,4:18.5,5:24;2.7;0.08
Mandela Keita;V;10;5.6;7 23;1:1.44,2:2.95,3:7.2,4:15.5,5:22;1:3.2,2:13,3:23;2:1.37,3:2.07,4:3.75,5:7.1,6:12.5;1:1.18,2:1.9,3:3.75,4:8,5:15,6:21;3.9;0.25
Timothy Castagne;V;10;5;6.2 22;1:1.67,2:4.2,3:11,4:20;1:3.75,2:15.5,3:24;1:1.11,2:1.57,3:2.67,4:5.2,5:10;1:1.37,2:2.67,3:6.5,4:14,5:21;5.4;0.85
Nathan Ngoy;V;10;7.6;9.75;1:1.98,2:5.9,3:15,4:23;1:4.25,2:17.5,3:24;1:1.29,2:2.25,3:5,4:10.75,5:18.5;1:1.47,2:3.15,3:7.8,4:16.5,5:23;2.77;0.80
Arda Güler;L;3.3;2.22;3.95 16 24;3:1.42,4:2,5:3.15,6:5.6,7:9.75,8:15,9:20;1:1.31,2:2.32,3:5.3,4:11.5,5:19.5;1:1.21,2:1.95,3:3.95,4:8.25,5:15.5;1:1.6,2:3.8,3:10,4:19,5:24;6.2;0.92
Yunus Akgün;L;3.3;2.55;5.6 21;1:1.16,2:1.8,3:3.45,4:7.3,5:14,6:21;1:1.85,2:5.2,3:13.5,4:22;1:1.21,2:1.95,3:3.95,4:8.25,5:15.5;1:1.6,2:3.75,3:9.75,4:18.5,5:24;4.3;0.60
Deniz Gul;L;3.2;2.62;6.5 22;2:1.28,3:1.88,4:3.2,5:6,6:11,7:17,8:22;1:1.47,2:3.15,3:7.9,4:16.5,5:23;1:1.62,2:3.8,3:9.75,4:18.5;1:1.2,2:1.98,3:4,4:8.75,5:16,6:22;5;0.25
Enes Ünal;L;3.65;2.9;6.5 22;2:1.45,3:2.35,4:4.5,5:8.75,6:15.5,7:21;1:1.62,2:3.85,3:10,4:19,5:24;1:1.62,2:3.8,3:9.75,4:18.5;1:1.47,2:3.2,3:8,4:16.5,5:23;3.9;0.55
Barış Yılmaz;L;3.8;2.85;5.8 21;1:1.14,2:1.72,3:3.15,4:6.6,5:13,6:19.5,7:23;1:1.87,2:5.2,3:14,4:22;1:1.25,2:2.12,3:4.45,4:9.5,5:17;1:1.15,2:1.75,3:3.3,4:6.9,5:13.5,6:20;3.15;0.90
Oguz Aydin;L;3.9;2.15;3.2 13 23;1:1.14,2:1.72,3:3.15,4:6.6,5:13,6:19.5,7:23;1:1.88,2:5.4,3:14,4:22;1:1.14,2:1.72,3:3.1,4:6.3,5:12;1:1.55,2:3.6,3:9.25,4:18,5:23;3.9;0.50
Ilhan Fakili;L;3.9;2.85;5.6 21;2:1.42,3:2.27,4:4.25,5:8.25,6:14.5,7:20;1:1.67,2:4.1,3:10.75,4:20,5:24;1:1.18,2:1.85,3:3.55,4:7.4,5:14;1:1.36,2:2.62,3:6.3,4:13.5,5:21;6.5;0.20
Can Uzun;L;3.9;2.62;4.7 19;2:1.4,3:2.2,4:4.05,5:7.9,6:14,7:20;1:1.78,2:4.8,3:13,4:21;1:1.13,2:1.67,3:3,4:6,5:11.5;1:1.37,2:2.65,3:6.4,4:14,5:21;3.9;0.40
Hakan Calhanoglu;L;4.65;3.85;8.5 24;2:1.22,3:1.72,4:2.77,5:5,6:9,7:15,8:20;1:1.37,2:2.6,3:6.2,4:13.5,5:21;1:1.11,2:1.6,3:2.77,4:5.4,5:10.5;1:1.45,2:3,3:7.4,4:15.5,5:22;4.3;0.40
Orkun Kökçü;L;4.65;2.4;3.4 14 23;1:1.19,2:1.93,3:3.85,4:8.25,5:15.5,6:22;1:1.93,2:5.7,3:15,4:23;1:1.15,2:1.72,3:3.15,4:6.4,5:12.5;1:1.5,2:3.35,3:8.5,4:17,5:23;3.75;0.75
Mustafa Eskihellaç;L;9.25;5.3;7 23;1:1.78,2:4.7,3:12.5,4:21;1:4.5,2:18,3:24;2:1.39,3:2.15,4:3.85,5:7.3,6:13;1:1.5,2:3.25,3:8.25,4:17,5:23;4.65;0.08
Salih Özcan;L;9.25;6.2;8.5 24;1:1.62,2:3.9,3:10.25,4:19.5,5:24;1:2.5,2:8.75,3:19.5,4:24;1:1.11,2:1.6,3:2.77,4:5.4,5:10.5;1:1.14,2:1.72,3:3.15,4:6.5,5:13,6:19.5,7:23;3.9;0.80
İsmail Yüksek;L;9.25;6.2;8.5 24;1:1.47,2:3.1,3:7.7,4:16,5:23;1:3.75,2:15.5,3:24;3:1.23,4:1.6,5:2.27,6:3.55,7:5.9;1:1.12,2:1.65,3:2.95,4:6,5:11.75,6:18.5,7:23;2.77;0.55
Zeki Celik;L;9.75;6.2;7.9 24;1:1.83,2:5.1,3:13.5,4:22;1:3.5,2:14.5,3:23;2:1.18,3:1.57,4:2.4,5:4.05,6:7.2;1:1.29,2:2.35,3:5.3,4:11.5,5:19.5,6:24;3.5;0.80
Merih Demiral;L;9.25;7.7;10.5;1:1.52,2:3.35,3:8.5,4:17.5,5:23;1:3.1,2:12.5,3:23;1:1.25,2:2.12,3:4.5,4:9.75,5:17;1:1.42,2:2.85,3:6.9,4:15,5:22;3.2;0.85
Ozan Kabak;L;9.75;8;10.5;1:2.18,2:7.1,3:17.5,4:24;1:4.65,2:18.5,3:25;1:1.21,2:1.95,3:3.9,4:8.25,5:15.5;1:1.33,2:2.5,3:5.8,4:13,5:20;2.9;0.40
Ferdi Kadıoğlu;L;9.25;5.5;7.3 23;1:1.88,2:5.4,3:14,4:22;1:4.45,2:18,3:24;1:1.12,2:1.62,3:2.82,4:5.6,5:10.75;1:1.7,2:4.25,3:11.25,4:20;4.3;0.85
Ahmetcan Kaplan;L;9.75;8;10.5;1:2.18,2:7.1,3:17.5,4:24;1:5.1,2:20,3:25;1:1.25,2:2.12,3:4.5,4:9.75,5:17;1:1.7,2:4.3,3:11.5,4:20;2.9;0.08
Abdülkerim Bardakcı;L;14.5;11.25;10.5;1:1.72,2:4.45,3:11.75,4:21;1:4.4,2:18,3:24;1:1.15,2:1.72,3:3.2,4:6.5,5:12.5;1:1.7,2:4.3,3:11.5,4:20;3.75;0.02
Eren Elmali;L;13.5;4.15;4.6 18.5;1:1.88,2:5.4,3:14,4:22;1:4.5,2:18,3:24;1:1.15,2:1.75,3:3.2,4:6.5,5:12.5;1:1.67,2:4.2,3:11,4:20;3.75;0.30
Emirhan Topcu;L;13.5;10.5;10.5;1:2.15,2:6.9,3:17,4:24;1:5.1,2:20,3:25;1:1.18,2:1.87,3:3.6,4:7.5,5:14;1:1.52,2:3.35,3:8.5,4:17.5,5:23;2.7;0.50
"""
def esc(s): return {int(k): float(v) for k, v in (it.split(':') for it in s.split(','))}
def asist(s):
    if not s.strip(): return None
    xs = s.split(); return {i + 1: float(x) for i, x in enumerate(xs)}
jug, info = [], []
for row in J.strip().splitlines():
    nm, ld, anota, aoa, asi, sh, sot, tk, fc, tj, tit = row.split(';')
    lado = 'local' if ld == 'L' else 'visitante'
    jug += [dict(jugador=nm, lado=lado, stat='remates', escalera=esc(sh)), dict(jugador=nm, lado=lado, stat='al_arco', escalera=esc(sot)),
            dict(jugador=nm, lado=lado, stat='entradas', escalera=esc(tk)), dict(jugador=nm, lado=lado, stat='faltas', escalera=esc(fc)),
            dict(jugador=nm, lado=lado, stat='anota', cuota=float(anota)), dict(jugador=nm, lado=lado, stat='anota_o_asiste', cuota=float(aoa)),
            dict(jugador=nm, lado=lado, stat='tarjeta', cuota=float(tj))]
    a = asist(asi)
    if a: jug.append(dict(jugador=nm, lado=lado, stat='asiste', escalera=a))
    info.append(dict(nombre=nm, lado=lado, titular=float(tit), minutos=82))
# porteros
jug += [dict(jugador='Uğurcan Çakır', lado='local', stat='atajadas', escalera={3: 1.36, 4: 1.9, 5: 3, 6: 5.1, 7: 8.75}),
        dict(jugador='Senne Lammens', lado='visitante', stat='atajadas', escalera={3: 1.45, 4: 2.12, 5: 3.5, 6: 6.2, 7: 10.75})]
info += [dict(nombre='Uğurcan Çakır', lado='local', titular=0.95, minutos=90), dict(nombre='Senne Lammens', lado='visitante', titular=0.95, minutos=90)]
# Lukaku: baja confirmada (cadera, 11-nov); Betano sigue con sus líneas
info.append(dict(nombre='Romelu Lukaku', lado='visitante', titular=0.0, minutos=0, fuera=True))

# ---- parejas «cualquiera de los jugadores…»
P = {
 'asiste': """Oguz Aydin|Arda Güler 2.22;Oguz Aydin|Romelu Lukaku 2.22;Oguz Aydin|Kevin De Bruyne 2.37;Oguz Aydin|Youri Tielemans 2.37;Romelu Lukaku|Arda Güler 2.5;Romelu Lukaku|Kevin De Bruyne 2.67;Arda Güler|Kevin De Bruyne 2.7;Arda Güler|Youri Tielemans 2.7;Kevin De Bruyne|Youri Tielemans 2.92;Youri Tielemans|Dodi Lukébakio 2.95;Dodi Lukébakio|Nicolas Raskin 3.1;Youri Tielemans|Nicolas Raskin 3.1;Dodi Lukébakio|Leandro Trossard 3.15;Youri Tielemans|Leandro Trossard 3.15;Nicolas Raskin|Leandro Trossard 3.35;Dodi Lukébakio|Barış Yılmaz 3.4;Nicolas Raskin|Barış Yılmaz 3.6;Leandro Trossard|Barış Yılmaz 3.7""",
 'anota_o_asiste': """Romelu Lukaku|Oguz Aydin 1.24;Romelu Lukaku|Arda Güler 1.24;Romelu Lukaku|Kevin De Bruyne 1.31;Oguz Aydin|Kevin De Bruyne 1.42;Oguz Aydin|Leandro Trossard 1.44;Arda Güler|Kevin De Bruyne 1.44;Arda Güler|Leandro Trossard 1.45;Kevin De Bruyne|Leandro Trossard 1.5;Leandro Trossard|Deniz Gul 1.53;Deniz Gul|Dodi Lukébakio 1.57;Leandro Trossard|Dodi Lukébakio 1.57;Leandro Trossard|Barış Yılmaz 1.57;Oguz Aydin|Arda Güler 1.62;Deniz Gul|Youri Tielemans 1.62""",
 'anota': """Romelu Lukaku|Kevin De Bruyne 1.4;Romelu Lukaku|Leandro Trossard 1.4;Romelu Lukaku|Deniz Gul 1.44;Romelu Lukaku|Arda Güler 1.45;Kevin De Bruyne|Leandro Trossard 1.72;Deniz Gul|Kevin De Bruyne 1.82;Deniz Gul|Leandro Trossard 1.82;Arda Güler|Kevin De Bruyne 1.85;Arda Güler|Leandro Trossard 1.85;Kevin De Bruyne|Barış Yılmaz 1.93;Leandro Trossard|Barış Yılmaz 1.93;Deniz Gul|Arda Güler 1.98;Dodi Lukébakio|Youri Tielemans 2.07;Deniz Gul|Barış Yılmaz 2.1""",
 'tarjeta': """Nicolas Raskin|Barış Yılmaz 1.93;Nicolas Raskin|Dodi Lukébakio 2.07;Barış Yılmaz|Dodi Lukébakio 2.07;Nicolas Raskin|Salih Özcan 2.1;Barış Yılmaz|Salih Özcan 2.1;Dodi Lukébakio|Salih Özcan 2.27;Oguz Aydin|Hakan Calhanoglu 2.4;Oguz Aydin|Youri Tielemans 2.5;Oguz Aydin|Kevin De Bruyne 2.57;Hakan Calhanoglu|Youri Tielemans 2.62;Hakan Calhanoglu|Kevin De Bruyne 2.7;Youri Tielemans|Kevin De Bruyne 2.82""",
}
parejas = []
for stat, txt in P.items():
    for it in txt.split(';'):
        nm, c = it.rsplit(' ', 1)
        a, b = nm.split('|')
        parejas.append(dict(stat=stat, jugadores=[a, b], cuota=float(c)))

out = dict(local='Turquía', visitante='Bélgica', liga='UEFA Nations League · Liga A', fecha='2026-11-12 12:00',
           betano=dict(lineas=lineas, unicos=unicos, jugadores=jug, parejas=parejas), jugadores=info)
aqui = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(aqui, 'ficha.json')):
    f = json.load(open(os.path.join(aqui, 'ficha.json')))
    out['ficha'] = f.get('ficha'); out['informe'] = f.get('informe'); out['estadio'] = f.get('estadio'); out['cuotas_leidas'] = f.get('cuotas_leidas')
json.dump(out, open(os.path.join(aqui, 'entrada.json'), 'w'), ensure_ascii=False, indent=1)
print(len(lineas), 'líneas', len(unicos), 'únicos', len(jug), 'líneas de jugador', len(parejas), 'parejas')
