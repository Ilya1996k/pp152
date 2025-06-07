from math import dist

def centroid(k):
    xk = 0
    yk = 0
    mn = 1000000000000000000
    for i in range(len(k)):
        x, y = k[i]
        mns = 0
        for j in range(len(k)):
            mns += dist(k[i], k[j])
        if mns < mn:
            mn = mns
            xk = x
            yk = y
    return xk, yk

def antycentroid(k):
    xk = 0
    yk = 0
    mx = -1000000000000000000
    for i in range(len(k)):
        x, y = k[i]
        sm = 0
        for j in range(len(k)):
            sm += dist(k[i], k[j])
        if sm > mx:
            mx = sm
            xk = x
            yk = y
    return xk, yk

def cnr(k):
    mx = 0
    for i in k:
        for j in k:
            mx = max(mx, dist(i, j))
    return mx


def fl(k):
    mx = 0
    for i in k:
        for j in k:
            mx = max(mx, abs(i[0] - j[0]), abs(i[1] - j[1]))
    return mx


with open('27A.txt') as f:
    s = [[float(j) for j in i.replace(',', '.').split()] for i in f.readlines()]


def cl():
    klaster = [s.pop(0)]
    for i in klaster:
        for j in s[::]:
            if dist(i, j) < 5:
                klaster.append(j)
                s.remove(j)
    return klaster
klasters = []
while len(s) > 0:
    cluster = cl()
    klasters.append(cluster)
print(len(klasters))
sm = 0
mx = 0
for x in klasters:
    sm += cnr(x)
    mx = max(mx, fl(x))
print(sm / len(klasters) * 10000, mx * 10000)