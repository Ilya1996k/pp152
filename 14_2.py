for x in '0123456789ABCDEFGHIJKLMN':
    a = int(f'4M{x}F', 24)
    b = int(f'265AFDN{x}', 24)
    c = int(f'N4{x}931B3L', 24)
    d = int(f'NG{x}4F', 24)
    f = int(f'FKJB5{x}IK', 24)
    r = a+b+c+d+f
    if r % 23 == 0:
        print(x, r // 23)
