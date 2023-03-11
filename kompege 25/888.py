def divisors(integer):
    result = []
    for i in range(1, int(integer ** 0.5) + 1):
        if integer % i == 0:
            lst.append(integer // i)
            lst.append(i)
    return result


for x in range(1000000, 1500001):
    lst = divisors(x)
    result = []
    for y in range(0, len(lst) - 1, 2):
        if lst[y] - lst[y + 1] <= 110:
            result.append(max(lst[y], lst[y + 1]))
    if len(result) >= 3:
        print(x, max(result))
