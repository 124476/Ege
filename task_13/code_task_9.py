from ipaddress import *

net = ip_network("184.178.54.144/255.255.255.240")
sm = 0

for ip in net:
    m = f"{ip:b}"
    if "111" in m:
        sm += 1

print(sm)