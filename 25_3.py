def dl(n):
    l = []
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            l.append(i)
            l.append(n//i)
    return l


for i in range(33333,55556):
    q = sum([j for j in dl(i) if dl(j)==[]])
    if q!=0 and i%q==0 and q>250:
        print(i,q)