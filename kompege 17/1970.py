lst_sum = []
counter = 0
with open('17_1970.txt') as f:
    seq = list(map(int, f.readlines()))
    for i in range(0, len(seq) - 1):
        num_1 = seq[i]
        num_2 = seq[i + 1]
        if num_1 % 3 == 0 or num_2 % 3 == 0:
            counter += 1
            lst_sum.append(num_2 + num_1)
    print(counter, max(lst_sum))
