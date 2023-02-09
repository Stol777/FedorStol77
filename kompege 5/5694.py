m = 278
m = bin(m)[2::]
answer = ''
for n in range(1, 100000000):
    n = bin(n)[2::]
    if len(n) == 9:
        pass
    else:
        while len(n) < 9:
            n += '0'
    # for item in m:
    #     for item_2 in n:
    #         answer += str(max(int(item), int(item_2)))
    #     if answer.count('1') == 7:
    #         print(n)
