def f(n):
    m = str(n)

    q = set()
    for i in range(len(m)):
        for j in range(len(m)):
            if i == j or m[i] == "0": continue

            q.add(int(m[i] + m[j]))

    return max(q) - min(q)


d = []
for i in range(100, 1000):
    r = f(i)

    if r == 35:
        d += [i]

print(len(d))
