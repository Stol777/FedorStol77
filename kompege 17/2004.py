with open('17_2004.txt') as f:
    seq = list(map(int, f.readlines()))
    summ = 0
    max_number = 0
    for i in range(len(seq)):
        if seq[i] % 13 == 4 and seq[i] % 8 == 1:
            summ += seq[i]
            if seq[i] > max_number:
                max_number = seq[i]
print(max_number, summ)
