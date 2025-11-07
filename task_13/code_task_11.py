from ipaddress import *

ip = ip_address("238.237.149.255")

for x in range(31):
    net = ip_network(f"238.237.149.255/{x}", False)
    if net[0] < ip < net[-1]:
        print(x, net)
