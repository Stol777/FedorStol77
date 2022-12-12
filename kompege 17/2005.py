def base10_to_any_base(base10, n):
    result = ''
    while base10:
        result += str(base10 % n)
        base10 //= n
    return result[::-1]


with open('17_2004.txt') as f:
    seq = list(map(int, f.readlines()))
    counter = 0
    lst = []
    for item in seq:
        if (item % 31 == 0 or item % 47 == 0 or item % 51 == 0) and (base10_to_any_base(item, 3))[-1] == (base10_to_any_base(item, 5))[-1]:
            counter += 1
            lst.append(item)
print(counter, min(lst))
