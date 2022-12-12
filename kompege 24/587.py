with open('24_587.txt') as f:
    lst = [item.strip() for item in f]
    counter = 0
    for string in lst:
        counter_A = string.count('A')
        counter_B = string.count('B')
if counter_A / counter_B <= 0.95:
    counter += 1
print(counter)
