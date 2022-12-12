def step_2(num):
    counter = 0
    new_num = ''
    for item in num:
        if item == '0' and counter == 0:
            new_num += num[0:2:]
            counter += 1
    else:
        new_num += item
    return new_num


lst = []
for n in range(0, 1000):
    r = bin(n)[2::]
    r = step_2(r)
    r = r[::-1]
    r = int(r, 2)
    if r == 119:
        print(n)

