from re import *

m = open("txt_task_5.txt").readline()

reg = r"(NPO|PNO)+"

print(max([len(x.group()) // 3 for x in finditer(reg, m)]))
