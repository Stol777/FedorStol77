s = open('24_279.txt').readline()
counter = 0
for i in range(len(s) - 5):
    item = s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4]
    if item == 'BOSS' and s[i + 5] != 'J' and s[i] != 'J':
        counter += 1
print(counter)
