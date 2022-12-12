with open('17_2004.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    sum_numbers = []
    for i in range(len(seq)):
        if seq[i] % 3 == 0 and seq[i] % 9 != 0 and seq[i] % 10 >= 4:
            counter += 1
            sum_numbers.append(seq[i])
print(counter, sum(sum_numbers) // counter)
