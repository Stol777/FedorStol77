def duble(number):
    a = str(number)
    l = len(a)
    a += a[l - 1]
    return a


for N in range(1000, 0, -1):
    N = bin(N)[2::]
    N = duble(N)
    N = int(N, 2)
    if N < 344:
        print(N)
        break
