for a in range(1, 300):
    f = 1
    for x in range(300):
        for y in range(300):
            if ((3*x + y > a) and (y < x) and (x < 30)) == 0:
                continue
            else:
                f = 0
                break
    if f == 1:
        print(a)
