'''for n in range(1, 100):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '1'
    else:
        s += '0'
    if n % 2 == 0:
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    if r > 67:
        print(n, r)'''

'''for n in range(1, 100):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '1'
    else:
        s += '0'
    if s.count('1') % 3 == 0:
        s = '10' + s[2:]
    else:
        s = '11' + s[2:]
    r = int(s, 2)
    if r < 40:
        print(n, r)'''

'''for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    s += '0'
    r = int(s, 2)
    if r < 114:
    print(n, r)'''

# Дублируется последняя цифра: s += s[-1]

'''def t(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(2, 1000):
    s = t(n)
    if n % 3 == 0:
        s += s[-2]:
    else:
        s += t((n % 3 + 1) * 2)
    r = int(s, 3)
    if r >= 235:
        print(n, r)
        break'''
for n in range(1000,10000):
    a, b, c, d = map(int,sorted(str(n)))
    x, y = a+d, b*c
    if x < y:
        r = int(f'{x}{y}')
    else:
        r = int(f'{y}{x}')
    if r > 85 and len(str(n)) == len(set(str(n))) :
        print(n, r)
        break
