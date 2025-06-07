from re import findall
s = open('24.txt').readline().replace('.', '. ')
c = r'[LNDlnd][lnd]*'
pattern = rf'[ ][LND][lnd]*(?:[ ]{c})+[.]'
a = findall(pattern, s)
mx = 0
print(len(max(a, key=len)))
for x in a:
    d = {}
    for i in x[:-1].split():
        d[i] = d.get(i, 0) + 1
    v = list(d.values())
    if len(v) - v.count(1) <= 2:
        mx = max(mx, len(x)-1)
print(mx)



