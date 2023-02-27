deposit = int(input())
percent = int(input())
percent *= 0.01
percent += 1
required_minimum = int(input())
counter = 0
while True:
    if deposit >= required_minimum:
        print(counter)
        break
    deposit *= percent
    deposit = int(deposit // 1)
    counter += 1
