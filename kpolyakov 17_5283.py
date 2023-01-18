with open('17-335.txt') as f:
    seq = list(map(int, f.readlines()))
    M = min([item for item in seq if item % 43 == 0])
    counter = 0
    maxi = 0
    for i in range(len(seq) - 1):
        if (seq[i] + seq[i + 1] % M == 0) or (seq[i] % 10 == M % 10) or (seq[i + 1] % 10 == M % 10):
            counter += 1
            maxi = max(maxi, seq[i], seq[i + 1])
    print(counter, maxi)
