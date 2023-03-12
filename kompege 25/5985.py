from fnmatch import fnmatch


def divisors(integer):
    result = []
    for x in range(2, int(integer ** 0.5) + 1):
        if integer % x == 0:
            result.append(x)
            result.append(integer // x)
    result.append(1)
    result.append(integer)
    return sorted(result)


for i in range(0, 10 ** 7, 12):
    list_of_divisors = divisors(i)
    if fnmatch(str(i), '12*348') and len(list_of_divisors) == 12:
        print(i, list_of_divisors[-2])
