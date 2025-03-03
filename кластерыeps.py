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
print(int(x*10000), int(y*10000))

