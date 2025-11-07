from re import finditer

m = open("txt_task_8.txt").readline()

num = r"(BB|DD)+"
reg = rf"(?=({num}))"

print(max([len(x.group(1)) // 2 for x in finditer(reg, m)]))