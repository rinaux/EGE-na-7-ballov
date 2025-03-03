from functools import lru_cache

def next(p):
    a,b = p
    x = []
    if a <= b:
        for t in range(a + 1, a * 3):
            x.append((t, b))
    if b <= a:
        for t in range(b + 1, b * 3):
            x.append((a, t))
    return x
    
@lru_cache(None)
def res(p):
    if sum(p) >= 65: return 'Win'
    if any(res(n) == 'Win' for n in next(p)): return 'P1'
    if all(res(n) == 'P1' for n in next(p)): return 'V1' # any
    if any(res(n) == 'V1' for n in next(p)): return 'P2'
    if all(res(n) in ('P1', 'P2') for n in next(p)): return 'V2'

for s in range(1, 58):
    print(s, res((6, s)))
