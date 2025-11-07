from math import *

kod = 10 + 52 + 1988
char = ceil(log2(kod))

for k in range(2, 1000):
    if ceil(k * char / 8) * 1974 <= 579 * 1024:
        print(k)