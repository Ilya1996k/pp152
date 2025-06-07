with open('26.txt') as file:
    s = file.readlines()
s.pop(0)
s = [[int(i.strip().split()[0]), int(i.strip().split()[1]), int(i.strip().split()[2]), i.strip().split()[3]] for i in s]
#s = [[4, 3, 5, 'A'],
#     [7, 4, 4, 'B'],
 #    [17, 2, 3, 'B'],
 #    [18, 6, 7, 'A']]
a = []
b = []
now = 0
time_b = 0
c = 0
s.sort()
while not(len(s) == 0 and len(a) == 0 and len(b) == 0):
    if len(a) != 0:
        a[0][1] -= 1
    if len(b) != 0:
        b[0][2] -= 1
    if len(a) != 0:
        if a[0][1] == 0:
            if a[0][3] == 'A':
                b.append(a.pop(0))
            else:
                a.pop(0)
    if len(b) != 0:
        if b[0][2] == 0:
            if b[0][3] == 'B':
                a.append(b.pop(0))
                if len(a) > 1:
                    c += 1
            else:
                b.pop(0)
            if len(b) == 0:
                time_b = now
    if len(s) != 0:
        if s[0][0] == now:
            if s[0][3] == 'A':
                a.append(s.pop(0))
                if len(a) > 1:
                    c += 1
            else:
                b.append(s.pop(0))
    print(now, a, b)
    now += 1
    #if now % 1000 == 0:
    #    print(len(b))
print(c, time_b)