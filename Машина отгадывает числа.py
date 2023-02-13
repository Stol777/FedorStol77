from random import randint


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


print(BinarySearch([i for i in range(0, 101)], randint(1, 100)))
