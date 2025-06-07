def f(n, m):
    if n > m:
        return 0
    if n == m:
        return 1
    if n < m:
        return f(n + 3, m) + f(n + 5, m) + f(n * 2, m)
a = f(4, 14) * f(14, 31)
b = f(4, 19) * f(19, 31)
exp = f(4, 14) * f(14, 19) * f(19, 31)
print(a + b - exp)