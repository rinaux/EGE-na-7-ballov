'''from itertools import product'''
'''i = 0
k = 0
a = []
for p in product(sorted('АМРС'), repeat=5):
    w = ''.join(p)
    i += 1
    if i % 2 == 1 and w[-1] != 'Р' and w.count('А') == 1:
        k += 1
        print(i, w)
        a.append(w)
print(a.index('ДОВОД')+1)
print(k)'''


'''a = []
for p in product('КОМПАС', repeat = 6):
    w = ''.join(p)
    if len(w) == len(set(w)) and w[0] != 'П' and 'АО' not in w:
        a.append(w)
print(a)
print(len(a))'''


'''a = []
for p in product ('0123', repeat = 5):
    w = ''.join(p)
    if w[0] != '0' and '02' not in w and '20' not in w and '13' not in w and '31' not in w:
        a.append(w)
print(a)
print(len(a))'''

'''a = []
for p in product('АИПРТ', repeat=5):
    w = ''.join(p)
    a.append(w)
print(a.index('АТИПА')+1)'''

'''i = 0
k = 0
a = []
for p in product('0123456789', repeat = 5):
    w = ''.join(p)
    i += 1
    if len(w) == len(set(w)) and (i % 2 == 0 or i % 2 == 1)and w[-1] == '9' and w[-2] == '2':
        k += 1
        print(i, w)
        a.append(w)
print(k)'''
'''print(a.index('ДОВОД')+1)'''

'''a = []
for p in product('КОМПАС', repeat = 6):
    w = ''.join(p)
    if w[-1] not in 'ИЕОА' and w[0] not in 'ИЕОА':
        t = w.replace('И', 'А').replace('Е','А').replace('О','А')
        t = t.replace('Г', 'Б').replace('П','Б').replace('Р','Б').replace('Л','Б')
        if 'БАБ' not in t:
            a.append(w)
print(a)
print(len(a))'''

from itertools import permutations 
a = [] 
for p in permutations('АКОСТ'): 
    w = ''.join(p) 
    if w[3] != 'С' and 'ТА' not in w: 
        a.append(w) 
print(len(a))

'''for n in range (1000, 10000):
    s = str(n)
    a, b, c, d = map(int, sorted(s)) I
    x, y = a + d, b * c
    if x < y:
        r = int (f'{x}{y}') # str(x) + str(y)
    else:
        r = int (f'{y}{x} ') # str(y) + str(x)
    if r > 85 and len(s) == len(set(s)):
        print(n, r)
        break'''
