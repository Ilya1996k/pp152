r = [list(map(int, i.split())) for i in open("26.txt").readlines()]


r = r[1:]

a={}
for i in r:
    a[i[0]] = sorted(a.get(i[0],[])+[i[1]])

mn = 10**100
for i in sorted(a.keys()):
    if i == 1 or i == 400004:
        continue
    if len(a[i]) >=35 and any([a[i][j] - a[i][j-1]>=3 for j in range(1,len(a[i]))]):
        if len(a.get(i-1,[])) + len(a.get(i+1,[]))<=mn:
            print(i)
            mn = min(len(a.get(i-1,[])) + len(a.get(i+1,[])),mn)
print(f"///{mn}")