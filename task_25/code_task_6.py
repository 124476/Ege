# Первый вариант
from fnmatch import *

for x in range(0, 10 ** 9, 17):
    if fnmatch(str(x), "23?456?89"):
        print(x, x // 17)

# Второй вариант
for c1 in range(0, 10):
    for c2 in range(0, 10):
        x = int(f"23{c1}456{c2}89")
        if x % 17 == 0:
            print(x, x // 17)
