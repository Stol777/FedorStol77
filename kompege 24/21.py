s = open('24_21.txt').readline()
sub = s[0]
m = 0
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        sub += s[i]
        m = max(m, len(sub))
    else:
        sub = s[i]
print(m)
