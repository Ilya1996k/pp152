with open('27B.txt') as file:
    s = file.readlines()
s = [tuple(float(j) for j in i.strip().split()) for i in s]
from math import dist
def get_cluster():
    cluster = [s.pop(0)]
    for i in cluster:
        for j in s[::]:
            if dist(i, j) < 1:
                cluster.append(j)
                s.remove(j)
    return cluster

clusters = []
while len(s) > 0:
    clusters.append(get_cluster())
clusters = [i for i in clusters if len(i) >= 20]

def get_anti(kl):
    anti = (0, 0)
    mx = -10 ** 23
    for a in kl:
        sm = 0
        for i in kl:
            sm += dist(a, i)
        if mx < sm:
            mx = sm
            anti = a
    return (anti, mx)

antis = []
for kl in clusters:
    antis.append(get_anti(kl))

for kl in clusters:
    print(get_anti(kl))
print(*[abs(int(i * 10000)) for i in max(antis, key = lambda x : x[-1])[0]])