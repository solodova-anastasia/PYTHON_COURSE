# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.

# Показывает информацию в файле
def show_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Записывает информацию в файл
def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {fio} | {phone_number}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_number}\n")

# Изменяет информацию из файла
def edit_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    my_choice = -1
    file_tel = "Lesson_8_PY\book_telephone.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экпорт данных")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()




#Другое решение
# def choose_action(phonebook):
#     while True:
#         print('Что вы хотите сделать?')
#         user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
# 4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
#         print()
#         if user_choice == '1':
#             file_to_add = input('Введите название импортируемого файла: ')
#             import_data(file_to_add, phonebook)
#         elif user_choice == '2':
#             contact_list = read_file_to_dict(phonebook)
#             find_number(contact_list)
#         elif user_choice == '3':
#             add_phone_number(phonebook)
#         elif user_choice == '4':
#             change_phone_number(phonebook)
#         elif user_choice == '5':
#             delete_contact(phonebook)
#         elif user_choice == '6':
#             show_phonebook(phonebook)
#         elif user_choice == '0':
#             print('До свидания!')
#             break
#         else:
#             print('Неправильно выбрана команда!')
#             print()
#             continue


# def import_data(file_to_add, phonebook):
#     try:
#         with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
#             contacts_to_add = new_contacts.readlines()
#             file.writelines(contacts_to_add)
#     except FileNotFoundError:
#         print(f'{file_to_add} не найден')


# def read_file_to_dict(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     headers = ['Фамилия', 'Имя', 'Номер телефона']
#     contact_list = []
#     for line in lines:
#         line = line.strip().split()
#         contact_list.append(dict(zip(headers, line)))
#     return contact_list


# def read_file_to_list(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         contact_list = []
#         for line in file.readlines():
#             contact_list.append(line.split())
#     return contact_list


# def search_parameters():
#     print('По какому полю выполнить поиск?')
#     search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
#     print()
#     search_value = None
#     if search_field == '1':
#         search_value = input('Введите фамилию для поиска: ')
#         print()
#     elif search_field == '2':
#         search_value = input('Введите имя для поиска: ')
#         print()
#     elif search_field == '3':
#         search_value = input('Введите номер для поиска: ')
#         print()
#     return search_field, search_value


# def find_number(contact_list):
#     search_field, search_value = search_parameters()
#     search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
#     found_contacts = []
#     for contact in contact_list:
#         if contact[search_value_dict[search_field]] == search_value:
#             found_contacts.append(contact)
#     if len(found_contacts) == 0:
#         print('Контакт не найден!')
#     else:
#         print_contacts(found_contacts)
#     print()


# def get_new_number():
#     last_name = input('Введите фамилию: ')
#     first_name = input('Введите имя: ')
#     phone_number = input('Введите номер телефона: ')
#     return last_name, first_name, phone_number


# def add_phone_number(file_name):
#     info = ' '.join(get_new_number())
#     with open(file_name, 'a', encoding='utf-8') as file:
#         file.write(f'{info}\n')


# def show_phonebook(file_name):
#     list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
#     print_contacts(list_of_contacts)
#     print()
#     return list_of_contacts


# def search_to_modify(contact_list: list):
#     search_field, search_value = search_parameters()
#     search_result = []
#     for contact in contact_list:
#         if contact[int(search_field) - 1] == search_value:
#             search_result.append(contact)
#     if len(search_result) == 1:
#         return search_result[0]
#     elif len(search_result) > 1:
#         print('Найдено несколько контактов')
#         for i in range(len(search_result)):
#             print(f'{i + 1} - {search_result[i]}')
#         num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
#         return search_result[num_count - 1]
#     else:
#         print('Контакт не найден')
#     print()


# def change_phone_number(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     print('Какое поле вы хотите изменить?')
#     field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
#     if field == '1':
#         number_to_change[0] = input('Введите фамилию: ')
#     elif field == '2':
#         number_to_change[1] = input('Введите имя: ')
#     elif field == '3':
#         number_to_change[2] = input('Введите номер телефона: ')
#     contact_list.append(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)


# def delete_contact(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)


# def print_contacts(contact_list: list):
#     for contact in contact_list:
#         for key, value in contact.items():
#             print(f'{key}: {value:12}', end='')
#         print()


# if __name__ == '__main__':
#     file = 'Lesson_8_PY\Phonebook.txt'
#     choose_action(file)