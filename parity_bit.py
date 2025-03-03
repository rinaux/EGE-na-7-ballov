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
