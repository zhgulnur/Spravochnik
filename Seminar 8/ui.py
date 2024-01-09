from logger import *

def interface():
    print("Добрый день! Вы попали в специальный бот-справочник. \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных")
    command = int(input("Введите число: "))
    
    while command not in [1, 2, 3, 4]:
        print("Неправильный ввод!")
        command = int(input("Введите число: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        name_or_surname = input("Введите имя или фамилию для изменения: ")
        entry_index = find_entry_by_name_or_surname(name_or_surname, 'data_first_variant.csv')
        if entry_index != -1:
            print("Найден вариант 1:")
            print_data_entry(entry_index, 'data_first_variant.csv')
            update_data(entry_index, 'data_first_variant.csv')
        else:
            entry_index = find_entry_by_name_or_surname(name_or_surname, 'data_second_variant.csv')
            if entry_index != -1:
                print("Найден вариант 2:")
                print_data_entry(entry_index, 'data_second_variant.csv')
                update_data(entry_index, 'data_second_variant.csv')
            else:
                print("Данные не найдены.")
    elif command == 4:
        name_or_surname = input("Введите имя или фамилию для удаления: ")
        entry_index = find_entry_by_name_or_surname(name_or_surname, 'data_first_variant.csv')
        if entry_index != -1:
            delete_data(entry_index, 'data_first_variant.csv')
            print("Данные удалены.")
        else:
            entry_index = find_entry_by_name_or_surname(name_or_surname, 'data_second_variant.csv')
            if entry_index != -1:
                delete_data(entry_index, 'data_second_variant.csv')
                print("Данные удалены.")
            else:
                print("Данные не найдены.")

def print_data_entry(entry_index, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        if file_path == 'data_first_variant.csv':
            print(''.join(data[entry_index:entry_index+4]))
        elif file_path == 'data_second_variant.csv':
            print(''.join(data[entry_index:entry_index+1]))


def update_data(entry_index, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print(f"Текущие данные: {data[entry_index:entry_index+4]}")
    
    if file_path == 'data_second_variant.csv':
        new_data = input(f"Введите новые данные (все в одну строку): ")
    else:
        new_data = ';'.join(input(f"Введите новые данные через точку с запятой (Имя;Фамилия;Телефон;Адрес): ").split(';'))

    updated_data = data.copy()

    for i in range(0, len(data), 4 if file_path == 'data_first_variant.csv' else 1):
        if i == entry_index:
            updated_entry = [f"{new_data}\n"] if file_path == 'data_second_variant.csv' else [f"{value}\n" for value in new_data.split(';')]
            updated_data[i:i+4] = updated_entry

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_data)

    print("Данные обновлены.")


