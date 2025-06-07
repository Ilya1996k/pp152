from ipaddress import *

#НОМЕР КОМПЬЮТЕРА
from ipaddress import *
ip = '192.168.108.157' #введите ип адрес
mask = '255.255.255.192'#введите маску
k = bin(int(ip_address(mask)))[2:].count('0')
ipb = bin(int(ip_address(ip)))[2:]
n = int(ipb[-k:], 2)
print(n)

#ПОИСК СЕТИ
from ipaddress import *
ip = '192.168.108.157' #введите ип адрес
mask = '255.255.255.192'#введите маску
net = ip_network(f'{ip}/{mask}', 0)
print(net.network_address) #сеть

#ПОИСК МАКСИ
from ipaddress import *
ip = '220.128.112.142' #введите ип адрес узла
net0 = '220.128.96.0' #введите адрес сети
for mask in range(31):
    net = ip_network(f'{ip}/{mask}', 0)
    if str(net.network_address) == net0:
        print('МАСКА:', net.netmask, '   количество 1:', mask,'   количество 0:', 32 -mask)


for A in range(256):
    ip=f'183.192.{A}.0'
    mask='255.255.252.0'
    net=ip_network(f'{ip}/{mask}',0)
    f=1
    for x in net:
        x=bin(int(x))[2:]
        x1=x[-16:]
        if x1.count('1')>3:
            continue
        else:
            f = 0
            break
    if f == 1:
        print(A)