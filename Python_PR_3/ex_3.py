import os


def read_file(path):
    with open(path, 'r') as myfile:
        for i in myfile:
            print(i, end='')
        print()


def append_file(path):
    read_file(path)

    with open(path, 'a') as myfile:
        print('Для выхода пропишите "quit"')
        while True:
            text = input('Введите информацию: ')
            if text != 'quit':
                text = text + '\n'
                myfile.write(text)
            else:
                break


def create_file(path):
    with open(path, 'w') as myfile:
        print('Для выхода пропишите "quit"')
        while True:
            text = input('Введите информацию: ')
            if text != 'quit':
                text = text + '\n'
                myfile.write(text)
            else:
                break


while True:
    print('Впишите путь до файла')
    print('Для выхода из программы пропишите "quit"')
    path = input('Путь: ')

    if path == 'quit':
        break

    if os.path.exists(path):
        print('Файл найден, что бы вы хотели с ним сделать?')
        print('"1" - создать новый файл')
        print('"2" - дописать информацию в файл')
        print('"3" - вывести информацию из файла')
        command = input('Впишите символ: ')

        if command == '1':
            create_file(path)
        elif command == '2':
            append_file(path)
        elif command == '3':
            read_file(path)
        else:
            print('Команда не распознана')
    else:
        print('По этому пути файл не найден, хотите его создать?')
        command = input('"Да" - создать файл, "Нет" - ввести путь снова: ')
        if command == 'Да':
            os.makedirs(path[:path.rfind('/')])
            create_file(path)
        elif command == 'Нет':
            continue
