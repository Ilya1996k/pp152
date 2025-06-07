a = open('24.txt').readline()
mx = 0
l = -1
r = -1
colA = 0
colO = 0
while True:
    if colO <= 100 and colA <= 100:
        r += 1
        if len(a) == r:
            break
        if a[r] == "A":
            colA += 1
        if a[r] == "O":
            colO += 1
    else:
        l += 1
        if a[l] == "O":
            colO -= 1
        if a[l] == "A":
            colA -= 1
    if colO <= 100 and colA <= 100:
        mx = max(mx, r - l)
print(mx)