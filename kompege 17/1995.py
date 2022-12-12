with open('17_2000.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    max_average = 0
    for i in range(len(seq) - 1):
        if abs(seq[i] + seq[i + 1]) % 2 == 0 and abs(seq[i] + seq[i + 1]) % 10 != 6:
            counter += 1
            if (seq[i] + seq[i + 1]) // 2 > max_average:
                max_average = (seq[i] + seq[i + 1]) // 2
print(counter, max_average)
