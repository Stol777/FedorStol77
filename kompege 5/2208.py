def step_1(num):
    new_num = str(num)
    result = 1
    for item in new_num:
        result *= int(item)
    return result


lst = []
for n in range(0, 1000):
    r = step_1(n)
    r = bin(r)[2::]
    r += '00'
    r = int(r, 2)
    if r == 864:
        lst.append(n)
for num in lst:
    if str(num)[0] == str(num)[1] == str(num)[2]:
        print(num)
