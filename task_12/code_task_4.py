for i in range(51):
    m = i * "6"

    while "66" in m:
        m = m.replace("66", "1", 1)
        m = m.replace("11", "2", 1)
        m = m.replace("22", "6", 1)

    if m == "21":
        print(i)
