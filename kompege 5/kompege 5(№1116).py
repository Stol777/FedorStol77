def res(number):
    null = 0
    one = 0
    for i in range(0, len(number)):
        if number[i] == '0':
            null += 1
        else:
            one += 1
    if null == one:
        number += number[i]
    elif null > one:
        number += '1'
    else:
        number += '0'
    return number


for N in range(100, 2, -1):
    R = bin(N)[2::]
    R = res(R)
    R = res(R)
    R = res(R)
    R = int(R, 2)
    if R % 4 == 0 and R % 8 != 0:
        print(N)
        break
