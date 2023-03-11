from fnmatch import fnmatch


def sum_of_numbers(integer):
    number = str(integer)
    result = 0
    for item in number:
        result += int(item)
    return result


for i in range(0, 10 ** 10, 2023):
    if fnmatch(str(i), '1?1?1?1*1') and sum_of_numbers(i) == 22:
        print(i)
