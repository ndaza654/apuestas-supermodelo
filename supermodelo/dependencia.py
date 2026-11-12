# -*- coding: utf-8 -*-
"""Corrección de la dependencia entre patas de un combo, medida con datos reales.

El simulador da la probabilidad conjunta de las patas, pero para algunas parejas su dependencia no coincide con la
real. Se midió el «lift» = P(A y B) / (P(A)·P(B)) en 62 000 partidos (dentro de liga × goles esperados × diferencia
de fuerza, con la línea de cada estadística en su media) y en el simulador calibrado (datos/dependencia_pares.json):
  · Gana el favorito + córners del favorito Más: real 0,88 (se estorban), simulador 0,93;
  · Más 2.5 goles + córners totales Más: real 0,98, simulador 1,035 (el combo del 9-nov salía inflado);
  · Menos 2.5 + córners Menos: real 0,98, simulador 1,03;
  · Más 2.5 + tarjetas Más: real 1,00, simulador 0,95;
  · Gana el favorito + sus tiros al arco Más: real 1,27, simulador 1,28 (bien).
El factor real/sim se aplica a la probabilidad conjunta de cada pareja de patas reconocida (en las dos direcciones:
si una pata es "Menos"/"No", se usa el complemento). Parejas no medidas: sin corrección.
"""
import json, os

RUTA = os.path.join(os.path.dirname(__file__), '..', 'datos', 'dependencia_pares.json')
_T = None


def tabla():
    global _T
    if _T is None:
        try:
            _T = json.load(open(RUTA, encoding='utf-8'))
        except OSError:
            _T = {}
    return _T


def categoria(sel, fav):
    """(clave, positiva) de una pata: positiva=False si es el lado complementario (Menos / No / pierde)."""
    m, lado, amb = sel.get('mercado'), sel.get('lado'), sel.get('ambito', 'total')
    quien = None
    if amb in ('local', 'visitante') and fav is not None:
        quien = 'fav' if (amb == 'local') == (fav == 0) else 'nofav'
    if m == 'resultado' and fav is not None:
        f = '1' if fav == 0 else '2'
        if lado == f:
            return ('fav_gana', True)
        return None
    if m == 'goles' and amb == 'total' and 1.5 <= float(sel.get('linea', 0)) <= 3.5:
        return ('o25', lado == 'mas')
    if m == 'ambos':
        return ('btts', lado == 'si')
    if m == 'corners' and amb == 'total':
        return ('c_mas', lado == 'mas')
    if m == 'corners' and quien:
        return ('c_' + quien, lado == 'mas')
    if m == 'tarjetas' and amb == 'total':
        return ('t_mas', lado == 'mas')
    if m == 'remates' and amb == 'total':
        return ('sh_mas', lado == 'mas')
    if m == 'remates' and quien == 'fav':
        return ('sh_fav', lado == 'mas')
    if m == 'al_arco' and quien == 'fav':
        return ('sot_fav', lado == 'mas')
    return None


def _lift_dir(L, pa, pb, pos_a, pos_b):
    """Lift para la dirección pedida a partir del lift 'positivo' L (A y B en su lado Más/Sí)."""
    pab = L * pa * pb
    if pos_a and pos_b:
        return L
    if pos_a and not pos_b:
        return (pa - pab) / (pa * (1 - pb)) if pa * (1 - pb) > 0 else 1.0
    if not pos_a and pos_b:
        return (pb - pab) / ((1 - pa) * pb) if (1 - pa) * pb > 0 else 1.0
    return (1 - pa - pb + pab) / ((1 - pa) * (1 - pb)) if (1 - pa) * (1 - pb) > 0 else 1.0


NOMBRES = {'fav_gana': 'gana el favorito', 'o25': 'goles Más', 'btts': 'ambos marcan Sí/No:', 'c_mas': 'córners totales Más',
           'c_fav': 'córners del favorito Más', 'c_nofav': 'córners del no favorito Más', 't_mas': 'tarjetas Más',
           'sh_mas': 'remates totales Más', 'sh_fav': 'remates del favorito Más', 'sot_fav': 'tiros al arco del favorito Más',
           'u25': 'goles Menos', 'c_mas_menos': 'córners Menos'}


def factor(patas, fav):
    """patas: lista de (sel, p_pata_simulada). Devuelve (factor, notas). Factor acotado a [0,85; 1,15]."""
    T = tabla()
    cats = [(categoria(s, fav), p) for s, p in patas]
    f, notas = 1.0, []
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            (ca, pa), (cb, pb) = cats[i], cats[j]
            if not ca or not cb:
                continue
            k = f'{ca[0]} & {cb[0]}' if f'{ca[0]} & {cb[0]}' in T else (f'{cb[0]} & {ca[0]}' if f'{cb[0]} & {ca[0]}' in T else None)
            if not k:
                continue
            if k.startswith(cb[0] + ' &') and not k.startswith(ca[0] + ' &'):
                (ca, pa), (cb, pb) = (cb, pb), (ca, pa)
            # Los lifts se midieron con la línea de cada estadística en su media (p ≈ 0,5); por eso la otra dirección se deriva
            # con p = 0,5. Si existe la pareja medida directamente en la dirección Menos + Menos (u25 & c_mas_menos), se usa esa.
            if k == 'o25 & c_mas' and not ca[1] and not cb[1] and 'u25 & c_mas_menos' in T:
                lr, ls = T['u25 & c_mas_menos']['real'], T['u25 & c_mas_menos']['sim']
            else:
                r, s_ = T[k]['real'], T[k]['sim']
                lr = _lift_dir(r, 0.5, 0.5, ca[1], cb[1]); ls = _lift_dir(s_, 0.5, 0.5, ca[1], cb[1])
            fx = lr / ls if ls > 0 else 1.0
            if abs(fx - 1) >= 0.01:
                f *= fx
                def nm(c_):
                    if c_[0] == 'fav_gana':
                        return 'gana el favorito'
                    if c_[0] == 'btts':
                        return 'ambos marcan ' + ('Sí' if c_[1] else 'No')
                    return NOMBRES.get(c_[0], c_[0]).replace(' Más', '') + (' Más' if c_[1] else ' Menos')
                notas.append(f"{nm(ca)} + {nm(cb)}: dependencia real {lr:.2f} contra {ls:.2f} del simulador (×{fx:.3f})")
    return max(0.85, min(1.15, f)), notas
