from ipaddress import *

net = ip_network("192.168.156.235/255.255.255.240", False)
print(net) # 192.168.156.224/28

ip1 = ip_address("192.168.156.235")
ip2 = ip_address("192.168.156.224")
print(int(ip1) - int(ip2))