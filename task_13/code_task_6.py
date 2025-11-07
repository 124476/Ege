from ipaddress import *

for x in range(33):
    net1 = ip_network(f"112.117.107.70/{x}", False)
    net2 = ip_network(f"112.117.121.80/{x}", False)
    if net1 == net2:
        print(net1.netmask)