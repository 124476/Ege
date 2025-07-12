from re import *

m = open("txt_task_15.txt").readline()

num = r"([1-9][0-9]*[05]{1,}|0|5)"
hnum = rf"{num}([\+|\*]{num})+"
reg = rf"(?=({hnum}))"

print([x.group(1) for x in finditer(reg, m)])
print(max([len(x.group(1)) for x in finditer(reg, m)]))