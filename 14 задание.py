'''n = 343**25-49**18+8**4-2
k =0
while n > 0:
  if n % 7 == 6:
    k +=1
  n//= 7
print (k)'''

'''for a in range (10):
    for b in range (10):
        n = int(f'1{a}24563{b}7')
        if n % 17 == 0:
            print (n, n // 17)'''

# 3535*57, дел. на 263
'''from fnmatch import fnmatch 
for n in range (0, 10**9, 263):
    if fnmatch(str(n), '3535*57'):
        print(n, n // 263)'''

'''n = (6561**1346 + 729**1473) * 9**820 - 81
k = [0] * 9
while n> 0:
  k[n % 9] += 1
  n //= 9
print (k[8] - k[0])'''

'''b = 14
for x in range(b):
    s = x*b**4 + 5*b**3 + 4*b**2 + 7*b + 2
    s += 6*b**4 + 4*b**3 + x*b**2 + 5*b + 3
    if s % 15 == 0:
        print (x, s // 15)
b = 14
for x in range(b):
    s = (((x*b+5)*b+4)*b+7)*b+2
    s += (((6*b+4)*b+x)*b+5)*b+3
    if s % 15== 0:
        print (x, s // 15)
b = 14
for n in range(b):
    s = int(f'{x}5472', 14) + int(f'64{x}53', 14)
    if s % 15 == 0:
        print(x, s // 15)'''

'''for x in range (10):
    b = 70854 + x*1000
    s =（6*b**2 + 4*b + 8）+（b**2 + 4*b + 3）
    if s % 115 == 0：
        print (x, s // 115)'''

'''def q(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s
for n in range(200, 0, -1):
    s = q(n)
    if s.endswith('123'):
        print(n, end='')'''
  
for x in range (1, 2001) :
    n = 4**120 - 26 * x
    k = 0
    while n > 0:
        if n % 4 == 0：
            k += 1
        n //= 4
    if k == 6：
        print (x)
        break
