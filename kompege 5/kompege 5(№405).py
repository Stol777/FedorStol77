for N in range(0, 1000):
    R = bin(N)[2::]
    if N % 2 == 0:
        R += '01'
    else:
        R += '10'
    R = int(R, 2)
    if R > 81:
        print(R)
        break