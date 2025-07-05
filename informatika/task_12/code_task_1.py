m = 70 * "8"

while "2222" in m or "8888" in m:
    if "2222" in m: m = m.replace("2222", "88")
    else: m = m.replace("8888", "22")

print(m)