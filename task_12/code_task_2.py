m = ">" + 10 * "1" + 20 * "2" + 30 * "3"

while ">1" in m or ">2" in m or ">3" in m:
    if ">1" in m: m = m.replace(">1", "22>", 1)
    if ">2" in m: m = m.replace(">2", "2>", 1)
    if ">3" in m: m = m.replace(">3", "1>", 1)
print(sum(int(x) for x in m if x != ">"))
