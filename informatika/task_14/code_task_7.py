a = []

for x in range(1, 51):
    b = bin(x)[2:]
    if b[-3:] == "011":
        a += [x]

print(len(a))