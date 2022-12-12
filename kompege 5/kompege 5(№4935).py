def p(x):
    sum = 0
    for item in x:
        sum += int(item)
    if sum % 2 == 0:
        x = '10' + x
        x = x[0:len(x)-2:] + '00'
    else:
        x = '11' + x
        x = x[0:len(x)-2:] + '11'
    return x


lst = []
for n in range(1, 30):
    r = bin(n)[2::]
    r = p(r)
    lst.append(int(r, 2))
print(max(lst))


