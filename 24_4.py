s = open('24 (2).txt').readline()
ka = [0]
kn = [0]
for x in s:
    if x.isdigit():
        ka.append(ka[-1])
        kn.append(kn[-1]+1)
    else:
        ka.append(ka[-1] + 1)
        kn.append(kn[-1])
r = []
for i in range(len(ka)):
    r.append((ka[i], kn[i]))
print(r[:20])
mx = 0
for i in range(len(r)-1):
    for j in range(i+1,len(r)):
        Lka = r[i][0]
        Lkn = r[i][1]
        Rka = r[j][0]
        Rkn = r[j][1]
        Ka = Rka - Lka
        Kn = Rkn - Lkn
        if Ka == 2*Kn:
            mx = max(mx , j-i)
print(mx)

