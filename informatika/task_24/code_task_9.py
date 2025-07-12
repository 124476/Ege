from re import *

m = open("txt_task_9.txt").readline()

num = r"(A.A|C.C)+"
reg = rf"(?=({num}))"

print([x.group(1) for x in finditer(reg, m)])
print(max([len(x.group(1)) // 3 for x in finditer(reg, m)]))
