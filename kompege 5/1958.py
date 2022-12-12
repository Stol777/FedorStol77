def step_2(num):
    summ = 0
    for item in num:
        summ += int(item)
    num += str(summ % 2)
    return num


for n in range(0, 1000):
    r = bin(n)[2::]
    r = step_2(r)
    r = step_2(r)
    r = int(r, 2)
    if r > 77:
        print(n)
        break
