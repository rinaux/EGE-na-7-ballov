# Для 1-ой кучи камней
'''from functools import lru_cache 

def n(p): 
    return p + 1, p * 2 

@lru_cache(None) 
def res(p): 
    if p >= 100: 
        return 'Lose' 
    if p >= 70: 
        return 'Win' 
    if any(res(x) == 'Win' for x in n(p)): 
        return 'P1' 
    if all(res(x) in ('P1', 'Lose') for x in n(p)): # any, если Петя поддаётся/ошибается
        return 'V1' 
    if any(res(x) == 'V1' for x in n(p)): 
        return 'P2' 
    if all(res(x) in ('P1', 'P2', 'Lose') for x in n(p)): 
        return 'V2' 

for p in range(1, 70): 
    r = res(p) 
    if r != None: 
        print(p, r)'''

# Для 2-х куч камней
'''from functools import lru_cache 

def n(p): 
    return p + 1, p * 2 

@lru_cache(None) 
def res(p): 
    if p >= 100: 
        return 'Lose' 
    if p >= 70: 
        return 'Win' 
    if any(res(x) == 'Win' for x in n(p)): 
        return 'P1' 
    if all(res(x) in ('P1', 'Lose') for x in n(p)): # any, если Петя поддаётся/ошибается
        return 'V1' 
    if any(res(x) == 'V1' for x in n(p)): 
        return 'P2' 
    if all(res(x) in ('P1', 'P2', 'Lose') for x in n(p)): 
        return 'V2' 

for p in range(1, 70): 
    r = res(p) 
    if r != None: 
        print(p, r)'''

'''from functools import lru_cache

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
    print(s, res((6, s)))'''

from functools import lru_cache 

def next(p): 
    return p + 1, p * 2 

@lru_cache(None) 
def res(p): 
    if p >= 66: return 'Lose' 
    if p >= 52: return 'Win' 
    if any(res(x) == 'Win' for x in next(p)): return 'P1' 
    if all(res(x) in ('P1', 'Lose') for x in next(p)): return 'V1' # any, если Петя поддаётся/ошибается
    if any(res(x) == 'V1' for x in next(p)): return 'P2' 
    if all(res(x) in ('P1', 'P2', 'Lose') for x in next(p)): return 'V2' 
        
d = {a: [] for a in('Lose', 'Win', 'P1', 'V1', 'P2', 'V2')}

for s in range(1, 70): 
    r = res(s) 
    if r is not None: 
        d[r].append(s)
for n in d:
    print(n, d[n])
