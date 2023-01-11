from fnmatch import fnmatch


def sum_left_side(number):
    length = len(str(number))
    summa = 0
    for a in range(0, length // 2):
        summa += int(str(number)[a])
    return summa


def sum_right_side(number):
    length = len((str(number)))
    summa = 0
    for b in range(length // 2, length):
        summa += int(str(number)[b])
    return summa


for i in range(0, 10 ** 13, 519):
    if fnmatch(str(i), '32*54?123'):
        if str(i).find('0') == -1 and len(str(i)) % 2 == 0 and sum_right_side(i) == sum_left_side(i):
            print(i, i // 519)
#321525543123 619509717
