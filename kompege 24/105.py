s = open('24_105.txt').readline()
counter = 1
lst = []
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        counter += 1
    else:
        counter = 1
    lst.append(counter)
print(max(lst))
