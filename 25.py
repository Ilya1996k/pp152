def p(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True


def R(n):
    r = 0
    for d in range(2, n):
        if n % d == 0 and p(d) == False:
            r += d
    return r


for i in range(987652,0,-1):
    if R(i) % 10 == 7:
        print(i)
