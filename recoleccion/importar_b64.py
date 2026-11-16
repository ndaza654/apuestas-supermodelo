# -*- coding: utf-8 -*-
"""Importa archivos recolectados en el navegador, enviados comprimidos (gzip + base64) para que pasen por el chat más cortos.

    python3 recoleccion/importar_b64.py <carpeta_base> < registros.txt

Cada línea de la entrada:  <ruta relativa>\t<sha256 (12 primeros)>\t<gzip+base64 del texto UTF-8>
En el navegador (flashscore.co o betano.co):
    const gz = async t => { const s = new Blob([t]).stream().pipeThrough(new CompressionStream('gzip')); const b = new Uint8Array(await new Response(s).arrayBuffer()); let x=''; for (const c of b) x += String.fromCharCode(c); return btoa(x); };
    const sha = async t => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))].map(b => b.toString(16).padStart(2,'0')).join('').slice(0,12);
Escribe el archivo SOLO si el sha256 del texto descomprimido coincide con el que calculó el navegador (si no, lo dice y no escribe).
"""
import base64, gzip, hashlib, os, sys


def main(base):
    ok = mal = 0
    for ln in sys.stdin:
        ln = ln.rstrip('\n')
        if not ln.strip():
            continue
        try:
            ruta, h, b64 = ln.split('\t')
            texto = gzip.decompress(base64.b64decode(b64)).decode('utf-8')
        except Exception as e:
            print('ERROR al leer la línea:', ln[:60], e)
            mal += 1
            continue
        sha = hashlib.sha256(texto.encode('utf-8')).hexdigest()[:12]
        if sha != h:
            print(f'HASH DISTINTO {ruta}: navegador {h}, aquí {sha} (no se escribe)')
            mal += 1
            continue
        dest = os.path.join(base, ruta)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w', encoding='utf-8', newline='') as f:
            f.write(texto)
        print(f'OK {ruta} {len(texto)} bytes sha {sha}')
        ok += 1
    print(f'{ok} archivos escritos, {mal} con error')
    sys.exit(1 if mal else 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
