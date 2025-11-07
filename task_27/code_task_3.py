points = []
for i in open("txt_task_3_b.txt"):
    x, y = [float(k) for k in i.replace(",", ".").split()]
    points += [[x, y]]

classers = [[], [], []]
for x, y in points:
    if x > 3:
        classers[0] += [[x, y]]
    elif y >= -2.5:
        classers[1] += [[x, y]]
    else:
        classers[2] += [[x, y]]


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return max(abs(x2 - x1), abs(y2 - y1))


def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p1, p) for p1 in cl)
        m += [[sm, p]]
    return min(m)[1]


centers = [center(cl) for cl in classers]

print(sum([p[0] for p in centers]) / len(centers) * 10000, end=' ')
print(sum([p[1] for p in centers]) / len(centers) * 10000)
