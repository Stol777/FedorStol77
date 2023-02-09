def sum_numbers(string):
    sum = 0
    for item in string:
        sum += int(item)
    return sum


lst = []
for n in range(100):
    r = bin(n)[2::]
    if sum_numbers(r) % 2 == 0:
        r = '1' + r[2::] + '0'
    else:
        r = '11' + r[2::] + '1'
    r = int(r, 2)
    if r == 50:
        print(n)
