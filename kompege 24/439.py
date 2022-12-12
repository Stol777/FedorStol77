f = open('24_439.txt').readline()
length = 1
for i in range(1, len(f)):
    if f[i] > f[i - 1]:
        length += 1
    else:
        length = 1
