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
