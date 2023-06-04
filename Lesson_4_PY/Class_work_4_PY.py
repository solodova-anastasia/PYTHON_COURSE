# Задача №25. Решение в группах 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# input_ = 'a a a b c a a d c d d'.split() # После сплита это будет список
# dict_count = {}
# for let in input_:
#     if let in dict_count:   #если let находится в dict_count
#         print(f'{let}_{dict_count[let]}', end=' ')
#         dict_count[let] += 1
#     else:                   #иначе, если букву заводим 1й раз, создаём ей счётчик
#         print(let, end=' ')
#     dict_count[let] = 1

# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore 
# I'm sure that the shells are sea shore shells
# Output: 13

# arr = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore 
# I'm sure that the shells are sea shore shells""".lower().split()
# print(len(set(arr)))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет 
# меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

# 1й вариант решения:
# chislo = 0
# while True:
#     num = int(input())
#     if num > 0:
#         if chislo < num:
#             chislo = num
#     else:
#         break
# print(chislo)

# 2й вариант решения
# count_numbers = 1
# number_ = int(input(f'Введите число {count_numbers}: '))
# maximum_ = number_
# while number_ != 0:
#     count_numbers += 1
#     number_ = int(input(f'Введите число {count_numbers}: '))
#     if number_ > maximum_:
#         maximum_ = number_
# print(f'Наибольший элемент последовательности: {maximum_}')

# 3й вариант решения
# maxx = -1
# while (num:=int(input('--> '))) != 0:  #МОРЖОВЫЙ ОПЕРАТОР := для присвоения значения
#     if num > maxx:
#         maxx = num
# print(maxx)