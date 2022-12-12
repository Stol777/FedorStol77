def e_bit(num):
    count = len(num)
    num = '0' * (8 - count) + num
    return num


def invert(num):
    new_num = ''
    for item in num:
        if item == '0':
            new_num += '1'
        else:
            new_num += '0'
    return new_num


for N in range(0, 128):
    R = bin(N)[2::]
    R = e_bit(R)
    R = invert(R)
    R = int(R, 2) + 1
    if R == 221:
        print(N)
        break
