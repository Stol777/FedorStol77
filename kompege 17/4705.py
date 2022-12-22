with open('17_4705.txt') as f:
    seq = list(map(int, f.readlines()))
    lst = []
    for item in seq:
        if str(item)[-1::] == '3':
            lst.append(item)
    max_elem = max(lst)
    lst = []
    counter = 0
    for i in range(len(seq) - 1):
        if (str(seq[i])[-1::] == '3' and str(seq[i + 1])[-1::] != '3') or (str(seq[i])[-1::] != '3' and str(seq[i + 1])[-1::] == '3'):
            if (seq[i] ** 2) + (seq[i + 1] ** 2) >= max_elem ** 2:
                counter += 1
                lst.append((seq[i] ** 2) + (seq[i + 1] ** 2))
    print(counter, max(lst))
