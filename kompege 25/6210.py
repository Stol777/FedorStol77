from fnmatch import fnmatch


def divisors(integer):
    lst = []
    for i in range(1, int(integer ** 0.5) + 1):
        if integer % i == 0:
            lst.append(i)
            lst.append(integer // i)
    return lst


def if_palindrome(number):
    number = str(number)
    if number[::-1] == number:
        return True
    else:
        return False


for x in range(0, 10 ** 7, 53):
    list_of_divisors = divisors(x)
    if fnmatch(str(x), '*2?2*') and if_palindrome(x) and len(list_of_divisors) >= 30:
        print(x, sum(list_of_divisors))
