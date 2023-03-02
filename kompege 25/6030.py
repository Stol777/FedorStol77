from fnmatch import fnmatch


for i in range(0, 10 ** 8, 129):
    if fnmatch(str(i), '12?3*46'):
        print(i, i // 129)
