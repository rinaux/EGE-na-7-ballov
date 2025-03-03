'''with open('8_0028. txt') as f:
    n = int (f. readline())
    a = [int(x) for x in f]
m = 0
for i in range(len(a) - 1):
    m = max (m, a[i] + a[i + 1])
print (m)'''

'''with open('8_0020. txt') as f:
    a = [int(x) for x in f]
m = float ('-inf')
for i in range(len(a)):
    if a[i] % 10 = 3:
        m = max (m, a[i])
k = 0
s = float ('-infl
for i in range(len(a)-1):
    if (a[i] % 10 == 3 and a[i+1] % 10 != 3 or a[i]
    k += 1
    s = max(s, a[i]**2 + a[i+1]**2)
print (k, s)'''

'''with open ('1_0038. csv') as f:
    a = [[int(y) for y in x.split(',')] for x in f]
k = 0
for a, b, c in a:
    if a < b + cand b < a + c and c < a + b:
        k += 1
print (k)'''

with open('8_0021,txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f]
m = 0
k = 0
b = 0
afor i in range(len(a)): 1
    if a[i] % 3 == 0:
        m = max (a[il, m)
for i in range(len(a)-1):
    if (a[i] % 4 == 0 or a[i+1] % 4 == 0) and ((a[i] + a[i+1]) <= m):
        k = max(k, abs (a[i] + a[i+1]))
        b += 1
print (b, k)

