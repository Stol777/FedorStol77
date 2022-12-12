with open('17_2000.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    min_diff = 9999999
    for i in range(len(seq) - 2):
        if seq[i] < seq[i + 1] < seq[i + 2]:
            counter += 1
            if seq[i + 2] - seq[i] < min_diff:
                min_diff = seq[i + 2] - seq[i]
print(counter, min_diff)
