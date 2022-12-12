f = open('24_505.txt').readline()
length = 1
lst = []
for i in range(1, len(f)):
    if int(f[i - 1]) + int(f[i]) > 10:
        length += 1
    else:
        lst.append(length)
        length = 1
print(max(lst))
