s = open('24_223.txt').readline()
# counter = 0
# for i in range(len(s) - 2):
#     str = s[i] + s[i + 1] + s[i + 2]
#     if str == 'TIK' or str == 'TOK':
#         counter += 1
# print(counter)
#
print(s.count('TIK') + s.count('TOK'))
