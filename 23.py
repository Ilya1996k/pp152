def f(a,b):
    if a==b:
        return 1
    if a>b:
        return 0
    if a<b:
        return f(a+1,b)+f(a*2,b)+f(a*3,b)
sm=0
for n in range(2,100,2):
    sm+=f(n,15)
print(sm)