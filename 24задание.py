'''with open('9_0021.txt') as f:
    s = f.readline().strip()

k = m = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        k += 1
        m = max(m,k)
    else:
        k = 1
print(m)'''
'''with open('9_0021.txt') as f:
    s = f.readline().strip()

k = m = 0
for i in range(len(s)):
    if s[i] not in 'ecf':
        k += 1
        m = max(m,k)
    else:
        k = 0
print(m)'''
'''with open('12_0147.txt') as f:
    s = f.readline().strip()

k = m = 0
for i in range(len(s)):
    if s[i] in '0123456789ABCDE':
        k += 1
        m = max(m,k)
    else:
        k = 0
print(m)'''
'''with open('14_0126.txt') as f:
    s = f.readline().strip()

k = m = 1
for i in range(1, len(s)):
    if s[i] in 'ABCDE'and s[i - 1] in 'ABCDE':
        k = 1
        m = max(m,k)
    else:
        k += 1
        m = max(m,k)
print(m)'''
'''with open('15_0001.txt') as f:
    s = f.readline().strip()
#первый способ
m = 0
p = ''
for i in range(len(s)):
    p += s[i]
    if 'XYZZY' in p:
        p = 'YZZY'
    else:
        m = max(m,len(p))
print(m)
#второй способ
s = s.replace('XYZZY', 'XYZZ YZZY').split()
print(max([len(x) for x in s]))'''
'''with open('19_0010.txt') as f:
    s = f.readline().strip()
    
print('XYZ'* 4 + 'X' in s)'''
'''with open('23_0052.txt') as f:
    s = f.readline().strip()
s = s.replace('E', 'A').replace('C','B').replace('D', 'B').replace('F','B')
print('BA' * 9 in s)'''
'''with open('21_0004.txt') as f:
    s = f.readline().strip()
s = s.replace('XY', 'ZY')
print('ZY' * 11 in s)'''
#повторяющиеся шаблоны с перекрытиями
'''with open('26_0001.txt') as f:
    s = f.readline().strip()
s = s.replace('XYZYX', 'XYZ ZYX').replace('ZYXYZ','ZYX XYZ')
s = s.replace('ZYX', 'XYZ')
print('XYZ' * 4 in s)'''


with open('1_0091.txt') as f:
    s = f.readline().strip()
p = ''
m = 0
for i in range(len(s)):
    p += s[i]
    while p.count('Y')>4:
        p = p[1:]
    m = max(m, len(p))
print(m)
