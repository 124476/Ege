from re import *

m = open("txt_task_6.txt").readline()

reg = r"([BCD][AO])+"

print(max([len(x.group()) // 2 for x in finditer(reg, m)]))