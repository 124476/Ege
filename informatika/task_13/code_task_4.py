from ipaddress import *

for x in range(33):
    net = ip_network(f"148.195.140.28/{x}", False)
    print(net)