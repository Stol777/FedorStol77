def sum_of_numbers(string):
    sum = 0
    for item in string:
        sum += int(item)
    return sum


with open('17_3370.txt') as f:
    seq = list(map(int, f.readlines()))
    result = []
    for i in range(1, len(seq) - 1):
        if sum_of_numbers(str(abs(seq[i - 1]))) == sum_of_numbers(str(abs(seq[i + 1]))):
            result.append(sum_of_numbers(str(seq[i])))
    print(len(result), 'самую часто встречающуюся сумму разрядов среди найденных чисел')
