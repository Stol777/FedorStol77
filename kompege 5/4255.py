def step_2(num):
    sum = 0
    for item in num:
        sum += int(item)
    num += str(sum % 2)
    return num


for n in range(0, 1000):
    r = bin(n)[2::]
    r = step_2(r)
    r = step_2(r)
    r = int(r, 2)
    if r > 452:
        print(r)
        break
