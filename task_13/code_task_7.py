from ipaddress import *

for x in range(33):
    net1 = ip_network(f"157.127.182.76/{x}", False)
    net2 = ip_network(f"157.127.190.80/{x}", False)
    if net1 != net2:
        print(net1)