import re, datetime as dt
MON={m:i+1 for i,m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
def parse(path):
    out=[]; year=None; last=None; cur=None
    d_re=re.compile(r'^\s*(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+([A-Z][a-z]{2})\s+(\d{1,2})(?:\s+(\d{4}))?\s*$')
    m_re=re.compile(r'^\s*(?:\d\d:\d\d\s+)?(.+?)\s+v\s+(.+?)\s+(\d+)-(\d+)(?:\s+\(\d+-\d+\))?(?:\s+\[.*\])?\s*$')
    txt=open(path,encoding='utf8').read()
    hy=re.search(r'# Date\s+\w+ \w+ \d+ (\d{4})',txt)
    year=int(hy.group(1)) if hy else None
    m2=re.compile(r'^\s*(?:\d\d:\d\d\s+)?(.+?)\s+(\d+)-(\d+)(?:\s+\(\d+-\d+\))?\s+(\S.*?)\s*$')
    for line in txt.splitlines():
        d=d_re.match(line)
        if d:
            mo=MON[d.group(1)]; day=int(d.group(2))
            if d.group(3): year=int(d.group(3))
            elif last and mo<last.month: year+=1
            cur=dt.date(year,mo,day); last=cur; continue
        m=m_re.match(line)
        if m and cur:
            out.append((cur,m.group(1).strip(),m.group(2).strip(),int(m.group(3)),int(m.group(4)))); continue
        m=m2.match(line)
        if m and cur and ' v ' not in line:
            out.append((cur,m.group(1).strip(),m.group(4).strip(),int(m.group(2)),int(m.group(3))))
    return out
if __name__=='__main__':
    import glob
    for f in sorted(glob.glob('*.txt')):
        r=parse(f); print(f,len(r),r[0][0],r[-1][0], sum(x[3] for x in r)/len(r), sum(x[4] for x in r)/len(r))
