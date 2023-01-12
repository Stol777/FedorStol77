print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = (y <= z) and not (z and x)
            if F == 1:
                print(x, y, z)

#!!!