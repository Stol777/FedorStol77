def divisors(integer):
    result = []
    for x in range(2, int(integer ** 0.5) + 1):
        if integer % x == 0:
            result.append(x)
            result.append(integer // x)
    return sorted(result)


for i in range(100806, 100951):
    list_of_divisors = divisors(i)
    if len(list_of_divisors) == 4:
        print(list_of_divisors[-2], end=' ')
        print(list_of_divisors[-1])
