a = "КАРА"
i = len(a)
k = 1
b = "Т"

while i > 1:
    c = a[i - 1]
    b = b + c
    i = i - k

print(b)