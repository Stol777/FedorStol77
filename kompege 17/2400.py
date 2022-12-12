with open('17_2400.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    lst = []
    for i in range(len(seq) - 1):
        if seq[i] + seq[i + 1] > 100 and (seq[i] < 0 or seq[i + 1] < 0):
            counter += 1
            lst.append(seq[i] * seq[i + 1])
print(counter, max(lst))
