def list_of_divisors(integer):
    lst = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            lst.append(i)
    return lst


def condition(integer):
    counter = 0
    lst = []
    for item in list_of_divisors(integer):
        if item in max_divisors_numbers_list:
            lst.append(item)
    if len(lst) >= 3:
        return True
    else:
        return False


def finding_common_divisors(number_1, number_2):
    lst = []
    number_1 = list_of_divisors(number_1)
    number_2 = list_of_divisors(number_2)
    for item in number_1:
        if item in number_2:
            lst.append(item)
    return lst


with open('17_4329.txt') as f:
    seq = list(map(int, f.readlines()))
    result = []
    max_divisors_number = max([len(list_of_divisors(item)) for item in seq])
    for item in seq:
        if len(list_of_divisors(item)) == max_divisors_number:
            max_divisors_numbers_list = list_of_divisors(item)
    for i in range(len(seq) - 1):
        if condition(seq[i]) is True and condition(seq[i + 1]) is True:
            result.append(len(finding_common_divisors(seq[i], seq[i + 1])))
    print(len(result), max(result))
