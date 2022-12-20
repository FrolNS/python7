def add_new(contact):
    try:
        with open('database.txt', 'a', encoding='utf-8') as db:
            db.write(f'\n{contact}')
    except FileNotFoundError:
        with open('database.txt', 'w', encoding='utf-8') as db:
            db.write(f'\n{contact}')


def get_base():
    with open('database.txt', 'r', encoding='utf-8') as db:
        return db.read()
