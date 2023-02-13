from random import randint
Hidden_number = 1000
counter = 0
while True:
    try:
        counter += 1
        number_2 = int(input('Введите число: '))
        if number_2 < Hidden_number:
            print('Больше')
        elif number_2 > Hidden_number:
            print('Меньше')
        elif number_2 == Hidden_number:
            print(f'Вы отгадали число {Hidden_number}, используя {counter} попыток(-ки)')
            break
    except ValueError:
        print('Было передано не число')
