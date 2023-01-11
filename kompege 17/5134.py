with open('17_5134.txt') as f:
    seq = list(map(int, f.readlines()))
    lst = []
    for item in seq:
        if str(item)[-2::] == '10':
            lst.append(item)
    max_element = max(lst)
    lst = []
    counter = 0
    for i in range(len(seq) - 1):
        if (seq[i] % 2023) * (seq[i + 1] % 2023) >= max_element:
            counter += 1
            lst.append(seq[i] + seq[i + 1])
