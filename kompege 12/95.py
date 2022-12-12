str = 204 * '4'
while '4444' in str or '777' in str:
    if '4444' in str:
        str = str.replace('4444', '77', 1)
    else:
        str = str.replace('777', '4', 1)
print(str)
