from fnmatch import fnmatch


for i in range(0, 10 ** 8):
    if i % 111 == 0:
        if fnmatch(str(i), '*15*7424'):
            print(i, i // 111)
    if i % 113 == 0:
        if fnmatch(str(i), '*15*7424'):
            print(i, i // 113)
    if i % 127 == 0:
        if fnmatch(str(i), '*15*7424'):
            print(i, i // 127)
