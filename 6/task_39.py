# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
import random


#Функция ввода массива
def input_array(number):
    out_list = []
    for i in range(number):
        out_list.append(int(input('Введите элемент массива: ')))
    return out_list

#Удаление элементов
def del_function(in_list_1, in_list_2):
    for i in in_list_2:
        if i in in_list_1:
            in_list_1.remove(i)

def del_function1(in_list_1, in_list_2):
    out_list  = []
    for i in in_list_1:
        if i not in in_list_2:
            out_list.append(i)
    return out_list

N = int(input('Введите количество элементов первого массива: '))
array_1 = input_array(N)
M = int(input('Введите количесво элементов второго массива :'))
array_2 = input_array(M)
print(*[i for i in array_1 if i in array_1])
print(*del_function1(array_1, array_2))
del_function(array_1, array_2)

#Вывод полученного списка
print(*array_1)

# array_1 = [random.randint(-10, 10) for _ in range(N)]
# array_2 = [random.randint(-10, 10) for _ in range(M)]
# print(*array_1)
# print(*array_2)