from re import *

m = open("txt_task_10.txt").readline()

num = r"[^D]*D{0,1}[^D]*D{0,1}[^D]*"

reg = rf"(?=({num}))"

print([x.group(1) for x in finditer(reg, m)])
print(max([len(x.group(1)) for x in finditer(reg, m)]))
