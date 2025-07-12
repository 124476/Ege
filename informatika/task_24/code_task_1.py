from re import *

m = open("txt_task_1.txt").readline()

reg = r"[ABEF]+"

d = [x.group() for x in finditer(reg, m)]

print(max([len(x) for x in d]))