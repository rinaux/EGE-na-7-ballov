import re

s = open('4_0224.txt').readline().strip()

m = ''
for p in re.finditer(r'((0|[6-9][0,6-9]*)[-*])*(0|[6-9][0,6-9]*)', s):
    t = p.group(0)
    m = max(m, t, key=lambda x: len(x))
print(m)
print(len(m))
