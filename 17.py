a = open('17 (1).txt').readlines()
for i in range(len(a)):
    a[i] = int(a[i])
mn = 100000000000000000000
for i in range(len(a)):
    if abs(a[i])%10 == 3:
        mn = min(mn, a[i])
k = 0
mxs = -1000000000
for i in range(len(a)-1):
    if abs(a[i])%10 == abs(a[i+1])%10:
        if ((a[i]%3 == 0) + (a[i+1]%3 == 0)) == 1:
            if a[i]**2 + a[i+1]**2 <= mn**2:
                k += 1
                mxs = max(mxs,a[i]**2 + a[i+1]**2)
print(k, mxs)