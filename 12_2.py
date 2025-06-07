for n in range(4,10001,2):
    s = n*"1"+"7"
    while "117" in s or "17" in s:
        if "117" in s:
            s = s.replace("117","73",1)
        else:
            s = s.replace("17","1117",1)
    l = sum(int(i) for i in s)
    print(l,n)