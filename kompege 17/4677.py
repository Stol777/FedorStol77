with open('17_4677.txt') as f:
    seq = list(map(int, f.readlines()))
    counter_100 = 0
    counter = 0
    lst = []
    for item in seq:
        if item % 100 == 0:
            counter_100 += 1
    for i in range(len(seq) - 1):
        if (seq[i] < 0 or seq[i + 1] < 0) and ((seq[i] + seq[i + 1]) < counter_100):
            counter += 1
            lst.append(seq[i] + seq[i + 1])
    print(counter, abs(max(lst)))
