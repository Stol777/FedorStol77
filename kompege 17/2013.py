with open('17_2013.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    min_number = 99999
    for i in range(len(seq)):
        if (seq[i] % 10 == 2 or seq[i] % 10 == 7) and seq[i] % 3 == 0 and seq[i] % 11 == 0:
            counter += 1
            if seq[i] < min_number:
                min_number = seq[i]
print(counter, min_number)
