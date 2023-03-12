def divisors(integer):
    result = []
    for x in range(2, int(integer ** 0.5) + 1):
        if integer % x == 0:
            result.append(x)
            result.append(integer // x)
    return result


for i in range(500000, 10 ** 6):
    lst = divisors(i)
    list_of_divisors = [item for item in lst if item % 10 == 8 and item != 8 and item != i]
    if len(list_of_divisors) > 0:
        print(i, min(list_of_divisors))
