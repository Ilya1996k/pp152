from ipaddress import *
ip = '195.102.65.64'
mask = '255.255.255.192'
net = ip_network(f'{ip}/{mask}', False)
k = 0
for i in net:
    x = bin(int(i))[2:][24:]
    if x.count('0') == x.count('1'):
        k += 1
print(k)