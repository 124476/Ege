d = {"0": 0}
data = []
for s in open("txt_task_1.txt"):
    data.append(s.replace(";", "").split())

while len(d) != len(data) + 1:
    for s in data:
        if all([x in d for x in s[2:]]):
            d[s[0]] = int(s[1]) + max([d[x] for x in s[2:]])

print(max(d.values()))
