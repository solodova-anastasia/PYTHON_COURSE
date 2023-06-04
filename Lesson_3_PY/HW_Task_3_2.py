# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

N = abs(int(input('Введите количество элементов массива: ')))
Ai = input("Введите целые числа через пробел: ").split()
A = list(map(int, Ai)) #создание нового списка из введенных пользователем чисел для последующего перебора
if len(A) != N or N <= 0:
    print('Введенные элементы не соответствуют заявленному количеству')
else:
        X = int(input('Введите число X, чтобы найти самый близкий по величине к нему элемент: '))
        min = abs(X - A[0])
        index = 0
        for i in range(1, N):
            difference = abs(X - A[i])  #разница между числом X и каждым из элементов
            if difference < min:
                min = difference
                index = i
print(f'Число {A[index]} в массиве наиболее близко по величине к числу {X}')