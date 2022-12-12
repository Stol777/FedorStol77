with open('17_2001.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    max_sum = 0
    for i in range(len(seq) - 3):
        if ((seq[i] % 2 == 0 and seq[i + 1] % 2 != 0) or (seq[i] % 2 != 0 and seq[i + 1] % 2 == 0)) and ((seq[i + 2] % 2 == 0 \
        and seq[i + 3] % 2 != 0) or (seq[i + 2] % 2 != 0 and seq[i + 3] % 2 == 0)) and ((seq[i + 1] % 2 != 0 and seq[i + 2] == 0) \
        or (seq[i + 1] % 2 == 0 and seq[i + 2] % 2 != 0)):
            counter += 1
            if seq[i] + seq[i + 1] + seq[i + 2] + seq[i + 3] > max_sum:
                max_sum = seq[i] + seq[i + 1] + seq[i + 2] + seq[i + 3]
print(counter, max_sum)
