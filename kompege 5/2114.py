def step_2(num):
    if int(num) % 2 == 0:
        num = '11' + num + '11'
    else:
        num = '1' + num + '0'
    return num


lst = []
for n in range(0, 1000):
    r = bin(n)[2::]
    r = step_2(r)
    r = int(r, 2)
    if r < 126:
        lst.append(r)
print(max(lst))
