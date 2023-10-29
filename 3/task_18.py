# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i
# . Последняя строка
# содержит число X

from random import randint

n = int(input("Введите количество элементов массива: "))
m = int(input("Введите число: "))

k = 5
list_ = []
for i in range(n):
    list_.append(randint(-k,k))
print(list_)

x = list_[0]
result = abs(list_[0] - m)
for i in list_:
    if abs(i - m) < result:
        result = abs(i - m)
        print(result)
        x = i

print('Первое самое близкое число к ', m, ' = ', x)