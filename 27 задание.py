'''def center(cluster):
    min_d = float('inf')
    for x1, y1 in cluster:
        d = 0
        for x2, y2 in cluster:
            d += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if d < min_d:
            min_d = d
            xc, yc = x1, y1
    return xc, yc
    
with open('4_0024.txt') as f:
    f.readline()
    c1, c2 = [], []
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if y >= 0.5*x+5:
            c1.append((x, y))
        else:
            c2.append((x, y))

x1, y1 = center(c1)
x2, y2 = center(c2)
x = (x1 + x2) / 2
y = (y1 + y2) / 2
print(int(x*10000), int(y*10000))'''

'''def center(cluster):
    min_d = float('inf')
    for x1, y1 in cluster:
        d = 0
        for x2, y2 in cluster:
            d += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if d < min_d:
            min_d = d
            xc, yc = x1, y1
    return xc, yc
    
with open('6_0042.txt') as f:
    f.readline()
    c1, c2, c3, c4 = [], [], [], []
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if y > 5 and x > 3.5:
            c1.append((x, y))
        elif y > 5 and x < 3.5:
            c2.append((x, y))
        elif y < 5 and x > 6:
            c3.append((x, y))
        else:
            c4.append((x, y))

x1, y1 = center(c1)
x2, y2 = center(c2)
x3, y3 = center(c3)
x4, y4 = center(c4)
x = (x1 + x2 + x3 + x4) / 4
y = (y1 + y2 + y3 + y4) / 4
print(int(x*10000), int(y*10000)'''

'''f = open('6_0042.txt')
n = f.readline()
a = [[] for i in range(4)]
for line in f:
    x, y = map(float, line.replace(',', '.').split())
    if y > 5 and x > 3.5:
        a[0].append([x, y])
    elif y > 5 and x < 3.5:
        a[1].append([x, y])
    elif y < 5 and x > 6:
        a[2].append([x, y])
    else:
        a[3].append([x, y])

sum_x = sum_y = tx = ty = 0
for i in a:
    mn = 100000050000
    for j in i:
        x1, y1 = j
        sm = 0
        for k in i:
            x2, y2 = k
            sm += ((x2-x1)**2 + (y2-y1)**2)**0.5
        if sm < mn:
            mn = sm
            tx, ty = x1, y1
    sum_x += tx
    sum_y += ty
print(int(sum_x / 4  * 10000))
print(int(sum_y / 4  * 10000))'''

'''def center(cluster):
    min_d = float('inf')
    for x1, y1 in cluster:
        d = 0
        for x2, y2 in cluster:
            d += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if d < min_d:
            min_d = d
            xc, yc = x1, y1
    return xc, yc
    
with open('4_0061.txt') as f:
    f.readline()
    c1, c2, c3 = [], [], []
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if y > 4 and x < 5 and y < 9:
            c1.append((x, y))
        elif y > 4 and y < 9 and x > 5 and x < 9:
            c2.append((x, y))
        else:
            c3.append((x, y))
    

x1, y1 = center(c1)
x2, y2 = center(c2)
x3, y3 = center(c3)
x = (x1 + x2 + x3) / 3
y = (y1 + y2 + y3) / 3
print(int(x*10000), int(y*10000))'''


'''from math import dist
from turtle import *

def visualize(clusters):
    m = 30
    screensize(2000, 2000)
    colors = ('blue', 'red', 'green', 'yellow') * 10
    up()
    tracer(0)
    for cluster, color in zip(clusters, colors):
        for x, y in cluster:
            goto(x * m, y * m)
            dot(6, color)
        update()
        done()
 
with open('11_0101.txt') as f:
    f.readline()
    data = []
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        data.append((x, y))
eps = 1
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data[:]:
            if dist(p1, p2) < eps:
                clusters[-1].append(p2)
                data.remove(p2)
print(len(clusters))
visualize(clusters)

x1, y1 = center(c1)
x2, y2 = center(c2)
x = (x1 + x2) / 2
y = (y1 + y2) / 2
print(int(x*10000), int(y*10000))'''

from math import dist
from turtle import *

def visualize(clusters):
    m = 30
    screensize(2000, 2000)
    colors = ('blue', 'red', 'green', 'yellow') * 10
    up()
    tracer(0)
    for cluster, color in zip(clusters, colors):
        for x, y in cluster:
            goto(x * m, y * m)
            dot(6, color)
    update()
    done()


with open('11_0101.txt') as f:
    f.readline()
    data = []
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        data.append((x, y))

eps = 1.5
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data[:]:
            if dist(p1, p2) < eps:
                clusters[-1].append(p2)
                data.remove(p2)
print(len(clusters))

centroids = []
for cluster in clusters:
    min_d = float('inf')
    for x1, y1 in cluster:
        d = 0.0
        for x2, y2 in cluster:
            d += dist((x1, y1), (x2, y2))
        if d < min_d:
            min_d = d
            cx, cy = x1, y1
    centroids.append((cx, cy))
sx, sy = 0.0, 0.0
for x, y in centroids:
    sx += x
    sy += y
print(int(sx / len(centroids) * 10000), int(sy / len(centroids) * 10000))

visualize(clusters)
