def alg(s):
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        else:
            s = s.replace('222', '11', 1)
    return s
mx = -10 ** 23
res = ''
for i in range(204):
    s = i * '1' + '2' + (203 - i) * '1'
    r = alg(s)
    if len(r) > mx:
        mx = len(r)
        res = r
print(res)