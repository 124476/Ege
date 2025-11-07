from ipaddress import *

sm = 0

for A in range(0, 256):
    ip = ip_address(f"207.0.{A}.167")
    net = ip_network(f"{ip}/255.255.255.192", False)
    if all(f"{ip:b}"[:16].count("0") > f"{ip:b}"[16:].count("0") for ip in net)\
            and net[0] < ip < net[-1]:
        sm += 1

print(sm)