counter = 0
str = 'еийкнот'
n_str = ''
for a in str:
    for b in str:
        for c in str:
            for d in str:
                for e in str:
                    for f in str:
                        for g in str:
                            n_str = n_str + a + b + c + d + e + f + g
                        if n_str.find('кот') != -1:
                            print(n_str)
                            counter += 1
print(counter)
