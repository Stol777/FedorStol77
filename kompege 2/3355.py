print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (y or x) == ((y <= w) or not z)
                if F == 0:
                    print(w, x, y, z)
#!!!
