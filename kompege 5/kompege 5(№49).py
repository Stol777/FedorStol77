def summ(number):
    summ = 0
    for item in number:
        summ += int(item)
    return summ


for i in range(0, 1001):
    R = bin(i)[2::]
    R += str(summ(R) % 2)
    R += str(summ(R) % 2)
    R_10 = int(R, 2)
    if R_10 > 80:
        print(R_10)
        break
