from ipaddress import *
net = ip_network('142.36.195.251/255.255.255.192',0)
for i in net.hosts():
    print(i)