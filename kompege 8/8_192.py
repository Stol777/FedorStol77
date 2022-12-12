counter = 0
string = 'абвгдя'
for a in string:
    for b in string:
        for c in string:
            for d in string:
                for e in string:
                    n_string = a + b + c + d + e
                    if n_string.count('я') == 3:
                        counter += 1
print(counter)
