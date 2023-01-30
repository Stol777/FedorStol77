print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                F = d and ((a or not c) <= (a and b and not c))
                if F == 1:
                    print(a, b, c, d)
