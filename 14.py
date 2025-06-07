def f(n):
    s = ""
    while n > 0:
        s += str(n % 9)
        n = n // 9
    return s[::-1]

def f25(n):
    s = []
    while n > 0:
        s += [n % 25]
        n = n // 25
    return s[::-1]

for x in range(1, 10000):
    a = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    k = f(a)
    if abs(k.count("2") - k.count("8")) == 471:
        print(x)