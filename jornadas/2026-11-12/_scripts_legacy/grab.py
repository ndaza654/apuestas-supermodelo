# -*- coding: utf-8 -*-
"""Saca del transcript de la sesión los bloques @@TAG:clave@@ ... @@END@@ devueltos por el navegador y los guarda en raw/."""
import json, re, sys, os, glob
T = sorted(glob.glob('/root/.claude/projects/-home-claude/*.jsonl'), key=os.path.getmtime)[-1]
OUT = '/home/claude/nov12/raw'
def textos():
    for line in open(T, encoding='utf8'):
        if '@@END@@' not in line or '"tool_result"' not in line: continue
        try: d = json.loads(line)
        except Exception: continue
        c = (d.get('message') or {}).get('content')
        if not isinstance(c, list): continue
        for b in c:
            if b.get('type') != 'tool_result': continue
            x = b.get('content')
            parts = [x] if isinstance(x, str) else [p.get('text', '') for p in x if isinstance(p, dict)]
            for t in parts:
                yield t
def main(tag=None):
    n = 0
    for t in textos():
        # el texto es una cadena JSON entre comillas (con \n escapados) seguida de notas del navegador
        m = re.match(r'\s*("(?:[^"\\]|\\.)*")', t, re.S)
        s = json.loads(m.group(1)) if m else t
        for mm in re.finditer(r'@@([A-Z0-9]+):([^@]+)@@\n(.*?)\n@@END@@', s, re.S):
            tg, k, body = mm.group(1), mm.group(2), mm.group(3)
            if tag and tg != tag: continue
            fn = os.path.join(OUT, f'{tg.lower()}_{k}.txt')
            open(fn, 'w', encoding='utf8').write(body); n += 1
    print(n, 'bloques guardados en', OUT)
if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
