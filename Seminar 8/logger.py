from data_create import *

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n\n"
                    f"Вариант 1: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"Вариант 2: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input("Введите число: "))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные из 1-го файда. \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        for i in range(0, len(data_first), 4):
            for line in data_first[i:i+4]:
                print(line.strip())
    
    print("Вывожу данные из 2-го файда. \n")
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        for line in data_second:
            print(line.strip())

def find_entry_by_name_or_surname(name_or_surname, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in range(0, len(data), 4 if file_path == 'data_first_variant.csv' else 1):
            if i < len(data):
                if name_or_surname.lower() in data[i].lower() or (file_path == 'data_first_variant.csv' and i+1 < len(data) and name_or_surname.lower() in data[i+1].lower()):
                    return i
        return -1

def delete_data(entry_index, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(data[:entry_index] + data[entry_index+4:])
    print("Данные удалены.")
