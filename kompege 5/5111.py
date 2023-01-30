def sum_of_number(string):
    sum = 0
    for item in string:
        sum += int(item)
    return sum


for n in range(1000):
    r = bin(n)[2::]
    if sum_of_number(r) % 2 == 0:
        r += '1'
        r = '10' + r[2::]
    else:
        r += '11'
        r = '1' + r[2::]
    r = int(r, 2)
    if r >= 100:
        print(n)
        break
