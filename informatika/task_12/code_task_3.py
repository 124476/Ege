d = set()
for i in range(301, 1000):
    m = i * "5"
    while "5555" in m or "888" in m:
        m = m.replace("5555", "88", 1)
        m = m.replace("888", "5", 1)
    d.add(m)

print(len(d))