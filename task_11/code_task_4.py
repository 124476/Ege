from math import *

# Первый вариант
kod = 26 * 2
char = ceil(log2(kod))
pas = ceil(char * 7 / 8)
user = pas + 12
mx = 2 * 1024
print(mx // user)

# Второй вариант
kod = 26 * 2
char = ceil(log2(kod))
pas = ceil(char * 7 / 8)
user = pas + 12
for k in range(2, 1000):
    if k * user <= 2 * 1024:
        print(k)
