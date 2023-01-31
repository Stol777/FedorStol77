with open('17_3370.txt') as f:
    seq = list(map(int, f.readlines()))
    max_number = sum([int(str(abs(item))[0]) for item in seq])
    result = []
    for i in range(len(seq) - 1):
        if seq[i] * seq[i + 1] >= max_number:
            result.append(seq[i] + seq[i + 1])
    print(len(result), max(result))
