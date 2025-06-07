from ipaddress import *

net = ip_network("192.168.76.160/255.255.255.240", 0)

cnt = 0

for i in net.hosts():
    ip = bin(int(i))[2:]
    if ip[-1] == '0' and ip[-8:].count('1') % 2 == 0:
        cnt += 1
print(cnt)