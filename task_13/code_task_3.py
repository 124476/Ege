from ipaddress import *

for x in range(33):
    net = ip_network(f"220.128.112.142/{x}", False)
    print(net, net.netmask)