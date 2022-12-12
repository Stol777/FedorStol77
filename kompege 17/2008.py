with open('17_2004.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    min_number = 9999999
    for i in range(len(seq)):
        if seq[i] > 100:
            if (seq[i] % 100) // 10 <= 4 and 3 <= (seq[i] % 1000) // 100 <= 7:
                counter += 1
                if seq[i] < min_number:
                    min_number = seq[i]
print(counter, min_number)
