from itertools import permutations
a = '.33'
b = '3.232'
v = '3.20'
g = '23'
counter = -1
lst = [a, b, v, g]
answer_lst = [*(permutations(['a', 'b', 'v', 'g'], 4))]
for item in list(permutations(lst, 4)):
    counter += 1
    access = True
    IP = ''
    for x in item:
        IP += x
    lst = IP.split('.')
    for y in lst:
        if y != '':
            if int(y) > 255 or len(y) > 3 or y == '':
                access = False
    if access is True:
        print(IP)
        print(*answer_lst[counter])
