with open('17_2491.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    lst = []
    average = sum(seq) // len(seq)
    for i in range(len(seq) - 2):
        if ('9' in str(seq[i]) and '9' in str(seq[i + 1]) and '9' in str(seq[i + 2])) and (seq[i] < average or seq[i + 1] < average or seq[i + 2] < average):
            counter += 1
        lst.append(seq[i] + seq[i + 1] + seq[i + 2])
print(counter, max(lst))
