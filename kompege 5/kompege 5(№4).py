def summ(number):
    summ = 0
    for item in number:
        summ += int(item)
    return summ


for N in range(0, 1001):
    R = bin(N)[2::]
    R += str(summ(R) % 2)
    R += str(summ(R) % 2)
    R = int(R, 2)
    if R > 77:
        print(N)
        break
