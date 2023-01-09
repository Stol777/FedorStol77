from fnmatch import fnmatch


def max_divisor(integer):
    lst = []
    for i in range(1, integer):
        if integer % i == 0:
            lst.append(i)
    return max(lst)


def if_odd_number_of_divisors(integer):
    counter = 0
    for i in range(2, integer):
        if integer % i == 0:
            counter += 1
    if counter % 2 == 0:
        return 0
    else:
        return 1


for i in range(10 ** 7):
    if fnmatch(str(i), '3*52?'):
        if if_odd_number_of_divisors(i) == 1:
            print(i, max_divisor(i))
