str = '2' + 81 * '5'
while '25' in str or '4555' in str or '355' in str:
    if '25' in str:
        str = str.replace('25', '4', 1)
    elif '355' in str:
        str = str.replace('355', '2', 1)
    elif '4555' in str:
        str = str.replace('4555', '3', 1)
print(str)
