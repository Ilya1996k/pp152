from ipaddress import *
ip1 = "121.171.5.70"
ip2 = "121.171.5.107"
mn = 10000000
for mask in range(30, 1, -1):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 == net2:
        if ip_address(ip1) in net1.hosts():
            if ip_address(ip2) in net2.hosts():
                print(len(list(net1)))