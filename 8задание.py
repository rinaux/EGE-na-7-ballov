import re

s = open('5_0284.txt').readline().strip()

m = ''
for p in re.finditer(r'(([1-9]+|[abc][1-9a-c]*)\+)*([1-9]+|[abc][1-9a-c]*)', s):
    t = p.group(0)
    m = max(m, t, key=lambda x: len(x))
print(m)
print(len(m))


