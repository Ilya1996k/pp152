a = open('24.txt').readline()
l = -1
r = -1
k3 = 0
mn = 10 ** 23
while True:
    if k3 < 1000:
        r += 1
        if r >= len(a):
            break
        if int(a[r], 36) % 3 == 0:
            k3 += 1
    else:
        l += 1
        if int(a[l], 36) % 3 == 0:
            k3 -= 1
    if k3 == 1000:
        mn = min(mn, r - l)
print(mn)
