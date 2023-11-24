# Задача №49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def new_db():
    file_name = input('Введите название базы данных: ') + '.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write('')
        return file_name

def show_all(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))

def add_new(file_name: str) -> None:
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')

def remove(file_name: str):
    old_data = find_(file_name)
    if old_data == None:
        return
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        # s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        data.remove(old_data)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)

def modify(file_name: str):
    old_data = find_(file_name)
    if old_data == None:
        return
    print('Введите новые данные: ')
    last_name_ = input('Введите фамилию: ')
    first_name_ = input('Введите имя: ')
    patronymic_ = input('Введите отчество: ')
    phone_number_ = input('Введите номер телефона: ')
    data = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)

def find_(file_name: str, flag = True):
    print('Поиск записи')
    variant = input('Введите 1 для поиска по фамилии и 2 для поиска по имени: ')
    opt = 0
    if variant == '1':
        opt = 0
    elif variant == '2':
        opt = 1
    elif variant:
        print('Введено некорректное значeние. Будет произведен поиск по фамилии')
    name_ = input('Введите фамилию/имя для поиска: ')
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == name_, data))
        if data != []:
            print(*(list(zip(range(1, len(data) + 1), data))), sep = '\n')
        else:
            print('Человека с такой фамимлией/именем в базе данных нет')
            return
        if flag:
            id_ = input('Введите номер нужного пользователя: ')
            if int(id_) <= len(data):
                return data[int(id_) - 1]
            print('Введено некорректное значeние.')

def copy_record(file_name: str):
    second_bd = input('Введите новое название базы данных: ') + '.txt'
    old_data = find_(file_name)
    if old_data == None:
        return
    with open(second_bd, 'a', encoding='utf-8') as f:
        f.write(old_data)

def main():
    first_bd = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('=============================')
        print('0 - задать имя базы данных')
        print('1 - показать все записи')
        print('2 - добавить запись')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - найти запись по фамилии/имени')
        print('6 - копировать запись в другую базу данных')
        answer = input('Введите номер операции или х для выхода: ')
        if answer == '0':
            first_bd = new_db()
        elif answer == '1':
            show_all(first_bd)
        elif answer == '2':
            add_new(first_bd)
        elif answer == '3':
            remove(first_bd)
        elif answer == '4':
            modify(first_bd)
        elif answer == '5':
            find_(first_bd, False)
        elif answer == '6':
            copy_record(first_bd)
        elif answer == 'x':
            flag_exit = True

if __name__ == '__main__':
    main()
