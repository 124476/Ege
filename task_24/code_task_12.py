from re import *

m = open("txt_task_12.txt").readline()

num = r"[1-9][0-9]{3}\.[0-9]{0,}[1-9]"
hnum = rf"{num}&{num}"
reg = rf"(?=({hnum}))"

print([x.group(1) for x in finditer(reg, m)])
print(max([len(x.group(1)) for x in finditer(reg, m)]))