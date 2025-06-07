def R(n):
    sm=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sm.add(i)
            sm.add(n//i)
    return sum(sm)
def p(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n%i==0:
            return 0
    return 1
for i in range(1500001, 10000000):
    r=R(i)
    if r!=0:
        if p(r):
            print(i,r)