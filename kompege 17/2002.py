with open('17_2001.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    min_sum = 9999999
    for i in range(len(seq) - 3):
        if seq[i] > seq[i + 1] > seq[i + 2] > seq[i + 3] and seq[i] - seq[i + 3] > 1000:
            counter += 1
            if seq[i] + seq[i + 1] + seq[i + 2] + seq[i + 3] < min_sum:
                min_sum = seq[i] + seq[i + 1] + seq[i + 2] + seq[i + 3]
print(counter, min_sum)
