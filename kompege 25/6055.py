from fnmatch import fnmatch


for i in range(0, 10 ** 7, 159):
    if fnmatch(str(i), '2?1*67'):
        print(i, i // 159)
