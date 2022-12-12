for i in range(1, 100):
    number = bin(i)[2::]
    if int(number) % 2 == 0:
        number += '01'
    else:
        number += '10'
    if int(number, 2) > 81:
        print(int(number, 2))
        break
