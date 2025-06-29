from ipaddress import *

for x in range(33):
    net = ip_network(f"241.185.253.57/{x}", False)
    print(net, 32 - x)