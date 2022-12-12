def p(x):
    sum = 0
    for item in x:
        sum += int(item)
    x += str(sum % 2)
    return x


counter = 0
for n in range(1000):
    r = bin(n)[2::]
    r = p(r)
    r = p(r)
    r = int(r, 2)
    if 20 <= r <= 50:
        counter += 1
print(counter)
