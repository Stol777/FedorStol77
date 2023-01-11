from fnmatch import fnmatch


def base10_to_any_base(base10, n):
    result = ''
    while base10:
        result += str(base10 % n)
        base10 //= n
    return result[::-1]


for i in range(0, 10 ** 9, 333):
    if fnmatch(str(base10_to_any_base(i, 7)), '?213*5664'):
        print(i, i // 333)
