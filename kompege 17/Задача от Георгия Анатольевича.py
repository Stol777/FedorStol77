ans = []
for i in range(10, 100):
    product = 1
    for item in str(i):
        product *= int(item)
    if i == 2 * product:
        ans.append(i)
print(ans)
