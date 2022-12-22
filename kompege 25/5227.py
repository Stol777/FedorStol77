def counter_of_divisors(integer):
    counter = 0
    lst = []
    for divisor in range(1, integer + 1):
        if integer % divisor == 0:
            counter += 1
            lst.append(divisor)
    return counter


def max_divisor(integer):
    lst = []
    for divisor in range(1, integer):
        if integer % divisor == 0:
            lst.append(divisor)
    return max(lst)


for x in ' 0123456789':
    for y in '0123456789':
        if x == ' ':
            string = f'1234{y}5'
        else:
            string = f'123{x}4{y}5'
        for z in ' 0123456789':
            if z == ' ':
                string_2 = '352'
            else:
                string_2 = f'3{z}52'
                if counter_of_divisors(int(string)) == counter_of_divisors(int(string_2)):
                    print(f'{string}      {max_divisor(int(string))}')
