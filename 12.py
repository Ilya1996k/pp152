def s(n):
    f=0
    for i in n:
        f+= int(i)
    return f

for i in range(10000):
    n='4'+'0'*i
    while '40' in n or '800' in n or '000' in n:
        if '40' in n:
            n=n.replace('40','0',1)
        if '800' in n:
            n=n.replace('800','04',1)
        if '000' in n:
            n=n.replace('000','8',1)
    if s(n)==36:
        print(i)