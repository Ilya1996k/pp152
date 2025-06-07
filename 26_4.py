a = [int(x) for x in open('26.txt').readlines()]
a.pop(0)
a= list(set(a))
a.sort()
mx = 0
el = 0
k = 1
for i in range(len(a)-1):
    if a[i+1] - a[i] == 1:
        k+=1
        mx = max(mx, k)
        if k == 55:
            print(a[i+2-55:i+2])
    else:
        k = 1
print(mx)



