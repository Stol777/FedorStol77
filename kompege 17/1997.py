with open('17_1997.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    max_sum = 0
    for i in range(len(seq) - 1):
        EvenOddNumber = None
        if seq[i] % 2 == 0 and seq[i + 1] % 2 == 1:
            EvenOddNumber = True
        elif seq[i] % 2 == 1 and seq[i + 1] % 2 == 0:
            EvenOddNumber = False
        if EvenOddNumber == True:
            if seq[i] % 4 == 0 and seq[i + 1] % 11 == 0:
                counter += 1
            if seq[i] + seq[i + 1] > max_sum:
                max_sum = seq[i] + seq[i + 1]
        elif EvenOddNumber == False:
            if seq[i] % 11 == 0 and seq[i + 1] % 4 == 0:
                counter += 1
            if seq[i] + seq[i + 1] > max_sum:
                max_sum = seq[i] + seq[i + 1]
print(counter, max_sum)
