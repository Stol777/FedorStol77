str = 70 * '8'
while '2222' in str or '8888' in str:
    if '2222' in str:
        str = str.replace('2222', '88', 1)
    else:
        str = str.replace('8888', '22', 1)
print(str)
