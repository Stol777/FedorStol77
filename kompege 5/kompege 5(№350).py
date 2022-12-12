def step(R):
    null = 0
    one = 0
    for item in R:
        if item == '1':
            one += 1
        else:
            null += 1
    if one > null:
        R += '0'
    else:
        R += '11'
    return R


for N in range(0, 1000):
    R = bin(N)[2::]
    R = step(R)
    R = step(R)
    R = int(R, 2)
    if R > 500:
        print(N)
        break
