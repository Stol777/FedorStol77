def add_task():
    todo_list.append(input('Введите задачу, которую хотите добавить: '))
    return print('Задача успешно добавлена\n')


def remove_task():
    index = int(input('Введите номер задачи, которую хотите удалить: '))
    index -= 1
    todo_list.pop(index)
    return print('Задача успешно удалена\n')


def show_todo_list():
    for index, item in enumerate(todo_list):
        print(f'{index + 1}: {item}', end='')
    print()


with open('todo_list', mode='a') as f:
    todo_list = list(f.readlines())
    while True:
        number = int(input("""Список задач:\n 1.Показать список дел\n 2.Добавить задачу\n 3.Удалить задачу\n 4.Завершить работу программы\n"""))
        if number == 4:
            print('Успешно')
            break
        elif number == 3:
            remove_task()
        elif number == 2:
            add_task()
        elif number == 1:
            show_todo_list()
        else:
            print('Введите корректное число')
