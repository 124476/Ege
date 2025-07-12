from re import *

m = open("txt_task_3.txt").readline()

reg = r"[0-9]+"

print(max([len(x.group()) for x in finditer(reg, m)]))