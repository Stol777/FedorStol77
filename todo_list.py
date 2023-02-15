def sort_by_time():
    pass


def show_list():
    sort_by_time()
    if len(todo_list) == 0:
        print('Список задач пуст')
    else:
        for index, item in enumerate(todo_list):
            print(f'{index + 1}: {item}')
    return print()


def add_task():
    obj = input('Введите задачу, которую хотите добавить (добавить время через "__"):(0 для отмены) ')
    if obj == '0':
        pass
    else:
        lst = obj.split('__')
        if len(lst) == 1:
            todo_list.append(obj)
        else:
            obj = f'[{lst[1]}] {lst[0]}'
            todo_list.append(obj)
        print('Yспешно\n')


def remove_task():
    try:
        index = int(input('Введите номер задачи, которую хотите удалить:(0 для отмены) '))
        if index == 0:
            pass
        else:
            index -= 1
            todo_list.pop(index)
            print('Yспешно\n')
    except IndexError:
        print('Не найдено доступных для удаления элементов\n')
        remove_task()


todo_list = ['Сделать ДЗ', 'Поесть', 'Лечь спать']
print("""Возможные действия:\n 1: Показать список задач\n 2: Добавить задачу\n 3: Удалить задачу\n 4: Завершить работу\n""")
while True:
    try:
        number = int(input('Введите номер действия: \n'))
        if number == 1:
            show_list()
        elif number == 2:
            add_task()
        elif number == 3:
            remove_task()
        elif number == 4:
            with open('todo_list.txt', 'a') as f:
                f.seek(0)
                f.truncate()
                for string in todo_list:
                    f.write(string + '\n')
            print('Yспешно')
            break
        else:
            print('Значения нет в списке доступных действий')
    except ValueError:
        print('Введите корректное значение(цифру/число)')
