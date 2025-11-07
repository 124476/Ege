from re import finditer

m = open("txt_task_11.txt").readline()

num = r"(YZ|Z){0,1}(XYZ){0,}(XY|X){0,1}"
reg = rf"(?=({num}))"

print([x.group(1) for x in finditer(reg, m[:100])])
print(max(len(x.group(1)) for x in finditer(reg, m)))
