def m(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + n // i
    return 0

from fnmatch import fnmatch
for n in range(34, 10 ** 8, 100):
    r = m(n)
    if r != 0 and r % 117 == 0:
        if fnmatch(str(n), '51*2?34'):
            print(n, r)