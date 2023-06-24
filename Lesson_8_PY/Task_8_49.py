# Задача №49. Решение в группах Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Вариант-1
# def write_contacts(filename):
#     with open(filename, 'a', encoding='UTF-8') as file:
#         file.write('\n' + input(f'Введите имя, фамилию, отчество, номер телефона: '))
#     return file

# def read_contacts(filename):
#     contacts = []
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name' : name,
#                 'surname' : surname,
#                 'patronymic' : patronymic,
#                 'phone' : phone
#             }
#             print(name, surname, patronymic, phone)
#             contacts.append(contact)
#     return contacts

# filename = r'Lesson_8_PY\book_telephone.txt'
# a = int(input('1 - для ввода, 2 - для вывода \n'))
# if a == 1:
#     add_contact = write_contacts(filename)
# elif a == 2:
#     contact=read_contacts(filename)

# else:
#     print('нет такой функции')

# Вариант-2
file_path = 'Lesson_8_PY\book_telephone.txt'
vvod = int(input('Введите команду \n1 - вывод всех данных, \n2 - добавление контакта, \n3 - поиск контакта: \n'))
if vvod ==1:
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())

elif vvod ==3:
    with open(file_path, 'r', encoding='utf-8') as f:
            #   poisk = int(input('Введите фамилию, имя, отчество для поиска'))
            #   for line in f:
            #         if poisk in line: print(line)
        data_tel = f.read()
    data_1 = data_tel.split(',')   
    print(data_1)
        
