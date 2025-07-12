from re import *

m = open("txt_task_14.txt").readline()

num = r"([1-5][0-5]*|0)"
hnum = rf"({num}((\+|\*){num})*)"
reg = rf"(?=({hnum}))"

print([x.group(1) for x in finditer(reg, m)])
print(max([len(x.group(1)) for x in finditer(reg, m)]))
