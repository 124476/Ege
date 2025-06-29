print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not(x == (w and z)) and (y == (x and not w))
                if f == 1:
                    print(x, y, w, z)