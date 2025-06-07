from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(50000)
@lru_cache()
def f(n):
    if n == 1:return 1
    return (4*n-3)*f(n-1)
for i in range(2,5169):
    f(i)
print(((f(5168)//11)+f(5166))//f(5165))



a = {}
a[1] = 1
for i in range(2,5169):
    a[i] = a[i-1]*(4*i-3)
print(((a[5168]//11)+a[5166])//a[5165])