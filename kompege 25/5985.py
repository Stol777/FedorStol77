from fnmatch import fnmatch


def if_tw_divisors(integer):
    result = 0
    for x in range(1, integer + 1):
        if integer % x == 0:
            result += 1
    if result == 12:
        return True
    else:
        return False


for i in range(0, 10 ** 7, 12):
    if fnmatch(str(i), '12*348') and if_tw_divisors(i):
        print(i, 'Надо дорешать')
