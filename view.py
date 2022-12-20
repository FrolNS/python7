def contact_to_s():
    return input('Введите имя: ')


def choose_mode():
    return input('Введите режим: 1 - добавление, 2 - поиск. Для выхода введите 3. \n')


def new_contact():
    name = input('Введите имя: ')
    p_number = input('Введите номер телефона: ')
    return f'{name} || {p_number}'


def show_found(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)