from ipaddress import *
ip = '172.16.8.0'
mask = '255.255.252.0'
net = ip_network(f'{ip}/{mask}',0)
print(net)
print(len(list(net)))